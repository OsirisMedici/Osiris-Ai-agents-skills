---
name: carousel
description: DEPRECATED — superseded by the `creative` skill (2026-04-15). Use `/creative` instead. This file is kept as reference for the Scale Advertisement 6-slide pillar-carousel format (Cover → Transition → Body × 3 → CTA). The creative skill handles Scale's own carousels by reading `Carousels/Visual Brain — Carousel System.md`.
---

# Carousel Generator

## Public setup

Resolve the user's authorized workspace before following file paths below.
`<workspace>` and named vault folders describe an existing layout, not bundled
data. Reuse equivalent files in the user's setup. Ask for a destination only
when discovery cannot resolve it. Private records and reference documents must
be supplied or located locally; do not invent their contents. Reuse answers
already in the request rather than repeating the intake. Use available supported
tools and the visible in-app Browser for browser work. Installing this skill
does not invoke it or authorize messages, publishing or unrelated service writes.

One-liner in. Full HTML carousel out. Brand-correct, export-ready, no manual filling in.

**Platform:** Claude Code writes the HTML. Opens in browser. html2canvas exports each slide as JPG.
**Output size:** 1080×1350px per slide (Instagram 4:5)
**Time to usable:** Under 2 minutes once inputs are confirmed.

---

## Step 0 — Load the brand system

Before writing any HTML, read:
`Carousels/Visual Brain — Carousel System.md`

This file contains everything: color tokens, typography rules, all 4 slide templates, 3 SVG diagram specs, the studio scaffold, and the naming convention. Do not rely on memory — read it fresh every time.

---

## Step 1 — Gather inputs

If Osiris gave a full brief → skip to Step 2.

If he gave only a topic, ask for the missing pieces in ONE message:

```
Got it. A few things before I build:

1. **Pillar** — Positioning, Ecosystem, or Bottleneck?
2. **Hook** — The provocative cover statement. What's the uncomfortable truth?
3. **Three insights** — The three things you want to teach (rough is fine — I'll sharpen them)
4. **CTA** — What's the offer or question on the last slide?

If you don't have all of these, just give me what you have and I'll fill in the rest.
```

Wait for his reply. Do not build until you have at minimum: topic + pillar + one insight.

If he says "you decide" or "fill it in" → make decisions, state them clearly, and build.

---

## Step 2 — Confirm the brief

Before building, confirm back in 4 lines max:

```
Building:
- Pillar: [X]
- Hook: "[The cover statement]"
- Insights: [A] / [B] / [C]
- CTA: [Offer or question]

Folder: Carousels/[NN] — [Title]/
```

Then build immediately — don't wait for confirmation unless something is unclear.

---

## Step 3 — Build the HTML

Write a complete, self-contained HTML file following the Visual Brain doc exactly.

**Required per the brand system:**
- Google Fonts: Space Grotesk 300–700 + Instrument Serif italic
- html2canvas 1.4.1 CDN
- Slide structure: Cover → Transition → Body × 3 → CTA
- Each slide: 1080×1350px, displayed at 0.75 scale (810×1013 preview)
- Color tokens exactly as specified (never approximate)
- Instrument Serif italic used ONLY on `.level-title` elements
- Every body slide has a BIG teaching SVG (not a small decorative one)
- Per-slide Export buttons + Download All with 700ms sequential delay
- `body { min-width: max-content; }` for horizontal scroll
- Slide IDs: `c[N]s[N]` — e.g. `c2s1`, `c2s2`... (increment carousel N from existing carousels)

**Copy rules:**
- Cover headline: 3–5 words per line, 3 lines max, provocative
- Level titles (Instrument Serif): short, lowercase, evocative — "the positioning gap" not "POSITIONING"
- Body headlines: 2–3 lines, sharp statement, Space Grotesk 700
- Body copy: 1–3 lines, muted (#bbb), explains the headline — doesn't repeat it
- CTA slide: question directed at the reader, 3 lines, lime background flip

**SVG diagrams — pick the right type per slide:**
- Scattered arrows → chaos, no direction, effort without system
- Funnel with gap → leads disappearing, no follow-up, broken pipeline
- Bar chart → conversion drop-off, proportion contrast, bottleneck callout
- Timeline/steps → process, sequence, before/after

Build all three body slides with different diagram types — never use the same type twice in one carousel.

---

## Step 4 — Save the file

Determine the next carousel number by checking what's in `Carousels/`.

Save to:
```
Carousels/[NN] — [Title]/[slug].html
```

Example: `Carousels/02 — The Positioning Gap/the-positioning-gap.html`

---

## Step 5 — Confirm back

One message:

```
Done → Carousels/[NN] — [Title]/[slug].html

6 slides. Open in browser → screenshot or use Export buttons.
[One line about what the carousel teaches — his words, not yours]
```

No summaries of what you built. No "here's what I did." Just path + slide count + one sharp line.

---

## If the output needs revision

Osiris opens the file, something's off. He describes it.

Common fixes:
- **Copy too generic** → sharpen the headlines. One idea per line. Remove anything that sounds like it was written for anyone.
- **SVG too small** → SVG should fill the bottom 40–50% of the body slide. Scale it up.
- **Colors wrong** → check hex values against Visual Brain doc. Never approximate.
- **Font not loading** → confirm Google Fonts link is in `<head>`, not in `<body>`
- **Export not working** → confirm html2canvas script is loaded before the export functions

Rewrite the affected sections and update the saved file.

---

## Carousel numbering

Check the `Carousels/` folder before assigning a number:

```bash
ls "Carousels/"
```

Use the next available two-digit number (`02`, `03`, etc.). If the folder is empty beyond `01`, start at `02`.
