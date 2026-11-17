# Scale design toolkit

Use this toolkit to turn saved design references into decisions for a real project. Start with the audience and the job, choose a small set of relevant references, and save the patterns that pass review. Keep each project's brand and existing implementation intact.

This first edition draws on Osiris's liked YouTube videos and starred GitHub repositories, reviewed on 11 November 2026. It includes website and product UI, visual identity, motion, creative production and spatial design. The research provides a reference library and templates. Skill installation and runtime checks are tracked separately.

## Start here

1. Fill [the project brief](brief.md) for the page, screen or asset being made.
2. Choose the appropriate resources below. Use the existing project stack before adding dependencies.
3. Build one representative section or interaction, including its relevant states.
4. Run [the review checklist](review-checklist.md), then save the accepted decisions with the owning project.

The complete [video catalog](videos.md) and [repository catalog](repositories.md) preserve the wider collection. [Video notes](video-notes.md) distinguish transcript review from descriptions and chapters. [Coverage](coverage.md) records what was inspected and what remains unverified.

## Saved website inspiration

For saved website examples, landing pages or creative scrolling references,
start with [the website inspiration index](website-inspiration.md) before
searching Canvas and GitHub again. It includes the 60 collected website links,
40 MotionSites example specifications, motion resources and original Canvas
boards. The selected Ather 450 direction is recorded for Dynamic Solution.

## The useful starting set

For existing implementation examples, start with [the implemented pattern candidates](implemented-patterns.md), including the Scale Apps app link, copy-link control and opt-in theme. Their pilot status and evidence are recorded before reuse.

| Need | Start with | Use it for |
| --- | --- | --- |
| A clear design process or an existing-page critique | [Hallmark](https://github.com/Nutlope/hallmark) | Define the page's job, inspect its existing materials and behavior, select a direction, and review a real browser result. Its stylistic preferences must yield to the actual brand and users. |
| Better reference selection | [Alina S. on web references](https://www.youtube.com/watch?v=P2_Rh7u96Sg) and [Louis Moss on moodboards](https://www.youtube.com/watch?v=xJEYViuQifg) | Give each reference a purpose: composition, typography, hierarchy, imagery or behavior. Explain what fits and what must differ. |
| Product UI that behaves correctly | [Griffin Wooldridge on UI libraries](https://www.youtube.com/watch?v=zsCGS-Yzjnw) and [Emil Kowalski's library guide](https://github.com/emilkowalski/skills/blob/main/skills/pick-ui-library/SKILL.md) | Separate foundations, specialist interactions and styled examples. Choose a tool for a specific task instead of rebuilding every control or combining whole design systems. |
| A short product illustration or scripted demo | [Stageshow](https://github.com/benjitaylor/skills/tree/main/stageshow), linked from [the saved AI LABS video](https://www.youtube.com/watch?v=of628n5754g) | Show one action and its result in a simplified version of the product. Design the phone version and static poster separately. These are authored illustrations, not evidence that the real app performed the action. |
| A visual marketing page | [MotionSites](https://github.com/Motionsites-AI/claude-skill) | Write a precise visual specification, select permitted assets, and revise from screenshots. Keep its copyrighted example/media collection as references rather than redistributing a local copy of the collection. |
| A focused interactive graphic | [Hairline](https://github.com/lucasmarkes/hairline) | Use a small interactive SVG when it helps explain the idea. Do not give every brand the same illustration style. |
| A more useful product screen | [Kole Jain's UI critique](https://www.youtube.com/watch?v=PDcQJOPby1k) | Remove irrelevant repeated KPIs and nonfunctional cards; make navigation, settings, color and hierarchy serve the screen's task. |
| A coherent marketing identity | [Kole Jain's visual identity walkthrough](https://www.youtube.com/watch?v=RCneB_MQ7qs) | Set typography, palette, imagery and repeated visual patterns before assembling sections from several sources. |
| A landing-page outline | [Flux Academy's walkthrough](https://www.youtube.com/watch?v=GTNgiTK-ic8) | Check the value proposition, explanation, product visual, proof and next action. Use only the sections the offer needs. |
| Editable design decisions | [Crayon](https://github.com/OsirisMedici/crayon) | Author named components, states and tokens when an editable design file is part of the handoff. The existing app's account access and running revision need their own verification. |

Stageshow and Emil's guide were discovered through liked videos. They are not presented as starred repositories.

## Choose tools by the interaction

These are options for a suitable project, not a requirement to install all of them. Inspect the owning repository and its existing dependencies first. The [saved library video](https://www.youtube.com/watch?v=zsCGS-Yzjnw) was reviewed through its full auto-generated transcript; the [current library guide](https://github.com/emilkowalski/skills/blob/main/skills/pick-ui-library/SKILL.md) provides the task mapping.

| Task | Candidate | Decision rule |
| --- | --- | --- |
| Dialogs, menus, popovers and accessible component behavior | [Base UI](https://base-ui.com/react/overview/quick-start), or the existing Radix-based foundation | Reuse one appropriate foundation. Preserve the project's current components when they already solve the task. |
| Editable styled components | [shadcn/ui](https://ui.shadcn.com/docs) | Treat the copied source as a starting point. Set the project's type, colors and shapes deliberately. |
| Toast notifications | [Sonner](https://sonner.emilkowal.ski/) | Consider when the current toast behavior needs stacking, actions or asynchronous states. Verify screen-reader behavior and reading time in the actual app. |
| Command menu | [cmdk](https://cmdk.paco.me/) | Consider when a real keyboard-driven command/search flow is required. |
| Changing numeric values | [NumberFlow](https://number-flow.barvian.me/) | Use for a meaningful change in value. Keep an immediate, readable result with reduced motion. |
| Simple hover or color transition | CSS | A small state transition does not justify an animation runtime. |
| Spring, layout, gesture or enter/exit choreography | [Motion](https://motion.dev/docs/react) | Add only when the behavior needs it and the stack supports it. |
| Interactive authored illustration | [Rive](https://rive.app/) | A specialist lane for a graphic with authored interaction. Check the selected runtime, export terms and performance before adoption. |
| One visual accent or finished section | The component collections linked in [the UI-library video](https://www.youtube.com/watch?v=zsCGS-Yzjnw) | Choose one piece that fits the identity. Inspect its code, dependencies and individual asset terms. |
| Native Mac UI | [BAMA's design and UX methods](https://github.com/daveebbelaar/bama) | Use native platform behavior and a native component gallery. SwiftUI source is a separate implementation lane from web UI. |

The broader specialist and production options, including recording, video editing, voice, canvas SDKs and architecture examples, are cataloged separately. No universal React stack is imposed on static pages, native apps or non-React products.

## A reusable workflow

### Establish the job

Inspect the real app or page before proposing changes. Record who uses it, their next action, the problem they have today, and the observable result. Decide whether the work is a task-oriented product screen, marketing page, explanation, static visual, recorded demo or spatial concept. Each needs a different structure.

### Collect references with a reason

Choose three useful references rather than a large unannotated folder. For each, record its URL, the exact section or interaction, the decision it informs, why it fits the audience, and what must not carry over. Save real website references for web behavior and separate them from concept art or static mockups. This is Scale's adaptation of [the reference video](https://www.youtube.com/watch?v=P2_Rh7u96Sg).

### Write one visual direction

Specify type roles, color roles, spacing and density, control shapes, imagery and motion purpose. Explain those choices in relation to the job. Keep one direction coherent across the page instead of collecting attractive sections with conflicting identities. Use the existing brand unless the brief asks to change it. [Visual identity walkthrough](https://www.youtube.com/watch?v=RCneB_MQ7qs)

### Build the smallest representative slice

Use the product's real content and a meaningful interaction. Include the empty, loading, error, success, long-text or permission states that the slice needs. Do not fill a task screen with repeated dashboards or controls that perform no action. For a demo illustration, write its one action and payoff before animating. [UI critique](https://www.youtube.com/watch?v=PDcQJOPby1k), [Stageshow source](https://github.com/benjitaylor/skills/blob/main/stageshow/SKILL.md)

### Review and retain what passed

Compare the actual browser or native result with the brief and the chosen references. Check desktop and phone, keyboard and focus, reduced motion, content extremes and real interactions. For motion, watch the sequence and its loop seam; a still cannot verify timing. Save the accepted tokens, component states, screenshot or clip, source attribution and test result in the owning project. [Hallmark](https://github.com/Nutlope/hallmark), [Stageshow verification](https://github.com/benjitaylor/skills/blob/main/stageshow/references/rehearse.md)

## Keep reuse explicit

Track a resource as **reviewed**, **trial candidate**, **tested**, **adopted** or **retired**. Reading a README is reviewed; installing a package is not tested; a working isolated trial is not adoption across every product.

Record the chosen version and the exact code/asset license when a project uses a resource. The catalogs call out mixed licenses, service access and historical examples. In particular, the MotionSites collection has separate restrictions, Stageshow's third-party icons and marks are outside its blanket MIT grant, 21st's proxy license does not grant hosted service access, and tldraw production licensing is separate from development. [MotionSites license](https://github.com/Motionsites-AI/claude-skill/blob/main/LICENSE), [Stageshow notices](https://github.com/benjitaylor/skills/blob/main/stageshow/NOTICE.md), [repository review](repositories.md)

When implementing JavaScript or TypeScript, follow Osiris's Bun rule and the owning project's instructions. Adapt commands to Bun where supported; a library's pasted npm command does not change the workspace default. Keep any required runtime exception documented in that project.
