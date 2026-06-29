---
name: after-action-review
description: Use after completing a significant task, feature, incident, or session to capture what happened, what broke, and what to carry forward. Use when the user asks for a debrief, retrospective, or post-mortem.
---

# After-Action Review

A structured debrief run after completing significant work. The goal is to extract durable signal before the session ends and context is lost.

Run this after: a feature shipped, a bug fixed, an incident resolved, a session with major decisions made.

## The Four Questions

Answer these in order. Be specific — vague answers produce nothing useful.

### 1. What did we set out to do?

State the original intent in one or two sentences. If the scope changed mid-task, note the original intent *and* what it became.

### 2. What actually happened?

Describe what was built, changed, or decided. Include:
- Files created or modified (key ones only)
- Decisions made and why
- Anything that deviated from the original plan

### 3. What broke or was harder than expected?

Honest account of friction:
- What assumptions were wrong?
- What took longer than it should have?
- What failed and had to be retried?
- What tooling, process, or information was missing?

Skip this section only if nothing went wrong — not because it's uncomfortable.

### 4. What should be carried forward?

Actionable outputs only:
- **Remember**: facts or decisions that future sessions need (candidates for memory)
- **Fix**: things left broken or incomplete that need a follow-up task
- **Change**: process or approach adjustments for next time
- **Skip**: things tried that weren't worth it

## Output Format

Write the review as a short document, not prose. Use headers and bullets. Aim for under 300 words. If it exceeds that, the review is covering too much — split into multiple reviews or cut to essentials.

```markdown
## After-Action Review — [Task Name] — [Date]

### Intent
[One sentence]

### What happened
- [Key fact or change]
- [Key decision]

### What was hard
- [Friction point + why]

### Carry forward
- Remember: [fact]
- Fix: [item]
- Change: [process adjustment]
```

## When to Save vs. Discard

Save the review (to memory or a file) if any of these are true:
- A non-obvious decision was made that will affect future work
- A failure mode was discovered that could recur
- A process change is being committed to

Discard if the session was routine and nothing surprised you. Not every session needs a written record.

## Common Mistakes

| Mistake | Fix |
|---|---|
| Writing "it went well" with no detail | Force specificity: what specifically worked and why |
| Skipping "what broke" because the task succeeded | Success with friction is still friction worth logging |
| Writing future tasks as vague intentions | Write them as concrete, actionable items or don't write them |
| Reviewing too late | Run immediately after the task; memory decays fast |
