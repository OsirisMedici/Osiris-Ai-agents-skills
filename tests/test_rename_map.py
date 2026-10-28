"""Offline checks for operational mapping errors; no account access."""

import csv
import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/meta/meta-ads-manager/scripts/validate_rename_map.py'
spec = importlib.util.spec_from_file_location('rename_map', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def row(**changes):
    value = dict.fromkeys(module.FIELDS, '')
    value.update(entity_type='ad', entity_id='900003', parent_id='900002',
                 current_name='Ad 7 | Previous', proposed_name='Ad 7 - Tutorial to Project',
                 observed_hook='tutorial-to-project', proposed_hook='tutorial-to-project',
                 approval_ref='fixture: user approved the exact list')
    value.update(changes)
    return value


class RenameMapChecks(unittest.TestCase):
    def test_original_number_survives_nonsequential_order(self):
        rows = [row(), row(entity_id='900004', current_name='Ad 2 | Old', proposed_name='Ad 2 - Tutorial to Project')]
        self.assertEqual(module.validate(rows, {'ad': 2}, True)[0], [])

    def test_renumbering_is_rejected(self):
        self.assertTrue(module.validate([row(proposed_name='Ad 2 - Tutorial to Project')])[0])

    def test_missing_objects_are_rejected(self):
        self.assertTrue(module.validate([row()], {'ad': 20})[0])

    def test_duplicate_ids_are_rejected(self):
        self.assertTrue(module.validate([row(), row(current_name='Ad 8 | Old', proposed_name='Ad 8 - Tutorial to Project')])[0])

    def test_duplicate_labels_within_parent_are_rejected(self):
        self.assertTrue(module.validate([row(), row(entity_id='900004')])[0])

    def test_hook_conflict_requires_actual_exception_record(self):
        conflict = row(observed_hook='model-assumptions')
        self.assertTrue(module.validate([conflict])[0])
        conflict.update(exception_approved='yes', exception_note='User approved intended label; image remains unresolved')
        self.assertEqual(module.validate([conflict], require_approval=True)[0], [])
        conflict['approval_ref'] = ''
        self.assertTrue(module.validate([conflict])[0])

    def test_unknown_hook_is_not_silently_accepted(self):
        self.assertTrue(module.validate([row(observed_hook='')])[0])

    def test_missing_approval_reference_is_rejected_when_required(self):
        self.assertTrue(module.validate([row(approval_ref='')], require_approval=True)[0])

    def test_wrong_parent_level_is_rejected(self):
        parent = row(entity_id='900002', parent_id='900001', current_name='Ad 1 | Old', proposed_name='Ad 1 - Tutorial to Project')
        self.assertTrue(module.validate([parent, row()])[0])

    def test_complete_four_set_twenty_ad_map(self):
        rows = []
        for version in range(1, 5):
            parent = str(910000 + version)
            rows.append(row(entity_type='adset', entity_id=parent, parent_id='910000',
                            current_name=f'Old set {version}', proposed_name=f'Programme | V{version}',
                            observed_hook='', proposed_hook=''))
            for slot in range(1, 6):
                number = (version - 1) * 5 + slot
                rows.append(row(entity_id=str(920000 + number), parent_id=parent,
                                current_name=f'Ad {number} | Previous', proposed_name=f'Ad {number} - Concept {slot}'))
        self.assertEqual(module.validate(rows, {'adset': 4, 'ad': 20}, True)[0], [])

    def test_cli_reads_quoted_names_and_rejects_partial_map(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'map.csv'
            with path.open('w', newline='') as stream:
                writer = csv.DictWriter(stream, fieldnames=module.FIELDS)
                writer.writeheader()
                writer.writerow(row(current_name='Ad 7 | Red, portrait'))
            good = subprocess.run([sys.executable, str(SCRIPT), str(path), '--expect-ads', '1', '--require-approval'], capture_output=True, text=True)
            bad = subprocess.run([sys.executable, str(SCRIPT), str(path), '--expect-ads', '20'], capture_output=True, text=True)
            self.assertEqual(good.returncode, 0, good.stdout + good.stderr)
            self.assertEqual(bad.returncode, 1, bad.stdout + bad.stderr)


if __name__ == '__main__':
    unittest.main()
