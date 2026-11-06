#!/usr/bin/env python3
"""Update local skills from GitHub and publish a reviewed batch."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

REPO_URL = "https://github.com/OsirisMedici/Osiris-Ai-agents-skills.git"
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
IGNORED_DIRS = {".git", "__pycache__", "node_modules", ".venv"}
PRIVATE_DIRS = {"client-data", "evidence", "runs", "credentials"}
INVENTORY = Path("docs/skill-sync-inventory.json")
STATE_DIRECTORY = ".osiris-skills-sync"
CATALOG_LINK = """## Sync across computers

For the first install, run these commands with Git and Python 3.9 or later.

```sh
git clone https://github.com/OsirisMedici/Osiris-Ai-agents-skills.git
cd Osiris-Ai-agents-skills
python3 skills/tools/osiris-skills-sync/scripts/sync.py --apply
```

On Windows, use `py -3` if Python is installed under that command. Reopen your
agent session to discover the new skills. For later updates, invoke
[`$osiris-skills-sync`](skills/tools/osiris-skills-sync/SKILL.md). Pulling
requires no GitHub account. Pass `--skills-dir` to target another supported
agent's user skill folder.

The sync installs missing packages and updates tracked copies with no local
edits. It reports differing pre-existing copies and leaves those in place.
Each updated copy has a local backup. Run the script without flags to preview
the work. GitHub contributors can also publish reviewed packages with
`--apply --publish NAME` or `--apply --publish NAME:CATEGORY`.

The [sync inventory](docs/skill-sync-inventory.json) lists the current packages
and file hashes.
"""


def git(*args, cwd=None, capture=False):
    command = ["git"]
    if shutil.which("gh"):
        command += ["-c", "credential.https://github.com.helper=!gh auth git-credential"]
    return subprocess.run(
        command + list(args), cwd=cwd, check=True, text=True, capture_output=capture,
        env={**os.environ, "GIT_TERMINAL_PROMPT": "0"},
    ).stdout


def package_files(root, *, publishing=False):
    if root.is_symlink() or not root.is_dir():
        raise ValueError(f"Expected a real skill directory at {root}")
    files = {}
    for directory, directories, names in os.walk(root):
        folder = Path(directory)
        directories[:] = sorted(name for name in directories if name not in IGNORED_DIRS)
        for name in directories + sorted(names):
            path = folder / name
            if path.is_symlink():
                raise ValueError(f"Symlink inside {root.name}: {path.relative_to(root)}")
            if publishing and (name in PRIVATE_DIRS or (
                name != ".env.example" and (name == ".env" or name.startswith(".env."))
            ) or path.suffix.lower() in {".pem", ".key", ".p12", ".pfx"}):
                raise ValueError(f"Private file or directory in {root.name}: {path.relative_to(root)}")
            if name in names and name != ".DS_Store" and path.suffix != ".pyc":
                if not path.is_file():
                    raise ValueError(f"Unsupported file in {root.name}: {path.relative_to(root)}")
                files[path.relative_to(root)] = path
    return files


def fingerprint(files):
    return {
        path.as_posix(): {
            "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "executable": bool(source.stat().st_mode & 0o100),
        }
        for path, source in sorted(files.items())
    }


def validate_skill(name, files):
    entry = files.get(Path("SKILL.md"))
    if entry is None:
        raise ValueError(f"{name} is missing SKILL.md")
    lines = entry.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        raise ValueError(f"{name} is missing YAML frontmatter")
    frontmatter = lines[1:lines.index("---", 1)]
    if f"name: {name}" not in frontmatter:
        raise ValueError(f"{name} must match its frontmatter name")


def copy_files(files, destination):
    for relative, source in files.items():
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def remote_packages(checkout):
    packages = {}
    for entry in sorted((checkout / "skills").glob("*/*/SKILL.md")):
        if any(path.is_symlink() for path in (entry, entry.parent, entry.parent.parent, checkout / "skills")):
            raise ValueError(f"Symlink in remote package path: {entry.relative_to(checkout)}")
        name = entry.parent.name
        if name in packages or not NAME.fullmatch(name) or not NAME.fullmatch(entry.parent.parent.name):
            raise ValueError(f"Invalid or duplicate remote skill: {entry.relative_to(checkout)}")
        packages[name] = entry.parent
    return packages


def read_state(state_dir):
    manifest = state_dir / "installed.json"
    return json.loads(manifest.read_text(encoding="utf-8")) if manifest.exists() else {}


def report(checkout, packages, skills_dir, state):
    plan = []
    for name, published in packages.items():
        local = skills_dir / name
        published_hash = fingerprint(package_files(published))
        if not os.path.lexists(local):
            print(f"Missing: {name}")
            plan.append((name, None, published_hash))
            continue
        try:
            local_hash = fingerprint(package_files(local))
        except ValueError:
            local_hash = None
        if local_hash == published_hash:
            state[name] = published_hash
        elif local_hash is not None and local_hash == state.get(name):
            print(f"Update: {name}")
            plan.append((name, local_hash, published_hash))
        else:
            print(f"Variant: {local} <> {published.relative_to(checkout)}")
    candidates = sorted({
        entry.parent.name for entry in skills_dir.glob("*/SKILL.md")
        if NAME.fullmatch(entry.parent.name)
    } - packages.keys())
    print("Local-only candidates:", ", ".join(candidates) or "none")
    return plan

def publish(checkout, packages, source_dir, selections):
    changes = []
    for selection in selections:
        name, separator, category = selection.partition(":")
        if not NAME.fullmatch(name) or (separator and not NAME.fullmatch(category)):
            raise ValueError(f"Expected NAME or NAME:CATEGORY, got {selection}")
        previous = packages.get(name)
        if previous and separator and previous.parent.name != category:
            raise ValueError(f"{name} already belongs in {previous.parent.name}")
        if previous is None and not separator:
            raise ValueError(f"Choose a category for {name} with --publish {name}:CATEGORY")
        destination = previous or checkout / "skills" / category / name
        if destination.parent.is_symlink() or (previous is None and os.path.lexists(destination)):
            raise ValueError(f"Unexpected existing publication path for {name}")
        files = package_files(source_dir / name, publishing=True)
        validate_skill(name, files)
        before = fingerprint(package_files(previous)) if previous else {}
        after = fingerprint(files)
        if before.keys() - after.keys():
            raise ValueError(f"{name} would remove published files. Review that change in Git.")
        if before != after:
            changes.append((destination, files))
        packages[name] = destination

    if not changes:
        print("Selected packages already match GitHub.")
        return

    with tempfile.TemporaryDirectory(prefix="osiris-skills-scan-") as directory:
        scan = Path(directory)
        for destination, files in changes:
            copy_files(files, scan / destination.name)
        subprocess.run(["gitleaks", "dir", "--redact=100", "--no-banner", str(scan)], check=True)
        for destination, files in changes:
            copy_files(package_files(scan / destination.name), destination)

    inventory = {
        name: {"path": folder.relative_to(checkout).as_posix(), "files": fingerprint(package_files(folder))}
        for name, folder in sorted(packages.items())
    }
    (checkout / INVENTORY).parent.mkdir(exist_ok=True)
    (checkout / INVENTORY).write_text(json.dumps(inventory, indent=2) + "\n", encoding="utf-8")
    readme = checkout / "README.md"
    contents = readme.read_text(encoding="utf-8") if readme.exists() else ""
    if INVENTORY.as_posix() not in contents:
        readme.write_text(contents.rstrip() + "\n\n" + CATALOG_LINK, encoding="utf-8")
    paths = [destination.relative_to(checkout).as_posix() for destination, _ in changes]
    git("add", "--", *paths, INVENTORY.as_posix(), "README.md", cwd=checkout)
    for destination, _ in changes:
        tracked = git(
            "ls-files", "-z", "--", destination.relative_to(checkout).as_posix(),
            cwd=checkout, capture=True,
        ).strip("\0").split("\0")
        expected = {(destination / path).relative_to(checkout).as_posix() for path in package_files(destination)}
        if set(tracked) != expected:
            raise ValueError(f"Git did not stage the complete {destination.name} package")
    git("diff", "--cached", "--check", cwd=checkout)
    git("commit", "-m", "Sync reviewed skills: " + ", ".join(path.name for path, _ in changes), cwd=checkout)
    git("push", "origin", "HEAD:refs/heads/main", cwd=checkout)
    print("Published:", git("rev-parse", "HEAD", cwd=checkout, capture=True).strip())


def install(name, published, skills_dir, state_dir, local_hash, published_hash):
    files = package_files(published)
    validate_skill(name, files)
    destination = skills_dir / name
    backup = None
    with tempfile.TemporaryDirectory(prefix="install-", dir=state_dir) as directory:
        staged = Path(directory) / name
        copy_files(files, staged)
        if fingerprint(package_files(staged)) != published_hash:
            raise ValueError(f"Staged files did not match GitHub for {name}")
        if local_hash is not None:
            if not destination.is_dir() or fingerprint(package_files(destination)) != local_hash:
                print(f"Skipped {name}: local files changed during sync")
                return False
            backups = state_dir / "backups"
            backups.mkdir(exist_ok=True)
            backup = Path(tempfile.mkdtemp(prefix=f"{name}-", dir=backups)) / name
            destination.rename(backup)
        try:
            if os.path.lexists(destination):
                raise FileExistsError(f"A local entry appeared at {destination}")
            staged.rename(destination)
        except OSError:
            if backup and not os.path.lexists(destination):
                backup.rename(destination)
            raise
    if backup:
        print(f"Updated: {destination} (backup: {backup})")
    else:
        print(f"Installed: {destination}")
    return True


def sync_local(checkout, packages, skills_dir, state_dir):
    state = read_state(state_dir)
    plan = report(checkout, packages, skills_dir, state)
    installed = updated = 0
    for name, local_hash, published_hash in plan:
        if install(name, packages[name], skills_dir, state_dir, local_hash, published_hash):
            state[name] = published_hash
            installed += local_hash is None
            updated += local_hash is not None
    with tempfile.TemporaryDirectory(prefix="manifest-", dir=state_dir) as directory:
        staged = Path(directory) / "installed.json"
        staged.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
        staged.replace(state_dir / staged.name)
    print(f"Installed {installed} missing skill(s), updated {updated} skill(s).")

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    codex_home = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")
    parser.add_argument("--skills-dir", type=Path, default=codex_home / "skills")
    parser.add_argument("--source-dir", type=Path, help="Directory containing reviewed package folders")
    parser.add_argument("--apply", action="store_true", help="Install or update local packages and push selected changes")
    parser.add_argument("--publish", action="append", default=[], metavar="NAME[:CATEGORY]")
    args = parser.parse_args()
    names = [item.split(":")[0] for item in args.publish]
    if args.publish and (not args.apply or len(names) != len(set(names))):
        parser.error("--publish requires --apply and each package can be selected only once")
    skills_dir = args.skills_dir.expanduser().resolve()
    source_dir = (args.source_dir or skills_dir).expanduser().resolve()
    with tempfile.TemporaryDirectory(prefix="osiris-skills-sync-") as directory:
        checkout = Path(directory)
        git("clone", "--quiet", "--depth", "1", "--branch", "main", REPO_URL, directory)
        packages = remote_packages(checkout)
        state_dir = skills_dir / STATE_DIRECTORY
        if state_dir.is_symlink():
            raise ValueError(f"Expected a real state directory at {state_dir}")
        if not args.apply:
            print("Repository revision:", git("rev-parse", "HEAD", cwd=checkout, capture=True).strip())
            report(checkout, packages, skills_dir, read_state(state_dir))
            return
        state_dir.mkdir(parents=True, exist_ok=True)
        lock = state_dir / "lock"
        try:
            lock.mkdir()
        except FileExistsError:
            raise ValueError(f"Another sync holds {lock}. If it stopped, verify it exited before removing the lock.")
        try:
            if args.publish:
                publish(checkout, packages, source_dir, args.publish)
            print("Repository revision:", git("rev-parse", "HEAD", cwd=checkout, capture=True).strip())
            sync_local(checkout, packages, skills_dir, state_dir)
        finally:
            lock.rmdir()


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"Sync stopped: {error}", file=sys.stderr)
        sys.exit(1)
