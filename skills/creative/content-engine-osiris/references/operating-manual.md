# Content Engine Osiris Operating Manual

## Product Essence

Content Engine Osiris is a local-first content production room. It is not mainly a UI project anymore. Its job is to help Osiris and agents think through a post, write the caption, compose editable carousel slides, export post-ready images, and copy the caption quickly.

The product is useful because it keeps content work in one local device-owned workspace instead of scattered across rented platforms.

## Locked Product Rule

During a content production run, agents must not change the app itself unless Osiris explicitly approves that change.

When Osiris says "work on the canvas," the agent should treat the canvas as the place to arrange the writing, not as permission to redesign the visual direction.

This means:

- Add the words to the canvas.
- Split caption ideas into slide text layers.
- Move, resize, align, and format text layers.
- Keep visuals/backgrounds/media unchanged unless Osiris explicitly asks for visual work.

This means no silent edits to:

- UI layout
- sidebars
- typography controls
- caption preview structure
- canvas controls
- export logic
- storage logic
- app copy or product labels
- CSS/JS behavior

Agents may still operate the app, create assets, write captions, export files, and organize folders.

If a product bug blocks content production, the correct move is:

1. State the exact blocker.
2. Explain the smallest proposed UI/product change.
3. Ask for permission.
4. Only then edit code.

## Content Workflow

Start every post with the caption. The carousel supports the caption; it does not need to carry every idea.

Preferred sequence:

1. Capture the user's raw thought.
2. Rewrite the caption in Osiris's voice.
3. Make it readable, human, and lightly imperfect.
4. Avoid unnecessary hashtags.
5. Avoid ending every sentence with a full stop.
6. Create the carousel as visual memory, proof, emotion, or story.
7. For normal canvas work, place the words first and leave existing visual choices untouched.
8. Use the app to adjust the output, not to redesign the app.
9. Export slides.
10. Copy caption exactly with spacing.

## Canonical Paths

- App: `/Users/osirismedici/Desktop/ScaleOS/canvas-v3-private/marketing/canvas-v3-first-post/carousel-engine.html`
- Product manual: `/Users/osirismedici/Desktop/ScaleOS/canvas-v3-private/marketing/content-engine-osiris/PRODUCT.md`
- Client template guide: `/Users/osirismedici/Desktop/ScaleOS/canvas-v3-private/marketing/templates/content-engine-client-template.md`
- Brand blueprint: `/Users/osirismedici/Desktop/ScaleOS/canvas-v3-private/marketing/OSIRIS_TECH_BRAND_BLUEPRINT.md`

## Client Template Pattern

For other clients, create a new company folder and post folder. Keep the app pattern, but do not mutate the canonical engine unless Osiris approves.

Recommended structure:

```text
marketing/
  companies/
    client-slug/
      approved-slide-images/
      inspirations/
      brand-notes.md
  client-slug/
    post-slug/
      carousel-engine.html
      caption.md
      brief.md
      slides/
      assets/
```

For a client copy, it is acceptable to adapt content, caption, company images, slide text, and exported files. Product/UI changes still need approval unless Osiris explicitly says the client copy is experimental.
