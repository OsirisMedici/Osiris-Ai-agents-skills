---
name: gap-check
description: Compare delivered work with the user's original plan, brief or inspiration. Use when asked to score how closely an output matches the intended result, explain the gaps and their causes, and identify how to close them.
---

# Gap check

Judge how well the actual output delivers the user's intent. Return a score out of 100, the meaningful gaps, why they exist, and concrete ways to close them. Apply to product work, designs, writing, videos, campaigns and other deliverables.

## Establish the comparison

Identify both the original plan or inspiration and the exact output being reviewed. Recover them from the current chat, supplied files and links, or the owning project's brief and decisions. Inspect the artifacts themselves. Use relevant connected tools and available domain skills; for browser inspection use the visible in-app Browser.

If either side cannot be identified or accessed, ask for that specific missing input. Prepare any supported comparison while waiting, and reserve the score until there is enough evidence to assess both sides.

Summarize the baseline in a short paragraph: intended audience, outcome, essential requirements, and the qualities to carry over from the inspiration. Separate explicit requirements from your interpretation. Honor the user's approved scope changes and identify which version governs the review. Resolve contradictions that would materially change the score.

Treat inspiration as evidence of the desired qualities. Identify what matters, such as hierarchy, rhythm, interaction, tone or atmosphere. Judge literal similarity when the user requested replication; otherwise evaluate whether the output carries those qualities into its own context. Keep your personal taste separate from the agreed intent.

## Inspect and score

Build a small rubric from that baseline before judging the output. Use observable criteria with weights totaling 100. Prioritize the user's stated priorities; if weights are unspecified, choose and disclose reasonable weights. For a product, the core user outcome and required behavior should outweigh decorative polish. For a visual reproduction, reference fidelity may carry the most weight.

Inspect the actual delivered version at the level needed for each criterion. A screenshot supports appearance; inspect interactions to assess behavior. Distinguish source code, a prototype and the deployed product. For video, inspect timing and audio when relevant. Describe any access or verification limits.

Award each criterion between zero and its full weight. Show a compact table with criterion, earned points / weight, and the supporting observation. Add the earned points for the headline score; round only the final result to a whole number. Avoid overlapping criteria or deducting twice for the same defect.

Use these anchors within each criterion:

- Full credit: the requirement is demonstrated in the reviewed output.
- Mostly met: the intended result works, with small departures that have limited effect.
- Partly met: meaningful elements are present, but a substantial gap affects the result.
- Little or no credit: the requirement is largely absent or the intended result fails.

Withhold points for unverified claims and mark them unverified, distinct from demonstrated failures. If uncertainty could materially change the result, label the score provisional, state the unverified point weight, and give the possible score range. A fully inaccessible output receives no numeric score. Treat scores as a reasoned assessment, not an objective measurement.

State clearly when a non-negotiable or the core outcome fails, even if other criteria earn a high total. Reserve 100 for a fully demonstrated match across the agreed scope. Extra features earn credit only when they serve that scope.

## Explain and close the gaps

Rank gaps by their effect on the intended outcome. For each material gap, connect:

- **What's the gap?** Contrast the intended result with the observed result. Cite the relevant reference and output evidence using links, file lines, screenshots or timestamps as appropriate. Explain the consequence for the audience.
- **Why?** Give the supported cause. Separate observed symptoms from inferred causes. When the cause is uncertain, name it as a hypothesis and identify the smallest check that would confirm it. Attribute intent or effort only when evidence supports it.
- **How to fill the gap?** Specify a concrete change and an observable acceptance check. Identify which rubric points it could recover. Keep suggestions within the user's constraints and preserve what already matches.

Consolidate related symptoms under their shared cause when one correction addresses them. Keep optional improvements beyond the brief separate from scored gaps. For a complete match, say that no material gap was found rather than inventing faults.

For a repeat review, retain the baseline and rubric unless the user changed the brief. Report the previous and current scores, what improved, and the remaining gaps. Do not raise the score merely because fixes were claimed; inspect the revised output.

## Present the result

Lead with the actual score on its own line, for example:

**72 / 100**

Follow with a one-sentence verdict and the baseline/version reviewed. Put a provisional label and material evidence limitations next to the score when needed. Include the compact scoring table so the number can be checked.

Use the user's questions as the main sections:

### What's the gap?

List the material gaps in priority order with their evidence and impact. Use stable numbers so each gap connects to its cause and fix below.

### Why?

Explain the cause of each numbered gap, distinguishing confirmed causes from hypotheses.

### How to fill the gap

Give the corresponding changes and acceptance checks, highest impact first. End with the first useful action, not a generic offer to help. Keep a small review short; expand only when the work warrants it.

This skill produces a review. Implement corrections when the user's current request authorizes that work; otherwise leave a concrete, reviewable fix plan. Create issues, publish reports or send feedback externally only within the user's authorization.
