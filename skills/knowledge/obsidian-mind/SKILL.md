---
name: obsidian-mind
description: Use when formatting any folder of notes, markdown files, or a knowledge base into Obsidian best-practices structure — YAML frontmatter, callouts, wikilinks, atomic concept notes, MOC files, and a Home dashboard. Does NOT change existing content, only adds structure around it.
---

# Obsidian Vault Formatter

## Public setup

Resolve the user's authorized workspace before following file paths below.
`<workspace>` and named vault folders describe an existing layout, not bundled
data. Reuse equivalent files in the user's setup. Ask for a destination only
when discovery cannot resolve it. Private records and reference documents must
be supplied or located locally; do not invent their contents. Reuse answers
already in the request rather than repeating the intake. Use available supported
tools and the visible in-app Browser for browser work. Installing this skill
does not invoke it or authorize messages, publishing or unrelated service writes.

Transforms any folder of markdown notes into a fully structured Obsidian vault. Preserves all existing content — only adds structure, metadata, and links around it.

## What This Skill Does

Given any folder of `.md` files, produce:

1. **YAML frontmatter** on every note
2. **Callouts** replacing plain section headers
3. **Inline wikilinks** connecting related notes
4. **Atomic concept notes** — one file per major framework/idea, in a `Concepts/` subfolder
5. **MOC file** (`🗺️ [Topic] MOC.md`) per folder
6. **Home dashboard** (`Home.md`) at the vault root if multiple folders
7. **Templates/** folder with reusable note starters

---

## Step-by-Step Process

### Step 1 — Read Every Existing File First
Before touching anything, read ALL files in the target folder. Understand:
- What topics are covered
- What frameworks or named concepts exist
- What the current structure looks like

Never rewrite content you haven't read.

### Step 2 — Plan the Concept Extraction
List every major framework, model, or named idea across all files. These become atomic concept notes.

Rule: if a framework has a name and could stand alone as a reference, it becomes its own file in `Concepts/`.

### Step 3 — Reformat Each Literature/Source Note

Add to every existing note — DO NOT change existing prose, quotes, or facts:

**YAML frontmatter:**
```yaml
---
tags:
  - [topic]
  - [subtopics]
type: literature-note
source: [YouTube / Article / Podcast / Book / Personal]
author: [Creator name]
created: [YYYY-MM-DD]
aliases: []
---
```

**Callouts** — replace plain sections with:
- `> [!abstract]` — summary block at the top
- `> [!quote]` — each direct quote
- `> [!tip]` — tactical takeaways (with `- [ ]` checkbox list)
- `> [!important]` — key insights or rules

**Inline wikilinks** — wrap every framework name that has (or will have) a concept note in `[[double brackets]]`.

**Connected section** — at the bottom, link to all concept notes extracted from this file + the folder MOC.

### Step 4 — Create Concept Notes

For each extracted concept, create `Concepts/[Concept Name].md`:

```yaml
---
tags: [topic, subtopics]
type: concept-note
created: [YYYY-MM-DD]
aliases: [alternative names]
---
```

Structure:
1. Opening claim — what this concept IS in 1-2 lines (no heading)
2. `> [!important]` or `> [!quote]` — sharpest articulation of the idea
3. `##` sections for sub-components (the how, steps, breakdown)
4. `> [!tip] How to Apply` — concrete, specific application
5. `## Connected` — wikilinks back to source note + related concepts

**The Iron Rule:** Concept notes contain the idea, not the source. Source notes link to concept notes. Concept notes link back to source notes. No duplication of content — just linked references.

### Step 5 — Create MOC File

One `🗺️ [Topic] MOC.md` per folder:

```yaml
---
tags: [moc, topic]
type: moc
created: [YYYY-MM-DD]
---
```

Sections:
- One-line description of what this topic covers
- `## Source Notes` — table: note title + one-line description of what it covers
- `## Concepts` — grouped links to all concept notes in `Concepts/`
- `## Cross-Topic Links` — links to related concepts in OTHER topic folders

### Step 6 — Create Home.md (if multiple folders)

At the vault root — navigation only, no YAML:

```markdown
# [Vault Name]

[1-line description of what this knowledge base is for]

## Topics
| [[🗺️ Topic MOC]] | What this topic covers |

## All Source Notes
[grouped by topic]

## All Concept Notes
[grouped by topic, dot-separated inline]

## Tags
[all tags in the vault]

## Templates
- [[Literature Note]] — for new captures
- [[Concept Note]] — for new atomic ideas
```

### Step 7 — Create Templates

Two files in `Templates/`:

**Literature Note.md** — YAML frontmatter + all callout placeholders (abstract, frameworks, quotes, takeaways, raw notes, connected). Static placeholder text — no plugin required.

**Concept Note.md** — YAML frontmatter + opening statement placeholder + section placeholders + connected section.

---

## What NOT to Change

- Existing prose, quotes, facts, raw notes — never rewrite these
- File names — never rename existing files
- The actual meaning or argument of any note
- Any existing wikilinks that already exist

Structure is added AROUND content. Content is never touched.

---

## Formatting Standard Reference

| Section | Callout |
|---------|---------|
| Summary / abstract | `> [!abstract]` |
| Key insight / rule | `> [!important]` |
| Direct quote | `> [!quote]` |
| Actionable takeaways | `> [!tip]` |

**Tag naming:** lowercase, hyphenated. e.g. `content-strategy`, `deep-work`, `hiring`

**Type field values:** `literature-note` · `concept-note` · `moc`

**File naming for concepts:** Title Case with spaces. e.g. `The Five-Line Story Framework.md`

---

## Common Mistakes

- **Changing content while reformatting** — never rewrite existing prose. Add callout wrappers, don't touch what's inside them.
- **Creating concept notes for things that don't have names** — only extract named frameworks/models/systems. Not every paragraph is a concept.
- **Skipping the Connected section** — every note needs links out. An isolated note is a dead note.
- **Generic wikilinks** — `[[Marketing]]` is useless. `[[The Affluence Paradox]]` is useful. Link to specific concepts.
- **Duplicating content** — if the idea is in the concept note, the source note just needs a wikilink to it, not a full re-explanation.
