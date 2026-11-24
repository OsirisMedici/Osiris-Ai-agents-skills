---
name: full-flow
description: "Run a software outcome through clarification, specification, dependent tickets, implementation, review and retro with minimal user input. Use when Osiris asks for the whole development flow while he is busy."
---

# Full Flow

## Public setup

Resolve the user's authorized workspace before following file paths below.
`<workspace>` and named vault folders describe an existing layout, not bundled
data. Reuse equivalent files in the user's setup. Ask for a destination only
when discovery cannot resolve it. Private records and reference documents must
be supplied or located locally; do not invent their contents. Reuse answers
already in the request rather than repeating the intake. Use available supported
tools and the visible in-app Browser for browser work. Installing this skill
does not invoke it or authorize messages, publishing or unrelated service writes.

Take the supplied outcome, issue or unfinished feature through all six stages in
one active run. Own implementation and verification; do not end after producing
a plan, spec or ticket list. Resume an existing run instead of recreating it.

This is Osiris's unattended adaptation of
[Matt Pocock's main flow](https://www.aihero.dev/skills): grill-with-docs →
to-spec → to-tickets → implement → code-review → retro. The procedure below is
self-contained. It does not require those six slash commands to be installed
or an interactive interview at every transition.

## Decide while Osiris is busy

- Carry forward his actual outcome, corrections, constraints and existing
  authorizations. Discover repository and product facts yourself.
- Invocation delegates routine implementation choices and low-impact,
  reversible product defaults. Record the chosen default and its reason.
- Ask only when an unresolved choice materially changes the audience, purpose,
  data exposure, cost, irreversible behavior or definition of success, or when
  the next step truly needs human action. Use the harness's native question
  tool, batch independent decisions and give a recommended answer.
- Keep working on independent requirements while a question is pending. A
  missing reply is not approval. Leave dependent work explicitly blocked.
- Spec, test-seam and ticket-granularity reviews happen inside this flow using
  the agreed outcome and evidence. They do not require routine user sign-off.

This skill changes the workflow, not the task's permissions. Complete any
already-authorized commit, PR, merge or deployment through its actual checks.
For release actions without authorization, finish the local reviewable result
first and request only the remaining permission. Preserve boundaries on
customer contact, secrets, production data and external access.

## Start and keep state

Read applicable project instructions, inspect the real product and repository,
and locate the existing issue and working changes. Verify the owning host and
checkout. Preserve unrelated dirty work; establish the baseline commit plus
the starting dirty changes before editing so review can distinguish this run.
If overlapping changes cannot be separated safely, resolve that boundary before
editing them. Use the project's tooling and current deployment conventions.

Use the existing project progress location when available; otherwise create
`.scratch/full-flow/<outcome-slug>/`. Keep these working records there:

- `state.md`: outcome, original constraints and grants, repository/base,
  starting dirty changes, owned paths, stage status, decisions, open questions,
  evidence links and next action.
- `spec.md`: the intended behavior and acceptance criteria.
- `tickets/`: one file per independently verifiable slice, with dependencies.
- `review.md` and `retro.md`: findings, resolutions and lessons from this run.

Reuse equivalent existing artifacts rather than duplicating them. Record a
stage as pending, in progress, verified or blocked, with evidence for verified.
Update state at stage transitions and before an interruption. On resume, read
it and inspect current reality; rerun checks invalidated by later changes.
Keep credentials and personal message content out of these artifacts.

### Build from an existing design

When the request or project records identify a Crayon Scale design, read its
`design-handoff.md` and inspect the linked current design before writing the
spec. Carry its outcome, accepted screens/states, tokens, responsive rules and
acceptance criteria into the implementation contract. Reuse its brief instead
of restarting discovery. Compare the implemented UI against its accepted boards
during verification, and record any agreed deviation.

Bind the build to the accepted checkpoint. An explicit instruction to build the
latest reviewed design counts as acceptance of that revision. If it changed
after acceptance or materially conflicts with the requested outcome, resolve
that specific difference while continuing independent work. A static mockup
does not establish backend capability or app behavior.

## 1. Clarify and document

Establish who will use the change, what they should accomplish, why it matters
and how success will be observed. Inspect the existing workflow and data model.

Challenge the plan before building: walk consequential decisions and the
decisions they depend on. Answer factual questions from evidence, preserve
settled user choices, and distinguish assumptions from confirmed decisions.
Check access boundaries, failure and recovery behavior where the feature needs
them. Resolve reversible details yourself; use the busy-mode question rule for
the remaining choices. Revisit the consequences when a decision changes.

Record domain terms and architectural decisions in the project's existing
glossary/ADR conventions when useful; otherwise keep them in the run's spec.
Explain the intended experience and tradeoffs briefly before implementation.

## 2. Write the spec

Write a spec proportional to the work: user problem, proposed behavior,
relevant user stories, included/excluded scope, key implementation decisions,
test seams and observable acceptance criteria. Include data migration and
rollback behavior when they are part of this change. Distinguish simulated
verification from provider, device and live-user acceptance.

Check it against the original request and known constraints. An unanswered
material choice must remain an explicit dependency, not invented agreement.
Save locally by default; reuse/update the owning issue when authorized. An
absent tracker setup is not a reason to stop local implementation.

## 3. Make dependent tickets

Split the spec into the fewest useful end-to-end slices. Each ticket names the
user-visible result, blockers and acceptance checks, and fits in a fresh
context window. A small task may need one ticket. For a wide mechanical
migration, use expand, migrate and contract steps that preserve working callers.

Check that every acceptance criterion has an owning ticket and that dependency
edges are necessary and acyclic. Keep tickets local unless tracker publication
is authorized. Reuse existing issues; avoid creating a new public issue for
each internal implementation step by default.

## 4. Implement and prove

Work through tickets whose blockers are satisfied, continuing through the
whole requested outcome. Reuse existing modules and test seams. Use focused
behavioral regression tests for bugs and meaningful tests for new behavior;
follow the project's test-first requirements where applicable. Scale checks
to the change instead of generating tests for trivial reversible edits.

Compare the working experience with the spec throughout. For UI or runtime
changes, exercise the actual app and inspect the rendered result. Use the
visible in-app Browser when browser verification is needed. Use authorized
fixtures and recipients. Mocked tests do not prove live delivery, pairing or
production behavior. Capture useful proof without sensitive content.

Mark each ticket complete only when its acceptance checks are observed. Record
test commands, results and genuine limitations. Finish feasible independent
work even if a device approval, credential or external service blocks another
criterion. Never mark that blocked criterion as passed.

## 5. Review, fix and verify

Review the complete owned change, including uncommitted and untracked files,
against the pinned baseline and starting dirty snapshot. Do not limit review to
commits and accidentally omit the implementation. Use two distinct passes:

1. Standards: documented project conventions, correctness, callers and relevant
   data, permission or concurrency boundaries.
2. Spec: missing or wrong required behavior, accidental extra scope and whether
   the evidence proves each acceptance criterion.

Use independent read-only reviewers when available and permitted by the current
instructions; otherwise identify the review as self-review. Keep execution in
the current chat unless the user authorizes another chat. Reviewer briefs must
include the outcome, exact diff boundary, relevant standards/spec and checks.

Assess findings yourself, fix real defects and rerun affected checks. Re-review
changed behavior and unresolved findings. Limit review to three rounds unless
project instructions specify otherwise; an unresolved material finding at the
limit is a blocker, not approval. Required final checks must pass on the final
artifact. A self-review cannot substitute for required independent approval.

## 6. Record the retro and deliver

Record what slowed or misdirected this run, what worked, and the smallest
evidence-backed improvement for next time. Check existing tests/tooling before
suggesting a new guardrail. Record unresolved work and recurring causes.
Apply a narrow task-related correction when justified; leave unrelated global
rules, skill changes and broader infrastructure improvements as proposals.

Complete authorized release steps and verify their saved results. If release
permission or human action is still needed, present the concrete artifact and
the exact outstanding step. Report partial work as partial. Local verification,
deployment, provider acceptance and human acceptance are separate claims.

Finish with what Osiris can now do, how to try it, observed verification,
important decisions made for him, artifact/preview/PR links, and honest limits.
The run is complete only when the requested outcome is proved within its
authorization, with no required work silently deferred. When blocked, leave
state and resumption instructions so the next turn can continue immediately.

This skill runs while the agent's task is active. It does not create an
automation, daemon, recurring reminder or a guarantee of work after the chat
has ended. If the user asks to create/install the skill, create it without
starting a project run until he invokes it for a specific outcome.
