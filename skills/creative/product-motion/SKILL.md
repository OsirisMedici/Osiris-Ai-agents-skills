---
name: product-motion
description: Design, implement, and review purposeful product UI animation. Use during frontend feature work that adds or changes interactive states, product design involving transitions, motion polish, and animation bug or interaction reviews, even when animation is not explicitly requested. Apply proportionately to the affected interaction. Skip backend-only work, static copy edits, and video animation.
---

# Product motion

Help users recognize state changes and act without waiting. Apply these defaults to the affected interaction alongside the project's design system. Adding no animation is a valid result. This is Osiris's working synthesis of public animations.dev material and Emil Kowalski's essays, not the author's packaged course skill.

## Understand the interaction

Inspect the existing component, live behavior, motion tokens, input methods and installed library before proposing changes. Identify the user's task, how often they repeat it, and what motion would communicate. Ask a product question only when the answer would change the result and cannot be discovered locally.

Keep the assignment's scope. For ordinary frontend work, consider motion where state changes; that does not require animating the page or redesigning unrelated components. Preserve established motion conventions unless the task or observed behavior justifies changing them.

## Choose motion by purpose

- Name the benefit: feedback, orientation, continuity, explanation, or occasional delight. Frequent command menus, arrow-key selection and repeated shortcuts should respond immediately. Preserve visible focus and meaningful loading or success feedback.
- Start routine transitions near 200ms, usually below 300ms. Tune for travel distance and repetition. Longer illustrative sequences can be appropriate; these values are starting points, not limits for every animation.
- Choose easing by the change. Use ease-out for responsive entrances and exits, ease-in-out for elements already visible that move or morph, ease for gentle hover colors, and linear for constant movement or timed progress. Slow-starting ease-in often delays perceived response. Custom curves are optional tuning choices; reuse project tokens first.
- Preserve spatial relationships. Anchor a popover's transform-origin to its trigger, including after collision handling flips placement. Keep navigation direction and entry or dismissal direction understandable.
- Try a subtle press scale near 0.97 where it fits the component. Small popovers can enter from near-full scale, roughly 0.95 to 0.98, rather than zero. Keep these optional, especially for dense controls and text-heavy surfaces.
- Delay the first tooltip to prevent accidental activation. Once the group is active, let adjacent tooltips appear immediately, usually without another animation. Use the library's existing group or delay controls.
- Use restrained springs when continuity, interruption or decorative movement benefits. Keep precise crosshairs, measurements and direct manipulation connected to input; spring lag can reduce their usefulness.

## Implement the affected states

Prefer the existing library and native CSS facilities that express the interaction. Verify current APIs from the installed project and official documentation when needed.

- Keep state transitions interruptible. Rapid open-close, hover reversal and arriving toasts should retarget from their current appearance. CSS transitions suit many changing targets; choose keyframes for suitable sequences rather than assuming they retarget automatically.
- Declare the intended transition properties explicitly instead of transition-all. Transform and opacity are useful performance defaults; size and layout animation require checking actual rendering cost. Neither CSS nor a library name guarantees compositor execution.
- Gate decorative hover effects by hover capability and retain tap and keyboard access. Read the installed framework's behavior before adding duplicate handling.
- Honor prefers-reduced-motion. Remove nonessential spatial movement, springs and looping effects, using immediate state changes or a restrained fade where useful. Retain the information conveyed by the interaction.
- Use brief blur only as optional polish after fixing timing and continuity. Check text clarity and rendering cost before keeping it.

## Verify and hand off

For implementation or rendered review, use the in-app Browser. Check the affected states at normal speed, rapid reversal and repeated activation, keyboard, touch behavior where relevant, reduced motion, and performance during representative loading or interaction. Reuse existing checks where they provide evidence. Record and scrub a difficult transition only when normal-speed inspection cannot explain the issue.

Compare with an instant version when the benefit is uncertain. Keep the motion when it improves the user's task. A code review or planning task should report the checks it could perform and the runtime checks still needed; it does not require unrelated implementation or deployment.

Finish with what the user can now do, how to test the changed interaction, what was verified, and any limitations. Distinguish code inspection from rendered behavior.

## Sources

Read [references/sources.md](references/sources.md) when tracing a principle, revisiting examples, or extending the guidance. Core use is self-contained. Treat source dates and historical library examples as context; check current APIs before reusing code.
