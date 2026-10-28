---
name: youtube-cleaner
description: Clean up Osiris's YouTube Watch Later, keep a chosen set, or organize its videos into existing topic playlists. Read Watch Later in the in-app Browser and use the YouTube MCP for ordinary playlists. Use for YouTube cleaner, Watch Later cleanup, or sorting saved videos, including dictated "wash later" and "washletter".
---

# YouTube cleaner

Make Watch Later a useful inbox and preserve videos in the user's chosen topic playlists. Osiris already has a playlist structure and a connected YouTube MCP. Reuse both rather than asking him to explain this setup again.

## Choose the requested operation

- **Inspect or estimate:** read the current count and controls without changing membership. Base time estimates on the actual operation and current tool performance.
- **Organize or copy:** save videos to suitable ordinary playlists; keep their Watch Later membership unless removal is authorized.
- **Move:** save to the destination, verify exact video IDs there, then remove only those verified videos from Watch Later.
- **Trim or clear:** preserve the specifically requested set and remove the authorized remainder. A keep count applies to the currently displayed order at inspection time. Freeze the keep set by video ID before removing anything.

The request determines the keep count, destination choices, and whether removal is included. The 12-video cutoff used on 25 October 2026 was a one-time choice, not a future default. If a spoken correction gives two possible cutoffs, show the boundary titles and resolve it before removal. Honor authorization already given; ask only for missing decisions or confirmation required by the active tool policy. Invoking the skill alone is not blanket authorization to delete videos, create public playlists, or reorganize unrelated playlists.

## Inspect the account and source

1. Discover the current YouTube MCP tools with a focused catalog search. Use `list_channels` to verify the connector account. Expected historical identity is **Osiris Medici**, handle **@OsirisMedici**; match the current browser identity before combining Browser reads with MCP writes.
2. Use the **in-app Browser** for browser work. Preserve existing user tabs and playback. Read and apply `~/.config/osiris-agent-rules/t3-browser-profiles.md` when using T3; select persistent Default explicitly where that API supports profiles. In the Codex Browser, reuse the verified signed-in session. Personal Chrome is outside this workflow.
3. Open or reuse `https://www.youtube.com/playlist?list=WL`. Verify the signed-in channel, displayed sort order, count, and unavailable-video notice. An authentication wall or an empty MCP response is not evidence of an empty Watch Later.
4. Read rendered playlist rows, retaining ordered video IDs, titles, channel names when needed, and availability. Load further rows through normal scrolling until the targeted scope is covered. Track hidden entries separately. The header total can exceed visible rows.

Read [references/browser-fastpath.md](references/browser-fastpath.md) for the proven UI selectors, fast removal loop, and persistence checks. Refresh locators from current page evidence before using the examples.

## Organize through the YouTube MCP

1. Call `list_playlists` and follow pagination. Inspect the live titles and descriptions to reuse Osiris's existing structure. [references/playlist-context.md](references/playlist-context.md) provides discovery hints from the verified account, not a substitute for the current listing.
2. Fetch missing video metadata in batches with `list_videos` when titles alone do not establish a topic. Use existing video IDs rather than expensive search calls.
3. Match each video to the requested destination or the best existing topic playlist. Show uncertain assignments or proposed new categories for a decision if they materially affect the result. Do not ask about clear assignments when the user has authorized sorting into the existing structure.
4. Read each selected destination with `get_playlist`, following pagination, and deduplicate by video ID. Call `add_to_playlist` only for missing IDs. A timeout or partial batch response requires a membership read before retrying.
5. Verify every requested video ID in its destination. Additions and removals are separate operations; a successful MCP addition does not remove Watch Later membership. For a move, leave any failed, unavailable, or unverified video in Watch Later and report it. Remove an unavailable entry only when its removal is authorized separately or explicitly included in the cleanup scope.
6. Create a new playlist only when needed and authorized. Use private visibility unless the user requests otherwise; preserve existing playlists' visibility.

The connected tool schemas are authoritative. On 25 October 2026 the connector exposed channel, playlist, and video reads, playlist creation, and additions, but no deletion tool. Discover capabilities again on a future run. Keep mutations sequential and respect quota or provider errors. Stop writes on quota exhaustion; retain unverified source entries.

## Remove from Watch Later and verify

1. Establish the exact removal set from the frozen snapshot, excluding the keep set and, for moves, every video not verified at its destination. When confirmation is required by the active UI policy, present this concrete set or count and the boundary titles immediately before removal.
2. Use each target row's **Action menu → Remove from Watch Later** through the supported Browser UI. Identify targets by video ID or a unique exact title, not a row number that shifts after removal. Check the menu before clicking the removal command and check that the target disappears afterward.
3. Batch short sequences of UI operations to reduce round trips. Keep each open-menu, inspect-menu, remove, and verify sequence serial. If an offscreen click does nothing, scroll the target into view and inspect before retrying.
4. For authorized hidden-entry cleanup, use the playlist-level **Action menu → Show unavailable videos**, then inspect and remove the identified rows. A private entry may have an unnamed menu button. Showing these rows can shift positions; the frozen keep IDs remain authoritative.
5. Reconcile the saved result after navigation or reload. Immediate disappearance and a toast can precede persistence. Compare the actual retained IDs and order with the keep set, inspect unavailable rows, and reconcile the header count. If an authorized target reappears, inspect current membership and retry once, then reload and verify. Report unresolved entries rather than looping.

Finish only when the retained IDs match the intended set and destination membership is verified for moved videos, or when a specific blocker is reported. Capture and embed a screenshot of the verified Browser result when required by the active browser instructions. Leave a requested user-facing Watch Later tab open with the current tab lifecycle API; close unused task-created tabs and preserve unrelated tabs. Report counts kept, copied or moved, removed, already present, and unresolved as applicable. End the final response with `over and out`.

## Watch Later API limitation

Checked 25 October 2026: Google's [playlistItems.list documentation](https://developers.google.com/youtube/data/reference/rest/v3/playlistItems/list#errors) explicitly lists `watchLaterNotAccessible`. This session's `get_playlist` call for `WL` returned an empty array while the Browser showed 105 entries. Do not repeat that probe or interpret it as an empty source.

The supported workflow is Browser discovery and removal for Watch Later, paired with MCP additions and verification for ordinary playlists. Use supported Browser actions rather than private endpoints, copied session material, or injected mutation scripts. If the user asks whether API access has changed, or the connector advertises a new Watch Later capability, check the current official documentation and actual account behavior. Explain any newly verified option. Do not promise background monitoring unless separately requested.
