---
name: capture
description: Use when Osiris says "/capture" or "capture this" or "save that insight" — preserves key insights from the current conversation into Knowledge Base/Osiris — Insights/ in his voice and words. Do NOT trigger for client insights, general knowledge, or task logging — this is specifically for Osiris's own thinking, frameworks, and named patterns.
---

# Insight Capture

## Public setup

Resolve the user's authorized workspace before following file paths below.
`<workspace>` and named vault folders describe an existing layout, not bundled
data. Reuse equivalent files in the user's setup. Ask for a destination only
when discovery cannot resolve it. Private records and reference documents must
be supplied or located locally; do not invent their contents. Reuse answers
already in the request rather than repeating the intake. Use available supported
tools and the visible in-app Browser for browser work. Installing this skill
does not invoke it or authorize messages, publishing or unrelated service writes.

Osiris said something worth keeping. Your job is to pull the real insight out of the conversation, preserve it in his voice, and file it in the right place. Fast. No analysis energy. No "great insight!" energy. Just capture it and confirm.

---

## Two Modes

**`/capture` with no argument** — scan the recent conversation (last 5–10 messages) and pull every insight worth keeping. Can be multiple entries. Save them all.

**`/capture [specific thing]`** — save exactly what he described. No interpretation. His words.

---

## How to identify what's worth capturing

Not everything in a conversation is an insight. Capture when:

- He names a pattern he's noticed about himself, business, or human behavior
- He articulates *why* something works or fails (not just that it does)
- He gives a framework — even a rough one — for thinking about a problem
- He says something that surprised even him as he said it
- He describes a distinction that most people would miss

Do NOT capture:
- Task status or to-do items (that's for Top-Priorities)
- Client-specific context (that's for client files)
- Generic knowledge from external sources (that's for knowledge-capture skill)
- Things he's already said before that are already in memory

---

## Where to save

Base path: `<workspace>/Knowledge Base/Osiris — Insights/`

Create the folder if it doesn't exist. Save to the file that matches the category:

| Category | File | Use for |
|---|---|---|
| Business | `Business Strategy.md` | Agency growth, pricing, positioning, client dynamics |
| Psychology | `Psychology & Patterns.md` | Mindset, procrastination, fear, self-awareness, identity |
| Systems | `Systems Thinking.md` | How to build things that work without willpower |
| Marketing | `Marketing & Positioning.md` | Content, distribution, audience, messaging |
| Identity | `Identity & Vision.md` | Who Osiris is, what he's building toward, life philosophy |

If the file doesn't exist yet, create it with a simple header:
```markdown
# [Category Name]
*Osiris's frameworks and named patterns — captured in his words.*

---
```

If the insight spans multiple categories, pick the dominant one.

---

## Entry format

Append to the end of the correct file:

```markdown
## [YYYY-MM-DD] — [Sharp title you derive from the insight — 5–8 words max]

**In his words:** "[The insight as close to his exact phrasing as possible. If he rambled to get there, clean it up but keep his voice — not yours.]"

**Why it matters:** [One line. What changes because of this insight — operationally or philosophically.]

---
```

Title should sound like a chapter heading in a book Osiris would write, not a document name.

**Voice rule:** If the entry sounds like something an assistant wrote about Osiris, rewrite it. It should sound like something Osiris said. His voice is direct, a little compressed, no fluff.

---

## After saving

One line back to him:

`Captured → [File name] — "[Title you gave it]"`

If multiple entries: list them all, one per line.

Do not summarize what you saved. Do not ask if he wants to do anything with it. Do not suggest next steps. Done means done.

---
