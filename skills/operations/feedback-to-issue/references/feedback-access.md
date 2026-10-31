# Feedback access and bounded backlink

`fti-feedback-task-intake` owns new-task intake and its rich-text template. This workflow reads an existing task and adds a link; it does not create or resequence Feedback tasks.

## Discover before choosing a fallback

Search current tools for Feedback task/page/detail, search, linked-issue, and document-update operations. Inspect their schemas. In the in-app Browser, prefer current WebMCP tools. Fetch the tool list for that tab/turn and after navigation; call only advertised operations. Verify the actor and exact task/board before a write.

For T3 browser tools, read `~/.config/osiris-agent-rules/t3-browser-profiles.md`, call `preview_status`, and explicitly select `profileId: "default"` on a new tab. For Codex's in-app Browser, use its advertised APIs and existing session. T3's profile arguments do not apply to a different tool schema. Never use personal Chrome or switch profiles to evade an access restriction.

Feedback base URL is `https://feedback.scaleadvertisement.com`. A known task link shape is `/?boardId=<board UUID>&task=<task UUID>`. Prefer the supplied URL and verify IDs against the loaded task.

## Existing routes

The installed FTI skill documents these discovery hints; recheck availability and schemas:

- `GET /api/bootstrap` identifies actor and accessible boards.
- `GET /api/tasks/<taskId>/detail` includes task, page, permissions, schedule, recurrence, and blocks.
- `GET /api/tasks/<taskId>/page` includes native document and version.
- Agent context/search operations resolve boards and related tasks; follow current pagination.

Use routes only through a supported authenticated app/API capability. Keep authentication in the session/private credential mechanism. Browser evaluation restricted to read-only DOM inspection cannot perform authenticated API requests or writes. Use WebMCP, supported direct tools, or visible UI instead of bypassing restrictions.

## Add one backlink

Prefer a native linked-issue field. Otherwise append a short rich-text paragraph with a real hyperlink, such as `GitHub implementation plan: <issue link>`. Preserve the full document, native lists, unknown attributes, and unrelated links. Read its current version immediately before saving and use the operation's request ID/version mechanism.

FTI documents versioned `PATCH /api/tasks/<taskId>/page` with `baseVersion`, `document`, `icon`, and `coverUrl`. Inspect the current supported schema and preserve existing fields. Task creation, calendar, recurrence, and renumbering operations are unnecessary for a backlink.

After actor expiry, reload the same authenticated tab once, refresh the actor, and reread before retrying the bounded edit. On conflict, merge against the fresh document. After a lost save response, inspect for the link before retrying. Stop on repeated access errors or security-policy blocks and retain the verified issue URL.

If no live route works, report the exact gap. Ask for access or task text only when needed. Text supplied by Osiris can become the accepted source, explicitly labelled as supplied text. Keep missing live verification visible in the issue and handoff.
