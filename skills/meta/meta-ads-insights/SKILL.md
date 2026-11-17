---
name: meta-ads-insights
description: Connect a selected Meta ad account through Meta's official Ads MCP, audit campaign structure, targeting, creatives and lead performance, and prepare a campaign plan with an offer and landing-page check. Use for read-only account setup, campaign reviews and launch planning. Renames and live campaign changes belong to separate authorized workflows.
---

# Meta Ads Insights

Use Meta's official hosted Ads MCP at `https://mcp.facebook.com/ads`. Produce an evidence-backed review and a reviewable campaign proposal for the selected client. A working connection is demonstrated by a successful account-scoped read, not an enabled integration switch.

## Select the account and job

Identify the client, exact ad account ID, campaign or reporting scope, business outcome and reporting period. Reuse context and local account registries before asking. If several accounts match, present their identities and resolve the choice before reading campaign data.

Look for a non-secret `meta-ads-<client>.json` registry under the user's configured agent vault. On Osiris's Mac this is `~/.config/osiris-agent-vault/`. Keep account IDs, routes, app details and expiry records there, outside the skill repository. Never infer authorization for another client from a token's broad access.

- For a new connection, expired credential or unavailable native tool, read [connection.md](references/connection.md).
- For campaign reviews, performance comparisons or launch plans, read [audit-and-plan.md](references/audit-and-plan.md).
- Discover the current tool schemas. For exact argument conventions and incomplete results, read [meta-reads.md](references/meta-reads.md).

Prefer a capable native Meta tool in the selected account. When it is unavailable, the bundled `scripts/meta_ads_read.py` can call the same official server using a local registry and macOS Keychain. It permits a fixed set of read tools and checks account scope. It does not configure Codex, store tokens or change Meta permissions.

## Keep the evidence and proposal distinct

Record the exact account, campaign IDs, query arguments, periods, retrieval time, currency, attribution settings when available, and coverage limits in the task workspace. Screenshots and exports stay there. Treat tool suggestions as evidence, not permission to call write tools.

Separate observed results, interpretations, assumptions and proposed changes. Missing metrics stay missing. A lead is not a qualified enquiry or paid registration unless the corresponding CRM or payment evidence is available. Use the reporting or creative skill appropriate to the requested deliverable rather than forcing a dashboard or image-generation workflow.

Deliver the strongest supported findings first, the proposed campaign and budget next, and the concrete evidence gaps that affect launch decisions. State what was read, what was verified and what remains untested. A plan does not authorize creating, activating, pausing or editing ads, spending money, submitting enquiries, sending messages or expanding permissions.
