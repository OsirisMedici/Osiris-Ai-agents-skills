---
name: ads-to-calls
description: Build an ads-to-calls system map for a Scale client. Use when a client is running multiple campaigns and needs a structured document that maps every campaign to a person, calling hours, and script — with blank fields for the client to fill in. Trigger when Osiris says things like "ads to calls", "who's calling leads", "ads report", "sales coverage", "build a system map", "campaigns and who calls", "create a calling system", or when a client has multiple campaigns running without a clear assignment of who handles what leads. This is the document that bridges ad spend and lead conversion — it should be built before planning the next campaign cycle.
---

# Campaign + Sales System Map

## Public setup

Resolve the user's authorized workspace before following file paths below.
`<workspace>` and named vault folders describe an existing layout, not bundled
data. Reuse equivalent files in the user's setup. Ask for a destination only
when discovery cannot resolve it. Private records and reference documents must
be supplied or located locally; do not invent their contents. Reuse answers
already in the request rather than repeating the intake. Use available supported
tools and the visible in-app Browser for browser work. Installing this skill
does not invoke it or authorize messages, publishing or unrelated service writes.

## What This Skill Builds

A structured document for a Scale client that maps:
- Every campaign → its offer, ICP, and script status
- Every campaign → who calls the leads and when
- A weekly calling coverage grid
- A sales person readiness check (whoever is handling calls)
- A data feedback section with full metrics and what Scale does with each one
- A shared next steps section

The output is a fill-in document. Pre-fill everything we already know. Leave blanks only for things the client must decide or confirm. The document should feel like 80% done when it lands in their hands.

---

## Step 1 — Load Client Context

Read these files in parallel:

1. `veronica-memory/business/clients/[client-name].md` — profile, team, current status
2. `Clients/[Client] - [Contact]/Work Log.md` — what has been built so far
3. Any calling script files in the client folder — to mark as ✅ Built or ❌ Missing
4. Any campaign folders — to understand what campaigns exist and what offers are in play

**What you're extracting:**
- List of campaigns (names and offers)
- For each campaign: does a calling script exist?
- Sales team members — names, roles, readiness level
- Any known calling hours or GHL setup status

If the client folder doesn't exist yet or is thin, ask Osiris for the missing context before proceeding.

---

## Step 2 — Ask for What's Missing

Before writing the document, confirm with Osiris:

1. **Campaigns running** — what's live and what's queued? For each campaign, how many verticals?
2. **Who's on sales** — who is actually calling leads right now? Any team changes, people leaving, or untrained members?
3. **Calling hours** — does Osiris know when they call, or is that a blank for the client?
4. **Script gaps** — are there campaigns without a script yet? (Scale builds it, or client has one?)

Keep this short. One message with all 4 questions. Don't ask them one at a time.

---

## Step 3 — Build the Document

Save to: `Clients/[Client] - [Contact]/[Client] — Ads + Sales System Map.md`

Use the structure below. Pre-fill everything known. Mark blanks clearly with `→ ____________`.

---

### Document Structure

```markdown
# [Client] — Ads + Sales System Map
*Prepared by Scale Advertisement — [Month Year]*
*Fill in the blanks marked with → and send back. This is the missing piece.*

---

## Why This Exists

[Bullet points — NOT paragraphs. Cover:]
- How many campaign sets are running
- What's already built (scripts, automations, offers)
- The gap: leads going cold because no one is assigned to call them on time
- The two things this fixes: coverage map + feedback loop
- Why the data matters: without call feedback, ads can't improve

---

## Campaign Map

[One section per campaign. Use this format:]

### Campaign [N] — [Campaign Name]
**Offer:** [what the ad promises]
**ICP:** [who we're targeting]
**Script:** [✅ Built — link to file] OR [❌ Not built yet — Scale to build]

**Verticals running:**

| Vertical | Location | Daily Budget | Approx Leads/Week |
|----------|----------|-------------|-------------------|
| [Name] | [geo] | → ₹______/day | → ______ leads |

**Who calls these leads:**
- → ____________

**Calling window:**
- → Morning: ______ to ______
- → Afternoon: ______ to ______

**Current status:**
- → [ ] Ads live   [ ] Ads paused   [ ] Not launched yet

---

## Calling Coverage — Full Picture

| Time Slot | Mon | Tue | Wed | Thu | Fri | Sat |
|-----------|-----|-----|-----|-----|-----|-----|
| 9–11am | → | → | → | → | → | → |
| 11am–1pm | → | → | → | → | → | → |
| 2–4pm | → | → | → | → | → | → |
| 4–6pm | → | → | → | → | → | → |

*Write the name of whoever is available to call leads in each slot.*
*Gaps here = leads going cold.*

---

## [Sales Person Name] — Readiness Check

[Adapt this section to whoever handles calls. If it's a new/junior hire, include training questions. If it's an experienced team member, focus on system setup and accountability.]

**Before going live on calls:**
- [ ] Has [name] read the onboarding doc and calling scripts?
- [ ] Has [name] listened to at least 3–5 real call recordings?
- [ ] Does [name] have GHL access and know how to log calls?
- [ ] Does [name] know the top credential line and when to use it?
- [ ] Are we having a morning check-in to review the day's leads and priorities?

**Note:** [Osiris's honest read on the person's current readiness — who's ready to go, who still needs management attention, what the internal communication gap is. Be direct. This section exists to prevent the client from assuming the caller is ready when they're not.]

---

## Data Feedback — Numbers We Review Together

[Frame this as "we all need these numbers" not "send us a report." We're in this together.]

**Weekly metrics (every Monday or Friday):**

| Metric | This Week |
|--------|-----------|
| Total leads received | |
| Leads called (connected) | |
| Leads not reached (no answer, 2+ attempts) | |
| Leads booked — consultation/Zoom set | |
| Not ICP — wrong profile or project type | |
| Not interested — right person, said no | |
| Callback scheduled — follow-up pending | |
| No-shows — booked but didn't attend | |
| No-shows recovered — rebooked after missing | |
| Top objection heard this week | |
| Best-converting vertical this week | |
| Weakest-converting vertical this week | |
| Leads still warm — in follow-up | |

**After the first 20 calls:**
Review together: what objections came up most, which lead profile converted fastest, what time of day had the best pick-up rate. That conversation directly changes targeting and copy.

**Call recordings:**
[Fill in current status — manual recording in place? GHL automation in progress? Fully live?]

---

## What We Do With This Data

- If "not ICP" is high → targeting is off. I'll adjust the audience.
- If "no answer" is high → I'll look at time of day, adjust ad scheduling, tighten the call window.
- If bookings are low despite connections → the script has a gap. I'll rewrite it.
- If no-show rate is high → the confirmation sequence needs to be stronger. I'll rebuild it.
- If one vertical outperforms → I'll scale budget there and pull from the weaker ones.
- If a specific lead profile converts fast → I'll refine ICP targeting to get more of those.

**The faster we have this data, the faster everything improves.**

---

## Next Steps

**[Client] fills in:**
- [ ] All blanks in the Campaign Map — one person assigned per campaign minimum
- [ ] Calling coverage grid
- [ ] [Sales person] readiness checklist
- [ ] Any missing campaign info (budget, vertical details)

**I will:**
- [ ] [Any scripts not yet built]
- [ ] Review the filled-in system map and confirm no gaps
- [ ] [Any GHL or automation setup pending]

---

*Questions? WhatsApp me directly.*
*Osiris, CEO — Scale Advertisement — [Month Year]*
```

---

## Tone Rules

- **Why This Exists** = bullet points only, never paragraphs. Direct and factual.
- **Campaign Map** = pre-fill what we know, leave blanks for what the client decides
- **Readiness Check** = honest and specific. If someone isn't ready, say so. If the client needs to step up as a manager, say that directly — but not harshly.
- **Data Feedback** = "we review together" not "send us." Scale is part of the process.
- **No options lists** in "Who calls" — one open field. The client names one person per campaign.
- Write as Osiris would write: direct, warm, zero corporate padding.

---

## After Saving

1. Tell Osiris the exact file path
2. Give him 2–3 things he should highlight verbally when he shares it with the client — the things the doc can't fully communicate on its own (e.g., urgency of a team member leaving, why the feedback loop matters this week specifically)
