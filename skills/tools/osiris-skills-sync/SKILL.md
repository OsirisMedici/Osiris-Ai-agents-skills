---
name: osiris-skills-sync
description: Install and update skills from Osiris's GitHub skills library and push reviewed local skill additions or updates. Use when Osiris asks to sync his skills across computers or publish skills to the Osiris AI Skills repo.
---

# Sync Osiris's skills

Run [scripts/sync.py](scripts/sync.py) with Python 3.9 or later and Git. It reads the public `OsirisMedici/Osiris-Ai-agents-skills` repository. By default it uses `${CODEX_HOME:-$HOME/.codex}/skills`; pass `--skills-dir` for a different supported user skill directory. A push needs GitHub write access, a configured Git author, and Gitleaks 8.19 or later.

1. Run the script with no flags to list missing packages, available updates, differing packages, and local candidates. Run with `--apply` for a pull-only or team sync. GitHub write access is needed only for publishing.
2. For a push or two-way sync, review the local package files and the delta against GitHub. Follow the repository's [publication rules](https://github.com/OsirisMedici/Osiris-Ai-agents-skills/blob/main/AGENTS.md). Collect custom or deliberately adapted packages, preserve attribution, and leave system, plugin, and unrelated upstream collections out. Remove client/account data, private IDs, credentials, exports, and machine-specific records in a separate source directory when needed. A scanner cannot make that editorial decision. Keep existing sanitized public variants unless a reviewed change can be applied to them.
3. Once the user has authorized the push and the package is reviewed, run `--apply --publish NAME` for an existing package or `--apply --publish NAME:CATEGORY` for a new one. Repeat `--publish` for each reviewed package. Use `--source-dir PATH` when publishing curated copies. The helper pulls the current main, scans the publication batch, commits and pushes it, and syncs the local skill directory. An advanced remote rejects the push. Recheck the delta against the new head before retrying.
4. Report the verified revision, installs, upgrades, and variants. The first sync tracks packages it installs and existing copies that match GitHub. Later syncs update tracked copies when their files match the last synced version and retain the previous package under `.osiris-skills-sync/backups`. Leave pre-existing variants and local edits for review.

Example for pulling from a shell:

```sh
python3 "${CODEX_HOME:-$HOME/.codex}/skills/osiris-skills-sync/scripts/sync.py" --apply
```
