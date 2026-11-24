---
name: creative
description: Use when anyone says "/creative", "make a creative", "build a carousel for [client]", or "design an image for [client]". Generates a brand-correct HTML creative (single image or N-slide carousel, 1080×1350px) per client. Two stages — blueprint once, then copy every time. Replaces the old carousel + scene-engine skills.
---

# Creative

## Public setup

Resolve the user's authorized workspace before following file paths below.
`<workspace>` and named vault folders describe an existing layout, not bundled
data. Reuse equivalent files in the user's setup. Ask for a destination only
when discovery cannot resolve it. Private records and reference documents must
be supplied or located locally; do not invent their contents. Reuse answers
already in the request rather than repeating the intake. Use available supported
tools and the visible in-app Browser for browser work. Installing this skill
does not invoke it or authorize messages, publishing or unrelated service writes.

One skill. Per client. Any format (single image, 2-slide, 3-slide, 5-slide, whatever the copy dictates). HTML out. No Higgsfield. No Canva.

**Output:** 1080×1350px slides, self-contained HTML with html2canvas export.
**Location:** `Clients/[Client Name]/Creatives/[slug].html`

---

## How it works

Two stages. First stage runs once per client (blueprint). Second stage runs every time they want a creative (copy → HTML).

---

## Stage 1 — Blueprint (once per client)

Trigger: user runs `/creative` for a client who has no blueprint yet.

Check for an existing blueprint: `Clients/[Client Name]/Creatives/_blueprint.json`. If it exists, skip to Stage 2.

If it doesn't, ask **exactly this, nothing else**:

```
Before I build anything, I need to lock the aesthetic for [Client].

Do you have:
- An existing blueprint JSON? Paste it.
- A folder of their past creatives or reference images? Point me to it.
- Reference images on hand? Drop them in the chat.

Anything works — even one image is enough to start.
```

Wait for the reply. Then:

1. Read/analyze whatever they gave you.
2. Extract:
   - **Colors** — background, accent, text (hex)
   - **Typography personality** — descriptors only, never font names. Examples: "bold condensed sans", "elegant serif italic", "heavy geometric grotesque all-caps", "light display sans"
   - **Overlay treatment** — gradient direction + colors, shadow zones, solid blocks, none
   - **Layout preferences** — where copy sits (top/bottom/overlay), ratio of copy zone to image zone
   - **Mood adjectives** — 2–3 max (e.g. "warm, editorial, confident")
3. Write `Clients/[Client Name]/Creatives/_blueprint.json`:

```json
{
  "client": "[Client Name]",
  "created": "[YYYY-MM-DD]",
  "colors": {
    "background": "#...",
    "accent": "#...",
    "text": "#..."
  },
  "typography": {
    "headline": "[personality descriptor]",
    "subhead": "[personality descriptor]",
    "body": "[personality descriptor]"
  },
  "overlay": "[description — gradient direction + colors, or 'none']",
  "layout": "[where copy sits, ratio of copy to image zone]",
  "mood": ["adjective", "adjective", "adjective"]
}
```

4. Confirm back in one line:

```
Blueprint saved → Clients/[Client Name]/Creatives/_blueprint.json

Ready for copy.
```

Then move straight to Stage 2 — don't wait for a separate trigger.

---

## Stage 2 — Copy → Creative (every time)

Read the client's blueprint.

Ask **exactly this**:

```
Give me the copy.

- One image → describe everything you want in it (headline, sub, CTA, URL, any photo that should sit behind it).
- Carousel → give me each slide as a separate block. However many blocks, that's how many slides.

If you want a photo in the background, drop it here or give me the path.
```

Read their reply and detect structure:
- **One block** → single static image
- **N blocks separated by blank lines or `---`** → N-slide carousel

Build the HTML using the blueprint. Every slide:
- 1080×1350px (displayed at 0.75 scale = 810×1013 preview)
- Colors straight from blueprint — never approximate
- Typography personality mapped to real font stacks:
  - "bold condensed sans" → `'Space Grotesk', sans-serif; font-weight: 700`
  - "elegant serif italic" → `'Instrument Serif', serif; font-style: italic`
  - "heavy geometric grotesque all-caps" → `'Space Grotesk', sans-serif; font-weight: 700; text-transform: uppercase; letter-spacing: 0.02em`
  - "thin serif italic" → `'Instrument Serif', serif; font-style: italic; font-weight: 300`
  - "light display sans" → `'Space Grotesk', sans-serif; font-weight: 300`
- Background photo → CSS `background-image` with gradient overlay for text legibility (match blueprint overlay)
- Per-slide Export button + Download All button (700ms sequential delay)
- `body { min-width: max-content; }` for horizontal scroll in browser
- Google Fonts in `<head>` — Space Grotesk 300–700 + Instrument Serif italic
- html2canvas 1.4.1 CDN
- Export clones the slide, strips `transform: scale(0.75)`, renders at native 1080×1350

Slide IDs: `s1, s2, s3...`.

---

## Save and report

Determine the slug from the copy (2–4 words, kebab-case). Save to:

```
Clients/[Client Name]/Creatives/[slug].html
```

Report in one message, nothing more:

```
Done → Clients/[Client Name]/Creatives/[slug].html

[N] slide[s]. Open in browser → hit Export or Download All.
```

No summaries. No "here's what I did."

---

## Revision loop

User opens the file, something's off. They tell you in plain words.

Common fixes:
- **Text too small / too big** → adjust font-size in the relevant slide
- **Wrong color** → check against blueprint, fix the hex
- **Font feels wrong** → remap the personality descriptor to a different Google Font stack
- **Photo washed out** → deepen gradient overlay
- **Layout off** → adjust copy zone position per blueprint.layout

Edit the HTML file directly. Don't regenerate from scratch.

If the *blueprint itself* is wrong (happens on first client setup), update the JSON and re-run Stage 2.

---

## Rules

- **Never** use a template library. Every HTML file is self-contained.
- **Never** open Higgsfield, Canva, or any external tool. Claude Code does everything.
- **Never** approximate colors. Copy hex from blueprint.
- **Never** ask the team for the format. Detect it from the copy structure.
- **One question per stage.** Stage 1 asks once for references. Stage 2 asks once for copy. That's it.
- If the team says "you decide" → decide, state it in one line, build.

---

## For Scale Advertisement itself

Scale has its own blueprint. If user runs `/creative` without a client, assume Scale and use:
- Colors: bg `#0a0a0a`, accent `#D9FC67` (lime), text `#ffffff`
- Typography: headline "bold condensed sans" (Space Grotesk 700), level-titles "elegant serif italic" (Instrument Serif), body "light display sans" (Space Grotesk 300)
- Overlay: none (dark bg is the overlay)
- Mood: sharp, provocative, editorial

Save Scale's own creatives to `Carousels/[NN] — [Title]/[slug].html` (existing convention — check folder for next number).

Reference doc for Scale brand specifics: `Carousels/Visual Brain — Carousel System.md`.
