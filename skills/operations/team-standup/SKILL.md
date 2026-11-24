---
name: team-standup
description: "Read a selected Slack standup channel and summarize each team member's latest update."
---

# Team standup digest

Resolve the intended Slack workspace and standup channel through the connected
tools. Use the user's selected roster or a known project roster when checking
for missing updates. This package contains no staff list or channel ID.

Read enough messages to cover the requested period, normally the last 24 to 48
hours. Follow pagination so a message limit cannot silently shorten the period.
Recognize the team's actual update format, including EOD, Done, Blockers and
Tomorrow fields. Group by author and use the latest relevant update per person.
Preserve material corrections and distinguish the posted date from the work date.

For each person, show completed work, any blocker and the next planned work.
List a missing update only when the expected roster and period are known. If
access or coverage is incomplete, state that gap. If no updates are found, say
so without diagnosing a broken automation from absence alone.

Return a concise digest with source links when available. Reading the channel
does not authorize posting reminders, sending messages or changing tasks.
