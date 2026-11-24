---
name: future-project
description: Use when Osiris is consuming content and thinks "this is a future project I could build." Takes any input — video, transcript, URL — extracts the build idea and saves it to the Future Projects vault.
---

# Future Project Capture

## Public setup

Resolve the user's authorized workspace before following file paths below.
`<workspace>` and named vault folders describe an existing layout, not bundled
data. Reuse equivalent files in the user's setup. Ask for a destination only
when discovery cannot resolve it. Private records and reference documents must
be supplied or located locally; do not invent their contents. Reuse answers
already in the request rather than repeating the intake. Use available supported
tools and the visible in-app Browser for browser work. Installing this skill
does not invoke it or authorize messages, publishing or unrelated service writes.

Osiris said "/future-project" or "this is a future project." Process whatever he shared, extract the build idea, save it.

## Step 1 — Get the content

- **Video file** → transcribe: `whisper "[path]" --model small --output_format txt --output_dir /tmp/`
- **Pasted transcript** → use as-is
- **URL** → WebFetch it
- **Image / screenshot** → read it visually

Nothing attached? Ask: "What are you saving?" Then wait.

## Step 2 — Extract the build idea

- **Mechanism** — what does it actually do, step by step?
- **The insight** — the thing that made him stop. The "I could build this" moment.
- **Scale relevance** — how does this apply to Scale Advertisement or his life specifically?
- **MVP shape** — smallest working version
- **Effort** — Quick win (< 1 day) / Medium (1 week) / Big project (1+ month)
- **Temperature** — 🔥 Hot (build this month) / ♨️ Warm (revisit in 60 days) / 🧊 Parked (interesting but not now)

Not sure on temperature? Ask once, then wait.

## Step 3 — Name it

Plain English. What would he call it telling a friend? No jargon.

## Step 4 — Save

Path: `<workspace>/Future Projects/[Project Name].md`

```markdown
# [Project Name]

**Source:** [Creator / URL]
**Type:** [Reel / YouTube / Article / Other]
**Captured:** [YYYY-MM-DD]
**Temperature:** [🔥 / ♨️ / 🧊]
**Effort:** [Quick win / Medium / Big project]

---

## What's Being Built
[The mechanism — what it does, how]

## The Insight
[The "oh shit" moment — why he stopped]

## Scale Relevance
[Specific to Scale Advertisement or his life]

## MVP Shape
[Smallest working version]

---

## Raw Notes
[Anything else worth keeping]
```

## Step 5 — Update the index

File: `<workspace>/Future Projects/_INDEX.md`

Add a row — most recent at top:

```
| [Project Name](ProjectName.md) | 🔥 Hot | Quick win | YYYY-MM-DD |
```

## Step 6 — Confirm back

One line: `Saved → Future Projects/[Name].md — [temperature] — [one sentence on what it is]`

No ceremony. Done means done.
