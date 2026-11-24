---
name: hooks
description: Use when generating 5-10 ad-ready hooks from a locked editorial narrative + article reference. Encodes the 12 luxury hook techniques (Patek/Rolex/Hermès/Ogilvy school) plus 2024-26 luxury zeitgeist rules and humanizer guardrails. Designed to plug into the Editorial workflow between Narrative and Carousel. Trigger on /hooks, "write hooks for [article]", "rewrite the hooks", "I need hook variations", or when sitting at the Hooks step in any editorial piece. Output goes into the article file's `## Hooks` section, not a separate Hooks.md.
---

# Hooks — Luxury Hook Generator

## Public setup

Resolve the user's authorized workspace before following file paths below.
`<workspace>` and named vault folders describe an existing layout, not bundled
data. Reuse equivalent files in the user's setup. Ask for a destination only
when discovery cannot resolve it. Private records and reference documents must
be supplied or located locally; do not invent their contents. Reuse answers
already in the request rather than repeating the intake. Use available supported
tools and the visible in-app Browser for browser work. Installing this skill
does not invoke it or authorize messages, publishing or unrelated service writes.

Veronica's job: take a locked editorial Strategy + Narrative + Article and generate 5-10 hooks that read like Patek Philippe print ads, not LLM analysis.

A hook is one ad-ready unit. It opens an ad, fronts a carousel, sits as the subject line of a long-form pitch. 1-3 sentences. Zero filler. Each hook deploys ONE specific technique from the luxury catalog below.

This skill **does not write articles, body copy, or carousels.** It writes hooks only.

---

## Stage 1 — Load context

Before writing a single hook, read these inputs:

1. **The narrative thesis** — `Editorial/_Sessions/[date] — [Client] narratives*.md` OR the piece's `Strategy.md`
2. **The specific article** the hooks are seeding — `Editorial/[NN]/Article N — [Title].md`
3. **The avatar** — pulled from `Strategy.md`
4. **Client voice notes** — e.g., `Clients/[Client]/[Research]/[NN] — [Founder] — Voice + Philosophy.md`
5. **Client-specific constraints** — no-brand-names rule, tonal restrictions, etc. (check Strategy.md and any Discussion Notes)

Print a 3-line summary back before generating:

> Spine: [the central tension]
> Avatar: [who reads this]
> Constraints: [what's off-limits]

---

## Stage 2 — Extract the spine

Identify these four elements before any hook is drafted. Every hook will reframe one or more of them.

- **Central tension** — the contradiction the article surfaces
- **Avatar's deepest fear** — the thing they don't want to be wrong about
- **Financial / strategic edge** — the hard data, the asymmetric advantage
- **The unspoken truth** — what the avatar is intuiting but hasn't said out loud

These four are the raw material. Each technique below is a different lens for cutting that material into hook form.

---

## Stage 3 — The 12 luxury hook techniques

Generate 8-10 hooks, **each using a different technique**. Tag every hook with the technique number and name. No two hooks may use the same technique in one batch.

### 01. Specificity Over Superlatives — the Ogilvy principle

**Principle:** Back the claim with one counterintuitive, provable, oddly specific fact. The single detail proves the larger truth.

**Verbatim example:** *"At 60 miles an hour the loudest noise in this new Rolls-Royce comes from the electric clock."* — David Ogilvy, 1958. 21 days of research distilled into one fact that proves "quiet" without ever saying "quiet."

**Structural template:** "At [precise condition], [the only thing happening] is [specific small detail]." Or: "[Action requires] exactly [N] [units] of [process]."

**When to deploy:** When the article has a hard, specific, citable fact buried in the body. Surface that fact. Don't dress it.

### 02. Contradiction / Inversion — the Patek principle

**Principle:** State the opposite of what the reader expects. Remove ownership, comfort, certainty — and replace with stewardship, complication, paradox.

**Verbatim example:** *"You never actually own a Patek Philippe. You merely look after it for the next generation."*

**Structural template:** "You never actually [verb the reader assumes]. You merely [the harder, deeper truth]."

**When to deploy:** When the article inverts a piece of conventional wisdom. The hook should embody the inversion.

### 03. Understatement / Silence — the Rolex / Hermès principle

**Principle:** Say less than the moment calls for. Trust the reader. Restraint reads as authority.

**Verbatim examples:** Rolex: *"A crown for every achievement."* / Hermès never uses the word "luxury" — they use "exceptional," "exquisite," and lean on the 1837 origin story.

**Structural template:** Single declarative sentence. No adjectives. Subject + verb + concrete noun. Stop.

**When to deploy:** When everything around the avatar is shouting. The hook becomes the quietest line in the room.

### 04. Sensory Specificity — texture over adjective

**Principle:** Replace any abstract quality word ("sumptuous," "elegant," "premium") with the material + the action that produces the quality.

**Verbatim example:** Not "elegant," but *"hand-polished in Geneva, each dial requires 60 hours of finishing before it meets the maison's exacting standards."* Not "sumptuous," but *"supple Italian calfskin, finished with subtle sheen, hand-stitched edges softening over time."*

**Structural template:** "[Specific material] from [specific place], [specific process verb] over [specific time]." The body, not the brain.

**When to deploy:** When the article references craft, material, or process. Surface the specifics. Names of places, hours, hands.

### 05. Heritage Anchoring — named place + craft + time

**Principle:** Bind the claim to geography + history + craft lineage. Inherited credibility is the cheapest credibility.

**Verbatim examples:** Aman: *"To own an Aman Residence is to see a destination in a new light, to discover its cultural nuances..."* / The Oberoi Delhi: *"overlooking Humayun's Tomb on one side and a lush, forested golf course on the other..."*

**Structural template:** "[Specific place], [specific time / lineage], [specific craft]." Geography does the work.

**When to deploy:** When the avatar's category rewards lineage (architecture, hospitality, watches, real estate, wine, anything where time is a credential).

### 06. Lifestyle / Aspirational Character — identity over feature

**Principle:** Don't describe the product. Describe the person who chooses it. The buyer becomes a character in a story they want to star in.

**Verbatim examples:** Lamborghini: *"We are not supercars. We are Lamborghini."* / Bentley philosophy: *"Those who view the automobile as a sanctuary gravitate toward Rolls-Royce; those who see it as an instrument gravitate toward Bentley."*

**Structural template:** "We are not [the category]. We are [the specific identity]." Or: "[Type of person] choose [the thing]. [Different type] choose [the alternative]."

**When to deploy:** When the avatar self-identifies as belonging to a tier, lineage, or sensibility — and the article validates that identity.

### 07. Exclusivity Gating — invitation language

**Principle:** Imply scarcity through what's withheld, not what's promised. No price. No availability. "Reserved for," "by appointment," "discover the collection."

**Verbatim examples:** Rolls-Royce — no public price, brochure must be requested. *"Reserved for collectors since 1921."* Aman: 6:1 staff-to-guest ratio (implicit: "we cannot serve everyone").

**Structural template:** "[Verb of invitation] [specific minority]. [What is reserved / withheld]."

**When to deploy:** When the article positions the offering as inherently selective. Never use this if the actual offering is broadly available — the gating must be true.

### 08. Emotional Payoff Before Feature

**Principle:** Lead with what the buyer feels, not what the product does. Spec is the proof; emotion is the lede.

**Verbatim example:** Not "sapphire crystal," but *"passes through your hands to the next generation's wrists."* Not "18-karat gold," but the inheritance.

**Structural template:** "[Emotional payoff in concrete form]. [The feature only as proof, in second clause if at all]."

**When to deploy:** When the article makes a financial / strategic / functional case, but the avatar is buying for emotional reasons underneath. Hook the emotion. Body proves the function.

### 09. Proof Architecture — numbered + named

**Principle:** Replace abstract claims with countable, nameable specifics. "Expensive" → "300 hours." "Quality" → "98 separate tests." "Exclusive" → "12 produced annually."

**Verbatim example:** Ogilvy backed every Rolls-Royce claim with specifics: 98 quality tests, engineers using stethoscopes, 21 days of research per ad.

**Structural template:** "[Number] + [specific noun] + [specific time/place/process]."

**When to deploy:** When the article cites a specific number that's punchy. Surface the number. Let it stand.

### 10. Status Without Shame — price as quality proof

**Principle:** When cost is part of the conversation, frame it as proof of standard, not as expense. The premium is the message.

**Verbatim examples:** A 6:1 staff-to-guest ratio costs money — but the copywriting frames it as service magnitude. The 21 days of Ogilvy research costs time — but the copy frames it as proof of care.

**Structural template:** "[Specific cost / commitment / scarcity] is what [specific outcome] requires."

**When to deploy:** When the avatar is price-sensitive but quality-driven. The hook reframes the cost as the credential.

### 11. Assertion Without Apology — confident brevity

**Principle:** State the claim flat. No softening, no hedging, no permission-asking. Authority comes from refusing to negotiate.

**Verbatim examples:** Audemars Piguet: *"To break the rules, you must first master them."* / Hermès: *"The horse is our first client."*

**Structural template:** Short imperative or declarative. No "perhaps," "we believe," "in our view." The sentence ends where confidence ends.

**When to deploy:** When the article makes a contrarian claim that's defensible. The hook lands the claim before the reader can object.

### 12. Open Loop / Story Initiation

**Principle:** Open with a fragment, an unfinished thought, a deliberate dissonance. The reader must continue reading to close the loop.

**Verbatim example:** Wallpaper* editorial: *"It freezes time or, rather, freezes out time."* The contradiction forces the read to continue. Fashion: *"Cut for twilight dinners on the Amalfi Coast"* — the reader has to ask what happens next.

**Structural template:** Begin mid-thought. Or with a contradiction the reader must resolve. Or with a sentence that demands a "wait, why?"

**When to deploy:** When the article has narrative momentum. The hook borrows that momentum to keep the reader inside.

---

## Stage 4 — The 2024-26 luxury zeitgeist rules

Apply these as overlays on every hook generated. They are direction-of-travel, not absolute laws.

- **Essentialism > feature lists.** Lead with the core, not the checklist.
- **Embodiment > authenticity claims.** Show the work. Don't say "authentic."
- **Empowerment > "experience."** Sell agency and decision power, not indulgence.
- **Strategy > beauty.** Intellectual rigor reads as luxury now. Pretty prose reads as desperation.
- **Craft mastery > escapism.** Post-pandemic affluent readers want to see expertise, not be told to relax.

---

## Stage 5 — The cliché blacklist (humanizer pass)

Run every hook through this list. If a hook contains any of these, it dies and gets rewritten.

**Banned words:**
- indulge, elevate, experience (overused as verbs), discerning, timeless, eternal, exquisite, magnificent, breathtaking, stunning, remarkable, vibrant, nestled, groundbreaking, sumptuous, opulent, lavish, world-class

**AI-vocabulary markers:**
- tapestry, landscape, foster, showcase, underscore, interplay, intersection, resonate, embark, journey (as a verb), curate (when overused), elevate (as a verb), unleash, unlock

**Significance inflation:**
- "marks a pivotal moment," "testament to," "broader trends," "evolving landscape," "in today's world," "in an era of," "more than ever"

**Banned patterns:**
- Superlative stacking ("the most exquisite, exceptional, extraordinary...")
- Em dash overuse (1 em dash per hook max)
- Rule of three lists ("innovation, inspiration, industry insights")
- Negative parallelism ("It's not just X, it's Y") — sounds like a webinar title
- First-person brand voice ("we pride ourselves," "we believe in")
- Vague attributions ("industry reports show," "experts argue," "many believe")
- Temporal opening clichés ("In 2026...", "Today...", "In a world where...")

---

## Stage 6 — The Patek test (final filter)

For every hook before saving, run this test:

**Substitute "Patek Philippe" or "Aman" or "Hermès" for the relevant client noun in the hook. Could this credibly appear in their print ad with one substitution?**

- If yes → ship.
- If it sounds like LLM analysis or marketing-deck language → scrap and redo.

This is the highest filter. Pass it or kill the hook.

---

## Stage 7 — Output format

Save the hooks into the article file's `## Hooks` section. **NEVER** save to a separate `Hooks.md` — Osiris's explicit instruction. Hooks live in the article file.

Use this exact format:

```markdown
## Hooks — N ad-ready variations

Each hook below uses a different technique from the luxury hook catalog and can stand as the opening line of an ad, the cover slide of a carousel, or the subject line of a long-form pitch.

---

**01. [Technique name]**<br>
[Hook text — 1 to 3 sentences]

---

**02. [Technique name]**<br>
[Hook text]

...
```

If a `## Hooks` section already exists in the file, **replace** it. Preserve everything else (title, subhead, body, carousel mapping).

After saving, tell Osiris the exact file path.

---

## Never

- Use any blacklisted word from Stage 5
- Paraphrase the article's body into marketing speak
- Save hooks to a separate `Hooks.md` file
- Use brand names when the client has a no-brand-names rule (check Strategy.md)
- Repeat a technique across hooks in the same batch
- Write hooks longer than 3 sentences
- Open with "In 2026..." or "Today..." or any temporal-cliché framing
- Generate hooks without reading Strategy + Narrative + Article first
- Submit hooks that fail the Patek test

## Always

- Read Strategy + Narrative + Article before writing the first hook
- Print the 3-line spine summary back to Osiris before generating
- Tag each hook with its technique number and name
- Run every hook through the Stage 5 humanizer pass
- Run every hook through the Stage 6 Patek test
- Save to the article file's `## Hooks` section
- Print exact file paths after saving
- Spread across at least 8 of the 12 techniques per batch of 10
- Vary tonal register (contrarian, quote-led, stat-led, philosophical, adversarial, understated)
