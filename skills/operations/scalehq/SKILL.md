---
name: scalehq
description: Audit and repair links between GitHub issues and the correct Feedback boards and tasks from ScaleHQ. Use for bulk issue-to-Feedback checks, missing project boards or tasks, and missing issue links in task descriptions. Supports audit-only runs. Does not implement issues or synchronize workflow statuses.
---

# ScaleHQ

Connect every issue in the requested scope to a task on the correct Feedback board. Reuse existing records. Create confirmed missing boards and tasks, and put the canonical GitHub issue URL in each task's saved description.

Examples:

- "Run ScaleHQ and connect all my issues to Feedback."
- "Use $scalehq for the repository I specify."
- "Audit ScaleHQ issue links only. Don't change anything."

"Run ScaleHQ" defaults to repair mode. That invocation, or an explicit sync/connect/repair request, authorizes the necessary board/task creation and description links. Complete those actions without another confirmation. An audit or check-only request is read-only. Creating or installing this skill does not run reconciliation. Do not create GitHub issues, repositories, comments, or portfolio cards in this workflow.

## Start from the checkout

Locate ScaleHQ from the workspace, its parent directories, or this skill's resolved location. Use checkout-relative paths. If installed separately, resolve the authorized checkout from current project configuration. If unavailable, request its location or access instead of guessing a private repository URL. Never assume a machine-specific home directory.

Read `AGENTS.md`, `START-HERE.md`, `registry/README.md`, `registry/board-routing.json`, and `ACCESS.md`. Resolve boards by UUID. `issue_repository` is the destination for new issues; `source_repositories` identifies code ownership. Existing linked issues retain their URLs, including issues shared by several tasks or boards.

Use the current machine's authenticated GitHub and Feedback access. Discover connected tools first, then use authenticated `gh` for GitHub gaps. Read [live access details](references/access.md) when collecting records or writing to Feedback. Credentials and sessions stay on their own machine.

## Establish complete scope

Honor supplied repositories, issue lists, board UUIDs, owners, and state filters. Otherwise enumerate repositories currently owned by the authenticated GitHub account, plus accessible organization repositories represented in ScaleHQ. Include registered issue destinations and repositories containing preserved existing issue links. Include new repositories outside the dated baseline. Do not include unrelated repositories merely because the account can access them.

An unqualified "all my issues" includes open and closed issues. List issues with full pagination and exclude pull requests returned by GitHub's Issues API. Record repository failures, truncation, and search caps as coverage gaps. Saved repository and board inventories do not establish current completeness.

Inventory live Feedback boards, including archived boards, and their tasks, including completed, archived, and undated records when supported. Follow every cursor and read saved rich descriptions, legacy notes, and relevant links. A bounded board list or filtered sidebar does not prove absence. Disclose inaccessible or unsupported portions and continue independent accessible work. Never create a replacement for an inaccessible record.

## Match before writing

Key each issue by its canonical URL and repository identity. Normalize trailing slashes, query strings, and fragments for matching. Resolve transfers through GitHub and preserve historical references. Use exact task UUIDs from existing links, issue bodies, and receipts. Confirm live records before trusting dated observations.

For each issue:

1. Find existing tasks across accessible boards. Distinguish the owning issue from references or dependencies. Read candidates; a similar title alone is insufficient. Preserve several legitimate tasks when one issue spans deliverables or boards.
2. Resolve the board using stable task identity, explicit exceptions, existing links, verified board routing, and project evidence. An issue in a shared backlog keeps its verified project board. Do not create a duplicate merely because the issue repository differs from the project name. A source repository can serve several boards and cannot choose a destination by itself.
3. For a confirmed existing task, append a native issue hyperlink only if its description lacks one. A link only in a comment or custom property does not satisfy the requirement. An existing description link is a no-op.
4. If the correct board exists but no task matches after a complete search, create a task there from the issue. Recheck immediately before creation. Preserve native task-code conventions without collisions or unrelated renumbering.
5. If no board route exists, inspect repository documentation, ScaleHQ context, and the complete live board inventory. Reuse a verified project board. Only if none exists, create a blank board named for that project, or the repository when no broader project is established. Route it to the repository already holding the issue, without provisioning another GitHub repository.

Investigate missing mapped UUIDs, name collisions, renamed repositories, archived boards, conflicting task locations, and multiple plausible boards. Do not automatically move tasks, merge projects, or restore boards. Ask only about unresolved routing while completing clear matches. Keep archived boards archived and report writes requiring restoration as blocked.

## Save and verify

Read the full issue title/body and relevant comments needed to understand scope. New task descriptions contain a short opening paragraph, two to four native action bullets, an observable `Outcome:` paragraph, and a visible native `GitHub issue` hyperlink. Keep long implementation detail in GitHub. Preserve useful source links without inventing requirements from an empty issue body.

Use ordinary board priority and an available `Not started` status unless verified task instructions specify otherwise. Assign the requested owner only after resolving their live Feedback identity. Do not infer Feedback accounts from GitHub logins. Leave dates, recurrence, and time blocks unset unless supplied. Clear accidental Today/automatic scheduling defaults and verify them. Record closed issue state/reason as source context; closure alone does not establish accepted completion or authorize a status change.

Existing tasks get only the missing description link. Preserve UUID, title/code, execution status, priority, assignees, dates, scheduling, recurrence, attachments, unrelated blocks, and checklists. Portfolio priority remains separate from execution status.

Use current page versions and stable request IDs where supported. After a conflict, reread and merge. Before retrying an uncertain creation, inspect live records and the run receipt. Board creation may lack idempotency support; never blindly retry. After one supported authentication refresh, stop affected writes on persistent denial and report the blocker.

Reopen every saved task and verify board UUID, saved description, clickable canonical issue link, and preserved metadata. Re-read each created board's identity. A successful HTTP response or returned UUID does not establish completion. A repeated run must leave correct records unchanged.

## Keep results portable

For new board routes, update `registry/board-routing.json` and the associated evidence and routing table using the current schema. Preserve historical snapshots and existing issue exceptions. Record live IDs, lifecycle, source boundary, verification time, and provenance. Do not label a partial refresh complete. Run `python3 scripts/verify_board_routing.py` after editing the map. If a consistent update cannot be completed, preserve the new UUID and repository in a pending receipt and report the registry gap.

Save a non-secret receipt under `evidence/issue-feedback-sync/<UTC timestamp>.json`. Include requested scope, actor identity, inspected repositories/states, completeness and pending cursors, canonical issue URLs, board/task UUIDs and links, actions, request IDs where supported, readback results, routing evidence, and blockers. Record pending creates before submitting them. Resume from receipts plus fresh live reads. Do not overwrite earlier runs or treat receipts as current task truth.

The checked-in skill and AGENTS entry work without global installation. Each machine needs its own service access. When asked to publish or share changes across machines, commit/push only intended skill, registry, and non-secret evidence changes. Otherwise identify local files that still need sharing. Preserve unrelated work.

Return inspected-issue counts, already linked records, description repairs, created tasks/boards, ambiguous matches, and access gaps. Include links to created/repaired records and the receipt. State coverage separately from write verification. Report remaining exceptions explicitly; claim full completion only when all issues in the stated scope have verified description links on their resolved boards.
