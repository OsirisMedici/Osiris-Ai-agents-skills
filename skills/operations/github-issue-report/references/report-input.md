# Report renderer input

Run with the bundled Python environment containing reportlab, pypdf and Pillow:

```sh
python3 /absolute/path/to/github-issue-report/scripts/render_report.py \
  --input /absolute/path/to/work/report.json \
  --output-dir /absolute/path/to/output/pdf/issue-specific-folder
```

Input strings are plain text, not Markdown or HTML. Paths are relative to the JSON file unless absolute. Source references are for local auditing and are not printed. The author reconciles facts and completion; the renderer only lays them out.

```json
{
  "title": "Exact GitHub issue title",
  "issue_url": "https://github.com/owner/repo/issues/123",
  "description": ["Task and audience.", "Current status and material limits."],
  "outcomes": ["Intended reader-facing result."],
  "tasks": [
    {"text": "Save the configuration in Draft.", "done": true, "source_refs": ["issue comment URL"]},
    {"text": "Verify delivery in production.", "done": false, "source_refs": ["issue URL"]}
  ],
  "proof_note": "Historical screenshots show saved configuration, not production acceptance.",
  "proof": [
    {"path": "images/01.png", "caption": "Saved configuration; remains unpublished.", "source_url": "https://github.com/user-attachments/assets/actual-id"}
  ]
}
```

Use an empty proof list only when the source has no proof images. State genuine unavailable-image gaps in proof_note and the evidence manifest; do not describe omitted images as included. A task requires an actual JSON boolean and source_refs. A completed task needs evidence for completion, not merely an intended requirement.

The renderer prefers the bundled Noto Sans pair, then installed Noto Sans/DejaVu Sans, with Arial as a final fallback. `--font-regular` and `--font-bold` can select another installed TrueType pair. It embeds those fonts and validates coverage for report text, including currency symbols. Older macOS Arial files lack the Indian rupee sign; use Noto Sans rather than substituting a box or silently changing the price notation. It preserves image aspect ratios and does not crop or alter screenshots.

Outputs are the exact-title PDF and a work receipt at `.report-work/layout.json`. The receipt contains document geometry, input hash, expected text, task states, proof hashes and element bounds measured from the document top. Keep it local.

For review strips, copy the final page with pypdf and set both MediaBox and CropBox to the desired vertical interval, accounting for UserUnit. Rasterize the temporary crop with Poppler at 120–144 DPI. Use overlapping intervals and cover the entire report. Verify the final PDF, not just source images or a design mockup.
