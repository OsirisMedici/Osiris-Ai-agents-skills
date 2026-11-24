---
name: vault-research
description: "Research a topic across selected sources and save a cited reference document in a knowledge vault."
---

# Vault research

Research a topic for a stated purpose and leave an inspectable reference document.
This is the custom Claude vault workflow, published under `vault-research` to
avoid replacing an unrelated installed engineering skill named `research`.

## Scope the question

Recover the topic, intended decision or use, freshness, depth, platforms,
exclusions and output destination from the request. Ask only for unresolved
choices that materially change the result, batching them through the host's
native question tool. A clear request can proceed without a second plan approval.
Explain the search approach briefly and continue useful independent work.

## Investigate

Use supported search tools, APIs and connected sources. Prefer primary sources
for technical and factual claims. Use communities for reported experience and
label those observations. Verify dates and source ownership. Collect title,
author, URL, publication or observation date, key contribution and relevance.
Read the source before summarizing it; mark inaccessible pages and missing
transcripts instead of claiming their full contents were reviewed.

Cover the selected sources, such as YouTube, Reddit, X, official documentation,
blogs, newsletters, podcasts, papers or GitHub. Deduplicate repeated results and
separate current evidence from older background. Do not use fixed URL filter
codes as proof of date coverage. Respect source quotation and reuse limits.

## Save and deliver

Use the requested vault destination or an existing research folder. Create a
dated note stating the question, purpose, scope and actual coverage. Group the
source table by platform with a short summary and relevance for each. Recommend
a starting source when useful, synthesize recurring themes and contradictions,
and state gaps. Link each consequential conclusion to its supporting source.

Preserve the existing vault's style. Use the optional `obsidian-mind` skill only
within the authorized output folder when that formatting is wanted. It must
preserve source text and unrelated notes. Return the saved file and main finding.

Create or modify a playlist only when the user requests that output. Verify the
target account and playlist, use purpose-built tools where available, and inspect
saved membership. For browser work, use the visible in-app Browser. Research
alone does not authorize playlist changes, external posts or messages.
