# Issue content

Adapt this structure to repository conventions. Replace braces with actual content or an explicit unresolved fact. Merge into existing issues; preserve their history and other authors' content.

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
