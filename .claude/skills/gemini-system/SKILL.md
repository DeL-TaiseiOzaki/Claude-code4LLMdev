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

**Gemini CLI is your research specialist with massive context and multimodal capabilities.**

> **Full details:** See "Gemini CLI Integration" section in AGENTS.md

## Gemini vs Codex: When to Use Which

| Use Case | Codex | Gemini |
|----------|-------|--------|
| Design decisions, debugging | ✓ | |
| Complex reasoning, code implementation | ✓ | |
| Large codebase understanding | | ✓ |
| Pre-implementation research | | ✓ |
| Google Search for latest info | | ✓ |
| Video/Audio/PDF analysis | | ✓ |
| Documentation comprehension | | ✓ |

## Gemini's Strengths

- **1M token context window** — Analyze entire repositories at once
- **Google Search grounding** — Access latest information and documentation
- **Multimodal** — Process videos, audio files, PDFs natively
- **Fast exploration** — Quick overview before deep analysis

## Quick Reference

### When to Consult Gemini

| Situation | Action |
|-----------|--------|
| Need to understand large codebase | **MUST** consult |
| Research before implementation | **MUST** consult |
| Analyze video/audio/PDF | **MUST** consult |
| Find latest library docs/examples | **MUST** consult |
| Quick web research | **SHOULD** consult |
| Code implementation, design decisions | Use Codex instead |

### How to Consult (Background Execution)

**Always use `run_in_background: true`:**

```bash
# Research / Analysis (read-only, headless mode)
gemini -p "Research: {question}" --output-format json 2>/dev/null

# Codebase understanding (include directories)
gemini -p "Analyze codebase structure and explain: {aspect}" --include-directories src,lib 2>/dev/null

# Multimodal analysis
gemini -p "Analyze this file and explain: {question}" < /path/to/file.pdf 2>/dev/null

# With Google Search grounding
gemini -p "Search and summarize: {topic} latest best practices 2025" 2>/dev/null
```

### Workflow

1. **Start Gemini** (background) → Get task_id
2. **Continue your work** → Don't wait
3. **Retrieve results** → Use `Read` tool on output file

### Language Protocol

1. Ask Gemini in **English**
2. Receive response in **English**
3. Synthesize and apply findings
4. Report to user in **Japanese**

## Common Patterns

### Pattern 1: Pre-Implementation Research

```bash
gemini -p "Research the best practices for implementing {feature} in Python.
Include:
- Common patterns and anti-patterns
- Library recommendations
- Performance considerations
- Security concerns" 2>/dev/null
```

### Pattern 2: Large Codebase Analysis

```bash
gemini -p "Analyze this repository structure and provide:
1. High-level architecture overview
2. Key modules and their responsibilities
3. Data flow between components
4. Entry points and main execution paths" --include-directories . 2>/dev/null
```

### Pattern 3: Multimodal Data Processing

```bash
# Video analysis
gemini -p "Analyze this video and describe:
- Main content and key points
- Technical concepts demonstrated
- Timestamps of important sections" < demo.mp4 2>/dev/null

# PDF documentation
gemini -p "Extract and summarize:
- API specifications
- Configuration options
- Usage examples" < api-docs.pdf 2>/dev/null
```

### Pattern 4: Latest Documentation Search

```bash
gemini -p "Search for the latest {library} documentation (2025).
Find:
- Breaking changes from previous versions
- New recommended patterns
- Migration guides if applicable" 2>/dev/null
```
