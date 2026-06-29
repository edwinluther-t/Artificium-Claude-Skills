---
name: prompt-optimizer
description: Analyze raw prompts, identify intent and gaps, and output a ready-to-paste optimized prompt. Advisory role only — never executes the task itself. Triggers when the user says "optimize prompt", "improve my prompt", "rewrite this prompt", or asks for help writing a better prompt.
---

# Prompt Optimizer

Analyze a draft prompt, critique it, and output a complete optimized prompt the user can paste and run.

## When to Use

- User says "optimize this prompt", "improve my prompt", "rewrite this prompt"
- User says "help me write a better prompt for..."
- User says "what's the best way to ask Claude Code to..."
- User pastes a draft prompt and asks for feedback or enhancement
- User says "I don't know how to prompt for this"
- User explicitly invokes `/prompt-optimize`

### Do Not Use When

- User wants the task done directly (just execute it)
- User says "optimize this code", "optimize performance" — these are refactoring tasks, not prompt optimization
- User says "just do it"

## How It Works

**Advisory only — do not execute the user's task.**

Do NOT write code, create files, run commands, or take any implementation action. Your ONLY output is an analysis plus an optimized prompt.

If the user says "just do it" or "don't optimize, just execute", tell the user this skill only produces optimized prompts, and instruct them to make a normal task request if they want execution instead.

Run this 6-phase pipeline sequentially. Present results using the Output Format below.

### Analysis Pipeline

### Phase 0: Project Detection

Before analyzing the prompt, detect the current project context:

1. Check if a `CLAUDE.md` exists in the working directory — read it for project conventions
2. Detect tech stack from project files:
   - `package.json` → Node.js / TypeScript / React / Next.js
   - `go.mod` → Go
   - `pyproject.toml` / `requirements.txt` → Python
   - `Cargo.toml` → Rust
   - `build.gradle` / `pom.xml` → Java / Kotlin (then check for `quarkus` in build file → Quarkus, or `spring-boot` → Spring Boot)
   - `Package.swift` → Swift
   - `Gemfile` → Ruby
   - `composer.json` → PHP
   - `*.csproj` / `*.sln` → .NET
   - `Makefile` / `CMakeLists.txt` → C / C++
   - `cpanfile` / `Makefile.PL` → Perl
3. Note detected tech stack for use in Phase 3 and Phase 4

If no project files are found, skip detection and flag "tech stack unknown" in Phase 4.

### Phase 1: Intent Detection

Classify the user's task into one or more categories:

| Category | Signal Words | Example |
|----------|-------------|---------|
| New Feature | build, create, add, implement | "Build a login page" |
| Bug Fix | fix, broken, not working, error | "Fix the auth flow" |
| Refactor | refactor, clean up, restructure | "Refactor the API layer" |
| Research | how to, what is, explore, investigate | "How to add SSO" |
| Testing | test, coverage, verify | "Add tests for the cart" |
| Review | review, audit, check | "Review my PR" |
| Documentation | document, update docs | "Update the API docs" |
| Infrastructure | deploy, CI, docker, database | "Set up CI/CD pipeline" |
| Design | design, architecture, plan | "Design the data model" |

### Phase 2: Scope Assessment

If Phase 0 detected a project, use codebase size as a signal. Otherwise, estimate from the prompt description alone and mark the estimate as uncertain.

| Scope | Heuristic | Orchestration |
|-------|-----------|---------------|
| TRIVIAL | Single file, < 50 lines | Direct execution |
| LOW | Single component or module | Single command or skill |
| MEDIUM | Multiple components, same domain | Command chain + verify |
| HIGH | Cross-domain, 5+ files | Plan first, then phased execution |
| EPIC | Multi-session, multi-PR, architectural shift | Blueprint skill for multi-session plan |

### Phase 3: Component Matching

Map intent + scope + tech stack (from Phase 0) to specific workflow components.

#### By Intent Type

| Intent | Workflow Steps |
|--------|--------------|
| New Feature | Plan → TDD → Code Review → Verify |
| Bug Fix | Write failing test → Fix to green → Verify |
| Refactor | Refactor → Code Review → Verify |
| Research | Search first → Plan based on findings |
| Testing | TDD → E2E for critical flows → Coverage check |
| Review | Code Review → Security Review |
| Documentation | Update docs → Update codemaps |
| Infrastructure | Plan → Verify |
| Design (MEDIUM-HIGH) | Plan first |
| Design (EPIC) | Use blueprint skill |

#### By Tech Stack

| Tech Stack | Skills to Add |
|------------|--------------|
| Python / Django | django-patterns, django-tdd, django-security, python-patterns |
| Go | golang-patterns, golang-testing |
| Spring Boot / Java | springboot-patterns, springboot-tdd, springboot-security, jpa-patterns |
| TypeScript / React | frontend-patterns, backend-patterns |
| Swift / iOS | swiftui-patterns, swift-concurrency |
| PostgreSQL | postgres-patterns, database-migrations |
| Other / Unlisted | language-agnostic coding standards |

### Phase 4: Missing Context Detection

Scan the prompt for missing critical information:

- [ ] **Tech stack** — Detected in Phase 0, or must user specify?
- [ ] **Target scope** — Files, directories, or modules mentioned?
- [ ] **Acceptance criteria** — How to know the task is done?
- [ ] **Error handling** — Edge cases and failure modes addressed?
- [ ] **Security requirements** — Auth, input validation, secrets?
- [ ] **Testing expectations** — Unit, integration, E2E?
- [ ] **Performance constraints** — Load, latency, resource limits?
- [ ] **UI/UX requirements** — Design specs, responsive, a11y? (if frontend)
- [ ] **Database changes** — Schema, migrations, indexes? (if data layer)
- [ ] **Existing patterns** — Reference files or conventions to follow?
- [ ] **Scope boundaries** — What NOT to do?

**If 3+ critical items are missing**, ask the user up to 3 clarification questions before generating the optimized prompt. Then incorporate the answers into the optimized prompt.

### Phase 5: Workflow & Model Recommendation

Determine where this prompt sits in the development lifecycle:

```
Research → Plan → Implement (TDD) → Review → Verify → Commit
```

For MEDIUM+ tasks, always start with planning. For EPIC tasks, use a blueprint skill.

**Model recommendation** (include in output):

| Scope | Recommended Model | Rationale |
|-------|------------------|-----------|
| TRIVIAL-LOW | Sonnet 4.6 | Fast, cost-efficient for simple tasks |
| MEDIUM | Sonnet 4.6 | Best coding model for standard work |
| HIGH | Sonnet 4.6 (main) + Opus 4.6 (planning) | Opus for architecture, Sonnet for implementation |
| EPIC | Opus 4.6 (blueprint) + Sonnet 4.6 (execution) | Deep reasoning for multi-session planning |

**Multi-prompt splitting** (for HIGH/EPIC scope):

For tasks that exceed a single session, split into sequential prompts:
- Prompt 1: Research + Plan (use search-first approach, then plan)
- Prompt 2-N: Implement one phase per prompt (each ends with verify)
- Final Prompt: Integration test + code review across all phases

---

## Output Format

Present your analysis in this exact structure. Respond in the same language as the user's input.

### Section 1: Prompt Diagnosis

**Strengths:** List what the original prompt does well.

**Issues:**

| Issue | Impact | Suggested Fix |
|-------|--------|---------------|
| (problem) | (consequence) | (how to fix) |

**Needs Clarification:** Numbered list of questions the user should answer. If Phase 0 auto-detected the answer, state it instead of asking.

### Section 2: Recommended Workflow Components

| Type | Component | Purpose |
|------|-----------|---------|
| Step | /plan | Plan architecture before coding |
| Skill | tdd-workflow | TDD methodology guidance |
| Model | Sonnet 4.6 | Recommended for this scope |

### Section 3: Optimized Prompt — Full Version

Present the complete optimized prompt inside a single fenced code block. The prompt must be self-contained and ready to copy-paste. Include:
- Clear task description with context
- Tech stack (detected or specified)
- Workflow step invocations at the right stages
- Acceptance criteria
- Verification steps
- Scope boundaries (what NOT to do)

### Section 4: Optimized Prompt — Quick Version

A compact version for experienced users. Vary by intent type:

| Intent | Quick Pattern |
|--------|--------------|
| New Feature | Plan [feature]. TDD to implement. Code review. Verify. |
| Bug Fix | Write failing test for [bug]. Fix to green. Verify. |
| Refactor | Refactor [scope]. Code review. Verify. |
| Research | Search [topic]. Plan based on findings. |
| Testing | TDD [module]. E2E for critical flows. Coverage check. |
| Review | Code review. Then security review. |
| Docs | Update docs. Update codemaps. |
| EPIC | Use blueprint skill for "[objective]". Execute phases with verify gates. |

### Section 5: Enhancement Rationale

| Enhancement | Reason |
|-------------|--------|
| (what was added) | (why it matters) |

### Footer

> Not what you need? Tell me what to adjust, or make a normal task request if you want execution instead of prompt optimization.

---

## Examples

### Trigger Examples

- "Optimize this prompt for Claude Code"
- "Rewrite this prompt so Claude Code uses the right commands"
- "How should I prompt for this task?"
- "Help me write a better prompt for building a login page"

### Example 1: Vague Prompt (Project Detected)

**User input:**
```
Write a user login page
```

**Phase 0 detects:** `package.json` with Next.js 15, TypeScript, Tailwind CSS

**Optimized Prompt (Full):**
```
Using the project's existing stack (Next.js 15 + TypeScript + Tailwind CSS), implement a user login page.

Requirements:
- Follow existing component structure and routing conventions
- Form validation using the project's existing validation approach (check for Zod/Yup)
- Auth: follow existing auth pattern (default JWT if none present)
- Include: email/password form, form validation, error messaging, loading states, responsive layout

Workflow:
1. Plan component structure and auth flow, referencing existing page patterns
2. TDD: write unit tests for login form and integration tests for auth flow
3. Implement the login page and auth logic
4. Code review
5. Verify all tests pass and page renders correctly

Security requirements:
- Passwords not sent in plaintext
- Rate limiting against brute force
- XSS protection
- CSRF token

Acceptance criteria:
- All tests pass, 80%+ coverage
- Page renders correctly on mobile and desktop
- Successful login routes to dashboard; failure shows error message

Do not:
- Implement registration page
- Implement forgot password
- Modify existing routing structure
```

### Example 2: EPIC Project

**User input:**
```
Migrate our monolith to microservices
```

**Optimized Prompt (Full):**
```
Use the blueprint skill to plan: "Migrate monolith to microservices architecture"

Before executing, answer these questions in the blueprint:
1. Which domain boundaries exist in the current monolith?
2. Which service should be extracted first (lowest coupling)?
3. Communication pattern: REST APIs, gRPC, or event-driven?
4. Database strategy: shared DB initially or database-per-service from start?
5. Deployment target: Kubernetes, Docker Compose, or serverless?

The blueprint should produce phases:
- Phase 1: Identify service boundaries and create domain map
- Phase 2: Set up infrastructure (API gateway, service mesh, CI/CD per service)
- Phase 3: Extract first service (strangler fig pattern)
- Phase 4: Verify with integration tests, then extract next service
- Phase N: Decommission monolith

Each phase = 1 PR, with verify gates between phases.

Recommended: Opus 4.6 for blueprint planning, Sonnet 4.6 for phase execution.
```

---

## Related Skills

- `search-first` — Research phase in optimized prompts
- `strategic-compact` — Long session context management
- `cost-aware-llm-pipeline` — Token optimization recommendations
