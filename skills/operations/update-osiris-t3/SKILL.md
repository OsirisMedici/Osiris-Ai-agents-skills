---
name: update-osiris-t3
description: Update OsirisMedici's T3 Code fork to a published upstream release while carrying the adopted local fixes, verifying the combined build, and installing compatible VPS server and Mac desktop artifacts. Use for requests to update the Osiris T3 installation or prepare its next release; ordinary official updates do not preserve these patches.
---

# Update Osiris T3

Produce **a published upstream release plus the adopted Osiris fixes**, then test and install that combined build. Default to the installed release channel (currently nightly); honor a requested version or `prepare only`. Creating or inspecting this skill is not an update request.

## Establish the update

Read [the installation reference](references/installation.md) and [the patch registry](references/patches.json). Run the read-only preflight:

```bash
python3 <skill-directory>/scripts/status.py --check-upstream
```

Use `--repo <checkout>` when its default source checkout is unavailable. The report is inventory, not authorization or proof that installation is ready. Resolve current source, running server, and installed Mac app separately. Do not infer the installed version from a worktree, the launcher binary, an open PR, or a passing dev test.

When invoked on the MacBook, run Mac commands locally. The historical source path and Linux service in the reference describe the VPS; they are not assumed to exist on the Mac. For a desktop-only request, inspect remote server compatibility without installing/restarting the VPS. If a compatible server update is also necessary, report that boundary instead of silently expanding the requested installation.

Discover an available Mac build/install host or an established fork build workflow. Record architecture, installation method, signing identity, and connectivity without exposing credentials. This Linux VPS cannot build a complete macOS release alone. If Mac access/build infrastructure is missing, prepare what is possible and name the missing prerequisite; do not report the desktop as updated.

## Assemble and verify

- Use the requested published tag, or resolve the newest published release on the selected channel from `pingdotgg/t3code`. Pin its exact commit. Do not substitute upstream `main` for a released version.
- Build in an isolated checkout/state directory, following the repository's worktree rules. Do not move the user's current thread or switch an existing working checkout. If this thread may not create another checkout, prepare in the authorized existing checkout or resolve that constraint before changing it.
- Carry every adopted patch in the registry, including unmerged fork fixes. Check the actual source and focused regressions before deciding an upstream release makes a patch redundant. An empty/conflicting cherry-pick alone is not proof of equivalence. Resolve conflicts against intended behavior; never silently drop a fix to obtain a green build.
- Do not merge PRs, rewrite shared branches, publish releases, or change fork `main` merely to assemble a local update. Preserve candidate commits and add an adopted future fix to the registry when the user requests it. If a requested publish action needs a release branch, use the recorded fork release branch after checking its actual history.
- Run meaningful checks for carried changes and affected clients **one at a time** on this VPS. Follow the current AGENTS.md; do not run repo-wide suites. Do not use an unmodified `check:changed` runner that starts heavy checks concurrently. Report failed/incomplete checks explicitly; a scoped typecheck is not a full package pass.
- Build fresh server **and web assets** from the candidate; package the Mac desktop when its bundled client changes. Do not pair a newly patched binary with old official web assets. Use current build scripts and verify packaged versions and hashes, not just source tests.
- Exercise the configured-browser override and fill viewport in both control states, resize, corner click mapping, fixed device sizing, and a second viewer where relevant. Use isolated browser profiles and harmless pages. Follow current browser-verification authorization and the repository's supported test skill. Never act on another thread's or a human-controlled tab.

Read the build/update-feed traps in the installation reference before choosing a custom version or packaging. Keep a manifest outside the source checkout recording the upstream tag/SHA, carried and superseded patches, candidate SHA, versions, artifacts/checksums, and check results.

## Install and prove the installed result

An explicit request to run this skill **to update/install** authorizes that scoped installation and its necessary controlled restart. Honor narrower requests, current authorization limits, or an explicit approval condition; do not ask again for already authorized actions. Making the skill does not authorize running it.

Before changing the live installation, finish artifact preparation and checks, record the current runtime/app and a concrete rollback path, and arrange a restart window that does not cancel unrelated work. Keep browser profiles, cookies, authentication/keyring stores, environment settings, and `T3CODE_SERVER_BROWSER_EXECUTABLE` in place. Do not copy credential stores into build/test directories, reset profiles, or change authentication/browser settings as part of an update. Never run candidate servers against live userdata.

Deploy through a verified installation mechanism on each host. For this VPS, account for the launcher/service-state layout described in the reference; never replay the historical rollout script with its stale PIDs and versions. An update can terminate the agent doing the work: persist the rollout state and arrange an independent, bounded coordinator before restarting its own host. Kill only processes this run started or a verified owner of its specific dev port.

Preserve the old runtime/app for rollback. Protect the application database using its supported backup procedure when migration requires it; do not blindly restore a database over newer user work. A migrated database may prevent runtime-only rollback. Never promise reversibility without checking the target's migration behavior.

After reconnecting, verify the **running** server and **installed** desktop versions and protocol compatibility, then repeat the harmless viewport/control test on the installed client. Check that existing threads/settings remain available without capturing private content. Claim completion only for hosts actually updated and verified; distinguish built, installed, running, and manually pending states. On failure, stop promotion and use the validated rollback where compatible rather than retrying live mutations blindly.

Report installed versions/source, carried fixes, checks and acceptance evidence, any remaining Mac install step, and rollback location. Link any release/PR created under explicit authorization using the host's required linking tools.
