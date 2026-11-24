---
name: verify
description: Boris Cherny's #1 tip — runs a verification pass after any output. Checks that what was built/written/decided is actually correct, complete, and won't cause problems. Use after any implementation, deliverable, or system change.
---

# Verify

## Public setup

Resolve the user's authorized workspace before following file paths below.
`<workspace>` and named vault folders describe an existing layout, not bundled
data. Reuse equivalent files in the user's setup. Ask for a destination only
when discovery cannot resolve it. Private records and reference documents must
be supplied or located locally; do not invent their contents. Reuse answers
already in the request rather than repeating the intake. Use available supported
tools and the visible in-app Browser for browser work. Installing this skill
does not invoke it or authorize messages, publishing or unrelated service writes.

Run a verification pass on whatever was just produced. This is the feedback loop that 2-3x's quality.

## What to verify (based on $ARGUMENTS or context)

**If a file was written:**
- Read the file back and confirm content matches intent
- Check word count if it's a hot cache or brief (should be under limit)
- Check that all links/file references actually exist (`Glob` to verify paths)
- Check for tone/format consistency with writing structure rules

**If a skill or command was created:**
- Read the file back
- Confirm the frontmatter is valid (name, description fields present)
- Confirm the steps are complete and actionable
- Confirm no broken file path references

**If a client update was made:**
- Confirm wiki page, veronica-memory file, and active thread were all updated
- Confirm _HOT.md was updated
- Check that status in _BRIEF.md matches what was just updated

**If a decision was made:**
- Confirm it was captured in _HOT.md
- Confirm any task list changes were saved to Top-Priorities.md
- Confirm relevant people/clients were noted

**If code or automation was built:**
- Run it (or ask Osiris to run it)
- Confirm output matches expected behavior
- Check for any broken dependencies

## Output format

**Verification: [PASS / WARN / FAIL]**
- [Specific check: result]
- [Specific check: result]
- Issues found: [list or "none"]
- Recommendation: [what to do if WARN or FAIL]

If PASS: "All checks passed. You're good."
If WARN: "Minor issues found — fix these before moving on."
If FAIL: "Do not proceed. Fix these first: [list]"
