#!/usr/bin/env python3
"""Read-only inventory for the Osiris T3 update skill; never build or install."""

import argparse
import json
import platform
import re
import subprocess
from pathlib import Path
from urllib.parse import urlparse


def command(args, cwd=None):
    result = subprocess.run(args, cwd=cwd, capture_output=True, text=True, check=False)
    if result.returncode:
        raise RuntimeError(f"{args[0]} failed (exit {result.returncode})")
    return result.stdout.strip()


def fork_matches(remote, fork):
    if remote.startswith("git@github.com:"):
        return remote.split(":", 1)[1].removesuffix(".git").lower() == fork.lower()
    parsed = urlparse(remote)
    return parsed.hostname == "github.com" and parsed.path.strip("/").removesuffix(".git").lower() == fork.lower()


def git_succeeds(repo, *args):
    return subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, check=False
    ).returncode == 0


def source_status(repo, registry):
    if not repo.is_dir() or not git_succeeds(repo, "rev-parse", "--is-inside-work-tree"):
        return {"path": str(repo), "available": False, "next": "Locate the fork checkout or prepare one in an authorized location, then rerun with --repo."}
    remote = command(["git", "remote", "get-url", "origin"], cwd=repo)
    return {
        "path": str(repo),
        "available": True,
        "origin_matches_fork": fork_matches(remote, registry["fork"]),
        "head": command(["git", "rev-parse", "HEAD"], cwd=repo),
        "branch": command(["git", "branch", "--show-current"], cwd=repo),
        "clean": not command(["git", "status", "--porcelain"], cwd=repo),
        "patches": [
            {
                "id": patch["id"],
                "commit": patch["commit"],
                "available_locally": git_succeeds(repo, "cat-file", "-e", patch["commit"] + "^{commit}"),
                "ancestor_of_source_head": git_succeeds(repo, "merge-base", "--is-ancestor", patch["commit"], "HEAD"),
            }
            for patch in registry["patches"]
        ],
    }


def descendants(pid):
    pending = [pid]
    seen = set()
    while pending:
        current = pending.pop()
        if current in seen:
            continue
        seen.add(current)
        yield current
        try:
            children = Path(f"/proc/{current}/task/{current}/children").read_text().split()
            pending.extend(int(child) for child in children)
        except (OSError, ValueError):
            continue


def server_status(t3_home):
    service = "t3code.service"
    report = {"service": service, "home": str(t3_home), "running_version": None}
    state_file = t3_home / "runtime/service-state.json"
    if state_file.exists():
        state = json.loads(state_file.read_text())
        report["state_version"] = state.get("activeVersion")
    try:
        values = command([
            "systemctl", "--user", "show", service, "-p", "ActiveState", "-p", "MainPID"
        ])
    except (OSError, RuntimeError):
        report["discovery"] = "User systemd unavailable; discover the actual server on its host."
        return report
    properties = dict(line.split("=", 1) for line in values.splitlines() if "=" in line)
    report["active"] = properties.get("ActiveState")
    report["main_pid"] = int(properties.get("MainPID", "0"))
    if not report["main_pid"]:
        return report
    versions = (t3_home / "runtime/versions").resolve()
    for pid in descendants(report["main_pid"]):
        try:
            process = Path(f"/proc/{pid}")
            argv = (process / "cmdline").read_bytes().split(b"\0")
            if len(argv) < 2 or argv[1] != b"serve":
                continue
            executable = (process / "exe").resolve(strict=True)
            relative = executable.relative_to(versions)
            report.update({"running_pid": pid, "running_version": relative.parts[0]})
            # Only this non-secret setting is extracted; never dump process environments.
            prefix = b"T3CODE_SERVER_BROWSER_EXECUTABLE="
            for item in (process / "environ").read_bytes().split(b"\0"):
                if item.startswith(prefix):
                    report["browser_executable_override"] = item[len(prefix):].decode(errors="replace")
                    break
            return report
        except (OSError, ValueError):
            continue
    report["discovery"] = "No managed serve child found; do not infer the running version from the launcher."
    return report


def choose_release(releases, channel):
    pattern = re.compile(r"^v?\d+\.\d+\.\d+" + (r"-nightly\.\d{8}\.\d+$" if channel == "nightly" else r"$"))
    candidates = [
        release for release in releases
        if not release.get("draft") and pattern.fullmatch(release.get("tag_name", ""))
        and (channel != "stable" or not release.get("prerelease"))
        and release.get("published_at")
    ]
    if not candidates:
        raise RuntimeError(f"No published {channel} release in the first 100 upstream releases; resolve it explicitly.")
    release = max(candidates, key=lambda value: value["published_at"])
    return {"tag": release["tag_name"], "published_at": release["published_at"], "url": release["html_url"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path)
    parser.add_argument("--home-dir", type=Path, default=Path.home() / ".t3")
    parser.add_argument("--channel", choices=["nightly", "stable"])
    parser.add_argument("--check-upstream", action="store_true", help="Read published releases via gh; does not fetch, build, publish, or install.")
    args = parser.parse_args()
    registry = json.loads((Path(__file__).resolve().parents[1] / "references/patches.json").read_text())
    repo = (args.repo or Path(registry["source_checkout"])).expanduser().resolve()
    report = {
        "mode": "read-only inventory; no build or installation performed",
        "host": {"system": platform.system(), "architecture": platform.machine()},
        "fork": registry["fork"],
        "source": source_status(repo, registry),
        "server": server_status(args.home_dir.expanduser().resolve()),
        "desktop": {"verified": False, "next": "Discover the Mac architecture, installed app, and available build/install access."},
    }
    if args.check_upstream:
        channel = args.channel or registry["default_channel"]
        releases = json.loads(command(["gh", "api", f"repos/{registry['upstream']}/releases?per_page=100"]))
        report["upstream_release"] = {"channel": channel, **choose_release(releases, channel)}
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (OSError, RuntimeError, ValueError, KeyError) as error:
        raise SystemExit(f"Preflight incomplete: {error}")
