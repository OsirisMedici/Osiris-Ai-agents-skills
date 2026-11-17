---
name: pick-ui-library
description: Choose a suitable UI library for a specific component or interaction after inspecting the project's existing dependencies. Use during frontend dependency decisions; preserve an existing working stack.
---

# Pick a UI library

Adapted from Emil Kowalski's curated library guide. The pinned source and MIT notice are retained in `PROVENANCE.json` and `LICENSE`.

Identify the actual interaction, framework and installed packages first. Keep an existing suitable solution; a recommendation alone does not justify dependency churn. For a clear task, recommend one fitting library and explain why. Check its current APIs and maintenance before implementation. Use Bun when adding a JS/TS dependency within an authorized implementation task.

| Task | Starting candidate |
| --- | --- |
| Accessible dialogs, menus, selects and popovers | Base UI, or the project's existing suitable foundation |
| Command menu | cmdk |
| Toasts | Sonner |
| OTP input | input-otp |
| Control panels | Leva; dialkit is an alternative |
| Springs, layout, enter/exit and gesture motion | Motion |
| Changing numbers | NumberFlow |
| Animated text | torph |
| 3D globe | Cobe |
| Dynamic HTML/CSS to image | Satori |
| Syntax highlighting | Shiki |
| Live streaming chart | Liveline |
| General charts | Recharts |
| Drag and drop | dnd kit |
| Long-list virtualization | Virtuoso |
| Shared UI state | Zustand |
| Conditional classes | clsx |
| Typed styling variants | cva |
| Theme switching | next-themes |

A simple hover or color fade can use CSS. Styling variants do not require a new state library. A small static page or native app may need none of this list. When a task falls outside the guide, say so and use primary documentation for the selected alternative.

The source table is a starting shortlist, not proof of compatibility, licensing or accessibility in every app. For component code copied from a catalog, inspect that component and its asset terms. Verify actual behavior, keyboard/focus, responsive states and relevant performance in the owning project.
