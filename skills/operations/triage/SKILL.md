---
name: triage
description: Morning task processing — reads every incomplete task in Top-Priorities.md and asks Osiris to Keep, Delegate, Reschedule (next week), or Delete. Moves tasks between Top-Priorities.md and Off-My-Plate.md automatically. Use /triage to process active tasks. Use /triage plate to pull something back from Off-My-Plate.md.
---

# Triage

## Public setup

Resolve the user's authorized workspace before following file paths below.
`<workspace>` and named vault folders describe an existing layout, not bundled
data. Reuse equivalent files in the user's setup. Ask for a destination only
when discovery cannot resolve it. Private records and reference documents must
be supplied or located locally; do not invent their contents. Reuse answers
already in the request rather than repeating the intake. Use available supported
tools and the visible in-app Browser for browser work. Installing this skill
does not invoke it or authorize messages, publishing or unrelated service writes.

Two modes: process your active list, or pull something back.

---

## Mode 1 — /triage (default)

Process incomplete tasks in Top-Priorities.md. Takes 3-5 minutes. Clears the dead weight.

### Steps

**1. Read both files**

Read `veronica-memory/Top-Priorities.md` and `veronica-memory/Off-My-Plate.md`.

**2. Pull incomplete tasks**

Collect every `- [ ]` task from the client sections under `## Week [N]` in Top-Priorities.md.
Exclude: Power List tasks and work owned by others.

**3. Present each task**

Show them one at a time in this format:

```
**[Client]** Task name

[k] Keep   [d] Delegate   [r] Next week   [del] Delete
```

Wait for his input before showing the next task. Accept single letters: k / d / r / del.

**4. Handle each decision**

**[k] Keep** — no change.

**[d] Delegate**
- Ask: "Who? And follow-up date?" (one line)
- Mark the task **[x]** in Top-Priorities.md client section (delegating = handling it — it counts toward week progress). Append `→ delegated **Name**` to the task text.
- Add to Off-My-Plate.md Delegate section for tracking:
  `- [ ] \`Client\` Task name → **Name** *(follow up [date])*`

**[r] Next week**
- Remove the task from Top-Priorities.md
- Add to Off-My-Plate.md Next Week section:
  `- [ ] \`Client\` Task name`

**[del] Delete**
- Remove from Top-Priorities.md. Gone.

**5. After all tasks processed**

Show a one-line summary: "Kept X · Delegated Y · Rescheduled Z · Deleted W"

Then trigger /power-list to rebuild the Power List from what remains.

---

## Mode 2 — /triage plate

Pull something back from Off-My-Plate.md into Top-Priorities.md.
Use this when circumstances change — [Colleague] can't do it anymore, [Contact] sent the number, etc.

### Steps

**1. Read Off-My-Plate.md**

Show all incomplete `[ ]` tasks grouped by section (Delegate, Team Sync, Waiting On, Next Week).

**2. Ask**

"Which one do you want to pull back?"

Wait for his selection.

**3. Move it**

- Remove from Off-My-Plate.md
- Add to the correct client section in Top-Priorities.md

**4. Confirm**

One line: "Pulled back. It's in your [Client] section."

---

## Notes

- Never move completed `[x]` tasks — those stay where they are.
- Never touch the Power List section — only the client sections under `## Week [N]`.
- If Osiris says "do them all" without specifying — ask once: "All keep, or do you want to go through them?" Don't assume.
- If he's in a rush: accept "delegate all of these" or "reschedule all of these" as bulk actions for a named set.

If there are no weekly tasks, report zero total and use zero percent; avoid division by zero. A local delegation entry records a handoff decision and does not prove the underlying task was completed or authorize messaging the assignee.
