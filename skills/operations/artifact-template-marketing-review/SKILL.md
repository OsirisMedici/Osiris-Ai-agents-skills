---
name: artifact-template-marketing-review
description: Create the approved marketing review for a named client and reporting period, with a dated tab in the client's marketing workbook or a separate spreadsheet for a requested test/comparison, exact Meta and CRM evidence, verbatim human notes, and viewer-accessible Drive ad references.
---

# Marketing review

Use the retained native Google Sheets template and its three independent column blocks. The user supplies the client and period. Preserve the approved report, without adding dashboards, sales tasks, rankings, or extra components.

Read [workflow](references/workflow.md), [layout contract](references/layout.json) and the [acceptance checklist](references/acceptance.md). Resolve the client registry, form mappings and user-selected native master from the authorized private workspace. They are external dependencies, not bundled examples. Read [Drive archive](references/drive-archive.md) when resolving assets or permissions.

## Run

1. Resolve the client and inclusive reporting dates. Ask only for missing dates, ambiguous client identity, or unavoidable authentication. Discover account and file facts through connected tools before asking.
2. Verify the actual Meta account, CRM location, workbook and client library. Read the selected period's Meta data and lead evidence. Preserve the data cutoff separately from the ads reporting window.
3. Resolve source and destination separately. For a test, comparison or explicit new-spreadsheet request, create a separate native workbook and verify its ID differs from the source, approved reference reference and master before edits. Use a dated tab per project sector when forms differ, such as Residential and Hospitality; each tab contains all three components. Preserve source workbooks. For an ordinary review, append the dated sector tabs to the verified client marketing workbook. A legacy lead/outcomes workbook is a data source unless explicitly selected as the destination. Copy the complete native master for a new workbook.
4. Populate exactly the three approved components on each tab. Include only that sector's campaigns and recalculate its weighted totals. Use its actual project-form questions, with separate clear headers and no empty slots for questions the form never asked. Campaign and ad-set names are exact. Lead name and ad name are clickable. The exact source ad-set name appears on a new plain-text line below each ad link. Human notes are verbatim; missing notes stay empty. Follow the light annotation policy in workflow.md. Keep one concise scope/metric footer and operational actions; retain build bookkeeping privately. Sage is a marketing prediction. Apply the compact fixed-height row policy; retain complete text and all grid lines.
5. Reuse matching Drive assets or archive new versions. When explicitly authorized, the ad library and linked children use **Anyone with the link: Viewer**. Otherwise prepare the exact sharing change for approval before applying it. The workbook remains restricted to invited people. Verify child-file access before declaring links usable.
6. Run `scripts/review_plan.py` on the normalized model, then audit the saved native output with `scripts/audit_saved_review.py` and the acceptance checklist. Compare saved native cells with the model, inspect all three components in the in-app Browser, and verify compact row heights and preserved source files. For comparisons, read the saved approved reference/reference and test output, classify expected client-data differences separately from missing SOP rules, and report concrete gaps without silently restyling the reference.
7. Update the non-secret client and asset indexes only with verified identifiers. Return the dated review link and material limitations.

The selected native master is read-only during report runs. This public package contains the layout contract and validators, but no client workbook, preview or native template asset. Verify the privately configured master before writing; do not invent a replacement template or target. Keep CRM exports and customer identifiers outside the skill and outside the public ad library. Invoking this workflow authorizes the requested report creation. File uploads and public link sharing require the corresponding explicit or standing user authorization. It does not authorize campaign changes, CRM mutations or outbound messages.

Example: `$artifact-template-marketing-review Example Client, 1–15 November 2026`.
