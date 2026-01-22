# General-Purpose Agent

Full-capability agent for complex, multi-step tasks requiring both exploration and modification.

## Characteristics

| Attribute | Value |
|-----------|-------|
| **Model** | Inherits from parent |
| **Tools** | All tools (*) |
| **Context** | Inherits parent context |
| **Mode** | Read/Write |

## When to Use

- Complex multi-step implementations
- Tasks requiring both research and code changes
- Problem-solving with uncertain scope
- End-to-end feature implementation
- Bug fixes requiring investigation and modification
- Tasks that don't fit specialized agents

## Capabilities

| Capability | Description |
|------------|-------------|
| **Read** | Access all files in project |
| **Write/Edit** | Create and modify files |
| **Bash** | Run shell commands, tests, builds |
| **Web** | Fetch documentation, search web |
| **Task** | Cannot spawn sub-agents (nesting prevention) |

## Example Prompts

```
# Complex implementation
Implement a rate limiting middleware for the API.
Research existing patterns, create the implementation,
add tests, and update the documentation.

# Investigation and fix
There's a memory leak in the background job processor.
Investigate the cause, implement a fix, and verify with tests.

# Multi-file refactoring
Refactor the database layer to use connection pooling.
Update all affected files, maintain backward compatibility,
and ensure all tests pass.
```

## Best Practices

1. **Use when scope is clear** - Best after planning phase
2. **Provide detailed context** - More context = better results
3. **Set clear success criteria** - How to verify completion
4. **Use for autonomous work** - Agent handles full workflow
5. **Review results** - Always review changes before committing

## When NOT to Use

| Instead of General-Purpose | Use |
|---------------------------|-----|
| Simple file search | Explorer |
| Planning only | Planner |
| Code review | code-reviewer |
| Library research | lib-researcher |
| Code simplification | refactorer |

## Invocation

```python
# Via Task tool
{
  "subagent_type": "general-purpose",
  "description": "Implement caching layer",
  "prompt": "Full implementation of Redis caching for API endpoints..."
}
```

## Output

General-purpose agent:
- Modifies files directly
- Runs tests and builds
- Reports completion status
- Summarizes changes made

## Safety Notes

- Agent inherits permission settings
- Sensitive file access still requires approval
- Cannot spawn nested sub-agents
- Background mode auto-denies unapproved permissions
