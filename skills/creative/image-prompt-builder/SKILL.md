---
name: image-prompt-builder
description: Create three Higgsfield image prompt variations from a reference and raw subject photos, preserving the subject and saving a reusable style blueprint.
---

# Image Prompt Builder for Higgsfield (Omni reference-first)

## Public setup

Resolve the user's authorized workspace before following file paths below.
`<workspace>` and named vault folders describe an existing layout, not bundled
data. Reuse equivalent files in the user's setup. Ask for a destination only
when discovery cannot resolve it. Private records and reference documents must
be supplied or located locally; do not invent their contents. Reuse answers
already in the request rather than repeating the intake. Use available supported
tools and the visible in-app Browser for browser work. Installing this skill
does not invoke it or authorize messages, publishing or unrelated service writes.

Take a reference image + Osiris's raw subject image(s), produce one dense Higgsfield-ready prompt under 3000 characters, and save the reference's style DNA as a reusable blueprint.

This skill is the image-side twin of `video-prompt-builder`. Same philosophy: brutal specificity over vague style words. Every output is anchored to concrete detail — hex codes, focal lengths, lighting directions, materials — because Higgsfield needs that density to produce polished output instead of generic AI slop.

---

## How Osiris uses this skill

1. He finds a reference image (magazine cover, ad, editorial shot, Pinterest save, architectural photo, interior creative).
2. He has his own raw subject image(s) — a client's building, interior, product, model.
3. He drops both to Veronica.
4. I decode the reference into a style DNA blueprint (JSON), save it to the vault, then generate the Higgsfield prompt.
5. He uploads reference + raw to Higgsfield as Omni ingredients, pastes the prompt, generates.

---

## Workflow

### Step 0 — Confirm inputs

At least one reference image and at least one raw subject image must be in the message. If either is missing, ask once:
- Missing reference → "Drop the reference image you're chasing the look of."
- Missing raw subject → "Drop the raw photo I'm transforming (the client's building / interior / subject)."

### Step 1 — Ask the editorial question

Before decoding, ask exactly one question:

> **Editorial cover (typography included — masthead, headlines, cover lines) or photo/creative (no typography)?**

Wait for answer. This decides whether Section 3 (Typography & Layout) appears in the output.

If he also mentions a client by name ([Client C], [Client D], [Client A], [Client B], etc.), note it for blueprint storage path.

### Step 2 — Decode the reference into a blueprint

Read the reference image carefully. Extract every element of its style DNA into the blueprint JSON below. Do not skip fields — if a field doesn't apply, write `null` or `"n/a"`, don't omit it.

Blueprint schema:

```json
{
  "source_reference": "filename-or-short-description",
  "decoded_at": "YYYY-MM-DD",
  "format": "editorial_cover | ad | architectural_photo | interior_photo | product_shot | portrait | lifestyle",
  "composition": {
    "framing": "full_bleed | contained | partial",
    "subject_position": "centered | rule_of_thirds_left | rule_of_thirds_right | low_third | high_third | off-center-left | off-center-right",
    "camera_angle": "eye_level | low_angle | high_angle | birds_eye | dutch_tilt | worms_eye",
    "focal_length_mm": 35,
    "depth_of_field": "shallow f/1.4 | medium f/4 | deep f/11 | tilt-shift miniature | full-frame hyperfocal",
    "crop": "tight | medium | wide | environmental"
  },
  "lighting": {
    "direction": "rembrandt | butterfly | split | side | backlit | top-down | front-flat | rim | cross-light",
    "quality": "hard | soft | diffused | dappled | overcast | direct-sun",
    "color_temperature_k": 3200,
    "key_highlights_hex": "#F5E6C8",
    "shadow_tone_hex": "#1A1A2E",
    "practicals": "tungsten lamps | overhead diffused | window light | neon | candlelight | mixed",
    "gels_or_tints": "warm amber | cool teal | magenta | green | none"
  },
  "color_grading": {
    "palette": [
      {"hex": "#2B1810", "role": "dominant", "name": "deep espresso"},
      {"hex": "#C9A961", "role": "accent", "name": "aged brass"},
      {"hex": "#E8DCC4", "role": "highlight", "name": "warm ivory"}
    ],
    "overall_mood": "teal_and_orange | desaturated_earth | high_contrast_bw | pastel | monochromatic | moody_editorial | kodak_warm | a24_muted | wes_anderson_pastel",
    "contrast": "high | medium | low",
    "saturation": "vivid | natural | muted | desaturated"
  },
  "typography": {
    "present": true,
    "masthead": {"font_style": "serif_display | sans_condensed | slab_serif | script | geometric_sans", "weight": "bold | regular | thin", "case": "uppercase | title_case | lowercase", "color_hex": "#FFFFFF", "position": "top_center | top_left | top_right | bottom_center"},
    "headlines": [
      {"text_slot": "H1", "style": "sans_condensed", "case": "title_case", "color_hex": "#E8DCC4", "position": "bottom_third_left"}
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
    "high-contrast geometric shadow on a plain wall",
    "film grain on skin tones"
  ]
}
```

Set `typography.present` to `false` if Osiris answered "photo/creative" — in that case, set the masthead/headlines/layout_hierarchy to `null`.

**Save the blueprint to:**
- Default: `<workspace>/Image Prompt System/Blueprints/[slug]-blueprint.json`
- If client was mentioned: also copy to `<workspace>/Clients/[Client Name] - [Contact]/Creatives/_image-blueprints/[slug]-blueprint.json`

Slug = lowercase, dashes, derived from `source_reference` (e.g., `ad-magazine-july-2024-cover` → `ad-mag-jul-2024`). Tell Osiris the exact path after saving.

### Step 3 — Read the raw subject image

Describe what's actually in his raw image(s) in 2-3 bullet points:
- What the subject is (building type, room, product, model)
- Current lighting / angle / condition
- Materials visible

This anchors the prompt to what Higgsfield is actually starting from. The prompt will say "the uploaded [subject]" — so I need to know what that subject is.

### Step 4 — Compose THREE prompt variations

**Default behavior: always output 3 variations in a mix of TEXT and JSON formats so Osiris can A/B test and pick what produces the best output.**

**Consult reference files for terminology density:**
- Lens, aperture, film stock → `references/photography-terminology.md`
- Lighting direction, color temperature, hex codes, grading presets → `references/lighting-and-color.md`
- Masthead, headlines, cover lines, whitespace (editorial only) → `references/editorial-layout-terminology.md`
- Materials, spatial qualities, architectural styles → `references/architecture-interior-terminology.md`
- Higgsfield / Nano Banana 2 syntax, edit vs generation mode, quoted-text rule, role labels → `references/higgsfield-omni-reference-syntax.md` ← **read this one every time**

Read whichever other files are relevant to the reference's format.

**Default mode: EDIT mode.** The skill is built for Osiris's workflow — real client project photos that must be preserved faithfully. Only switch to generation mode if he explicitly says "make something new" or there's no raw subject image.

#### Variation 1 — TEXT (creative / narrative)

Natural-language, atmospheric prose. Best when feel > precision. Edit mode phrasing, but the language flows. Useful when Osiris wants a more poetic take or the reference is mood-driven.

Structure:
```
Edit the uploaded [subject] photo using the attached [reference] as the [role] reference.
Keep the [subject] exactly identical — [long specific preserve list with materials,
geometry, proper nouns in quotes]. Do not regenerate.

Transform the scene into [atmospheric prose describing the mood, the sky, the lighting,
the signature moves — flowing sentences, but every hex code, Kelvin, and proper noun
stays specific]. [Typography layer if editorial — every exact text string in quotes.]

Aspect ratio: [X]. Style: [editorial descriptors]. [One short negative list at the end.]
```

Target: under 3000 chars.

#### Variation 2 — TEXT (tight / edit-mode optimized)

Imperative, numbered, dense. The reliable workhorse — this is what produces the most faithful output when preservation matters most. Use this as the default if Osiris picks only one.

Structure:
```
Edit the uploaded [subject] photo using the attached [reference] as the style reference.
Keep the [subject] exactly identical — [preserve list]. Do not regenerate, redraw, or
reinterpret.

Only modify these three things:

1. [Sky / time of day / background]: [specifics with hex codes]
2. [Lighting / mood]: [specifics with Kelvin + hex codes]<br>
3. [Typography overlay, if editorial — every string in quotes with font/color/position/size]

Aspect ratio: [X]. Style: [short editorial descriptors]. [Short negative list.]
```

Target: under 3000 chars. This is the pattern that already produced good output for Osiris — use the bundled `references/higgsfield-omni-reference-syntax.md`.

#### Variation 3 — JSON (structured / reusable)

Machine-parseable structure. Best when typography is heavy, when he wants to script the prompt, or when Nano Banana Pro's structured-region feature is the priority. Gemini parses JSON cleanly.

Structure (see `references/higgsfield-omni-reference-syntax.md` for the full template):
```json
{
  "operation": "edit",
  "base_image": "uploaded_image_1 ([raw subject description])",
  "style_reference": "uploaded_image_2 ([reference description])",
  "preserve": [list of specific elements],
  "modifications": [
    {"element": "sky", "action": "replace", "specification": "..."},
    {"element": "lighting", "action": "add", "specification": "..."},
    {"element": "typography_overlay", "action": "add", "layers": [
      {"type": "masthead", "text": "...", "font": "...", "color_hex": "...", "position": "...", "size": "..."},
      ...
    ]}
  ],
  "output": {"aspect_ratio": "...", "style": "..."},
  "constraints": ["render every text string exactly", "no AI gloss", ...]
}
```

Target: under 3000 chars (count the rendered JSON string).

### Step 5 — Character-limit pass (per variation)

For EACH of the three variations, count characters. If any exceeds 3000:
1. Remove redundancy — same hex code appearing in multiple sections, consolidate.
2. Collapse adjacent qualifiers.
3. In the JSON, tighten descriptions inside `specification` strings, not the structure.
4. Never cut hex codes, Kelvin, proper nouns, or the preserve list.

Report the character count of each variation when you output.

### Step 6 — Output

Present all 3 variations clearly labeled, each in its own code block for easy copy-paste:

```
─── VARIATION 1 — TEXT (creative) — [N] chars ───
[prompt text]

─── VARIATION 2 — TEXT (tight, edit-mode) — [N] chars ───
[prompt text]

─── VARIATION 3 — JSON (structured) — [N] chars ───
[JSON prompt]
```

Tell Osiris:
- The exact vault path where the blueprint was saved.
- The Higgsfield workflow: "Upload raw + reference as Omni ingredients, pick Nano Banana 2 or Pro, paste one variation, generate."
- Which variation is recommended as the default if he's in a hurry (usually Variation 2 for preservation-critical work, Variation 3 for typography-heavy covers).
- Any placeholder text strings he should swap before pasting (cover lines, client-specific copy).

---

## Blueprint reuse (second-time trigger)

If Osiris says "use the [name] blueprint with this new raw image" or similar, **skip Stage 1 and Stage 2**. Instead:
1. Find the blueprint at `Knowledge Base/Image Blueprints/` or the relevant client folder.
2. Load the JSON.
3. Jump straight to Step 3 (read the raw subject).
4. Compose the prompt using the saved blueprint's decoded values.

This is the whole point of saving blueprints — one decode, many reuses.

---

## Creative principles

Same philosophy as `video-prompt-builder`:

1. **Specificity over vagueness.** "35mm, f/2.8, light falling from camera-left at 3200K, key highlight `#F5E6C8`" beats "cinematic warm lighting." Generic language produces generic output.
2. **Anchor every section to the uploaded ingredients.** Higgsfield's Omni reference works best when the prompt names what's uploaded: "the uploaded interior", "the uploaded building facade." Don't describe the subject from scratch — describe what it becomes.
3. **Signature moves matter.** Every strong reference has 1-3 specific visual moves (a shaft of light, a prop placement, a particular crop). Name them exactly. Don't paraphrase into blandness.
4. **Transitions between style and subject are the hard part.** The prompt's real job is telling Higgsfield: "take THIS subject and transform it using THESE rules from THAT reference." Don't just describe the reference — describe the transformation.
5. **Contrast drives impact.** If the reference is moody and the raw image is flat-lit, call out the shift explicitly: "the uploaded interior currently has flat north light — transform to warm 2700K tungsten practicals with deep `#1A1A2E` shadows in the corners."

---

## Tone

Write like a photography director giving shot notes to a cinematographer — technical, precise, no fluff. No "stunning" or "breathtaking." Describe what happens in the image, let the result speak.
