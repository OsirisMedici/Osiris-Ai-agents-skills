# Live access and inventory

These are discovery hints. Prefer current tool schemas and live responses. Resolve Feedback's owning source from the authorized project registry. Source inspection alone does not establish the production revision or deployed capabilities.

## GitHub

Prefer connected repository and issue list/read tools. With authenticated GitHub CLI:

```bash
gh api user --jq '{login,id}'
gh api --paginate 'user/repos?affiliation=owner&per_page=100'
gh api --paginate 'repos/OWNER/REPO/issues?state=all&per_page=100'
```

Replace `OWNER/REPO` with the resolved repository and honor supplied state filters. Exclude entries with `pull_request`. Retain repository IDs, issue numbers, canonical `html_url`, state/reason, title/body, and existing Feedback references. Fetch details or relevant comments when needed. Enumerate explicitly scoped organization repositories with pagination too. Record archived flags and access failures without changing them.

Search helps find UUIDs and candidates but its caps make it unsuitable as the full inventory. Enumerate live ownership to find new repositories missing from the baseline. Report failures per repository and retain a resumable checkpoint.

## Feedback

Base URL: `https://feedback.scaleadvertisement.com`.

Discover board/sidebar context, task search/read/source, task creation, body-edit, board management, and detail/schedule capabilities. Verify the actor and current board/task permissions. Inspect live schemas before invoking. Known source capabilities include:

- `feedback_get_sidebar` for active and archived board identities. `feedback_list_boards` can be active-only and bounded without continuation. Source inspected on 2026-11-09 caps it at 20, which may be smaller than the accessible inventory. Never infer absence from that call alone.
- `feedback_find_tasks` with explicit scope, exact board UUIDs, and all cursors. Include done/archived tasks when supported; disclose exclusions.
- `feedback_read_tasks` and `feedback_read_task_source` for complete saved descriptions and sources. Continue truncated sections. Saved rich body wins over stale notes.
- `feedback_edit_task_body` for bounded versioned appends. Source schemas use `taskId`, `expectedPageVersion`, UUID `requestId`, and edits such as `append_section`. Confirm the operation saves clickable links. Use supported native document editing for link spans or lists the tool cannot create.
- `feedback_manage_board` for blank-board creation when advertised. Source maps this to context operation `manage_board` with input `{action:"create",name:"<verified project>"}`. Its inspected schema has no request ID. After an uncertain outcome, re-list and resolve before retrying. Read the created UUID back rather than guessing from a name.

Source hints were checked in `src/lib/feedback-webmcp-workspace-tools.ts`, `src/lib/feedback-agent-workspace-server.ts`, and `docs/agent-task-context.md`. They do not grant permission or establish deployed capabilities.

## Supported fallback

For gaps, use a supported authenticated API or the environment's in-app Browser. In T3, call `preview_status` first and use its persistent authenticated profile. Follow available browser-profile rules under the current user's configuration. Do not assume another machine's home path, extract cookies, or start a separate profile to bypass access restrictions.

Existing operating workflows document these API hints. Inspect current schemas before writes:

- `GET /api/bootstrap` for actor and accessible boards.
- `POST /api/agent/context` with `{operation,input}` for supported sidebar, context, board resolution, or management.
- `POST /api/agent/tasks/search` with `{input:{scope:"selected-boards",boardIds:[boardId],limit:50}}`. Follow `data.nextCursor` with identical filters.
- `POST /api/agent/tasks/batch` with `{operation:"create",input:{tasks:[...]}}`. Inspect task schema, request-ID support, batch limits, and every per-item result.
- `GET /api/tasks/<taskId>/page`. Versioned `PATCH` uses `{baseVersion,document,icon,coverUrl}`; preserve existing rich blocks and unknown fields.
- `GET /api/tasks/<taskId>/detail` for saved task, page, schedule, recurrence, and permissions.
- `PUT /api/calendar/tasks/<taskId>/schedule` with `{mode:"date_only"}` to clear unwanted automatic scheduling for a new undated task.

Use JSON bodies and the live actor header only through supported authenticated capabilities. Keep credentials and session data out of receipts, scripts, and output. A browser evaluation capability restricted to DOM inspection cannot be repurposed for authenticated API writes. If no supported route works, preserve the plan and report the specific blocker.

Task URL: `https://feedback.scaleadvertisement.com/?boardId=<board UUID>&task=<task UUID>`.

Board URL: `https://feedback.scaleadvertisement.com/?boardId=<board UUID>&view=table`.
