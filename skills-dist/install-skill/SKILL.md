---
name: install-skill
description: Use when deploying a skill from this collection into a Claude Code environment — globally, per-project, or for a specific user. Also use when verifying a skill is correctly installed and discoverable.
---

# Install Skill

How to deploy skills from The Artificium into a Claude Code environment.

## Skill Resolution Order

Claude Code loads skills in this order (last wins on name collision):

1. Global: `~/.claude/skills/`
2. Project: `{project-root}/.claude/skills/`
3. Local override: `.claude/skills/` (relative to cwd)

Install at the lowest scope that fits the need.

## Installation

### Global (all projects)

```bash
cp skills/{category}/{subcategory}/skill-name.md ~/.claude/skills/
```

### Project-scoped

```bash
mkdir -p .claude/skills
cp skills/{category}/{subcategory}/skill-name.md .claude/skills/
```

### Bulk install by category

```bash
# All engineering/core skills globally
mkdir -p ~/.claude/skills
cp skills/engineering/core/*.md ~/.claude/skills/
```

## Verify Installation

```bash
# Confirm file is present
ls ~/.claude/skills/ | grep skill-name

# Confirm frontmatter is valid (name + description only, no extra fields)
head -5 ~/.claude/skills/skill-name.md
```

Claude Code reads the `name:` field as the skill identifier and `description:` for trigger matching. If either is malformed or missing, the skill will not load.

## Naming Conflicts

If two skills share the same `name:` value, the more local scope wins. To audit for conflicts:

```bash
grep -rh "^name:" ~/.claude/skills/ .claude/skills/ 2>/dev/null | sort | uniq -d
```

Resolve by renaming the lower-priority skill's `name:` field before installing.

## Updating a Skill

Overwrite the file. No restart required — Claude Code reads skill files at session start.

```bash
cp skills/{category}/{subcategory}/skill-name.md ~/.claude/skills/skill-name.md
```

## Removing a Skill

```bash
rm ~/.claude/skills/skill-name.md
```

## Common Mistakes

| Problem | Fix |
|---|---|
| Skill not triggering | Check `name:` and `description:` fields are present and under 1024 chars total |
| Wrong skill loaded | Check for name collision across scopes (`grep -rh "^name:"`) |
| Skill installed but ignored | Verify file extension is `.md`, not `.md.txt` or similar |
| Edited skill not reflecting | Confirm you edited the installed copy, not the source in `skills/` |
