#!/usr/bin/env python3
"""Read-only macOS performance snapshot; names and counters, never process arguments."""
import argparse
import datetime
import json
import os
import pathlib
import platform
import re
import subprocess
import time


def command(*args, timeout=20):
    try:
        r = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
        return {'exit_code': r.returncode, 'stdout': r.stdout.strip(),
                'stderr': r.stderr.strip()[:2000]}
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {'exit_code': None, 'error': str(exc)}


def vm():
    r = command('/usr/bin/vm_stat')
    raw = r.get('stdout', '')
    match = re.search(r'page size of (\d+)', raw)
    if not match:
        return None, None, r
    return int(match.group(1)), {key: int(value) for key, value in
        re.findall(r'^([^\n:]+):\s+(\d+)\.', raw, re.M)}, r


def write_report(path, report):
    p = pathlib.Path(path).expanduser()
    p.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    fd = os.open(p, os.O_WRONLY | os.O_CREAT | os.O_TRUNC | os.O_NOFOLLOW, 0o600)
    with os.fdopen(fd, 'w') as f:
        os.fchmod(f.fileno(), 0o600)
        json.dump(report, f, indent=2)
        f.write('\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', help='Private JSON receipt path')
    parser.add_argument('--interval', type=float, default=5,
                        help='Swap-rate measurement interval, 1 to 30 seconds')
    args = parser.parse_args()
    if platform.system() != 'Darwin':
        parser.error('This helper requires macOS.')
    if not 1 <= args.interval <= 30:
        parser.error('--interval must be between 1 and 30 seconds.')
    page_size, before, first_result = vm()
    start = time.monotonic()
    time.sleep(args.interval)
    _, after, last_result = vm()
    elapsed = time.monotonic() - start
    report = {'read_only': True,
              'measured_at': datetime.datetime.now().astimezone().isoformat(),
              'os': command('/usr/bin/sw_vers'),
              'hardware': command('/usr/sbin/sysctl', 'hw.model', 'hw.memsize',
                                  'hw.ncpu', 'machdep.cpu.brand_string'),
              'swap': command('/usr/sbin/sysctl', '-n', 'vm.swapusage'),
              'pressure_level_raw': command('/usr/sbin/sysctl', '-n',
                                             'kern.memorystatus_vm_pressure_level'),
              'memory_query': command('/usr/bin/memory_pressure', '-Q'),
              'sample_seconds': round(elapsed, 3)}
    if before is not None and after is not None:
        deltas = {k: after.get(k, 0) - before.get(k, 0) for k in ['Swapins', 'Swapouts']}
        if min(deltas.values()) >= 0:
            report['swap_in_MB_per_second'] = round(deltas['Swapins'] * page_size / elapsed / 1e6, 2)
            report['swap_out_MB_per_second'] = round(deltas['Swapouts'] * page_size / elapsed / 1e6, 2)
        else:
            report['swap_sample_error'] = 'Counters reset during interval; rate unavailable.'
        report['compressor_bytes'] = after.get('Pages occupied by compressor', 0) * page_size
    else:
        report['vm_stat_errors'] = [first_result, last_result]
    s = os.statvfs('/System/Volumes/Data')
    report['data_volume'] = {'capacity_bytes': s.f_blocks * s.f_frsize,
                             'available_bytes': s.f_bavail * s.f_frsize,
                             'available_GB_decimal': round(s.f_bavail * s.f_frsize / 1e9, 2)}
    for name, cli in {
        'disk_free': ['/bin/df', '-h', '/', '/System/Volumes/Data'],
        'disk_io': ['/usr/sbin/iostat', '-d', '-w', '1', '-c', '2'],
        'thermal': ['/usr/bin/pmset', '-g', 'therm'],
        'battery_power': ['/usr/bin/pmset', '-g', 'batt'],
        'backup_status': ['/usr/bin/tmutil', 'status'],
        'indexing_status': ['/usr/bin/mdutil', '-s', '/'],
        'largest_processes': ['/usr/bin/top', '-l', '2', '-s', '1', '-o', 'mem',
                              '-n', '20', '-stats', 'pid,command,cpu,mem,state'],
    }.items():
        report[name] = command(*cli)
    top = report['largest_processes']
    if top.get('exit_code') == 0:
        top['stdout'] = 'Processes:' + top['stdout'].rsplit('Processes:', 1)[-1]
    report['limits'] = [
        'Resource indicators do not measure perceived UI latency or certify hardware health.',
        'Swap rates count logical memory-page bytes, not SSD throughput.',
        'Process memory can include compressed/shared allocations; summed values are not physical residency.',
        'High swap total alone does not prove current thrashing; compare rates, pressure, and workload.',
    ]
    if args.output:
        write_report(args.output, report)
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
