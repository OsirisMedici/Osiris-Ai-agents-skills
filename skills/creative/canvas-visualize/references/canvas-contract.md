# Inspected Canvas contract

Source: `OsirisMedici/canvas-core` at `f13a1a379c71aecb0e4ea498bf30dbd3928ecf72`, inspected 9 November 2026. Read `src/lib/canvas-webmcp-drawing-tools.ts`, `canvas-webmcp-contract.ts`, `excalidraw-scene.ts`, and `docs/focused-core-and-board-duplication.md`. Recheck the running app before use.

| Tool | Purpose |
| --- | --- |
| `canvas_get_board` | Exact open board, revision, access, bounded summary and capabilities. |
| `canvas_list_whiteboard_objects` | Paginated geometry, text, style, groups and bindings. Follow `nextCursor`. |
| `canvas_find` | Find identities by ID, type or text. |
| `canvas_show` | Focus up to 20 existing IDs. |
| `canvas_apply_whiteboard` | Bounded native changes with strict persisted save. |
| `canvas_export_whiteboard` | Native `.excalidraw`, PNG or SVG download receipt. |

Workspace tools may include `canvas_list_boards` and `canvas_open_board`. Registration follows current board and access. A viewer does not receive mutation or export tools in this implementation.

## Manifest rules

Required fields are `requestId`, a UUID, and `expectedRevision`, a nonnegative integer. Include `create`, `update`, `group` or `ungroup`. At most 40 total create/update changes fit in a batch.

Creation supports rectangle, diamond, ellipse, text, arrow, line and frame. Coordinates are finite, between -100000 and 100000. Width and height are between 1 and 20000. IDs contain 1 to 80 ASCII letters, digits, underscores or hyphens. Text is at most 5000 characters and must be nonempty on a text object.

Create text separately. A shape's `text` field does not create a bound label here. Font styles on a non-text object are rejected. Grouping can keep separate text and shapes together.

Styles include six-digit hex colors or transparent, stroke width 1 to 8, solid/dashed/dotted strokes, fill style, roughness 0 to 2, opacity 1 to 100, font size 12 to 96 and supported families. Families include Excalifont 5, Nunito 6 and Helvetica 2. Object links accept absolute HTTP, HTTPS or mailto URLs, or null.

Arrow `startId` and `endId` must refer to new rectangles, diamonds or ellipses in the same manifest. The constructor derives points from positive width and height. It does not accept points, signed deltas, explicit arrowheads or route bends. Do not assume arbitrary horizontal, vertical, reverse or curved paths work. Inspect the render.

Updates accept ID plus geometry, angle, text, style, link, locked and deleted fields. They do not accept bindings or arrowheads. Grouping requires all members of existing groups and rejects grouping frames themselves. To avoid frame clipping, use a neutral rectangle as a visual zone when connectors cross its boundary.

## Gaps that affect this video

- One double-headed arrow per mutual relationship cannot be requested through this schema.
- Adding a bound arrow between existing nodes or changing bindings in place is unavailable.
- Image upload, web embeds and Mermaid conversion are unavailable in the drawing pack.
- Native storage requires image bytes in `files`. The video's URL-only image convention does not transfer automatically.
- Summaries truncate long text, point lists, groups and links. A supported full read or export may be needed for exact preservation.
- A save receipt may show only eight affected IDs. Enumerate the board for full verification.

The internal scene is `{engine:"excalidraw",sceneVersion:1,elements,appState,files}`. This differs from native `.excalidraw` export. Do not write directly to storage or treat a generated file as an imported board.
