#!/usr/bin/env python3
"""Check an offline rename map. Never access Meta or perform a mutation."""

import argparse
import csv
import re
from collections import Counter
from pathlib import Path


FIELDS = (
    'entity_type', 'entity_id', 'parent_id', 'current_name', 'proposed_name',
    'observed_hook', 'proposed_hook', 'approval_ref', 'exception_approved',
    'exception_note',
)
AD_NUMBER = re.compile(r'\bad[\s_-]*(\d+)\b', re.IGNORECASE)


def validate(rows, expected=None, require_approval=False):
    errors, ids, names = [], {}, set()
    counts = Counter()
    for line, row in enumerate(rows, 2):
        kind, identifier, parent = (row.get(k, '').strip() for k in FIELDS[:3])
        prefix = f'Row {line}'
        counts[kind] += 1
        if kind not in {'campaign', 'adset', 'ad'}:
            errors.append(f'{prefix}: invalid entity_type {kind!r}')
        if not identifier.isdigit():
            errors.append(f'{prefix}: entity_id must be an actual numeric Meta ID')
        if identifier in ids:
            errors.append(f'{prefix}: duplicate entity_id {identifier}')
        ids[identifier] = kind
        if kind in {'adset', 'ad'} and not parent.isdigit():
            errors.append(f'{prefix}: parent_id must be an actual numeric Meta ID')
        if identifier == parent:
            errors.append(f'{prefix}: an entity cannot be its own parent')
        old, new = row.get('current_name', ''), row.get('proposed_name', '')
        if not old.strip() or not new.strip():
            errors.append(f'{prefix}: current_name and proposed_name are required')
        if new != new.strip():
            errors.append(f'{prefix}: proposed_name has leading or trailing whitespace')
        name_key = (kind, parent, new.casefold())
        if name_key in names:
            errors.append(f'{prefix}: duplicate proposed name within the same parent')
        names.add(name_key)
        if kind == 'ad':
            before, after = AD_NUMBER.search(old), AD_NUMBER.search(new)
            if before and (not after or before.group(1) != after.group(1)):
                errors.append(f'{prefix}: original ad number was removed or changed')
        approval = row.get('approval_ref', '').strip()
        if require_approval and not approval:
            errors.append(f'{prefix}: approval_ref is required for this check')
        observed = row.get('observed_hook', '').strip().casefold()
        proposed = row.get('proposed_hook', '').strip().casefold()
        if bool(observed) != bool(proposed):
            errors.append(f'{prefix}: supply both hook fields or leave both empty')
        elif observed != proposed:
            exception = row.get('exception_approved', '').strip().casefold() == 'yes'
            note = row.get('exception_note', '').strip()
            if not (exception and note and approval):
                errors.append(f'{prefix}: hook mismatch needs an explicit approved exception, note, and approval_ref')
    if not rows:
        errors.append('The map contains no entities')
    for kind, count in (expected or {}).items():
        if count < 0 or counts[kind] != count:
            errors.append(f'Expected {count} {kind} entities; found {counts[kind]}')
    for line, row in enumerate(rows, 2):
        kind, parent = row.get('entity_type', '').strip(), row.get('parent_id', '').strip()
        wanted = {'adset': 'campaign', 'ad': 'adset'}.get(kind)
        if wanted and parent in ids and ids[parent] != wanted:
            errors.append(f'Row {line}: parent in this map must be a {wanted}')
    return errors, counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('map', type=Path)
    parser.add_argument('--expect-campaigns', type=int)
    parser.add_argument('--expect-adsets', type=int)
    parser.add_argument('--expect-ads', type=int)
    parser.add_argument('--require-approval', action='store_true')
    args = parser.parse_args()
    try:
        with args.map.open(newline='', encoding='utf-8-sig') as stream:
            reader = csv.DictReader(stream)
            missing = set(FIELDS) - set(reader.fieldnames or [])
            if missing:
                parser.error('Missing columns: ' + ', '.join(sorted(missing)))
            rows = []
            for row in reader:
                if None in row or any(v is None for v in row.values()):
                    parser.error('Malformed CSV row; quote names containing commas')
                if any(v.strip() for v in row.values()):
                    rows.append(row)
    except (OSError, UnicodeError, csv.Error) as exc:
        parser.error(str(exc))
    expected = {kind: count for kind, count in (
        ('campaign', args.expect_campaigns), ('adset', args.expect_adsets),
        ('ad', args.expect_ads),
    ) if count is not None}
    errors, counts = validate(rows, expected, args.require_approval)
    if errors:
        print('\n'.join('ERROR: ' + error for error in errors))
        return 1
    print('Map valid: ' + ', '.join(f'{counts[kind]} {kind}' for kind in ('campaign', 'adset', 'ad')))
    print('Offline integrity only; verify live context, actual approval, and saved Meta state separately.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
