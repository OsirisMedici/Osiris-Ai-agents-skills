---
name: reference
description: Use when Osiris says "/reference", "decode this reference", "extract a prompt from this image", or drops a reference image (magazine cover, ad, poster, creative) and wants a reusable prompt. Analyzes the image into a structured JSON blueprint — layout, typography, colors, imagery, mood — then lets him swap in his own content to generate a detailed prompt ready for Hexfield, Midjourney, DALL-E, or any image AI.
---

# Reference Decoder

## Public setup

Resolve the user's authorized workspace before following file paths below.
`<workspace>` and named vault folders describe an existing layout, not bundled
data. Reuse equivalent files in the user's setup. Ask for a destination only
when discovery cannot resolve it. Private records and reference documents must
be supplied or located locally; do not invent their contents. Reuse answers
already in the request rather than repeating the intake. Use available supported
tools and the visible in-app Browser for browser work. Installing this skill
does not invoke it or authorize messages, publishing or unrelated service writes.

Turn any reference image into a reusable, variable-driven prompt. The reference stays the style template; Osiris's content becomes the variables.

**Output:** A detailed text prompt (copy-paste into Hexfield or any image AI) + the JSON blueprint (for reuse/tweaking later).

---

## The Flow

Three phases. Move through them tightly — no filler.

### Phase 1 — Decode the reference

1. Read the image Osiris provided using the Read tool (he either dropped it in chat or gave a path).
2. Extract every visual element into the JSON blueprint schema below. Be specific — real hex values, precise typography descriptions, exact spatial positions.
3. Output the JSON blueprint in a fenced code block.
4. Output a one-sentence "style summary" — what this reference looks like in plain English.

### Phase 2 — Ask what he wants to swap

Show him a compact list of the variables he can override. Ask which ones he wants to change. He can reply with any mix:

- "Change the headline to X"
- "Swap the main image to X"
- "Keep everything, just change the masthead to X"
- "Keep it all — just give me the prompt"

Don't walk through every variable one-by-one unless he asks you to. Respect his time.

### Phase 3 — Generate the final prompt

1. Apply his overrides to the blueprint.
2. Build the final text prompt using the format below.
3. Output it in a fenced code block so he can copy-paste it straight into Hexfield.
4. Done. No summary, no next steps.

---

## JSON Blueprint Schema

Extract the image into this exact structure. Every field. Use real hex values you sample from the image, not guesses.

```json
{
  "format": "magazine_cover | social_post | ad | poster | book_cover | packaging | other",
  "dimensions": { "width": 1080, "height": 1350, "unit": "px" },
  "orientation": "portrait | landscape",

  "layout": {
    "grid": "single_column | two_column | asymmetric | freeform",
    "masthead_position": "e.g. top_center",
    "headline_position": "e.g. bottom_left",
    "image_coverage": "full_bleed | contained | partial",
    "margins": { "top": "5%", "right": "5%", "bottom": "5%", "left": "5%" },
    "element_order": ["masthead", "main_image", "headline", "subheadlines"]
  },

  "typography": {
    "masthead": {
      "text": "exact text as shown",
      "style": "serif | sans-serif | slab | display | script",
      "weight": "thin | light | regular | bold | black",
      "case": "uppercase | lowercase | title_case | sentence_case",
      "size_ratio": "large | medium | small (relative to canvas)",
      "color": "#hex"
    },
    "headline": { "text": "", "style": "", "weight": "", "case": "", "size_ratio": "", "color": "#hex" },
    "subheadlines": [{ "text": "", "style": "", "weight": "", "case": "", "size_ratio": "", "color": "#hex" }],
    "body_text": [{ "text": "", "style": "", "weight": "", "case": "", "size_ratio": "", "color": "#hex" }],
    "additional_text": [{ "text": "", "purpose": "tagline | price | date | issue_number | contributor", "style": "", "color": "#hex" }]
  },

  "colors": {
    "palette": [{ "hex": "#hex", "role": "background | accent | text | decorative", "name": "descriptive name" }],
    "background": { "type": "solid | gradient | image", "value": "#hex or gradient description" },
    "text_primary": "#hex",
    "text_accent": "#hex",
    "overlay": { "color": "#hex", "opacity": 0.4 }
  },

  "imagery": {
    "main_image": {
      "description": "detailed description of what is depicted",
      "style": "photography | illustration | 3d_render",
      "treatment": "e.g. high_contrast, desaturated, duotone, warm_filter",
      "subject_position": "center | left_third | right_third | etc",
      "crop": "headshot | full_body | landscape | detail"
    },
    "secondary_images": [{ "description": "", "position": "", "size": "" }],
    "decorative_elements": [{ "type": "line | border | shape | pattern", "position": "", "description": "" }]
  },

  "content": {
    "headline_count": 1,
    "subheadline_count": 0,
    "image_count": 1,
    "has_barcode": false,
    "has_price": false,
    "has_date": false,
    "special_elements": []
  },

  "mood": {
    "aesthetic": "minimalist | maximalist | editorial | luxe | grunge | etc",
    "era": "modern | retro_70s | art_deco | mid_century | etc",
    "tone": "authoritative | playful | aspirational | provocative | serene",
    "lighting_quality": "bright | moody | natural | studio | dramatic",
    "overall_impression": "one sentence summarizing the overall vibe"
  }
}
```

**Rules for extraction:**

- For fonts: describe the style (serif/sans-serif/slab/display/script), weight, and case. Don't guess font names unless you're confident.
- For colors: extract actual hex values you observe in the image. Name them descriptively ("deep navy", "warm cream").
- For layout: describe spatial relationships as percentages or named positions.
- For mood: be specific and evocative, not generic. "Moody editorial with warm tungsten lighting" beats "atmospheric".
- Count every text element, every image, every decorative element.
- `overlay` is `null` when there's no overlay treatment.
- If something is ambiguous, describe what you see and give your best interpretation.

---

## Prompt Output Format

Build the final prompt as labeled sections, one per category. Keep it dense and specific — every detail matters for image AIs.

```
Create a [format] with the following specifications:

FORMAT: [orientation] [format], [width]x[height][unit]

LAYOUT: [image_coverage] [grid] layout. Masthead positioned [masthead_position]. Main headline positioned [headline_position]. Margins: top [X], right [X], bottom [X], left [X]. Element stacking order: [list].

MAIN IMAGE: [description]. [style] style, [treatment] treatment. Subject positioned [subject_position], cropped as [crop].

TYPOGRAPHY:
- Masthead: "[text]" in [weight] [style], [case], [size_ratio], color [color]
- Headline: "[text]" in [weight] [style], [case], [size_ratio], color [color]
- Subheadline 1: "[text]" in [weight] [style], [case], [size_ratio], color [color]
- [any additional_text items: e.g. price "$12.99" in [style], color [color]]

COLOR PALETTE: [name] ([hex], [role]), [name] ([hex], [role]), ... Background: [type] [value]. Primary text color [hex]. Accent text color [hex]. [If overlay: Semi-transparent overlay [color] at [X]% opacity.]

MOOD & STYLE: [aesthetic] aesthetic. [era] era. [tone] tone. [lighting_quality] lighting. Overall impression: [overall_impression].

[If decorative_elements exist]
DECORATIVE ELEMENTS:
- [type] at [position]: [description]

[If content flags true]
ADDITIONAL ELEMENTS: barcode, price "[text]", date "[text]", [special_elements].
```

---

## Variable Swap Menu

After Phase 1, show this compact menu. Use the actual extracted values so he can see what's there.

```
Extracted. Here's what's swappable — tell me which ones to change (or "use as-is"):

• Masthead: "ARCHDIGEST"
• Headline: "The Future of Living"
• Subheadlines (1): "Inside the world's most innovative homes"
• Main image: "Modern minimalist house with floor-to-ceiling windows at dusk"
• Price / date / additional text: [$12.99]
• Any specific colors to swap: [list key hex values from palette]
• Anything else from the blueprint
```

Skip any sections that don't apply (e.g. if there are no subheadlines, don't mention them).

---

## Edge Cases

**No image provided:** Ask for one. Don't start analyzing thin air.

**Multiple images dropped:** Ask which one is the reference. Don't guess.

**Non-magazine-cover reference** (ad, poster, social post, packaging): Still works — the schema is flexible enough. Set `format` to the right value and adapt accordingly. Fields that don't apply (e.g. `has_barcode` for a social post) stay `false`.

**He wants to skip variable swap:** Go straight to Phase 3. Output the prompt as-is from the reference.

**He wants to save the blueprint to a file:** Save it to `<workspace>/reference-decoder/blueprints/[slug].json` — creates the folder if needed. Use a descriptive slug from the reference (e.g. `vogue-spring-2026.json`).

---

## Tone

- No "Great reference!" / "Love the style!" energy.
- Just decode, ask, generate.
- Treat this like a utility — precise, fast, no filler.
- Output the JSON and the prompt in fenced code blocks so he can copy them cleanly.
