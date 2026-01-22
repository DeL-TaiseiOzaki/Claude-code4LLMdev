---
name: plan
description: Create a detailed implementation plan for a feature or task. ALWAYS delegates to Codex CLI for comprehensive analysis.
disable-model-invocation: true
---

# Create Implementation Plan

Create an implementation plan for $ARGUMENTS.

## CRITICAL: Always Use Codex

**This skill MUST delegate planning to Codex CLI.**

Codex is the most powerful sub-agent with exceptional reasoning capabilities.
Trust it completely for complex analysis, design decisions, and planning.

## Workflow

```
┌─────────────────────────────────────────────────────────────┐
│  1. GATHER CONTEXT                                          │
│     - Read relevant files                                   │
│     - Understand current codebase state                     │
└─────────────────────┬───────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  2. DELEGATE TO CODEX (REQUIRED)                            │
│     Run in background:                                      │
│     codex exec --model gpt-5.2-codex --sandbox read-only \  │
│       --full-auto "Create implementation plan for: ..."     │
└─────────────────────┬───────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  3. REVIEW & PRESENT                                        │
│     - Format Codex's plan for user                         │
│     - Add any clarifying notes                              │
└─────────────────────────────────────────────────────────────┘
```

## Codex Invocation

**Always run Codex with this command:**

```bash
codex exec --model gpt-5.2-codex --sandbox read-only --full-auto "
Task: Create a detailed implementation plan

Feature/Task: {$ARGUMENTS}

Context:
- Project type: {from AGENTS.md}
- Relevant files: {list discovered files}
- Current patterns: {existing conventions}

Requirements:
1. Analyze the codebase thoroughly
2. Consider all dependencies and impacts
3. Break into small, testable steps
4. Identify risks and mitigations
5. Suggest verification method for each step

Output format:
## Implementation Plan: {Title}

### Purpose
{1-2 sentences}

### Scope
- New files: {list}
- Modified files: {list}
- Dependencies: {list}

### Implementation Steps
#### Step 1: {Title}
- [ ] {Specific task}
**Verification**: {How to verify}

### Risks & Considerations
### Open Questions
" 2>/dev/null
```

## Why Codex?

| Aspect | Codex Advantage |
|--------|-----------------|
| **Analysis depth** | Comprehensive codebase understanding |
| **Pattern recognition** | Identifies existing conventions |
| **Risk assessment** | Thorough consideration of edge cases |
| **Step breakdown** | Optimal task decomposition |
| **Consistency** | Aligned with project standards |

## Notes

- **Never skip Codex** - It's mandatory for this skill
- Run Codex in background (`run_in_background: true`) for efficiency
- Wait for Codex response before presenting to user
- If Codex is unavailable, inform user and suggest retry

## Language

- **Codex prompt**: English
- **Codex response**: English
- **User presentation**: Japanese
