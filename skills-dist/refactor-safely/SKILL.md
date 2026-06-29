---
name: refactor-safely
description: Use when restructuring code without changing behavior — extracting functions, renaming, splitting files, moving modules, changing call patterns. Use when the task is structural change, not style cleanup or bug fixing.
---

# Refactor Safely

Structural code changes without breaking behavior. The constraint is absolute: a refactor commit must not change what the code does.

## The Core Rule

**One concern per commit.** Never mix structure changes with behavior changes.

If you need to fix a bug *and* extract a function: fix the bug first, commit, then extract.
If you need to rename *and* add a feature: rename first, commit, then add.

Mixing them makes the diff unreadable, breaks bisect, and makes rollback destructive.

## Before You Touch Anything

1. **Establish a safety net.** Tests must exist and pass before the first change. If they don't exist, write them first — or acknowledge explicitly that you're refactoring without a net and accept the risk.
2. **Understand the blast radius.** Search for all callers of what you're changing before moving it.
   ```bash
   grep -rn "function_name\|ClassName\|module_path" src/
   ```
3. **Commit the current state.** Even if it's messy. You need a clean rollback point.

## Refactor in Phases

### Phase 1 — Rename
Change names only. No logic moves, no signature changes. Commit.

### Phase 2 — Move
Relocate code to new files or modules. Update imports. No logic changes. Commit.

### Phase 3 — Extract / Inline
Pull repeated logic into shared functions, or inline single-use abstractions that add noise. Commit.

### Phase 4 — Restructure signatures
Change how functions are called (parameter order, shape, return type). Update all callers. Commit.

Run tests after each phase. If tests fail after a refactor commit, the refactor introduced a behavior change — that's a bug, not a structural change.

## Signals You've Left Refactor Territory

Stop and split into a separate commit if you find yourself:
- Fixing a bug you noticed while moving code
- Adding a guard or null check that wasn't there
- Changing a default value
- Adding a log statement
- Optimizing a loop

All of these are behavior changes. Log them, finish the refactor, then address them separately.

## Commit Message Convention

```
refactor: extract payment validation into PaymentValidator

No behavior change. Moved logic from OrderService.processPayment()
into a dedicated class. All existing tests pass unchanged.
```

The phrase "No behavior change" in the commit message is a claim — make sure it's true.

## When Tests Don't Exist

Be explicit with yourself and the user:

> "There are no tests covering this path. I'm proceeding with the refactor but cannot verify behavior preservation mechanically. Manual verification is required."

Do not pretend test coverage exists. Do not skip the warning.

## Common Mistakes

| Mistake | Fix |
|---|---|
| Refactoring and bug-fixing in one commit | Split: fix first, commit, then refactor |
| Moving code without searching for all callers | Grep first, update all call sites before committing |
| Treating a rename as "trivial" and skipping tests | Run tests — renames break things in dynamic languages |
| Changing a function signature and "updating callers" in the same commit as the rename | Phase it: rename first, signature change second |
| Calling it a refactor when behavior changes | That's a feature change or bug fix; name it correctly |
