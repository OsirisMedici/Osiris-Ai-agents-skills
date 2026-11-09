---
name: life-log
description: Build or backfill a personal Google Calendar Life Log from Computer History and the user's recollections. Use for daily review, historical activity blocks, sleep corrections, or Life Log colors.
---

# Life Log

Keep a private, glanceable record of how the user actually spent their time. Give work, entertainment, browsing, errands, meals, and rest the same factual treatment.

## Resolve the date and calendar

1. Use the user's timezone to interpret dates and midnight boundaries. For a scheduled review, use the previous completed local day. For a backfill, resolve the inclusive dates from the request. Check existing events across that range before proposing additions.
2. Use the Google Calendar connector to find the intended account and the separate calendar named Life Log. If calendar listing lacks scope, verify the account and calendar ID in Google Calendar settings in the in-app Browser. Use that ID for connector event actions. Create a calendar only when requested and verify it is private and unshared. Use a custom pale blue calendar color (#C5D9F6) where the UI supports it.

## Reconstruct the timeline

1. Use the Computer History skill. Check the recorder status and compare the source timestamps with the local date. Start with six-hour summaries for orientation, then use ten-minute summaries and available raw events to place boundaries and resolve video titles. Broad summary timestamps mark windows, so use finer evidence to place individual activities. In older ranges, check which dates have only summaries and report that limitation.
2. Make separate timed blocks of 30 minutes to two hours. Group close activity with a useful common title and keep meaningful gaps open. When an activity lasts longer than two hours, use adjacent blocks. Use local times and identify estimates. A title should tell the user what they were doing from the week grid without opening an event. Include recognizable video names when playback is supported. Distinguish watching from browsing or opening a tab. Name both activities when the record shows meaningful switching.
3. Put the user's recollection ahead of conflicting computer evidence. Use user-provided meal and sleep times or ask for a time anchor. If the user explicitly requests estimates, use their timing and duration guidance, fit them around observed activity, and mark the titles estimated. A gap on the Mac does not establish sleep or other offline activity by itself. Keep sensitive source material local and record only the activity summary.

## Save and verify

1. For a recurring review, show a draft in the originating chat and collect the user's corrections or offline context before saving. Use the existing automation if available. Create or change a schedule only when requested. For a directly authorized backfill, proceed within its date range. For a correction, update the affected existing events and reconcile any overlaps before adding replacements.
2. Write only to Life Log. Make events private and Free, with no guests, conferencing, notifications, or description. Match existing records by calendar, time, and title to avoid duplicates. After an uncertain write, reread that interval before retrying.
3. Apply the palette by dominant activity. Use the user's own judgment about a break or time sink when provided.

   | Activity | Calendar color |
   | --- | --- |
   | Client and agency work | Sage, event color ID 2 |
   | Passive watching or browsing | Flamingo, event color ID 4 |
   | Sleep, restorative breaks, or meals | Wisteria, muted lavender |
   | Internal projects, errands, or unclear mixes | Inherit the pale blue calendar color |

   The connector supports the standard event color IDs. For Wisteria on the secondary calendar, use the in-app Browser. Right-click the verified Life Log event, select Wisteria, and read back the resulting event color. Use the displayed calendar, date, title, and time to identify the event. If that swatch is unavailable, leave the event pale blue and report the color limitation.

4. Read back the target range. Verify titles, local boundaries, colors, and absence of unintended duplicates or overlaps. Report the dates covered, the saved result, and any material gaps or estimates. Link the relevant calendar view.
