---
name: power-list
description: Use when Osiris says /power-list or asks for today's task list. Builds a focused deep work session list (2-3 hours) ordered by momentum logic — quick wins first, then big rocks. Overwrites the Power List section at the top of veronica-memory/Top-Priorities.md every time.
---

# Power List — Daily Deep Work Session

## Public setup

Resolve the user's authorized workspace before following file paths below.
`<workspace>` and named vault folders describe an existing layout, not bundled
data. Reuse equivalent files in the user's setup. Ask for a destination only
when discovery cannot resolve it. Private records and reference documents must
be supplied or located locally; do not invent their contents. Reuse answers
already in the request rather than repeating the intake. Use available supported
tools and the visible in-app Browser for browser work. Installing this skill
does not invoke it or authorize messages, publishing or unrelated service writes.

## What It Does

Builds a focused 2–3 hour deep work block for Osiris — solo tasks only, ordered for maximum momentum. Saves to the top of `veronica-memory/Top-Priorities.md`.

The Power List is Osiris's and Osiris's only. No team tasks. No waiting-on tasks. No tasks that need another person present.

## Task Sources (read all of these)

1. `veronica-memory/Top-Priorities.md` — the full priority list (all sections below the Power List)
2. `Daily Notes/[today's date].md` — if it exists, check for loose tasks or notes

Do NOT load all client files. Only check the ones that are live/active right now.

## Eligibility Rules — What NEVER Goes in the Power List

Before picking tasks, filter out everything that falls into these categories:

- **Team Sync tasks** — require another person on a call. Skip entirely.
- **Waiting On tasks** — ball is in someone else's court. Skip entirely.
- **Delegate tasks** — already handed off. Skip entirely.
- **Tasks owned by another person** — follow the actual ownership recorded in the workspace.
- **Reactive/conditional tasks** — e.g. "WhatsApp number received → activate." These happen when triggered, not as planned deep work. Skip entirely.
- **Fabricated tasks** — only include tasks explicitly written in Top-Priorities.md. Never reframe or invent. Take tasks as written.

## Task Order — Momentum Logic

**Tier 1 — Quick Wins:** Important + can be closed in under 30 minutes. Send a message, review a doc, make a decision. These go FIRST — they build momentum before the heavy work.

**Tier 2 — Big Rocks:** Important + require 1–2 hours of real focus. Campaign builds, reports, strategy docs, system builds. These go after the quick wins while energy is high.

If there aren't enough tasks to fill 2–3 hours, include as many as exist. Do NOT fabricate tasks to hit a number.

## Time Estimates

Add a time estimate to every task. Format: `*(~Xm)*` or `*(~Xhr)*`

Examples:
- `- [ ] \`[Client D]\` Write hiring ad copy *(~45m)*`
- `- [ ] \`[Client B]\` Ads report *(~1hr)*`

**Total session time** should be 2–3 hours. If the available tasks add up to less, that's fine — show what's real. Never pad.

Add a total at the bottom of the Power List:
`*Session: ~X hrs total*`

## Output Format

Overwrite the Power List + Delegate sections at the **top** of `veronica-memory/Top-Priorities.md`. Keep everything below the Delegate section untouched.

```markdown
# Top Priorities
*Call /power-list to refresh anytime.*

*Week Progress*

*`X / Y done`*

*Z%*

*~N tasks/day*

*D days left*

---

## Power List — [Month Day, Year] · `0 / N done`

- [ ] `Client` Task name *(~Xm)*
- [ ] `Client` Task name *(~Xhr)*
- [ ] `Client` Task name *(~Xm)*

*Session: ~X hrs total*

---

## Delegate

> Hand these off today. Assign → set deadline → check back.

*(ask Osiris)*
```

**Delegation:** Leave Delegate section as `*(ask Osiris)*` when writing the file. After reading the list back, ask: "Which of these do you want to delegate?" — wait for his answer, then add only what he picks with the right team member.

## Week Progress — Recalculate on Every Run

Before writing the file, recalculate the week progress line and update it.

Count checkboxes in all client sections under the `## Week [N]` header in Top-Priorities.md.
Exclude: Power List and work owned by others.
Note: Delegate, Team Sync, and Waiting On tasks now live in Off-My-Plate.md — they will not appear in Top-Priorities.md and do not need to be filtered.

- `done` = count of `[x]` in those sections
- `total` = count of all `[ ]` + `[x]` in those sections
- `remaining` = total - done
- `pct` = round(done / total * 100)
- `days_left` = days remaining until Sunday (end of week), including today
- `daily_target` = ceil(remaining / days_left)

Update these lines at the top of the file. Use two trailing spaces after each line (hard line break) so they render as separate lines with no gap between them:
```
*Week Progress*<br>
*`X / Y done`*<br>
*Z%*<br>
*~N tasks/day*<br>
*D days left*
```

## After Writing the File

Read the list back directly in chat — don't make him open the file. One clean read-through, no commentary.

Then one sentence max: the single most important task and why. That's it.

If there are no weekly tasks, report zero total and use zero percent; avoid division by zero. A local delegation entry records a handoff decision and does not prove the underlying task was completed or authorize messaging the assignee.
