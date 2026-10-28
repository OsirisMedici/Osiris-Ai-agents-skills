# VPS skill collection

Collected on 28 October 2026 (UTC) from `vps-1` as `t3worker`, in a fresh dedicated checkout. The owner authorized committing and pushing the complete custom skill set. The existing 23 Mac/Meta packages and the Mac source inventory are unchanged.

Added `update-osiris-t3` under operations and nine standalone workflows under engineering: `babysit-pr`, `council`, `file-pr`, `full-send`, `full-stop`, `leaving-pr-comments`, `modernize`, `sol-loop`, and `takeover`. These workflow names were excluded from the earlier Mac pass. This VPS pass includes them individually as installed T3-aware workflows under the owner's instruction to push all skills; it does not claim that Osiris originally authored each workflow. Their upstream authorship, adaptation history and licensing have not been supplied. Do not infer a public redistribution license. No standalone package includes a license file; no license was removed or invented.

Every source file is preserved byte for byte, with executable modes. Supporting files comprise agent metadata, the updater's installation reference and patch registry, its `status.py` helper, and the `pr-wait` helper. There are no package assets/templates or bundled license files omitted from these ten sources. No packaging sanitization was necessary after reviewing their actual text: they contain reusable instructions, non-secret environment pointers, synthetic syntax, and a public fork PR reference. No credentials, account/client mappings, customer data, sessions, browser state, generated output, or whole source archives are included.

The [VPS inventory](vps-skill-inventory.json) records each source and package file SHA-256, complete-package signatures, full-content duplicate comparison, remote baseline comparison, upstream provenance, search scope, and coverage limitations. No same-name entrypoint among the ten additions exists at the remote baseline, so none replaces an existing package. The nine Claude mirrors are identical to their complete Codex packages. No ambiguous custom-package conflict remains.

## T3 update skill

The requested equivalent is **`update-osiris-t3`**, found at `/home/t3worker/.codex/skills/update-osiris-t3/`. It is published at [`skills/operations/update-osiris-t3/`](../skills/operations/update-osiris-t3/SKILL.md). The separately found `/home/t3worker/.local/share/t3-artifacts/update-osiris-t3.zip` contains the same five files with identical contents. The generated ZIP is not duplicated in Git. No package with the exact requested alternative spellings was found in the accessible inventory.

This is the actual installed package, including its existing patch registry and helper; it was not recreated. Its installation facts are historical and explicitly require live rediscovery when the updater is invoked. No updater preflight, build, installation, workflow, restart, browser operation or customer action was performed during collection.

## Inventory-only sources and conflicts

The separate inventory covers 371 discovered `SKILL.md` entrypoints: 19 standalone source installations (10 Codex and 9 identical Claude mirrors), plus 352 vendor/system/project-upstream entries representing 201 distinct name/content packages. Plugin caches and ordinary imported engineering collections are recorded with their supporting-file hashes rather than copied into this library.

Project-local skill aliases in T3 source checkouts resolve to already inventoried `.agents/skills` packages. The old Crayon `cad` alias resolves to Chalk. These aliases were inspected deliberately; no source symlink was copied.

`test-t3-app` and `test-t3-mobile` each have two upstream content revisions in clean source checkouts. The inventory preserves both versions' file hashes, source paths, checkout heads and last package commits separately. These are upstream source revisions, not conflicting versions of a collected custom package; no version was selected for installation. OpenPlan3D's authoring package and its two examples match the pinned upstream archive at `laanlabs/openPlan3D` commit `4e66c60c00fba494181d647cc10324becd9a50b5` exactly across five copies, so it remains inventory-only with its upstream provenance. Ordinary Crayon, Bitwarden and Effect source skills also remain separately inventoried.

The operating user's Codex, Claude, plugin and T3 directories, projects, worktrees, accessible deployment trees and backup/source locations were searched. No additional configured skill root was found. `/root`, `/home/canvasadmin`, and some deployment/private backup directories are unreadable to this account. No privileged bypass was attempted. Caches, sessions, raw logs, credentials and browser profiles are outside content collection. This is not a claim that every file or every other user's skills on the VPS was inspected.

## Requirements and validation

The updater needs Python 3, Git, authenticated `gh` for optional release discovery, Linux `/proc` and user systemd for server discovery, the external fork checkout and patch commits, and a separately accessible Mac build/install host. `pr-wait` needs Python 3.10+, Unix `fcntl`, Git and authenticated `gh`. The workflows depend on T3 orchestration/watch/PR tools or the alternate harness capabilities described in their text; sibling workflow dependencies are collected together. Applications, patch source code, credentials and the Mac host are external dependencies, not bundled resources.

Validation results are recorded below after offline checks. Publication establishes package integrity and remote availability; runtime acceptance of these workflows remains untested by design.

Offline checks passed: Skill Creator validation for all 33 entrypoints; folder/frontmatter agreement; agent YAML; complete source/package hashes and executable modes for all 19 added files; all new-package relative references and JSON; Python/helper syntax; 15 isolated helper behavior cases with live subprocess execution blocked; the 11 existing Meta tests; whitespace checking; and a redacted secret/credential/contact scan. Public `git@github.com` syntax was the sole reviewed email-pattern false positive. The notes and inventory preserve outstanding provenance and access limitations.

Before publication, fetch discovered two intervening remote commits that renamed the repository to `OsirisMedici/Osiris-Ai-agents-skills` and recorded owner authorization for public visibility in AGENTS.md and the collection prompt. GitHub confirms the destination is public. This collection preserves those changes and does not alter visibility. Original authorship/licensing of the nine standalone workflows remains unverified; no new license or authorship claim is added.
