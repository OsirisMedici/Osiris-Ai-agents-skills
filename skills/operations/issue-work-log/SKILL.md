---
name: issue-work-log
description: Update an existing GitHub issue with client-shareable progress and actual proof files from the current task or chat. Use when asked to log meaningful work in an issue, attach screenshots, or publish a verified progress update.
---

# Issue work log

Publish an accurate progress comment on the task's existing GitHub issue, with every useful distinct proof image and relevant receipts from the current work. Keep all meaningful visual evidence and remove only established duplicates. There is no image-count limit or target. Return the verified direct comment link.

Explicit invocation authorizes an ordinary issue update and appropriate safe proof uploads for that issue. Complete them without repeated generic approval prompts. Automatic skill selection still requires a user request to publish. Keep the issue's audience/access unchanged. This workflow does not authorize implementation, deployment, client messages, customer changes, payments, closing issues, or changing Feedback task status.

## 1. Establish the issue and actual delta

Resolve the issue from the current task/chat, Feedback's linked issue, a verified mapping receipt, or exact task-UUID/source-link search. Read the issue and all comments. Distinguish the canonical issue from references or pull requests. Ask only if the destination remains materially ambiguous. Reuse the issue; this skill does not create a replacement. If Feedback is unavailable but the issue is established, continue using the verified issue and current evidence.

Reconstruct actual work since the last log using available chat/tool outputs, source diffs, saved readbacks, tests, and evidence files. Name what changed, why, who did it, what was saved/verified, the result, limits, remaining work/blockers, and next steps. Distinguish this task's work from pre-existing or concurrent work. Baseline observations remain baseline; plans remain future work.

| Evidence | Supported claim |
| --- | --- |
| Local source diff | Code changed locally; identify commit state when relevant. |
| Configuration readback | Named settings persisted, with version and draft/published state. |
| Structural validator | The structure passed that validator. |
| Test run and receipt | Named behavior passed in the stated environment/fixtures. |
| Deployment and runtime check | That deployed version behaved as observed. |
| End-to-end execution and downstream readback | The tested journey produced the observed downstream result. |
| Explicit user acceptance | The user accepted the stated result. |

A screenshot proves the visible state. It does not independently prove a save, delivery, runtime test, payment, or acceptance. Synthetic tests remain synthetic; an unpublished draft remains a draft. Tie completion claims to evidence at its actual level.

## 2. Gather and review proof

Inventory relevant files from this task's known attachments, returned generated-media paths, screenshot outputs, and evidence folders. Search scoped locations with `rg --files`. For an image without a local file, use an advertised export/download capability or retain its accessible artifact reference. Never claim access to another chat's images or absent files.

Inspect every candidate image and receipt. Verify provenance, relevance, and what each proves. Include every safe, relevant image that documents a distinct setup step, setting, screen, result, test, audit, or meaningful historical state. Similar-looking screens can show different work and must remain when they add evidence. Keep the full useful proof set rather than a highlight sample. Shorten repetitive prose, not distinct visual evidence; group images with concise captions when helpful.

Prefer actual captured/generated files; label mockups as mockups. Keep originals. If redaction is necessary, create and inspect a separate sanitized copy with an appropriate supported image tool. Remove credentials, session/signature material, unnecessary learner/customer details, hidden metadata, and unrelated private content. A generated redaction must preserve factual evidence; use a clean recapture or omit it if fidelity cannot be established. Confirm the issue audience is suitable. Public repositories, gists, external hosts, and access expansion are not upload fallbacks.

If an image is unavailable, state the limit and use available proof. Request it only if necessary. Meaningful text progress without safe images can be logged as text. Never manufacture proof to fill a section.

## 3. Deduplicate and attach

Read [attachment and recovery handling](references/attachments.md) before uploads or when transport/access fails. Discover current attachment tools first. When none supports issue uploads, use the in-app Browser's supported file chooser on the same issue, upload reviewed files, and collect permanent attachment Markdown. Prefer direct GitHub tools for comment text. Never invent an endpoint or copy browser credentials into a CLI.

Optionally run [the manifest helper](scripts/proof_manifest.py) with reviewed delta text and selected files. Read its `--help`. It computes file hashes and a deterministic log marker without network calls/uploads. Keep the manifest local because it contains local paths. Hashes prove neither provenance nor privacy nor truth.

Compare the delta and files against prior comments/upload receipts. Deduplicate repeated attachment URLs and identical file bytes. Different captures are duplicates only when visual inspection establishes the same work/state with no meaningful added detail; retain the clearer complete capture. Different steps, settings, or meaningful before/after states remain distinct. When uncertain, keep both.

Reuse verified permanent URLs instead of uploading identical files again. If an image is already visible on the issue, link its existing proof location rather than embedding it again. Every useful distinct image from this task must have a retained visual home; a hidden link is not a substitute for displaying new distinct proof. Preserve previous history and attachments. Exact log-marker matches are a no-op. For old unmarked or reworded logs, compare facts/evidence manually. If nothing material changed, return the existing comment link. New evidence can justify a supplemental comment referencing the earlier update, with every useful distinct new image included.

Keep a non-secret receipt beside task evidence when useful: issue URL, marker, file SHA-256 to permanent URL mapping, caption, provenance/proof level, upload state, verified comment URL. Record successful uploads immediately. After an unknown upload/comment outcome, inspect the editor/current comments and receipt before retrying. Reuse partial uploads.

## 4. Write and publish

Read [the progress template](references/progress-template.md). It adapts `proof-of-work-log`'s communication labels to GitHub with verification and next steps. Its optional Notion publishing does not apply here.

Read installed `leaving-pr-comments` before posting. Apply its attribution once, using the verified public model name or `Codex` if the harness exposes none, and verified user's name/login. Preview the entire Markdown, captions, and attachments for private data. Match claims to the evidence ledger. Include a stable hidden marker when available.

Discover GitHub schemas. Connected `add_comment_to_issue` may name its issue-number parameter `pr_number`; inspect its schema rather than assuming another destination. For a CLI gap, use authenticated `gh` with an exact UTF-8 `--body-file`; keep tokens private. Final Markdown contains permanent remote attachment URLs, never local paths or expiring signed redirects. Post once the text and safe proof are ready. If upload is blocked, publish useful verified text when authorized, disclose omitted proof, and retain files for a later supplement.

Append progress to preserve history. Edit a prior agent-authored comment only for a bounded correction or recovery of the same interrupted log. Preserve substantive history and identify corrections. Leave other authors' comments unchanged.

## 5. Verify and reconcile the checklist

Fetch the saved comment and match text, attribution, marker, captions, and permanent URLs to the draft. Reconcile the proof inventory: every useful distinct image is displayed once or already visible at its linked proof location; each omitted duplicate identifies its retained counterpart. Record unavailable or unsafe proof separately. Open the comment in the in-app Browser when available to verify rendered images or downloadable receipts under the intended account. Verify permanent URLs from the saved body rather than signed redirects. Record rendering/access failures separately from text-save success. URL text readback alone does not verify the attachment.

Reconcile checklist items only when evidence satisfies their completion conditions. Read the fresh issue body, change only supported check states, preserve concurrent/unrelated edits, save, and fetch again. Keep deployment/end-to-end items open when only code, configuration, or synthetic tests passed. Leave issue state open unless separately authorized to close it.

Return the direct progress comment link, what was logged, proof attached/reused/omitted, checklist changes, and material remaining work or verification limits. On persistent publication failure, retain a ready local draft and explain the blocker. End a completed final response with `over and out`.
