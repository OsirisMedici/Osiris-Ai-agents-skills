# Skill publication, 17 November 2026

Published 16 new packages in `da286f355f6185047d2794e6bc2b41938fc10abf`. The public library now contains 65 skills. The owner requested publication through `osiris-skills-sync`; its publishing helper created and pushed the reviewed batch directly to main.

## Packages

| Package | Category | Source |
| --- | --- | --- |
| [80-20-next](../skills/tools/80-20-next/SKILL.md) | tools | Mac |
| [artifact-template-marketing-review](../skills/operations/artifact-template-marketing-review/SKILL.md) | operations | Mac |
| [canvas-visualize](../skills/creative/canvas-visualize/SKILL.md) | creative | VPS |
| [focused-task-chats](../skills/operations/focused-task-chats/SKILL.md) | operations | Mac |
| [hallmark](../skills/creative/hallmark/SKILL.md) | creative | Mac |
| [life-compass](../skills/operations/life-compass/SKILL.md) | operations | Mac |
| [meta-ads-insights](../skills/meta/meta-ads-insights/SKILL.md) | meta | Mac |
| [pick-ui-library](../skills/engineering/pick-ui-library/SKILL.md) | engineering | Mac |
| [recordly-to-youtube](../skills/youtube/recordly-to-youtube/SKILL.md) | youtube | Mac |
| [right-now](../skills/operations/right-now/SKILL.md) | operations | Mac |
| [scale-cinematic-web](../skills/creative/scale-cinematic-web/SKILL.md) | creative | Mac |
| [scale-design-toolkit](../skills/creative/scale-design-toolkit/SKILL.md) | creative | Mac |
| [stageshow](../skills/creative/stageshow/SKILL.md) | creative | Mac |
| [veronica](../skills/operations/veronica/SKILL.md) | operations | Mac |
| [watchlist](../skills/operations/watchlist/SKILL.md) | operations | Mac |
| [yumsss](../skills/operations/yumsss/SKILL.md) | operations | Mac |

## Packaging and privacy

Mac installed packages and resolved design-toolkit symlink targets were curated into separate publication copies. Meta Ads Insights came from its existing task source checkout; Canvas Visualize came from the installed VPS package. Live source packages and their configuration were preserved.

The marketing-review package retains its layout and validators, but client registries, ad indexes, native source workbook IDs and workbook/preview assets remain external private inputs. Users must resolve an authorized native master and client form mappings before running it. Public asset sharing requires the corresponding authorization.

Life Compass and Right Now resolve calendar/account identities from private configuration. Yumsss resolves its private diary and targets live. Watchlist resolves the existing private master. Recordly to YouTube verifies the intended channel per run. The shared design toolkit omits private Canvas board links. Upstream licenses, provenance pins and notices accompany adapted packages. Limited whitespace normalization fixed publication checks without changing the source installations.

The 37 remaining Mac-only candidates belong to the previously excluded upstream engineering/orchestration collection or vendor skill-discovery package. They remain inventory-only. Existing sanitized public variants were not overwritten with private local copies. The sole VPS-only installed candidate, Canvas Visualize, is now included; existing VPS variants remain unchanged. The [source inventory](skill-sync-2026-11-17.json) records package hashes, transformations, exclusions and local sync results.

## Validation and sync

- All 16 packages passed Skill Creator validation and entrypoint link checks.
- All 3 Python helpers parsed; 15 YAML and 13 JSON resources parsed.
- Sixteen offline helper checks passed for Meta read/account/credential boundaries and marketing totals, comparisons, notes, sector allocation and saved-cell interpretation.
- The 11 existing repository tests passed.
- Gitleaks 8.30.1 found no leaks in the publication batch. Git whitespace checks passed after five source-copy formatting fixes.
- The publish helper installed Canvas Visualize and Meta Ads Insights locally. It updated no existing package and retained local variants, including private configuration and established symlinks.

These checks establish package integrity and offline helper behavior. They do not establish live browser, calendar, diary, Meta, marketing-report, design or YouTube acceptance. No collected workflow was executed against a live account as part of publication.
