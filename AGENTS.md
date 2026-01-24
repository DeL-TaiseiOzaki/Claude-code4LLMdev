# fastslow-claude-code

LLM/Agent Development Project with Multi-Agent Collaboration

---

## Multi-Agent System (CRITICAL)

```
┌─────────────────────────────────────────────────────────────┐
│                 Claude Code (You)                           │
│                      ↓                                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐  │
│  │  Codex CLI   │  │  Gemini CLI  │  │  Subagent        │  │
│  │  (Deep)      │  │  (Research)  │  │  (Parallel)      │  │
│  ├──────────────┤  ├──────────────┤  ├──────────────────┤  │
│  │ 設計判断     │  │ リポジトリ   │  │ 独立タスク       │  │
│  │ デバッグ     │  │ 全体分析     │  │ 探索・検索       │  │
│  │ コードレビュー│  │ ライブラリ調査│  │ シンプル実装     │  │
│  │ リファクタ   │  │ マルチモーダル│  │                  │  │
│  └──────────────┘  └──────────────┘  └──────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Codex CLI — 設計・デバッグ・深い推論

**MUST consult before**: 設計判断、デバッグ、トレードオフ分析、リファクタリング

| Trigger (日本語) | Trigger (English) |
|------------------|-------------------|
| 「どう設計？」「実装方法は？」 | "How to design/implement?" |
| 「なぜ動かない？」「エラー」 | "Debug" "Error" "Not working" |
| 「どちらがいい？」「比較して」 | "Compare" "Which is better?" |
| 「考えて」「深く分析」 | "Think" "Analyze deeply" |

```bash
codex exec --model gpt-5.2-codex --sandbox read-only --full-auto "{question}"
```

> 詳細: `/codex-system` skill

### Gemini CLI — リサーチ・大規模分析

**MUST consult for**: ライブラリ調査、リポジトリ全体理解、マルチモーダル

| Trigger (日本語) | Trigger (English) |
|------------------|-------------------|
| 「調べて」「リサーチ」 | "Research" "Investigate" |
| 「PDF/動画/音声を見て」 | "Analyze PDF/video/audio" |
| 「コードベース全体」 | "Entire codebase" |

```bash
gemini -p "{question}" 2>/dev/null
```

> 詳細: `/gemini-system` skill

---

## Tech Stack

- **Language**: Python
- **Package Manager**: uv (pip禁止)
- **Dev Tools**: ruff, ty, pytest, poe
- **Commands**: `poe lint` `poe test` `poe all`

---

## Workflow

### プロジェクト開始時

```
/startproject <機能名>
```

1. Gemini → リポジトリ分析・ライブラリ調査
2. Claude → 要件ヒアリング・計画作成
3. Codex → 計画レビュー・精査
4. Claude → タスクリスト作成 (Ctrl+T で表示)

### 実装中

- **設計判断が必要** → Codex相談
- **調査が必要** → Gemini相談
- **テスト失敗** → Codex分析
- **大量実装後** → Codexレビュー

> Hooks が自動で協調を提案します

---

## Key Skills

| Skill | Purpose |
|-------|---------|
| `/startproject` | マルチエージェント協調でプロジェクト開始 |
| `/codex-system` | Codex CLI連携の詳細 |
| `/gemini-system` | Gemini CLI連携の詳細 |
| `/plan` | 実装計画作成 |
| `/tdd` | テスト駆動開発 |

---

## Documentation

| Location | Content |
|----------|---------|
| `.claude/docs/DESIGN.md` | 設計決定 |
| `.claude/docs/research/` | Gemini調査結果 |
| `.claude/docs/libraries/` | ライブラリ制約 |
| `.claude/rules/` | コーディングルール |

---

## Notes

- API keys → 環境変数で管理 (`.env`はコミット禁止)
- 設計決定 → 自動で `DESIGN.md` に記録
- 不明点 → 推測せず調査 (Gemini活用)
