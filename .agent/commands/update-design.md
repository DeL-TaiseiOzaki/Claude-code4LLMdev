会話の内容から，プロジェクトの設計・実装方針を `.agent/docs/DESIGN.md` に記録・更新してください．

Note: This command explicitly invokes the same workflow as the `design-tracker` skill.
Use this when you want to force a design document update.

## Workflow

1. Read existing `.agent/docs/DESIGN.md`
2. Extract decisions/information from the conversation
3. Update the appropriate section
4. Add entry to Changelog with today's date

## Sections

| Topic | Section |
|-------|---------|
| Goals, purpose | Overview |
| Structure, components | Architecture |
| Design patterns | Implementation Plan > Patterns |
| Library choices | Implementation Plan > Libraries |
| Decision rationale | Implementation Plan > Key Decisions |
| Future work | TODO |
| Unresolved issues | Open Questions |

## Language

- Document content: English (technical), Japanese OK for descriptions
- User communication: Japanese

$ARGUMENTS があれば，その内容を重点的に記録してください．
