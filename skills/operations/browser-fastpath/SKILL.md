---
name: browser-fastpath
description: Save the fastest reusable path after browser-heavy work. Use when Osiris says things like "browser fastpath", "save the fast path", "close this chat", "log this browser session", "save what you learned", "make this faster next time", "learn this workflow", or asks Codex to remember how a website/tool/browser task was handled. Especially useful after Chrome, in-app Browser, Computer Use, GoHighLevel, Meta, Slack, Google tools, authenticated SaaS, or workflow-debugging sessions.
---

# Browser Fastpath

## Purpose

Turn a messy browser session into a compact reusable operating note so the next Codex session can move faster.

This skill does not save cookies, passwords, private tokens, screenshots of sensitive data, or raw browser storage.

## Closeout Workflow

1. Identify the website, client, account, and business task.
2. List the browser surface used:
   - Use the in-app Browser for browser work, including authenticated sessions. Preserve personal Chrome and follow the active workspace browser and profile rules.
   - `Browser` for Codex in-app browser, local apps, localhost, simple unauthenticated web targets, or visible app testing.
   - `Computer Use` for desktop UI fallback when browser automation cannot reach the control.
   - `node_repl` when a plugin skill routes browser automation through the persistent JavaScript runtime.
3. Capture only reusable facts:
   - Exact URLs and IDs that matter.
   - Which tab/page is the source of truth.
   - UI locations, menu names, selectors, or button labels that were hard to find.
   - Errors, toasts, blocked actions, auth walls, iframe issues, and workaround paths.
   - Successful shortest path for next time.
   - What not to touch.
4. Save a short note when the user explicitly asked to log/learn/remember.
5. Update a domain skill if the lesson belongs there and the user asked for durable skill improvement.
6. Keep the user-facing closeout blunt: what was saved, where, and the next shortcut.

## Where To Save

For memory-style learning notes, create one small Markdown file here:

`/Users/osirismedici/.codex/memories/extensions/ad_hoc/notes/`

Filename format:

`YYYY-MM-DDTHH-MM-SS-browser-fastpath-[site-or-client].md`

Use `apply_patch` to create the file.

For domain-specific browser procedures, update the matching skill instead:

- GoHighLevel/GHL lessons: `/Users/osirismedici/.codex/skills/go-highlevel-operator/SKILL.md`
- Browser closeout process changes: this skill.

## Note Template

Use this shape and keep it short:

```markdown
# Browser Fastpath — [Site / Client / Task]

- Date: YYYY-MM-DD
- Surface used: Browser / Computer Use / node_repl
- Website/tool: [name]
- Client/account: [if relevant]
- Task: [one sentence]

## Reusable Path

- [Step 1]
- [Step 2]
- [Step 3]

## Tool Lessons

- [Which browser/tool worked and why]
- [Which browser/tool failed and why]

## UI Gotchas

- [Hard-to-find menu/button]
- [Iframe/modal/search behavior]
- [Error/toast and meaning]

## Next-Time Shortcut

- [Fastest reliable path next time]

## Do Not Do

- [Anything that wastes time or creates risk]
```

## Quality Bar

- Prefer five sharp bullets over a long diary.
- Save actions and lessons, not emotions or raw transcript.
- Do not claim a lesson is universal if it may be account-specific.
- If a fact can drift, say "current as of YYYY-MM-DD".
- If the note came from a live production tool, include the client/location/workflow ID when available.
