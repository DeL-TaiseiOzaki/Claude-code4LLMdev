このプロジェクトを分析し，AGENTS.md を生成してください．

## 手順

### 1. プロジェクト分析

以下のファイルを探して技術スタックを特定:

- `package.json` → Node.js/TypeScript プロジェクト
- `pyproject.toml` / `setup.py` / `requirements.txt` → Python プロジェクト
- `Cargo.toml` → Rust プロジェクト
- `go.mod` → Go プロジェクト
- `Makefile` / `Dockerfile` → ビルド/デプロイ設定
- `.github/workflows/` → CI/CD 設定

### 2. ユーザーに確認

AskUserQuestion ツールで以下を質問:

1. **プロジェクト概要**: このプロジェクトは何をするものですか？（1-2文で）
2. **言語設定**: コードは英語/日本語どちらで書きますか？
3. **追加のルール**: 他に守るべきコーディング規約はありますか？

### 3. AGENTS.md 生成

分析結果と回答を元に AGENTS.md を生成:

```markdown
# プロジェクト概要

{ユーザーの回答}

## 言語設定

- **思考・推論**: 英語で行う
- **コード**: {分析結果に基づく}
- **ユーザーとのやり取り**: 日本語で出力

## 技術スタック

- **言語**: {検出した言語}
- **パッケージ管理**: {検出したツール}
- **開発ツール**: {検出したツール}
- **主要ライブラリ**: {検出したライブラリ}

---

## 拡張機能

このプロジェクトには以下の拡張機能が設定されています。
Claude Code と Codex CLI の両方で利用可能です。

### Agents（自動委譲）

| エージェント | 用途 | トリガー例 |
|-------------|------|-----------|
| **code-reviewer** | コード変更後のレビュー | 「レビューして」 |
| **lib-researcher** | ライブラリ調査・文書化 | 「このライブラリについて調べて」 |
| **debugger** | エラー調査・修正 | 「エラーが出た」 |
| **refactorer** | リファクタリング | 「シンプルにして」 |

### Skills（自動発動）

| スキル | 用途 | トリガー例 |
|--------|------|-----------|
| **design-tracker** | 設計決定の記録 | 「記録して」 |
| **mcp-builder** | MCPサーバー開発ガイド | 「MCPサーバーを作りたい」 |
| **skill-creator** | 新規スキル作成 | 「スキルを作りたい」 |
| **codex-system** | 複雑なタスクを Codex CLI (System 2) に委譲 | 「深く考えて」「second opinion」 |

### Commands（明示的呼び出し）

#### Claude Code コマンド

| コマンド | 用途 |
|---------|------|
| `/init` | プロジェクト分析・AGENTS.md 生成 |
| `/plan <feature>` | 実装計画の立案 |
| `/tdd <feature>` | テスト駆動開発ワークフロー |
| `/research-lib <library>` | ライブラリを調査してドキュメント化 |
| `/simplify <path>` | 指定コードをシンプルにリファクタリング |
| `/update-design` | 会話から設計ドキュメントを更新 |
| `/update-lib-docs` | ライブラリドキュメントを最新化 |

#### Codex CLI プロンプト

> 使用するには `~/.codex/prompts/` へコピーが必要

| コマンド | 用途 |
|---------|------|
| `/prompts:analyze <topic>` | 問題を深く分析し、選択肢とトレードオフを整理 |
| `/prompts:review-architecture <path>` | アーキテクチャをレビュー、懸念点と推奨事項を提示 |
| `/prompts:consult <question>` | Claude Code からの相談に回答 |
| `/prompts:update-design` | 設計判断を整理して記録 |

### Rules（常時適用）

| ルール | 内容 |
|--------|------|
| **coding-principles** | シンプルさ，単一責任，早期リターン，型ヒント |
| **dev-environment** | uv，ruff，ty，marimo の使用方法 |
| **security** | 機密情報管理，入力検証，SQLi/XSS防止 |
| **testing** | TDD，AAA パターン，カバレッジ 80% |

---

## ドキュメント参照

- 設計決定・アーキテクチャ: `.claude/docs/DESIGN.md`
- ライブラリ文書: `.claude/docs/libraries/`
- コーディングルール: `.claude/rules/`

---

## 開発方針

### コーディング原則

- **シンプルさを最優先** - 複雑より読みやすさ
- **単一責任** - 1関数/クラスは1つのことだけ
- **早期リターン** - ネストを浅く
- **型ヒント必須** - すべての関数に型アノテーション
{ユーザーが追加したルール}

---

## よく使うコマンド

{検出したコマンド（npm scripts, poe tasks, make targets など）}

## 注意事項

- APIキーは環境変数で管理（`.env` はコミットしない）
```

### 4. 確認

生成した AGENTS.md をユーザーに見せ，問題なければ保存．
