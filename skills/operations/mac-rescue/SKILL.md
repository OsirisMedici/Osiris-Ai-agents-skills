---
name: mac-rescue
description: Diagnose a slow MacBook or Mac, investigate RAM and disk pressure, assess what can stay local, move to an external SSD, or be deleted, then execute one consolidated approval plan and verify the result. Use for slow-laptop, low-storage, excessive-swap, or Mac cleanup requests.
---

# Mac rescue

Give Osiris one terminal-only sequence: inspect, diagnose, review one exact plan, execute the approved actions, and measure the result. A new invocation authorizes read-only diagnosis. One approval covers the complete listed plan, including stated fallbacks; it is not blanket approval for other files, apps, or later runs. Use supported CLIs and Python from the terminal; do not use browser or native UI automation for this workflow.

## 1. Establish the current problem

Inspect this Mac instead of reusing old PIDs, sizes, mount paths, or approval lists. Save receipts in a private, dated output folder in the current workspace. The bundled scripts use `python3`, need no extra packages, and never stop apps or delete data.

```bash
python3 <skill-directory>/scripts/snapshot.py --output <output-directory>/before.json
python3 <skill-directory>/scripts/storage_inventory.py --output <output-directory>/storage.json
```

The storage helper scans sequentially at reduced priority. Start with its overview, then use `--root <path> --depth 1` for the largest relevant directories. Keep long scans bounded, report inaccessible or timed-out areas, and avoid repeated traversals of the same tree.

Inspect CPU, memory pressure, swap traffic over an interval, compressed memory, actual free disk space, disk I/O, power/thermal status, backups/indexing, and the largest processes. Map heavy processes to their app or working directory and inspect active T3 tasks before proposing a stop. Use supported terminal interfaces, including the T3 ACP MCP CLI when available for task state. Preserve personal Chrome. If unsaved app state cannot be established from terminals, label it unknown and explain the force-quit consequence in the approval plan rather than opening UI.

**Done when:** identify the main measured bottleneck, contributors, and unknowns. RAM pressure and stored data are different problems. Cumulative swap alone does not prove active thrashing; free RAM alone does not describe pressure. Summed process memory needs a shared/compressed-memory caveat. Resource checks do not certify hardware or prove perceived UI responsiveness.

## 2. Assess storage in the same run

Read [references/storage-and-ssd.md](references/storage-and-ssd.md) before assessing candidates or proposing migration. Report internal capacity, actual free bytes, and the largest measured categories. Classify exact candidates as:

- **Keep local:** active projects, current work, and protected application or private data.
- **Archive or move to SSD:** inactive durable files whose future access and restore needs are understood.
- **Delete or regenerate:** verified disposable files, with the rebuild/download consequence stated.
- **Unknown:** ownership, use, backup, or permission is not established. Keep it pending.

Inspect mounted external drives even when memory is the main issue. For a missing SSD, finish the local diagnosis and plan; report migration as unavailable. A folder under `/Volumes` is not proof of a mounted disk. Audit startup items when their measured load or the request warrants it. Read the existing cache-retention script and LaunchAgent before proposing changes to that policy.

**Done when:** every proposed action has an exact source, owner/purpose, measured size, activity status, rationale, data-loss/rebuild consequence, and any destination and verification requirement. Candidate sizes, expected reclaimed bytes, and actual free space remain separate.

## 3. Present one approval plan

Lead with the outcome and why it should improve this Mac. Explain the finished experience, included/excluded scope, actions, verification, and honest limits. Use a compact action table when useful. Save the exact plan and manifest in the output folder.

List app/service stops individually, exact deletion paths, SSD source/destination pairs, verification before source removal, and the fallback order. For approved app stops, use terminal force quit as Osiris requested; state that unsaved work may be lost and name the exact apps in the one approval plan. Give an expected range without double-counting overlapping folders or copy sizes. Use at least 20 GB free as an initial working target for this Mac, with 30 GB preferred when practical; label this as a chosen target, not an Apple requirement.

Ask once: `Reply Approve to apply this exact plan.` After approval, execute all listed steps without another design conversation. A material expansion stays outside the plan and is reported as a remaining option. Preserve narrowed/rejected actions. An SSD becoming available does not expand a prior cache-only approval.

**Done when:** `Approve` identifies the full authorized sequence, including any listed fallback if the first stage misses its target.

## 4. Execute the authorized sequence

Recheck each target immediately before mutation: host, owner, real path and symlink status, mount identity, open files, active processes/tasks, and capacity. Use a scoped open-file check; an unreadable or inconclusive check means skip that target. Process arguments, environments, auth files, and browser state may contain secrets; collect only the names, PIDs, working directories, and metadata needed.

For approved generated dependencies or cache contents, remove only the listed scope, preserve source/manifests/lockfiles, and compare affected Git status before and after with `GIT_OPTIONAL_LOCKS=0`. A directory called `.cache` can contain unique source, application candidates, proof, or rollback material. Inspect it before classification. Keep cache parents when approval covers contents only.

Force-quit only the approved apps from terminals. Revalidate exact executable identities and PIDs immediately before signaling, include only those apps' helpers, then reread process state. Prefer exact PID signals over broad name matches. App force-quit permission does not authorize stopping active development tasks, deleting app data, or signaling unrelated helpers. An empty container list may support stopping an approved Colima VM through its CLI, never deleting disks or volumes. Preserve active T3/Codex helpers and development servers. Current protected apps include Handy, MonitorControl, and Raycast unless Osiris changes that choice.

Use the reference's copy/verify/remove sequence for SSD work. Save a receipt after each action, including skips and partial transfers. For long transfers, provide a resumable user-runnable workflow with progress and logs when preferable to chat polling.

**Done when:** every action is completed, skipped with a reason, or recorded as incomplete. Continue other approved actions when a target changes or a check fails. Rebooting, force-quitting active work, disabling swap/indexing, disk repair, permission changes, and Docker volume pruning require their own exact proposed scope; none is an implicit cleanup step.

## 5. Verify and hand off

Re-run the snapshot after cleanup I/O settles. Compare immediate pre-execution and post-execution free bytes, pressure, swap rates, and retained/closed processes. Keep earlier diagnostic snapshots separate from the mutation baseline when other tasks continued working. Verify Git state, protected data, and archive checks separately; Git status does not verify private app data.

Verify the affected app through its supported CLI or scoped diagnostics when available. Keep UI-only acceptance explicitly unverified; do not launch apps, record, or open a browser to check it. State that resource measurements do not prove the original interactive symptom has disappeared. A missed free-space target does not authorize new deletions.

Report what Osiris can now do, measured changes, remaining pressure or unknowns, how to check the original symptom, and receipt paths. Finish user-facing responses with `over and out`. Leave no background cleaner, recurring task, or startup-policy change unless included and approved.
