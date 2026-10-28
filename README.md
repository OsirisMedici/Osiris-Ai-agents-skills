# Osiris Ai agents skills

Private source library for Osiris's reusable operations, creative, product, and tool skills. Repository: [Osiris-Ai-agents-skills](https://github.com/OsirisMedici/Osiris-Ai-agents-skills). On 29 October 2026 its scope expanded beyond social and campaign operations to collect custom and adapted skills available on Mac and VPS.

## Catalog

| Category | Skills |
| --- | --- |
| Meta | [meta-ads-manager](skills/meta/meta-ads-manager/SKILL.md) |
| Operations | [browser-fastpath](skills/operations/browser-fastpath/SKILL.md), [clean-pinned-tasks](skills/operations/clean-pinned-tasks/SKILL.md), [fti-feedback-task-intake](skills/operations/fti-feedback-task-intake/SKILL.md), [go-highlevel-operator](skills/operations/go-highlevel-operator/SKILL.md), [mac-rescue](skills/operations/mac-rescue/SKILL.md), [proof-of-work-log](skills/operations/proof-of-work-log/SKILL.md) |
| Creative and product | [content-engine-osiris](skills/creative/content-engine-osiris/SKILL.md), [eden-ingestion-pattern](skills/creative/eden-ingestion-pattern/SKILL.md), [eden-workspace-feel](skills/creative/eden-workspace-feel/SKILL.md), [hatch-pet](skills/creative/hatch-pet/SKILL.md), [osiris-tweets](skills/creative/osiris-tweets/SKILL.md), [product-motion](skills/creative/product-motion/SKILL.md), [stich](skills/creative/stich/SKILL.md), [tesseract-design](skills/creative/tesseract-design/SKILL.md), [tesseract-editor](skills/creative/tesseract-editor/SKILL.md), [tesseract-motion](skills/creative/tesseract-motion/SKILL.md), [tesseract-video](skills/creative/tesseract-video/SKILL.md), [weftcut](skills/creative/weftcut/SKILL.md), [working-todo-builder](skills/creative/working-todo-builder/SKILL.md) |
| YouTube | [youtube-cleaner](skills/youtube/youtube-cleaner/SKILL.md), [youtube-watch-later](skills/youtube/youtube-watch-later/SKILL.md) |
| Tools | [cli-hub-meta-skill](skills/tools/cli-hub-meta-skill/SKILL.md) |

## Collection status

The Mac collection adds 22 custom and adapted skills alongside the existing Meta skill. The [source inventory](docs/local-skill-inventory.json) records included paths, file hashes, and packaging differences. [Collection notes](docs/collection-notes.md) describe validation and external dependencies.

The VPS has not been inspected in this collection. `osiris-t3-update`, or an equivalent T3 update skill, remains unlocated. Use the [VPS collection prompt](docs/vps-skill-collection-prompt.txt) to find and reconcile remaining skills. A missing local file does not prove that no VPS copy exists.

## Install and use

Copy or link an individual `skills/<category>/<skill-name>/` folder into the target agent's supported skills directory, preserving any existing same-name installation until its differences have been reviewed. Invoke it by its frontmatter name, for example `$tesseract-video` or `$fti-feedback-task-intake`.

Some skills target macOS, a local app, a private workspace, or specific MCP tools. Inspect their requirements and resolve environment pointers on the target host before use. This library stores skill packages, not those applications, private reference documents, dependencies, credentials, or signed-in sessions. Copying a skill does not run its workflow or grant external write permission.

## Maintenance

Keep skills in `skills/<category>/<skill-name>/`, including their references, helpers, templates, assets, metadata and existing licenses. Preserve attribution for adapted and curated upstream material. System/plugin caches and unrelated installed engineering collections are outside this custom-skill collection.

Follow [AGENTS.md](AGENTS.md). Run the available Skill Creator `quick_validate.py` on changed skills and appropriate checks on modified helpers. Keep the repository private and retain client/account data in its authorized workspace.
