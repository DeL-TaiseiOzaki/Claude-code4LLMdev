---
name: brainstorm
description: Clarify ambiguous user requests through structured questioning. Use when user input is vague, incomplete, or could have multiple interpretations. Collects requirements before planning.
disable-model-invocation: true
---

# Brainstorming Skill

## Purpose

Transform vague user requests into clear, actionable requirements through structured questioning.

## When to Use

- User request is ambiguous or incomplete
- Multiple interpretations are possible
- Scope is unclear
- Technical decisions need user input
- Requirements need clarification before planning

## Workflow

```
┌─────────────────────────────────────────────────────────────┐
│  1. ANALYZE - Identify what's unclear in the request        │
└─────────────────────┬───────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  2. ASK - Ask 3-5 clarifying questions (use AskUserQuestion)│
└─────────────────────┬───────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  3. SUMMARIZE - Confirm understanding with user             │
└─────────────────────┬───────────────────────────────────────┘
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  4. PLAN - ALWAYS invoke /plan skill with collected info    │
└─────────────────────────────────────────────────────────────┘
```

## Question Categories

Ask questions from relevant categories:

### 1. Scope & Goals
- What is the main goal/outcome you want?
- What problem are you trying to solve?
- Who will use this feature?

### 2. Technical Requirements
- Any specific technologies/libraries to use or avoid?
- Performance requirements?
- Compatibility constraints?

### 3. Existing Context
- Is there existing code to integrate with?
- Any patterns to follow or avoid?
- Related features to consider?

### 4. Constraints
- Timeline or priority?
- Budget/resource limitations?
- Security or compliance requirements?

### 5. Success Criteria
- How will you know this is complete?
- What does "done" look like?
- Any specific acceptance criteria?

## Execution Steps

### Step 1: Analyze the Request

Read the user's input and identify:
- What is clear
- What is ambiguous
- What information is missing
- Potential interpretations

### Step 2: Ask Clarifying Questions

Use `AskUserQuestion` tool to ask 3-5 targeted questions:

```
Questions should be:
- Specific (not open-ended)
- Actionable (answers lead to decisions)
- Prioritized (most important first)
- Provide options when possible
```

Example:
```json
{
  "questions": [
    {
      "question": "What type of authentication do you need?",
      "header": "Auth Type",
      "options": [
        {"label": "JWT tokens", "description": "Stateless, good for APIs"},
        {"label": "Session-based", "description": "Traditional, server-side state"},
        {"label": "OAuth/SSO", "description": "Third-party authentication"}
      ]
    }
  ]
}
```

### Step 3: Summarize Understanding

After receiving answers, summarize:

```markdown
## 要件の確認

理解した内容を確認させてください：

**目標**: [What user wants to achieve]
**スコープ**: [What's included/excluded]
**技術要件**: [Technologies, constraints]
**成功基準**: [How to verify completion]

この理解で正しいですか？
```

### Step 4: Invoke Plan Skill

**CRITICAL: After brainstorming, ALWAYS invoke `/plan` skill.**

```
/plan [Feature/Task Name]

Based on brainstorming session:
- Goal: [summarized goal]
- Requirements: [collected requirements]
- Constraints: [identified constraints]
- Success criteria: [defined criteria]
```

## Example Session

**User**: 「認証機能を作りたい」

**Brainstorm Response**:
```
認証機能について、いくつか確認させてください。

1. **認証方式**: JWT / セッション / OAuth のどれを使いますか？
2. **ユーザー管理**: 新規登録機能は必要ですか？
3. **統合先**: 既存のAPIやデータベースはありますか？
4. **セキュリティ要件**: 2FAや監査ログは必要ですか？
```

**After answers**:
```
## 要件の確認

- JWT認証でAPIを保護
- 新規登録 + ログイン + パスワードリセット
- PostgreSQLの既存usersテーブルを使用
- 2FAは将来対応、監査ログは必要

この理解で進めてよろしいですか？

[確認後、/plan を実行]
```

## Language

- **Questions**: Japanese (user-facing)
- **Internal processing**: English
- **Summary**: Japanese
- **Plan invocation**: English (technical)

## Notes

- Never skip the planning phase after brainstorming
- Keep questions focused and minimal (3-5 max)
- Provide sensible defaults in options
- If user says "おまかせ" or "any", make reasonable choices and document them
