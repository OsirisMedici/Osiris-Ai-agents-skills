---
name: watchlist
description: Manage Osiris's movie and series watchlists in the local master and Cinejoy, or find and verify playback for a requested title or episode.
---

# Watchlist

Resolve the user's existing Markdown master watchlist from authorized private configuration or their selected workspace, and use that exact file as the source of truth. Keep list contents and private export files outside this package. Cinejoy My Lists is Osiris's private browsing UI. Playback can move between platforms without moving the lists.

- `$watchlist make "List name" from <YouTube link or titles>` saves the master and adds the requested entries to the matching Cinejoy list. Read [make a list](references/make.md).
- `$watchlist find <series or movie> [season/episode] [sub/dub]` finds and checks a playable alternative. Read [find playback](references/find.md).

Accept natural-language equivalents, including "I want to watch [title]" for `find`. In `make`, use a relevant source already supplied in the chat when available. In `find`, use the current matching watch page to recover the episode when available. Ask only when a material ambiguity remains.
