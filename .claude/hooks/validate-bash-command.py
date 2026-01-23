#!/usr/bin/env python3
"""
PreToolUse hook: Validate Bash commands for safety and best practices.

This hook:
- Blocks dangerous commands (rm -rf /, sudo, etc.)
- Warns about deprecated patterns (grep -> rg, find -> rg --files)
- Prevents path traversal attacks
- Blocks access to sensitive files
"""

import json
import re
import sys

# Dangerous command patterns that should be BLOCKED (exit code 2)
BLOCKED_PATTERNS = [
    (r"\brm\s+(-[rf]+\s+)*[/~](?!\S)", "Blocked: rm on root or home directory"),
    (r"\brm\s+-[rf]*\s+--no-preserve-root", "Blocked: rm --no-preserve-root"),
    (r"\bsudo\s+rm\s+-rf", "Blocked: sudo rm -rf is dangerous"),
    (r"\bmkfs\b", "Blocked: filesystem formatting"),
    (r"\bdd\s+.*of=/dev/", "Blocked: dd to device"),
    (r">\s*/dev/sd[a-z]", "Blocked: writing to disk device"),
    (r"\bchmod\s+(-R\s+)?777\s+/", "Blocked: chmod 777 on root"),
    (r"\bchown\s+(-R\s+)?.*\s+/(?!\S)", "Blocked: chown on root"),
    (r":\(\)\s*\{\s*:\|:\s*&\s*\}\s*;", "Blocked: fork bomb"),
    (r"\bkillall\s+-9", "Blocked: killall -9"),
    (r"\bpkill\s+-9\s+-u\s+root", "Blocked: pkill root processes"),
]

# Patterns that should trigger a WARNING but not block
WARNING_PATTERNS = [
    (r"\bgrep\b(?!\s+--)", "Recommendation: Use 'rg' (ripgrep) instead of 'grep' for better performance"),
    (r"\bfind\s+\S+\s+-name\b", "Recommendation: Use 'rg --files -g' instead of 'find -name' for faster search"),
    (r"\bcat\s+\S+\s*\|\s*grep", "Recommendation: Use 'rg' directly instead of 'cat | grep'"),
]

# Sensitive file patterns
SENSITIVE_PATHS = [
    r"\.env(?:\.[^/\s]*)?$",
    r"\.pem$",
    r"\.key$",
    r"credentials",
    r"secret",
    r"/\.ssh/",
    r"/\.aws/",
    r"/\.gnupg/",
]


def check_path_traversal(command: str) -> str | None:
    """Check for path traversal attempts."""
    if re.search(r"\.\./\.\.", command):
        return "Blocked: Path traversal detected (../..)"
    return None


def check_sensitive_files(command: str) -> str | None:
    """Check if command accesses sensitive files."""
    for pattern in SENSITIVE_PATHS:
        if re.search(pattern, command, re.IGNORECASE):
            return f"Warning: Command may access sensitive files matching '{pattern}'"
    return None


def validate_command(command: str) -> tuple[bool, list[str], list[str]]:
    """
    Validate a bash command.

    Returns:
        tuple: (should_block, block_reasons, warnings)
    """
    block_reasons = []
    warnings = []

    # Check for blocked patterns
    for pattern, message in BLOCKED_PATTERNS:
        if re.search(pattern, command, re.IGNORECASE):
            block_reasons.append(message)

    # Check path traversal
    traversal_msg = check_path_traversal(command)
    if traversal_msg:
        block_reasons.append(traversal_msg)

    # Check warning patterns
    for pattern, message in WARNING_PATTERNS:
        if re.search(pattern, command):
            warnings.append(message)

    # Check sensitive files
    sensitive_msg = check_sensitive_files(command)
    if sensitive_msg:
        warnings.append(sensitive_msg)

    should_block = len(block_reasons) > 0
    return should_block, block_reasons, warnings


def main():
    try:
        input_data = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON input: {e}", file=sys.stderr)
        sys.exit(1)

    tool_name = input_data.get("tool_name", "")
    tool_input = input_data.get("tool_input", {})
    command = tool_input.get("command", "")

    # Only process Bash tool
    if tool_name != "Bash" or not command:
        sys.exit(0)

    should_block, block_reasons, warnings = validate_command(command)

    if should_block:
        # Exit code 2 = block the tool call
        error_message = "Command blocked for safety:\n" + "\n".join(f"  • {r}" for r in block_reasons)
        print(error_message, file=sys.stderr)
        sys.exit(2)

    if warnings:
        # Return warnings as additional context (non-blocking)
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "additionalContext": "[Bash Validation] " + "; ".join(warnings)
            }
        }
        print(json.dumps(output))

    sys.exit(0)


if __name__ == "__main__":
    main()
