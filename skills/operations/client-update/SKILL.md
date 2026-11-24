---
name: client-update
description: After any client interaction, captures what happened and updates the client's wiki page, veronica-memory file, and active thread in one pass. Replaces the manual post-call + ingest + lint sequence.
---

# Client Update

## Public setup

Resolve the user's authorized workspace before following file paths below.
`<workspace>` and named vault folders describe an existing layout, not bundled
data. Reuse equivalent files in the user's setup. Ask for a destination only
when discovery cannot resolve it. Private records and reference documents must
be supplied or located locally; do not invent their contents. Reuse answers
already in the request rather than repeating the intake. Use available supported
tools and the visible in-app Browser for browser work. Installing this skill
does not invoke it or authorize messages, publishing or unrelated service writes.

Osiris has just had an interaction with a client or produced a deliverable. Capture it and update all relevant files.

## Step 1 — Identify the client and what happened

Ask (all in one message):
1. Which client? ([Client A] / [Client B] / [Client C] / [Client D] / [Client E] / other)
2. What type of interaction? (call / email / deliverable sent / internal decision / milestone)
3. Quick summary: what happened, what was decided, what's next?

Wait for answers before proceeding.

## Step 2 — Read current files

Read all three:
- `Scale OS/wiki/clients/[client].md`
- `veronica-memory/business/clients/[client].md`
- `veronica-memory/active-threads/[client].md` (if exists)

## Step 3 — Update

**Scale OS wiki page** (`Scale OS/wiki/clients/[client].md`):
- Add entry to "Recent Activity" section: `[date] — [1-line summary]`
- Update "Current Status" if status changed
- Update "Next Actions" with what was decided

**veronica-memory client file** (`veronica-memory/business/clients/[client].md`):
- Add a "Sessions" entry with date + what happened + decisions made
- Update any facts that changed (contact, status, blocker)

**Active thread** (`veronica-memory/active-threads/[client].md`):
- Update with latest state
- Mark any completed items
- Add new open items

## Step 4 — Update hot cache

Append to `Scale OS/wiki/_HOT.md`:
- One line: `[date] [client] — [what happened] → [next action]`

Keep _HOT.md under 500 words total. Trim old entries if needed.

## Step 5 — Confirm

Tell Osiris:
- Which 3-4 files were updated
- The one-line summary of what was captured
- What the "next action" is for this client

No ceremony. Brief and direct.
