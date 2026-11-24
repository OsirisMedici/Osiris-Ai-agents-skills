---
name: crayon-scale
description: Turn a product or feature discussion into editable Crayon UI designs, iterate on feedback, and prepare the accepted design for full-flow implementation. Use for "crayon scale", discussion-to-design requests, or revisions to that design.
---

# Crayon Scale

## Public setup

Resolve the user's authorized workspace before following file paths below.
`<workspace>` and named vault folders describe an existing layout, not bundled
data. Reuse equivalent files in the user's setup. Ask for a destination only
when discovery cannot resolve it. Private records and reference documents must
be supplied or located locally; do not invent their contents. Reuse answers
already in the request rather than repeating the intake. Use available supported
tools and the visible in-app Browser for browser work. Installing this skill
does not invoke it or authorize messages, publishing or unrelated service writes.

Turn settled product decisions into a reviewable Crayon design. Keep feedback in the same design, then leave an implementation contract that `$full-flow` can consume. Installing this skill does not start a design run. Design invocation authorizes relevant design work, not app implementation or deployment.

## Recover the brief

Read the current discussion, corrections, supplied references and existing project decisions. Identify the owning repository, current product, existing design and unfinished work. Inspect the actual UI and relevant data model before designing an existing feature. For a new product, distinguish confirmed decisions from assumptions. Recover a specifically referenced chat through available chat tools when needed; ask for missing context only when it cannot be recovered.

Apply the installed `scale-design-toolkit` skill and its relevant brief/review guidance. Preserve the current product's visual language unless the discussion calls for a new direction. For a new product, choose and explain a direction suited to its users.

Consolidate who uses it, their task and desired result, primary journey, scope, devices, non-negotiables and observable acceptance criteria. Preserve settled answers instead of restarting the interview. Ask through native question input only when an unresolved choice materially changes the result. Continue independent work while waiting. Choose reversible details and record their reasons.

Explain briefly, in order, what will be designed, why, the finished experience, included/excluded scope, the Crayon approach and how it will be reviewed. Proceed without a routine plan-approval pause.

Use the project's existing design/progress location. Otherwise use `docs/design/<feature-slug>/` in the owning repository. If ownership is unknown, use a named local working folder and record that uncertainty. Reuse these records across rounds:

- `design-brief.md`: consolidated outcome, decisions, assumptions and scope.
- `design-handoff.md`: design identity, status, review evidence and implementation contract.
- `evidence/`: useful exports, without credentials or session material.

## Connect to the right editor

Discover purpose-built Crayon tools and read their `high_level_overview` before other operations. Verify product and target session. Crayon is the Penpot-based UI design app. Chalk is a separate architecture editor whose descriptions can mention Crayon because it reuses its shell.

Read [the connection guide](references/connection.md) when available tools belong to Chalk, no suitable Crayon connector is exposed, or recovery is needed. It includes a registered direct MCP fallback. Use supported APIs and current member documentation rather than guessing methods or writing raw database content.

Inspect caller-owned sessions, workspace permissions, current file and page. Reuse the feature's file or create a clearly named file in the resolved project. Ask for the target only if multiple plausible workspaces remain after discovery. Preserve unrelated designs. Reacquire objects after navigation. Store durable project/file/page/board IDs and authenticated editor links in the handoff, not transient session IDs.

Use the visible in-app Browser for browser work and interaction verification. If manual connection is required, give the exact step and preserve the prepared brief. Report blocked work as partial. A prompt or local image alone is not a completed Crayon design.

## Build and review

Create native editable boards, text, controls and reusable components. Use tokens and flex/grid where they help later edits. A flattened screenshot is a reference asset, not the UI design deliverable. Prefer realistic synthetic content where private data is unnecessary.

Establish hierarchy and density with a representative journey, then cover the agreed scope in the same run. Do not impose approval for every screen. Include the states the feature needs, such as empty, loading, validation, error, success, permission restrictions and long content. Provide boards for agreed devices and record behavior between sizes. Avoid inventing a mobile app for a desktop-only request.

Keep actions consistent with the real product and data model. Label future capabilities as proposed. A designed action does not prove backend support. Link the primary journey with prototype interactions when supported. Identify illustrative or unconnected controls in the handoff.

Before presenting each round:

- Wait for layout updates. Inspect containment and actual text bounds, especially long labels and dialogs. Respect layout systems when positioning children.
- Export and visually inspect changed boards. Correct clipping, overlap, weak hierarchy and illegible text in the actual output.
- Try the core prototype journey when available. Record static checks separately from interaction checks and future app checks.
- Confirm backend save acknowledgement with the supported save/wait tool. An edit call or export is not proof of saving. Recheck active file after navigation or human edits.

Return an authenticated design link, useful previews, changes and unresolved decisions. Public share links, invitations and role changes require the user's explicit request.

## Iterate on feedback

Treat subsequent feedback as revisions to this feature. Read the current file and handoff first, including human changes. Edit in place while preserving accepted decisions and unrelated work. Create clearly named alternatives when requested or useful for a specific tradeoff.

Record material feedback decisions and affected boards in the handoff. Recheck affected screens/journeys, save and show the result. Update the brief for scope changes. Surface consequential conflicts with prior decisions instead of silently changing the product contract.

Use `draft` for incomplete design, `in-review` for saved work awaiting feedback, `accepted` when Osiris accepts a specific revision, and `superseded` for replaced candidates. Silence is not acceptance. Natural instructions to build the latest reviewed design can constitute acceptance. Further changes return the new revision to `in-review` until accepted or explicitly authorized for building.

## Prepare the implementation handoff

Keep `design-handoff.md` current during review. Identify the accepted revision with a saved checkpoint/version where supported, or timestamped exports and board IDs otherwise. Reuse the project's equivalent format if present. Include:

- Status, feature, owning repository/checkout and inspected source revision.
- Authenticated Crayon URL, project/file/page/board IDs, accepted checkpoint and acceptance instruction/date.
- Outcome, included/excluded scope and observable acceptance criteria.
- Screen/state/viewport map, main journey, existing components and API/data dependencies.
- Actual typography, colors, spacing, component variants, responsive rules and interactions needed to reproduce the design. Extract values from the accepted design.
- Evidence paths, save acknowledgement, prototype checks, assumptions and blockers.
- A build instruction pointing to this file, the accepted design and existing owning task/issue.

Offer `Use $full-flow to build the accepted design in <absolute design-handoff.md path>.` A later build request or `$full-flow` invocation begins implementation. Design work alone ends with the reviewable design and handoff. If the user already requested design followed by implementation, honor that scope and any stated review boundary without asking again.

For revisions, resume the existing design. For building, load `$full-flow` and use the accepted contract as its UI specification. Preserve outcome and data model as well as appearance. Verify implemented screens against accepted boards. State unsupported APIs, untested prototype behavior and unresolved dependencies plainly.
