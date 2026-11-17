---
name: scale-design-toolkit
description: Plan, build or review website and product UI design using Scale's shared references, briefs and quality checks. Also use for visual identity, graphic or motion direction. Apply only the requested design scope.
---

# Scale design toolkit

Use the bundled references from any project. They are a portable snapshot of Scale's design toolkit; the current repository remains authoritative for its own product, brand, data and implementation.

Canonical shared source: [OsirisMedici/scale-design-system](https://github.com/OsirisMedici/scale-design-system). Improve shared references, guidance and accepted system patterns in that repository, then rebuild and reinstall its bundle. Installed references are a snapshot. Keep project-specific product decisions in the owning project.

## Work from the outcome

Inspect the actual page, screen or asset and its owning repository. Identify the user's task, what should become easier, and the result that will demonstrate success. Reuse supplied answers and discoverable project facts. Ask only when a missing decision would change the work.

For substantial new design, use [the brief](references/brief.md) to record the outcome, a few annotated references, one visual direction and a representative slice. For a small existing change, apply the relevant fields without creating an unrelated design exercise. Keep useful decisions and acceptance evidence in the owning project.

## Choose the relevant specialist

For an app-directory link, copy-link control or semantic theme, inspect [the implemented pattern candidates](references/implemented-patterns.md) before making another implementation. They link to the canonical source and state what was verified. Adapt them to the owning product and verify its actual behavior.

Read [the library](references/library.md) when choosing resources. Load one specialist for the immediate design problem, rather than combining every skill's defaults.

| Work | Skill or reference |
| --- | --- |
| New website or page direction, or an explicitly requested Hallmark review | `hallmark`. Preserve existing design for ordinary changes. |
| A component or interaction dependency decision | `pick-ui-library`. Inspect installed packages first. |
| Product illustrations and short authored UI demos | `stageshow`. A scripted scene is not acceptance proof of a real app action. |
| A cinematic marketing section or detailed builder prompt | `scale-cinematic-web`. Use only when visual storytelling serves the brief. |
| Product state transitions and interaction motion | The existing `product-motion` skill, when available. |
| Graphic, brand or spatial reference research | Relevant sections of [the video catalog](references/videos.md) and [repository catalog](references/repositories.md); use the current host's suitable design tool. |

Sibling packages are available under the same user skills directory. Read their `SKILL.md` only for the selected branch. These installation adapters take precedence over conflicting upstream defaults in linked resources.

## Implement and verify

Preserve the current product's wiring, content and brand unless the request changes them. Use the project's existing stack; add a dependency only when it serves the authorized task. Apply Osiris's Bun rule for JS/TS work. For browser inspection and visual verification, use the supported in-app Browser; choose purpose-built tools where they cover the operation.

Build the representative slice with real content and the states it needs. Use [the review checklist](references/review-checklist.md) proportionately, including functional behavior, phone/desktop, keyboard/focus, content extremes and reduced motion where relevant. Review motion in playback. Distinguish source inspection, static checks, rendered behavior and acceptance.

Preserve attribution and check the actual code/asset license at use. [Coverage](references/coverage.md) distinguishes descriptions, transcripts and runtime evidence. Resources marked reviewed are not automatically tested or adopted.

Finish with the usable result, how to test it, what was verified and any remaining limitation. Installation grants no additional publishing, paid-service, account or production-change authority.
