#!/usr/bin/env python3
"""Read-only audit of saved native Sheets snapshots against evidence and the retained layout."""
import argparse, json, math, re
from pathlib import Path

def value(c):
    return c.get('formattedValue', c.get('userEnteredValue', {}).get('stringValue', ''))

def number(c):
    return c.get('effectiveValue', {}).get('numberValue', c.get('userEnteredValue', {}).get('numberValue'))

def links(c):
    urls = [c.get('hyperlink'), c.get('userEnteredFormat', {}).get('textFormat', {}).get('link', {}).get('uri')]
    urls += [r.get('format', {}).get('link', {}).get('uri') for r in c.get('textFormatRuns', [])]
    urls += re.findall(r'https://[^"\s]+', c.get('userEnteredValue', {}).get('formulaValue', ''))
    return [u for u in urls if u]

def hexcolor(c):
    return '#' + ''.join(f'{round(c.get(k, 0)*255):02X}' for k in ('red', 'green', 'blue'))

def budget(text):
    s=text.lower().replace(',', '')
    if re.search('not (captured|decided)|unknown|undecided', s): return None
    nums=re.findall(r'\d+(?:\.\d+)?', s)
    if not nums: return None
    n=0 if 'below' in s else float(nums[0])
    first=re.search(r'\d+(?:\.\d+)?',s)
    unit=re.search(r'(?<![a-z])(cr(?:ore)?|lakhs?|l)(?![a-z])',s[first.end():])
    u=unit.group(1) if unit else ''
    return n*(1e7 if u.startswith('cr') else 1e5 if u.startswith('l') else 1)

def audit(snapshot, evidence, access):
    layout=json.loads((Path(__file__).parent.parent/'references/layout.json').read_text())
    sheets=snapshot['sheets']; s=next((x for x in sheets if x['properties']['sheetId']==evidence.get('sheet_id')),sheets[0]); g=s['data'][0]; rows=g.get('rowData', [])
    def at(r,c): return rows[r].get('values', [])[c] if r<len(rows) and c<len(rows[r].get('values', [])) else {}
    def result(key, label, passed, detail=''):
        checks.append(dict(id=key, rule=label, status='pass' if passed else 'gap', detail=detail))
    checks=[]; note_cols=[i for i in range(17,len(rows[3].get('values', []))) if re.fullmatch(r'Note \d+',str(value(at(3,i))))]
    note_start=min(note_cols); lead_end=max(note_cols)+1; action_start=lead_end+7
    header=[str(value(at(3,c))) for c in range(lead_end)]
    blocker_col=header.index('Main blocker'); ad_col=header.index('Ad / creative')
    project_fields=evidence.get('project_columns') or [dict(key=k,width=w) for k,w in zip(['budget','city','work','stage','size','start'],[140,110,140,160,170,110])]
    lead_rows=[r for r in range(4,len(rows)) if re.match(r'^[A-Z]+-?\d+ \| ', str(value(at(r,17))))]
    bycode={str(value(at(r,17))).split(' | ',1)[0]:r for r in lead_rows}
    allcells=[c for row in rows for c in row.get('values', [])]
    result('one_tab','Expected dated sector tabs only',sorted(x['properties']['title'] for x in sheets)==sorted(evidence.get('expected_tabs',[evidence['period_label']])) and s['properties']['title']==evidence['period_label'])
    result('destination','Destination distinct from protected sources',snapshot['spreadsheetId'] not in evidence.get('protected_source_ids', []))
    components=[str(value(at(2,c))) for c in (0,17,action_start)]
    result('three_components','Exactly the approved three side-by-side components',components==['1. Ads performance','2. Lead evidence by capture source','3. Media-buyer checks and next actions'])
    gaps=[(10,17),(lead_end,action_start)]
    result('gaps','Seven truly empty columns between components',all(b-a==7 and not any(at(r,c).get('userEnteredValue') for r in range(len(rows)) for c in range(a,b)) for a,b in gaps))
    widths=[x.get('pixelSize') for x in g.get('columnMetadata', [])]
    expected=layout['blocks']['ads']['pixel_widths']+[24]*7+[190]+[f['width'] for f in project_fields]+[100,260]+[190]*len(note_cols)+[24]*7+layout['blocks']['actions']['pixel_widths']
    result('widths','Independent canonical column widths',widths==expected)
    result('merges','No merges cross component gaps',not any(m['startColumnIndex']<b and m['endColumnIndex']>a for m in s.get('merges',[]) for a,b in gaps))
    result('grid','Native grid lines remain visible',not s['properties']['gridProperties'].get('hideGridlines',False))
    result('freeze','Title row stays frozen',s['properties']['gridProperties'].get('frozenRowCount')==1)
    result('borders','Lead data keeps table borders',all(all(at(r,c).get('userEnteredFormat',{}).get('borders',{}).get(side,{}).get('style')=='SOLID' for side in ['top','bottom','left','right']) for r in lead_rows for c in range(17,lead_end)))
    result('font','Arial body text remains 11 pt',all(at(r,18).get('userEnteredFormat',{}).get('textFormat',{}).get('fontFamily')=='Arial' and at(r,18)['userEnteredFormat']['textFormat'].get('fontSize')==11 for r in lead_rows))
    role_checks=[]
    for role,r,c in [('title',0,0),('subtitle',1,0),('ads_section',2,0),('leads_section',2,17),('actions_section',2,action_start),('column_header',3,17)]:
        actual=at(r,c).get('userEnteredFormat',{}); f=actual.get('textFormat',{}); exp=layout['text_roles'][role]
        role_checks.append(f.get('fontSize')==exp['font_size'] and bool(f.get('bold'))==exp['bold'])
        if 'fill' in exp:role_checks.append(hexcolor(actual.get('backgroundColor',{}))==exp['fill'])
        if 'text' in exp:role_checks.append(hexcolor(f.get('foregroundColor',{}))==exp['text'])
    result('headings','approved reference heading sizes, weights and section fills',all(role_checks))
    result('blocker_style','approved reference compact bold Main blocker style',all(at(r,blocker_col).get('userEnteredFormat',{}).get('textFormat',{}).get('fontSize')==10 and at(r,blocker_col)['userEnteredFormat']['textFormat'].get('bold') and hexcolor(at(r,blocker_col)['userEnteredFormat']['textFormat'].get('foregroundColor',{}))==layout['text_roles']['blocker']['text'] for r in lead_rows if value(at(r,blocker_col))))
    result('padding','Compact approved reference cell padding',all(at(r,c).get('userEnteredFormat',{}).get('padding')==layout['text_roles']['padding_px'] for r in lead_rows for c in range(17,lead_end)))
    heights=[x.get('pixelSize') for x in g.get('rowMetadata',[])]
    compact=all(r<len(heights) and heights[r]==72 for r in lead_rows)
    checks.append(dict(id='compact',rule='Latest compact row policy',status='pass' if compact else 'reference_difference' if evidence.get('reference') else 'gap',detail='Reference formatting is preserved; native auto-fit metadata can differ from rendered height.'))
    result('lead_count','Every selected lead retained',len(lead_rows)==evidence['lead_count'] and len(bycode)==len(lead_rows))
    result('crm','Stable code + name links to the correct CRM location',all(any('/location/'+evidence['crm_location_id']+'/contacts/detail/' in u for u in links(at(r,17))) for r in lead_rows))
    if evidence.get('leads'):
        result('crm_identity','Each code/name retains its own exact source contact link',all(l['crm_url'] in links(at(bycode[l['code']],17)) for l in evidence['leads']))
    headers=[str(value(at(3,c))) for c in range(40)]
    result('all_metric_labels','All ad metric headers match their actual metric and unit',headers[:10]==layout['blocks']['ads']['columns'])
    result('all_lead_labels','Lead headers match the verified client project mapping',headers[17:lead_end]==evidence['lead_headers'])
    result('all_action_labels','Actions keep the three approved column labels',headers[action_start:action_start+3]==layout['blocks']['actions']['columns'])
    result('no_contact_columns','Project answers only; no phone/email/WhatsApp columns',not any(re.search(r'phone|email|whatsapp',h,re.I) for h in headers))
    result('no_sales_columns','No sales owner decision, sales stage or precise rank columns',not any(re.search(r'sales owner|decision|sales stage|rank',h,re.I) for h in headers))
    result('no_source_column','CRM/ad links replace a separate Source column',not any(h.strip().lower()=='source' for h in headers))
    result('one_blocker','At most one concise supported blocker per lead',all(str(value(at(r,blocker_col))) in ['','Budget','Vacancy','Location','Scope','Missing details','Possible spam / verify'] for r in lead_rows))
    groups=[]; current=[]; labels=[]
    for r in range(4,len(rows)):
        t=str(value(at(r,17)))
        if re.match(r'^(Facebook lead form|Instagram lead form|Instagram DM enquiries|Other)',t) and re.search(r'\(\d+\)$',t):
            if current:groups.append(current)
            current=[];labels.append((t,r))
        elif r in lead_rows:current.append(r)
    if current:groups.append(current)
    result('source_counts','Capture-source headers count their actual records',len(groups)==len(labels) and all(len(group)==int(re.search(r'\((\d+)\)$',label).group(1)) for group,(label,_) in zip(groups,labels)))
    sorted_ok=True
    for group in groups:
        nums=[budget(str(value(at(r,18)))) for r in group]
        sorted_ok &= nums==sorted(nums,key=lambda n:(n is None,-(n or 0)))
    result('budget_order','Budget descending within comparable source groups; unknown last',sorted_ok)
    result('note_columns','One default note column plus only real extra notes',len(note_cols)==max(1,max((sum(bool(value(at(r,c))) for c in note_cols) for r in lead_rows),default=0)))
    note_count=sum(bool(value(at(r,c))) for r in lead_rows for c in note_cols)
    result('note_count','All actual human notes retained',note_count==evidence['manual_note_count'])
    result('no_note_placeholders','Missing human notes stay empty',not any('No GHL notes found' in str(value(at(r,c))) for r in lead_rows for c in note_cols))
    model_leads={l['code']:l for l in evidence.get('leads',[])}
    if model_leads:
        exact=all(str(value(at(bycode[code],note_start+i)))==n['source_text'] for code,l in model_leads.items() for i,n in enumerate(l.get('manual_notes',[])))
        raw=all([str(value(at(bycode[code],18+i))) for i,f in enumerate(project_fields)]==[l[f['key']] for f in project_fields] for code,l in model_leads.items())
        result('verbatim_notes','Manual wording and line breaks match source records',exact)
        result('raw_project_answers','All mapped project answers match source evidence',raw)
        result('platform_evidence','Capture groups match original submission platforms',all(any(l['capture_channel'] in label and bycode[code] in group for (label,_),group in zip(labels,groups)) for code,l in model_leads.items()))
    else: result('empty_notes','Reference manual-note cells remain empty',note_count==0)
    boiler=re.compile(r'^Source: .*Values preserved|^Marketing-team prediction:|^Manual GHL note ID:|^Underlying link clicks:')
    result('annotations','No repeated generated cell-note boilerplate',not any(boiler.match(c.get('note','')) for c in allcells))
    palette=set(layout['palette'].values()); coloured=[]
    for r in lead_rows:
        colors={hexcolor(at(r,c).get('effectiveFormat',{}).get('backgroundColor',{})) for c in range(17,lead_end)}
        coloured.append(len(colors)==1 and next(iter(colors)) in palette)
    result('colours','Whole-row light sage/rose/cream predictions',all(coloured))
    result('colour_legend','Legend states marketing prediction, not sales confirmation',any('marketing-team predictions, not confirmed sales qualification' in str(value(c)) for c in allcells))
    archive={x['drive_id']:x for x in evidence['assets']}
    paid=[]; unresolved=[]; matched=[]; line_ok=[]; exact_sets=[]
    for r in lead_rows:
        c=at(r,ad_col);t=str(value(c));url=next((u for u in links(c) if 'drive.google.com/file/d/' in u),None)
        if not url:unresolved.append(t);continue
        paid.append(r);fid=url.split('/d/')[1].split('/')[0];a=archive.get(fid)
        matched.append(a is not None and t.split('\n')[0]==a['name'])
        expected_set=evidence.get('adset_names_by_ad_id',{}).get(a['ad_id']) if a else None
        exact_sets.append(expected_set is not None and t.split('\nAd set: ',1)[-1]==expected_set)
        runs=c.get('textFormatRuns',[])
        line_ok.append('\nAd set: ' in t and bool(runs) and bool(runs[0].get('format',{}).get('link')) and any(x.get('startIndex',0)>=len(t.split('\n')[0]) and not x.get('format',{}).get('link') for x in runs[1:]))
    result('ad_names','Full exact ad names link to their exact cached Drive reference',all(matched) and len(paid)==evidence['paid_lead_count'])
    result('adset_line','Ad-set name is a plain second line below the linked ad name',all(line_ok))
    result('adset_identity','Lead ad-set labels match originating submission evidence',all(exact_sets))
    result('unattributed','Unattributed enquiries are explicit; no guessed ad',all(t=='Unattributed DM' for t in unresolved))
    result('library_header','Ad / creative header opens the complete Drive library/index',any('drive.google.com' in u for u in links(at(3,ad_col))))
    campaign_rows=[]
    for r in range(4,len(rows)):
        if str(value(at(r,0)))=='Total':total_row=r;break
        if number(at(r,2)) is not None:campaign_rows.append(r)
    else:total_row=None
    campaigns=evidence['campaigns'];byname={c['name']:c for c in campaigns}
    result('campaign_names','Exact campaign names and account-specific Meta links',len(campaign_rows)==len(campaigns) and all(value(at(r,0)) in byname and any('act='+evidence['account_id'] in u and byname[value(at(r,0))]['id'] in u for u in links(at(r,0))) for r in campaign_rows))
    result('adset_links','Included ad-set names are linked, not campaign shorthand',all(links(at(r,1)) and value(at(r,1)) for r in campaign_rows))
    expected_sets=evidence.get('campaign_adset_names',{})
    result('campaign_adsets','Campaign ad-set names match source evidence',all(str(value(at(r,1)))=='\n\n'.join(expected_sets.get(byname[value(at(r,0))]['id'],[])) for r in campaign_rows))
    result('metric_headers','Link CTR and Link CPC are explicitly distinguished',str(value(at(3,7)))=='Link CTR' and str(value(at(3,8))).startswith('Link CPC'))
    result('metric_formats','CTR renders as percent and costs keep decimals',all(at(r,7).get('userEnteredFormat',{}).get('numberFormat',{}).get('type')=='PERCENT' and '0.00' in at(r,2).get('userEnteredFormat',{}).get('numberFormat',{}).get('pattern','') for r in campaign_rows))
    sums={k:sum(c[k] for c in campaigns) for k in ['spend','forms','impressions','link_clicks']}
    expected_total=[sums['spend'],sums['forms'],sums['spend']/sums['forms'],sums['impressions'],sums['spend']/sums['impressions']*1000,sums['link_clicks']/sums['impressions'],sums['spend']/sums['link_clicks']]
    result('weighted_totals','Totals use summed spend and raw denominators',total_row is not None and all(number(at(total_row,i+2)) is not None and abs(number(at(total_row,i+2))-n)<(0.000051 if i==5 else .0051) for i,n in enumerate(expected_total)))
    result('campaign_metrics','Campaign spend/form/impression counts match evidence',all(abs(number(at(r,2))-byname[value(at(r,0))]['spend'])<.0051 and number(at(r,3))==byname[value(at(r,0))]['forms'] and number(at(r,5))==byname[value(at(r,0))]['impressions'] for r in campaign_rows))
    useful_findings=all('Paid forms are the full-period Meta form result, not this selected cohort.' not in str(value(at(r,9))) for r in campaign_rows)
    operational_actions=not any(re.search(r'notes preserved|placeholders excluded|copied verbatim|rows resized',str(value(at(r,c))),re.I) for r in range(4,7) for c in range(action_start,action_start+3))
    result('quality_findings','Campaign findings/actions contain operating evidence, not repeated audit boilerplate',useful_findings and operational_actions)
    result('timezone','Native workbook timezone matches the reporting timezone',snapshot['properties'].get('timeZone') in evidence['timezone_aliases'],snapshot['properties'].get('timeZone'))
    result('currency','Money columns identify account currency',all('₹' in str(value(at(3,c))) for c in [2,4,6,8]))
    result('period_cutoff','Reporting period and evidence cutoff are stated',bool(value(at(1,0))) and evidence['period_marker'] in str(value(at(1,0))))
    client_access=[x for x in access if x['ref']['client']==evidence['client']]
    public=[x for x in client_access if x['ref'].get('kind')!='report']
    result('viewer_assets','Every ad/library/index is public Viewer only',all(any(p['type']=='anyone' and p['role']=='reader' for p in x['result'].get('permissions',[])) and not any(p['type']=='anyone' and p['role']!='reader' for p in x['result'].get('permissions',[])) for x in public))
    reports=[x for x in client_access if x['ref'].get('kind')=='report']
    result('restricted_report','Spreadsheet remains restricted to invited people',bool(reports) and all(not any(p['type']=='anyone' for p in x['result'].get('permissions',[])) for x in reports))
    result('media_scope','No business-followup or supplier sections added',not any(re.search(r'^Business follow-ups|supplier enquiries',str(value(c)),re.I) for c in allcells))
    result('no_extra_components','No extra charts, dashboards or sections',not s.get('charts') and sum(bool(re.match(r'^[123]\. ',str(value(c)))) for c in allcells)==3)
    return dict(client=evidence['client'],lead_count=len(lead_rows),manual_note_count=note_count,checks=checks,
                gaps=[c['id'] for c in checks if c['status']=='gap'])

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('snapshot');p.add_argument('evidence');p.add_argument('access');a=p.parse_args()
    read=lambda x:json.loads(Path(x).read_text())
    print(json.dumps(audit(read(a.snapshot),read(a.evidence),read(a.access)),ensure_ascii=False,indent=2))
