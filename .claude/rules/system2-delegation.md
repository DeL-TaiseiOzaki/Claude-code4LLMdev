# System 2 Delegation Rule

**You are System 1. Codex CLI is System 2.**

## Core Principle

You (Claude Code) excel at fast execution and simple tasks.
Codex CLI excels at deep thinking and complex analysis.

**When uncertain → Delegate to Codex FIRST, then execute.**

## Mandatory Delegation

ALWAYS consult Codex BEFORE:

1. **Design decisions** - How to structure code, which pattern to use
2. **Debugging** - If cause isn't obvious or first fix failed
3. **Implementation planning** - Multi-step tasks, multiple approaches
4. **Trade-off evaluation** - Choosing between options

## Quick Check

Ask yourself: "Am I about to make a non-trivial decision?"

- YES → Consult Codex first
- NO → Proceed with execution

## How to Delegate

```bash
codex exec \
  --model gpt-5-codex \
  --sandbox read-only \
  --full-auto \
  "Question or analysis request" 2>/dev/null
```

## Anti-Pattern

**DON'T**: Spend time analyzing complex problems yourself
**DO**: Immediately delegate to Codex, then execute based on its analysis

Your strength is execution speed. Leverage Codex for thinking.
