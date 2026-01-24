---
name: gemini-system
description: |
  PROACTIVELY consult Gemini CLI for research, large codebase comprehension,
  and multimodal data processing. Gemini excels at: massive context windows (1M tokens),
  Google Search grounding, video/audio/PDF analysis, and repository-wide understanding.
  Use for pre-implementation research, documentation analysis, and multimodal tasks.
  Explicit triggers: "research", "investigate", "analyze video/audio/PDF", "understand codebase".
metadata:
  short-description: Claude Code ↔ Gemini CLI collaboration (research & multimodal)
---

# Gemini System — Research & Multimodal Specialist

**Gemini CLI (gemini-3-pro-preview) is your research specialist with 1M token context.**

## Gemini vs Codex

| Task | Gemini | Codex |
|------|--------|-------|
| **リポジトリ全体理解** | ✓ | |
| **ライブラリ調査** | ✓ | |
| **マルチモーダル (PDF/動画/音声)** | ✓ | |
| **最新ドキュメント検索** | ✓ | |
| **設計判断** | | ✓ |
| **デバッグ** | | ✓ |
| **コード実装** | | ✓ |

## When to Consult (MUST)

| Situation | Trigger Examples |
|-----------|------------------|
| **Research** | 「調べて」「リサーチ」 / "Research" "Investigate" |
| **Library docs** | 「ライブラリ」「ドキュメント」 / "Library" "Docs" |
| **Codebase analysis** | 「コードベース全体」 / "Entire codebase" |
| **Multimodal** | 「PDF」「動画」「音声」 / "PDF" "Video" "Audio" |

## When NOT to Consult

- Design decisions (use Codex)
- Debugging (use Codex)
- Code implementation (use Codex)
- Simple file operations (do directly)

## How to Consult

### Background Execution (Recommended)

Always use `run_in_background: true` for parallel work:

```bash
# Research
gemini -p "Research: {question}" 2>/dev/null

# Codebase analysis
gemini -p "Analyze: {aspect}" --include-directories src,lib 2>/dev/null

# Multimodal (PDF/video/audio)
gemini -p "Extract: {what}" < /path/to/file.pdf 2>/dev/null

# Latest docs search
gemini -p "Search latest {library} docs 2025" 2>/dev/null
```

### Workflow

1. **Start Gemini** in background → Get task_id
2. **Continue your work** → Don't wait
3. **Retrieve results** → Use `Read` tool on output file
4. **Save to docs** → `.claude/docs/research/{topic}.md`

## Language Protocol

1. Ask Gemini in **English**
2. Receive response in **English**
3. Synthesize and apply findings
4. Report to user in **Japanese**

## Output Location

Save Gemini research results to:
```
.claude/docs/research/{topic}.md
```

This allows Claude and Codex to reference the research later.

## Task Templates

### Pre-Implementation Research

```bash
gemini -p "Research best practices for {feature} in Python 2025.
Include:
- Common patterns and anti-patterns
- Library recommendations (with comparison)
- Performance considerations
- Security concerns
- Code examples" 2>/dev/null
```

### Repository Analysis

```bash
gemini -p "Analyze this repository:
1. Architecture overview
2. Key modules and responsibilities
3. Data flow between components
4. Entry points and extension points
5. Existing patterns to follow" --include-directories . 2>/dev/null
```

### Library Research

See: `references/lib-research-task.md`

### Multimodal Analysis

```bash
# Video
gemini -p "Analyze video: main concepts, key points, timestamps" < tutorial.mp4 2>/dev/null

# PDF
gemini -p "Extract: API specs, examples, constraints" < api-docs.pdf 2>/dev/null

# Audio
gemini -p "Transcribe and summarize: decisions, action items" < meeting.mp3 2>/dev/null
```

## Integration with Codex

| Workflow | Steps |
|----------|-------|
| **New feature** | Gemini research → Codex design review |
| **Library choice** | Gemini comparison → Codex decision |
| **Bug investigation** | Gemini codebase search → Codex debug |

## Why Gemini?

- **1M token context**: Entire repositories at once
- **Google Search**: Latest information and docs
- **Multimodal**: Native PDF/video/audio processing
- **Fast exploration**: Quick overview before deep work
- **Shared context**: Results saved for Claude/Codex
