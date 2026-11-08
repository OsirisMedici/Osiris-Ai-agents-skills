# Issue content

Adapt this structure to repository conventions. Replace braces with actual content or an explicit unresolved fact. Merge into existing issues; preserve their history and other authors' content.

## Bug reports

Adapt the [T3 Code bug report form](https://github.com/pingdotgg/t3code/blob/ade473018d32003658b7d38693e083ee2e314bd8/.github/ISSUE_TEMPLATE/bug_report.yml). Name the symptom and affected area in the title. Lead with the reproduction. Keep the Feedback identity marker when applicable and put its human-readable source link after the bug evidence.

```markdown
<!-- feedback-task:{task UUID} -->

## Steps to reproduce

1. {Open the affected area with the minimum relevant data and settings.}
2. {Take the action and identify the exact point where the failure appears.}

## Expected behavior

{What the person should see or be able to do.}

## Actual behavior

{What the person sees instead, including repeatability or frequency if known. Distinguish firsthand observations from reported behavior.}

## Impact and environment

{What this interrupts, the tested environment, and the affected version or commit if verified. State when the deployed version is unknown. Include a verified workaround if available.}

## Visual evidence

{Embed reviewed evidence images with captions near the claims they support.}

## Source and investigation

{Source link and applicable Feedback metadata from the general template. Record measured evidence, relevant code and tests, known scope, and separately labelled hypotheses.}

## Implementation and verification

- [ ] Reproduce the failure with a stable fixture and assert the user-visible result. Record the baseline failure before changing code.
- [ ] Trace the relevant path and test the suspected cause. State what needs to be confirmed before selecting a fix.
- [ ] Make the smallest scoped fix. Identify adjacent behavior and data that must be preserved.
- [ ] Show the regression passes and check relevant controls and edge cases. Record the candidate revision, commands, observed results, and before/after images for visual changes in the PR.
```

## Visual evidence for every issue

Include at least one real, relevant image in a visible section of the issue. Collect supplied images and any existing proof from the source task or issue. If proof is missing, capture the observed behavior, current state, or relevant test output from an authorized environment. For a UI bug, show the failing state and a distinct control or comparison when it helps explain the failure. Label mockups as design references. Capture fixed-state evidence only after the fix is available.

Keep every useful distinct image. Deduplicate only established repeats and keep uncertain pairs. Inspect each image for relevance and sensitive content before upload. Use a clean capture or a verified redacted copy when necessary. Keep images within the issue's authorized audience.

Use a supported GitHub attachment operation, or follow the [issue upload and recovery procedure](../../issue-work-log/references/attachments.md) for in-app Browser uploads. Embed permanent attachment URLs with descriptive alt text and a caption that says what each image shows. Reopen the saved issue and check that the images render. If no safe image can be captured, uploaded, or verified, report the exact gap and retain a ready draft or recoverable files. Treat the evidence step as incomplete and never manufacture proof.

## General implementation issues

```markdown
<!-- feedback-task:{task UUID} -->

## Source

[Feedback task]({canonical task URL})
Task UUID: {UUID}. Board/client: {board and client}.
Code/title at intake: {current title}. Read: {timestamp and source version}.
{Relevant owner, status, dates, dependencies, and context links.}

## Requirements and acceptance criteria

{Faithful source requirements and criteria, with source references.}
{Unavailable attachments or unresolved source details, explicitly labelled.}

## Outcome and users

{What we are building, who uses it, why it matters, and what becomes easier.}

## Finished experience and success

{Concrete user journey and observable acceptance conditions.}

## Scope and decisions

{Included/excluded work, confirmed decisions, dependencies, open questions.}
{Separate confirmed decisions, assumptions, and proposals.}

## Product and repository evidence

{Current behavior/data model; precise files, commits, or inspected app views.}
{Evidence limits and anything still unverified.}

## Visual evidence

{Embed reviewed evidence images with captions near the claims they support.}

## Implementation plan

{Technical approach, sequence, reasoning, and tradeoffs.}

## Testing and handoff

{Meaningful checks, required evidence, review/acceptance steps, and next owner.}

## Ordered checklist

- [ ] 1. {Resolve prerequisite decision and name its completion condition.}
- [ ] 2. {Implement a concrete slice and name its completion condition.}
- [ ] 3. {Verify behavior and name the expected result.}
- [ ] 4. {Complete handoff and name the acceptance evidence.}

Intake and planning are saved. Implementation requires a separate request.
```

Use as many checklist items as needed. Retain original source step numbers in quoted history. Use stable Feedback links for dependencies. Keep sensitive source content within its authorized audience; if repository visibility would expose it, prepare a safe draft and resolve the destination before publishing.
