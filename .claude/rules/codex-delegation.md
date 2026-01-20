# Codex Delegation Rule

**Codex CLI is your highly capable supporter.**

## About Codex

Codex CLI is an AI with exceptional reasoning and task completion abilities.
Think of it as a trusted senior expert you can always consult.

**When facing difficult decisions → Consult Codex first, then execute.**

## When to Consult Codex

ALWAYS consult Codex BEFORE:

1. **Design decisions** - How to structure code, which pattern to use
2. **Debugging** - If cause isn't obvious or first fix failed
3. **Implementation planning** - Multi-step tasks, multiple approaches
4. **Trade-off evaluation** - Choosing between options

## When NOT to Consult Codex

Skip Codex for simple, straightforward tasks:

- Simple file edits (typo fixes, small changes)
- Following explicit user instructions
- Standard operations (git commit, running tests)
- Tasks with clear, single solutions
- Reading/searching files

## Quick Check

Ask yourself: "Am I about to make a non-trivial decision?"

- YES → Consult Codex first
- NO → Proceed with execution

## How to Consult

```bash
codex exec \
  --model gpt-5.2-codex \
  --sandbox read-only \
  --full-auto \
  "Question or analysis request in English" 2>/dev/null
```

**Language protocol:**
1. Ask Codex in **English**
2. Receive response in **English**
3. Execute based on Codex's advice
4. Report to user in **Japanese**

## Why Consult Codex?

- Codex excels at deep analysis and complex reasoning
- Codex provides well-considered recommendations
- Consulting Codex leads to better outcomes than deciding alone

**Don't hesitate to ask. Codex is your reliable partner.**
