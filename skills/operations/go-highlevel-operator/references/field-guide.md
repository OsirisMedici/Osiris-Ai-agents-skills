# GoHighLevel Field Guide

## Workflow Builder

- Top tabs: `Builder`, `Settings`, `Enrollment History`, `Execution Logs`.
- Top right: `Test Workflow`, Draft/Publish toggle, Save state.
- Use `Execution Logs` for objective action status.
- Use `Enrollment History` for who entered and where they are in the workflow.
- Use contact conversation details for final email/WhatsApp delivery reality.

## Safe Workflow Change Pattern

- Duplicate before editing when the current workflow is live or messy.
- Remove redundant waits and duplicate sends before adding more actions.
- Keep original workflow off after publishing the cleaned duplicate.
- Make one change, save, then verify.
- Do not leave both original and duplicate active unless double-enrollment is intentional.

## WhatsApp Debug Checklist

- Did the lead enter the workflow?
- Did the WhatsApp action execute?
- Which branch executed: Delivered or Undelivered?
- Does `View Details` show Success or failure?
- Does the contact conversation show the message bubble?
- Did the lead message first in the last 24 hours?
- Is the template Marketing, Utility, or service-style?
- Are multiple outbound templates firing back-to-back?
- Is the phone valid and formatted with country code?

## Email Debug Checklist

- Did the email action execute in workflow logs?
- Does the contact have a valid email?
- Does the conversation show Delivered, Failed, Opened, or another final status?
- If failed, is it mailbox invalid, sender/domain issue, or workflow config?
- Sender fields to fill: From Name, From Email, Subject.

## Slack Alert Checklist

- Prefer private channel actions.
- Name channels by client and offer.
- Include campaign, workflow, lead name, phone, email, city/state if available.
- Failure alert should state the manual action: WhatsApp or call now.

## Contact Search Tips

- Use full phone with country code first: `+91...`.
- Try plain digits if full format fails.
- Try name/email if phone search behaves strangely.
- In contacts list, full `+91` can find a contact while partial digits show zero.
- A duplicate-contact toast means the phone exists even if current search looked empty.

## Contact Detail Anatomy

- Left column: contact fields, tags, owner, DND, actions.
- Center: conversation and sent messages.
- Right column: activity timeline.
- Bottom/center composer can reveal WhatsApp availability and 24-hour-window warnings.

## Common GHL Truth Split

- `Executed` in workflow log means GHL ran the action.
- `Success` in event details means the action call succeeded.
- `Delivered` branch means GHL/WhatsApp classified the branch as delivered.
- A later contact-message status can still show delivery nuance.
- Email action executed does not prove inbox delivery.
