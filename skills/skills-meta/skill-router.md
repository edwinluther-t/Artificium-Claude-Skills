---
name: skill-router
description: Use when the task is ambiguous and multiple skills could apply, or when deciding which skill to load from The Artificium collection for a given request. Use to resolve skill selection conflicts or identify the right skill without loading all of them.
---

# Skill Router

Dispatch logic for The Artificium skill collection. Use this to pick the right skill before loading it.

## Collection Map

| Domain | Subcategory | When to reach here |
|---|---|---|
| `agents/debugging/` | agent eval, introspection | Agent behaving unexpectedly, eval failures |
| `agents/harnesses/` | loops, OS, dynamic workflows | Building or running an autonomous agent |
| `agents/meta/` | context, cost, prompts, council | Designing agent behavior, prompt architecture |
| `agents/orchestration/` | parallel, team, plan | Coordinating multiple agents or subagents |
| `content/brand/` | voice, discovery, guidelines | Brand identity, tone of voice work |
| `content/marketing/` | campaigns, SEO, ads | Marketing copy, campaign planning |
| `content/sales/` | investor, leads, outreach | Sales materials, investor decks |
| `content/writing/` | articles, docs, research | Long-form writing, content production |
| `design/aesthetics/` | brutalist, minimalist, soft | Applying a visual style or aesthetic |
| `design/assets/` | slides, video, banners, shaders | Generating visual or media assets |
| `design/motion/` | animation, transitions | Motion design and animation patterns |
| `design/systems/` | tokens, design system, Figma | Design system management and governance |
| `design/ui/` | components, a11y, review | UI implementation, accessibility, redesign |
| `engineering/architecture/` | ADRs, API design, migration | System-level design decisions |
| `engineering/backend/` | Go, Python, Rust, DB | Language-specific or backend patterns |
| `engineering/core/` | review, debug, refactor, onboard | General engineering practices |
| `engineering/data/` | SQL, ML, scraping, pipelines | Data engineering and ML workflows |
| `engineering/frontend/` | React, Angular, perf, a11y | Frontend framework and performance |
| `engineering/infra/` | CI/CD, K8s, observability | Infrastructure and deployment |
| `engineering/mobile/` | Android, iOS, Flutter | Mobile platform development |
| `engineering/security/` | audit, hardening, bounty | Security review and hardening |
| `engineering/testing/` | TDD, e2e, benchmarks | Testing strategy and execution |
| `ops/comms/` | email, meetings, internal | Communication and meeting ops |
| `ops/documents/` | PPTX, DOCX, PDF, XLSX | Office document generation |
| `ops/git/` | workflow, changelog, worktrees | Git operations and versioning |
| `ops/project/` | planning, specs, blueprints | Project management and planning |
| `research/competitive/` | analysis, platform reports | Competitor and market research |
| `research/market/` | deep research, literature | Market research and academic review |
| `skills-meta/` | create, install, audit, route | Working on the skill collection itself |

## Routing Decision

When a task maps to more than one skill:

1. **Scope first** — pick the most specific skill over the more general one. `react-patterns` over `frontend-patterns`; `golang-testing` over `test-driven-development`.
2. **Action first** — if the task is primarily about doing vs. designing, pick the doing skill. `executing-plans` over `writing-plans`.
3. **Domain first** — if the task is in a known language or framework, pick that skill over a generic equivalent.
4. **Load both only if** the task genuinely spans two distinct concerns (e.g., designing an API *and* writing an ADR — load `api-design-patterns` + `architecture-decision-records`).

## Common Ambiguities

| Task description | Load this | Not this |
|---|---|---|
| "Review my code" | `engineering/core/code-review.md` | `design/ui/design-review.md` (unless it's UI) |
| "Write a plan" | `ops/project/writing-plans.md` | `ops/project/planning-and-task-breakdown.md` (that's for breakdown, not prose plans) |
| "Debug the agent" | `agents/debugging/agent-introspection-debugging.md` | `engineering/core/debugging.md` (that's for code, not agents) |
| "Create a skill" | `skills-meta/skill-creator.md` | `skills-meta/writing-skills.md` (that's the TDD methodology; creator is the workflow) |
| "Refactor this" | `engineering/core/refactor-safely.md` | `engineering/core/code-simplification.md` (simplification is style; refactor-safely is structural) |
| "Set up CI" | `engineering/infra/ci-cd-and-automation.md` | `ops/git/git-workflow-and-versioning.md` |
| "Write tests" | `engineering/testing/test-driven-development.md` | Language-specific testing skill (use language skill *in addition* if stack-specific) |

## When No Skill Matches

If no skill in the collection covers the task:

1. Check `skills-meta/skill-scout.md` — search before creating.
2. If nothing exists, use `skills-meta/skill-creator.md` to build it.
3. File the new skill in the correct subcategory per the collection map above.
