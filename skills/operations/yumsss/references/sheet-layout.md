# Osiris Food Diary layout

Use this guide to locate data, then inspect the live Sheet. Locations below were verified on 15 November 2026 and can move when rows are inserted. Current Sheet values and metadata take precedence over this guide or old exports.

Resolve the private spreadsheet and connected account before using this layout. Verify current tab names and IDs live. A permission failure is a reason to verify the selected identity, not to change sharing or duplicate the diary.

## Food diary

Header row 6; entries begin at row 7. The preformatted entry region was A7:K1000 in the native `FoodRecords` table. Inspect current bounds before extending it.

| Column | Meaning | Editing rule |
| --- | --- | --- |
| A | Date eaten | Native date, Asia/Kolkata; observed display DD/MM/YYYY |
| B | Meal | Existing dropdown option; `Not specified` is available |
| C | Food / drink | Include meaningful brand or variant |
| D | Qty | Amount consumed, in the unit in E |
| E | Unit | Piece, banana, ml, bowl, etc.; assumed sizes go in Details |
| F | kcal / unit | Numeric label value or qualified estimate |
| G | Protein / unit, g | Same unit basis as F |
| H | Calories, kcal | Preserve formula |
| I | Protein, g | Preserve formula |
| J | Entry ID | Retain IDs; find the next unused `FOOD-` ID live, preserving zero-padding |
| K | Notes | Short readable note; full provenance in Details |

H and I already contain formulas returning blank when quantity or nutrition is missing. For example, H22 was `=IF(C22="","",IF(AND(ISNUMBER(D22),ISNUMBER(F22)),D22*F22,""))`. Preserve formulas and relative references instead of replacing them with computed numbers.

Safe input rectangles are A:G and J:K. Preserve blue inputs, peach nutrition and green calculated columns. Copy appropriate structure when new rows need it, excluding another food's values or source IDs.

### Visible summary and weight

- D1:G5 holds the review-date summary. F1 is the review date in a merged F:G cell. Preserve summary formulas and target labels.
- H1:I2 shows current weight: H1 `Weight`, I1 its readable value with kg, H2 `As of`, I2 the date. Save the dated numeric measurement in the weigh-in log as well.
- Keep summaries near the top, numbers left aligned and notes readable. Longer assumptions/source URLs belong in Details.

## Daily totals

`DayRecords` has headers in row 4: Date, Day coverage, Calories, Protein, Items logged, With calories, With protein, Nutrition coverage. Formulas summarize Food diary by date and treat missing nutrition as unknown.

Find the date first. For a missing date, extend the summary with a neighboring row's formulas and validation, then replace date/status inputs. Insert space before the lower profile block when necessary. Preserve the table and lower profile/research material.

Locate the historical profile and weigh-in log by their visible headers. Preserve historical baselines and target formulas. Record a new measurement in the dated weigh-in log without replacing earlier measurements. Sheet row numbers can move.

## Details

Header row 4: Entry ID, Food / drink, Estimate basis, Original kcal low, Original kcal high, Nutrition reference, Additional reference, Original report, Report ID.

Match records by Entry ID. Preserve original reports and report IDs, appending latest clarifications/provenance where needed. When no initial estimate existed, populate its basis/source and optional rough portion range. Preserve previous estimate history when correcting it; current food inputs and a clearly dated detail note should agree.

For a new report, assign the next unused `REPORT-` ID from live Details, preserving its zero-padding. Foods from the same report share that report ID. Keep the user's original wording in Original report; put dated corrections in the provenance instead of replacing the initial report.

Source entries are followed by editing notes and review-coverage notes. Locate that boundary before adding records. Insert space ahead of the notes rather than overwriting them. Record unresolved evidence gaps here, not as fictional food entries.

## Browser fallback

When the connector cannot access this file, use the authenticated in-app Browser and verify the account shown in the Sheet. Tab IDs/CUA handles are session-specific; rebind after interruptions. Read the current browser-control documentation.

The demonstrated UI route selected a bounded A1 range through `#t-name-box`, pressed Enter and copied cells through the supported browser clipboard API. Paste tab-separated rows only into verified input rectangles, then read them back. Pasting A:G and J:K separately preserves H:I formulas. Use native row insertion to make room in Details or Daily totals.

Selections intersecting merged profile/summary cells can expand beyond the requested rectangle. Check the selected range before pasting. After a timeout, inspect actual state and saved cells before retrying a mutation.

The October `WORKFLOW.md` under the old Karen outputs path was unavailable in November. This reference supplies the reusable layout; the live Sheet remains authoritative.
