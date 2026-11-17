#!/usr/bin/env python3
"""Validate normalized review evidence and emit a deterministic layout/totals plan. No network or writes."""
import argparse, datetime as dt, json, re

def col(n):
    out = ""
    while n >= 0:
        n, x = divmod(n, 26)
        out = chr(65 + x) + out
        n -= 1
    return out

def ratio(a, b, multiplier=1):
    return None if a is None or b in (None, 0) else a / b * multiplier

def build(model):
    client = model["client"].strip()
    if not client:
        raise ValueError("Client is required")
    sectors=sorted({l.get('sector') for l in model.get('leads',[]) if l.get('sector')})
    if len(sectors)>1:
        reviews=[];assigned=[]
        for sector in sectors:
            ids=model.get('sector_campaign_ids',{}).get(sector)
            fields=model.get('sector_project_columns',{}).get(sector)
            if ids is None or fields is None:
                raise ValueError('Separate sector tabs require verified campaign IDs and form columns: '+sector)
            part=dict(model,leads=[dict(l,source=l.get('capture_channel',l['source'])) for l in model['leads'] if l.get('sector')==sector],
                      campaigns=[c for c in model.get('campaigns',[]) if str(c['id']) in ids],project_columns=fields,
                      sector=sector,period_label=sector+' | '+(model.get('period_label') or dt.date.fromisoformat(model['period']['start']).strftime('%d %b')+'–'+dt.date.fromisoformat(model['period']['end']).strftime('%d %b %Y')))
            reviews.append(build(part));assigned.extend(ids)
        if len(assigned)!=len(set(assigned)) or set(assigned)!={str(c['id']) for c in model.get('campaigns',[])}:
            raise ValueError('Sector campaign allocation must cover campaigns exactly once')
        return {'workbook':reviews[0]['workbook'],'reviews':reviews,'separate_sector_tabs':True,
                'lead_count':sum(r['lead_count'] for r in reviews),'manual_notes':sum(len(l.get('manual_notes',[])) for l in model['leads'])}
    mode = model.get("run_mode", "review")
    if mode not in ("review", "comparison"):
        raise ValueError("Unknown review run mode")
    separate = mode == "comparison" or model.get("new_spreadsheet") is True
    protected_ids = {model.get(k) for k in ("source_spreadsheet_id", "reference_spreadsheet_id", "master_spreadsheet_id")} - {None, ""}
    target_id = model.get("destination_spreadsheet_id")
    if separate and (model.get("destination_mode") == "existing_workbook" or target_id in protected_ids):
        raise ValueError("A comparison/new-spreadsheet run requires a distinct output workbook")
    start, end = (dt.date.fromisoformat(model["period"][k]) for k in ("start", "end"))
    if end < start:
        raise ValueError("Reporting period ends before it starts")
    campaigns = model.get("campaigns", [])
    campaign_ids = [str(c["id"]) for c in campaigns]
    if len(campaign_ids) != len(set(campaign_ids)):
        raise ValueError("Duplicate campaign: would double-count totals")
    fields = ("spend", "forms", "impressions", "link_clicks")
    totals = {}
    for key in fields:
        vals = [c.get(key) for c in campaigns]
        if any(v is not None and (not isinstance(v, (int, float)) or isinstance(v, bool) or v < 0) for v in vals):
            raise ValueError("Invalid metric: " + key)
        totals[key] = None if any(v is None for v in vals) else sum(vals)
    totals.update(cpl=ratio(totals["spend"], totals["forms"]),
                  cpm=ratio(totals["spend"], totals["impressions"], 1000),
                  link_ctr=ratio(totals["link_clicks"], totals["impressions"]),
                  link_cpc=ratio(totals["spend"], totals["link_clicks"]))
    leads = model.get("leads", [])
    codes = [l["code"] for l in leads]
    if len(codes) != len(set(codes)):
        raise ValueError("Duplicate stable lead code")
    note_count = 1
    for lead in leads:
        notes = lead.get("manual_notes", [])
        for note in notes:
            if note.get("kind") != "manual" or not note.get("source_id") or note.get("text") != note.get("source_text"):
                raise ValueError("Manual note must match the identified human source verbatim: " + lead["code"])
            if not note["text"]:
                raise ValueError("An empty note is not an additional note")
        note_count = max(note_count, len(notes))
        ad = lead.get("ad")
        if ad:
            if ad.get("public_role") != "reader" or ad.get("attribution_evidence") not in ("meta_lead_id", "crm_ad_id", "source_row"):
                raise ValueError("Unverified ad access/attribution: " + lead["code"])
            if not ad.get("id") or not ad.get("name") or not ad.get("adset_name") or not re.match(r"https://drive.google.com/file/d/[^/]+/", ad.get("drive_url", "")):
                raise ValueError("Incomplete exact ad reference: " + lead["code"])
        fit = lead.get("marketing_fit", "verify_fit")
        if fit not in ("promising", "low_fit", "verify_fit"):
            raise ValueError("Unknown marketing prediction")
        if fit != "verify_fit" and not lead.get("assessment_basis"):
            raise ValueError("Marketing colour needs evidence or user review: " + lead["code"])
        if lead.get("spam_signals") and set(lead["spam_signals"]) <= {"name_language", "name_ethnicity", "unfamiliar_name"}:
            raise ValueError("A plausible name/language alone is not spam evidence")
    fields=model.get('project_columns') or [dict(key=k,label=h,width=w) for k,h,w in zip(
        ['budget','city','work','stage','size','start'],
        ['Budget planned','City','Work needed','Home stage','Home size (sq ft, as entered)','Preferred start'],
        [140,110,140,160,170,110])]
    if not fields or len({f['key'] for f in fields})!=len(fields) or any(not f.get('label') or not f.get('width') for f in fields):
        raise ValueError('Project columns require distinct source keys, exact labels and widths')
    lead_start, lead_end = 17, 17 + 3 + len(fields) + note_count
    action_start = lead_end + 7
    period = model.get("period_label") or (start.strftime("%d %b") + "–" + end.strftime("%d %b %Y"))
    existing = set(model.get("existing_tabs", []))
    tab, i = period, 2
    while tab in existing:
        tab = period + " (" + str(i) + ")"
        i += 1
    order = {"Facebook lead form": 0, "Instagram lead form": 1, "Instagram DM enquiries": 2}
    groups = {}
    for lead in leads:
        groups.setdefault(lead["source"], []).append(lead)
    placements, row = [], 5
    for source in sorted(groups, key=lambda s: (order.get(s.split(" | ")[0], 3), s)):
        placements.append({"row": row, "source_header": source, "count": len(groups[source])})
        row += 1
        group = sorted(groups[source], key=lambda l: (l.get("budget_min") is None, -(l.get("budget_min") or 0)))
        for lead in group:
            placements.append({"row": row, "code": lead["code"], "manual_note_count": len(lead.get("manual_notes", [])),
                               "marketing_fit": lead.get("marketing_fit", "verify_fit")})
            row += 1
    return {"workbook": client + (" | Marketing review comparison" if mode == "comparison" else " | Marketing reviews"),
            "destination_mode": "new_spreadsheet" if separate else "append_dated_tab", "preserve_source_workbooks": True,
            "new_tab": tab, "campaign_totals": totals,
            "lead_count": len(leads), "manual_note_columns": note_count,
            "project_columns":fields,
            "lead_headers":['Code + name / CRM']+[f['label'] for f in fields]+['Main blocker','Ad / creative']+['Note '+str(i+1) for i in range(note_count)],
            "lead_pixel_widths":[190]+[f['width'] for f in fields]+[100,260]+[190]*note_count,
            "blocks": {"ads": "A:J", "leads": col(lead_start) + ":" + col(lead_end - 1),
                       "actions": col(action_start) + ":" + col(action_start + 2)},
            "gaps": ["K:Q", col(lead_end) + ":" + col(action_start - 1)], "gap_columns": 7,
            "lead_rows": placements, "lead_footer_row": row, "colour_is_marketing_prediction": True}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model")
    args = parser.parse_args()
    with open(args.model, encoding="utf-8") as stream:
        print(json.dumps(build(json.load(stream)), ensure_ascii=False, indent=2))
