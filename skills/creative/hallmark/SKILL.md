---
name: hallmark
description: Design new websites and pages with a deliberate visual direction, real materials and browser review. Use on existing designs when the user requests a Hallmark audit or redesign.
---

# Hallmark for Scale

Adapted from Nutlope/Hallmark. The pinned source and MIT notice are recorded in `PROVENANCE.json` and `LICENSE`. Use this entry point with the retained upstream references and scripts.

## Apply the project contract

Inspect the product, brand, content, assets and existing implementation before choosing a visual direction. Project instructions and the current user's outcome take precedence over upstream style gates. A brand's typography, colors, layout and existing interactions remain in place unless the requested work changes them. Upstream aesthetic bans and section/word counts are critique prompts, not universal product requirements.

Reuse the audience, task, material and tone already supplied or discoverable. Ask only about decisions that would materially change the result. A small change does not require a new theme, a questionnaire or a whole-page redesign.

## Design the requested experience

For a new page, select relevant guidance from `references/anatomy.md`, `references/layout.md`, `references/craft.md` and `references/imagery.md`. Choose the page's job and useful content before its composition. Use one coherent direction and real, permitted materials. A custom direction may use `references/direction.md`; an upstream theme is optional, and only its selected reference needs loading.

Build one representative section first, then compare it with the brief and reference decisions. Make the product's behavior, hierarchy and responsive layout work before adding polish. Treat tokens, legibility, focus, meaningful feedback and reduced motion as implementation concerns, with checks in the actual output.

For an explicit audit or redesign, read `references/redesign.md` for preservation questions. Report observed findings for an audit; change only the requested parts for a redesign. Preserve content, routes and working integrations unless the brief says otherwise.

## Supported helpers and verification

Use Bun for compatible JS helpers, such as `bun <skill-dir>/scripts/theme.mjs list` or a static `sloplint.mjs` check. Inspect a helper's arguments before running it. The theme/scaffold tools are optional and write only within the requested project.

Use the supported in-app Browser for rendered inspection and screenshots. The retained `capture`, render, browser-launch and install helpers are upstream resources, not permission to control another browser. Run static lint without `--render` or `--url`; assess its style findings against the actual brief. Do not report a render gate as passed from static lint.

Review the real page at relevant desktop and phone sizes, with keyboard/focus, content states and reduced motion. Use upstream gate and review references as useful questions, not authority to ignore user decisions or expand scope. Report an unavailable visual check as unverified. Use independent review only when the task warrants it and delegation is permitted.

Record the chosen direction, material sources, tested revision and actual check results. Follow the user's publishing and completion instructions. Paid comps, API setup, subscriptions and promotional copy are not part of this skill's default workflow.
