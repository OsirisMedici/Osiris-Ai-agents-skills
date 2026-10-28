---
name: meta-ads-manager
description: Inspect existing Meta campaigns and creatives, propose professional attribution names, and apply approved campaign, ad set, or ad renames with saved-state verification. Use for naming audits and bulk renaming; this does not cover campaign launches or performance optimization.
---

# Meta Ads Manager

Produce a reliable mapping from each existing Meta object to its approved name, then apply only the authorized changes. Names must be useful to media buyers, CRM operators, clients, and leadership reading attribution reports.

## Establish the exact scope

- Identify the client, browser/profile, ad account, campaign, entity levels, expected counts, and whether the user wants proposals, draft changes, or publication. Retrieve available context before asking for information already supplied.
- Honor the user's named profile. Verify the live profile and account ID before the first mutation and again after any window, tab, profile, or account change. A URL alone does not prove the right signed-in session.
- Prefer a capable connected tool in the authorized account; otherwise use the documented browser/computer tool. A connector in another profile is not a substitute for the requested session.
- A request to rename ad sets and ads does not include the campaign, creative, audience, budget, destination, tracking parameters, or delivery toggles.

## Inspect and propose

1. Inventory the scoped objects and parent relationships. Record actual IDs where exposed. Preserve original ad numbers, including nonsequential display order. If an ID cannot be read, use an unambiguous parent/name/creative mapping and resolve collisions before writing.
2. Open each actual creative needed to determine its hook. Verify the selected object and parent, then wait for its media to render. A changed heading, thumbnail, or loading skeleton does not prove that the new image is loaded. Inspect placement-specific overrides when present; do not assume one preview represents every placement.
3. Treat matching hooks across visual families as a hypothesis until inspected or explicitly established by the user. Record repeated hooks, missing hooks, and image/copy/name disagreements. Never reconstruct the mapping from row position or ad number alone.
4. Use the smallest useful naming scheme from [naming-and-approval.md](references/naming-and-approval.md). Present exact current-to-proposed names grouped by parent, with all requested objects covered. Keep facts, intended labels, and unresolved mismatches distinct.
5. When the user asks to approve names first, do not edit name fields before approval. Approval of an exact list authorizes that list; do not ask again merely because execution starts later. If a mismatch affects a proposed label, resolve it or obtain an explicit exception. Do not silently replace a creative or override approved labels.

For multi-item work, use a task-local mapping. [assets/rename-map.csv](assets/rename-map.csv) is an optional template. The offline validator checks mapping integrity, not Meta state or user authorization:

```bash
python3 scripts/validate_rename_map.py /path/to/rename-map.csv --expect-adsets 4 --expect-ads 20
# After approval, require a recorded approval reference on every row:
python3 scripts/validate_rename_map.py /path/to/rename-map.csv --expect-adsets 4 --expect-ads 20 --require-approval
```

## Apply and verify

- Before editing, capture the relevant starting state and the approved mapping in the current task's evidence location. Do not put client data or screenshots in this skill repository.
- Read [browser-operations.md](references/browser-operations.md) before native browser execution or when adapting the workflow to a different UI.
- Edit one identified object at a time. Use a name-only control where available. Verify the old value before replacing it, the exact new value before saving, and the resulting row or reopened field after saving. Read the current UI to select the actual save action; do not hardcode labels, coordinates, or element indices from another session.
- Track each object as proposed, approved, entered, save submitted, verified saved, or blocked. A click, successful tool call, or closed popup is not proof of persistence. After a timeout, inspect the actual state before retrying; a save may already have happened.
- Verify the complete approved mapping, counts, ad numbers, and parent assignments from saved UI/tool readbacks. Revisit or refresh a relevant view to check persistence. Stop when the required checks pass; do not inspect unrelated campaign settings.
- Saving drafts and publishing are separate outcomes. Do not click a publish control to finish a rename unless publication is explicitly within scope. A review/publish count can include preexisting creative changes; inspect its contents before any authorized publication.

## Report completion

State the verified count at each entity level, where the changes were saved, whether anything was published, and any unresolved mismatch or partial result. Include relevant before/after screenshots when the environment supports them. If capture fails, report the precise gap and the readback evidence used instead. Never describe entered, submitted, or queued changes as verified saved.

For partial completion, list the verified objects and remaining objects so another run can resume without renaming the wrong ad or repeating a save. Do not claim a cross-client workflow is live-tested merely because this skill or its offline validator passes.
