---
name: lint
description: Scale OS health check — audits the wiki for staleness, gaps, orphaned files, and missing relationships. Trigger when Osiris says "/lint", "run a health check", "audit the wiki", or "what's stale in Scale OS".
---

# Scale OS — Lint

## Public setup

Resolve the user's authorized workspace before following file paths below.
`<workspace>` and named vault folders describe an existing layout, not bundled
data. Reuse equivalent files in the user's setup. Ask for a destination only
when discovery cannot resolve it. Private records and reference documents must
be supplied or located locally; do not invent their contents. Reuse answers
already in the request rather than repeating the intake. Use available supported
tools and the visible in-app Browser for browser work. Installing this skill
does not invoke it or authorize messages, publishing or unrelated service writes.

Run a full health check on the Scale OS wiki. Find what's stale, what's missing, what's broken, and what connections are missing.

## Step 1 — Read the index

Read `Scale OS/wiki/_INDEX.md`. This is the master map. Everything in the wiki should be reachable from here.

## Step 2 — Check for staleness

For each file in the wiki, check the "Last Updated" date (if present). Flag anything:
- **Not updated in 30+ days** — likely stale
- **References a status that may have changed** (e.g., "pending" tasks that are now old)
- **References people, clients, or projects that may no longer be active**

## Step 3 — Check for orphaned pages

Look through all wiki files. Flag any page that:
- Is NOT linked from `_INDEX.md`
- Has no backlinks from other wiki pages
- Has no "Connected Notes" or "Related" section

These are orphaned — they exist but can't be found.

## Step 4 — Check for gaps

Based on what you know about Scale Advertisement, flag missing pages:
- Is there a client who has no wiki page?
- Is there a framework mentioned in client pages that doesn't have its own page?
- Is there a team member mentioned in multiple places with no person page?
- Is there a concept that's repeated across multiple files but never captured as its own page?

## Step 5 — Check raw/

Read `Scale OS/raw/`. If there are unprocessed files in here (not in raw/processed/), flag them. These should have been ingested.

## Step 6 — Check _HOT.md

Read `_HOT.md`. Is it current? If it references things from more than 2 weeks ago as "recent", it needs updating. Flag it.

## Step 7 — Check _BRIEF.md

Read `veronica-memory/_BRIEF.md`. Is it current? If it's more than 5 days old, flag it. (This is also enforced at session start — just adding it to the lint pass.)

## Step 8 — Report back

Deliver a clean audit report:

```
## Scale OS Lint Report — [Date]

### Stale Files
- [file] — last updated [date], may be stale: [reason]

### Orphaned Pages
- [file] — not linked from index

### Gaps (Missing Pages)
- [description of what's missing and why it should exist]

### Unprocessed Raw Files
- [filename] — in raw/ but not processed

### Hot Cache
- [current / stale — reason]

### Priority Fixes
1. [most important thing to fix]
2. [second most important]
3. [third]
```

Keep it tight. No padding. Just what needs attention and in what order.

## After the report

Ask: "Want me to fix any of these now?" Then do exactly what Osiris says.
