---
name: stageshow
description: Create still product illustrations and short animated UI demos with a focused story and a separate compact layout. Use for marketing or documentation illustrations rather than real application automation.
---

# Stageshow for Scale

Adapted from Benji Taylor's Stageshow. The pinned source, MIT license and third-party notices are retained with the kit and examples. Use this entry point; project instructions and the current user's brief take precedence over conflicting upstream defaults.

These are authored illustrations. The kit draws a cursor and changes scene state; it does not perform the depicted operation in a real product. Label that distinction in acceptance evidence.

## Plan the illustration

Inspect the product and the place the illustration will appear. Decide the focal object, one action, its payoff and what detail can be omitted. Reuse the product's type, colors, icons and component language. A short sequence of three to five beats is a useful starting point, not a requirement for every subject.

Read `references/framing.md` and the relevant parts of `references/craft.md` for a still. For an animation, also read `references/motion.md`. Choose a close example from `examples/` for structure and adapt it to the actual product. Read `references/kit.md` only for the kit parts being used. The compact design should suit its available width rather than simply shrinking the desktop composition.

Use real words where they communicate the story, with subordinate detail simplified. Keep the result legible and visible long enough to understand. Use a static poster that communicates the outcome, plus a reduced-motion state. A branded product's genuine requirements take precedence over illustration-style defaults.

## Build in the owning project

Copy only the selected kit, example and permitted assets the project needs. The kit targets React; use the existing project stack and current dependencies when it is unsuitable. Do not add a framework merely to use an illustration.

Apply Osiris's Bun tooling rule. Install runtime dependencies into the owning project only when the current implementation request needs them. Skill installation itself does not install the playground or its dependencies. Brand marks and app artwork in the package remain subject to `NOTICE.md` and per-file notices.

## Rehearse through supported tools

Use the supported in-app Browser to inspect desktop and compact layouts, actual playback, cursor targets, transitions, text fit, reduced motion and the loop seam. Capture a clip or contact sheet when a supported capability exists and it helps review. Do not use the upstream filming/browser-launch scripts to control another browser or install a browser.

`references/rehearse.md`, `references/review.md` and `references/verify.md` supply useful checks and the handoff-note structure. Their mandatory command-based filming gate is replaced in this installation by the supported visual checks above. Report exactly what was checked; an unavailable clip or gate remains unverified, and a still does not prove smooth motion.

Hand off the illustration, how to preview it, its tested dimensions, actual evidence and any remaining issue. Preserve license notices and follow the project's completion and publishing instructions.
