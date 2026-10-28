# Eden Pane Behavior Recording Notes - 2026-07-15

Source: Record & Replay, captured from 11:10:02Z to 11:12:54Z. These notes sanitize workspace names, URLs, and content. Treat them as interaction evidence, not a replay script.

## Demonstrated Comparison

1. In Canvas Vault, open a saved document into the source viewer.
2. Expand it into distraction-free focus, return to the board, then repeat to confirm the focus/back loop.
3. Open a media source in focus and add a second media source through `Open in pane`.
4. Replace the companion several times through a picker.
5. Open Eden and navigate from its workspace home into nested boards.
6. Open a document/item detail, expose item actions, and use `Open in Pane`.
7. Keep the resulting companion visible while navigating through other folders and boards in the main workspace.
8. Open an item in the main pane while the companion remains present.
9. Observe explicit `Swap with main pane`, `Swap with other pane`, `Close pane`, and draggable swap/divider affordances.

## Important Interaction Difference

Canvas's first implementation proved the focus and 50/50 presentation, but its picker treated the companion mainly as a replaceable selection. The Eden demonstration showed a stronger model: the companion is persistent workspace state.

- Main-pane navigation and companion-pane state are independent.
- The sidebar remains useful for driving the main pane while the companion stays put.
- Pane controls are local and reversible: swap roles, close one pane, return to one surface.
- `Open in Pane` is available close to the source: sidebar rows, board/item actions, or context menus.
- Opening an item inside one pane changes that pane without destroying the other.
- The divider communicates that both sides are first-class working surfaces, not a modal plus inspector.

## Product Translation

Use product-native names and content. For Canvas Vault:

- Primary pane: current board or focused source/document.
- Companion pane: pinned document, media source, PDF, post, or board reference.
- Initial inputs: current item, chosen companion, optional preferred side/width.
- Stable state: companion identity, each pane's scroll/editor state, and current board navigation.
- Controls: Open in pane, Swap, Close pane, Back to board, and optional resize.

## Acceptance Checks

- Open a document alone in focus and return without losing the draft.
- Add a media or document companion and render both at once.
- Navigate to another board or item in the primary pane; the companion must remain unchanged.
- Swap panes; both artifacts must remain present and usable.
- Close either pane; the remaining artifact must become the coherent primary surface.
- Confirm compact toolbar labels do not overflow and both panes remain usable at common desktop widths.
