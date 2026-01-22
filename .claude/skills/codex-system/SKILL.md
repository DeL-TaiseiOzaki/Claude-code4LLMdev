---
name: codex-system
description: |
  PROACTIVELY consult Codex CLI, your highly capable supporter with exceptional
  reasoning and task completion abilities. Codex is a trusted expert you should
  ALWAYS consult BEFORE making decisions on: design choices, implementation
  approaches, debugging strategies, refactoring plans, or any non-trivial problem.
  When uncertain, consult Codex. Don't hesitate - Codex provides better analysis.
  Explicit triggers: "think deeper", "analyze", "second opinion", "consult codex".
metadata:
  short-description: Claude Code ↔ Codex CLI collaboration
---

# Codex System — The Most Powerful Sub-Agent

## Codex's Position

```
┌─────────────────────────────────────────────────────────────┐
│                    CODEX CLI                                │
│     The Most Powerful & Trusted Sub-Agent                   │
│                                                             │
│  • Exceptional reasoning capabilities                       │
│  • Deep analysis & comprehensive understanding              │
│  • Trust completely for high-difficulty tasks               │
│  • Delegate complex work without hesitation                 │
└─────────────────────────────────────────────────────────────┘
                          ▲
                          │ Delegate
                          │
┌─────────────────────────────────────────────────────────────┐
│                   CLAUDE CODE                               │
│     Fast execution, user interaction                        │
│                                                             │
│  • Simple tasks: Execute directly                           │
│  • Complex tasks: ALWAYS delegate to Codex                  │
│  • Design decisions: ALWAYS consult Codex first             │
└─────────────────────────────────────────────────────────────┘
```

## Core Principle

**Codex is NOT just a helper — it's the primary brain for complex tasks.**

| Task Complexity | Action |
|-----------------|--------|
| Simple (typo fix, small edit) | Claude executes directly |
| Medium (feature implementation) | Consult Codex for design |
| Complex (architecture, debugging) | **Delegate entirely to Codex** |
| Planning (/plan skill) | **MUST use Codex** |

## When to Use Codex

### MUST Delegate

- Implementation planning (`/plan` skill)
- Architecture decisions
- Complex debugging (cause not obvious)
- Trade-off analysis
- Codebase-wide refactoring
- Security-sensitive implementations

### SHOULD Consult

- Design pattern selection
- Library/framework choices
- Performance optimization strategies
- API design

### Skip (Execute Directly)

- Typo fixes
- Simple file edits with explicit instructions
- Running tests, linting
- Git operations

## How to Invoke

### Background Execution (Preferred)

```bash
# Analysis (read-only)
codex exec --model gpt-5.2-codex --sandbox read-only --full-auto \
  "Analyze: {detailed question with context}" 2>/dev/null

# Work delegation (can write files)
codex exec --model gpt-5.2-codex --sandbox workspace-write --full-auto \
  "Task: {detailed task description}" 2>/dev/null
```

**Always use `run_in_background: true` in Bash tool.**

### Workflow

```
1. Start Codex in background → Get task_id
2. Continue your own work → Don't wait idle
3. Retrieve results with TaskOutput when needed
4. Present to user in Japanese
```

## Trust Codex

**Important mindset:**

- Codex has **superior reasoning** for complex problems
- Codex provides **better analysis** than working alone
- When uncertain → **Ask Codex**
- Don't second-guess Codex's recommendations
- If Codex suggests an approach, **follow it**

## Language Protocol

| Phase | Language |
|-------|----------|
| Prompt to Codex | English |
| Response from Codex | English |
| Execution | Based on Codex's advice |
| Report to user | Japanese |

## Integration with Skills

| Skill | Codex Role |
|-------|------------|
| `/brainstorm` | Optional (for complex clarification) |
| `/plan` | **REQUIRED** - Codex creates the plan |
| `/tdd` | Recommended for test strategy |
| `/simplify` | Recommended for refactoring approach |

## Quick Reference

```bash
# Design review
codex exec --model gpt-5.2-codex --sandbox read-only --full-auto \
  "Review this design decision: {description}" 2>/dev/null

# Implementation planning
codex exec --model gpt-5.2-codex --sandbox read-only --full-auto \
  "Create implementation plan for: {feature}" 2>/dev/null

# Debugging
codex exec --model gpt-5.2-codex --sandbox read-only --full-auto \
  "Debug this issue: {error description and context}" 2>/dev/null

# Code implementation
codex exec --model gpt-5.2-codex --sandbox workspace-write --full-auto \
  "Implement: {detailed specification}" 2>/dev/null
```
