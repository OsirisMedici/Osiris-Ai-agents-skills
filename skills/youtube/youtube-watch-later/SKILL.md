---
name: youtube-watch-later
description: Add requested YouTube videos or recommendations from the current chat to Osiris's Watch Later playlist using T3's saved browser profile. Verify each saved video and close unused task-created tabs afterward. Use for Watch Later saves, including batches; recommendations alone do not authorize saving.
---

# YouTube Watch Later

Save the requested videos to the signed-in account at https://www.youtube.com/playlist?list=WL. Finish after every requested video ID is confirmed in the playlist, or report the exact unsaved subset and blocker.

## Start with the existing session

1. Resolve videos from the current chat or supplied URLs. Deduplicate by video ID. Track requested, newly saved, already-present, and unresolved IDs. Reuse verified recommendations instead of researching them again.
2. Call `preview_status` first and record initial tab IDs. Discover current tool declarations from the live catalog when needed; MCP prefixes can vary.
3. Use T3's in-app `preview_*` tools. Osiris's personal Chrome is outside this workflow. He imported his main Chrome sessions into **Default**; **scale Chrome** is a separate work profile. These choices were confirmed on 2026-10-20. Use Default unless the current request specifies Scale or another account. Resolve profile IDs from current status and preserve the user's default.
4. Prefer one new task tab: `preview_open({url: 'https://www.youtube.com/playlist?list=WL', profileId: '<current Default ID>', reuseExistingTab: false, open: false, show: false})`. Store its returned tab ID and pass it on every later call. Background mode avoids disrupting the user's native T3 window and other agents. Preserve existing user videos and their playback positions.
5. Confirm the signed-in account and inspect the playlist before saving. If identity is unclear, inspect the account menu. An auth wall differs from an empty playlist. Use normal authorized sign-in if available; otherwise explain the specific human step. Keep cookies and credentials inside the browser profile; the skill stores neither.

`available: true` with `visible: false` can still support working preview calls. Test the relevant call rather than treating visibility alone as a blocker. If T3 is downloading its browser, inspect progress and retry once when ready. Follow current runtime instructions for other errors; report a remaining connection failure instead of switching to personal Chrome.

## Save each missing video

Use the same task tab sequentially; navigations, saves, and verification depend on one another.

1. Navigate to `https://www.youtube.com/watch?v=<ID>` and confirm the video. Pause playback in your own tab if it starts automatically.
2. Click the observed **Save to playlist** button. The verified locator on 2026-10-20 was `role=button[name="Save to playlist"]`. If Save moved into an overflow menu, inspect the current page to find it.
3. Wait for the playlist picker. The Watch Later row was a **menuitem**, not a checkbox. Read its `aria-label` and `aria-pressed` before acting:
   - `Watch later, Private, Not selected`, `aria-pressed="false"`: click once to save.
   - A selected row with `aria-pressed="true"`: it is already saved; leave it selected.
4. Expect **Saved to Watch later**. The picker can close immediately and leave a stale hidden row that still says `false`. That stale value does not justify clicking again. Read the result, then verify in the playlist.

Once these elements are observed, focused DOM reads through `preview_evaluate` avoid repeated full-page snapshots:

```javascript
[...document.querySelectorAll('button[role=menuitem]')]
  .filter(e => e.getAttribute('aria-label')?.startsWith('Watch later'))
  .map(e => ({
    label: e.getAttribute('aria-label'),
    pressed: e.getAttribute('aria-pressed')
  }))
```

Use `preview_wait_for` on the observed row when the picker is still loading. Refresh locators if markup changes. Limit output to the relevant row and save result.

## Verify the saved playlist

Navigate back to `https://www.youtube.com/playlist?list=WL`. Compare exact video IDs against rendered playlist links, not the total count or toast alone:

```javascript
[...document.querySelectorAll('ytd-playlist-video-renderer')].map(e => {
  const link = e.querySelector('#video-title');
  const href = link?.getAttribute('href');
  return {
    id: href ? new URL(href, location.origin).searchParams.get('v') : null,
    title: link?.textContent?.trim()
  };
})
```

The final save can take a moment to appear. A fresh navigation resolved this in the verified run. If IDs remain missing, inspect the playlist's sort order and load more rows as needed, then recheck only those videos. Keep retries bounded and inspect current membership before another save. A cached count or hidden unavailable item does not prove membership.

## Clean up and hand back

Osiris explicitly requested on 2026-10-20 that agents close their unused task tabs after finishing. After verification:

- Close tabs created for this task with `t3_preview_close`. Keep any tab the user asks to retain, and preserve pre-existing user tabs and other threads' tabs.
- Reread `preview_status` or `t3_preview_list` to confirm the task tabs are gone. Do not call `preview_open` merely because cleanup leaves no active tab.
- If another thread explicitly requested shared-UI coordination, send one completion/free notice to that exact thread. This is conditional coordination, not background monitoring.
- Report the verified result briefly, with the Watch Later link and any unsaved items. Follow the current completion-signal rule.

## T3 settings only when relevant

For chat links opening externally, use native T3 settings: **Settings → Integrations → Open links in → T3 Code**. Verify it remains selected after leaving and reopening Integrations. This was saved on 2026-10-20; a Watch Later task normally needs no setting changes.

Chrome session import is **Settings → Integrations → Browser profiles → Add profile → Import from → Chrome**. It copies cookies once; some sites still need sign-in and sessions can expire. Reuse existing profiles instead of reimporting for each chat. Consult https://github.com/pingdotgg/t3code/blob/main/docs/user/browser-import.md if import is actually requested.
