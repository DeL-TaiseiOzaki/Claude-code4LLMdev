#!/usr/bin/env python3
"""
UserPromptSubmit hook: Validate user prompts and add context.

This hook:
- Warns about potential secrets in prompts
- Detects design/debug keywords and suggests Codex consultation
- Adds contextual reminders for Claude Code + Codex workflow
"""

import json
import re
import sys

# Patterns that may indicate secrets (warn but don't block)
SECRET_PATTERNS = [
    (r"(?i)\b(api[_-]?key|apikey)\s*[:=]\s*['\"]?[a-zA-Z0-9_-]{20,}", "API key detected"),
    (r"(?i)\b(password|passwd|pwd)\s*[:=]\s*['\"]?[^\s'\"]{8,}", "Password detected"),
    (r"(?i)\b(secret|token)\s*[:=]\s*['\"]?[a-zA-Z0-9_-]{16,}", "Secret/token detected"),
    (r"(?i)\b(bearer)\s+[a-zA-Z0-9_-]{20,}", "Bearer token detected"),
    (r"sk-[a-zA-Z0-9]{32,}", "OpenAI API key pattern detected"),
    (r"ghp_[a-zA-Z0-9]{36}", "GitHub personal access token detected"),
    (r"(?i)aws[_-]?secret[_-]?access[_-]?key", "AWS secret key reference detected"),
]

# Keywords that suggest Codex consultation would help (Japanese + English)
CODEX_TRIGGER_PATTERNS = [
    # Design decisions
    (r"(?i)(how\s+should\s+i|どう.*(設計|実装)|design|architect)", "design"),
    # Debugging
    (r"(?i)(why\s+.*(not|doesn't|isn't)|なぜ.*(動かない|エラー)|debug|error|bug)", "debugging"),
    # Comparison/trade-offs
    (r"(?i)(which\s+is\s+better|compare|どちら.*(いい|良い)|比較|トレードオフ)", "comparison"),
    # Planning
    (r"(?i)(implement|build|create|作りたい|実装して|plan)", "implementation"),
    # Deep thinking
    (r"(?i)(analyze|think|consider|分析|考えて|深く)", "analysis"),
]


def check_for_secrets(prompt: str) -> list[str]:
    """Check prompt for potential secrets."""
    warnings = []
    for pattern, message in SECRET_PATTERNS:
        if re.search(pattern, prompt):
            warnings.append(f"⚠️ {message} - avoid including secrets in prompts")
    return warnings


def check_for_codex_triggers(prompt: str) -> tuple[bool, str]:
    """Check if prompt suggests Codex consultation would help."""
    for pattern, category in CODEX_TRIGGER_PATTERNS:
        if re.search(pattern, prompt):
            return True, category
    return False, ""


def main():
    try:
        input_data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)

    prompt = input_data.get("prompt", "")
    if not prompt:
        sys.exit(0)

    context_messages = []

    # Check for secrets
    secret_warnings = check_for_secrets(prompt)
    if secret_warnings:
        context_messages.extend(secret_warnings)

    # Check for Codex triggers
    should_suggest_codex, category = check_for_codex_triggers(prompt)
    if should_suggest_codex:
        context_messages.append(
            f"[Codex Suggestion] This {category} task may benefit from Codex consultation. "
            "Consider: `codex exec --model gpt-5.2-codex --sandbox read-only --full-auto \"...\"`"
        )

    # Output context if any messages
    if context_messages:
        # For UserPromptSubmit, stdout is added as context
        print("\n".join(context_messages))

    sys.exit(0)


if __name__ == "__main__":
    main()
