---
name: working-todo-builder
description: Build or customize a portable Studio Flow style Working TODO planning page for any project. Use when Codex needs to create a project-specific planning checklist, approval/disapproval board, decision-brief accordion, or local-only HTML build-room tracker with the same UI, animations, copy queue, and task workflow as the AND OS Working TODO.
---

# Working TODO Builder

Create a local-first `working-todo.html` page and optional `reference-stack.html` sidebar shell for a project using the bundled templates and generator. Keep the UI, animation, approval queue, disapprove flow, decision brief accordion, clipboard fallback, sticky phase rail, localhost sidebar, and paper-like Studio Flow visual language intact.

## Workflow

1. Read the project context, repo docs, user notes, or transcript.
2. Turn the work into phases with decision-grade tasks, not a huge feature dump.
3. Create a plan JSON matching `references/plan-authoring.md`.
4. Run `scripts/create_working_todo.py --plan <plan.json> --out <working-todo.html> --stack-out <reference-stack.html>`.
5. Open the output locally and verify that one brief opens at a time, approval/disapproval works, copied approved tasks include the decision brief, and the sidebar switches between working apps.

## Resources

- `assets/working-todo-template.html`: standalone exact UI/functionality template derived from AND OS Working TODO.
- `assets/reference-stack-template.html`: standalone localhost sidebar shell for working apps and references.
- `assets/example-plan.json`: example project plan input.
- `assets/example-working-todo.html`: generated example output.
- `assets/example-reference-stack.html`: generated example sidebar output.
- `references/plan-authoring.md`: phase/task schema and planning guidance.
- `scripts/create_working_todo.py`: deterministic generator.

## Guardrails

- Preserve the template behavior unless the user explicitly asks to redesign it.
- Keep task labels short and task briefs useful. The brief should explain why a task matters, what decision it supports, and when to approve or disapprove it.
- Prefer 4-8 phases and 3-8 tasks per phase for new project plans unless the user asks for a larger operating plan.
- Use local files only. Do not add cloud databases, login, or SaaS assumptions unless the project explicitly requires them.
