# Naming and approval

## Choose the fields that support decisions

Keep each dimension at a useful level. Do not fill every name with every available fact.

| Level | Useful dimensions | Example |
|---|---|---|
| Campaign | Client, offer/programme, objective, meaningful cohort | `ExampleCo | Programme L1 | Website Leads | Nov2026` |
| Ad set | The audience or visual family actually distinguishing that set | `Programme | V1 | Green` |
| Ad | Existing ad number, meaningful hook/angle | `Ad 1 - Workflow Integration` |

These are configurable examples, not required campaign facts. Include geography, funnel stage, language, placement, or conversion location only when verified and useful. Do not label an audience as cold, retargeting, broad, or India-wide without evidence. If an ad set contains multiple visual families, do not name the whole set after a single preview.

For the colour/version scheme used in a visual test:

- Use a stable, explicit mapping such as `Programme | V1 | Green`, `Programme | V2 | Red`, `Programme | V3 | Blue`, `Programme | V4 | Lime Green`.
- Preserve the user's exact separator, spelling, capitalization, and version decisions once approved.
- A visual version such as `V1` is different from a programme's level or product release. Do not conflate them.
- Preserve `Ad 1` through `Ad 20` when those are the existing identifiers. Do not reset numbering within each set unless requested.
- Reuse the same hook label for the same message across visual families. Use a version suffix for multiple instances only if needed and approved; retain the ad number even then.
- Use a presenter name only when known and appropriate; otherwise describe the visual neutrally. Avoid informal honorifics, audience judgments, and performance claims such as “cheap leads,” “bad audience,” “winner,” or “loser” in client-visible labels.

## Build the approval mapping

Show current parent and name, proposed parent/name, and any material mismatch. An optional task-local CSV has these fields:

| Field | Meaning |
|---|---|
| `entity_type` | `campaign`, `adset`, or `ad` |
| `entity_id` | Actual Meta ID read from the authorized surface |
| `parent_id` | Campaign ID for ad sets; ad set ID for ads |
| `current_name`, `proposed_name` | Exact strings, not approximate labels |
| `observed_hook` | Stable descriptive key for the actual inspected creative |
| `proposed_hook` | The key represented by the proposed label |
| `approval_ref` | Reference to the user's approval of this exact mapping |
| `exception_approved`, `exception_note` | Explicit user-approved exception and its reason |

Keep hook keys consistent; for example `workflow-integration`, `tutorial-to-project`, `model-assumptions`, `modelling-rationale`, and `reason-behind-each-step`. Do not require these particular hooks for other clients. Leave both hook fields empty for a purely administrative rename that makes no hook claim. If IDs are unavailable, use a separate readable approval table rather than inventing IDs to satisfy the CSV validator.

An exception note does not itself prove authorization. Record what the user actually confirmed. A user may deliberately approve intended sequence labels while leaving a known image mismatch unresolved; apply only that approved naming decision and disclose the remaining creative issue. Do not interpret it as approval to change the image.

## Attribution continuity

Inspect existing tracking configuration when attribution is part of the request. Report name-based dependencies that could affect this rename, without silently editing UTMs or CRM workflows. Keep Meta IDs alongside readable names as stable keys. Names alone are a weak automation contract because people can rename them; do not promise that historical URLs, existing leads, or GHL records will be updated by a Meta rename.
