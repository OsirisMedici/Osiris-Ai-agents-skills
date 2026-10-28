# Proven Watch Later browser path

Verified in Codex's in-app Browser on 25 October 2026. Use the current browser tool's documented API; T3 preview tools and Codex CUA expose different interfaces. Keep one exact task tab handle.

## Read a snapshot

After inspecting current page structure, this read-only DOM extraction captured the ordered visible rows:

```javascript
let source = await tab.playwright.evaluate(() =>
  [...document.querySelectorAll('ytd-playlist-video-renderer')].map(row => {
    const link = row.querySelector('#video-title');
    const href = link?.getAttribute('href');
    return {
      title: link?.textContent?.trim(),
      videoId: href ? new URL(href, location.origin).searchParams.get('v') : null
    };
  })
);
```

Scroll to load more if necessary. Extract again and reconcile by video ID. The initial page rendered 100 rows for 105 entries; a later 49-entry view rendered 48 and explicitly hid one private video. A row count alone does not establish completeness.

## Remove a known target

For a unique title previously observed on the page:

```javascript
const row = tab.playwright.locator('ytd-playlist-video-renderer')
  .filter({has: tab.playwright.getByRole('link', {
    name: target.title, exact: true
  })});
await row.getByRole('button', {name: 'Action menu', exact: true}).click();
let state = await tab.playwright.domSnapshot();
if (!state.includes('menuitem "Remove from Watch Later"')) {
  throw Error('Expected removal menu is not visible');
}
await tab.playwright.getByRole('menuitem', {
  name: 'Remove from Watch Later', exact: true
}).first().click();
let remaining = await tab.playwright.getByRole('link', {
  name: target.title, exact: true
}).count();
```

The menu snapshot contained nested menuitems with identical names; `.first()` selected the outer removal item. Recheck current markup. If titles repeat, use the observed video link ID to scope the row unambiguously.

Batching several such serial sequences in one tool call was fast. Native scrolling brought offscreen targets into view after the first locator click produced no menu. The same visible row position then received the next video as each target disappeared. Continue using frozen identities rather than relying on that position.

## Saved-state verification

One regular video reappeared during reconciliation. A private video's first reload still showed a stale 13-entry total even though the next **Show unavailable videos** navigation contained only the intended 12. A subsequent reload showed exactly 12 with no hidden-entry notice. Treat this as evidence of delayed updates, not a reason to repeatedly delete an absent target.

Reconcile current visible IDs, hidden entries, and the header. Retry only targets that actually reappear. In the completed run, all 37 removals were verified and the original first 12 video IDs remained in order after reload. This outcome is evidence for the procedure, not a future keep-count setting or a guaranteed speed estimate.
