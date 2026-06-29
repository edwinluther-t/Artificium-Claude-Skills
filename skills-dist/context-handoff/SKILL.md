---
name: context-handoff
description: Use when ending a session with unfinished work, or when preparing a summary so a future Claude session can pick up without drift, repeated questions, or lost decisions.
---

# Context Handoff

A compact, structured artifact that lets a new Claude session resume work with zero re-derivation.

The failure mode this prevents: next session spends the first 10 messages re-establishing what was decided, re-reading files already understood, or making choices that conflict with prior decisions.

## When to Write One

- Ending a session mid-task
- Handing work to a different context (different project, different day)
- After a long session where decisions accumulated and aren't obvious from the code

## The Handoff Artifact

Write this as a fenced block the next session can read verbatim. Keep it under 400 words.

```markdown
## Handoff — [Task Name] — [Date]

### State
[One sentence: what is the current state of this work? Deployed? In progress? Blocked?]

### What was decided
- [Decision 1]: [why — the constraint or reason, not just the choice]
- [Decision 2]: [why]

### What's next
1. [Immediate next action — specific enough to act on without asking]
2. [Second action]

### Watch out for
- [Non-obvious risk, constraint, or gotcha discovered during this session]

### Key files
- [path/to/file.ext] — [one-line description of its role in this task]

### Open questions
- [Question that needs an answer before proceeding, if any]
```

## What to Include vs. Skip

**Include:**
- Decisions that aren't derivable from the code or git history
- The *why* behind architectural or approach choices
- Risks or constraints discovered mid-session
- The exact next action (not "continue the work")

**Skip:**
- Anything already obvious from reading the files
- Decisions that are self-evident from the implementation
- Completed work that has no bearing on what's next
- Status updates that git log already provides

## Placing the Artifact

Options in order of preference:

1. Paste into the next session's first message — fastest pickup
2. Write to a temp file (`handoff.md` at project root, delete after pickup)
3. Add as a section in an existing `NOTES.md` or planning doc if one exists

Do not commit handoff files to git. They are session artifacts, not project history.

## Common Mistakes

| Mistake | Fix |
|---|---|
| Listing completed work in "what's next" | "What's next" is only future actions |
| Vague next action ("continue implementing X") | Name the specific file, function, or step |
| Omitting the why on decisions | Without the why, the next session may reverse a good decision |
| Writing a handoff for a routine session | Only write one if the next session will actually need it |
