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
cp .claude-starter/AGENTS.md .
cp -P .claude-starter/CLAUDE.md .  # シンボリックリンクを保持

# 4. クローンしたディレクトリを削除
rm -rf .claude-starter

# 5. コミット
git add .agent .claude AGENTS.md CLAUDE.md
git commit -m "Add Claude Code configuration"
```

**ワンライナー版:**
```bash
git clone --depth 1 https://github.com/DeL-TaiseiOzaki/Claude-code4LLMdev.git .claude-starter && \
cp -r .claude-starter/.agent .claude-starter/.claude .claude-starter/AGENTS.md . && \
cp -P .claude-starter/CLAUDE.md . && rm -rf .claude-starter
```

## 導入後にやること

1. **`AGENTS.md` を編集** - プロジェクト固有の情報を記入（CLAUDE.md は symlink）
2. **`.claude/settings.json` を確認** - 必要に応じて権限を調整
3. **Claude Code を起動** - `claude` コマンドで開始

## 含まれるもの

### ディレクトリ構成

```
.agent/                    # 共通設定
├── commands/              # スラッシュコマンド
├── docs/
│   ├── DESIGN.md          # 設計ドキュメント（自動更新）
│   └── libraries/         # ライブラリ文書
└── skills/                # 自動発動スキル

.claude/                   # Claude Code 固有設定
├── settings.json          # 権限設定
└── agents/                # サブエージェント

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
| **codex-auto** | 大規模タスクを Codex CLI に自動委譲（任意） |

### コマンド

| コマンド | 説明 |
|----------|------|
| `/research-lib <lib>` | ライブラリを調査して文書化 |
| `/simplify <path>` | コードをシンプルにリファクタリング |
| `/update-design` | 設計ドキュメントを更新 |
| `/update-lib-docs` | ライブラリドキュメントを最新化 |

## 権限設定

デフォルトで最大権限を付与し、機密ファイルのみ保護:

- **許可**: `Bash(*)`, `Read(*)`, `Edit(*)`, `Write(*)`, `WebFetch(*)`
- **拒否**: `.env`, `*.pem`, `*.key`, `~/.ssh/**`, `~/.aws/**`

必要に応じて `.claude/settings.json` を編集してください。

## Codex CLI との併用

`.agent/` ディレクトリは Codex CLI と共有できます。Codex CLI を使う場合は `.codex/config.toml` を追加してください。

```bash
cp -r .claude-starter/.codex .  # Codex CLI 設定も追加する場合
```

## カスタマイズ

### AGENTS.md（= CLAUDE.md）

プロジェクト固有のルールを記載します:

- 技術スタック
- コーディング規約
- よく使うコマンド
- 注意事項

### .agent/docs/DESIGN.md

設計決定が自動的に記録されます。手動で編集も可能です。

### .agent/docs/libraries/

`/research-lib` コマンドでライブラリの制約・使用パターンが文書化されます。

## ライセンス

MIT
