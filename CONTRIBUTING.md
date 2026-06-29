# Contributing to The Artificium

Contributions are welcome — new skills, fixes, and improvements all help the
collection grow. This guide covers how to add or change a skill.

The bar here is simple: **a skill should earn its place in someone's context
window.** If it's vague, redundant with an existing skill, or padded with cruft,
it makes the whole collection worse. Sharp and useful beats long and impressive.

## Ways to contribute

- **Add a new skill** — propose a skill that fills a gap.
- **Improve an existing skill** — sharper instructions, better examples, fixes.
- **Report a problem** — open an issue if a skill is broken, unclear, or outdated.

If you're unsure whether an idea fits, open an issue first and ask.

## Skill format

Every skill is a single Markdown file with two-field frontmatter only:

```markdown
---
name: skill-name
description: One-line description used for trigger matching.
---

# Skill Title

...content...
```

Rules:

- `name:` must be unique across the collection and match the file/directory name.
- `description:` is what Claude matches against to decide when to use the skill —
  make it specific about *when* to trigger, not just what it does.
- **Frontmatter is `name:` and `description:` only.** No `metadata:`, `license:`,
  `argument-hint:`, or author fields.

## Keep skills clean

When adding or editing a skill:

- No author tags, vendor names, or references to private/internal tooling.
- No platform-locked tool names — describe the technique generically so it works
  in any Claude Code setup.
- Keep all behavioral instructions, checklists, workflows, code examples, and
  trigger logic. The value is in the content, not the metadata.

## Directory layout

Source skills live in `skills/`, organized by category and subcategory:

```
skills/<category>/<subcategory>/<skill-name>.md
```

The installable format in `skills-dist/<skill-name>/SKILL.md` is generated —
**do not edit `skills-dist/` by hand.**

## Build before you submit

After editing anything in `skills/`, regenerate the distributable copies:

```bash
python build-dist.py
```

Commit both your `skills/` change and the regenerated `skills-dist/` output.

## Git hooks

This repo ships a `commit-msg` hook that rejects AI co-author attribution in
commit messages. Enable it once after cloning:

```bash
git config core.hooksPath .githooks
```

Keep commit messages clean — no `Co-Authored-By` or "Generated with" lines.

## Quality checklist

Before you open a PR, run your skill against this:

- [ ] **Triggers cleanly** — the `description` says *when* to use it, not just what it is.
- [ ] **Doesn't already exist** — search the README table; if it overlaps, improve the existing skill instead.
- [ ] **Frontmatter is clean** — `name` + `description` only.
- [ ] **No cruft** — no vendor names, author tags, dead tool references, or platform-locked paths.
- [ ] **Self-contained** — someone can use it without external context or private tooling.
- [ ] **Built** — `python build-dist.py` has been run and `skills-dist/` is committed.

## Submitting a PR

1. Fork the repo and create a branch.
2. Add or edit your skill in `skills/`.
3. Run `python build-dist.py`.
4. Add yourself to `AUTHORS.md` under Contributors.
5. Open a PR describing the skill and when it should trigger.

By contributing, you agree your work is licensed under the project's
[MIT License](LICENSE).
