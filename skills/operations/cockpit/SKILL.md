---
name: cockpit
description: "Build a daily operations page from connected tasks, calendars and private workspace notes."
---

# Cockpit

Maintain one daily operations page from the user's actual task service, calendars
and workspace. Read-only regeneration is the default. A request to view the page
does not authorize changes in connected services.

## Resolve the workspace

Find the existing cockpit, priority list, client status, training log and inbox
from the authorized workspace's instructions. The original layout uses
`veronica-memory/_COCKPIT.md`, `_BRIEF.md`, `Top-Priorities.md` and `_TRAINING.md`.
Use equivalent existing files rather than creating a second system. Resolve the
task workspace, assignee, selected calendars and timezone through supported tools
or local configuration. Ask for an ambiguous destination. This package contains
no account mappings, project IDs, revenue targets or personal calendar names.

## Regenerate

1. Read today's and tomorrow's selected calendar events, incomplete assigned
   tasks, current client status, priorities, training state and inbox count.
   Fetch independent sources together. Stamp each unavailable feed as unavailable.
2. Select three to five real priorities. Prefer explicitly ranked tasks, due
   work and known blockers. Fall back to the local priority list when the task
   feed is empty, and label that fallback.
3. Show today's schedule by calendar, overlaps and free intervals. Use event
   boundaries in the configured timezone, including overnight events.
4. Include client last contact, next action, blocker and days silent. Derive last
   contact from an activity record. A file modification time is not proof of contact.
5. Show today's training partner, current SOP and last completed session. Apply
   reminders only when the user has configured a training commitment and threshold.
6. Add overdue decisions, upcoming calls and due check-ins. Show weekly metrics
   only when their definitions and source coverage are known. Use observed
   completion events, not keywords or file timestamps, to count shipped work.
7. Write the existing cockpit page with a regeneration timestamp. Keep sections
   for schedule, priorities, training, clients, pipeline, overdue work, metrics
   and inbox when those sources are configured. Read it back and return its path.

## Apply a requested update

Resolve the exact task, client or calendar before writing. A task name with
multiple matches needs clarification. Check availability for scheduling and
preserve the requested assignee, dates and timezone. Use supported service tools.
The user's instruction must authorize the particular mutation; regeneration
alone grants none. Record the returned ID and observed saved result in the
private cockpit log, then regenerate. Preserve uncertain outcomes for inspection
before retrying. Keep credentials and session material outside the log.

Use the installed `training` skill for training updates when available. A missing
optional feed should leave a useful partial page with explicit gaps.
