# In-app Browser export procedure

Use current documented browser APIs. Prefer direct PDF export if an advertised capability preserves the requested layout. In the observed Codex in-app Browser, the supported `cdp` tab capability provides `send()` for `Page.printToPDF`, `IO.read` and `IO.close`. Read its documentation first. Native Cmd+P opened an inaccessible app dialog in the original run; direct PDF printing in a fresh task-owned tab worked. Do not switch to personal Chrome or copy session credentials into another renderer.

## Prepare a faithful local view

Inspect the current title, issue-body and comment nodes. The bundled script currently recognizes `h1 bdi` or `h1 .markdown-title`, `[data-testid="issue-body-viewer"]`, and comment containers below `[data-testid="issue-timeline-container"]`. These are observed GitHub selectors, not a permanent API. Confirm loaded comment count against the direct read or visible pagination. A changed selector must not silently omit comments.

In a fresh permitted tab, use `Emulation.setEmulatedMedia` with `media: "screen"` and a light `prefers-color-scheme` feature. Execute the preparation helper through the documented CDP `Runtime.evaluate` capability, not a read-only DOM evaluator. It changes only the temporary document, never the saved issue. It sets GitHub's root theme attributes to light, clones issue content, removes UI controls, and fixes the content column to `210mm` with `8mm` internal padding. It does not modify source screenshots or replace their own native UI colors.

The helper returns the exact title, comment/proof counts, repeated URL occurrences, content dimensions and pending images. Require all retained images to load, then inspect the export. If useful linked proof is absent from the cloned embeds, add it to this local view with its existing caption and permanent URL. Visually compare suspected duplicates; the helper only removes exact repeated image sources. Private-image pixels remain embedded, while expiring signed image-link targets are removed from the export copy. Preserve verified permanent links and avoid persisting signed redirects in HTML/receipts.

The source browser viewport can be wider than A4. Measure `#codex-issue-pdf` itself, not the full browser or document scroll width. Its expected width is about `793.7008` CSS px. Check for content overflow; long code/URLs/tables must wrap or fit without cropping.

## Print and save

After the PDF skill's operation marker succeeds, the core print parameters are:

```javascript
{
  printBackground: true,
  displayHeaderFooter: false,
  preferCSSPageSize: false,
  paperWidth: 210 / 25.4,
  paperHeight: (Math.ceil(contentHeightCssPx) + 4) / 96,
  marginTop: 0,
  marginBottom: 0,
  marginLeft: 0,
  marginRight: 0,
  scale: 1,
  transferMode: 'ReturnAsStream'
}
```

Read the returned stream with `IO.read`, decode each chunk according to `base64Encoded`, save the browser PDF under work, then `IO.close`. Do not print the PDF bytes to tool output. If the renderer rejects excessive height, print supported consecutive A4-width chunks with zero browser margins and join them. Check the actual output instead of assuming a large paperHeight produced one page.

If a repeated print command stalls, retain any valid raw export already saved. When a new export is necessary, recover once in a fresh task-owned in-app tab, prepare its local view and print once. Stop after a persistent browser/security failure instead of switching browser surfaces or looping.

Use the Python runtime returned by `load_workspace_dependencies`; the join helper needs `pypdf`. Its normal command is:

```sh
python3 /absolute/path/to/github-issue-to-pdf/scripts/join_continuous.py \
  --input /absolute/path/to/work/browser-print.pdf \
  --output-dir /absolute/path/to/outputs \
  --title 'Exact title read from GitHub'
```

Keep title text in structured arguments or properly quoted strings, never shell interpolation. The helper refuses genuinely wide input so a sidebar layout cannot be disguised by shrinking it. Chromium may round a requested A4 width to `595.92 pt`; the helper accepts at most a one-point discrepancy and normalizes it to exactly `595.2756 pt`. Effective width includes UserUnit when present.

If printing unexpectedly adds a separate footer, first remove that non-content footer from the temporary export view. If multiple actual content segments remain, join the segments without dropping text, images or links. Avoid padding an entire nearly blank page into the final document. Inspect native renderer page-height and viewer support for unusually tall issues; report a real blocker rather than changing width or limiting evidence.

Close the temporary view after verification so DOM/theme overrides do not remain in the user's browser. The export changes no GitHub source data and requires no cleanup comment on the issue.
