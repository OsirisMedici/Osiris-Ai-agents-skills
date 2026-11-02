# GHL newsletter editor notes

Observed in native GHL Design Editor work in November 2026. UI labels and selectors are discovery hints, not a stable API. Reinspect the current interface before acting.

## Saved-state reliability

- Selecting a canvas item opens its settings. Clicking the selected item again can close the panel; inspect panel state before repeating a click.
- Rich-text fields can show DOM edits that never reach the app's saved model. Generic clear/type operations on a contenteditable were insufficient in the source task. Prefer native typing/formatting. If the host permits standard browser editing commands, select the intended text block, focus its contenteditable, perform the browser edit and let that editor transaction commit before moving on. Never mutate application stores or use undocumented internal write APIs.
- Edit one block at a time. Batched edits across blocks before the app commits can affect the wrong selected block. Wait for observable editor/save state rather than assuming a fixed delay proves persistence.
- Save, reload and compare the complete copy. A successful toast alone does not prove every edit persisted. Wait for the template to finish loading before reading fields; subject/preheader can appear blank during loading.
- Undo or retry only after reconciling actual state. If a duplicate/save result is uncertain, inspect the template library before creating another copy.

## Formatting pitfalls

Pasted body paragraphs can inherit a heading's style. Inspect paragraph semantics, size and alignment separately from the heading. Normalising paragraph formatting can remove centring; use the native Text Align control to restore it where the selected design calls for it. Check the generated preview, not only selected text in the editor.

Buttons have separate label and URL fields. Editor-canvas anchors can use `#top` while preview HTML contains the real destination; validate the saved generated link. Update subject and preview text in Template settings, not just the visible headline. Preserve sender fields unless their change is in scope.

## Native reuse and copying

Duplicate inside a client location for ordinary revisions. Keep the master and use a new edition name. Copying between locations needs the intended destination account and a supported share/copy path. If authorized, prefer agency-restricted sharing and remove temporary sharing after copying; do not expose a public template link merely to bypass account limitations. A same-name account is insufficient identity evidence.

Image blocks, text blocks, buttons and social links should remain separately editable when native editing is required. Verify this after importing; do not describe an opaque HTML block or screenshot as a fully editable native template.

## Preview and handoff

Check the actual GHL desktop/mobile previews for:

- Image loading and sensible cropping; column pairs stack in the intended reading order.
- Headline wrapping, body typography and alignment, section spacing and CTA visibility.
- Correct image labels/alt text, social links and footer identity.
- Complete new copy and absence of old brand, project, recipient-specific tracking or restricted assets.

If the UI exposes generated HTML in a preview iframe's `srcdoc`, it can be read as a saved-template export. Cross-origin/sandbox rules may prevent reading the frame document itself; do not bypass them. Parse the exposed HTML separately for links/text when supported. For large tool responses, read bounded chunks and concatenate without printing the full HTML or inline image data into logs.

Website-hosted images are convenient for a demo, but are an external dependency. For a separately authorized send, confirm permitted hosting, format support, image weight, meaningful alt text and client approval. Browser WebP rendering does not establish support in every inbox client.

For a visual deliverable, use the host's supported preview/render tools. Keep the native GHL template as the editable master and make clear if the shown artifact is an export. Do not claim actual Gmail/Outlook delivery, MIME, unsubscribe or reply routing passed unless those were tested in the authorized scope.
