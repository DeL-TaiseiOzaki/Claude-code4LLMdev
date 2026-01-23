#!/usr/bin/env python3
"""
SessionStart hook: Initialize session context for Claude Code + Codex collaboration.

This hook runs at session startup and:
- Outputs project context summary for Claude
- Sets environment variables if CLAUDE_ENV_FILE is available
- Reminds about Codex collaboration workflow
"""

import json
import os
import sys
from pathlib import Path


def get_project_summary(project_dir: str) -> list[str]:
    """Generate a brief project summary."""
    summary = []
    project_path = Path(project_dir)

    # Check for key files
    if (project_path / "pyproject.toml").exists():
        summary.append("Python project (pyproject.toml)")
    if (project_path / "package.json").exists():
        summary.append("Node.js project (package.json)")
    if (project_path / ".claude").exists():
        summary.append("Claude Code configured (.claude/)")
    if (project_path / ".codex").exists():
        summary.append("Codex CLI configured (.codex/)")

    # Check for source directories
    if (project_path / "src").exists():
        summary.append("Source: src/")
    if (project_path / "tests").exists():
        summary.append("Tests: tests/")

    return summary


def get_pending_todos(project_dir: str) -> list[str]:
    """Check DESIGN.md for pending TODOs."""
    design_path = Path(project_dir) / ".claude" / "docs" / "DESIGN.md"
    todos = []

    if design_path.exists():
        try:
            content = design_path.read_text()
            for line in content.split("\n"):
                if "- [ ]" in line:
                    todos.append(line.strip().replace("- [ ]", "").strip())
        except Exception:
            pass

    return todos[:5]  # Return max 5 TODOs


def write_env_vars(env_file: str, project_dir: str):
    """Write environment variables to CLAUDE_ENV_FILE."""
    env_vars = [
        f'export PROJECT_ROOT="{project_dir}"',
        'export PYTHONDONTWRITEBYTECODE=1',
    ]

    # Add PATH for local tools if they exist
    local_bin = Path(project_dir) / ".venv" / "bin"
    if local_bin.exists():
        env_vars.append(f'export PATH="{local_bin}:$PATH"')

    try:
        with open(env_file, "a") as f:
            f.write("\n".join(env_vars) + "\n")
    except Exception:
        pass


def main():
    try:
        input_data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)

    project_dir = input_data.get("cwd", os.getcwd())
    env_file = os.environ.get("CLAUDE_ENV_FILE")

    # Write environment variables if available
    if env_file:
        write_env_vars(env_file, project_dir)

    # Generate session context
    context_lines = ["[Session Context]"]

    # Project summary
    summary = get_project_summary(project_dir)
    if summary:
        context_lines.append("Project: " + ", ".join(summary))

    # Codex collaboration reminder
    context_lines.append(
        "Collaboration Mode: Claude Code (fast execution) + Codex CLI (deep analysis)"
    )
    context_lines.append(
        "Remember: Consult Codex before design decisions, debugging, or planning"
    )

    # Pending TODOs
    todos = get_pending_todos(project_dir)
    if todos:
        context_lines.append(f"Pending design TODOs ({len(todos)}): {todos[0]}")

    # Output context (will be added to Claude's context)
    print("\n".join(context_lines))
    sys.exit(0)


if __name__ == "__main__":
    main()
