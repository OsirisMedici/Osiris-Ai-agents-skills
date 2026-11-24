#!/usr/bin/env python3
"""Build the README skill table and fail when a package lacks a description."""
import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- skill-catalog:begin -->'
END = '<!-- skill-catalog:end -->'
LABELS = {
    'creative': 'Creative and product design',
    'engineering': 'Engineering',
    'knowledge': 'Knowledge and research',
    'legacy': 'Legacy creative workflows',
    'marketing': 'Marketing and sales planning',
    'meta': 'Meta advertising',
    'operations': 'Operations and planning',
    'tools': 'Tools and chat workflows',
    'writing': 'Writing',
    'youtube': 'YouTube',
}


def render():
    descriptions = json.loads((ROOT / 'docs/skill-catalog.json').read_text())
    packages = {}
    for entry in sorted((ROOT / 'skills').glob('*/*/SKILL.md')):
        name = entry.parent.name
        if name in packages:
            raise ValueError(f'Duplicate package name: {name}')
        if not re.search(r'^name: ' + re.escape(name) + r'\s*$', entry.read_text(), re.M):
            raise ValueError(f'Frontmatter name differs from folder: {entry}')
        packages[name] = entry
    if set(packages) != set(descriptions):
        raise ValueError(f'Catalog mismatch. Missing descriptions: {sorted(set(packages)-set(descriptions))}; stale descriptions: {sorted(set(descriptions)-set(packages))}')
    categories = sorted({entry.parent.parent.name for entry in packages.values()})
    lines = [START, f'{len(packages)} skills across {len(categories)} categories. Click **Open skill** to read its instructions and requirements.', '']
    for category in categories:
        lines += ['### ' + LABELS.get(category, category.replace('-', ' ').capitalize()), '']
        if category == 'legacy':
            lines += ['These three older workflows are retained for reference. Use [creative](skills/creative/creative/SKILL.md) for the current HTML creative workflow.', '']
        lines += ['| Skill | What it does | |', '| --- | --- | --- |']
        for name, entry in sorted(packages.items()):
            if entry.parent.parent.name != category:
                continue
            description = descriptions[name]
            if not isinstance(description, str) or not description.endswith('.') or any(c in description for c in '\n|'):
                raise ValueError(f'Expected a one-line sentence for {name}')
            link = entry.relative_to(ROOT).as_posix()
            lines.append(f'| `{name}` | {description} | [Open skill]({link}) |')
        lines.append('')
    lines.append(END)
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    options = parser.parse_args()
    path = ROOT / 'README.md'
    content = path.read_text()
    if content.count(START) != 1 or content.count(END) != 1:
        raise ValueError('README must contain exactly one catalog marker pair')
    start, end = content.index(START), content.index(END) + len(END)
    expected = content[:start] + render() + content[end:]
    if options.check:
        if expected != content:
            raise SystemExit('README catalog is stale. Run python3 scripts/build_catalog.py')
        print('README catalog matches every skill package and description.')
    else:
        path.write_text(expected)
        print('Updated README catalog.')


if __name__ == '__main__':
    main()
