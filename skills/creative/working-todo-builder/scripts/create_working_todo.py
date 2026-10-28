#!/usr/bin/env python3
"""Generate a standalone Working TODO HTML page from a project plan JSON."""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TEMPLATE = ROOT / "assets" / "working-todo-template.html"
DEFAULT_STACK_TEMPLATE = ROOT / "assets" / "reference-stack-template.html"


def read_plan(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        plan = json.load(handle)
    validate_plan(plan)
    return plan


def validate_plan(plan: dict) -> None:
    phases = plan.get("phases")
    if not isinstance(phases, list) or not phases:
        raise ValueError("Plan must include a non-empty phases array.")

    seen_task_ids: set[str] = set()
    for phase_index, phase in enumerate(phases, start=1):
        phase.setdefault("order", phase_index)
        required_phase_fields = ["id", "name", "description", "checklist"]
        missing = [field for field in required_phase_fields if field not in phase]
        if missing:
            raise ValueError(f"Phase {phase_index} missing: {', '.join(missing)}")
        if not isinstance(phase["checklist"], list) or not phase["checklist"]:
            raise ValueError(f"Phase {phase.get('id', phase_index)} needs at least one task.")

        phase.setdefault("icon", "FileText")
        for task_index, task in enumerate(phase["checklist"], start=1):
            required_task_fields = ["id", "code", "label", "note"]
            missing = [field for field in required_task_fields if field not in task]
            if missing:
                raise ValueError(
                    f"Task {task_index} in phase {phase['id']} missing: {', '.join(missing)}"
                )
            if task["id"] in seen_task_ids:
                raise ValueError(f"Duplicate task id: {task['id']}")
            seen_task_ids.add(task["id"])
            if "brief" in task and not isinstance(task["brief"], list):
                raise ValueError(f"Task {task['id']} brief must be a list of paragraphs.")


def replace_token(template: str, token: str, value: str) -> str:
    return template.replace(token, value)


def render(template: str, plan: dict) -> str:
    default_phase_id = plan["phases"][0]["id"]
    replacements = {
        "__HTML_TITLE__": plan.get("html_title") or plan.get("project_title") or "Working TODO",
        "__WORKSPACE_NAME__": plan.get("workspace_name", "Project Build Room"),
        "__WORKSPACE_SUBTITLE__": plan.get("workspace_subtitle", "Osiris + Codex"),
        "__AVATAR__": plan.get("avatar", "OC"),
        "__PROJECT_TITLE__": plan.get("project_title", "Project Working Plan"),
        "__PROJECT_DESCRIPTION__": plan.get(
            "project_description",
            "Use this private build checklist to approve the best next tasks.",
        ),
        "__DEFAULT_PHASE_ID__": default_phase_id,
        "__PHASES_JSON__": json.dumps(plan["phases"], ensure_ascii=False, indent=10),
    }

    output = template
    for token, value in replacements.items():
        if token == "__PHASES_JSON__":
            output = replace_token(output, token, value)
        else:
            output = replace_token(output, token, html.escape(str(value), quote=True))
    return output


def default_sidebar(plan: dict) -> dict:
    return {
        "title": "Reference Stack",
        "subtitle": "Localhost sidebar",
        "mark": "APP",
        "note": "Keep this page open while building. Use the sidebar to compare the current app, references, and the active Working TODO plan.",
        "primary_label": "App",
        "primary_url": "./index.html",
        "apps": [
            {
                "name": plan.get("project_title", "Current App"),
                "label": "Current App",
                "description": "Live project app",
                "url": "./index.html",
            },
            {
                "name": "Working TODO",
                "label": "Working TODO",
                "description": "Build plan checklist",
                "url": "./working-todo.html",
            },
        ],
    }


def render_nav_buttons(apps: list[dict]) -> str:
    lines: list[str] = []
    for index, app in enumerate(apps):
        classes = ' class="is-active"' if index == 0 else ""
        lines.append(
            "          "
            f"<button{classes} type=\"button\" "
            f"data-name=\"{html.escape(str(app['name']), quote=True)}\" "
            f"data-url=\"{html.escape(str(app['url']), quote=True)}\">"
        )
        lines.append(f"            <strong>{html.escape(str(app['label']))}</strong>")
        lines.append(f"            <span>{html.escape(str(app.get('description', 'Local app')))}</span>")
        lines.append("          </button>")
    return "\n".join(lines)


def render_reference_stack(template: str, plan: dict) -> str:
    sidebar = {**default_sidebar(plan), **plan.get("sidebar", {})}
    apps = sidebar.get("apps") or default_sidebar(plan)["apps"]
    first_app = apps[0]
    primary_url = sidebar.get("primary_url") or first_app["url"]
    primary_label = sidebar.get("primary_label") or first_app.get("label") or "App"

    replacements = {
        "__STACK_TITLE__": sidebar.get("html_title", f"{sidebar['title']}"),
        "__BRAND_MARK__": sidebar.get("mark", "APP"),
        "__BRAND_TITLE__": sidebar.get("title", "Reference Stack"),
        "__BRAND_SUBTITLE__": sidebar.get("subtitle", "Localhost sidebar"),
        "__NAV_BUTTONS__": render_nav_buttons(apps),
        "__SIDEBAR_NOTE__": sidebar.get("note", ""),
        "__DEFAULT_NAME__": first_app["name"],
        "__DEFAULT_URL__": first_app["url"],
        "__PRIMARY_LABEL__": primary_label,
        "__PRIMARY_URL__": primary_url,
    }

    output = template
    for token, value in replacements.items():
        if token == "__NAV_BUTTONS__":
            output = replace_token(output, token, str(value))
        else:
            output = replace_token(output, token, html.escape(str(value), quote=True))
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", required=True, type=Path, help="Path to plan JSON.")
    parser.add_argument("--out", required=True, type=Path, help="Output HTML path.")
    parser.add_argument("--template", default=DEFAULT_TEMPLATE, type=Path, help="Template HTML path.")
    parser.add_argument("--stack-out", type=Path, help="Optional output reference-stack HTML path.")
    parser.add_argument(
        "--stack-template",
        default=DEFAULT_STACK_TEMPLATE,
        type=Path,
        help="Reference stack template HTML path.",
    )
    args = parser.parse_args()

    plan = read_plan(args.plan)
    template = args.template.read_text(encoding="utf-8")
    output = render(template, plan)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(output, encoding="utf-8")
    print(f"Wrote {args.out}")

    if args.stack_out:
        stack_template = args.stack_template.read_text(encoding="utf-8")
        stack_output = render_reference_stack(stack_template, plan)
        args.stack_out.parent.mkdir(parents=True, exist_ok=True)
        args.stack_out.write_text(stack_output, encoding="utf-8")
        print(f"Wrote {args.stack_out}")


if __name__ == "__main__":
    main()
