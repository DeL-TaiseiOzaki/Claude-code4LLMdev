# Claude Code Starter Kit

既存のコードベースに Claude Code の設定を一発で導入するためのスターターキットです。

## 導入方法

```bash
# 1. 既存プロジェクトのルートに移動
cd your-project

# 2. このリポジトリをクローン
git clone --depth 1 https://github.com/DeL-TaiseiOzaki/Claude-code4LLMdev.git .claude-starter

# 3. 必要なファイルをコピー
cp -r .claude-starter/.agent .
cp -r .claude-starter/.claude .
cp -r .claude-starter/.codex .
cp .claude-starter/AGENTS.md .
cp -P .claude-starter/CLAUDE.md .  # シンボリックリンクを保持

# 4. クローンしたディレクトリを削除
rm -rf .claude-starter

# 5. .gitignore に追加（ローカル設定として使う場合）
cat >> .gitignore << 'EOF'

# Claude Code / Codex CLI (local config)
.agent/
.claude/
.codex/
AGENTS.md
CLAUDE.md
EOF

# 6. または、チームで共有する場合はコミット
# git add .agent .claude .codex AGENTS.md CLAUDE.md
# git commit -m "Add Claude Code configuration"
```

**ワンライナー版（.gitignore に追加）:**
```bash
git clone --depth 1 https://github.com/DeL-TaiseiOzaki/Claude-code4LLMdev.git .claude-starter && \
cp -r .claude-starter/.agent .claude-starter/.claude .claude-starter/.codex .claude-starter/AGENTS.md . && \
cp -P .claude-starter/CLAUDE.md . && rm -rf .claude-starter && \
echo -e "\n# Claude Code / Codex CLI\n.agent/\n.claude/\n.codex/\nAGENTS.md\nCLAUDE.md" >> .gitignore
```

## 導入後にやること

1. **Claude Code または Codex CLI を起動**
2. **`/init` を実行** - プロジェクトを分析して AGENTS.md を自動生成
3. **`.claude/settings.json` を確認** - 必要に応じて権限を調整

## 含まれるもの

### ディレクトリ構成

```
.claude/                   # Claude Code（System 1）の設定・知識ベース
├── settings.json          # 権限設定
├── agents/                # サブエージェント
├── docs/                  # 知識ベース（実体）
│   ├── DESIGN.md          # 設計ドキュメント
│   └── libraries/         # ライブラリ文書
├── skills -> ../.agent/skills
└── commands -> ../.agent/commands

.agent/                    # 共通ツール
├── commands/              # Claude Code 用コマンド
├── skills/                # 自動発動スキル
└── docs -> ../.claude/docs   # 知識ベースへのリンク

.codex/                    # Codex CLI（System 2）の設定
├── config.toml            # Codex 設定
└── commands/              # 分析・判断系コマンド

AGENTS.md                  # プロジェクトメモリ（実体）
CLAUDE.md -> AGENTS.md     # シンボリックリンク
```

### サブエージェント

| エージェント | 用途 | トリガー例 |
|-------------|------|-----------|
| **lib-researcher** | ライブラリ調査・文書化 | 「langchainを調べて」 |
| **code-reviewer** | コードレビュー | 「レビューして」 |
| **debugger** | エラー調査・修正 | 「エラーが出た」 |
| **refactorer** | リファクタリング | 「シンプルにして」 |

### スキル（自動発動）

| スキル | 用途 |
|--------|------|
| **design-tracker** | 設計決定を自動で `DESIGN.md` に記録 |
| **mcp-builder** | MCP サーバー開発をガイド |
| **skill-creator** | 新規スキル作成をガイド |
| **codex-system** | 複雑なタスクを Codex CLI (System 2) に委譲 |

## 権限設定

デフォルトで最大権限を付与し、機密ファイルのみ保護:

- **許可**: `Bash(*)`, `Read(*)`, `Edit(*)`, `Write(*)`, `WebFetch(*)`
- **拒否**: `.env`, `*.pem`, `*.key`, `~/.ssh/**`, `~/.aws/**`

必要に応じて `.claude/settings.json` を編集してください。

## Claude Code と Codex CLI の役割分担

本スターターキットでは、2つのツールを **System 1 / System 2** として使い分けます。

| | Claude Code (System 1) | Codex CLI (System 2) |
|---|------------------------|----------------------|
| **役割** | 実行者・即応 | 参謀・深い思考 |
| **得意** | 素早い実装・修正・調査 | 設計判断・複雑な問題分析 |
| **使うとき** | 日常的な開発作業 | 困ったとき・重要な判断 |

### Claude Code のコマンド

| コマンド | 説明 |
|----------|------|
| `/init` | プロジェクトを分析して AGENTS.md を生成 |
| `/research-lib <lib>` | ライブラリを調査して文書化 |
| `/simplify <path>` | コードをシンプルにリファクタリング |
| `/update-design` | 設計ドキュメントを更新 |
| `/update-lib-docs` | ライブラリドキュメントを最新化 |

### Codex CLI のコマンド

| コマンド | 説明 |
|----------|------|
| `/analyze <topic>` | 問題を深く分析し、選択肢とトレードオフを整理 |
| `/review-architecture <path>` | アーキテクチャをレビューし、懸念点と推奨事項を提示 |
| `/consult <question>` | Claude Code からの相談に回答 |
| `/update-design` | 設計判断を整理して記録 |

## カスタマイズ

### AGENTS.md（= CLAUDE.md）

プロジェクト固有のルールを記載します:

- 技術スタック
- コーディング規約
- よく使うコマンド
- 注意事項

### .claude/docs/DESIGN.md

設計決定が自動的に記録されます。Codex の分析結果もここに蓄積されます。

### .claude/docs/libraries/

`/research-lib` コマンドでライブラリの制約・使用パターンが文書化されます。

## ライセンス

MIT
