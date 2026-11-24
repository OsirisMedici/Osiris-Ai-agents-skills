---
name: knowledge-capture
description: Save knowledge from any source — YouTube videos, articles, podcast transcripts, book notes — into the Knowledge Base vault. Trigger when Osiris shares a URL with intent to save it, says "/learn", "/kb", "/capture", "save this", "add this to the knowledge base", or pastes content he wants captured. Do NOT trigger for general browsing or research — only when he explicitly wants to save something to the knowledge base.
---

# Knowledge Capture

## Public setup

Resolve the user's authorized workspace before following file paths below.
`<workspace>` and named vault folders describe an existing layout, not bundled
data. Reuse equivalent files in the user's setup. Ask for a destination only
when discovery cannot resolve it. Private records and reference documents must
be supplied or located locally; do not invent their contents. Reuse answers
already in the request rather than repeating the intake. Use available supported
tools and the visible in-app Browser for browser work. Installing this skill
does not invoke it or authorize messages, publishing or unrelated service writes.

Osiris is saving something to the knowledge base. Your job is to extract everything useful, structure it cleanly, and file it in the right place. Fast, no ceremony.

## Step 1 — Identify the source type

- **YouTube URL** → WebFetch the URL to get title, description, transcript if available
- **Article URL** → WebFetch the URL and extract full content
- **Podcast transcript / book notes / raw text** → he'll paste it inline
- **No content yet** → ask "What are you saving?" then wait

## Step 2 — Identify the topic

Look at the content and determine the best topic folder. Common topics:

- `Sales` — closing, objections, funnels, sales psychology
- `Marketing` — positioning, messaging, ads, content strategy
- `Psychology` — behavior, persuasion, decision-making, human nature
- `Business` — systems, operations, hiring, growth, equity
- `Leadership` — management, culture, team dynamics
- `Mindset` — identity, habits, performance, mental models
- `Copywriting` — writing, hooks, headlines, story
- `Design & Architecture` — industry-specific knowledge relevant to Scale's clients
- `Finance` — money, pricing, investment, wealth

If none fit cleanly, create a new topic folder that makes sense. If you can't tell, ask: "What topic does this belong to?" One question, then wait.

## Step 3 — Extract everything

Pull all of this from the content:

### Source metadata
- Title
- Creator / Author / Channel
- Source type (YouTube / Article / Podcast / Book / Other)
- URL (if applicable)
- Date saved

### Summary
2-3 sentences. What's the core argument or point of this piece?

### Key Frameworks
Any named models, systems, or structured ways of thinking the creator introduces. If they name it, use their name. If they don't, name it yourself in brackets.

### Direct Quotes
The best lines — things that are quotable, sharp, or surprising. Use the creator's exact words. Pull at least 3-5 if they exist.

### Tactical Takeaways
Concrete things you can DO with this knowledge. Specific, actionable, no fluff.

### Raw Notes
Anything else worth preserving — context, nuance, examples, tangents that might matter later.

## Step 4 — Save the file

**Path:** `<workspace>/Knowledge Base/[Topic]/[Source Title].md`

Create the topic folder if it doesn't exist.

**Also save a summary entry to Scale OS wiki sources:**

Path: `Scale OS/wiki/sources/[Source Title].md`

Format:
```markdown
# [Title]
**Source:** [Creator] | **Type:** [Type] | **Saved:** [Date]
**Full notes:** `Knowledge Base/[Topic]/[Source Title].md`

## 2-Line Summary
[Core argument in 2 sentences max]

## Top 3 Takeaways
- [Takeaway 1]
- [Takeaway 2]
- [Takeaway 3]
```

This keeps the wiki sources index lean while the full extract lives in Knowledge Base.

**File format:**

```markdown
# [Title]

**Source:** [Creator / Channel / Author]
**Type:** [YouTube / Article / Podcast / Book / Other]
**URL:** [URL or "N/A"]
**Saved:** [Date]

---

## Summary

[2-3 sentence summary of the core argument]

---

## Key Frameworks

### [Framework Name]
[Explanation of the framework in plain language]

### [Framework Name]
[Explanation]

---

## Direct Quotes

> "[Exact quote]"
> — [Creator name]

> "[Exact quote]"

---

## Tactical Takeaways

- [Specific actionable thing]
- [Specific actionable thing]
- [Specific actionable thing]

---

## Raw Notes

[Anything else — context, examples, nuance, tangents worth keeping]
```

## Step 5 — After saving

Tell Osiris:
- Full extract path in Knowledge Base
- Summary path in Scale OS/wiki/sources/
- Topic folder it went into
- One-line summary of what got captured

Example:
- `Knowledge Base/Sales/Alex Hormozi — How to Close Without Pressure.md`
- `Scale OS/wiki/sources/Alex Hormozi — How to Close Without Pressure.md`
- Hormozi's 3-part reframe for objection handling.

That's it. No "great resource!" energy. No suggestions unless he asks.

## Edge cases

- **Video with no transcript available:** Extract from title + description + any text on the page. Note at the top: `[Transcript not available — extracted from title and description]`
- **Long article or book notes:** Don't truncate. Capture everything. The point is a complete record.
- **Multiple URLs at once:** Save each as a separate file. Tell him all file paths at the end.
- **He's unsure of the topic:** Default to the most likely fit, tell him which folder you put it in, and say "move it if that's wrong."
