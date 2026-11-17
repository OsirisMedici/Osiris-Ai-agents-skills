# Feedback read access

Use purpose-built Feedback tools when available. This reference is the fallback for reading the real portfolio, not an intake or editing workflow.

- Product: `https://feedback.scaleadvertisement.com`.
- Verify the signed-in identity through the current tool or authenticated bootstrap response.
- Discover all accessible boards live. Saved board IDs and local routing maps may be incomplete.
- Paginate the entire requested board/task scope, including undated work. Record inaccessible boards and partial coverage.

If native tools are unavailable, use the signed-in in-app Browser with the persistent Default profile. Read the current user's `~/.config/osiris-agent-rules/t3-browser-profiles.md` before browser work. Reuse the appropriate tab and obey browser security boundaries. Session credentials stay in their supported store.

The authenticated in-page API documented by the existing FTI workflow provides these read operations:

- `GET /api/bootstrap` for `currentUser` and accessible boards.
- `POST /api/agent/context` with `{operation, input}`, including `get_context` and `resolve_board`.
- `POST /api/agent/tasks/search` with `{input:{scope:"selected-boards",boardIds:[...],limit:50}}`. Follow `data.nextCursor` using the live API's supported cursor field and unchanged filters until exhausted. Inspect the current response/schema before assuming optional field names.
- `GET /api/tasks/<taskId>/detail` for current task, scheduling and permissions.
- `GET /api/tasks/<taskId>/page` for its actual brief.

Use the live actor identity/header when required. POST context/search operations are reads; task create/update/delete, page edits and schedule writes are outside Right Now. Inspect current schemas if the documented shape differs. These routes are an established fallback, not proof that the current session is authenticated or that every board is accessible.

Task links are `https://feedback.scaleadvertisement.com/?boardId=<boardId>&task=<taskId>`.

If neither a native reader nor the supported signed-in Browser is available, report that live Feedback access is blocked. Preserve the verified calendar findings and explain what connection is needed. Never replace missing live tasks with remembered tasks or claim full portfolio coverage.
