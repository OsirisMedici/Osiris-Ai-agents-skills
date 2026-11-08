# Edits for macOS

## Connect and inspect

In Edits, open **Settings → Automation**. Use the Automation Server only with the user's authorization. Keep it on loopback. Prefer a configured Edits MCP connector. Otherwise, use the bundled Python bridge with an exported token in the current process, or copy the app's **Codex** setup snippet and pass `--clipboard` to read it in memory. Never paste the snippet into a chat, execute the copied shell text, print the token, or save it in a project. The bridge accepts only a loopback endpoint and does not follow redirects.

From the skill folder, for the default port:

```sh
python3 scripts/edits_mcp.py --clipboard call appState
python3 scripts/edits_mcp.py --clipboard tools --match 'elements|tracks|addMedia|Transform|saveProject'
python3 scripts/edits_mcp.py --clipboard call elements --args '{"fields":["id","trackId","startTime","endTime","text"]}'
```

`--clipboard` reads the current app-generated snippet each time. If the clipboard changed, copy the snippet again. With an existing `METAPILOT_TOKEN` environment variable, omit `--clipboard`. The tool catalog differs between the library and an open editor. Discover current schemas before a write. The bridge requires `--write` for calls outside its read allowlist. The flag expresses tool intent and does not grant authorization.

## Build the timeline

- Confirm the project ID against a saved-state readback before timeline changes. Take a snapshot of existing clips and caption transforms for a revision. Keep a copy or baseline export when practical.
- The Mac file picker can grant source access that an absolute-path MCP import lacks. If a direct import reports a sandbox bookmark or permission error, use **File → Import Media**, select the specific files, then confirm the assets appear online in the media panel. Store derived cutaways in a stable project folder rather than a temporary directory.
- `addMediaPanelItemsToTimeline` can place an alias as an overlay with `startTime`, `sourceIn`, and `sourceOut`. Give it an exact frame span. `setTransform` applies position and scale; use `keyframes="reject"` for a static transform on an unkeyframed clip if the live schema requires a keyframe policy. Confirm the transform and render a frame. `moveToLayer` takes the current layer index, so resolve that index from `tracks` again after any track change.
- When there is no suitable editable caption import, short native text overlays can work as captions. Verify font, contrast, safe position, and exact speech timing in a rendered frame. Newly added shapes can cover text reused on an existing lower track. Check layer order and move the background to a free lower lane if needed.
- If a replacement import is deduplicated and returns no alias, use the existing media-bin alias to add the replacement at the same frame edges. Remove only the old target element and verify the new clip's track and transform.

## Check coverage and export

For continuous overlays, get the exact main timeline end frame, export the `elements` response to JSON with at least `trackId`, `startTime` and `endTime`, then run:

```sh
python3 scripts/check_overlay_track.py elements.json --track TRACK_ID --fps 30 --end-frame FRAME_COUNT
```

The checker fails on a missing span, an overlap, an off-frame edge, or an end that disagrees with the intended edit. Check frames near the formerly empty spans as well, since timing alone does not prove that media renders.

Use the normal Edits **Export** control if a programmatic destination fails with macOS permissions. Choose the source-appropriate resolution, frame rate and SDR/HDR setting. Read the actual export status or find the newly written file, then probe it. Native output may be HEVC. For a compatible local review copy, encode H.264 and copy the original audio when appropriate. For an overlay-only revision, FFmpeg's decoded audio MD5 can verify the same dialogue before and after. Keep the native project and review copy separate.

If the library offers `exportMcomp`, treat a portable project package as a separate deliverable. Edits may reject caption or font features that its interchange format cannot preserve. Keep the saved native timeline and archive the frame plan, typography, and source media if the original design cannot be packaged faithfully.
