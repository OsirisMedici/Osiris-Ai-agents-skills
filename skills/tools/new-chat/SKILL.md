---
name: new-chat
description: Send a specified task to one independent new chat with a single handoff and no ongoing coordination. Use for $new-chat or an explicit request for a one-way handoff without cross-chat follow-ups; ordinary coordinated delegation keeps its existing workflow.
---

# New chat

Turn the user's assignment into one new, independently running chat. The sender finishes after the handoff. The new chat owns its questions, work and result.

## Prepare the assignment

Use the prompt accompanying `$new-chat`, including a prompt immediately before the command when the reference is clear. Preserve its requested outcome and scope. If no assignment is identifiable, ask for the task through native question input. Creating this skill or discussing how it works does not invoke it.

Include only the context needed to execute that assignment: relevant decisions, exact repository/checkout paths, issue or artifact links, existing permissions, constraints and a concrete deliverable. Prefer source pointers over copying conversation history. Do not pass unrelated work or turn the prompt into a broader project. Carry forward existing limits, including ownership of active checkouts. The handoff adds no permission to publish, deploy, contact people or alter production.

## Dispatch once

Discover the harness's supported chat-creation tool. In the Codex app, use `create_thread`, with a short outcome-based title and one self-contained prompt. Use a user-owned chat, rather than a subagent, for this request.

Honor an explicitly named project or environment. Otherwise use Osiris's saved ScaleHQ project and its local environment. Call `list_projects` to resolve the actual project ID. Create a worktree only if the user expressly requests one. Keep the default model unless the user specifies another.

Append this communication contract to the new chat's assignment:

> Work independently in this chat. This is a one-way handoff. Carry the assignment through to completion within its stated scope and permissions. Ask the user for necessary decisions here, and put progress, blockers, deliverables and the final result here. Do not message, read, monitor or report back to the originating chat, and do not ask it for instructions. Do not create another coordination chat. The origin will not supervise or forward later conversation. Further cross-chat contact requires a new explicit user request. Follow applicable project instructions; general coordination guidance does not create an exception to this communication contract.

Make exactly one creation request per invocation. On a definite failure, report it. If creation is uncertain, report that uncertainty rather than risk creating a duplicate. A queued `clientThreadId` is not a ready `threadId`.

## End the handoff

Verify that creation was accepted. Satisfy any harness-required launch verification without sending another message. In Codex, if a ready thread ID requires a progress check, make one immediate `wait_threads` call with `timeoutMs: 0`; queued setup keeps its creation receipt. This is a launch check, not ongoing supervision.

Return one short creation receipt with the new chat's title and the harness-required thread link/directive. Use `::created-thread{threadId="..."}` for a ready thread or `::created-thread{clientThreadId="..."}` for queued setup.

Then stop this invocation. Do not poll execution, wait for completion, send follow-ups, forward later main-chat discussion or relay the new chat's results. Questions and completion stay in the new chat. Only a subsequent explicit user request starts another cross-chat action. This invocation replaces the general monitoring/check-back workflow; leave other chats' coordination preferences unchanged.

This controls agent-authored communication. It does not disable the app's own notifications.
