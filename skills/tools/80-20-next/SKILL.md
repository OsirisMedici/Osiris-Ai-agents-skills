---
name: 80-20-next
description: Review the current chat and turn its latest results into three ranked 80/20 next steps with prompts ready to paste. Use when the user asks what to send next to make the most progress or regain focus in a long chat.
---

# 80/20 next steps

Read the current chat and recommend the smallest actions that can materially advance the user's goal. This is a read-only review. The user chooses which prompt to send.

1. Recover the active goal from the user's latest relevant messages. Carry forward settled decisions, scope limits, and the evidence that would count as done.
2. Parse the three most recent substantive outputs relevant to that goal, or all available if fewer than three. An output is a deliverable, verification result, decision, or blocker that changes what should happen next. Use the strongest available evidence for each. Distinguish completed and verified work from claims, proposals, and attempts. Skip routine updates and repeated conclusions. Look further back only to recover a constraint or evidence that changes the ranking. If history is missing, state the specific gap that affects the advice.
3. Rank the next actions by impact on the goal, effort, and what each action unlocks. Favor the smallest action that closes the biggest gap or settles a decision that could prevent rework. Put prerequisites before dependent work. When progress depends on the user, turn the prerequisite into one concrete decision or action. Flag alternatives and dependent steps so the user knows which prompts to paste and in what order.

Give one sentence on where the work stands, then three ranked recommendations. For each, give the action, why it matters now, and one ready-to-paste prompt in its own plain-text code block. The prompt should name the target, carry forward the constraints that matter, and give a checkable result. Use exact names or artifact references from the chat when they help. Leave out secrets. Keep the response short enough to scan without rereading the chat.

Put the best next prompt first. If the evidence supports fewer than three useful actions, give those and state what would make another step worthwhile.
