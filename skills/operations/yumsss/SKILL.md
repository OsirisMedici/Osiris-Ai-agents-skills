---
name: yumsss
description: Log Osiris's reported meals, drinks, portions and weigh-ins from chat in his existing Osiris Food Diary Google Sheet, including nutrition estimates and corrections. Use for food-diary updates; work activity belongs in Life Log.
---

# Yumsss

Turn ordinary chat reports into saved entries in Osiris's existing food diary. He supplies what he ate or his current weight; handle the spreadsheet entry and calculations for him.

Resolve the user's existing Food Diary spreadsheet and account from authorized private configuration or a user-supplied link. Verify ownership and access before writing. This public package contains no diary ID, account mapping, nutrition targets or personal records.

## Manual logging

When invoked without a new report, invite Osiris to describe what he ate/drank, its portions, or his weight in normal chat, then wait for that input. Use earlier saved reports as context rather than replaying them as new entries.

1. Extract the food or drink, amount actually consumed, eating date, and any weight report or correction. Use the client's current date and Asia/Kolkata for relative dates. Resolve each item separately when a message spans days. Ask one bundled question only for gaps that materially change the record; save independent confirmed items meanwhile.
2. Read [the sheet layout](references/sheet-layout.md) and the available Google Sheets editing skill. Read live headers, relevant existing entries, formulas, source details and affected daily summaries before writing. Use a connector with access to this private file; use the in-app Browser when needed. Keep this native Sheet as the working record.
3. Match corrections to existing entries by date, food, portion and source. Retain their IDs. For genuinely new items, assign the next unused `FOOD-` ID from the live sheet. Save the original report and date/portion assumptions in Details. A report such as "also one full leg" adds the leg to the existing meal rather than duplicating the previously logged wings.
4. Fill nutrition per unit using the rules below. Write inputs, preserving calculated columns, native tables, dropdowns and human edits. Extend the daily summary and source-detail sections only as necessary, preserving their lower notes and profile blocks.
5. Re-read the written entries and affected daily totals. Confirm persistence, valid meal dropdowns and intact calculations, then inspect the changed area for readability. Reply briefly with the saved date/items or correction, the Sheet link and any material assumptions or unresolved portions. Report "saved" only after readback confirms it.

Invoking this skill to log reported intake authorizes updating this diary. Apply those updates directly without another approval round. If access is blocked, retain a factual unsaved draft and identify the access problem instead of claiming a successful write.

## Intake and estimates

- Record what Osiris actually consumed. Order size, visible food, discarded leftovers, other people's meals and planned future food are distinct evidence. Three wings eaten from a four-piece order means three logged. "No separate dips" excludes those dips while sauce already coating the ordered food remains part of its recipe.
- Reuse an existing nutrition reference when the food, brand/variant and unit match. Otherwise check appropriate manufacturer or reliable food-composition references. Preserve a source link and calculation basis in Details. Separate verified labels from generic recipe proxies.
- Ordinary size assumptions, such as a medium banana, can support a clearly labeled estimate. Keep reported counts distinct from assumed weights. For unweighed bowls or uncertain recipes, state the cup/weight and oil assumptions; use a reasonable provisional estimate when supported. Unknown consumed quantity remains unknown unless Osiris accepts an assumed portion. Log the known item and ask only the material follow-up.
- Keep calories and protein per unit consistent with Qty and Unit. The green columns calculate totals. Describe estimates as estimates; rough portion/recipe ranges are not statistical confidence intervals. Revise an estimate when a later clarification identifies a different variant or portion.
- Keep days Open until Osiris explicitly confirms all intake for the day is captured. Complete nutrition for logged items does not establish a complete day. Missing days or meals represent unknown intake, not fasting or zero calories.

## Weight

Record a new weight with its report/measurement date in the existing weigh-in log and refresh the visible current-weight header. Correct a same-date measurement when the user is correcting it; preserve measurements from other dates.

Read the currently approved targets and historical baseline from the private diary. A weigh-in by itself does not authorize changing those targets, the historical baseline, or adding a calorie deficit.

## Optional evidence review

Default to the user's chat report and supplied attachments. Review Photos, order history, SMS or WhatsApp only when requested, for the requested dates. Preserve unsent messages and keep sending outside this logging workflow. Do not promise unattended WhatsApp monitoring.

If phone navigation is blocked, report the specific blocker and continue with usable evidence. Avoid repeated unlock/restart cycles for the same failed control action. When Osiris says to use what is already available, finish from confirmed evidence and retain remaining gaps as unknown.

## Examples

- `$yumsss today I had 2 bananas and a full 250 ml regular Red Bull.`
- `$yumsss yesterday I ate half a bowl of dal with 2 bowls of rice.`
- `$yumsss correction: only 3 wings, plus 1 full leg. No separate dips.`
- `$yumsss my current weight is <reported weight>.`

Keep this workflow for food, drink and weight. Use the separate Life Log skill for actual work/activity and Life Compass for future planning.
