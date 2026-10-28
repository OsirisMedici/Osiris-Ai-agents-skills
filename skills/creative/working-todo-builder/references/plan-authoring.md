# Plan Authoring

Use this JSON shape:

```json
{
  "html_title": "Working TODO",
  "workspace_name": "Project Build Room",
  "workspace_subtitle": "Osiris + Codex",
  "avatar": "OC",
  "project_title": "Project Working Plan",
  "project_description": "Short sentence describing what this board is for.",
  "sidebar": {
    "title": "Reference Stack",
    "subtitle": "Localhost sidebar",
    "mark": "APP",
    "primary_label": "App",
    "primary_url": "./index.html",
    "note": "Keep this page open while building.",
    "apps": [
      {
        "name": "Current App",
        "label": "Current App",
        "description": "Live project app",
        "url": "./index.html"
      },
      {
        "name": "Working TODO",
        "label": "Working TODO",
        "description": "Build plan checklist",
        "url": "./working-todo.html"
      }
    ]
  },
  "phases": [
    {
      "id": "ui",
      "order": 1,
      "icon": "Layout",
      "name": "UI And Usability Polish",
      "description": "Make the working surface clear and decision-ready.",
      "checklist": [
        {
          "id": "A01",
          "code": "A01",
          "label": "Paper checklist clarity",
          "note": "Clean paper sheet, no blurry text, completed rows still readable.",
          "brief": [
            "Explain why this task matters and what decision it supports.",
            "Explain what makes this task worth approving now versus disapproving or parking."
          ]
        }
      ]
    }
  ]
}
```

Supported icons: `Layout`, `Calendar`, `Layers`, `FileText`, `Users`, `BookOpen`, `MessageSquare`, `Clipboard`, `HardDrive`, `Sparkles`, `CheckCircle`, `Flag`.

Sidebar rules:

- Always include the current app and Working TODO.
- Add reference apps, local inspiration pages, original source apps, docs pages, or comparison pages as extra `sidebar.apps`.
- Use relative URLs when the generated files sit beside the target app. Use localhost URLs when comparing multiple running servers.

Planning rules:

- Make tasks decision-sized. A task should be something the user can approve, disapprove, or ask to discuss.
- Use `note` for the short row summary.
- Use `brief` for one or two paragraphs that help planning. Avoid vague explanation.
- Put the best first picks in early phases. Later phases can hold parked integrations.
- Keep task IDs stable because approval/disapproval state is saved in browser localStorage.
