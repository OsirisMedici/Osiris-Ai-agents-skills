---
name: osiris-t3
description: Guide Osiris through his custom T3 setup, choosing Mac or VPS work, handing Writer between machines, using T3 Connect, connecting Claude, and coordinating fork updates. Use when he asks how to use or maintain his T3 setup or says he is confused about its machines or builds.
---

# Osiris T3

Make the next action obvious. Osiris uses T3 as the product; Codex and Claude are providers inside it.

## Everyday rule

Most projects and agents run on the VPS. The Mac desktop app is a client for that VPS. A browser using T3 Connect can reach the same VPS while the Mac sleeps. Writer is the chosen local exception: use the Mac's registered Writer project when working on local Writer files.

One coordinated custom release has two builds: Mac desktop on the Mac, Linux server and web assets for the VPS, from the same source revision with the adopted fixes. Building or installing one does not update the other. Contributions upstream are separate from the installed fork.

Start with the user's intent. If missing, ask one small question: **work, Writer handoff, connect/sign in, or update?** Fill machine, paths and current versions from discovery rather than asking Osiris. Explain the immediate choice in a few sentences, then do authorized work.

Read the authorized local setup record for registered environments, paths, and the current release manifest. If it is unavailable, discover these through the configured T3 tools or CLI. Verify dated observations against the active environment.

## Choose where work runs

- Writer local work: registered Mac project, not the similarly named extra clone. Confirm its current workspace through T3 tools.
- Other work: the corresponding VPS project. Discover T3 environment tools first; established SSH is a fallback when those tools are unavailable.
- Verify the target environment before launching or changing a thread. Existing threads, terminals, files and credentials stay with their original environment. Preserve existing local history; the rule does not authorize deleting projects or migrating active work.
- Keep automatic load balancing off for this explicit workflow unless Osiris asks to change it. Choosing an environment is distinct from choosing a Git branch or local/worktree mode.

## Writer handoff

Inspect both worktrees: branch, HEAD, dirty state, upstream and remote commits. Finish the chosen source changes and transfer committed work through GitHub on the same branch. Preserve dirty files and other agents' work. If unfinished work prevents a safe handoff, state exactly which copy needs attention; do not reset, clean, force-push or replace a folder. Files synchronize through Git; T3 thread history and running agents do not.

## Connect or sign in

Read [connections.md](references/connections.md) for T3 Connect and Claude. Check live status before requesting a login. Use the paid Scale Claude subscription rather than creating API billing. Browser sign-in, Claude CLI sign-in and T3 Connect sign-in are separate.

Use the in-app Browser for agent browser work, following the host's profile rules and any explicit current user browser preference. Announce before taking over a screen and release it promptly. Prefer account approval links the user can open themselves. Credentials stay in the provider's supported credential store. Use a private secret tool if a returned code must be provided to the agent.

## Update my custom T3

For an update request, read and run the installed `update-osiris-t3` skill. Supply the current setup and verify the latest installed manifest on the target machine. Preserve the full adopted behavior recorded in that manifest, including newer fixes beyond the older patch registry. Recheck its source commits and focused tests; registry ancestry alone is insufficient.

Prepare a coordinated release with Mac desktop, Linux server and web assets from one chosen published upstream release plus the adopted fork changes. Keep development checkouts distinct from installed runtimes. Follow the update skill for isolated builds, active-work checks, backups, rollback, controlled restarts and installed acceptance. Preserve custom update feeds and browser profiles. Ordinary official updates do not reapply unmerged fork commits.

When asked only to explain the setup, explain it. Creating or invoking this guide is not by itself permission to update, restart or migrate anything.

## Hand back

Give Osiris the next action, the machine it affects and a short verified status. Distinguish installed, configured, authenticated and actually tested. Keep pending account approval or restart work explicit. Update the GitHub guide's progress checklist after meaningful setup changes when that publication is authorized. Keep secrets and temporary authorization links out of the guide and this skill.
