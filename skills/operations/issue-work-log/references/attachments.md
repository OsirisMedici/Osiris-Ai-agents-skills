# Attachments and recovery

## Supported paths

Discover current GitHub upload/attachment tools and inspect schemas. At authoring on 29 October 2026, connected tools supported issue reads/writes and private-image download, but exposed no issue attachment upload operation. Authenticated `gh` supported ordinary issue operations. Its presence does not establish an upload API. Recheck on use.

For upload gaps, use the in-app Browser on the exact issue. Read its current file-upload documentation before interaction. In T3, apply `~/.config/osiris-agent-rules/t3-browser-profiles.md` and persistent Default explicitly. In Codex, use its advertised in-app Browser. Never automate personal Chrome.

Inspect the issue and signed-in account. Open the editor's visible attachment control and use the supported file chooser with reviewed absolute paths. Wait for upload completion, inspect returned Markdown, and record each permanent URL with its file hash. Files must be visible to the browser environment; remote paths are not automatically local browser paths. Use only supported, authorized transfers when needed.

Handle the complete retained proof inventory. Upload batching or a failed transfer does not authorize selecting a smaller highlight set. Reuse existing uploads, continue with remaining distinct files, and explicitly record any transport-blocked files for recovery. Apply the main skill's no-image-limit and established-duplicates-only rule.

Observed permanent URL shapes include `https://github.com/user-attachments/assets/<opaque ID>` for images and `https://github.com/user-attachments/files/<ID>/<filename>` for receipts. Use URLs returned by GitHub; do not construct them. Rendered private images may redirect to signed `private-user-images.githubusercontent.com` URLs. Keep permanent URLs in comments/receipts; do not print or persist signed query strings. Private-image download tools provide inbound access, not uploads.

## Browser uploads with direct comments

If the editor contains only your upload scratch text, capture completed attachment Markdown, then post the assembled comment through the connector. Do not also submit the browser draft. Preserve existing human drafts; use a separate task-owned tab/editor if necessary. Clear only your own scratch text after successful readback. Close temporary task-created tabs when safe. If browser submission is the available path, submit once and retrieve the comment URL/readback directly.

Repository files, gists, release assets, public hosts, and newly shared storage require a separate request. Local Markdown paths are not issue attachments.

## Recovery and verification

- Missing file: record the gap and use available proof; request it only when needed.
- Expired session: restore the permitted session under current account rules. Osiris handles required MFA/CAPTCHA or credential changes. Stop at security-policy blocks.
- Partial upload: record/reuse completed URLs. Inspect the editor for in-flight results before retrying.
- Unknown comment outcome: reread comments for marker/matching content before retrying. If duplicates cannot be ruled out, preserve the draft and report uncertainty.
- Attachment verification: reopen the saved comment and confirm images render or receipts download. A body URL proves a reference was saved, not reachability. If the Browser is unavailable, use an advertised authenticated read/download capability when it supports that URL; otherwise disclose the access/rendering gap.
- Persistent upload blocker: post useful verified text when authorized, disclose omitted attachments, and save proof locally for later supplementation. A text-save blocker leaves a draft, never a claim of publication.

## Local receipt

Keep non-secret recovery metadata beside task evidence. Check live comments before using it to skip work.

```json
{
  "issue_url": "https://github.com/OWNER/REPO/issues/NUMBER",
  "log_marker": "issue-work-log:HASH",
  "delta_file": "relative/path/to/reviewed-progress.md",
  "uploads": [
    {
      "sha256": "HASH_OF_UPLOADED_SANITIZED_BYTES",
      "local_path": "relative/path/to/safe-proof.png",
      "caption": "What this proves and its limit",
      "proof_level": "saved configuration",
      "url": "PERMANENT_URL_RETURNED_BY_GITHUB",
      "state": "uploaded",
      "access_verified": true
    }
  ],
  "comment_url": "URL_RETURNED_AND_READ_BACK",
  "comment_verified": true
}
```

Use false/null until verified. Local paths stay in this internal receipt; published text contains reviewed content and permanent links.
