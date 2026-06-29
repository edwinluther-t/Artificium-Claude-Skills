# The Artificium

![Skills](https://img.shields.io/badge/skills-229-f5a623)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Claude Code](https://img.shields.io/badge/Claude%20Code-skills-7c3aed)
[![Stars](https://img.shields.io/github/stars/edwinluther-t/Artificium-Claude-Skills?style=social)](https://github.com/edwinluther-t/Artificium-Claude-Skills/stargazers)

**229 production-ready Claude Code skills. One install. Zero cruft.**

A curated arsenal covering engineering, design, agents, research, content, and ops — every skill cleaned, named, and ready to trigger as `/skill-name` the moment it lands.

| | |
|---|---|
| 🧩 **229 skills** | across 6 domains |
| 🧹 **Two-field frontmatter** | `name` + `description`, nothing else |
| ⚡ **Instant triggering** | `/skill-name`, no restart |
| 📦 **Drop-in install** | one `cp`, global or per-project |

## Why this exists

Most Claude Code skills floating around are scattered across a dozen repos, inconsistent in format, and bloated with vendor lock-in, dead tool references, and author cruft that bleeds into your context window.

The Artificium fixes that. Every skill here has been stripped to pure behavioral instruction — no `metadata` blocks, no platform-locked tool names, no third-party branding. Just the workflow, the checklists, and the trigger logic that make the skill actually fire when you need it. Curated by hand, organized by what you actually do, and built to be installed once and used everywhere.

If you've ever copied a skill only to spend twenty minutes ripping out junk before it worked — this is the collection you wish you'd started with.

Created and maintained by **[Edwin Luther](https://github.com/edwinluther-t)**. Licensed under [MIT](LICENSE) — free to use, fork, and adapt. Attribution appreciated. Contributions welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

💬 Questions, ideas, or want to show what you built? Jump into [Discussions](https://github.com/edwinluther-t/Artificium-Claude-Skills/discussions).

---

## Quick start (30 seconds)

```bash
git clone https://github.com/edwinluther-t/Artificium-Claude-Skills.git
cp -r Artificium-Claude-Skills/skills-dist/* ~/.claude/skills/
```

Open Claude Code and type `/` — all 229 skills are live. That's it.

---

## Install

Each skill lives in `skills-dist/<skill-name>/SKILL.md`. Copy the contents of `skills-dist/` into your Claude Code skills directory:

**Global (available in every project):**
```bash
cp -r skills-dist/* ~/.claude/skills/
```

**Windows:**
```bash
cp -r skills-dist/* "C:/Users/<you>/.claude/skills/"
```

**Project-only (current project):**
```bash
cp -r skills-dist/* .claude/skills/
```

Once copied, skills are available immediately as `/skill-name` in Claude Code — no restart needed.

---

## Rebuild after edits

If you edit skills in `skills/`, regenerate `skills-dist/` with:

```bash
python build-dist.py
```

---

## Skills

### Agents

| Skill | What it does |
|---|---|
| `/agent-architecture-audit` | Full-stack diagnostic for agent and LLM applications. Audits the 12-layer agent stack for wrapper regression, memory pollution, tool discipline failures, hidden repair loops, and rendering corruption. |
| `/agent-eval` | Head-to-head comparison of coding agents (Claude Code, Aider, Codex, etc.) on custom tasks with pass rate, cost, time, and consistency metrics. |
| `/agent-harness-construction` | Design and optimize AI agent action spaces, tool definitions, and observation formatting for higher completion rates. |
| `/agent-introspection-debugging` | Structured self-debugging workflow for AI agent failures using capture, diagnosis, contained recovery, and introspection reports. |
| `/agent-self-evaluation` | Self-rates output on 5 axes — accuracy, completeness, clarity, actionability, conciseness — with concrete evidence per criterion. Produces a structured 1-5 scorecard with improvement suggestions. |
| `/agentic-engineering` | Operate as an agentic engineer using eval-first execution, decomposition, and cost-aware model routing. |
| `/agentic-os` | Build persistent multi-agent operating systems on Claude Code. Covers kernel architecture, specialist agents, slash commands, file-based memory, scheduled automation, and state management. |
| `/ai-first-engineering` | Engineering operating model for teams where AI agents generate a large share of implementation output. |
| `/autonomous-agent-harness` | Transform Claude Code into a fully autonomous agent system with persistent memory, scheduled operations, computer use, and task queuing. |
| `/continuous-agent-loop` | Patterns for continuous autonomous agent loops with quality gates, evals, and recovery controls. |
| `/context-budget` | Audits Claude Code context window consumption across agents, skills, MCP servers, and rules. |
| `/context-engineering` | Optimizes agent context setup — rules files, context configuration, and session quality. |
| `/cost-aware-llm-pipeline` | Cost optimization patterns for LLM API usage — model routing by task complexity, budget tracking, retry logic, and prompt caching. |
| `/cost-tracking` | Track and report Claude Code token usage, spending, and budgets from the local cost-tracker metrics log. |
| `/council` | Convene a four-voice council for ambiguous decisions, tradeoffs, and go/no-go calls. Use when multiple valid paths exist and you need structured disagreement before choosing. |
| `/dispatching-parallel-agents` | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies. |
| `/dynamic-workflow-mode` | Design task-local harnesses, eval gates, and reusable skill extraction for adaptive agent workflows. |
| `/eval-harness` | Formal evaluation framework implementing eval-driven development (EDD) principles with pass/fail criteria, pass@k metrics, and regression test suites. |
| `/gan-style-harness` | GAN-inspired Generator-Evaluator agent harness. Separates generation from evaluation in an adversarial feedback loop that drives quality beyond what a single agent achieves. |
| `/gateguard` | Fact-forcing gate that blocks destructive actions and demands concrete investigation before allowing them. Measurably improves output quality. |
| `/iterative-retrieval` | Pattern for progressively refining context retrieval — use when spawning subagents that cannot predict upfront which files they need. |
| `/knowledge-ops` | Knowledge base management, ingestion, sync, and retrieval across multiple storage layers (local files, MCP memory, vector stores, Git repos). |
| `/parallel-execution-optimizer` | Use when you want a task done much faster through parallel work, concurrent agents, batched tool calls, or isolated worktrees. |
| `/plan-orchestrate` | Read a plan document, decompose it into steps, design a per-step agent chain, and emit ready-to-paste orchestration prompts. |
| `/prompt-architecture` | Use when designing or structuring a system prompt from scratch — for an agent, a pipeline step, a tool wrapper, or a Claude API call. |
| `/prompt-optimizer` | Analyze raw prompts, identify intent and gaps, and output a ready-to-paste optimized prompt. |
| `/santa-method` | Multi-agent adversarial verification with convergence loop. Use when output will be published, deployed, or consumed by end users. |
| `/strategic-compact` | Suggests manual context compaction at logical intervals to preserve context through task phases. |
| `/subagent-driven-development` | Dispatches a fresh implementer subagent per task, reviews after each, and runs a broad whole-branch review at the end. |
| `/team-agent-orchestration` | Run team-based orchestration for agent squads using work items, ownership, agent Kanban, merge gates, and control pane handoffs. |
| `/team-builder` | Interactive agent picker for composing and dispatching parallel teams. |
| `/token-budget-advisor` | Offers an informed choice about how much response depth to consume before answering. |
| `/verification-loop` | Comprehensive verification system — run after completing a feature, before creating a PR, or after refactoring. |

---

### Engineering

#### Architecture & Core

| Skill | What it does |
|---|---|
| `/api-and-interface-design` | Guides stable API and interface design — REST, GraphQL, type contracts, and module boundaries. |
| `/api-design` | REST API design patterns including resource naming, status codes, pagination, filtering, error responses, versioning, and rate limiting. |
| `/architecture-decision-records` | Capture architectural decisions as structured ADRs during coding sessions. |
| `/codebase-onboarding` | Analyze an unfamiliar codebase and generate a structured onboarding guide with architecture map, key entry points, and a starter CLAUDE.md. |
| `/code-review-and-quality` | Multi-axis code review across multiple quality dimensions before any change enters the main branch. |
| `/code-simplification` | Simplifies code for clarity without changing behavior. |
| `/code-tour` | Create CodeTour `.tour` files — persona-targeted, step-by-step walkthroughs with real file and line anchors. |
| `/coding-standards` | Baseline cross-project coding conventions for naming, readability, immutability, and quality review. |
| `/debugging-and-error-recovery` | Systematic root-cause debugging — for failed tests, broken builds, or unexpected behavior. |
| `/deprecation-and-migration` | Manages deprecation and migration of old systems, APIs, or features. |
| `/documentation-and-adrs` | Records architectural decisions, API changes, and feature context future engineers will need. |
| `/documentation-lookup` | Fetches up-to-date library and framework docs instead of relying on training data. |
| `/doubt-driven-development` | Adversarial review of every non-trivial decision before it stands. Use when correctness matters more than speed. |
| `/error-handling` | Patterns for robust error handling across TypeScript, Python, and Go — typed errors, error boundaries, retries, circuit breakers. |
| `/incremental-implementation` | Delivers changes incrementally for any feature touching more than one file. |
| `/intent-driven-development` | Turn ambiguous product and engineering changes into scoped, verifiable acceptance criteria before implementation. |
| `/opensource-pipeline` | Safely open-source any project — fork, sanitize, and package. Strips secrets before publishing. |
| `/refactor-safely` | Restructure code without changing behavior — extracting functions, renaming, splitting files, moving modules. |
| `/repo-scan` | Cross-stack source code asset audit — classifies every file, detects embedded third-party libraries. |
| `/search-first` | Research-before-coding workflow. Search for existing tools, libraries, and patterns before writing custom code. |
| `/source-driven-development` | Grounds every implementation decision in official documentation. Authoritative, source-cited code free from outdated patterns. |
| `/spec-driven-development` | Creates specs before coding — for new projects, features, or significant changes without existing specifications. |
| `/verification-before-completion` | Requires running verification commands and confirming output before making any success claims. |

#### Backend

| Skill | What it does |
|---|---|
| `/backend-patterns` | Backend architecture patterns, API design, database optimization, and server-side best practices for Node.js, Express, and Next.js API routes. |
| `/cpp-coding-standards` | C++ coding standards based on the C++ Core Guidelines. Modern, safe, and idiomatic practices. |
| `/cpp-testing` | Writing/updating/fixing C++ tests, configuring GoogleTest/CTest, coverage, and sanitizers. |
| `/database-migrations` | Database migration best practices for schema changes, data migrations, rollbacks, and zero-downtime deployments across PostgreSQL, MySQL, and common ORMs. |
| `/dotnet-patterns` | Idiomatic C# and .NET patterns, DI, async/await, and best practices for robust .NET applications. |
| `/fullstack-dev` | Full-stack backend architecture and frontend-backend integration — REST APIs, CRUD, real-time, and production hardening. |
| `/golang-patterns` | Idiomatic Go patterns, best practices, and conventions for robust, efficient Go applications. |
| `/golang-testing` | Go testing patterns — table-driven tests, subtests, benchmarks, fuzzing, and test coverage. |
| `/java-coding-standards` | Java coding standards for Spring Boot and Quarkus services — naming, immutability, streams, reactive patterns. |
| `/latency-critical-systems` | For latency-sensitive systems — realtime dashboards, market data, streaming agents, execution gateways. |
| `/nestjs-patterns` | NestJS architecture patterns — modules, controllers, DTOs, guards, interceptors, config, and production-grade TypeScript backends. |
| `/nuxt4-patterns` | Nuxt 4 app patterns for hydration safety, performance, route rules, and SSR-safe data fetching. |
| `/python-patterns` | Pythonic idioms, PEP 8, type hints, and best practices for robust, efficient Python applications. |
| `/python-testing` | Python testing with pytest — TDD, fixtures, mocking, parametrization, and coverage. |
| `/redis-patterns` | Redis data structure patterns, caching strategies, distributed locks, rate limiting, pub/sub, and connection management. |
| `/regex-vs-llm-structured-text` | Decision framework for choosing between regex and LLM when parsing structured text. |
| `/rust-patterns` | Idiomatic Rust — ownership, error handling, traits, concurrency, and best practices for safe, performant applications. |
| `/rust-testing` | Rust testing — unit tests, integration tests, async testing, property-based testing, mocking, and coverage. |
| `/tsdown` | Bundle TypeScript and JavaScript libraries with Rolldown. Library builds, type declarations, multiple formats. |
| `/turborepo` | Turborepo monorepo build system — tasks/pipelines, packages, cache debugging, CI optimization. |

#### Frontend

| Skill | What it does |
|---|---|
| `/a11y-audit` | Audit a UI or design against WCAG 2.2 AA/AAA and ARIA patterns — contrast, keyboard/screen-reader review, POUR. |
| `/accessibility` | Design, implement, and audit inclusive digital products using WCAG 2.2 Level AA standards. |
| `/angular-developer` | Angular code and architectural guidance — signals, forms, DI, routing, SSR, ARIA, animations, Tailwind. |
| `/browser-qa` | Automate visual testing and UI interaction verification using browser automation. |
| `/browser-testing-with-devtools` | Tests in real browsers via Chrome DevTools MCP — DOM inspection, console errors, network analysis, performance profiling. |
| `/click-path-audit` | Trace every user-facing button through its full state change sequence to find bugs where functions cancel each other out. |
| `/e2e-testing` | Playwright E2E testing patterns, Page Object Model, CI/CD integration, artifact management, and flaky test strategies. |
| `/frontend-a11y` | Accessibility patterns for React and Next.js — semantic HTML, ARIA, form labeling, keyboard navigation, focus management. |
| `/frontend-patterns` | Frontend development patterns for React, Next.js, state management, performance optimization, and UI best practices. |
| `/frontend-ui-engineering` | Builds production-quality UIs — components, layouts, state, interaction — that look and feel production-quality. |
| `/performance` | Optimize UI performance against Core Web Vitals — LCP, INP, CLS — loading strategy, layout-shift prevention, animation performance. |
| `/performance-optimization` | Application performance — profiling, bottleneck fixing, Core Web Vitals, load time improvement. |
| `/react-native-dev` | React Native and Expo — components, styling, animations, navigation, state, performance, testing, and deployment. |
| `/react-patterns` | React 18/19 — hooks discipline, server/client boundaries, Suspense, form actions, data fetching, accessibility. |
| `/react-performance` | React and Next.js performance — waterfalls, bundle size, server-side, re-render, rendering, and JS micro-perf. |
| `/react-testing` | React component testing with React Testing Library, Vitest/Jest, MSW, axe, and E2E decision boundary. |
| `/webapp-testing` | Playwright-based testing for local web applications — frontend verification, UI debugging, screenshots, browser logs. |

#### Data & ML

| Skill | What it does |
|---|---|
| `/ai-regression-testing` | Regression testing strategies for AI-assisted development — sandbox API testing and patterns to catch AI blind spots. |
| `/data-scraper-agent` | Build a fully automated AI-powered data collection agent for any public source — scheduled, enriched, stored. |
| `/data-throughput-accelerator` | Large data ingestion, backfill, export, ETL, warehouse loading — much faster while preserving data correctness. |
| `/ml-adoption-playbook` | End-to-end methodology for adding machine learning to existing non-ML codebases. |
| `/mle-workflow` | Production ML engineering — data contracts, reproducible training, model evaluation, deployment, monitoring, rollback. |
| `/recsys-pipeline-architect` | Design composable recommendation, ranking, and feed pipelines — social feeds, RAG rerankers, notification triage. |
| `/sql-query-management` | Writing, reviewing, and optimizing SQL — DDL, DML, migrations, stored procedures, schema design, query performance. |

#### Infra & Mobile

| Skill | What it does |
|---|---|
| `/android-clean-architecture` | Clean Architecture for Android and Kotlin Multiplatform — module structure, dependency rules, UseCases, Repositories. |
| `/android-native-dev` | Android native development — Material Design 3, Kotlin/Compose, accessibility, and build troubleshooting. |
| `/benchmark` | Measure performance baselines, detect regressions, and compare stack alternatives. |
| `/benchmark-optimization-loop` | Recursive optimization loop — many variants, benchmark latency/throughput/cost, choose the best implementation. |
| `/canary-watch` | Monitor and verify a deployed URL after releases — HTTP endpoints, SSE streams, assets, console errors. |
| `/ci-cd-and-automation` | Automates CI/CD pipeline setup — build pipelines, quality gates, test runners, deployment strategies. |
| `/dashboard-builder` | Build monitoring dashboards that answer real operator questions for Grafana, SigNoz, and similar platforms. |
| `/deployment-patterns` | Deployment workflows, CI/CD patterns, Docker containerization, health checks, rollback strategies. |
| `/flox-environments` | Reproducible, cross-platform development environments with Flox (Nix-based). |
| `/flutter-dev` | Flutter cross-platform — widget patterns, Riverpod/Bloc, GoRouter, performance, and platform-specific implementations. |
| `/ios-application-dev` | iOS development covering UIKit, SnapKit, SwiftUI, touch targets, navigation, Dynamic Type, Dark Mode, accessibility. |
| `/kubernetes-patterns` | Kubernetes workload patterns, resource management, RBAC, probes, autoscaling, and kubectl debugging. |
| `/observability-and-instrumentation` | Instruments code for production visibility — logging, metrics, tracing, alerting. |
| `/shipping-and-launch` | Pre-launch checklist, monitoring setup, staged rollout planning, and rollback strategy. |
| `/terminal-ops` | Evidence-first repo execution — run commands, debug CI failures, and push narrow fixes with verified output. |

#### Security & Testing

| Skill | What it does |
|---|---|
| `/production-audit` | Local-evidence production readiness audit for shipped apps, pre-launch reviews, and post-merge checks. |
| `/safety-guard` | Prevent destructive operations when working on production systems or running agents autonomously. |
| `/security-and-hardening` | Hardens code against vulnerabilities — user input, authentication, data storage, external integrations. |
| `/security-bounty-hunter` | Hunt for exploitable, bounty-worthy security issues in repositories — remotely reachable vulnerabilities. |
| `/test-driven-development` | Drives development with tests — implementing logic, fixing bugs, or changing behavior. |

---

### Design

#### Visual & Aesthetic

| Skill | What it does |
|---|---|
| `/apply-aesthetic` | Apply a visual direction — an archetype or one of 138 named design systems (Apple, Linear, Stripe, Vercel, Notion, Material, shadcn, Spotify, Tesla…) — by resolving it into the token system. |
| `/design-taste-frontend` | Senior UI/UX Engineer skill. Enforces metric-based rules, strict component architecture, CSS hardware acceleration, and balanced design engineering. |
| `/frontend-design` | Guidance for distinctive, intentional visual design — aesthetic direction, typography, and choices that don't read as templated defaults. |
| `/high-end-visual-design` | Teaches the exact fonts, spacing, shadows, card structures, and animations that make a website feel expensive. Blocks common defaults that make AI designs look cheap. |
| `/industrial-brutalist-ui` | Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics. For data-heavy dashboards or editorial sites that need to feel like declassified blueprints. |
| `/make-interfaces-feel-better` | Apply concrete design-engineering details that make interfaces feel polished — spacing, typography, shadows, motion, hit areas. |
| `/minimalist-ui` | Clean editorial-style interfaces. Warm monochrome palette, typographic contrast, flat bento grids, muted pastels. |
| `/redesign` | Upgrade an existing website or app to premium quality — audit the current design, identify generic AI tells, apply taste and system rules surgically. |
| `/ui-ux-pro-max` | UI/UX design intelligence for web and mobile. 50+ styles, 161 color palettes, 57 font pairings, 99 UX guidelines, and 25 chart types across 10 stacks. |

#### Design Systems

| Skill | What it does |
|---|---|
| `/brandkit` | Generate a complete, accessible brand design system from a brief — primitive → semantic → component DTCG tokens, light + dark, theme.css — verified for WCAG. |
| `/design-system` | Token architecture, component specifications, and slide generation. Three-layer tokens, CSS variables, spacing/typography scales. |
| `/design-tokens` | Generate, extend, or audit design tokens in DTCG format with the 3-tier architecture. Colors, typography, spacing, shadows, borders, motion, theming. |
| `/figma-integration` | Keep Figma and code in sync — map DTCG tokens to Figma Variables, sync in either direction, verify component parity. |
| `/governance` | Govern design system evolution — SemVer for tokens/components, contribution workflow, deprecation policy, change communication. |
| `/migrate-design-system` | Map this token system to or from any external design system (Material Design 3, Apple HIG, Fluent, Carbon, shadcn/ui, Radix, Chakra…). |
| `/theme-factory` | Style artifacts with a theme — slides, docs, HTML landing pages. 10 pre-set themes or generate a new one on-the-fly. |
| `/token-build` | Set up or run the token build pipeline — transform DTCG tokens into platform artifacts (CSS variables, Tailwind, JS/TS, iOS, Android, Compose). |

#### Components & Code

| Skill | What it does |
|---|---|
| `/design-code` | Generate production-ready, accessible, token-driven component code for any framework — React, Next.js, SwiftUI, Vue, Svelte, Angular, React Native, Flutter, and more. |
| `/design-component` | Design a UI component spec — anatomy, variants, sizes, 8 states, token mapping, and accessibility — before or alongside code. |
| `/design-qa` | Set up or run design QA gates — token lint, automated a11y (axe), contrast, visual regression across variants/states/themes/RTL. |
| `/design-review` | Review or audit a design across 6 weighted dimensions with Nielsen's 10 heuristics and a prioritized findings table. |
| `/image-to-code` | Turn a reference image or screenshot into token-driven, accessible code — infer the design system, map to 3-tier tokens, rebuild, verify. |
| `/prototype` | Move an idea up the fidelity ladder (content-first → wireframe → low-fi → high-fi → code) with a validation plan at each level. |
| `/ui-styling` | Beautiful, accessible UIs with shadcn/ui, Radix, and Tailwind — themes, dark mode, responsive layouts, accessible components. |
| `/ux-writing` | Write or review UI copy — buttons, errors, empty states, microcopy, notifications — using the voice & tone system. |

#### Assets & Media

| Skill | What it does |
|---|---|
| `/banner-design` | Design banners for social media, ads, website heroes, creative assets, and print. Multiple art direction options per request. |
| `/frontend-slides` | Create zero-dependency, animation-rich HTML presentations from scratch or by converting PowerPoint files. |
| `/motion-advanced` | Advanced motion patterns for React/Next.js — drag & drop, gestures, text animations, SVG path drawing, custom hooks. |
| `/motion-foundations` | Motion tokens, spring presets, performance rules, device adaptation, and accessibility enforcement for React/Next.js. |
| `/motion-patterns` | Production-ready animation patterns — button, modal, toast, stagger, page transitions, exit animations, scroll, and layout. |
| `/remotion-video-creation` | GLSL shader techniques and Remotion best practices — ray marching, SDF modeling, fluid simulation, particle systems. |
| `/shader-dev` | Comprehensive GLSL shader techniques for stunning visual effects — ray marching, SDF modeling, fluid simulation, procedural generation. |
| `/slides` | Create strategic HTML presentations with Chart.js, design tokens, responsive layouts, and copywriting formulas. |
| `/slidev` | Web-based slidedecks for developers using Slidev — Markdown, Vue components, code highlighting, animations. |
| `/video-editing` | AI-assisted video editing — cutting, structuring, augmenting footage with FFmpeg, Remotion, ElevenLabs, fal.ai. |
| `/web-artifacts-builder` | Suite of tools for creating elaborate, multi-component HTML artifacts using React, Tailwind CSS, and shadcn/ui. |
| `/web-asset-generator` | Generate web assets — favicons, PWA app icons, and social media meta images (Open Graph) for all major platforms. |

#### Design Orchestration

| Skill | What it does |
|---|---|
| `/design` | Unified design skill covering brand identity, design tokens, UI styling, logo design, corporate identity, HTML presentations, banners, icons, and social images. |
| `/design-router` | Automatically routes to the best UI/UX design skills based on project type, industry, and aesthetic requirements. |

---

### Content & Brand

| Skill | What it does |
|---|---|
| `/article-writing` | Write articles, guides, blog posts, tutorials, and long-form content in a distinctive voice derived from supplied examples or brand guidance. |
| `/brand` | Brand voice, visual identity, messaging frameworks, asset management, and brand consistency. |
| `/brand-discovery` | Discover or articulate brand identity through structured multi-session interviews across 8 modules — purpose, positioning, audience, personality, voice, and narrative. |
| `/brand-voice` | Build a source-derived writing style profile from real posts and copy, then reuse that profile across content, outreach, and social workflows. |
| `/competitive-ads-extractor` | Extract and analyze competitors' ads from ad libraries (Facebook, LinkedIn) to understand what messaging and creative approaches are working. |
| `/content-engine` | Create platform-native content systems for X, LinkedIn, TikTok, YouTube, newsletters, and multi-platform campaigns. |
| `/content-research-writer` | Research-assisted content writing — citations, improved hooks, outline iteration, and real-time section feedback. |
| `/doc-coauthoring` | Structured workflow for co-authoring documentation, proposals, technical specs, and decision docs. |
| `/investor-materials` | Create and update pitch decks, one-pagers, investor memos, accelerator applications, and financial models. |
| `/investor-outreach` | Draft cold emails, warm intro blurbs, follow-ups, and investor communications for fundraising. |
| `/lead-research-assistant` | Identify high-quality leads by analyzing your business, searching for target companies, and providing actionable contact strategies. |
| `/marketing-campaign` | End-to-end marketing campaign planning — audience research, positioning, landing page copy, email sequences, social posts, ad copy, content calendars. |
| `/seo` | Audit, plan, and implement SEO improvements — technical SEO, on-page optimization, structured data, Core Web Vitals, and content strategy. |

---

### Research

| Skill | What it does |
|---|---|
| `/competitive-platform-analysis` | Scope a competitive landscape — identify, categorize, and score-filter a competitor set before any benchmarking begins. First step in the three-skill competitive pipeline. |
| `/competitive-report-structure` | Assemble competitive findings into a decision-grade report — landscape map, competitor profiles, benchmarking matrix, white-space analysis, strategic recommendations. |
| `/deep-research` | Multi-source deep research using web research tools — synthesizes findings and delivers cited reports. |
| `/literature-review` | Systematic literature-review workflow for academic, biomedical, technical, and scientific topics. |
| `/market-research` | Conduct market research, competitive analysis, investor due diligence, and industry intelligence with source attribution. |
| `/research-ops` | Evidence-first current-state research workflow for fresh facts, comparisons, enrichment, or recommendations from current public evidence. |
| `/scholar-evaluation` | Structured evaluation for papers, proposals, literature reviews, methods sections, evidence quality, and citation support. |
| `/social-graph-ranker` | Weighted social-graph ranking for warm intro discovery, bridge scoring, and network gap analysis across X and LinkedIn. |

---

### Ops

#### Git & Project

| Skill | What it does |
|---|---|
| `/after-action-review` | Capture what happened, what broke, and what to carry forward after completing a significant task, feature, incident, or session. |
| `/blueprint` | High-level planning and project structuring. |
| `/brainstorming` | Explores user intent, requirements, and design before implementation. Use before any creative work. |
| `/changelog-generator` | Automatically creates user-facing changelogs from git commits — transforms technical commits into customer-friendly release notes. |
| `/context-handoff` | Prepare a summary so a future Claude session can pick up without drift, repeated questions, or lost decisions. |
| `/executing-plans` | Execute a written implementation plan in a separate session with review checkpoints. |
| `/finishing-a-development-branch` | Guides completion of development work — merge, PR, or cleanup decisions when implementation is done and tests pass. |
| `/git-workflow` | Git workflow patterns — branching strategies, commit conventions, merge vs rebase, conflict resolution, collaborative development. |
| `/git-workflow-and-versioning` | Structures git workflow practices for committing, branching, resolving conflicts, and organizing parallel work streams. |
| `/github-ops` | GitHub repository operations — issues, PRs, CI status, releases, contributors, stale items, and automation. |
| `/idea-refine` | Refine raw ideas into sharp, actionable concepts through structured divergent and convergent thinking. |
| `/incident-commit` | Commit fixes, rollbacks, or investigation changes under time pressure during or after an incident while preserving investigation trail. |
| `/planning-and-task-breakdown` | Break work into ordered, implementable tasks from a spec or clear requirements. |
| `/product-capability` | Translate PRD intent and roadmap asks into an implementation-ready capability plan before multi-service work starts. |
| `/product-lens` | Validate the "why" before building — run product diagnostics and pressure-test product direction. |
| `/spec-driven-development` | Creates specs before coding when requirements are unclear, ambiguous, or only exist as a vague idea. |
| `/using-git-worktrees` | Start feature work in isolation via git worktrees before executing implementation plans. |
| `/writing-plans` | Write a spec or requirements plan for a multi-step task before touching code. |

#### Communications & Documents

| Skill | What it does |
|---|---|
| `/docx` | Create, read, edit, or manipulate Word documents — formatted docs with tables of contents, headings, page numbers, or letterheads. |
| `/email-ops` | Evidence-first mailbox triage, drafting, send verification, and sent-mail-safe follow-up workflow. |
| `/internal-comms` | Write all kinds of internal communications — status reports, leadership updates, incident reports, project updates, FAQs, and newsletters. |
| `/interview-me` | Extracts what you actually want instead of what you think you should want — one-question-at-a-time interview until 95% confidence about the underlying intent. |
| `/meeting-insights-analyzer` | Analyze meeting transcripts to uncover behavioral patterns, communication insights, and actionable feedback. |
| `/pdf` | Read, extract, merge, split, rotate, watermark, create, fill, encrypt, decrypt PDFs, and OCR scanned documents. |
| `/pptx` | Create, read, edit, combine, split, or manipulate PowerPoint presentations — slide decks, pitch decks, templates, speaker notes. |
| `/tailored-resume-generator` | Analyze job descriptions and generate tailored resumes that highlight relevant experience and maximize interview chances. |
| `/xlsx` | Open, read, edit, create, clean, or convert spreadsheets — .xlsx, .xlsm, .csv, .tsv — formulas, charts, formatting. |

---

### Skills Meta

| Skill | What it does |
|---|---|
| `/automation-audit-ops` | Evidence-first automation inventory and overlap audit — which jobs, hooks, connectors, MCP servers, or wrappers are live, broken, redundant, or missing. |
| `/claude-api` | Build LLM-powered applications with Claude — single calls, workflows, tool use, and managed agents across Python, TypeScript, Go, Java, Ruby, C#, PHP. |
| `/config-gc` | Garbage collection for your Claude Code configuration — scans ~/.claude for redundant, stale, or low-value items and walks you through cleanup. |
| `/install-skill` | Deploy a skill from this collection into a Claude Code environment — globally, per-project, or for a specific user. |
| `/mcp-builder` | Create high-quality MCP (Model Context Protocol) servers to integrate external APIs and services — Python (FastMCP) or TypeScript. |
| `/rules-distill` | Scan skills to extract cross-cutting principles and distill them into rules files. |
| `/skill-comply` | Visualize whether skills, rules, and agent definitions are actually followed — auto-generates scenarios, runs agents, reports compliance rates. |
| `/skill-creator` | Create new skills, modify existing skills, run evals, benchmark performance, and optimize skill descriptions for better triggering. |
| `/skill-router` | Resolve skill selection conflicts and identify the right skill for a given request without loading all of them. |
| `/skill-scout` | Search existing local, marketplace, GitHub, and web skill sources before creating a new skill. |
| `/skill-stocktake` | Audit Claude skills for quality — Quick Scan (changed skills only) or Full Stocktake with sequential batch evaluation. |
| `/using-superpowers` | Establishes how to find and use skills at the start of any conversation. |
| `/writing-skills` | Create new skills, edit existing skills, or verify skills work before deployment. |

---

## Contributing

Found a gap? Built a skill worth sharing? Spotted something broken? Contributions
are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md) for the skill format and PR flow.
Every merged skill makes the collection sharper for everyone.

## License

[MIT](LICENSE) — use freely, fork it, build on it. Attribution appreciated, never required.

---

<sub>Built and maintained by [Edwin Luther](https://github.com/edwinluther-t). If The Artificium saves you time, a ⭐ helps others find it.</sub>
