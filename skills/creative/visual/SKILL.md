---
name: visual
description: A→Z reference-to-Higgsfield prompt generator. Use when Osiris runs `/visual` or drops a single reference image and wants a complete Higgsfield prompt for his own project. Decodes the reference, asks for raw images + every text variable in ONE structured form (with one-line suggestions per slot), and outputs two prompts (text + JSON) saved to a session folder. Trigger on `/visual`, `/visual [project]`, "build me a prompt for this reference", "decode this and prompt me", or any time a reference image is dropped together with a request for a Higgsfield-ready prompt for a new project. Standalone, manual A→Z, no blueprint reuse. For the older Higgsfield workflow with 3 variations + blueprint reuse use /image-prompt-builder. For HTML carousels use /creative.
---

# Visual — A→Z Reference-to-Higgsfield Prompt Generator

## Public setup

Resolve the user's authorized workspace before following file paths below.
`<workspace>` and named vault folders describe an existing layout, not bundled
data. Reuse equivalent files in the user's setup. Ask for a destination only
when discovery cannot resolve it. Private records and reference documents must
be supplied or located locally; do not invent their contents. Reuse answers
already in the request rather than repeating the intake. Use available supported
tools and the visible in-app Browser for browser work. Installing this skill
does not invoke it or authorize messages, publishing or unrelated service writes.

One reference in. Two prompts out. Five steps. Self-contained per session.

The skill is deliberately minimal: no blueprint reuse, no client-folder branching, no upfront questions. Every run is a fresh session with its own folder.

---

## Workflow

### Step 0 — Confirm reference image

If no reference image is in the message, ask once:

> "Drop the reference image you're chasing the look of."

Wait. Don't proceed without one.

If Osiris also mentions a project or client by name, note it for slug + suggestion sourcing.

### Step 1 — Decode + Variable Inventory

Read the reference image carefully. Output, in this order:

**1a. Style summary** — one line, plain English. Example: *"Moody editorial cover with desaturated earth palette and serif display masthead."*

**1b. Variable Inventory** — exact counts of every variable element. Format:

```
─── VARIABLE INVENTORY ───

TEXT (distinct text blocks in the reference):
  • Masthead: [N] string, [case], [position], ~[N] chars
  • Headline (H1): [N] string, [N-N] words, [position]
  • Subheadline: [N] strings, [N-N] words each, [position]
  • Cover lines: [N] strings, [N-N] words each, [position]
  • Captions / pull quotes: [N] strings, [N-N] words each
  • Bylines / contributors: [N] strings
  • Date / issue number: yes/no
  Total text blocks: [X]
  Approximate total word count: [Y]
  Distinct font styles: [N] ([list — e.g., "serif display + sans condensed"])

IMAGES:
  • Hero image: 1 — [framing, crop, treatment]
  • Secondary images: [N] — [position, size]
  • Decorative elements: [N] — [type, position]

BRAND ELEMENTS:
  • Logo: yes/no — [position if yes]
  • Website / URL: yes/no — [position if yes]
  • Barcode / price / date / social handles: as visible
```

Skip categories with zero entries (don't write "no decorative elements" — just omit the line).

**1c. Save `decode.json`** — full style DNA blueprint.

Session folder path: `<workspace>/Image Prompt System/Sessions/[YYYY-MM-DD]-[slug]/`

- Slug = lowercase-dashes from a 2–3 word description of the reference (e.g., `dwell-cover-jul-2015`, `vogue-portrait-spring`, `ad-magazine-editorial`).
- If a client was mentioned, prefix the slug with the client slug (e.g., `client-editorial-cover`).
- Create the folder if it doesn't exist (Write tool handles this automatically).
- Tell Osiris the absolute path after saving.

`decode.json` schema:

```json
{
  "source_reference": "filename or short description",
  "decoded_at": "YYYY-MM-DD",
  "format": "editorial_cover | ad | architectural_photo | interior_photo | product_shot | portrait | lifestyle",
  "style_summary": "one-line plain-English summary",
  "composition": {
    "framing": "full_bleed | contained | partial",
    "subject_position": "centered | rule_of_thirds_left | rule_of_thirds_right | low_third | high_third | off-center-left | off-center-right",
    "camera_angle": "eye_level | low_angle | high_angle | birds_eye | dutch_tilt | worms_eye",
    "focal_length_mm": 35,
    "depth_of_field": "shallow f/1.4 | medium f/4 | deep f/11",
    "crop": "tight | medium | wide | environmental"
  },
  "lighting": {
    "direction": "rembrandt | butterfly | split | side | backlit | top-down | front-flat | rim | cross-light",
    "quality": "hard | soft | diffused | dappled | overcast | direct-sun",
    "color_temperature_k": 3200,
    "key_highlights_hex": "#F5E6C8",
    "shadow_tone_hex": "#1A1A2E",
    "practicals": "tungsten lamps | window light | overhead diffused | mixed",
    "gels_or_tints": "warm amber | cool teal | none"
  },
  "color_grading": {
    "palette": [
      {"hex": "#2B1810", "role": "dominant", "name": "deep espresso"},
      {"hex": "#C9A961", "role": "accent", "name": "aged brass"},
      {"hex": "#E8DCC4", "role": "highlight", "name": "warm ivory"}
    ],
    "overall_mood": "moody_editorial | desaturated_earth | high_contrast_bw | pastel | monochromatic | kodak_warm | a24_muted",
    "contrast": "high | medium | low",
    "saturation": "vivid | natural | muted | desaturated"
  },
  "typography": {
    "present": true,
    "masthead": {"font_style": "serif_display | sans_condensed | slab_serif | script | geometric_sans", "weight": "bold | regular | thin", "case": "uppercase | title_case | lowercase", "color_hex": "#FFFFFF", "position": "top_center | top_left | top_right | bottom_center"},
    "headlines": [
      {"slot": "H1", "style": "sans_condensed", "case": "title_case", "color_hex": "#E8DCC4", "position": "bottom_third_left", "approx_words": 5}
    ],
    "layout_hierarchy": "masthead > hero_image > headline > subhead > bylines"
  },
  "atmosphere": {
    "era": "1970s | 1980s | 1990s | contemporary | futuristic | timeless",
    "mood": "luxurious_calm | energetic_chaos | introspective_quiet | opulent | minimal | monastic | nostalgic | romantic | clinical",
    "texture": "matte | glossy | film_grain | clean_digital | painterly | halation",
    "props_or_elements": ["leather-bound book", "brass lamp", "linen curtain"]
  },
  "materials_and_surfaces": ["travertine", "walnut", "brushed_brass", "raw_concrete"],
  "signature_moves": [
    "single shaft of light cutting diagonally across the floor",
    "high-contrast geometric shadow on a plain wall"
  ],
  "variable_inventory": {
    "text_blocks_total": 7,
    "approximate_word_count": 63,
    "distinct_fonts": 2,
    "hero_image_count": 1,
    "secondary_image_count": 0,
    "logo_present": true,
    "website_present": false,
    "barcode_present": false
  }
}
```

If `typography.present` is false (photo with no text overlay), set masthead/headlines/layout_hierarchy to null.

### Step 2 — One-shot Intake Form

Output a single message asking for everything. Each text slot includes a one-line suggestion in italics. Suggestions come from:

- The reference's tonal register (luxurious calm, minimal, opulent, etc.)
- Any project/client context Osiris mentioned
- Client metadata if a client was named — pull from `<workspace>/Clients/[Client Name] - [Contact]/` for brand voice, taglines, past copy

**Suggestion-writing rules:**

- Match the reference's word counts exactly. If H1 is 5 words, suggest 5 words.
- Use proper nouns when known (project name, client, city).
- No generic luxury copy. *"The House That Listens"* beats *"Discover the Future of Design."*
- One line per suggestion.
- Skip slots that don't apply (no logo in reference → don't include the logo line).

**Format:**

```
─── INTAKE FORM ───
Reply with all of the below in one message. Suggestions in italics — override anything that doesn't fit, or say "use as-is" to accept all.

A. RAW IMAGES
   Drop your project image(s). I need: 1 hero image of [subject type from reference]. Format JPG/PNG.

B. TEXT SLOTS

1. Masthead: ____
   *suggested: "[CLIENT NAME UPPERCASE]" — using the client's brand as a publication masthead*

2. Headline (H1) — [N] words: ____
   *suggested: "[atmospheric headline anchored to project's emotional thesis]"*

3. Subheadline — [N] words: ____
   *suggested: "[one-sentence project description, tonally matched to the reference]"*

[continue for each slot in the inventory — only the ones that apply]

C. PROJECT CONTEXT
   • Client name: ____
   • Project name: ____
   • Location: ____

D. BRAND ASSETS (only if logo/website were in the inventory)
   • Logo file path: ____
     *suggested: confirm `Clients/[Client]/Brand/logo.png`*
   • Website URL: ____
     *suggested: [from vault if known]*
```

**Wait for Osiris's response. Do not proceed to Step 3 until he replies.**

If he says "use as-is" — accept all suggestions verbatim, but he still needs to provide raw images.

If he fills only some slots — use his fills for those, suggestions for the rest.

### Step 3 — Read raw subject + save filled intake

After Osiris replies:

1. Read the raw image(s) he uploaded. Describe what's in them in 2–3 bullets:
   - Subject (building type, room, product, model)
   - Current lighting / angle / condition
   - Materials visible

2. Take his filled slots (or accept suggestions verbatim if he said "use as-is").

3. Save `intake.md` to the session folder. Markdown format with the completed form, including:
   - The raw image filenames he provided
   - Every filled slot (his copy in quotes)
   - Project context
   - Brand assets

### Step 4 — Compose two prompt formats

Both prompts must:

- Use Higgsfield Omni edit-mode framing — *"Edit the uploaded [subject] using the attached [reference] as the style reference. Keep the [subject] exactly identical — [preserve list]. Do not regenerate."*
- Quote every text string exactly as Osiris filled it. Nano Banana 2 / ChatGPT Image 2 hallucinate fake words when text isn't quoted.
- **Enforce type-size discipline** — see below. This is the #1 factor in avoiding "AI swamp" output.
- Stay under 3000 characters each (3000 is a guideline; up to ~3200 is acceptable for the JSON).

**TYPE-SIZE DISCIPLINE — applies to every editorial cover with typography**

Image-gen models (Nano Banana 2, ChatGPT Image 2, etc.) interpret "magazine cover" as "make the type huge." Without explicit caps, they output mastheads occupying 25–30% of canvas height — instant AI-swamp aesthetic. Real editorial covers keep masthead ≈10% of canvas, H1 10–11%, everything else ≤2%.

Both prompts MUST include the following two blocks:

1. A `CRITICAL` block at the top with hard letterform caps:

```
CRITICAL — match the reference's type-to-photo proportions EXACTLY. Reference masthead is small (≈1/14 canvas). Headline sits in negative space, doesn't crowd the photo. Hard caps:
- Masthead letterform ≤ 7% canvas
- H1 letterform ≤ 10% per line, stacked 2 lines
- All other type ≤ 1.8%
- Any type > 12% canvas = wrong
```

2. A `NEGATIVE LIST` block at the bottom anchoring those caps:

```
NEGATIVE LIST: NO masthead > 7% letterform. NO H1 > 10% per line. NO type > 12% canvas anywhere. NO AI typography artifacts (oversharp edges, warped kerning, hallucinated text). NO drop shadows. NO outline strokes. Type must look professionally typeset by a magazine art director — refined, restrained, intentional — NOT AI-rendered.
```

Skip both blocks only if `typography.present` is `false` (no text overlay needed).

**Consult these reference files for terminology density (read every time, don't restate):**

- `references/higgsfield-omni-reference-syntax.md` — required, read every time
- `references/photography-terminology.md` — lens, aperture, film stock
- `references/lighting-and-color.md` — direction, K, hex codes
- `references/editorial-layout-terminology.md` — read if `typography.present` is true
- `references/architecture-interior-terminology.md` — read if subject is architectural/interior

**`prompt.txt` — TIGHT TEXT (edit-mode optimized):**

Imperative, numbered, dense. The reliable workhorse.

```
Edit the uploaded [subject] using the attached [reference] as style + proportional reference. Output: complete [magazine cover / photograph] — photo + typography as one finished print-ready image.

CRITICAL — match the reference's type-to-photo proportions EXACTLY. Reference masthead is small (≈1/14 canvas). Hard caps: masthead letterform ≤ 7% canvas, H1 ≤ 10% per line stacked 2 lines, all other type ≤ 1.8%, any type > 12% canvas = wrong.

Keep the [subject] exactly identical — [preserve list with materials, geometry, proper nouns]. Do not regenerate.

Modify the photo:

1. [Sky / atmosphere]: [specifics with hex codes + Kelvin]
2. [Color grading]: [specifics with hex codes]
3. Typography (render every quoted string EXACTLY, no fake words):
   - "[masthead string]" — sans condensed regular, title case, #FFFFFF, top-left 5% margin, 7% letterform.
   - [continue for each filled slot — "string", font, case, color hex, position, letterform %]

Aspect ratio: [X]. Output: complete editorial cover, print-ready.

NEGATIVE LIST: NO masthead > 7% letterform. NO H1 > 10% per line. NO type > 12% canvas. NO AI typography artifacts (oversharp edges, warped kerning, hallucinated text). NO drop shadows. NO outline strokes. NO oversaturation. NO AI cloud spirals. NO plastic sheen. Type must look professionally typeset, NOT AI-rendered.
```

Save to `<workspace>/Image Prompt System/Sessions/[YYYY-MM-DD]-[slug]/prompt.txt`.

**`prompt.json` — STRUCTURED JSON:**

```json
{
  "operation": "edit",
  "base_image": "uploaded_image_1 ([raw subject description])",
  "style_reference": "uploaded_image_2 ([reference description]) — match type-to-photo proportions; masthead ≈1/14 canvas, headline in negative space",
  "type_caps": {
    "masthead": "≤7% letterform",
    "h1": "≤10% per line, stacked 2 lines",
    "other": "≤1.8%",
    "ceiling": "any type >12% canvas = wrong"
  },
  "preserve": ["specific elements unchanged — materials, geometry, proper nouns"],
  "modifications": [
    {"element": "sky", "spec": "..."},
    {"element": "grading", "spec": "..."},
    {"element": "typography", "render_exactly": true, "layers": [
      {"text": "[exact string from intake]", "font": "...", "case": "...", "color": "#...", "position": "...", "letterform": "X%"}
    ]}
  ],
  "output": {"aspect_ratio": "...", "style": "..."},
  "constraints": [
    "render every quoted string exactly",
    "masthead ≤7%, H1 ≤10% per line, type ceiling 12%",
    "no AI typography artifacts (warped kerning, oversharp edges, drop shadows, outlines)",
    "type looks professionally typeset NOT AI-rendered",
    "preserve [subject] geometry exactly",
    "no AI gloss, no plastic sheen, no oversaturation, no AI clouds"
  ]
}
```

Save to `<workspace>/Image Prompt System/Sessions/[YYYY-MM-DD]-[slug]/prompt.json`.

**Character-limit pass:** count chars in each prompt. If over 3000:

1. Remove redundancy — consolidate hex codes that appear in multiple sections.
2. Collapse adjacent qualifiers.
3. In the JSON, tighten descriptions inside `specification` strings, not the structure.
4. Never cut hex codes, Kelvin temperatures, proper nouns, or the preserve list.

### Step 5 — Output + handoff

Show both prompts in chat in fenced code blocks for clean copy:

```
─── prompt.txt — [N] chars ───
[full text prompt]

─── prompt.json — [N] chars ───
[JSON prompt]
```

Then tell Osiris:

- The session folder path: `<workspace>/Image Prompt System/Sessions/[YYYY-MM-DD]-[slug]/`
- Higgsfield steps: *"Upload raw + reference as Omni ingredients in Higgsfield, pick any model (Nano Banana 2/Pro, ChatGPT Image 2, etc.), paste either prompt, generate."*
- That's it. No follow-up questions.

If he comes back wanting another creative, treat it as a fresh `/visual` run — new session, new folder.

---

## Tone

Photography director giving shot notes to a cinematographer. Technical, precise, no fluff. No "stunning" or "breathtaking." Describe what happens in the image, let the result speak.

---

## What this skill is NOT

- No blueprint reuse logic — every run is a fresh session
- No editorial-vs-photo upfront question — the inventory step detects typography automatically
- No client-folder branching — everything goes to `Sessions/`
- No 3-variation output — only `prompt.txt` and `prompt.json`
- No automatic image generation or publication

For 3 variations + blueprint reuse, use `/image-prompt-builder`.
For HTML carousels, use `/creative`.
