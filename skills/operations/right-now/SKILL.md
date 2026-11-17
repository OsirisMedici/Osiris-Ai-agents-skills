---
name: right-now
description: Check the current time, Life Compass and live Feedback tasks, ask for a work mode through native choices, and recommend five useful next actions. Use when Osiris asks what to work on now or invokes Right Now.
---

# Right Now

Give Osiris a short, source-backed choice of work he can start now. Each invocation is a fresh snapshot. Run when asked; refresh on rerun rather than monitoring or switching modes in the background.

## Read the moment

1. Read the current clock and use Asia/Kolkata unless Osiris gives a travel zone. State the local date and time. Read the connected Calendar profile and verify it against the account in the user's authorized private configuration.
2. Read Life Compass for the current local day, including events overlapping now. Resolve its existing calendar ID from the private calendar configuration; never publish that identifier in the skill. Use explicit RFC3339 bounds and follow every page. Identify the active block, its end, time remaining and the next commitment. Read primary-calendar commitments in the same interval to identify conflicts. Life Compass records the intended activity; Life Log records history and does not establish what Osiris must do now.
3. If two plans conflict, report the conflict and use the active Life Compass block to frame suggestions. Ask a native clarification only if the ambiguity prevents a useful recommendation. An empty interval is unallocated personal time, not automatic availability for work. Preserve the distinction between a sales-call availability hold and a booked appointment.

## Ask the mode once

Use the harness's native question-input feature. Prefer a native choice tool that supports the full option list, such as `request_user_input_async` when available. Put the calendar-matching option first. A preselected choice is not an answer; wait for an explicit reply before ranking tasks.

- **Build and code:** applications, product features, technical diagnosis and implementation.
- **Sales and marketing:** sales preparation, prospect follow-up, advertising, outreach preparation and content.
- **Client work and operations:** client delivery, lead handling, campaign/client reviews, coordination and essential admin.
- **Personal time and learning:** learning, personal projects, practical personal tasks or rest.

During an agency block, show only the first three options. Hide Personal time and learning as Osiris requested. During other intervals, offer all four. Determine agency purpose from the title and context, including yellow sales-call holds; color alone is insufficient. If the user has explicitly supplied a mode in this invocation, use it without asking again. Native free text can refine a mode. If native input is unavailable, state that limitation rather than substituting a chat questionnaire.

For a sleep, meal or wind-down block, acknowledge the intended rest/basic-care activity. Recommend work for the next work interval unless Osiris explicitly chooses to work now. During unallocated personal time, still offer five optional tasks after the mode choice, as Osiris requested; keep the time unallocated in the calendar. A selected work mode authorizes optional recommendations, not calendar changes or a claim that he ought to work. If the mode is personal/rest and no work is wanted, honor that choice.

## Read the live task portfolio

1. Discover current Feedback app/MCP tools first. Resolve the live signed-in identity and all accessible boards, including Needs my attention and the client, agency and product boards. Read all pages of unfinished tasks, including undated work. Follow the read-only fallback in [Feedback access](references/feedback-read.md) only when native tools are insufficient.
2. Match tasks to Osiris's actual user ID, tasks explicitly needing his decision, and unassigned work he can take. Team tasks may be useful context; distinguish delegation/review from doing another person's assigned implementation. Read `~/.codex/instructions/feedback-task-codes.md`: lower codes indicate earlier work within their board; codes from different boards are not a universal priority scale. Read-only recommendations preserve codes, UUIDs, dates, owners and statuses.
3. Exclude completed, cancelled, archived and future-start tasks from immediate actions. Identify blocked work and recommend a concrete unblocking action only when Osiris can perform it. Distinguish portfolio priority from executable status. Existing recurring tasks remain unchanged.
4. Read the current details, dependencies and linked brief for shortlisted tasks. Use existing issue links as context rather than creating issues or treating stale issue text as current task status. Resolve board identity by ID; the local ScaleHQ board map is a routing aid, not a live task inventory.
5. Track coverage. If a board, task source or permission is inaccessible, name the gap briefly. Use verified available tasks and label partial coverage. If Feedback cannot be read at all, report the access blocker and the verified calendar context; do not fabricate five tasks from memory.

## Choose five next actions

Rank verified tasks by selected mode and active block, actual commitments/deadlines, prerequisites, need for Osiris's attention, then readiness and effort. Use board code order as a sequencing signal within a board. Calendar fit guides selection; a genuinely urgent mismatch should be explained rather than hidden.

Tasks longer than the remaining block are allowed, as Osiris requested. Mark the likely full duration and offer a bounded first action that fits before the next commitment. Estimates are labeled estimates; do not imply unknown durations are measured. A long task does not authorize overrunning a booked call, sleep or meal. Avoid repeated variants of the same task merely to reach five. Return fewer than five when fewer verified, appropriate tasks exist, with a brief reason.

## Respond

Lead with local time, the active Life Compass block and time left. Show the selected mode. Then give up to five ranked options, each with:

- The live task title/code and direct Feedback link.
- One concrete first action and why it fits now.
- A brief time estimate, including any longer-task warning.

Recommend one best starting option with a short reason. Keep the report concise. In voice, show exact links and technical values visibly and speak the useful takeaway. Refresh the clock before reporting if the read has materially reduced the remaining time.

This skill recommends only. Starting work, changing tasks, calendar edits, messages, booking/cancelling calls and external actions require their own user instruction. It creates no recurring automation or background watcher.
