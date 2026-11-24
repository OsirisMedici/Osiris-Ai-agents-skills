# Skill publication, 24 November 2026

Published 38 missing custom packages, bringing the public library from 66 to 104.
Three are newer Codex workflows: `crayon-scale`, `full-flow` and `ship-live`.
The other 35 come from the older Claude user skill folder. Three deprecated
creative workflows are labeled legacy, leaving 101 active packages.

The README now gives every package its own row with its name, a one-sentence
description and an Open skill link. It also links to the repository ZIP and
installation instructions. `scripts/build_catalog.py --check` verifies that every
package has exactly one catalog entry and that no stale descriptions remain.
Maintain descriptions in `docs/skill-catalog.json` and regenerate the README.

## Public-copy changes

Existing public packages and private installed variants were preserved. New
packages were curated separately. Public copies contain no client mappings,
account/calendar IDs, staff rosters, personal session profiles or browser state.
Personal examples, private title drafts and fixed revenue targets were removed.
Workspace folders describe a layout to discover in the installing user's setup.

The usage package excludes its account registry and credential-reading helper.
Its public workflow reads authorized connected tools or the signed-in usage
interface. Reflective support excludes the author's personal profile. Project
sync and training retain reusable procedures without named participants or past
session records. Visual includes the required terminology references directly.
The pitch deck workflow uses a discovered exporter and Bun-based setup rather
than fixed paths from a prior container environment. Full-flow preserves its
attribution to Matt Pocock's main development flow. No new license was added.

The custom Claude research command is published as `vault-research`, preserving
the separate installed upstream engineering command named `research`. The old
index package is published as `blueprint-index` to match its own frontmatter.
`blueprint-index`, `carousel` and `scene-engine` remain clearly marked deprecated;
`creative` is their current replacement for the HTML creative workflow.

## Coverage and exclusions

Inspected the configured Mac Codex, Claude and shared-agent user skill roots and
the ScaleHQ skill roots. Also verified the owning VPS user and inspected its
Codex, Claude and shared-agent skill roots through the existing private route.
No additional unpublished custom package was found there. The GUI driver was
identified as a vendor package and left outside this library. This is not a
claim about other users' homes or unregistered directories.

The imported engineering/orchestration collection, vendor discovery packages,
Humanizer, Remotion rules, system skills and plugin caches remain excluded.
The [source inventory](skill-sync-2026-11-24.json) lists exclusions, command
renames, original and published file hashes, omissions and transformations.
It supersedes the older collection's exclusion of Claude-only custom skills.
No existing private skill installations or fleet sync allowlists were changed.

## Verification

- All 38 new package names and frontmatter validated with Skill Creator.
- Bundled Python syntax and YAML parsed; the Crayon helper's CLI help loaded
  without requesting credentials or contacting its service.
- The reviewed publication batch and the completed repository passed Gitleaks
  with zero findings.
- A clean isolated sync installed all 104 packages from the published repository.
- Catalog generation, link coverage, inventory hashes and Git whitespace checks
  are checked against the completed repository before the documentation push.

These are packaging and offline checks. They do not claim live acceptance of
all 104 workflows, provision their external dependencies or authorize use of
another person's accounts. No captured workflow was executed to collect it.
