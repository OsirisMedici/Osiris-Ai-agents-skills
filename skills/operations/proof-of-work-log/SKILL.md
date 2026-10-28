---
name: proof-of-work-log
description: "Generate copy-paste-ready proof logs using Scale's Communication template: Title, Domain / Area, What Exactly Happened, What We Did, Outcome, and Proof of work screenshots. Use when the user says document this, proof log, proof of work, client update, team update, save what we did, summarize the task, log this, or after browser/GHL/Gmail/Notion/Slack/client-ops work that needs a reusable communication record with screenshot previews. Default to giving the proof log in chat; only publish to Notion when explicitly asked."
---

# Proof of Work Log

Use this skill to turn completed operational work into a copy-paste-ready proof log.

The default output is a clean chat block the user can paste into Notion, Slack, a doc, or any client workspace.

Do not operate Notion by default. Only publish to Notion when the user explicitly asks.

## Default Template

Always follow this template:

- `Title`
- `Domain / Area`
- `What Exactly Happened`
- `What We Did`
- `Outcome`
- `Proof of work (screenshots)`

Keep the exact labels unless the user gives a different template.

## Output Rule

- Give the finished proof log directly in chat.
- Make it copy-paste-ready.
- Include screenshot images using Markdown image syntax when local image paths exist.
- Use absolute local paths in image tags so Codex can render previews in chat.
- Do not paste raw screenshot paths as the main proof.
- Put backup file paths only when the user asks for evidence locations.
- Keep the language plain, calm, and operational.
- Use bullets only when they make the proof easier to scan.

## Optional Notion Destination

Only use this when the user explicitly asks to publish, create, or update a Notion item.

Resolve the user's intended proof-log board and its `communication` template from the connected Notion workspace. Confirm the board, template, and current data source before writing. Keep their account-specific IDs outside this skill.

Load `references/notion-database.md` only when publishing to Notion.

## Workflow

1. Identify the capture mode.

- Team update: internal, direct, exact proof.
- Client update: calm, client-safe, no internal blame or tool chatter.
- Both: include internal proof plus a separate client-safe section.

2. Reconstruct the work.

- Name the task.
- Name the client or project.
- List systems touched.
- Capture the start state.
- Capture the completed state.
- List anything blocked or partially complete.
- Estimate time saved only when there is a clear manual baseline.

3. Gather proof.

- Use existing evidence folders when the task already created one.
- For new evidence, create a dated folder under the client or operating-system area.
- Name screenshots with ordered purpose labels: `01-ghl-execution-log.png`, `02-gmail-category-proof.png`.
- Prefer raw proof over vibes: URLs, IDs, screenshots, headers, logs, reports, exports, local file paths.
- Do not screenshot secrets, tokens, cookies, payment details, or private personal data unless the user explicitly asks and it is necessary.

4. Write the proof log in the template shape.

```markdown
### Title

Completed work title.

### Domain / Area

GHL, WhatsApp automation, Slack recovery, reporting.

### What Exactly Happened

The starting problem, the system behavior that caused confusion, and the client or team impact.

### What We Did

The concrete changes made, systems touched, owners or routes created, and anything intentionally left unchanged.

### Outcome

Current status, result produced, and remaining action if any.

### Proof of work (screenshots)

Short screenshot label:

![Screenshot label](/absolute/path/to/screenshot.png)
```

5. Screenshot handling.

- In chat, use Markdown image embeds with absolute paths.
- For Notion paste, give screenshot labels plus image embeds so the user can paste or drag as needed.
- If Notion refuses local image embeds, tell the user to paste the screenshot files under the section; do not keep fighting the UI.
- Never represent screenshot proof as only a code-formatted path.

6. Final handoff.

- Return the proof log in chat.
- Return the Notion URL only if it was published.
- Return the evidence folder path only when useful.
- Name the next owner and next step when there is one.

## Publishing To Notion

If the user explicitly asks to publish to Notion:

- Create or update an item in `Scale Client's Work`.
- Use the `communication` template.
- Parent it under the live data source resolved for the intended board.
- Set `Energy Block` to `["Communication"]`.
- Set `Executor` to `Codex` when the agent did the work, `Team` when it is a human task, or the named owner when the user gives one.
- Set `Progress` to `Done` only when the work is actually complete.
- Set `Firm Name` to the client name when it exists in the select list.
- If image upload through MCP is unavailable, leave the text clean and tell the user which screenshots to paste under `Proof of work`.

Do not add many custom fields for proof logging. Use the page body.

## Quality Bar

- Do not confuse tool execution with real completion.
- Do not say "delivered" when the system only says "executed."
- Do not say "fixed" when the result is only diagnosed.
- Do not bury a blocker in a paragraph.
- Separate internal and client-safe language.
- Keep client-safe sections calm and factual.
- Keep internal sections exact enough that another operator can continue the task.
- Default to chat-first proof logs.
- Use the `communication` template labels.
- Screenshot proof must render as images in chat when files are available.
- Notion work is optional and explicit, not automatic.
