# Review coverage

Snapshot date: 11 November 2026. The YouTube connection identified Osiris Medici, and both the GitHub connector and CLI identified OsirisMedici. This is a review of the saved collection at that time.

## What was inventoried

| Source | Complete inventory | Detailed screening and retained material |
| --- | --- | --- |
| YouTube Liked videos | 4,978 unique entries across 100 API pages; no next-page token remained | Title/channel screening selected 197 candidates in two passes. All 197 returned current creator metadata and descriptions. The catalog retains 58 core resources, 34 supporting or visual references and 24 adjacent references; 81 candidates were excluded as incidental matches. |
| GitHub stars | 72 repositories; the complete authenticated starred list was retrieved | 41 plausible design candidates had README/source/tree inspection. The report catalogs 27 reusable, specialist, workflow or product-pattern references and 13 historical examples, including items with insufficient usable source. One candidate was a false positive; another 31 stars were screened as unrelated through metadata. |

620 liked entries have unavailable titles: 353 Deleted video and 267 Private video. Their contents and design relevance are unknown. The remaining 4,358 titles were identifiable. Screening the complete title list does not prove every video with an ambiguous title was classified correctly.

## Depth of review

The video catalog labels creator-description/chapter review separately from thin metadata. Full auto-generated transcripts were read for [Griffin Wooldridge's UI-library video](https://www.youtube.com/watch?v=zsCGS-Yzjnw) and [Kole Jain's UI critique](https://www.youtube.com/watch?v=PDcQJOPby1k). Most other entries use creator descriptions and chapters, not full playback. Auto-generated captions can contain transcription errors.

Of the 116 retained catalog entries, 83 have descriptions that support their listed subject or proposed use, while 33 are thin-description or metadata-only pointers. A pointer needs closer review before extracting a method or selecting a tool.

The UI-library transcript distinguishes foundational behavior, specialist interactions and styled components. It recommends deliberate type, color and shape choices, then a restrained use of visual effects. The [current primary library guide](https://github.com/emilkowalski/skills/blob/main/skills/pick-ui-library/SKILL.md) and official Base UI, shadcn/ui, Sonner and Motion documentation were checked separately before the toolkit's task mapping was written.

Stageshow's README, skill source, MIT license and notices were read from its owning repository. Its scripted demonstrations are illustrations, and its third-party icons and trademarks retain separate rights. These sources and Emil's guide came from liked-video links, not the starred inventory.

The [repository catalog](repositories.md) records README/source evidence and current license/activity signals. Those checks do not establish runtime compatibility, production readiness or adoption across Scale projects.

## What is ready to use

The [toolkit entry point](library.md), [project brief](brief.md), [review checklist](review-checklist.md), catalogs and [resource manifest](resource-manifest.json) are available in this repository. They provide a starting workflow and a way to choose resources for a real project. No third-party skill, dependency, service subscription or product migration was performed for this review.

The work did not change saved likes, stars, playlists, accounts, campaigns, live designs, app source or issue records. A direct caption download encountered a rate limit; the successful transcript exports used the in-app Browser. Further transcript export was interrupted by a browser timeout, so unreviewed videos remain labeled accordingly.

## Evidence and refresh

Raw snapshots and source captures remain in the original private ScaleHQ research workspace and are excluded from this repository. This includes unrelated private liked-video history, so do not publish or upload the raw inventory as part of sharing a toolkit excerpt.

- Complete liked inventory (private source capture retained in ScaleHQ)
- All 197 video decisions (private source capture retained in ScaleHQ)
- Complete starred inventory (private source capture retained in ScaleHQ)
- Structured repository review (private source capture retained in ScaleHQ)
- UI-library transcript (private source capture retained in ScaleHQ)
- UI-critique transcript (private source capture retained in ScaleHQ)

Before adopting a resource, recheck its current source, selected version, applicable code and asset terms, and fit with the owning product. Keep the raw snapshot as dated evidence; record tested results separately.
