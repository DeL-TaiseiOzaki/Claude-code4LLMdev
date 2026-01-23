# Project Overview

LLM/Agent Development Project - Claude Code + Codex CLI Collaboration

## Language Settings

- **Thinking/Reasoning**: English
- **Code**: English (variables, functions, comments, docstrings)
- **User Communication**: Japanese

---

## Codex CLI Integration (CRITICAL)

**Codex CLI is your highly capable supporter. Consult it proactively.**

### When You MUST Consult Codex

| Trigger (JA) | Trigger (EN) | Action |
|--------------|--------------|--------|
| 「どう設計すべき？」 | "How should I design this?" | Consult Codex |
| 「なぜ動かない？」 | "Why doesn't this work?" | Consult Codex |
| 「どちらがいい？」 | "Which is better?" | Consult Codex |
| 「〜を実装して」 | "Implement X" | Consult Codex for design first |
| 「分析して」 | "Analyze this" | Consult Codex |

### How to Consult (Background Execution)

```bash
# Analysis (read-only) - run with run_in_background: true
codex exec --model gpt-5.2-codex --sandbox read-only --full-auto "Analyze: {question}" 2>/dev/null

# Work delegation (can write) - run with run_in_background: true
codex exec --model gpt-5.2-codex --sandbox workspace-write --full-auto "Task: {description}" 2>/dev/null
```

**Protocol**: Ask in English → Receive in English → Execute → Report to user in Japanese

### When NOT to Consult

Simple edits, explicit instructions, git/test/lint, obvious single solutions

---

## Context Management

**Context degradation is the primary failure mode. Manage it proactively.**

### Commands

| Command | When to Use |
|---------|-------------|
| `/clear` | Between unrelated tasks, after completing a feature |
| `/compact` | When context grows large, before complex tasks |

### Best Practices

- **Clear early, clear often**: Don't let context accumulate irrelevant information
- **One task, one context**: Complete and clear before starting unrelated work
- **Pre-task cleanup**: `/compact` before design decisions or complex implementations
- **Token awareness**: Long contexts degrade Claude's performance

### Memory Persistence

Important information survives `/clear` via documentation:

| When Detected | Record To |
|---------------|-----------|
| Design decision | `.claude/docs/DESIGN.md` |
| Library constraint | `.claude/docs/libraries/{name}.md` |
| Project rule | This `AGENTS.md` |

---

## Tech Stack

- **Language**: Python
- **Package Manager**: uv (required, no pip)
- **Dev Tools**: ruff, ty, pytest, poe
- **Main Libraries**: <!-- Add libraries here -->

---

## Extensions Summary

### Agents (Auto-Delegation)

| Agent | Purpose |
|-------|---------|
| **code-reviewer** | Review after code changes |
| **lib-researcher** | Library research & docs |
| **refactorer** | Simplify/clean up code |

### Skills

**Auto-invoked**: `codex-system`, `design-tracker`

**User-invoked**: `/init`, `/plan`, `/tdd`, `/research-lib`, `/simplify`, `/update-design`, `/update-lib-docs`

### Rules (Always Applied)

`language`, `codex-delegation`, `coding-principles`, `dev-environment`, `security`, `testing`

→ Details in `.claude/rules/`

### Hooks (Automatic)

| Hook | Trigger | Purpose |
|------|---------|---------|
| SessionStart | Session begins | Context initialization |
| UserPromptSubmit | Prompt submitted | Secrets detection, Codex suggestion |
| PreToolUse (Bash) | Before Bash | Dangerous command blocking |
| PreToolUse (Edit/Write) | Before file changes | Design decision reminder |
| PostToolUse (Task) | After planning | Codex review suggestion |

---

## Directory Structure

```
.claude/
├── settings.json      # Hooks & permissions
├── rules/             # Coding rules (always applied)
├── agents/            # Sub-agents
├── skills/            # Workflows
├── hooks/             # Hook scripts
└── docs/
    ├── DESIGN.md      # Design decisions
    └── libraries/     # Library documentation

.codex/
├── AGENTS.md          # Codex global instructions
├── config.toml        # Features config
└── skills/            # Codex skills

src/                   # Source code
tests/                 # Tests
```

## Common Commands

```bash
# Dependencies
uv add <package>
uv sync

# Quality (via poe)
poe lint          # ruff check + format
poe test          # pytest
poe typecheck     # ty
poe all           # all checks
```

---

## Notes

- API keys via environment variables (never commit `.env`)
- Watch token consumption
- Retry logic for rate limits
