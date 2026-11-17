# Video benchmark and next test

Source: [Draw Excalidraw Diagrams in Obsidian with Claude Code](https://youtu.be/_apBzliAD9c), Beomsu Koh. The browser page also presents “Obsidian Visualize: My Open-Source Skill for Canvas, Excalidraw and Mermaid”. Read and captured 9 November 2026.

The source skill lives in [GoBeromsu/secondbrain-skills](https://github.com/GoBeromsu/secondbrain-skills/tree/e14de23c54d381751a4a9a5f00d9a4452d3b1454/skills/obsidian-visualize). We inspected its skill and Excalidraw design reference at that revision. Its output choices are Obsidian JSON Canvas, Excalidraw and Pele/Mermaid. This adaptation targets Canvas's existing Excalidraw Whiteboard.

| Video time | Reference |
| --- | --- |
| [00:10](https://youtu.be/_apBzliAD9c?t=10) | Original wide map, colored groups and small labels. |
| [02:25](https://youtu.be/_apBzliAD9c?t=145) | Three-format comparison and preference for editable Excalidraw. Workflow reference. |
| [03:25](https://youtu.be/_apBzliAD9c?t=205) | Existing map before the larger two-row redesign. |
| [04:25](https://youtu.be/_apBzliAD9c?t=265) | Intermediate map with enlarged groups and routed relationships. |
| [05:18](https://youtu.be/_apBzliAD9c?t=318) | Final two-row map, enlarged labels and single double-headed connectors. Bottom/right content is partly obscured. |

These frames are source references, not proof of Canvas behavior. Preserve timestamps and visible occlusions. Do not invent hidden labels or links. Start with a clearly identified subset rather than claim a complete transcription.

## Ready test prompt

> Use $canvas-visualize on a disposable Canvas Whiteboard named “Visualize reference test”. Recreate a small editable subset of the final map: a Capture group containing capture and inbox, a Compile group containing ingest, and a Use group containing query, verify, audit and lint. Use green entry points, blue inbox, yellow checks, gray outlines and larger labels. Place the core flow in the top row with a source-reference note below. Preserve the observed capture/inbox mutual relationship as one double-headed arrow. Inspect the current tool schema before creating connectors. If it cannot express that arrow or required bindings, report the gap and prepare the supported portion without guessing or changing the relationship. Export editable Excalidraw and PNG, inspect the PNG, reload, and prove the elements remain editable.

Resolve an actual disposable board, or create one through an available authorized app flow. No live board was selected during skill drafting.

## Acceptance

- Record exact board ID, app/build when discoverable, and tool capabilities.
- Match the subset's labels and verified links. Keep an explicit edge list. Identify obscured source material.
- Keep native shapes, text and connectors editable. The reference screenshot is not the deliverable.
- Read every object page and preserve unrelated objects.
- Enlarge labels without clipping. Show the two-row organization and source link.
- Verify bidirectional representation if supported. Otherwise record the gap and distinguish partial creation from a match.
- Save, reread, export, inspect and reload. Report evidence levels separately.
- On a second edit, retain IDs and prove the same nodes were revised. On a conflict, reread and rebuild.

This is the prepared next test. It has not been run on a live Canvas board.
