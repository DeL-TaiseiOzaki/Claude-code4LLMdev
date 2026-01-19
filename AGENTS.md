# プロジェクト概要

LLM/エージェント開発プロジェクト

## 言語設定

- **思考・推論**: 英語で行う
- **コード**: 英語（変数名，関数名，コメント，docstring）
- **ユーザーとのやり取り**: 日本語で出力

## 技術スタック

- **言語**: Python
- **パッケージ管理**: uv（必須）
- **開発ツール**:
  - ruff（リント・フォーマット）
  - ty（型チェック）
  - poe / poethepoet（タスクランナー）
  - pytest（テスト）
  - marimo（ノートブック環境，オプション）
- **環境管理**: venv（uv経由で管理）
- **主要ライブラリ**: <!-- 使用ライブラリを記入 -->

---

## 拡張機能

このプロジェクトには以下の拡張機能が設定されています。
Claude Code と Codex CLI の両方で利用可能です。

### Agents（自動委譲）

独立したコンテキストで専門タスクを実行するエージェント：

| エージェント | 用途 | トリガー例 |
|-------------|------|-----------|
| **code-reviewer** | コード変更後のレビュー | 「レビューして」「チェックして」 |
| **lib-researcher** | ライブラリ調査・文書化 | 「このライブラリについて調べて」 |
| **debugger** | エラー調査・修正 | 「エラーが出た」「動かない」 |
| **refactorer** | リファクタリング | 「シンプルにして」「整理して」 |

### Skills（自動発動）

会話内容に応じて自動的に発動するスキル：

| スキル | 用途 | トリガー例 |
|--------|------|-----------|
| **design-tracker** | 設計決定の記録 | 「記録して」「アーキテクチャ」 |
| **mcp-builder** | MCPサーバー開発ガイド | 「MCPサーバーを作りたい」 |
| **skill-creator** | 新規スキル作成 | 「スキルを作りたい」 |
| **codex-system** | 複雑なタスクを Codex CLI (System 2) に委譲 | 「深く考えて」「second opinion」 |

### Commands（明示的呼び出し）

`/command` で呼び出すコマンド：

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

> **注意**: 使用するには `cp .codex/prompts/*.md ~/.codex/prompts/` でユーザーレベルにコピーが必要

| コマンド | 用途 |
|---------|------|
| `/prompts:analyze <topic>` | 問題を深く分析し、選択肢とトレードオフを整理 |
| `/prompts:review-architecture <path>` | アーキテクチャをレビュー、懸念点と推奨事項を提示 |
| `/prompts:consult <question>` | Claude Code からの相談に回答 |
| `/prompts:update-design` | 設計判断を整理して記録 |

### Rules（常時適用）

常に従うべきルール（`.claude/rules/`）：

| ルール | 内容 |
|--------|------|
| **coding-principles** | シンプルさ，単一責任，早期リターン，型ヒント |
| **dev-environment** | uv，ruff，ty，marimo の使用方法 |
| **security** | 機密情報管理，入力検証，SQLi/XSS防止 |
| **testing** | TDD，AAA パターン，カバレッジ 80% |

---

## ドキュメント参照

設計決定・アーキテクチャ・実装方針:
- `.claude/docs/DESIGN.md`

各ライブラリの機能・制約・使用パターン:
- `.claude/docs/libraries/`

コーディングルール（常時適用）:
- `.claude/rules/`

## 記憶の整理（自動）

**重要な情報は自動的に記録すること。ユーザーに「覚えておいて」と言われるのを待たない。**

会話中に以下が発生したら、即座に適切な場所に記録する：

| 検出したら | 記録先 | 例 |
|-----------|--------|-----|
| 設計決定・方針決定 | `.claude/docs/DESIGN.md` | 「ReActパターンでいこう」 |
| ライブラリの制約発見 | `.claude/docs/libraries/{name}.md` | 「このAPIは非同期のみ」 |
| プロジェクト固有のルール | この `AGENTS.md` に追記 | 「エラーは日本語で出力」 |

記録後は「DESIGN.mdに記録しました」のように簡潔に報告する。

---

## 開発方針

### コーディング原則
- **シンプルさを最優先** - 複雑なコードより読みやすいコードを選ぶ
- **単一責任** - 1つの関数/クラスは1つのことだけを行う
- **早期リターン** - ネストを浅く保つ
- **型ヒント必須** - すべての関数に型アノテーション
- **英語でコーディング** - 変数名，関数名，コメント，docstringはすべて英語

### ライブラリ管理
- **uvを使用**（pip直接使用は禁止）
- 依存関係は `pyproject.toml` で管理
- 各ライブラリの機能・制約を `.claude/docs/libraries/` に文書化
- ライブラリ間の依存関係・競合に注意

### 情報収集
- **最新情報はWeb検索を活用** - ライブラリの仕様変更，ベストプラクティスは常に確認
- 公式ドキュメント，GitHub Issues，Discussionsを参照
- 不明点は推測せず，必ず調査する

---

## ディレクトリ構造

```
.claude/                   # Claude Code（System 1）の設定・知識ベース
├── settings.json          # 権限設定
├── agents/                # サブエージェント
├── rules/                 # 常時適用ルール
│   ├── coding-principles.md
│   ├── dev-environment.md
│   ├── security.md
│   └── testing.md
├── docs/                  # 知識ベース（実体）
│   ├── DESIGN.md          # 設計ドキュメント
│   └── libraries/         # ライブラリドキュメント
├── skills -> ../.agent/skills
└── commands -> ../.agent/commands

.agent/                    # 共通ツール
├── commands/              # Claude Code 用コマンド
├── skills/                # 自動発動スキル
└── docs -> ../.claude/docs   # 知識ベースへのリンク

.codex/                    # Codex CLI（System 2）の設定
├── skills -> ../.agent/skills  # 共通スキル
└── prompts/               # カスタムプロンプト（~/.codex/prompts/ へコピー）

src/                       # ソースコード
tests/                     # テスト
```

## よく使うコマンド

```bash
# プロジェクト初期化（uv必須）
uv init
uv venv
source .venv/bin/activate  # Linux/Mac

# 依存関係
uv add <package>           # パッケージ追加
uv add --dev <package>     # 開発依存追加
uv sync                    # 依存関係同期

# タスク実行（poethepoet）
poe lint                   # ruff check + format
poe test                   # pytest実行
poe typecheck              # ty実行
poe all                    # 全チェック実行

# 個別実行
uv run ruff check .
uv run ruff format .
uv run ty check src/
uv run pytest -v --tb=short
```

## 注意事項

- APIキーは環境変数で管理（`.env`はコミットしない）
- トークン消費に注意（特に長いコンテキスト）
- Rate limitに注意（リトライロジック実装推奨）
