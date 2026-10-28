---
name: fti-feedback-task-intake
description: FTI - Feedback task intake. Capture Osiris's spoken or written tasks in Feedback using the shared task template. Use when asked to add, save, or capture a task in Feedback, when Osiris says FTI with a task, or when invoked with a new task. Defaults important work needing his later attention to the Needs my attention board.
---

# FTI - Feedback task intake

Turn a rough task into a saved, readable Feedback task. Capture the work for later unless Osiris also asks to execute it. Invoking this skill with a task authorizes its creation; complete the save and readback without asking for a second confirmation.

## Destination and defaults

- Product: https://feedback.scaleadvertisement.com
- Default board: `Needs my attention`. Resolve its current ID from Feedback before writing.
- This board holds important work that needs Osiris's personal attention later. Use it when no other destination is requested. An explicit destination takes precedence.
- Board prefix: `ATT`. Format `ATT-NNN · Action-led task title`. Determine the next code and execution position from live tasks and the code register, never from the example below.
- Default assignee: the verified Osiris Medici account. Resolve the live identity rather than guessing an ID.
- Default status: `Not started`. Keep the product's ordinary priority unless Osiris supplies a different priority.
- Without a requested date, preserve null due/end dates, no start restriction or fixed block, `hardDeadline: false`, no recurrence, and scheduling mode `date_only`. In Feedback this mode also represents an undated task without automatic time allocation.

## Capture and save

1. Read [the shared task template](references/task-template.md) on every invocation before drafting. This file owns the FTI structure and approved example. Read `/Users/osirismedici/.codex/instructions/feedback-task-codes.md` and its referenced register for board codes and ordering. The template follows the wider Karen task-writing rule at `/Users/osirismedici/Desktop/Karen/TASK_WRITING.md`.
2. Inspect the live destination and all its tasks, following every continuation and including completed and undated tasks. Search the exact board for duplicates. Reuse a clear match when the user is adding context to it; clarify genuinely ambiguous matches before a write. If the saved board is inaccessible, explain the blocker instead of creating a replacement board.
3. Extract the intended work, reason, next actions, and observable outcome. Keep uncertain decisions as actions to resolve during the task. Ask only when missing information changes the destination, scope, owner, or a real scheduling commitment. Resolve relative dates in Asia/Kolkata, state the absolute date, and clarify ambiguous dates.
4. Fill the shared template with the task's content. Preserve its section order, sentence and bullet ranges, and observable outcome. Create a native rich-text document with real paragraphs and list items. Preserve supplied source links without requiring research just to capture the task.
5. Create on the exact board with a stable UUID client request ID. Save the body using the current page version. Apply the task-code ordering rule to affected unfinished work while preserving task UUIDs and completed history. A task request authorizes this bounded insertion, not unrelated board cleanup.
6. Reopen the task and read the saved document and metadata. Compare the saved body with the template's acceptance check, including native list structure and the first viewport. Verify title, text, board, assignee, status, notes, dueDate, endDate, hardDeadline, start restriction, schedule mode, calendar blocks, and recurrence. Creation can silently apply Today and automatic scheduling even with null dates. Clear those defaults for undated captures and reread them.
7. Check code uniqueness across the complete board, update the code register after verification, and report the task code and direct link. State the owner and date briefly. Save only a compact local receipt when needed for verification or resequencing.

## Improving the template

When Osiris asks to improve the format, edit [references/task-template.md](references/task-template.md) and increment its version. Keep the structure and acceptance check together in that file so future runs read one current definition. Preserve the approved example as the original reference unless he asks to revise it.

Template improvements apply to future authoring. Rewrite existing Feedback tasks only when requested. A one-task wording exception does not change the shared template unless Osiris asks to make it the new default.

## Access and API fallback

Discover current Feedback MCP or app tools first. If unavailable, use T3's in-app Browser with the persistent `Default` profile. Read `/Users/osirismedici/.config/osiris-agent-rules/t3-browser-profiles.md` before opening it. Verify the signed-in identity. Respect tab ownership and keep session material out of output. If authentication is required, follow the workspace account-routing and private credential instructions.

The authenticated in-page API is a usable fallback when app tools are absent. These routes were verified on 26 October 2026; inspect current responses and schemas when behavior differs:

- `GET /api/bootstrap` identifies `currentUser` and accessible boards. Return only the fields needed.
- `POST /api/agent/context` uses `{operation, input}`, including `get_context` and `resolve_board`.
- `POST /api/agent/tasks/search` uses `{input:{scope:"selected-boards",boardIds:[boardId],limit:50}}`. Follow `data.nextCursor` with the same filters until complete.
- `POST /api/agent/tasks/batch` uses `{operation:"create",input:{tasks:[...]}}` or versioned `update`. Inspect each result; HTTP success can contain failed items.
- `GET /api/tasks/<taskId>/page` reads the document and version. `PATCH` uses `{baseVersion,document,icon,coverUrl}`. Preserve document layout and unknown fields; preserve unrelated blocks on existing tasks. The generic append-section tool creates paragraphs and cannot create native bullet items.
- `PUT /api/calendar/tasks/<taskId>/schedule` with `{mode:"date_only"}` clears automatic time scheduling for a later-work capture.
- `GET /api/tasks/<taskId>/detail` reads saved task, page, schedule, recurrence, permissions, and blocks. Return only relevant fields.

Use JSON request bodies and the live `x-feedback-actor-id` header. If a mutation returns `401 Reload Feedback before saving from this session`, reload that same Default tab once, refresh the actor, reread state, and retry the same idempotent request. On version conflicts, reread and recompute. After a lost create response, find the task or retry its stable request ID before creating anything else. Report a persistent access or transport blocker honestly.

Task links use `https://feedback.scaleadvertisement.com/?boardId=<boardId>&task=<taskId>`.
