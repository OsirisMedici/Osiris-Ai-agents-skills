# Eden Workspace Recording Notes - 2026-07-02

Source: Record & Replay, captured from 08:00:04Z to 08:02:39Z. These notes intentionally sanitize private board contents and should be treated as design evidence, not a replay script.

## Observed Timeline

1. Start in Codex, switch from Dock into Eden web app.
2. Land on Home with a left workspace sidebar and a main getting-started/recents surface.
3. Open a board/folder from the Boards section.
4. Use browser zoom shortcuts to inspect density.
5. Open board settings, inspect sort/version/template-related actions, then return to the board.
6. Toggle between List and Grid view.
7. Select media/image items in a board; selected item actions appear.
8. Double-click/open items into a focused state; Back returns to the parent board.
9. Navigate across nested boards from the sidebar, including inspiration/swipe-file style boards.
10. Open saved media/post examples, showing preview/player or text-card details with actions.
11. Return to Codex after the demo.

## Shell Of The App

- Top browser/app chrome is not part of the product pattern.
- Product shell uses a persistent left sidebar.
- Sidebar begins with `Create or search`.
- Primary navigation includes Home, Discover, Briefs, More.
- Sidebar sections include Chats and Boards.
- Board rows can have an adjacent `Open in Pane` action.
- Some board rows behave as folders with nested boards below them.
- User/account and Trash sit near the lower sidebar.
- A draggable sidebar splitter/resizer is present.

## Board/Canvas Surface

- Main board region is exposed as a `Workspace canvas`.
- Board-level toolbar appears near the canvas: Add to board, Chat, Share.
- Board header includes Back to parent, editable title, Grid/List view mode, and Board settings.
- Boards can contain images, videos, text references, and instructional text blocks.
- Grid view is visually central for media/reference boards.
- List/detail style surfaces are used for swipe files and saved examples.
- Browser zoom changes were used during the demo, so density should be resilient across scale.

## Selection And Detail Pattern

- Clicking a media artifact selects it and reveals a contextual toolbar.
- Common selected actions: Move to Board, Open in Pane, Chat with, Download.
- Double-clicking an item opens or enlarges it into a focused/detail state.
- Focused states retain a Back control naming the parent board.
- Detail surfaces may add item-specific actions such as Chat, Boost in chat, Open original, Download thumbnail, or media player controls.
- Returning should restore the parent board without losing orientation.

## Reference/Swipe File Pattern

- Swipe-file boards mix saved external examples with editable guidance text.
- Example cards include creator/source metadata, engagement/performance numbers, and a compact performance badge.
- Each example tends to expose a quick "chat/boost/add to list" style action near the item.
- Guidance text explains what the board is for and how references are used as pattern material, not copied one-to-one.
- For Orbit, translate this into the user's domain: saved references, source cards, rationale, scores, actions, and AI-assisted analysis.

## What To Borrow

- Persistent sidebar plus deep board tree.
- Fast board switching from the sidebar.
- Canvas-first main workspace.
- Grid/list toggle.
- Contextual toolbars for selected artifacts.
- Pane/detail actions that keep users oriented.
- Back controls that name the parent.
- Reference examples as first-class materials.
- Compact badges for ranking, score, status, or performance.
- Chat/AI actions attached to boards and selected artifacts.

## What Not To Copy

- Eden name, URLs, onboarding copy, or exact feature labels.
- Private board names or captured user content.
- Exact social posts, media thumbnails, or creator lists from the recording.
- Eden's product scope. The target app should use this feel for Orbit's own feature set.

## Orbit Adaptation Prompts

- What is the left sidebar tree for this feature: projects, boards, campaigns, rooms, or assets?
- What is the main canvas collecting: references, screenshots, client inputs, content ideas, product records, or tasks?
- What should a selected artifact let the user do: move, inspect, chat, compare, export, annotate, or convert?
- What does "Open in Pane" mean in this app: split view, side inspector, editor, preview, or analysis panel?
- What compact score or badge helps users scan value quickly?
