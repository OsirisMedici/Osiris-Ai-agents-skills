---
name: life-compass
description: Plan Osiris's future priorities, day or week in the Life Compass calendar, revise upcoming time blocks, or compare the plan with the separate Life Log record.
---

# Life Compass

Turn priorities into a realistic future plan. Life Compass and Life Log are two separate calendars and two separate skills: this skill manages intentions; `$life-log` reconstructs actual activity.

## Open Calendar first

On every invocation, first open or select Google Calendar in the visible in-app Browser, before reviewing tasks or drafting the plan. Reuse an existing Calendar tab when available. Then verify the account, local date and time zone against the routing below. Keep that tab available for the user and final verification. Use the connector for reliable calendar reads and writes after opening the browser.

## Calendar routing

Resolve the connected account and the existing Life Compass and Life Log calendar IDs from the user's authorized private configuration. Keep those account details and IDs outside this public package. Use the user's current time zone, with Asia/Kolkata as the configured default when no other preference applies.

Verify that planning and activity history are separate calendars owned by the intended user. Reuse verified IDs rather than creating replacements. Search with explicit date bounds. Calendar listing can fail for missing connector scopes even while event searches work. If a saved ID is rejected, inspect Calendar settings in the visible in-app Browser and verify the calendar and owner.

## Build the plan

1. Establish the horizon and desired outcomes from the request. With no dates, start with the remaining local day. Read existing Life Compass entries and the user's primary calendar in that bounded range for commitments and conflicts. Consult relevant live tasks when the request identifies a project or workstream; distinguish deadlines from aspirations.
2. Ask through native question input only for missing decisions that materially affect the plan: priority, available hours, hard commitments, energy or rest needs. Use known context first. Do not infer sleep/wake times from computer gaps or fill the day with assumed work.
3. Translate chosen outcomes into concrete blocks whose titles explain what to accomplish. Fit them around commitments, with realistic estimates, breaks, meals, rest and contingency space. Mark uncertain durations. Separate Osiris's attention from unattended agent runtime; an agent running does not by itself establish either human work or leisure.

   When Osiris wants a continuous primary work block and spontaneous secondary tasks during agent waiting time, plan only the primary block. Keep secondary tasks unplanned unless he names a commitment to schedule. Capture what actually happens later through Life Log. A request for both calendars can include an explicitly provisional Life Log placeholder, handled by that skill; keep intentions and verified actuals distinguishable.

4. Present the proposed local times, outcomes and meaningful tradeoffs. When asked only to plan, draft first. When asked to save or schedule a sufficiently specified plan, act within that authorization. Calendar creation alone does not authorize filling it with invented commitments.

## Save and verify

Read and apply the [shared Life calendar colors](~/.codex/instructions/life-calendar-colors.md), including its separate sleep and sales-call categories. The palette is identical to Life Log. Color follows the activity's purpose, not the planned-versus-actual calendar. For an authorized color correction, change only the color of matching existing events and read them back.

Write personal planning blocks only to Life Compass. Use private visibility, Busy availability, no guests, no conferencing, and no notifications unless requested. With the Calendar connector, explicitly use `self_attendance: "omit"` when creating a solo block: its default can add the owner as a guest even with an empty attendee list. Verify guests after creation and remove any automatically inserted owner attendee silently.

Reuse event IDs for revisions. Check current event details before changing boundaries, and reread the affected range after uncertain writes before retrying. Verify titles, local times, privacy, availability, attendees and conflicts. A deliberate planning overlap with Life Log is expected because they represent plan and actual; unintended overlaps within the plan need resolution. Report saved events and remaining uncertainties with a calendar link.

## Compare intention with reality

For a requested review, read both calendars for the same interval and compare intended outcomes, actual activity, interruptions and carryovers. Use Osiris's account of the dominant activity; foreground videos alone cannot establish priority while Codex work runs. Treat a scheduled block as intention, not proof it happened. Route missing actuals to `$life-log` and its review process.

Keep historical plans intact so differences remain visible. Replan future blocks only within the requested scope; do not rewrite the past plan to make it match actuals. Create recurring schedules or automations only when requested.
