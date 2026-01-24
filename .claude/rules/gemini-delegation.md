# Gemini Delegation Rule

**Gemini CLI is your research specialist with massive context and multimodal capabilities.**

## About Gemini

Gemini CLI excels at:
- **1M token context window** — Analyze entire codebases at once
- **Google Search grounding** — Access latest information
- **Multimodal processing** — Video, audio, PDF analysis

Think of Gemini as your research assistant who can quickly gather and synthesize information.

**When you need research, context, or multimodal data → Consult Gemini.**

## Gemini vs Codex: Choose the Right Tool

| Task | Codex | Gemini |
|------|-------|--------|
| Design decisions | ✓ | |
| Debugging | ✓ | |
| Code implementation | ✓ | |
| Trade-off analysis | ✓ | |
| Large codebase understanding | | ✓ |
| Pre-implementation research | | ✓ |
| Latest docs/library research | | ✓ |
| Video/Audio/PDF analysis | | ✓ |

## When to Consult Gemini

ALWAYS consult Gemini BEFORE:

1. **Pre-implementation research** - Best practices, library comparison
2. **Large codebase analysis** - Repository-wide understanding
3. **Documentation search** - Latest official docs, breaking changes
4. **Multimodal tasks** - Video, audio, PDF content extraction

### Trigger Phrases (User Input)

Consult Gemini when user says:

| Japanese | English |
|----------|---------|
| 「調べて」「リサーチして」「調査して」 | "Research" "Investigate" "Look up" |
| 「このPDF/動画/音声を見て」 | "Analyze this PDF/video/audio" |
| 「コードベース全体を理解して」 | "Understand the entire codebase" |
| 「最新のドキュメントを確認して」 | "Check the latest documentation" |
| 「〜について情報を集めて」 | "Gather information about X" |

## When NOT to Consult

Skip Gemini for:

- Design decisions (use Codex instead)
- Code implementation (use Codex instead)
- Debugging (use Codex instead)
- Simple file operations (do directly)
- Running tests/linting (do directly)

## How to Consult

**IMPORTANT: Always run Gemini in background to enable parallel work.**

### Step 1: Start Gemini (Background)

Use Bash tool with `run_in_background: true`:

```bash
# Research (headless mode)
gemini -p "Research: {question}" 2>/dev/null

# Codebase analysis
gemini -p "Analyze: {aspect}" --include-directories src,lib 2>/dev/null

# Multimodal (pipe file to stdin)
gemini -p "Extract: {what to extract}" < /path/to/file.pdf 2>/dev/null

# JSON output for structured data
gemini -p "List: {what to list}" --output-format json 2>/dev/null
```

### Step 2: Continue Your Work

While Gemini is processing, you can:
- Work on other files
- Run tests
- Consult Codex for design decisions

### Step 3: Check Results

Use `Read` tool on the output file when ready.

## Common Command Patterns

### Research Pattern

```bash
gemini -p "Research best practices for {topic} in 2025.
Include:
- Recommended approaches
- Common pitfalls
- Library recommendations" 2>/dev/null
```

### Codebase Analysis Pattern

```bash
gemini -p "Analyze this codebase:
1. Architecture overview
2. Key modules and responsibilities
3. Data flow
4. Entry points" --include-directories . 2>/dev/null
```

### Multimodal Pattern

```bash
# PDF
gemini -p "Extract API specifications from this document" < api.pdf 2>/dev/null

# Video
gemini -p "Summarize the key concepts in this tutorial" < tutorial.mp4 2>/dev/null
```

**Language protocol:**
1. Ask Gemini in **English**
2. Receive response in **English**
3. Synthesize findings
4. Report to user in **Japanese**

## Why Consult Gemini?

- Gemini can analyze entire repositories at once
- Gemini has access to the latest information via Google Search
- Gemini can process multimedia content natively
- Quick research before committing to implementation saves time

**Use Gemini for research, Codex for reasoning, Claude for execution.**
