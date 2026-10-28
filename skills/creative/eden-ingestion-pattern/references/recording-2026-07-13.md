# Eden content ingestion recording — 2026-07-13

## Capture

- Window: `2026-07-13T13:21:21Z` to `2026-07-13T13:23:54Z`
- Evidence source: Record & Replay event stream

## Directly observed behavior

1. A public YouTube link was copied and pasted onto an Eden board canvas with `Command-V`.
2. Roughly 12 seconds after the paste, Eden displayed a rich item containing:
   - an embedded YouTube player;
   - video title;
   - creator name and handle;
   - publication date;
   - view count;
   - thumbnail access;
   - the source description;
   - an Open original action.
3. The same newly created item explicitly displayed: `No transcript stored for this post yet — fetch one now to pull it from the source.`
4. A `Fetch transcript` button was visible. The transcript was therefore deferred rather than generated automatically during paste ingestion.
5. A different existing YouTube item also showed the same no-transcript state and fetch action.
6. Eden offered `Chat`, `Chat with`, and `Boost in chat` actions that could carry selected sources into a chat pane.
7. An existing chat response said it had pulled transcripts from foundational board videos and synthesized them. This supports on-demand transcript retrieval during a chat workflow, but does not reveal which backend service performed it.

## Strong inference

The product is consistent with three separately metered layers:

1. **Cheap metadata ingestion** — resolve the URL, fetch source metadata, normalize it, and create the board card.
2. **Deferred transcript acquisition** — use source captions when available; otherwise run speech-to-text only after a fetch request or a chat requires the content.
3. **Paid generative chat** — retrieve stored source text and send selected passages to a language model for synthesis or revision.

The recording does not identify Eden's actual code, vendors, cloud provider, database, or transcription model. Treat the technology choices below as a proposed implementation, not a claim about Eden.

## Proposed local-first implementation

### Source adapters

- YouTube: oEmbed or permitted metadata API for the first card; `yt-dlp` for captions and source metadata where lawful and reliable.
- Articles: HTTP fetch plus Readability-style extraction.
- Documents: native text extraction first; OCR only for scanned pages.
- Audio/video: source captions first, then `faster-whisper` as fallback.
- Social posts: official API or permitted browser capture; store the canonical URL and raw response for reproducibility.

### State machine

```text
captured
  -> metadata_pending
  -> metadata_ready
  -> transcript_available | transcript_not_requested
  -> transcript_fetching
  -> transcript_ready | transcript_failed
  -> indexed
```

The item should remain usable at `metadata_ready`; transcript failure must not destroy the card.

### Core records

- `content_items`: canonical URL, source type, external ID, title, author, description, timestamps, status.
- `content_assets`: thumbnails, original files, cached media, MIME type, checksum, storage path.
- `transcripts`: item ID, origin (`source_caption`, `generated`, `manual`), language, text, segments, model/version, generated time.
- `ingest_jobs`: type, status, attempts, error, scheduled time, started time, completed time.
- `search_documents`: normalized searchable text tied to the item and transcript version.
- `chat_sources`: chat ID, item ID, transcript version, selected ranges or retrieval citations.

### Cost controls

- Deduplicate by canonical URL and external source ID.
- Cache metadata and transcripts permanently unless the user refreshes them.
- Never transcribe when usable source captions exist.
- Do not download full media until transcription is requested.
- Use a background queue with retry limits and per-source throttling.
- Start with SQLite FTS5; retrieve small passages rather than sending whole transcripts to chat.
- Track per-job duration, bytes downloaded, transcript minutes, and chat tokens separately.

## MVP acceptance flow

1. Paste a YouTube URL onto a board.
2. See a metadata card without waiting for a transcript.
3. Open the detail view and see `Transcript not fetched`.
4. Request the transcript.
5. Reuse source captions or run local speech-to-text.
6. Persist the transcript so a second request performs no transcription work.
7. Search for an exact phrase through SQLite FTS.
8. Open a Codex task with citations or local paths pointing only to relevant transcript passages.
