---
name: eden-ingestion-pattern
description: Design or implement a low-cost content vault inspired by the demonstrated Eden ingestion workflow. Use when Codex needs to plan, build, review, or explain URL ingestion for YouTube videos, social posts, articles, documents, metadata cards, deferred transcripts, searchable local storage, or chat grounded in saved sources.
---

# Eden Ingestion Pattern

Build from observed product behavior without claiming access to Eden's private backend.

## Workflow

1. Read [references/recording-2026-07-13.md](references/recording-2026-07-13.md).
2. Separate direct recording evidence from architectural inference.
3. Inspect the target repository before proposing new infrastructure.
4. Preserve any working storage, database, upload, or search spine already present.
5. Default to a staged pipeline:
   - capture the source URL or file;
   - fetch cheap metadata immediately;
   - render a usable card;
   - fetch or generate a transcript only on demand;
   - persist normalized text once;
   - retrieve only relevant passages for chat.
6. Prefer source-native text and captions before speech-to-text.
7. Prefer SQLite FTS5 for a local MVP; add embeddings only when semantic retrieval is demonstrably necessary.
8. Treat platform APIs, robots rules, rate limits, and terms of service as implementation constraints.
9. Verify the full user flow: paste, card creation, detail view, transcript request, transcript persistence, search, and grounded chat.

## Required distinctions

- Label visible UI behavior as observed.
- Label backend choices as inferred or proposed.
- Do not describe metadata extraction as transcription.
- Do not assume every saved video has a transcript.
- Do not promise unlimited or free chat: ingestion can be cheap while model usage still consumes tokens.

## Deliverable defaults

For architecture requests, provide the state machine, data model, worker boundaries, cost controls, and an incremental build order. For implementation requests, create the smallest end-to-end vertical slice in the existing repository and leave a manual test path.
