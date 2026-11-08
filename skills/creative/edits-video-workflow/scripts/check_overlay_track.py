#!/usr/bin/env python3
"""Check exact, contiguous frame coverage on one Edits overlay lane."""
import argparse
import json
from fractions import Fraction
from pathlib import Path


def check(snapshot, track, fps, end_frame):
    items = snapshot.get("elements") if isinstance(snapshot, dict) else snapshot
    if not isinstance(items, list):
        raise ValueError("Expected an elements array or an object containing elements")
    if fps <= 0 or end_frame <= 0:
        raise ValueError("Frame rate and end frame must be positive")

    def frame(value):
        exact = Fraction(str(value)) * fps
        snapped = round(exact)
        if abs(exact - snapped) > Fraction(1, 1000):
            raise ValueError(f"Off-frame edge at {value}s")
        return snapped

    spans = sorted(
        (frame(item["startTime"]), frame(item["endTime"]))
        for item in items if item.get("trackId") == track
    )
    if not spans:
        raise ValueError("No elements on the requested track")
    cursor = 0
    for start, end in spans:
        if start != cursor:
            label = "Gap" if start > cursor else "Overlap"
            raise ValueError(f"{label}: expected frame {cursor}, found {start}")
        if end <= start:
            raise ValueError(f"Non-positive span at frame {start}")
        cursor = end
    if cursor != end_frame:
        raise ValueError(f"Expected final edge at frame {end_frame}, found {cursor}")
    return {"spans": spans, "end_frame": cursor}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    parser.add_argument("--track", required=True)
    parser.add_argument("--fps", type=Fraction, required=True)
    parser.add_argument("--end-frame", type=int, required=True)
    args = parser.parse_args()
    try:
        result = check(json.loads(args.snapshot.read_text()), args.track, args.fps, args.end_frame)
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.exit(1, f"{error}\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
