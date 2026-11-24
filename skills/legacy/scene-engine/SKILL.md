---
name: scene-engine
description: DEPRECATED — superseded by the `creative` skill (2026-04-15). The HTML+CSS output from `/creative` replaces the Higgsfield compositing flow. Use `/creative` instead. Kept for reference only.
---

# Scene Engine

## Public setup

Resolve the user's authorized workspace before following file paths below.
`<workspace>` and named vault folders describe an existing layout, not bundled
data. Reuse equivalent files in the user's setup. Ask for a destination only
when discovery cannot resolve it. Private records and reference documents must
be supplied or located locally; do not invent their contents. Reuse answers
already in the request rather than repeating the intake. Use available supported
tools and the visible in-app Browser for browser work. Installing this skill
does not invoke it or authorize messages, publishing or unrelated service writes.

Conversation-only pipeline. No files saved. Everything happens in chat.

Team drops a project image. Veronica reads the blueprint library, suggests styles, refines through back-and-forth, outputs two prompts ready for Higgsfield.

**Platform:** Higgsfield — model: Nano Banana 2
**Input at runtime:** Project photo (@image2) + prompt (generated here)
**Reference images:** Not needed — replaced by blueprints

---

## Step 0 — Load learnings and client brand guide

Before anything else:
1. Read `Scene Engine/_learnings.md`. Apply every confirmed learning to this session automatically. Don't mention this step to the team.
2. If a client is mentioned or a client folder is referenced, check for `Clients/[client-name]/Creatives/_brand-guide.md`. If it exists, read it silently and override these defaults:
   - Use the brand guide's specified fonts instead of generic font descriptions
   - Use the brand guide's copy voice for headline suggestions
   - Note any logo/badge instructions from the guide

Don't mention this step to the team.

---

## Step 1 — Ask for inputs

Ask for:
- Project photo (required — @image2)
- Client — which client is this for? (optional — if provided, loads their brand guide automatically)
- Copy — headline, sub, CTA, URL (optional — will generate suggestions if missing)
- Context — mood, placement preferences, things to avoid, format preference (optional)

Don't move to Step 2 until the project photo is in the chat.

---

## Step 2 — Read blueprints

Read all files in `Scene Engine/blueprints/`.

For each blueprint extract:
- Style name (from filename)
- Images indexed count
- Mood adjectives
- Signature characteristics
- Layout description (one-sentence summary)

If blueprints/ is empty or no files found:
→ Tell team: "No blueprints indexed yet. Drop reference images into Scene Engine/library/ and run /blueprint-index first."
→ Stop.

---

## Step 3 — Show blueprint menu

Display all available blueprints as a numbered menu.

Format per item:
```
[N]. [Style Name]  ([X] images indexed)
     [Mood adjectives] — [one-line layout description]
     Signature: [characteristic 1], [characteristic 2]
```

After the menu, ask:
"Which style do you want to work with? Pick a number — or tell me what feeling you're going for and I'll suggest the closest match."

---

## Step 4 — Analyze the project photo

Once a blueprint is selected, silently analyze @image2:

- Dominant geometry and materials
- Color temperature and palette
- Lighting quality and direction
- Best visible angle
- Any elements that might conflict with the chosen blueprint's style
- Aspect ratio of the photo

Note any conflicts between the photo and the blueprint — these will need to be resolved in the prompt.

---

## Step 5 — Back-and-forth refinement (4-5 rounds max)

Each round, ask ONE focused question to lock a variable.

Priority order:
1. Copy — if not provided, ask for headline + subheadline. If team doesn't have it, generate 2-3 options and ask them to pick or adjust.
2. Format — portrait (4:5), square (1:1), or landscape (16:9)?
3. Placement — any specific preferences for where the building sits vs where copy sits?
4. Mood adjustment — does the blueprint match exactly or should it skew warmer/colder/bolder?
5. Negatives — anything specific to avoid (AI-looking building, cluttered layout, specific colors)?

Rules:
- One question per round, not multiple
- If team says "you decide" → make a decision, state it clearly, move on
- After round 4 or 5 → lock all variables and move to output regardless

---

## Step 6 — Output the prompt

One JSON prompt only. This is the confirmed format — complete ad creative, image preserved, text integrated, no Canva or post-processing needed.

**Do not describe room details in the prompt — this causes Higgsfield to regenerate the space. Only describe tone treatment and typography.**

### Higgsfield JSON — Confirmed Format

```json
{
  "model": "Nano Banana 2",
  "task": "advertisement creative",
  "background": {
    "image": "@image2",
    "instruction": "use @image2 as the exact background photograph — do not regenerate, alter, or reinterpret the space in any way",
    "treatment": "[tone adjustment from blueprint — e.g. 'deepen warm amber, enrich shadow depth in lower half, preserve existing lighting exactly']"
  },
  "format": {
    "orientation": "[portrait/landscape/square]",
    "ratio": "[4:5 / 1:1 / 16:9]",
    "crop": "center crop @image2 to [ratio]"
  },
  "typography": {
    "headline": {
      "text": "[EXACT HEADLINE]",
      "font": "[font personality from blueprint — e.g. 'elegant display serif light italic' or 'bold condensed sans']",
      "size": "large — approximately 1/8 of frame height",
      "color": "warm ivory #F5EDD8",
      "position": "horizontally centered, bottom quarter of frame",
      "alignment": "center",
      "letter_spacing": "wide",
      "line_height": "relaxed"
    },
    "subheadline": {
      "text": "[EXACT SUBHEADLINE]",
      "font": "light sans-serif",
      "size": "small — approximately 1/24 of frame height",
      "color": "warm white",
      "position": "centered directly below headline",
      "alignment": "center"
    },
    "badge": {
      "text": "[URL]",
      "font": "light sans-serif",
      "size": "very small",
      "color": "warm white",
      "position": "top-right corner, 40px inset"
    }
  },
  "design": {
    "text_background": "none — text sits directly on image in natural shadow zone, model handles gradient legibility",
    "text_color_temperature": "warm ivory and cream — not cold white",
    "composition": "photograph is the hero, typography is designed into it — not overlaid as an afterthought"
  },
  "style": {
    "mood": "[mood adjectives from blueprint]",
    "quality": "magazine quality, cinematic editorial"
  },
  "negative": "do not regenerate or alter @image2, do not change the architecture or interior, no cold white text, no text background blocks, no text boxes, no border, no vignette, no AI-generated elements"
}
```

---

**Non-negotiable rules for this format:**
- `"task": "advertisement creative"` — always present, reframes prompt as layout not generation
- Never describe the room or building in the prompt body — triggers regeneration
- Text color is always warm ivory `#F5EDD8` — never cold white (exception: monochrome-editorial blueprint — can use black text on white zones)
- Text always center-aligned, bottom quarter — never hard left corner
- No background blocks behind text — model handles legibility naturally via shadow zone

---

## Font Personality Matrix

Use these descriptors in the `"font"` field — never use actual font names (the model reads aesthetic intent, not font catalogs):

| Copy Type | Descriptor | Blueprints |
|---|---|---|
| Philosophical / emotional | `elegant display serif light italic` | warm-residential, minimal-clean |
| Declarative / bold | `bold condensed sans-serif` | warm-residential, cinematic-exterior |
| Prestige / ultra-luxury | `thin serif italic, wide letter-spacing` | luxury-dark-prestige |
| Editorial / journalistic | `heavy geometric grotesque all-caps` (masthead) + `editorial italic serif` (headline) | monochrome-editorial |
| Versatile default | `light display sans-serif` | any |

**Rule:** If the headline is philosophical (abstract, evocative, poetic) → use serif italic. If the headline is declarative (direct, confident, statement) → use bold sans.

---

## Higgsfield Image Strength Guidance

After generating, if the architecture is being altered or regenerated:
- Increase **Structure Strength** slider toward 1.0
- Increase **Image Strength** slider toward 1.0 (keeps the input image dominant)
- These sliders live in the Higgsfield interface, not in the JSON — but note them in output so team knows

Add this line at the end of the JSON output:

```
// Higgsfield settings: set Image Strength → 0.85–0.95, Structure Strength → 0.8–0.9 if architecture is being altered
```

---

After outputting the prompt, ask one question:

"Anything to adjust before you run it?"

---

## If Output Needs Revision

Team pastes the result back into chat, describes what's off.

Common fixes:
- **Room was regenerated** — the prompt described room details; remove all room description from body, keep only `background.treatment`
- **Text rendered wrong** — shorten copy, fewer words render more accurately
- **Text still cold/white** — re-specify `"color": "warm ivory #F5EDD8"` explicitly
- **Text cornered** — re-specify `"position": "horizontally centered, bottom quarter of frame"` and `"alignment": "center"`
- **Higgsfield keeps altering image** — increase image strength / structure strength slider inside Higgsfield toward 1.0
- **Wrong style feel** — go back to blueprint menu and try a different one

Rewrite and output the updated version in chat.

---

## When feedback is received — always log it

After any feedback on a creative output, append a new entry to `Scene Engine/_learnings.md`.

Format:

```
## Session: [date] — [client/project name]

### Round [N]

**My output:**
[The exact prompt or key decisions I made]

**Feedback received:**
[Exact words from Osiris or team]

**What I understood:**
[What the feedback revealed — what was wrong, what the fix is, what principle applies going forward]
```

Then update the Learnings Index table at the bottom of the file with any new confirmed principles.

This file makes the system smarter with every creative. Never skip logging.
