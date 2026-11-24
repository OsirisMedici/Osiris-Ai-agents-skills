---
name: blueprint-index
description: DEPRECATED — superseded by the `creative` skill (2026-04-15). Blueprints are now generated per-client inside `/creative` (Stage 1) and saved to `Clients/[Client]/Creatives/_blueprint.json`. No separate indexing step needed.
---

# Blueprint Index

## Public setup

Resolve the user's authorized workspace before following file paths below.
`<workspace>` and named vault folders describe an existing layout, not bundled
data. Reuse equivalent files in the user's setup. Ask for a destination only
when discovery cannot resolve it. Private records and reference documents must
be supplied or located locally; do not invent their contents. Reuse answers
already in the request rather than repeating the intake. Use available supported
tools and the visible in-app Browser for browser work. Installing this skill
does not invoke it or authorize messages, publishing or unrelated service writes.

Scans the library for new images since the last run. Generates or updates written style blueprints. No UI. Pure analysis and file writing.

---

## Step 1 — Read the index

Read `Scene Engine/_index.md`.

Extract:
- Last run timestamp
- List of already-processed filenames

If last run is "never" → process everything in library/.

---

## Step 2 — Scan for new images

Use Glob to find all image files (*.jpg, *.jpeg, *.png, *.webp) inside `Scene Engine/library/`.

Pattern: `Scene Engine/library/**/*.{jpg,jpeg,png,webp}`

Cross-reference against the processed files list from _index.md.

New = any filename NOT already in the processed list.

Group new images by their parent subfolder (subfolder name = style category).

---

## Step 3 — Analyze each new image

For each new image, read it visually and extract:

**Layout**
- Orientation (portrait / landscape / square)
- Zone split — where does copy live vs where does the image live (top/bottom/left/right/overlay)
- Ratio of copy zone to image zone (approximate)

**Typography**
- Serif or sans-serif or display
- Weight (light / regular / bold / black)
- Size hierarchy — how many levels (H1, H2, sub, CTA, URL)
- Text color(s)
- Letter spacing (tight / normal / wide)

**Color Palette**
- Dominant background color or gradient
- Accent colors
- Overall temperature (warm / cool / neutral)

**Mood**
- 2-3 adjectives maximum (e.g. "cinematic, minimal, cold")

**Lighting**
- Quality of light in the architectural photo (golden hour / overcast / dramatic shadow / flat daylight)
- Direction if identifiable

**Composition**
- Where the building/subject sits in frame
- How much of the frame it occupies
- Use of negative space

**Overlay Treatment**
- Gradient overlay (describe direction and colors)
- Solid color block
- Transparent overlay
- None

**Signature Characteristics**
- The 2-3 things that make this style instantly recognizable
- What a designer would notice first

---

## Step 4 — Write or update the blueprint

Blueprint file location: `Scene Engine/blueprints/[style-category-name].md`

**If blueprint file does not exist:**
Create it using this format:

```
# Blueprint: [Style Category Name]

Images indexed: [count]
Last updated: [today's date]

---

## Layout
[description]

## Typography
[description]

## Color Palette
[description]

## Mood
[description]

## Lighting
[description]

## Composition
[description]

## Overlay Treatment
[description]

## Signature Characteristics
- [characteristic 1]
- [characteristic 2]
- [characteristic 3]

---

## Source Images
- [filename] — [one-line note on what this image contributes]
```

**If blueprint file already exists:**
- Add new observations to each section (don't overwrite — merge and enrich)
- Add new filenames to Source Images list
- Update "Images indexed" count
- Update "Last updated" date
- If a new image contradicts existing descriptions, note the variation: "Some images in this set use X, others use Y"

---

## Step 5 — Update _index.md

Rewrite `Scene Engine/_index.md`:
- Update "Last run" to today's date
- Update "Images processed" total count
- Update "Blueprints active" count
- Add all newly processed filenames to the Processed Files list
- Update the Style Categories list with all active blueprint names + image counts

---

## Step 6 — Report

Output in chat:

```
Blueprint Index complete.

[X] new images processed
[Y] blueprints updated
[Z] blueprints created

Updated:
- [style name] → [X] images total
- [style name] → [X] images total

Run /scene-engine to use these blueprints.
```

If no new images found:

```
Nothing new. Library is current as of [last run date].
```
