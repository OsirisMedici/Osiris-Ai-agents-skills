---
name: go-highlevel-operator
description: Operate GoHighLevel/GHL for Osiris when tasks involve workflows, automations, Facebook lead forms, contacts, WhatsApp messages, email actions, Slack alerts, execution logs, enrollment history, or delivery debugging. Use for live authenticated GHL browser work, especially when diagnosing why messages did not send, duplicating/editing workflows, testing a contact through a workflow, or making GHL streams cleaner and faster.
---

# GoHighLevel Operator

## Quick Start

- Use Chrome/logged-in browser for authenticated GHL work.
- Reuse the user's existing GHL tab when available.
- Name the browser session by client/task.
- Confirm the exact client/location before editing.
- Prefer visible browser verification over assumptions.
- Do not touch Meta Ads when the user says ads/forms are fine.
- For private Slack alerts, use private Slack channels by default.

## Core URLs

- Workflow builder: `https://app.gohighlevel.com/location/{locationId}/workflow/{workflowId}`
- Contacts list: `https://app.gohighlevel.com/v2/location/{locationId}/contacts/smart_list/All`
- Contact detail: `https://app.gohighlevel.com/v2/location/{locationId}/contacts/detail/{contactId}`
- Automation section: `https://app.gohighlevel.com/v2/location/{locationId}/automation/workflows`

Use `/v2/location/...` for contacts. The older `/location/.../contacts/...` route can load blank.

## Workflow Debugging Flow

1. Identify the active workflow and old duplicate workflows.
2. Check trigger, current status, Draft/Publish toggle, and Save state.
3. Check `Execution Logs` first for truth.
4. Open `View Details` on failed or important rows.
5. Distinguish action execution from final delivery.
6. Open the contact conversation when delivery outcome matters.
7. If changing a live workflow, duplicate first when the blast radius is unclear.
8. Turn off the old workflow after the cleaned duplicate is published.
9. Run `Test Workflow` with a known contact.
10. Save the result in the client's stream map or handoff file.

## WhatsApp Rules

- Leads entering GHL correctly means the Facebook lead sync is probably not the issue.
- Error text like `healthy ecosystem engagement` points to Meta/WhatsApp delivery enforcement, template pressure, or opt-in/conversation-window constraints.
- Avoid back-to-back Marketing templates.
- Keep one immediate WhatsApp only.
- Prefer an offer-specific Utility or service-style template when possible.
- Use click-to-chat on the thank-you screen so the lead can message first.
- The thank-you CTA number does not need to match the automation sender number if both are monitored.
- Add an Undelivered branch with a private Slack alert and manual call/WhatsApp instruction.

## Email And Slack

- Email is backup/proof, not the primary India conversion channel.
- Fill From Name and From Email instead of leaving defaults.
- Improve message spacing inside GHL editors; cramped copy reads broken.
- A workflow email action can show `Executed` while the contact conversation shows final email delivery `Failed`.
- Invalid mailbox failures are contact-data quality issues, not workflow build failures.
- New lead Slack and WhatsApp failure Slack should route to the client/offer private channel.

## Browser Lessons

- GHL workflow builder often sits inside an iframe.
- If DOM/Playwright selectors fail with cross-origin or iframe errors, use screenshots and coordinate clicks.
- `Execution Logs` table columns usually show Contact, Action, Status, Executed On, and `View Details`.
- `View Details` reveals Event Status, Branches Executed, Action Executed From, Message, and timestamp.
- For `Test Workflow`, use the right-side panel, open `Select Contact`, search, select contact, then `Run Test`.
- Contact selector search can require the full formatted phone, using the exact country-coded phone from the authorized task.
- Contact list search can behave differently for `+91...`, plain digits, and partial digits.
- Duplicate-contact toasts may reveal an existing hidden contact even when a partial search shows none.
- Contact detail view has fields on the left, conversation/messages in the center, and activity on the right.

## Tooling Caution

- GHL MCP contact tools may use a configured default location that is not the browser's current client.
- Treat browser location ID as source of truth for location-specific contact/workflow operations.
- Use MCP tools for quick read/search only after confirming they are pointed at the right location.
- For live production sends, prefer browser-visible verification unless the tool contract clearly includes the correct location.

## Client context

Read the configured sub-account's non-secret registry and current campaign stream map before account-specific work. Resolve live location, workflow, channel and template IDs there; historical test results are not current delivery proof. Keep customer contact details and campaign mappings in that authorized client workspace.
