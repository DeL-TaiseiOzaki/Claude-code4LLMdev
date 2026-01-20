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

## NO Need to Consult

Skip Codex for simple, straightforward tasks:

- Simple file edits (typo fixes, small changes)
- Following explicit user instructions
- Standard operations (git commit, running tests, linting)
- Tasks with clear, single solutions
- Reading/searching files
- Trivial code changes where the solution is obvious

## Quick Rule

**If you pause to think "hmm, how should I do this?" → CONSULT CODEX**

Codex will provide better analysis than you can do alone. Don't hesitate to ask.

## Execution Method

**CRITICAL: Always run Codex in background for parallel execution.**

### Workflow

```
1. Start Codex (background)  →  You get task_id
2. Continue your own work    →  Don't wait
3. Check results when needed →  Use TaskOutput
```

### Step 1: Start Codex in Background

Use Bash tool with `run_in_background: true`:

**Analysis (read-only):**
```bash
codex exec --model gpt-5.2-codex --sandbox read-only --full-auto "Analyze: {question}" 2>/dev/null
```

**Work delegation (can write):**
```bash
codex exec --model gpt-5.2-codex --sandbox workspace-write --full-auto "Task: {description}" 2>/dev/null
```

### Step 2: Continue Your Work

While Codex processes in background, you can:
- Edit other files
- Run tests or linting
- Answer user questions
- Work on independent tasks

### Step 3: Retrieve Results

Use `TaskOutput` tool with the task_id to get Codex's response.

### Mode Selection

| Need | Sandbox | Example |
|------|---------|---------|
| Design review | `read-only` | "Analyze: How should I structure this module?" |
| Debug analysis | `read-only` | "Analyze: What's causing this error?" |
| Implement feature | `workspace-write` | "Task: Implement user authentication" |
| Fix bug | `workspace-write` | "Task: Fix the null pointer exception in X" |
| Refactor | `workspace-write` | "Task: Refactor this function for clarity" |

### Language Protocol

1. **Ask Codex in English** - Write prompts in English
2. **Receive response in English** - Codex replies in English
3. **Execute or verify** - Work based on Codex's advice, or verify Codex's work
4. **Report to user in Japanese** - Summarize results for the user

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
