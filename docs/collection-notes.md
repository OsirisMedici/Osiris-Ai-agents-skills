# Mac collection, 29 October 2026

This collection adds 22 locally available custom and adapted packages to the existing Meta skill. The repository now contains 23 skill entrypoints. The owner authorized this collection and the expansion of the original social-only scope. Installed source packages were read and copied; they were not edited, replaced, linked, or invoked.

## Source and packaging

`local-skill-inventory.json` records the exact included files, original and packaged SHA-256 hashes, and whether each file changed during packaging. Source locations are host-relative pointers, not a claim that those files exist on the VPS. System skills, plugin caches, upstream engineering/orchestration collections, and older Claude-only skills are outside this collection. The inventory names excluded local Codex packages so this boundary can be reviewed.

Existing attribution, licenses, and public source links remain in the packages. Some packages are curated or adapted upstream workflows rather than wholly original work, including the CLI discovery helper, pet tooling, and local Tesseract workflows. Their presence does not relicense upstream material.

Packaging changes:

- Feedback intake resolves the destination board ID live; the task template uses an illustrative example without a private task link.
- GHL's old client case, contact number, location/workflow IDs and private channel mapping are omitted. The skill points to the authorized current registry and stream map instead.
- Proof logs resolve the Notion destination and template live. Private IDs and client/employee select-list mappings are omitted. The entrypoint description and UI text are YAML-quoted so they parse correctly.
- YouTube account identity is reverified live rather than pinned to a saved channel ID. Topic and procedural notes remain discovery hints.
- Browser Fastpath follows the current in-app Browser requirement and preserves personal Chrome.
- Eden references retain interaction findings but omit raw recording session identifiers.
- Generated Python caches, OS metadata, credentials and build outputs are excluded.

## Environment requirements

The packages retain non-secret operating pointers to local content-engine files, writing voice documents, Feedback task-code rules, browser-profile instructions, and other external workspace material. These are dependencies to resolve on the target host; the private source documents themselves are not included. macOS tools such as Mac Rescue require macOS. Tesseract, video tooling, browser sessions, MCP connectors and accounts must be installed or connected separately. Collected scripts were not run against user data or live services.

The existing Meta package and tests are preserved. No installed skill was upgraded as part of collection, and no live customer/account operation was performed.

## Verification

The publication check covers Skill Creator validation for all 23 entrypoints, folder/frontmatter agreement, agent metadata YAML parsing, relative Markdown link resolution, Python helper syntax, bundled JavaScript syntax, the 11 existing Meta validator tests, whitespace checking, and a redacted secret scan. These checks establish package integrity; they do not establish runtime acceptance for each workflow.

## VPS follow-up

The T3 update skill was not found in local installed Codex/Claude skills, configured skill directories, or the source skill packages inspected on this Mac. Its presence on the VPS remains unverified. It has not been recreated or added under a guessed name.

Use `vps-skill-collection-prompt.txt` from a VPS agent to inventory source packages, locate the T3 update skill, compare duplicates by contents and provenance, preserve uncertain variants, and publish supported additions. The VPS agent should write its own inventory rather than replacing the Mac source snapshot.

## VPS collection completed on 28 October 2026 (UTC)

The VPS follow-up above describes the earlier Mac-only state. The equivalent updater has now been found and collected as `update-osiris-t3`, with all nine other standalone installed VPS workflows. See [VPS collection notes](vps-collection-notes.md) and the separate [VPS inventory](vps-skill-inventory.json). The original Mac inventory remains an unchanged historical snapshot; its `vps_pending` field is superseded by the VPS inventory. The original Mac heading uses its source date; VPS timestamps are recorded independently in UTC.
