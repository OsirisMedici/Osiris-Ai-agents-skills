#!/usr/bin/env python3
"""Read-only storage inventory. Scans sequentially at reduced priority; never moves/deletes data."""
import argparse
import datetime
import json
import os
import pathlib
import platform
import plistlib
import subprocess
import time

HOME = pathlib.Path.home()
DEFAULTS = ['Desktop', 'Documents', 'Downloads', 'Movies', 'Pictures', 'Music',
            'Applications', 'Library/Caches', 'Library/Application Support',
            'Library/Developer', 'Library/Logs', 'Library/pnpm', '.t3', '.codex',
            '.cache', '.colima', '.npm', '.bun']


def disk_info(path):
    try:
        r = subprocess.run(['/usr/sbin/diskutil', 'info', '-plist', str(path)],
                           capture_output=True, timeout=15)
        if r.returncode:
            return {'path': str(path), 'error': 'diskutil info failed'}
        raw = plistlib.loads(r.stdout)
        keys = ['VolumeName', 'MountPoint', 'DeviceIdentifier', 'VolumeUUID',
                'FilesystemType', 'FilesystemName', 'TotalSize', 'VolumeFreeSpace',
                'ReadOnlyVolume', 'Internal', 'BusProtocol']
        result = {'path': str(path), **{key: raw[key] for key in keys if key in raw}}
        s = os.statvfs(path)
        result['filesystem_capacity_bytes'] = s.f_blocks * s.f_frsize
        result['filesystem_available_bytes'] = s.f_bavail * s.f_frsize
        result['statvfs_read_only'] = bool(s.f_flag & os.ST_RDONLY)
        result['write_access_reported_for_current_user'] = os.access(path, os.W_OK)
        return result
    except (OSError, ValueError, plistlib.InvalidFileException, subprocess.TimeoutExpired) as exc:
        return {'path': str(path), 'error': str(exc)}


def measure(path, depth, timeout):
    p = pathlib.Path(path).expanduser().absolute()
    record = {'root': str(p), 'started_at': datetime.datetime.now().astimezone().isoformat()}
    if p.is_symlink():
        return {**record, 'status': 'skipped_symlink'}
    if not p.exists():
        return {**record, 'status': 'missing_or_inaccessible'}
    cli = ['/usr/bin/du', '-k', '-x']
    cli += ['-s'] if depth == 0 else ['-d', str(depth)]
    cli.append(str(p))
    start = time.monotonic()
    try:
        r = subprocess.run(cli, capture_output=True, text=True, timeout=timeout)
        rows = []
        for line in r.stdout.splitlines():
            try:
                size, name = line.split('\t', 1)
                rows.append({'path': name, 'allocated_bytes': int(size) * 1024})
            except ValueError:
                continue
        rows.sort(key=lambda x: x['allocated_bytes'], reverse=True)
        record.update(status='complete' if r.returncode == 0 else 'partial_or_denied',
                      exit_code=r.returncode, entries=rows[:30],
                      omitted_entries=max(0, len(rows)-30), stderr=r.stderr.strip()[:2000])
    except subprocess.TimeoutExpired:
        record.update(status='timed_out', timeout_seconds=timeout)
    except OSError as exc:
        record.update(status='error', error=str(exc))
    record['elapsed_seconds'] = round(time.monotonic() - start, 2)
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', action='append', help='Exact root; repeat to scan several sequentially')
    parser.add_argument('--depth', type=int, choices=[0, 1, 2], default=0)
    parser.add_argument('--timeout', type=int, default=90, help='Per-root timeout, seconds')
    parser.add_argument('--output', help='Private JSON receipt path')
    args = parser.parse_args()
    if platform.system() != 'Darwin':
        parser.error('This helper requires macOS.')
    if not 1 <= args.timeout <= 300:
        parser.error('--timeout must be between 1 and 300 seconds.')
    try:
        os.nice(10)
    except OSError:
        pass
    s = os.statvfs('/System/Volumes/Data')
    report = {'read_only': True,
              'measured_at': datetime.datetime.now().astimezone().isoformat(),
              'data_volume': {'capacity_bytes': s.f_blocks * s.f_frsize,
                              'available_bytes': s.f_bavail * s.f_frsize},
              'internal_disk': disk_info('/'), 'mounted_volumes': [], 'scans': []}
    try:
        for p in pathlib.Path('/Volumes').iterdir():
            if p.is_symlink() or not os.path.ismount(p):
                continue
            report['mounted_volumes'].append(disk_info(p))
    except OSError as exc:
        report['volumes_error'] = str(exc)
    roots = args.root or [str(HOME / name) for name in DEFAULTS]
    for path in dict.fromkeys(roots):
        print('Measuring ' + str(path), flush=True)
        row = measure(path, args.depth, args.timeout)
        report['scans'].append(row)
        print('  ' + row['status'], flush=True)
        if args.output:
            write_report(args.output, report)
    report['limits'] = [
        'Metadata inventory only; classifications and mutation approval require agent review.',
        'Partial, denied, and timed-out scans are not complete inventories.',
        'Nested paths, APFS clones, hard links, snapshots, sparse files and concurrent work affect estimates.',
        'Allocated folder bytes are not guaranteed reclaimable bytes; do not sum overlapping roots.',
        'Device identity metadata is private and should not be pasted into public reports.',
    ]
    if args.output:
        write_report(args.output, report)
    print(json.dumps(report, indent=2))


def write_report(path, report):
    p = pathlib.Path(path).expanduser()
    p.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    fd = os.open(p, os.O_WRONLY | os.O_CREAT | os.O_TRUNC | os.O_NOFOLLOW, 0o600)
    with os.fdopen(fd, 'w') as f:
        os.fchmod(f.fileno(), 0o600)
        json.dump(report, f, indent=2)
        f.write('\n')


if __name__ == '__main__':
    main()
