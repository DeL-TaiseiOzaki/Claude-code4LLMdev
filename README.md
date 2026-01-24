# fastslow-claude-code

Claude Code (Fast/System 1) と Codex CLI (Slow/System 2) と Gemini CLI (Research/Multimodal) の設定を既存プロジェクトに導入するスターターキット。

## コンセプト

| ツール | 役割 | 得意なこと |
|--------|------|-----------|
| **Claude Code** | Fast (System 1) | 素早いコード編集、反復作業 |
| **Codex CLI** | Slow (System 2) | 深い推論、設計判断、デバッグ |
| **Gemini CLI** | Research | 大規模コード理解、調査、マルチモーダル |

## 導入方法

```bash
# 1. 既存プロジェクトのルートで実行
git clone --depth 1 https://github.com/DeL-TaiseiOzaki/fastslow-claude-code.git .starter

# 2. 必要なファイルをコピー
cp -r .starter/.claude .starter/.codex .starter/.gemini .starter/AGENTS.md .
cp -P .starter/CLAUDE.md .

# 3. クリーンアップ
rm -rf .starter

# 4. プロジェクトを初期化
claude  # Claude Code を起動
/init   # AGENTS.md をプロジェクトに合わせて更新
```

**ワンライナー:**
```bash
git clone --depth 1 https://github.com/DeL-TaiseiOzaki/fastslow-claude-code.git .starter && cp -r .starter/.claude .starter/.codex .starter/.gemini .starter/AGENTS.md . && cp -P .starter/CLAUDE.md . && rm -rf .starter
```

## Codex CLI のグローバル設定（初回のみ）

Codex CLI が `.claude/` のコンテキストを読み込むために、以下の設定が必要です:

```bash
# 1. Codex 用グローバル指示をコピー
cp .codex/AGENTS.md ~/.codex/AGENTS.md

# 2. スキル機能を有効化（未設定の場合）
cat >> ~/.codex/config.toml << 'EOF'
[features]
skills = true
EOF
```

## Gemini CLI のセットアップ（初回のみ）

```bash
# 1. Gemini CLI をインストール
npm install -g @google/gemini-cli

# 2. 認証（Google アカウントでログイン）
gemini

# 3. （オプション）グローバル設定をコピー
mkdir -p ~/.gemini
cp .gemini/settings.json ~/.gemini/settings.json
```

**認証方法:**
- **Google アカウント**: 無料枠（60 req/min, 1000 req/day）
- **API キー**: `GEMINI_API_KEY` 環境変数を設定
- **Vertex AI**: エンタープライズ利用

**Gemini CLI の強み:**
- 1M トークンのコンテキストウィンドウ
- Google Search によるグラウンディング
- 動画・音声・PDF のマルチモーダル処理

## 構成

```
.claude/          # Claude Code 設定
├── agents/       # サブエージェント（自動委譲）
├── skills/       # スキル（自動発動・手動起動）
├── rules/        # 常時適用ルール
├── docs/         # 知識ベース
├── hooks/        # 自動トリガー
└── settings.json # 権限設定

.codex/           # Codex CLI 設定
├── AGENTS.md     # グローバル指示（~/.codex/ へコピー）
├── config.toml   # 機能設定
└── skills/       # スキル
    └── context-loader/  # .claude/ コンテキスト読み込み

.gemini/          # Gemini CLI 設定
├── GEMINI.md     # コンテキストファイル
└── settings.json # Gemini CLI 設定

AGENTS.md         # プロジェクト設定（全ツール共通）
CLAUDE.md         # AGENTS.md へのシンボリックリンク
```

## ライセンス

MIT
