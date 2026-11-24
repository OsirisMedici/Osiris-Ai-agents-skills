# Higgsfield Omni reference syntax (Nano Banana 2 / Nano Banana Pro)

How to write prompts that work well with Higgsfield's Nano Banana 2 / Pro model and Omni reference feature. Higgsfield runs Nano Banana on top of Google's Gemini 3.1 Flash image backbone — prompts that work for Gemini / Nano Banana also work here.

## The single biggest insight — edit mode vs. generation mode

**Nano Banana 2 has two fundamentally different prompt modes.** Picking the wrong one is the #1 reason output drifts from what Osiris wants.

### Generation mode (wrong default for our use case)
Narrative description of a scene from scratch. The model builds everything based on the description, with the reference images used as loose style/subject donors. It may invent a NEW building inspired by the uploaded one, a NEW interior inspired by the uploaded one — similar but not identical.

Structure: `[Subject] + [Action] + [Location] + [Composition] + [Style]` — narrative, descriptive.

### Edit mode (what we usually want)
The uploaded image is treated as the **literal base**. The prompt says what to **preserve** and what to **change**. The model modifies the base image rather than regenerating.

Structure: `[Base image] + [what to keep exactly the same] + [specific edits to make] + [typography overlay if any]` — imperative, explicit.

**Osiris's core use case (reference photo + raw architectural image → editorial cover) is an EDIT, not a generation.** The raw image is his client's actual project and must be preserved literally. Only the sky, lighting mood, and typography overlay are changing.

## Edit-mode prompt structure (the correct default)

Use this structure when Osiris has a real raw image he wants preserved faithfully:

```
Edit the uploaded [subject] photo. Keep [everything important about the subject] exactly
identical — [list the specifics]. The [subject]'s geometry, pose, and position must not
change. Do not regenerate or reinterpret the [subject].

Only modify these things:

1. [First edit — e.g., sky and time of day]: [specifics with hex codes]
2. [Second edit — e.g., interior lighting]: [specifics]
3. [Third edit — typography overlay]: [exact text in quotes, positioning, font, color]

Aspect ratio: [e.g., 3:4 portrait].
Style: [editorial descriptors, photography terminology].
```

Key phrases that work:
- "Edit the uploaded [subject]"
- "Keep [X] exactly identical / exactly the same"
- "Preserve the original [attribute]"
- "Don't alter the [attribute]"
- "The [subject]'s geometry, pose, and position must not change"
- "Only modify these things: 1. ... 2. ... 3. ..."
- "Do not regenerate or reinterpret the [subject]"

Avoid phrases that trigger generation mode:
- "A [subject]..." (describes a new subject)
- "Using the uploaded [subject] as the hero..." (sets up narrative description)
- Long descriptive passages of the subject's attributes (these are for generation)

## Typography — wrap ALL exact text in quotation marks

Nano Banana 2 renders text correctly **only when the exact string is in quotation marks**. Unquoted text guidance ("add headlines about luxury architecture") produces hallucinated gibberish like "Hew Roman Security Series on Umart Home" — the model invents fake words.

Always provide:
- The **exact string** of every text element, in quotes.
- Font style.
- Color hex.
- Position on canvas.
- Size.

Strong:
```
Masthead: "dwell" in bold lowercase geometric sans, #E8B61A yellow, top-left, ~35% of canvas width.
Cover line: "The Next Modern Residence" in italic high-contrast serif, white #FFFFFF, 64pt, middle-left over sky.
Small cover line 1: "Home Security: A New Series on Protecting Your Residence" in white serif, 14pt, top-right, right-aligned.
Small cover line 2: "The Rise of Vertical Gardens in Luxury Residential" in white serif, 14pt, below cover line 1, right-aligned.
```

Weak (will hallucinate):
```
Top-right: three short cover lines in white serif about smart homes, security, and design.
```

If Osiris doesn't provide exact cover-line strings, I should ask for them OR propose specific strings and label them as "placeholder — swap before generating."

## Multi-image reference with role labels (when using both reference + raw)

Google's documented template for multi-image prompts — works on Nano Banana 2 and by extension on Higgsfield:

```
Using the attached [image 1] as the [role — structure / base / subject / background]
and the attached [image 2] as the [role — style / texture / lighting / reference],
[relationship verb — transform into / combine with / style like] [output specification].
```

For Osiris's case:
```
Using the attached F 70 architectural photo as the base image and the attached Dwell
magazine cover as the editorial style reference, transform the base image's lighting
and sky to match the Dwell cover's blue-hour mood, then overlay the Dwell magazine
cover typography layer on top. Keep the F 70 building itself exactly identical to
the base image.
```

Role labels that work:
- "as the base image"
- "as the structure"
- "as the texture"
- "as the style reference"
- "as the lighting reference"
- "as the mood reference"
- "as the typography reference"
- "as the background"
- "as the subject"

## Bundle all edits into one prompt

Nano Banana 2 handles multi-part edits in a single pass better than iterative prompts. Bundle the changes:

Strong:
```
"Make the lighting warm tungsten 2700K, replace the sky with blue-hour dusk #4A5968,
and add the masthead 'dwell' in #E8B61A yellow top-left."
```

Weak:
```
"Make the lighting warm tungsten."
[next turn] "Now replace the sky."
[next turn] "Now add the masthead."
```

## Positive framing, not negatives

Describe what you want, not what you don't want:
- ✅ "dusk sky with soft cloud cover"
- ❌ "not daytime, no bright sun"
- ✅ "empty driveway"
- ❌ "no cars"

Exception: at the very end of the prompt, one short negative list is useful for common AI failures:
```
No AI gloss, no plastic smoothness, no CGI, no hallucinated text or fake Latin.
```

## Concrete photography terms beat mood words

Nano Banana 2's Gemini backbone responds strongly to technical photography language:
- ✅ "35mm, f/8, eye-level, deep DOF"
- ✅ "shot on medium-format digital camera"
- ✅ "three-point softbox setup, key light at 45° camera-left"
- ❌ "cinematic vibe"
- ❌ "professional look"
- ❌ "aesthetic lighting"

## Preserve-list pattern (critical for architecture/interior)

When the base image contains fine detail that matters (every window, material, gate plaque, tree), list specifics in a "preserve" block:

```
Preserve exactly: the black steel exoskeleton frame, grey basalt stone upper facade,
warm teak wood panels, perforated metal screen at center, twin vertical garden columns,
wood-slat ground-floor fence, white compound wall, "F 70" gate plaque (including the
exact text), all flowering trees, and the white picket fence in front.
```

A long specific preserve-list anchors the model. Vague preserve ("keep the building") lets Gemini reinterpret.

## The core principle — role labels when using multi-image

Higgsfield Omni takes **multiple images as ingredients**. The prompt must label each ingredient with a role:
- **Raw subject image** → `as the base image` (preserve literally)
- **Reference image** → `as the [style / lighting / typography] reference` (donor role only)

Without role labels, Higgsfield blends randomly — sometimes it preserves the wrong element, sometimes it ignores the reference style. Explicit role labels are the leverage point.

## Ingredient labeling patterns

**Pattern A — Style transfer to a specific subject:**
```
Transform the uploaded [subject] in the style of the uploaded [reference aesthetic].
Preserve: [what must stay the same about the subject].
Transform: [what should change to match the reference].
```

**Pattern B — Editorial cover from a project photo:**
```
Using the uploaded [building/interior/space] as the hero subject, compose an editorial magazine cover
in the style of the uploaded reference. Preserve the architectural identity and materials of the uploaded
subject. Transform lighting, color grading, atmosphere, and composition to match the uploaded reference.
```

**Pattern C — Product shot restyled:**
```
Photograph the uploaded [product] in the environment and lighting of the uploaded reference.
Keep product color, shape, and branding exact. Adopt the reference's camera angle, lens characteristics,
and color palette.
```

## Preserve vs transform — be explicit

Higgsfield needs to know what from the raw subject is sacred and what is negotiable. Always include two lists:

**Preserve (from raw subject):**
- Geometry of the space / building / object
- Material identity (if the travertine floor stays travertine, say so)
- Color of the subject (if the brand color is #C9A961, lock it)
- Layout of permanent elements (wall positions, fenestration, fixed furniture)

**Transform (from reference):**
- Lighting direction and quality
- Color grading and mood
- Atmosphere, props, styling
- Camera angle and focal length (if different from raw)
- Time of day
- Typography (if editorial)

Example:
> Preserve from uploaded interior: the room's wall positions, the window proportions, the walnut herringbone floor, the pale limewash wall. Transform from uploaded reference: warm 2700K tungsten practicals replacing the current flat daylight, deep `#1A1A2E` shadows in corners, a single shaft of evening light cutting diagonally across the floor, bouclé sofa in cream styled lived-in.

## Phrasing to use

Strong:
- "the uploaded [subject]"
- "the uploaded reference"
- "preserve the uploaded subject's [attribute]"
- "adopt the reference's [attribute]"
- "shot as if in the same series as the reference"
- "match the reference's [specific element]"

Avoid:
- "a building like this" (ambiguous — like which image?)
- "this style" (no anchor)
- Generic aesthetic words without hex codes ("moody", "cinematic", "cozy") — always back them with specifics

## Sequencing inside the prompt

Higgsfield parses left-to-right with some attention to section structure. Best ordering:

1. **Subject anchor first** — what the image is of (the uploaded [subject])
2. **Composition** — how it's framed
3. **Lighting** — direction, quality, temperature, hex codes
4. **Color grading** — palette, mood
5. **Typography** — only for editorial covers
6. **Atmosphere / signature moves** — specific, concrete, visual
7. **Preserve/transform callouts** — at the end, as disambiguation

## Negative prompts / what to exclude

Higgsfield image models sometimes accept a negative list. Useful entries:
- "not cartoon, not illustration, not 3D render, not Midjourney-default"
- "no CGI gloss, no AI smoothness, no plastic skin"
- "no stock photography lighting"
- "no generic warm filter"
- "avoid symmetric face/building distortion"

Include these only if Higgsfield's output is drifting toward common AI failures. Don't include by default — negatives take character count.

## Common Higgsfield failure modes and prompt-level fixes

| Failure | Why | Fix in prompt |
|---|---|---|
| Output ignores reference's lighting | Reference role not labeled | Say explicitly "adopt lighting from the uploaded reference" |
| Output drifts to generic "warm filter" | Lighting described only in mood words | Add specific direction + Kelvin + hex codes |
| Output loses subject identity | Preserve list missing | Add preserve callouts for subject's key attributes |
| Output adds random elements | Prompt left gaps | Tighten Section 4 with specific signature moves, no gaps |
| Output feels "rendered" / plastic | Missing film/grain spec | Add a film stock or "35mm photograph, slight grain" |
| Output has AI "face smoothness" | No preservation instruction | "preserve natural skin texture, no smoothing" |
| Output has wrong era / style drift | Era not specified | Add "shot in 2023 on a professional medium-format camera" or similar anchor |
| Architectural lines warp | No "architectural correction" note | Add "straight architectural lines, no barrel distortion, tilt-shift correction applied" |

## Aspect ratio and canvas

Higgsfield typically takes an aspect ratio as a separate control. But it helps to state intent in the prompt:
- Magazine cover: **3:4 portrait** (8.5×11" standard)
- Instagram square: **1:1**
- Instagram carousel / portrait: **4:5**
- Landscape editorial: **3:2** or **16:9**
- Billboard: **16:9** or wider

Include the aspect ratio intent in Section 1: "composed for a 3:4 portrait magazine cover, with space reserved at the top for masthead and at the bottom-third-left for cover lines."

## Model-specific notes

Higgsfield supports several image models. They interpret prompts slightly differently:

- **Nano Banana / Soul** (fast, good at style transfer) — responds well to short, dense prompts. Keep under 2500 chars. Emphasize color palette and lighting.
- **Seedream / Seedance image mode** (detail-heavy) — can handle 3000+ chars, rewards specificity. Great for editorial covers with typography.
- **Flux-based variants** — respond strongly to photography terminology (lens, aperture, film stock). Lean into those.

If Osiris says which model he's using, prioritize accordingly. If he doesn't say, write to the generic 3000-char target.

## A complete example prompt (skeleton)

```
Editorial magazine cover composition at 3:4 portrait aspect. Using the uploaded living room
interior as the hero subject (preserve the walnut herringbone floor, the wall of arched windows,
the pale limewash walls, the coffered ceiling). Transform the lighting, atmosphere, and styling
to match the uploaded reference (an Architectural Digest night-shoot cover).

Shot on 35mm at f/2.8, eye-level, subject positioned using the uploaded interior as the full
environmental frame. Medium-wide crop showing the full room with a hint of ceiling and floor.
Deep layered foreground-to-background with a travertine coffee table in mid-ground.

Lighting: warm 2700K tungsten practicals as the primary key — a brass floor lamp camera-left,
a pair of wall sconces camera-right. Cool 9000K blue-hour ambient through the arched windows
as fill. Hard specular highlights on the travertine at #F5E6C8. Shadow tone #1A1A2E in the
corners. Mixed-temperature signature — warm interior against cool exterior.

Color palette: dominant deep espresso #2B1810, accent aged brass #C9A961, highlight warm ivory
#E8DCC4. Moody editorial grading, medium contrast with crushed shadows only in deepest corners,
muted saturation except the brass which stays warm-saturated.

Masthead: "ARCHITECTURAL DIGEST" in slab serif, condensed, uppercase, #FFFFFF, top-center,
5% of vertical canvas, tight tracking. Hero cover line "THE QUIET HOUSE" in 72pt Didone
uppercase, #E8DCC4, bottom-third-left. Three secondary cover lines in 18pt Neue Haas Grotesk
Medium, uppercase, letter-spaced. Small barcode bottom-right, date marker top-left.

Atmosphere: contemporary 2020s, luxurious calm, film grain on surfaces, Portra 400 film stock
character. Signature moves: (1) single shaft of tungsten light cutting diagonally across the
travertine floor from the brass lamp, (2) a leather-bound book face-down on the arm of the
bouclé sofa, (3) fresh orchid stem in a raw ceramic vase on the coffee table, (4) a half-drawn
linen curtain letting a knife-edge of blue-hour light through.

Preserve from uploaded interior: wall positions, window proportions, walnut floor, limewash
walls, coffered ceiling. Transform from uploaded reference: all lighting, mood, atmosphere,
color grading, and cover typography.

Shot on a medium-format digital camera, natural skin texture if figures present, straight
architectural lines with tilt-shift correction, no AI gloss or plastic smoothness.
```

This is approximately 2200 characters — leaves room for more without hitting the 3000 cap.

---
— Add new entries here —
