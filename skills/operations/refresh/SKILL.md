---
name: refresh
description: Use when Osiris says "refresh" — reorders every task list in Top-Priorities.md so uncompleted tasks are on top and completed tasks are on the bottom, within each existing section. No separators added.
---

# Refresh — Task List Reorder

## Public setup

Resolve the user's authorized workspace before following file paths below.
`<workspace>` and named vault folders describe an existing layout, not bundled
data. Reuse equivalent files in the user's setup. Ask for a destination only
when discovery cannot resolve it. Private records and reference documents must
be supplied or located locally; do not invent their contents. Reuse answers
already in the request rather than repeating the intake. Use available supported
tools and the visible in-app Browser for browser work. Installing this skill
does not invoke it or authorize messages, publishing or unrelated service writes.

## What It Does

Reorders every task list in `veronica-memory/Top-Priorities.md` in place:
- Uncompleted `[ ]` tasks → top of each section
- Completed `[x]` tasks → bottom of each section
- No separators, no new sections, no labels — just reordered

## Rules

- Reorder **within** each section — never move tasks between sections
- Preserve the exact text of every task, only the position changes
- If a section is all `[ ]` or all `[x]`, leave it as-is (no change needed)
- Do NOT add any visual divider between uncompleted and completed

## Execution

1. Read `veronica-memory/Top-Priorities.md`
2. For each list section: pull all `[ ]` tasks to top, push all `[x]` tasks to bottom
3. Recalculate Week Progress (see below) and update the progress line
4. Write the file
5. Tell Osiris the file path — one line, done

## Week Progress Calculation

Count checkboxes in all client sections under the `## Week [N]` header.
Exclude: Power List and work owned by others. Note: Delegate, Team Sync, and Waiting On now live in Off-My-Plate.md — they won't appear here.

- `done` = count of `[x]` in those sections
- `total` = count of all `[ ]` + `[x]` in those sections
- `remaining` = total - done
- `pct` = round(done / total * 100)
- `days_left` = days remaining until Sunday (end of week), including today
- `daily_target` = ceil(remaining / days_left)

Update these lines at the top of the file. Two trailing spaces after each line (hard line break) — separate lines, no gap:
```
*Week Progress*<br>
*`X / Y done`*<br>
*Z%*<br>
*~N tasks/day*<br>
*D days left*
```

If there are no weekly tasks, report zero total and use zero percent; avoid division by zero. A local delegation entry records a handoff decision and does not prove the underlying task was completed or authorize messaging the assignee.
