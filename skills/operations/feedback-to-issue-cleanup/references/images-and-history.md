# Preserving proof and removing duplicates

## Image decisions

For each candidate, note its source comment/body, permanent URL, observed date/state, what it proves, safety/relevance, and retention decision. Use local hashes when identical bytes are available; visual review is still needed for different files showing the same state. Keep all useful distinct images. Osiris explicitly corrected the earlier highlight-gallery interpretation: no three-image limit, no one-to-four guideline, and no smallest-set objective. Do not download unrelated evidence or expose signed private-image URLs in output.

An image is useful if it documents any of these:

1. A result, setup step, configured setting, or created object.
2. A distinct saved state, audit, test, or verification.
3. A meaningful historical step, correction, failure, or before/after change.

Remove repeated occurrences of the same URL or identical bytes. Different captures count as duplicates only when they show the same work/state and add no meaningful detail; retain the clearer complete capture. Different configuration steps are not duplicates merely because their screens look similar. Keep both when uncertain. Preserve originals and reuse permanent GitHub URLs. Existing `issue-work-log` upload receipts can match hashes/URLs. Routine cleanup needs no new uploads.

Do not retain sensitive screenshots in the visible gallery. Use a verified safe existing alternative, clean recapture, or omit the image and state the evidence gap. Redaction requires an appropriate supported image tool and visual verification; fabricated or generatively altered proof cannot establish the original state. Do not copy secrets into a collapsed archive or rollback text.

When images cannot be inspected, clean the text and remove only mechanically established repeated embeds. Preserve unique embeds and describe the incomplete visual review. Do not downgrade an uninspected image to a hidden link or claim visual deduplication.

## Example of a compact current brief

This is a shape, not a required template:

```markdown
{The user's concrete problem and intended outcome in two or three sentences.}

## Where this stands

{Useful current result, what was actually verified, and the remaining limit.}

## What remains

- [ ] {Existing requirement with its original completion state and clear condition.}
- [ ] {Next dependency or acceptance step.}

## Proof

{Caption explaining the distinct result and its limit.}

![{Descriptive alt text}]({existing permanent attachment URL})

[{Relevant test receipt}]({existing permanent file URL})

<details>
<summary>Implementation notes and earlier decisions</summary>

{Only useful continuation details and history, with source permalinks.}

</details>

{Preserved Feedback source link and exact task UUID marker, when present.}
```

## Example of compacting an agent work-log comment

Keep the same comment ID and truthful attribution. Link the issue itself for the current brief; use a section fragment only after confirming the heading/anchor exists.

```markdown
> [!NOTE]
> 🤖 **{verified model/harness} responding on behalf of {verified user}**

{Original date}: {Unique result of this update, with its actual verification level.}
See the [current issue brief]({issue URL}) for status and selected proof.

<details>
<summary>Earlier work and evidence</summary>

{Unique historical facts, decisions, corrections, and unresolved limits.}
[{Historical image caption}]({original permanent image URL})
[{Original receipt label}]({original permanent file URL})

</details>
```

Do not put the repetitive log back into the visible summary or embed an image twice. The historical-image link in this example assumes that image is also visible in the main gallery or is an established duplicate. Otherwise retain its original image embed. Preserve all meaningful distinct proof, concise historical facts, and recovery text. Keep unknown/human authors' comments intact and explain that limitation in the handoff.
