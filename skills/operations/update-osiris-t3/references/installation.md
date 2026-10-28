# Installation facts and release traps

These are verified starting facts from 2026-10-28, not permanent assertions. Rediscover live versions and capabilities on each invocation.

- Fork: `OsirisMedici/t3code`; upstream: `pingdotgg/t3code`. A clean source checkout was at `~/projects/t3code-live-browser`, branch `fix/live-3770-browser-executable`. The viewport worktree was separate. The suggested long-lived `osiris/live` branch is **not created by this skill installation**.
- Linux VPS server: user systemd service `t3code.service`, T3 home `~/.t3`, data `~/.t3/userdata`, HTTP bound to loopback port 3773. The last accepted installed server was `0.1.4-nightly.20261027.3770+osiris.browser.1`: upstream commit `7c3b3b3605efa695e9948051b569937fc1482c0f` plus the configured-browser patch. The viewport patch was tested and published as fork PR #3, but had not been installed.
- The service's ExecStart can name an old launcher version. Its `serve` child executable and `runtime/service-state.json` determine what is actually running. Version directories live at `~/.t3/runtime/versions/<version>`. Preserve service environment/drop-ins, including the browser executable override `/opt/google/chrome/chrome`. Read only settings needed; never dump service environments or secret files.
- The user views T3 in a **Mac desktop app**. Its architecture, current app version/path, signing identity, and remote installation access have not been established in this task. Do not invent an SSH hostname or claim that replacing a Linux server also updates the Mac's bundled web client.
- GitHub and Google browser sessions were verified to survive the earlier controlled browser-executable rollout. Those sessions must stay in their existing profiles. Use a separate profile/state for tests and keep private account content out of captures and release evidence.
- Historical rollout records are at `~/.local/state/t3-live-rollouts/20261028-browser`. They explain the installed layout, but their Python helpers hard-code old PIDs/versions and a server-only asset-copy shortcut. **Do not execute them as a general updater.** That shortcut cannot deliver the viewport client fix or a new upstream release. Do not copy historical credentials or profiles.

## Build and release discovery

Read the candidate revision's `AGENTS.md`, `docs/operations/release.md`, and build scripts. Entrypoints at the initial revision include `vp run build:desktop`, `scripts/build-cli-archive.ts`, and `scripts/build-desktop-artifact.ts` (`--platform mac --target dmg --arch <verified-arch> --build-version <version>`). Verify current flags with their source or help; do not assume this reference pins future APIs.

The fork's API listed CI/PR workflows only; it had **no active release workflow or repository release secrets**. The checked-out upstream release workflow is guarded to `pingdotgg/t3code` and uses custom Blacksmith runners and production configuration. Dispatching that workflow in the fork is not a working release setup. A first-time fork Actions/signing setup is separate work that must stay within the user's requested scope. A usable Mac build host is the alternative. Request needed secrets through `request_secret`, never chat.

Build server, web client, and desktop artifacts from the **same candidate**. Record exact upstream and candidate commits. Publish only to the fork when explicitly authorized; do not use upstream release automation to publish official npm packages, deploy the shared relay, or update the official hosted app.

## Versions and update feeds

The original desktop packager supports `T3CODE_DESKTOP_UPDATE_REPOSITORY=OsirisMedici/t3code` for its GitHub update feed. That requires compatible fork release assets and metadata; setting a repository alone does not create an updater service. Inspect current feed behavior before enabling it.

At this revision, `resolveDesktopUpdateChannel` accepts a nightly only when the version ends in `-nightly.YYYYMMDD.NUMBER`. Appending `+osiris...` does **not** preserve that desktop channel classification. Do not blindly reuse the previous server's suffix for Mac releases; verify version/feed compatibility and record the source/patch identity in a release manifest.

`packages/shared/src/cliRelease.ts` and the stock install scripts target official `pingdotgg/t3code` releases. A normal official update does not reapply local commits. A fork desktop feed alone does not retarget CLI/server updates. Do not invent an unsupported environment override, alter updater settings unasked, or silently install an official binary that drops the Osiris fixes.

If automatic fork updates are not configured, deliver the verified custom installer and report the manual Mac install boundary. An accessible built artifact is not an installed desktop update.
