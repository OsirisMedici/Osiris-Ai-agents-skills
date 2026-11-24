---
name: ingest
description: Scale OS ingest — processes raw content dropped into Scale OS/raw/ and organizes it into the wiki. Trigger when Osiris says "/ingest", "ingest this", "process the raw folder", or drops content and says "add this to the wiki" or "add this to Scale OS".
---

# Scale OS — Ingest

## Public setup

Resolve the user's authorized workspace before following file paths below.
`<workspace>` and named vault folders describe an existing layout, not bundled
data. Reuse equivalent files in the user's setup. Ask for a destination only
when discovery cannot resolve it. Private records and reference documents must
be supplied or located locally; do not invent their contents. Reuse answers
already in the request rather than repeating the intake. Use available supported
tools and the visible in-app Browser for browser work. Installing this skill
does not invoke it or authorize messages, publishing or unrelated service writes.

Osiris has dropped content into `Scale OS/raw/` or is sharing something to be processed into the wiki. Your job is to read it, understand it, and file it correctly.

## Step 1 — Identify what's in raw/

Read the contents of `<workspace>/Scale OS/raw/`. List what's there. If nothing is there, ask: "What do you want to ingest? Drop it in raw/ or paste it here."

## Step 2 — Read and understand the content

For each file in raw/:
- Read the full content
- Identify: What is this? (call transcript / article / EOD update / framework / meeting notes / other)
- Identify: What is it ABOUT? (client / team / concept / framework / Osiris / Scale)
- Identify: What relationships does it have? (mentions a client, references a framework, connects to an active thread)

Ask clarifying questions if needed — but batch them. One message with all your questions, not sequential.

## Step 3 — Decide where it goes

Wiki folder targets:
- `wiki/clients/[ClientName].md` — update or create a client page
- `wiki/people/[Name].md` — update or create a person page
- `wiki/frameworks/[FrameworkName].md` — update or create a framework page
- `wiki/concepts/[ConceptName].md` — a new idea or concept worth capturing
- `wiki/sources/[Title].md` — a source document (article, video, research) — use this when it doesn't fit neatly into the above

If content spans multiple categories, create multiple pages with cross-links.

## Step 4 — Write the wiki page(s)

### For a client update:
Update the existing client page in `wiki/clients/`. Add new info. Update status. Note the date.

### For a new source (article, video, call transcript):
Create a new file in `wiki/sources/`. Format:

```markdown
# [Title]

**Type:** [Call transcript / Article / YouTube / EOD / Meeting notes / Other]
**Date:** [Date of content]
**Ingested:** [Today's date]
**Related:** [[clients/X]], [[frameworks/Y]], [[people/Z]]

---

## Summary
[2-3 sentences. Core insight or what happened.]

## Key Takeaways
- [Specific, concrete point]
- [Specific, concrete point]

## Raw Notes
[Anything else worth preserving — context, nuance, quotes, decisions made]
```

### For a new concept:
Create `wiki/concepts/[ConceptName].md`. Keep it tight — one idea, its relationships, how it applies.

## Step 5 — Update the index and log

After creating/updating pages:

1. **Update `_INDEX.md`** — add any new pages to the right section with a one-line description
2. **Update `_LOG.md`** — add an entry at the top:
```
## [Today's Date]
**Action:** Ingested [filename]
**What was created/updated:** [list of pages]
**Source type:** [type]
```
3. **Update `_HOT.md`** if the content contains something that should be in immediate context (recent decision, active blocker, new client development)

## Step 6 — Move processed files

After a file in raw/ has been successfully ingested, move it to `Scale OS/raw/processed/` (create this folder if it doesn't exist). Don't delete — archive.

## Step 7 — Report back

Tell Osiris:
- What you ingested
- What pages were created or updated (with file paths)
- Any relationships you found that weren't obvious
- Any gaps you noticed while reading

One message. No ceremony. Just the facts.

## Edge Cases

- **Call transcript with multiple clients mentioned:** Create/update the primary client's page. Reference the other client by name. Don't split the context.
- **EOD update from team:** Update relevant client pages + team page. Log it.
- **Article or YouTube video:** Goes in `wiki/sources/`. Also update any concept or framework pages it connects to.
- **Something you can't categorize:** Ask Osiris before filing it anywhere.
