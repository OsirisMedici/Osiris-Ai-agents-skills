# Osiris Ai agents skills

Public source library for Osiris's reusable operations, creative, product, and tool skills. Repository: [Osiris-Ai-agents-skills](https://github.com/OsirisMedici/Osiris-Ai-agents-skills). On 29 October 2026 its scope expanded beyond social and campaign operations to collect custom and adapted skills available on Mac and VPS.

## Catalog

| Category | Skills |
| --- | --- |
| Meta | [meta-ads-manager](skills/meta/meta-ads-manager/SKILL.md) |
| Operations | [browser-fastpath](skills/operations/browser-fastpath/SKILL.md), [clean-pinned-tasks](skills/operations/clean-pinned-tasks/SKILL.md), [fti-feedback-task-intake](skills/operations/fti-feedback-task-intake/SKILL.md), [go-highlevel-operator](skills/operations/go-highlevel-operator/SKILL.md), [mac-rescue](skills/operations/mac-rescue/SKILL.md), [proof-of-work-log](skills/operations/proof-of-work-log/SKILL.md), [update-osiris-t3](skills/operations/update-osiris-t3/SKILL.md) |
| Creative and product | [content-engine-osiris](skills/creative/content-engine-osiris/SKILL.md), [eden-ingestion-pattern](skills/creative/eden-ingestion-pattern/SKILL.md), [eden-workspace-feel](skills/creative/eden-workspace-feel/SKILL.md), [hatch-pet](skills/creative/hatch-pet/SKILL.md), [osiris-tweets](skills/creative/osiris-tweets/SKILL.md), [product-motion](skills/creative/product-motion/SKILL.md), [stich](skills/creative/stich/SKILL.md), [tesseract-design](skills/creative/tesseract-design/SKILL.md), [tesseract-editor](skills/creative/tesseract-editor/SKILL.md), [tesseract-motion](skills/creative/tesseract-motion/SKILL.md), [tesseract-video](skills/creative/tesseract-video/SKILL.md), [weftcut](skills/creative/weftcut/SKILL.md), [working-todo-builder](skills/creative/working-todo-builder/SKILL.md) |
| YouTube | [youtube-cleaner](skills/youtube/youtube-cleaner/SKILL.md), [youtube-watch-later](skills/youtube/youtube-watch-later/SKILL.md) |
| Engineering workflows (VPS) | [babysit-pr](skills/engineering/babysit-pr/SKILL.md), [council](skills/engineering/council/SKILL.md), [file-pr](skills/engineering/file-pr/SKILL.md), [full-send](skills/engineering/full-send/SKILL.md), [full-stop](skills/engineering/full-stop/SKILL.md), [leaving-pr-comments](skills/engineering/leaving-pr-comments/SKILL.md), [modernize](skills/engineering/modernize/SKILL.md), [sol-loop](skills/engineering/sol-loop/SKILL.md), [takeover](skills/engineering/takeover/SKILL.md) |
| Tools | [cli-hub-meta-skill](skills/tools/cli-hub-meta-skill/SKILL.md) |

## Collection status

The Mac collection adds 22 custom and adapted skills alongside the existing Meta skill. The [source inventory](docs/local-skill-inventory.json) records included paths, file hashes, and packaging differences. [Collection notes](docs/collection-notes.md) describe validation and external dependencies.

The VPS collection adds all 10 standalone non-system installed packages: `update-osiris-t3` and nine T3-aware engineering workflows. The updater was found at `~/.codex/skills/update-osiris-t3`; its five files match the delivery ZIP exactly. The library now has 33 skill entrypoints. The [VPS inventory](docs/vps-skill-inventory.json) records hashes, identical mirrors, upstream content variants, provenance limits and search coverage; [VPS collection notes](docs/vps-collection-notes.md) record validation and dependencies. Vendor/system packages remain inventory-only. Some other-user and deployment directories were unreadable; coverage is limited to accessible configured homes and sources.

## Install and use

Copy or link an individual `skills/<category>/<skill-name>/` folder into the target agent's supported skills directory, preserving any existing same-name installation until its differences have been reviewed. Invoke it by its frontmatter name, for example `$tesseract-video` or `$fti-feedback-task-intake`.

Some skills target macOS, a local app, a private workspace, or specific MCP tools. Inspect their requirements and resolve environment pointers on the target host before use. This library stores skill packages, not those applications, private reference documents, dependencies, credentials, or signed-in sessions. Copying a skill does not run its workflow or grant external write permission.

## Maintenance

Keep skills in `skills/<category>/<skill-name>/`, including their references, helpers, templates, assets, metadata and existing licenses. Preserve attribution for adapted and curated upstream material. System/plugin caches and unrelated installed engineering collections are outside this custom-skill collection.

Follow [AGENTS.md](AGENTS.md). Run the available Skill Creator `quick_validate.py` on changed skills and appropriate checks on modified helpers. The owner authorized public visibility on 29 October 2026. Retain client/account data in its private authorized workspace.
