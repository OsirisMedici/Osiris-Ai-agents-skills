# Browser execution and recovery

Use the current tool documentation. This is a task workflow, not a browser API specification.

## Choose and hold the correct context

- Discover the available sessions, then select the profile/account the user named. Do not use another logged-in profile simply because its connector is easier to access.
- Prefer a browser binding that targets the intended tab. If only native app control exposes the requested profile, verify its title/profile, address, account and selected object before entering data.
- Native app bindings may follow whichever Chrome window is active. If the user or another activity changes the window, discard stale indices and coordinates, refresh state, and reselect the authorized window/profile through normal UI.
- For a native-control focus failure, make one bounded reselect/refresh attempt. If the same error repeats, ask the user to bring the specific window onto the current desktop and keep it focused for the mutation pass. Explain the exact tool error, preserve completed work, and stop dependent writes until the context is restored. Avoid repeated focus prompts, window-switch loops, or installing a workaround without authorization.
- Never export cookies, tokens, browser storage, or credentials to bridge profiles. Do not use hidden browser endpoints or undocumented remote-debugging access as a workaround.

## Inspect without stale previews

Capture the parent, object number/name and ID where available. After navigation, inspect current state before the next action. Confirm both selection and loaded media; a changed URL with an old heading or old image is an intermediate state.

When media is still loading, use another supported observation to check the missing evidence rather than capturing a placeholder as the final creative. If it remains unavailable, record it as unverified and continue independent work. Do not infer its hook from neighboring ads.

Virtualized tables and sidebars expose only some rows. Scroll the correct region and reacquire its state. If scrolling does not expose the needed object, use a normal search, filter, or parent view and verify that it targets the intended object. A visible total count does not establish that all rows have been inspected. Restore temporary filters when useful and report any remaining view change.

## Prefer a narrow name editor

In the observed workflow, the table's name-column edit control opened a `Name` field with a `Save to draft` action. This avoided scrolling through the full creative editor. Treat those labels as observed examples; confirm what the current UI exposes.

1. Match the exact current name and parent, using the ID to disambiguate where available.
2. Open that row's name editor and confirm its old value.
3. Replace only the name using a documented input method. Read it back before saving.
4. Save using the current UI's appropriate action.
5. Verify the exact resulting row value or reopen the field. For asynchronous saves, use a fresh observation to distinguish saving from saved.

Changing a name must not change selection toggles that control delivery, creative settings, audience, budget, destination, or tracking. Do not dismiss an unresolved modal with Escape unless its effect is known; in the observed UI, Escape could close the whole editor instead of only its menu.

## Keep calls recoverable

Use short, resumable operations. For native controls, one rename per call or a small batch is preferable to a long loop vulnerable to a runtime timeout. Persist the verified mapping and progress in the task's evidence files, not just runtime variables. Reacquire indices after observations or navigation; do not reuse screenshot-only indices without refreshing the accessible state as the tool requires.

If a call times out during a write, do not replay the whole batch. Reinitialize the tool as its documentation requires, inspect the live field/row, and classify that object:

- Old value present: no completed rename is verified.
- Approved value entered but editor still open: check whether a save is still needed.
- Approved value persisted in the row/reopened field: record verified saved and move on.
- Another value or ambiguous object: stop that write and reconcile the mapping.

A screenshot capture failure does not justify renaming the wrong account or expanding permissions. Make a bounded capture retry and state any remaining visual-evidence gap.

## Close the loop

Compare the exact approved names against saved readbacks, including counts, original ad numbers and parent relationships. Revisit or refresh a relevant view to check persistence. Save a few readable before/after screenshots, not a gallery of every click. Note whether changes remain drafts; a review/publish badge can already contain unrelated pending changes and is not a completion receipt.
