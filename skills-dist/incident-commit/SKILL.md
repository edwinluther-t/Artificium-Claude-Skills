---
name: incident-commit
description: Use during or immediately after an incident — outage, data corruption, failed deploy, security event — when committing fixes, rollbacks, or investigation changes under time pressure. Use to preserve rollback points and investigation trail without polluting history.
---

# Incident Commit

Commit discipline during an incident. The goal is to preserve rollback granularity and investigation trail while moving fast.

## The Two Mistakes

**Committing everything in one blob** — you lose the ability to bisect, partial-rollback, or understand what actually fixed it.

**Over-engineering commits during the incident** — you slow down when speed matters.

The middle path: commit at natural decision points, not at the end.

## When to Commit During an Incident

Commit at each of these moments:

1. **Before you touch anything** — if the repo is in a clean state, commit it. This is your rollback baseline.
2. **After each hypothesis** — if you tried something and it didn't work, commit (or stash and discard). Don't layer failed attempts.
3. **When something works** — commit immediately, before layering the next fix.
4. **Before a rollback** — tag the broken state before reverting so it can be examined later.

## Commit Message Format

During an incident, messages must be fast to write and easy to grep later.

```
incident: [what changed] — [status]

Context: [one sentence on why this change was made]
Ref: [ticket, alert ID, or "no ref"]
```

Examples:
```
incident: revert worker pool size to 10 — testing

Context: pool size increase to 50 caused connection exhaustion under load.
Ref: INC-2024-0612
```

```
incident: disable feature flag payments_v2 — mitigating

Context: v2 payment flow throwing 500s after 14:30 UTC deploy.
Ref: INC-2024-0612
```

```
incident: restore db index on orders.created_at — fix confirmed

Context: Missing index caused full table scan, query time 8s → 40ms after restore.
Ref: INC-2024-0612
```

**Status tags**: `investigating` / `testing` / `mitigating` / `fix confirmed` / `rolled back`

## Tagging

Tag the commit that resolves the incident:

```bash
git tag incident/INC-2024-0612/resolved <commit-sha>
git push origin incident/INC-2024-0612/resolved
```

Tag the commit where the incident was introduced (when known):

```bash
git tag incident/INC-2024-0612/root-cause <commit-sha>
```

These tags survive branch cleanup and make post-mortems trivial.

## Rollback Commits

When rolling back, do not use `git revert` blindly on a range. Be explicit:

```bash
# Revert a single commit
git revert <sha> --no-edit

# Rollback to a known-good state
git checkout <good-sha> -- path/to/affected/file
git commit -m "incident: rollback orders.py to pre-deploy state — mitigating

Context: deploy at 14:22 UTC broke order creation. Restoring file to last known good.
Ref: INC-2024-0612"
```

Never `git reset --hard` on a shared branch during an incident. You'll destroy the investigation trail for everyone else.

## After the Incident

1. Run `git log --oneline --grep="incident:"` to reconstruct the timeline.
2. Use this as the skeleton for the post-mortem timeline section.
3. Clean up tags that are no longer needed after the post-mortem is closed.

## Common Mistakes

| Mistake | Fix |
|---|---|
| One giant "fix incident" commit | Commit at each decision point; status tag shows what it was for |
| No commit before attempting a fix | Always commit (or tag) the broken state first |
| Force-pushing during an incident | Never — it destroys others' investigation trail |
| Vague messages like "hotfix" | Include what changed, why, and the incident ref |
| Forgetting to tag the resolution | Tag immediately when confirmed; memory fades fast |
