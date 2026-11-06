---
name: chat-rescue
description: Give the user a read-only decision brief when work in the current AI chat is stuck or they need to decide what to tell the agent next.
---

Use the current conversation to help the user decide what to tell the agent next. Treat this invocation as read-only. Inspect only relevant, authorized evidence and return the report in chat. Leave execution of the proposed plan for a separate request.

1. Recover the latest objective, success criteria, and scope from the user's messages. Preserve corrections and settled decisions. If the visible chat is incomplete, say which gap matters.
2. Check the evidence behind claims that affect the next decision. Start with visible tool results, logs, diffs, and artifacts. Use a targeted read-only lookup when it can resolve a material gap. Match each check to what it actually covered, including the version or environment when relevant. Treat an agent's claim without direct evidence as reported and unverified. If evidence conflicts, show the discrepancy and explain what would settle it.
3. Return the following sections. Aim for 250 to 400 words, including the reply prompt. Give each fact one home and use source pointers the user can follow.

- **Goal.** State the problem, the desired outcome, and any constraint that shapes the decision.
- **Done and verified.** Name what was done and what the evidence confirms. Label reported work separately when it matters. Distinguish an attempted action from a successful outcome.
- **Remaining.** Name unfinished work, actual blockers and their prerequisites, and any uncertainty that affects the plan. Say which evidence would resolve it and whether other work can proceed.
- **Proposed next steps.** Number the actions in priority and dependency order. Name the first actionable step and its check for success. Mark any step that needs a decision or authorization as conditional.
- **Decisions.** Separate settled decisions from choices still open. For consequential open choices, give the options, the tradeoff, and your recommendation if the evidence supports one. Attribute suggestions and approvals to the right person.
- **What to tell the agent.** Give up to three questions or corrections that would change the next action. Direct questions to the agent when it can find the answer. Flag choices only the user can make.
- **Reply to paste.** End the report with one short, ready-to-send prompt for the current agent. Carry forward the agreed scope and ask for the highest-priority safe action or the evidence needed to make it possible. Keep blocked actions conditional and preserve existing approval gates.
