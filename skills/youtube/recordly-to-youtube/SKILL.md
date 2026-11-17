---
name: recordly-to-youtube
description: Turn Osiris's Recordly recordings into full YouTube uploads. Read the complete transcript, create a title and thumbnail, upload, and verify publication. Use after a recording or to resume an interrupted upload.
---

# Recordly to YouTube

Osiris records real work and thinks aloud. Preserve the full session for YouTube. Instagram excerpts are a separate deliverable when requested. Understand the recording before proposing its title, story, or edits.

## Resolve this run

- Use the supplied recording or project. Otherwise inspect Recordly's recent-project list, completed MP4s, and project metadata to identify the latest completed recording. Cross-check its identity rather than relying on a filename or modification time alone. Ask only when several recordings are plausible.
- An explicit request to run this workflow and publish a recording authorizes that recording's upload and publication on the verified existing channel. A preparation or review request stops at that scope. Automatic skill selection alone does not authorize publishing.
- Honor an already approved title, thumbnail, visibility, and choice to keep the full video. Resolve a genuinely ambiguous channel or visibility once. Continue within the authorization already given.
- Reuse the recording's transcript and publish package when their source identity matches. If a video ID exists, read its status and resume that upload before considering a new one.

## Inspect and transcribe

1. Resolve this skill's real directory and read [the local and upload reference](references/workflow.md). Check the MP4 and Recordly project. Record duration, dimensions, audio streams, file size, and SHA-256. Preserve the source and cursor sidecar.
2. For a missing MP4, inspect recent move or archive receipts. Restore only the matching source and needed sidecars to absent paths, verify their recorded hashes, and authenticate the complete archive. Keep unrelated archived material on its existing storage. A project file or preview image cannot replace the video.
3. Transcribe the complete audio using available local tooling. Reuse a matching full transcript. Save timestamped JSON and a readable transcript with the recording's working files. Read every segment through the end before making editorial decisions. Sample frames at meaningful points as well.
4. Automatic transcription can contain word errors. Check important names and quoted phrases against the source when they affect packaging or excerpts. Disclose any inability to audition audio. A transcript review does not establish that every frame was watched or the entire recording was listened to.

## Package the full session

- Follow Osiris's voice records through `$osiris-brand` when drafting copy. Read the shared design toolkit required by the current workspace. Use `$imagegen` for a generated raster thumbnail.
- Choose one title from the recording unless Osiris already chose it. Preserve his reflections and conversational character. The subject may extend beyond the software visible on screen.
- Create one readable landscape thumbnail tied to the title. Use a selected real image or an honest graphic. Keep accurate wording and avoid invented faces, results, or private calendar labels. Inspect it and save the final upload asset locally.
- Write a concise description from the source. Add useful chapters using the full video's clock. Distinguish estimates and personal opinions from verified results. Keep private client details out of newly written packaging unless specifically authorized.
- For an unchanged full recording, upload the verified source MP4. When Osiris requests Recordly framing, overlays, or edits, export and inspect the intended project first. Preserve the full duration unless he requests cuts.
- Save `youtube-publish-package.json` beside the transcript. Include source path, hash, duration, approved choices, title, description, thumbnail path and prompt, channel ID, visibility, video ID when assigned, and current status. This is the resume record.

## Upload and publish

1. Verify the signed-in channel using direct tools. Use a suitable upload connector when available; otherwise use the in-app Browser. Follow the focused browser route in [workflow.md](references/workflow.md). Keep credentials in their registered account system.
2. Upload the full file once. Record the video ID as soon as YouTube assigns it. On an uncertain response, read that video's status before retrying.
3. Set title, description, and thumbnail. Inspect inherited defaults and replace unrelated descriptions or tags on this video. Keep its language accurate and choose a suitable category. Classify audience, paid promotion, and realistic AI alterations from the content and displayed questions. An abstract AI-generated thumbnail does not make the original screen recording a fabricated realistic event.
4. Wait for upload and processing. When checks remain pending, inspect the saved status before interpreting an open dialog or retrying publication. Distinguish a private uploaded draft from a published video. If a provider restriction needs user verification, preserve the upload and return the exact required action.
5. Publish with the authorized visibility. Read back title, channel, visibility, processing status, duration, and thumbnail. Open the watch page, confirm playback advances, save a screenshot, and pause playback.
6. Update the package with the verified URL, status, timestamps, checks, and unresolved limits. Retain source media, project, transcript, thumbnail, and receipts for later excerpts. Creating or installing this skill does not itself run an upload.

Finish with the video link, actual visibility, confirmation that the full recording was retained, and any processing still pending. Follow the workspace's completion signal.
