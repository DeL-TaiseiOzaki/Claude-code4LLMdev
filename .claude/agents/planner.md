# Planner Agent

Research and planning specialist for analyzing codebases and creating implementation strategies.

## Characteristics

| Attribute | Value |
|-----------|-------|
| **Model** | Inherits from parent |
| **Tools** | Read, Glob, Grep |
| **Context** | Inherits parent context |
| **Mode** | Read-only |

## When to Use

- Creating implementation plans before coding
- Analyzing codebase architecture
- Evaluating trade-offs between approaches
- Designing new features or refactoring strategies
- Understanding existing patterns before changes
- Risk assessment for proposed changes

## Workflow

```
User Request → Plan Agent Research → Implementation Plan → Execution
```

1. **Gather context** - Read relevant files and understand structure
2. **Analyze patterns** - Identify existing conventions and constraints
3. **Evaluate options** - Consider multiple approaches and trade-offs
4. **Create plan** - Detailed, step-by-step implementation strategy

## Example Prompts

```
# Feature planning
Plan how to implement a caching layer for the API endpoints.
Research existing patterns, identify integration points, and propose a strategy.

# Refactoring planning
Analyze the authentication module and create a plan to refactor it
into separate concerns: validation, token management, and session handling.

# Architecture analysis
Research the current data flow between frontend and backend.
Identify bottlenecks and propose optimization strategies.
```

## Output Format

Plan agent typically returns:

```markdown
## Implementation Plan: [Feature Name]

### Overview
Brief description of the approach

### Prerequisites
- What needs to be understood/ready first

### Steps
1. Step one with details
2. Step two with details
...

### Files to Modify
- path/to/file.py - Description of changes

### Risks & Considerations
- Potential issues and mitigations

### Testing Strategy
- How to verify the implementation
```

## Best Practices

1. **Use before implementation** - Plan first, code second
2. **Provide context** - Share relevant background information
3. **Ask for trade-offs** - Request comparison of multiple approaches
4. **Review with Codex** - Have Codex CLI review the plan before execution
5. **Iterate** - Refine the plan based on feedback

## Integration with Brainstorming

After `/brainstorm` skill clarifies requirements:
1. Brainstorm collects information via questions
2. Plan agent creates detailed implementation strategy
3. Codex reviews the plan (optional but recommended)
4. Implementation begins

## Invocation

```python
# Via Task tool
{
  "subagent_type": "Plan",
  "description": "Plan authentication refactor",
  "prompt": "Create a detailed plan for refactoring the auth module..."
}
```
