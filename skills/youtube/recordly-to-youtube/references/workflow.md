# Local files and YouTube upload route

These are discovery hints for Recordly on macOS. Verify current paths, tools, channel identity and UI before use.

## Locate the recording

Recordly's state was under `~/Library/Application Support/Recordly/`:

- `recent-projects.json` named recently opened projects.
- Each `.recordly` project contained `videoPath` and editor settings.
- `recordings/Projects/` held project files and preview images.
- The source had an MP4 and an `.mp4.cursor.json` sidecar.

Read only relevant metadata. Use `ffprobe` for stream and duration inspection. Hash the MP4 to distinguish a new recording from an upload retry.

If a source file is missing, inspect authorized move/archive receipts and verify its hash before restoring only the required media and sidecars.

## Transcribe locally

The first run had FFmpeg and Whisper installed, with the `base` model cached. Discover current tools and models before installing or downloading anything. Check memory pressure before running heavy work concurrently.

Reuse a matching complete transcript. Otherwise extract mono 16 kHz audio into the recording's working directory and transcribe it once. Set these variables to the actual paths:

```bash
ffmpeg -v error -i "$recording_path" -vn -ac 1 -ar 16000 "$audio_path"
PYTHONUNBUFFERED=1 whisper "$audio_path" --model base --device cpu --fp16 False --threads 4 --output_dir "$transcript_dir" --output_format all --verbose True
```

Use a fresh destination or verified existing working files. Choose language based on the recording, including mixed-language speech. Read every transcript segment and check that the last reaches the spoken ending. Remove an extracted temporary WAV only after verifying the retained transcript and source.

This 32-minute recording took several minutes to transcribe locally. Keep output unbuffered, use bounded waits, and give progress updates. CPU completion time is not a reason to review only the opening. Do not start a second transcriber merely because the first is quiet.

## Channel and browser route

Verify the user-selected existing channel for each upload through its current account connection. Discover whether the connected tools support upload before choosing the browser route. Keep channel/account mappings in private configuration.

1. Open YouTube Studio in the in-app Browser and verify the channel. Select **Upload videos**, then **Select files**.
2. Read the browser's file-upload documentation. Start the chooser wait before clicking its visible control, then pass the absolute local path through the returned chooser. Attach an error handler immediately so a timeout does not reset the browser session.
3. Prefer the documented Playwright button click for the chooser flow. An accessibility click failed to deliver the chooser event on the first attempt. Inspect current UI after an action times out, because it may already have succeeded.
4. Fill title and description by their current accessible names. Use the thumbnail's **Upload file** chooser. An encoded JPEG made the first thumbnail compact without changing its composition.
5. Inspect **Show advanced settings**. The old channel defaults contained an agency sales description and unrelated HVAC, podcast, and advertising tags. Correct only this video's metadata. The first personal session used English and **People and blogs**.
6. Continue through video elements, initial checks, and visibility. Uploading does not establish public visibility. Read status back by the assigned video ID.

For the first run, a checks warning remained visible while the connector later reported **public** and **processed**. Avoid another upload or publish attempt based solely on a stale dialog. Open the watch page and saved Studio details.
