---
name: ship-live
description: Deploy finished code to the official running app and verify the team can use the changes. Use when Osiris says "ship live", "deploy to the official app", or asks to release completed coding work to the team's existing production app.
---

# Ship live

## Public setup

Resolve the user's authorized workspace before following file paths below.
`<workspace>` and named vault folders describe an existing layout, not bundled
data. Reuse equivalent files in the user's setup. Ask for a destination only
when discovery cannot resolve it. Private records and reference documents must
be supplied or located locally; do not invent their contents. Reuse answers
already in the request rather than repeating the intake. Use available supported
tools and the visible in-app Browser for browser work. Installing this skill
does not invoke it or authorize messages, publishing or unrelated service writes.

Turn the finished work in the current chat into a verified release on the app's existing official URL. The team should open its usual app and use the new behavior with its existing access.

`$ship-live` is the reusable command. Infer the app and intended changes from the current chat and owning repository. Creating or editing this skill does not itself invoke a deployment.

## Authorization and scope

A user request to ship live authorizes the ordinary release steps for the identified work: scoped commits, pushes, a PR and merge when the project's release process requires them, production deployment, and the documented service restart or promotion needed to activate that release. Proceed without asking for the same deployment permission again. Automatic discovery of this skill alone grants no production permission.

Respect branch protection, required checks, release locks, and approval controls. Ask a focused native question only when discovery cannot resolve the intended release or when an additional action needs authorization. Complete independent preparation first and show the concrete action needing approval.

Keep existing team access and security settings. "Everybody can use it" means the intended team through the established access model. Expanding permissions, making private data public, customer messaging, destructive data changes, new paid infrastructure, and unrelated releases need their own authorization.

## 1. Establish the release

- Read applicable project instructions and deployment documentation. Inspect Git status, the actual diff, branch, remotes, and any linked PR or task. Include finished task changes that are still uncommitted; preserve unrelated work. If the branch also contains unrelated commits, use an isolated release branch or worktree containing only the intended changes.
- Resolve the owning source repository, official app URL, production project or service, host, and established release method. In ScaleHQ, consult its registry for source ownership, then verify against current provider or host state. An issue tracker, old deployment file, or preview URL does not establish the live target.
- Identify the current production revision or artifact and its rollback route. Compare it with the intended release so another person's deployed work is preserved. If the intended version is already live, verify its behavior and report that result without deploying again.
- Resolve a genuinely ambiguous app, target, or change set with a native question. Ask only for information that inspection cannot establish.

Before mutation, give a short update naming the app, official URL, intended user-visible change, and release method. This is a progress update, not another approval request.

## 2. Prepare the exact version

- Run the project's required release checks and checks appropriate to the changed behavior. Reuse valid results for the same source revision and relevant environment. Resolve failures caused by this release; report a blocking failure rather than bypassing it.
- Before JS/TS tooling work, read `~/.config/osiris-agent-rules/javascript-tooling.md` and use Bun as directed. For cross-machine work, read `~/.config/osiris-agent-rules/t3-fleet.md`. Build and deploy on the owning host through its established process.
- Inspect any changed configuration, database migrations, workers, scheduled jobs, or feature flags needed for the behavior. Apply documented compatible release steps within the authorized scope. Prepare recovery for affected data when required by the project's process. Stop for approval before a destructive or incompatible migration that the user has not authorized.
- Commit and push only the intended work when the release process requires it. Use the project's PR and merge process, wait for required checks and reviews, and resolve release-related findings. Honor approvals without bypasses or force-pushing shared branches.

This step is complete when the checked source revision or immutable artifact is identified and ready for the established production process.

## 3. Deploy and follow through

Discover relevant purpose-built tools first. Use the established provider API, CLI, CI workflow, or host deployment script. Read the relevant installed provider skill when needed. Preserve the existing hosting arrangement.

Deploy the prepared version through that route. A push, merge, uploaded build, or green build job is an intermediate result. Follow the release through production promotion or service activation, including any required backend and worker components. Wait for a terminal deployment result and inspect failures while keeping the user informed of meaningful changes.

Check for another release before promotion. If production has moved since preparation, reconcile the intended changes with the newer version and revalidate before proceeding. Do not overwrite it blindly.

On failure, inspect the cause before retrying. Correct release-related problems within scope. If this release causes a regression, use the established compatible rollback to the recorded working version when available, then verify recovery. A rollback restores service but leaves the requested release incomplete. Stop repeated attempts when the same failure remains unresolved or continuing needs new authorization.

## 4. Verify the team's live experience

- Confirm the official URL serves the intended revision or artifact using provider deployment metadata, running image identity, a version endpoint, or comparable runtime evidence. A successful HTTP response alone cannot identify the release.
- Exercise the changed workflow on the official app. For UI changes, inspect the rendered result and affected interaction in the visible in-app Browser. Keep existing hidden sessions visible before interaction, and use its persistent Default profile as directed by `~/.config/osiris-agent-rules/t3-browser-profiles.md` when applicable.
- Check normal team access with an available authorized member session or supported permission inspection. Preserve authentication. Use sanctioned test records or reversible test actions for writes, and keep external sends outside smoke tests unless separately authorized.
- Check relevant service health and errors after activation. For stateful changes, verify the backend result as well as the screen. Confirm required flags and dependencies make the shipped behavior available to its intended audience.

Distinguish what was observed from what remains unverified. If authentication, browser policy, missing access, or unavailable runtime evidence blocks a check, report the precise limit. Continue independent checks, but do not claim that everyone can use the feature based only on deployment status.

## Handoff

Finish with the official app link, what the team can now do, the deployed revision or release identifier, what you verified, and a short way to try the change. State any remaining limitation or rollback plainly. Claim a verified live release only when the production identity and changed behavior have both been checked.

Keep useful non-secret release evidence in the project's existing deployment notes when appropriate. If the deployment route was missing or stale, record the verified source, target, release method, and recovery route there for the next run. Preserve existing task and issue links; skill invocation alone does not authorize messages or task-status changes.
