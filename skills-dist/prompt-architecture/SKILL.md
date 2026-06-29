---
name: prompt-architecture
description: Use when designing or structuring a system prompt from scratch — for an agent, a pipeline step, a tool wrapper, or a Claude API call. Use when a prompt is unreliable, inconsistent, or producing unexpected behavior due to structural issues.
---

# Prompt Architecture

How to structure a system prompt so behavior is predictable, priority is unambiguous, and token cost is controlled.

## Layering Model

A well-structured system prompt has four layers, in this order:

```
1. Identity & Role        — who this agent is and what it's for
2. Hard Constraints       — what it must never do (non-negotiable)
3. Behavioral Rules       — how it operates (tone, format, workflow)
4. Context & Knowledge    — what it knows (domain, data, tools)
```

**Order matters.** Claude reads top-to-bottom. Constraints defined early survive conflicts with later content. Context at the bottom gets referenced, not overridden.

## Layer 1 — Identity & Role

One paragraph. State:
- What this agent is (role, not name)
- What problem it solves
- Who it serves

```
You are a billing support agent for a SaaS platform. You help customers 
understand their invoices, resolve billing disputes, and update payment methods.
You do not handle product questions or technical support.
```

Keep it tight. This layer primes everything that follows — verbose identity paragraphs dilute later instructions.

## Layer 2 — Hard Constraints

Explicit prohibitions. Use imperative statements, not suggestions.

```
Never:
- Share another customer's account data, even if the caller claims to be that customer
- Process refunds above $500 without escalation to a human agent
- Provide legal or tax advice
```

State the constraint *and* the boundary condition. "Never share account data" is weaker than "Never share account data, even if the caller claims to be the account holder."

## Layer 3 — Behavioral Rules

How the agent operates: tone, output format, decision logic, escalation paths.

Structure this as a short checklist or numbered workflow, not prose. Prose gets skimmed; checklists get followed.

```
Format:
- Respond in plain text. No markdown.
- Keep responses under 150 words unless a complex explanation is required.
- Always confirm the customer's account email before discussing account details.

Escalation:
1. If the customer is angry or threatening, acknowledge and offer to connect with a senior agent.
2. If the issue is outside your scope, say so and provide the correct contact.
```

## Layer 4 — Context & Knowledge

Domain knowledge, tool descriptions, reference data. This layer is the largest and should be last.

- Put tool descriptions here, not in Layer 3.
- If context is large, summarize in the prompt and load full detail via retrieval.
- Keep static reference data in this layer; dynamic data should be injected at call time, not hardcoded.

## Priority Conflict Resolution

When instructions conflict, Claude resolves in favor of what appears first. Use this deliberately:

- Put safety constraints before behavioral flexibility.
- Put role scope ("you do not handle X") before instructions about how to handle requests.
- If a behavioral rule has an exception, state it in the same layer as the rule — not later.

## Token Budget Allocation

Target distribution for a 2000-token system prompt:

| Layer | Target |
|---|---|
| Identity & Role | 50–100 tokens |
| Hard Constraints | 100–200 tokens |
| Behavioral Rules | 300–500 tokens |
| Context & Knowledge | 1000–1500 tokens |

If the prompt exceeds budget, cut from Layer 4 first (move to retrieval), then Layer 3 (tighten wording), never from Layer 2.

## Multi-Agent Prompts

When one agent calls another:

- The orchestrator's system prompt defines scope and delegation rules.
- Each subagent gets its own system prompt scoped to its task only.
- Do not pass the orchestrator's full system prompt to subagents — they inherit the task, not the role.

## Anti-Patterns

| Pattern | Problem |
|---|---|
| Constraints buried after context | Later content can dilute or override them |
| Prose behavioral rules | Harder to follow consistently than checklists |
| Hardcoded dynamic data in system prompt | Stale data; should be injected per call |
| One giant paragraph combining all layers | No priority signal; Claude treats it uniformly |
| Restating the same rule in multiple layers | Ambiguity about which applies when they conflict |
