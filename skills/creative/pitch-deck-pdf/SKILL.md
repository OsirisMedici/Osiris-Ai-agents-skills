---
name: pitch-deck-pdf
description: >
  Create a professional marketing pitch deck and export it as both .pptx and .pdf.
  Use this skill whenever the user wants to build a presentation, pitch deck, sales deck,
  or proposal — especially when they mention a client name, a pitch topic, marketing services,
  or say things like "make a deck", "create a presentation", "build a pitch", "I need slides for",
  or "turn this into a presentation". Also trigger when the user uploads a research report, brief,
  or notes and asks to make something visual or presentable from it.

  The skill produces a polished, branded pitch deck in the navy-and-gold executive style, with
  charts, tables, stat cards, and diagrams — then converts it to PDF automatically. Both files
  are saved to the user's workspace folder.
---

# Pitch Deck PDF Skill

## Public setup

Resolve the user's authorized workspace before following file paths below.
`<workspace>` and named vault folders describe an existing layout, not bundled
data. Reuse equivalent files in the user's setup. Ask for a destination only
when discovery cannot resolve it. Private records and reference documents must
be supplied or located locally; do not invent their contents. Reuse answers
already in the request rather than repeating the intake. Use available supported
tools and the visible in-app Browser for browser work. Installing this skill
does not invoke it or authorize messages, publishing or unrelated service writes.

Produces a professional `.pptx` + `.pdf` pitch deck from a client brief or research document.
The output matches the quality of an agency-grade presentation: dark navy/gold palette, real charts,
data tables, stat callout cards, and a logical narrative arc from problem → solution → ROI → CTA.

---

## Quick Reference

| Step | What to do |
|------|-----------|
| 1 | Gather brief (see "Inputs" below) |
| 2 | Read [slides.md](slides.md) for slide-by-slide structure |
| 3 | Read [design.md](design.md) for the full design system (colors, helpers, QA rules) |
| 4 | Write and run `build.js` using pptxgenjs |
| 5 | Convert to PDF using soffice.py |
| 6 | QA: convert to images and inspect visually |
| 7 | Fix any issues, re-export, save both files |

---

## Inputs to Gather

Before writing a single line of code, make sure you have:

- **Client name** and **business type** (mall, startup, restaurant, real estate, SaaS, etc.)
- **Pitch objective** — what are you asking the client to invest in or approve?
- **Key numbers / data** — revenue figures, market size, ROI projections, occupancy rates, etc.
- **Presenter / agency name** — who is delivering this pitch?
- **Audience** — who is sitting in the room? (investors, owners, board, clients)
- **Tone** — executive/formal, energetic/startup, minimal/clean?

If the user has uploaded a research report, strategy document, or notes — read it fully before starting. Extract numbers, narrative, and structure from it rather than inventing placeholders.

---

## Slide Structure (Standard 12-Slide Deck)

See [slides.md](slides.md) for the full content spec per slide.

The standard arc is:
1. **Cover** — Client name, tagline, presenter
2. **The Opportunity** — Market data, key stats, competitive landscape table
3. **The Problem** — Powerful statement slide identifying the gap
4. **Asset / Product Overview** — What exists, revenue potential table + bar chart
5. **Why Action Is Urgent** — Before/after comparison table + cost-of-inaction callout
6. **Strategy** — Three-track or multi-pillar approach, track cards
7. **Financial Projections** — Line chart + 3-year summary table + valuation cards
8. **Target Segments** — Who you'll reach, segment cards + doughnut chart + leads table
9. **Execution Roadmap** — 90-day or quarterly timeline, 3-column month layout
10. **Conversion Mechanics** — Funnel diagram + tactics table
11. **Investment & ROI** — Cost breakdown table + ROI scenario cards + bar chart
12. **CTA / Next Steps** — Numbered steps + urgency callout + contact

Adjust the number of slides based on the complexity of the pitch. A smaller pitch may need 8 slides; a large investor deck may need 15.

---

## Design System

See [design.md](design.md) for the complete design system reference, including:
- The full color palette (hex codes)
- All helper functions (`makeCard`, `lightCard`, `goldTag`, `slideNum`, etc.)
- Typography rules
- Layout patterns (stat cards, track cards, funnels, tables)
- QA checklist and common pitfalls

---

## Build Process

### 1. Setup

Use the host's installed presentation workflow when available. For an environment
using PptxGenJS, resolve an actual build directory and use the project's package
manager. Bun is the default for a new build: `bun init -y`, then `bun add pptxgenjs`.

### 2. Write build.js

Write a single `build.js` file. Start by pasting the full helper library from [design.md](design.md),
then add slides one at a time. Use `pres.layout = "LAYOUT_WIDE"` (13.3" × 7.5").

Key rule: **never put both slide title lines in a single `sectionTitle()` call on slides that also
have tables or charts below**. Always write them as two separate `addText()` calls with explicit
`y` positions, keeping at least 0.5" gap between the second title line and the first content element.

### 3. Run

```bash
bun run build.js
```

The file is saved to the user's workspace folder directly.

### 4. Convert to PDF

Use the host's supported presentation export or its installed LibreOffice tool.
Discover the actual executable and output directory instead of assuming a
container-specific helper path. Keep the `.pptx` and `.pdf` together.

### 5. Visual QA

```bash
rm -f slide-*.jpg
pdftoppm -jpeg -r 120 output.pdf slide
ls -1 "$PWD"/slide-*.jpg
```

Read each image. Look specifically for:
- Title lines overlapping tables or chart areas below them
- Text cut off at right edge
- Cards cramped or overflowing
- Very light text on light backgrounds

Fix issues, rebuild, reconvert, re-inspect. Do at least one full fix-and-verify cycle.

### 6. Deliver the files

Save both outputs in the authorized workspace and return usable file links.
Report what was rendered and inspected and any unavailable export capability.

## Tips for Great Pitches

- **Lead with the client's reality**, not yours. The first few slides should make them feel seen — their asset, their market, their gap.
- **Every number must come from the brief or research**, not invented. If a number is estimated, label it as such.
- **Alternate dark and light slides** — dark for statement/title moments, light for data-heavy slides. This creates visual rhythm.
- **Charts should reinforce the narrative**, not just display data. A line chart going up-and-to-the-right after the "with marketing" scenario is more compelling than a table of the same numbers.
- **The CTA slide must be specific** — exact retainer amount, exact timeline, exact next step. No vague "let's connect."
- **Keep body text short** — slides should be skimmable in 5 seconds. Put the detail in the presenter notes if needed.
