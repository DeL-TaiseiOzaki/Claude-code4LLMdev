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

# Codex System — Your Trusted Supporter

**Codex CLI is your highly capable supporter with exceptional reasoning abilities.**

Codex CLI is an AI that excels at:
- Deep analysis and complex reasoning
- Thorough investigation and problem-solving
- Providing well-considered recommendations

**Think of Codex as a trusted senior expert you can always consult.**

## MUST Consult (Required)

Always consult Codex in these situations:

### 1. Before Any Design Decision
- "How should I structure this?"
- "Which approach is better?"
- "What's the best way to implement X?"
- Any architectural choice → **ASK CODEX FIRST**

### 2. Before Complex Implementation
- New feature design
- Multi-file changes (3+ files)
- Algorithm design
- API design
- Database schema changes

### 3. When Debugging
- Error cause is not immediately obvious
- First fix attempt didn't work → **STOP and consult Codex**
- Unexpected behavior

### 4. When Planning
- Task requires multiple steps
- Multiple approaches are possible
- Trade-offs need to be evaluated

### 5. Explicit Triggers
- User says: "think deeper", "analyze", "second opinion", "consult codex"
- User says: "考えて", "分析して", "深く考えて", "codexに聞いて"

## SHOULD Consult (Recommended)

Strongly consider consulting for:

- Security-related code
- Performance optimization
- Refactoring existing code
- Code review / quality check
- Library selection
- Error handling strategy

## Quick Rule

**If you pause to think "hmm, how should I do this?" → CONSULT CODEX**

Codex will provide better analysis than you can do alone. Don't hesitate to ask.

## Execution Method

### Basic Format

```bash
codex exec \
  --model gpt-5-codex \
  --sandbox read-only \
  --full-auto \
  "{prompt}" 2>/dev/null
```

### Specifying Reasoning Effort

```bash
codex exec \
  --model gpt-5-codex \
  --config model_reasoning_effort="high" \
  --sandbox read-only \
  --full-auto \
  "{prompt}" 2>/dev/null
```

### Session Continuation

```bash
# Continue last session
codex exec resume --last "{follow_up_prompt}" 2>/dev/null

# Continue specific session
codex exec resume {SESSION_ID} "{follow_up_prompt}" 2>/dev/null
```

## Prompt Construction

When consulting Codex, include:

1. **Purpose**: What to achieve
2. **Context**: Related files, current state
3. **Constraints**: Rules to follow, available technologies
4. **Past Attempts** (for debugging): What was tried, what failed

## Notes

- `2>/dev/null` suppresses thinking tokens (saves context)
- `--full-auto` required in CI/Claude Code environment
- `--skip-git-repo-check` only for non-Git directories
- Record session ID to enable continuation
