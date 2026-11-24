---
name: idea
description: Capture a raw video idea or concept and save it to the vault. Trigger immediately when Osiris says "/idea", "I have an idea", "I have a video idea", "save this idea", "log this idea", "add this to my ideas", or dumps a concept he wants to remember for content. Do NOT trigger the writer skill — this is just capture, not scripting.
---

# Idea Capture

## Public setup

Resolve the user's authorized workspace before following file paths below.
`<workspace>` and named vault folders describe an existing layout, not bundled
data. Reuse equivalent files in the user's setup. Ask for a destination only
when discovery cannot resolve it. Private records and reference documents must
be supplied or located locally; do not invent their contents. Reuse answers
already in the request rather than repeating the intake. Use available supported
tools and the visible in-app Browser for browser work. Installing this skill
does not invoke it or authorize messages, publishing or unrelated service writes.

Osiris is dropping a raw idea. Your job is to capture it cleanly and save it fast. No scripting, no analysis, no "great idea!" energy. Just get it into the vault.

## What to do

1. **If he gave you the idea inline** (e.g. `/idea the reason most agencies fail is they optimize for the wrong metric`) — save it immediately. No follow-up questions unless something is genuinely unclear.

2. **If he just said "/idea" with nothing after it** — ask: "What's the idea?" One line, then wait.

3. **Once you have the idea** — append it to `Ideas.md` in the vault root (`<workspace>/Ideas.md`). Create the file if it doesn't exist.

## Format to append

```
---
## [DATE] — [One-line title you derive from the idea]

[Clean 1-2 sentence distillation of the core insight]

**Type:** [video / insight / story / framework / rant — pick the best fit]

**Raw:** "[His exact words, verbatim]"
```

Keep the title short and punchy — it should feel like a video title draft, not a description.

## After saving

Tell him the file path and the title you gave it. One line. Done.

Example: `Saved → Ideas.md — "Why agencies optimize for the wrong metric"`

Do not summarize what you did. Do not suggest next steps unless he asks. Do not offer to turn it into a script unless he asks.
