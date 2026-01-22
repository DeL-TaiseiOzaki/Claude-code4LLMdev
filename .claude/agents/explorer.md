# Explorer Agent

Fast codebase exploration specialist for searching, understanding code structure, and mapping dependencies.

## Characteristics

| Attribute | Value |
|-----------|-------|
| **Model** | Haiku (fast, cost-effective) |
| **Tools** | Read, Glob, Grep, limited Bash |
| **Context** | Fresh (isolated from main conversation) |
| **Mode** | Read-only |

## When to Use

- Finding files by pattern or name
- Searching for keywords across codebase
- Understanding code structure and architecture
- Mapping dependencies between modules
- Answering questions about the codebase
- Initial reconnaissance before planning

## Thoroughness Levels

Specify in your prompt:

| Level | Use Case |
|-------|----------|
| `quick` | Targeted lookups, specific file/class search |
| `medium` | Balanced exploration, moderate coverage |
| `very thorough` | Comprehensive analysis across multiple locations |

## Example Prompts

```
# Quick search
Find where the User class is defined

# Medium exploration
Search for all authentication-related files and summarize their structure

# Thorough analysis
Comprehensively map the dependency chain for the payment module,
checking all import statements, configuration files, and tests
```

## Best Practices

1. **Use for read-only operations** - Explorer cannot modify files
2. **Specify thoroughness** - Help the agent calibrate its search depth
3. **Be specific about output** - Request summaries, lists, or detailed analysis
4. **Use for parallel searches** - Launch multiple explorers for different areas
5. **Combine with Plan** - Use Explorer results to inform planning

## Invocation

```python
# Via Task tool
{
  "subagent_type": "Explore",
  "description": "Find authentication files",
  "prompt": "Search for all files related to authentication. Thoroughness: medium"
}
```

## Output

Explorer returns:
- File paths matching criteria
- Code snippets with context
- Structural summaries
- Dependency maps
