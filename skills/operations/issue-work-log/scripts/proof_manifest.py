#!/usr/bin/env python3
"""Hash explicitly selected proof files and a reviewed progress delta. No network."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit


def canonical_issue(value):
    parsed = urlsplit(value)
    if (parsed.scheme != "https" or not parsed.hostname or parsed.username
            or parsed.password or parsed.query or parsed.fragment or parsed.port):
        raise ValueError("Use a canonical HTTPS issue URL without credentials/query/fragment/port")
    if not re.fullmatch(r"/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/issues/[1-9][0-9]*/?", parsed.path):
        raise ValueError("Issue URL must end in /OWNER/REPO/issues/NUMBER")
    return f"https://{parsed.hostname.lower()}{parsed.path.rstrip('/')}"


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def build_manifest(issue, facts_path, files):
    issue = canonical_issue(issue)
    # Normalize line endings/trailing whitespace, preserving meaningful text/order.
    facts = "\n".join(line.rstrip() for line in Path(facts_path).read_text(encoding="utf-8").splitlines()).strip()
    if not facts:
        raise ValueError("Reviewed delta text must not be empty")
    facts_hash = sha256(facts.encode("utf-8"))
    records = []
    seen_paths = set()
    for value in files:
        path = Path(value).resolve(strict=True)
        if not path.is_file():
            raise ValueError(f"Not a regular file: {path}")
        if str(path) in seen_paths:
            continue
        seen_paths.add(str(path))
        content = path.read_bytes()
        records.append({"path": str(path), "bytes": len(content), "sha256": sha256(content)})
    unique_hashes = sorted({record["sha256"] for record in records})
    identity = {"version": 1, "issue_url": issue, "facts_sha256": facts_hash, "file_hashes": unique_hashes}
    key = sha256(json.dumps(identity, sort_keys=True, separators=(",", ":")).encode("utf-8"))
    return {
        "schema_version": 1,
        "issue_url": issue,
        "facts_sha256": facts_hash,
        "log_key": key,
        "marker": f"<!-- issue-work-log:{key} -->",
        "files": records,
        "unique_file_count": len(unique_hashes),
        "duplicate_content_count": len(records) - len(unique_hashes),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__, epilog="Output contains local paths. Review privacy/provenance manually. This does not upload or verify remote URLs.")
    parser.add_argument("--issue", required=True, help="Canonical HTTPS issue URL")
    parser.add_argument("--facts", required=True, type=Path, help="UTF-8 file containing the reviewed progress delta")
    parser.add_argument("--file", action="append", default=[], help="Explicit proof file; repeat as needed")
    args = parser.parse_args()
    try:
        manifest = build_manifest(args.issue, args.facts, args.file)
    except (OSError, ValueError, UnicodeError) as error:
        print(f"Manifest not produced: {error}", file=sys.stderr)
        return 2
    print(json.dumps(manifest, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
