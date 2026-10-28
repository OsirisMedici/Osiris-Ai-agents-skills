---
name: eden-workspace-feel
description: Capture and apply the Eden-inspired creative workspace feel from Osiris's July 2026 Record & Replay demos. Use when building or revising Orbit, Canvas Vault, creative-workspace flows, board/canvas experiences, swipe files, inspiration libraries, media/reference boards, focused editors, or persistent pane interactions that should borrow Eden's interaction grammar without cloning the Eden product.
---

# Eden Workspace Feel

## Core Rule

Borrow the feel, not the app. Preserve the interaction grammar from the demo: calm creative workspace, dense left navigation, board/canvas center, fast item focus, contextual actions, and reference material that can be chatted with or moved. Do not copy Eden branding, exact copy, URLs, private content, or product-specific feature names unless the user explicitly requests a direct placeholder.

## Required References

Read [references/recording-2026-07-02.md](references/recording-2026-07-02.md) before implementing or reviewing the overall workspace. It contains the observed flow, sanitized structure, and concrete interface patterns.

For focus, split-view, or `Open in Pane` work, also read [references/recording-2026-07-15-pane-behavior.md](references/recording-2026-07-15-pane-behavior.md). It records the persistent-pane behavior demonstrated against a live Canvas comparison.

## Implementation Bias

- Start on the actual workspace surface, not a marketing page.
- Use a persistent left rail/sidebar for navigation, search/create, recent chats or sessions, and nested boards/spaces.
- Make the main area feel like a canvas or board: scrollable, media-rich, and capable of grid/list switching.
- Show contextual actions only when useful: selected item actions, item detail actions, and board-level actions.
- Prefer quiet, utilitarian controls with icons and short labels over decorative explanations.
- Use fast but legible transitions: selected item focus, detail expansion, back navigation, pane open/close, grid/list toggles, and zoom/scale changes.
- Build the user's feature on top of this grammar instead of recreating Eden's exact information architecture.

## Focus And Pane Model

- Treat focus and pane states as related but distinct:
  - Focus makes one artifact prominent and may hide navigation for distraction-free work.
  - A companion pane keeps a second artifact or board visible while the main workspace remains independently navigable.
- Let `Open in Pane` originate from useful surfaces such as a sidebar row, selected-item toolbar, board/card menu, or focused-item toolbar.
- Keep the companion stable while the user navigates folders, boards, or items in the main pane. Do not make every main-pane navigation replace the companion.
- Give both panes an identity and compact controls. At minimum support close and swap; use a draggable divider when the product benefits from adjustable widths.
- When the user swaps panes, preserve each pane's editor state, media position when feasible, and navigation context.
- Let closing the companion return cleanly to a single primary surface. Let closing focus return to the parent board without losing orientation.
- Avoid a picker-only model that merely replaces the companion. A picker can choose the initial companion, but the resulting pane should behave as a persistent workspace.

## Motion And Flow

- Treat click -> select -> act -> back as the primary loop.
- Let a single item become prominent when opened, with surrounding board context still recoverable through a clear Back control.
- Make toolbar/state changes feel immediate; avoid full-page reload effects.
- Keep pane actions available for secondary work: open in pane, chat with, move, download/export, or domain-specific equivalents.
- Preserve editor drafts and scroll position while changing focus, splitting, swapping, or navigating the other pane.
- Use lightweight hover/selection affordances, not heavy cards inside larger cards.

## Visual Direction

- Dense but calm sidebar.
- Spacious canvas/board center.
- Small, stable icon buttons for repeated actions.
- Grid items should feel like collected references or artifacts, not generic SaaS cards.
- Performance/status badges may appear as compact pills when they clarify ranking or importance.
- Preserve generous whitespace around focused content while keeping lists scannable.

## Verification

When building a frontend from this skill, verify the first screen and at least one board/detail interaction in-browser. Confirm:

- Sidebar, board/canvas, and contextual actions are all visible.
- Grid/list or equivalent view mode works.
- Opening an item creates a focused state and Back returns to the board.
- Opening a companion creates two independently useful panes.
- Main-pane navigation does not replace the companion.
- Swap reverses pane roles and Close returns to a coherent single-pane state.
- Text does not overflow compact controls.
- The final UI feels inspired by the recorded workspace without copying Eden identity or private demo content.
