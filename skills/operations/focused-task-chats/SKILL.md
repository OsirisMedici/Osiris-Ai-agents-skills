---
name: focused-task-chats
description: Keep delegated work in separate focused task chats while the main chat stays conversational. Apply whenever an agent dispatches or coordinates work for Osiris.
---

# Focused task chats

Keep the main conversation responsive. Give each execution chat one coherent outcome and let it finish.

## Dispatch

- Follow the harness's authorization and routing rules. Use the existing owning chat for the same outcome; create a distinct chat for a different task when creation is authorized. Osiris wants new task chats in the saved ScaleHQ project unless he explicitly names another project. Use the saved local environment unless he requests a worktree or other environment.
- Send one focused, self-contained task brief: outcome, target, necessary facts or source links, authorized actions, important constraints and expected result. Include the relevant user decisions needed to do that task correctly. Leave unrelated conversation, personal reflection, other tasks and full transcripts in the main chat.
- Prefer pointers to the actual issue, task or source over copying its entire history. Avoid conversational shorthand that the executor cannot resolve. Concise does not mean omitting a necessary fact.
- After dispatch, say what was sent and identify the task chat by its human-readable title.

## Let it run

Let the executor work to completion. Monitor with the harness's bounded wait/status tools. Keep routine unchanged snapshots out of the conversation.

Send a follow-up only for a material user correction, an actual blocker, a required decision or a change to the same task's scope. New unrelated work gets its own task chat. Avoid repeatedly forwarding the conversation, restating the brief or interrupting a running task merely to request progress.

Use the main chat for the user's thinking, questions and decisions. Share verified findings and meaningful blockers naturally. A dispatch is not completion; collect and assess the actual result. Promote requested links, drafts and other useful outputs into the main chat so Osiris can inspect them.

For an explicitly invoked Veronica session, follow `../veronica/SKILL.md`: one operator for the coherent live browser workflow, one action at a time. This convention does not create automations, authorize external changes or require delegation for a conversation that should remain interactive. Respect explicit requests to keep work in the current chat, subject to actual harness capabilities and routing requirements. Explain any necessary exception briefly.
