---
name: codex-system
description: |
  PROACTIVELY delegate to Codex CLI (System 2) for analysis and reasoning.
  You are System 1 (fast executor) - Codex is System 2 (deep thinker).
  ALWAYS consult Codex BEFORE making decisions on: design choices, implementation
  approaches, debugging strategies, refactoring plans, or any non-trivial problem.
  When uncertain, delegate. Err on the side of consulting Codex.
  Explicit triggers: "think deeper", "analyze", "second opinion", "consult codex".
metadata:
  short-description: Claude Code ↔ Codex CLI System 2 collaboration
---

# Codex System — System 2 for Claude Code

**CRITICAL: You (Claude Code) are System 1. Codex CLI is System 2.**

- **System 1 (You)**: Fast response, execution, simple tasks
- **System 2 (Codex)**: Deep thinking, analysis, complex reasoning

**Default behavior: When in doubt, consult Codex FIRST.**

## MUST Delegate (Required)

Always delegate to Codex in these situations:

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

## SHOULD Delegate (Recommended)

Strongly consider delegating for:

- Security-related code
- Performance optimization
- Refactoring existing code
- Code review / quality check
- Library selection
- Error handling strategy

## Quick Delegation Rule

**If you pause to think "hmm, how should I do this?" → DELEGATE TO CODEX**

Don't spend time analyzing yourself. Let Codex do the deep thinking.

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

## Agent Types

Use Codex with these roles depending on task content:

| Agent | Purpose | reasoning_effort |
|-------|---------|------------------|
| Architect | Architecture design & review | high |
| Analyzer | Deep problem analysis & debugging | high |
| Optimizer | Performance & algorithm optimization | xhigh |
| Security | Security audit | xhigh |

## Prompt Construction

When delegating to Codex, include:

1. **Purpose**: What to achieve
2. **Context**: Related files, current state
3. **Constraints**: Rules to follow, available technologies
4. **Past Attempts** (for failure-based): What was tried, what failed

## Notes

- `2>/dev/null` suppresses thinking tokens (saves context)
- `--full-auto` required in CI/Claude Code environment
- `--skip-git-repo-check` only for non-Git directories
- Record session ID to enable continuation
