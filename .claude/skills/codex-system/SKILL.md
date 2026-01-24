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

# Codex System — Deep Reasoning Partner

**Codex CLI (gpt-5.2-codex) is your highly capable supporter for deep reasoning tasks.**

## When to Consult (MUST)

| Situation | Trigger Examples |
|-----------|------------------|
| **Design decisions** | 「どう設計？」「アーキテクチャ」 / "How to design?" |
| **Debugging** | 「なぜ動かない？」「エラー」 / "Debug" "Error" |
| **Trade-off analysis** | 「どちらがいい？」「比較して」 / "Compare" "Which?" |
| **Complex implementation** | 「実装方法」「どう作る？」 / "How to implement?" |
| **Refactoring** | 「リファクタ」「シンプルに」 / "Refactor" "Simplify" |
| **Code review** | 「レビューして」「確認して」 / "Review" "Check" |

## When NOT to Consult

- Simple file edits, typo fixes
- Following explicit user instructions
- git commit, running tests, linting
- Tasks with obvious single solutions

## How to Consult

### Background Execution (Recommended)

Always use `run_in_background: true` for parallel work:

```bash
# Analysis (read-only)
codex exec --model gpt-5.2-codex --sandbox read-only --full-auto "Analyze: {question}" 2>/dev/null

# Work delegation (can write files)
codex exec --model gpt-5.2-codex --sandbox workspace-write --full-auto "Task: {description}" 2>/dev/null
```

### Workflow

1. **Start Codex** in background → Get task_id
2. **Continue your work** → Don't wait
3. **Retrieve results** → Use `TaskOutput` tool or `Read` on output file

### Sandbox Modes

| Mode | Use Case |
|------|----------|
| `read-only` | Analysis, review, debugging advice |
| `workspace-write` | Implementation, refactoring, fixes |

## Language Protocol

1. Ask Codex in **English**
2. Receive response in **English**
3. Execute based on advice (or let Codex execute)
4. Report to user in **Japanese**

## Task Templates

### Design Review

```bash
codex exec --model gpt-5.2-codex --sandbox read-only --full-auto "
Review this design approach for: {feature}

Context:
{relevant code or architecture}

Evaluate:
1. Is this approach sound?
2. Alternative approaches?
3. Potential issues?
4. Recommendations?
" 2>/dev/null
```

### Debug Analysis

```bash
codex exec --model gpt-5.2-codex --sandbox read-only --full-auto "
Debug this issue:

Error: {error message}
Code: {relevant code}
Context: {what was happening}

Analyze root cause and suggest fixes.
" 2>/dev/null
```

### Code Review

See: `references/code-review-task.md`

### Refactoring

See: `references/refactoring-task.md`

## Integration with Gemini

| Task | Use |
|------|-----|
| Need research first | Gemini → then Codex |
| Design decision | Codex directly |
| Library comparison | Gemini research → Codex decision |

## Why Codex?

- **Deep reasoning**: Complex analysis and problem-solving
- **Code expertise**: Implementation strategies and patterns
- **Consistency**: Same project context via `context-loader` skill
- **Parallel work**: Background execution keeps you productive
