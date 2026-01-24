---
name: startproject
description: |
  Start a new project/feature implementation session with multi-agent collaboration.
  Gemini analyzes repository and libraries, Claude gathers requirements and drafts plan,
  Codex reviews and refines the plan, then Claude creates the final task list.
metadata:
  short-description: Project kickoff with multi-agent collaboration
---

# Start Project — Multi-Agent Project Kickoff

**Use this skill at the beginning of any significant implementation work.**

## Overview

This skill orchestrates a complete project kickoff using three AI agents:

```
┌─────────────────────────────────────────────────────────────────┐
│  Phase 1: Gemini CLI (Research)                                 │
│  → Repository analysis & library investigation                  │
│  → Output: .claude/docs/research/{feature}.md                   │
├─────────────────────────────────────────────────────────────────┤
│  Phase 2: Claude Code (Planning)                                │
│  → Read Gemini's research                                       │
│  → Gather requirements from user                                │
│  → Draft implementation plan                                    │
├─────────────────────────────────────────────────────────────────┤
│  Phase 3: Codex CLI (Review)                                    │
│  → Read Gemini's research + Claude's draft plan                 │
│  → Deep review and refinement                                   │
│  → Risk analysis and recommendations                            │
├─────────────────────────────────────────────────────────────────┤
│  Phase 4: Claude Code (Execution)                               │
│  → Synthesize all inputs                                        │
│  → Create comprehensive task list                               │
│  → Get user confirmation and start                              │
└─────────────────────────────────────────────────────────────────┘
```

## Workflow

### Phase 1: Gemini Research (Background)

Launch Gemini CLI to analyze the codebase and relevant libraries.
**Run in background** so Claude can prepare for Phase 2.

```bash
# Run with run_in_background: true
gemini -p "Analyze this repository for implementing: {feature}

Provide comprehensive analysis:

## 1. Repository Structure
- Overall architecture and patterns
- Key modules and their responsibilities
- Data flow between components
- Entry points and extension points

## 2. Relevant Existing Code
- Files/modules related to this feature
- Existing patterns to follow
- Code conventions used

## 3. Library Investigation
- Current dependencies that may be useful
- Recommended libraries for this feature (with rationale)
- Version compatibility considerations

## 4. Technical Considerations
- Potential integration points
- Database/API changes needed
- Security considerations

## 5. Recommendations
- Suggested implementation approach
- Files to create vs modify
- Order of implementation

Output in markdown format suitable for documentation.
" --include-directories . 2>/dev/null
```

**Save Gemini output to:** `.claude/docs/research/{feature-name}.md`

This allows both Claude Code and Codex to reference the research.

### Phase 2: Requirements Gathering (Claude Code)

While waiting for Gemini (or after), Claude gathers requirements from user.

**Read Gemini's research first** (if available):
```
Read .claude/docs/research/{feature-name}.md
```

**Ask user these questions (in Japanese):**

1. **目的**: 何を達成したいですか？（1-2文で）
2. **スコープ**: 含めるもの・除外するものは？
3. **技術的要件**: 特定のライブラリ、パターン、制約は？
4. **成功基準**: 完了の判断基準は何ですか？
5. **優先度**: 最も重要な部分はどこですか？

**Don't proceed until you have clear answers.** Ask follow-up questions based on Gemini's research.

**Draft Implementation Plan:**

Based on Gemini research + user requirements, create draft plan:

```markdown
# Implementation Plan Draft: {feature}

## Overview
{1-2 sentences}

## Approach
{Based on Gemini's recommendations + user requirements}

## Components
1. {Component 1}: {description}
2. {Component 2}: {description}
...

## File Changes
- Create: {list}
- Modify: {list}

## Dependencies
- {library}: {purpose}

## Open Questions
- {Any uncertainties for Codex to address}
```

### Phase 3: Codex Deep Review (Background)

Submit the draft plan to Codex for deep review.
**Include reference to Gemini's research.**

```bash
# Run with run_in_background: true
codex exec --model gpt-5.2-codex --sandbox read-only --full-auto "
Review this implementation plan for: {feature}

## Gemini Research Summary
{Read from .claude/docs/research/{feature}.md or include key points}

## Draft Plan
{Claude's draft plan from Phase 2}

## User Requirements
{Summary from Phase 2}

---

Provide deep analysis:

1. **Plan Assessment**
   - Is the approach sound?
   - Are there better alternatives?
   - Missing considerations?

2. **Risk Analysis**
   - Technical risks and mitigations
   - Complexity hotspots
   - Potential blockers

3. **Implementation Order**
   - Optimal sequence of tasks
   - Parallelizable work
   - Critical path

4. **Refinements**
   - Specific improvements to the plan
   - Additional tasks needed
   - Tasks that can be simplified or removed

5. **Complexity Estimates**
   - Low/Medium/High for each component
   - Total estimated effort

Be thorough. This plan will guide the entire implementation.
" 2>/dev/null
```

### Phase 4: Task List Creation (Claude Code)

Synthesize all inputs and create the final task list.

**Inputs to synthesize:**
1. Gemini's research (`.claude/docs/research/{feature}.md`)
2. User requirements (from Phase 2)
3. Codex's review and refinements (from Phase 3)

**Create tasks using TodoWrite:**

```python
# Task structure
{
    "content": "Implement {specific feature}",     # Imperative
    "activeForm": "Implementing {specific feature}", # Present continuous
    "status": "pending"
}
```

**Task Breakdown Guidelines:**

| Category | Examples |
|----------|----------|
| Setup | Install dependencies, create directories, config files |
| Core | Business logic, data models, main features |
| Integration | Connect components, wire dependencies, APIs |
| Testing | Unit tests, integration tests, manual verification |

**Ordering:**
1. Independent tasks first
2. Then dependent tasks in order
3. Testing interleaved or at end (based on TDD preference)

### Phase 5: Confirmation and Kickoff

Present final plan to user (in Japanese):

```markdown
## プロジェクト計画: {feature}

### 調査結果 (Gemini)
{Key findings from research - 3-5 bullet points}

### 設計方針 (Codex レビュー済み)
{Approach with Codex's refinements}

### タスクリスト ({N}個)

#### 準備
- [ ] {Task 1}
- [ ] {Task 2}

#### コア実装
- [ ] {Task 3}
- [ ] {Task 4}
...

#### テスト
- [ ] {Task N-1}
- [ ] {Task N}

### リスクと注意点
{From Codex analysis}

### 参考資料
- 調査レポート: `.claude/docs/research/{feature}.md`

---
この計画で進めてよろしいですか？
```

**Wait for user confirmation before starting implementation.**

## Tips

- **Ctrl+T**: Toggle task list visibility
- **`/todos`**: Show all current tasks
- Tasks persist across context compactions
- Update task status immediately upon completion
- Only have ONE task `in_progress` at a time
- Re-consult Codex if unexpected complexity arises

## Output Files

| File | Purpose | Created By |
|------|---------|------------|
| `.claude/docs/research/{feature}.md` | Repository & library analysis | Gemini |
| Task list (internal) | Progress tracking | Claude (TodoWrite) |

## Example Usage

**User:** `/startproject ユーザー認証機能を追加したい`

**Claude will:**
1. Launch Gemini to analyze repo and auth libraries (background)
2. Ask user about OAuth vs session, password requirements, etc.
3. Draft plan based on Gemini research + user answers
4. Submit to Codex for deep review (background)
5. Create 10-15 specific tasks from all inputs
6. Present plan with research reference and wait for confirmation
