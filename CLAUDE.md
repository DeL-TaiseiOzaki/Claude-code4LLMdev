# プロジェクト概要

LLM/エージェント開発プロジェクト

## 言語設定

- **思考・推論**: 英語で行う
- **コード**: 英語（変数名，関数名，コメント，docstring）
- **ユーザーとのやり取り**: 日本語で出力

## 技術スタック

- 言語: Python
- 主要ライブラリ: <!-- 使用ライブラリを記入 -->

## 開発方針

### コーディング原則
- **シンプルさを最優先** - 複雑なコードより読みやすいコードを選ぶ
- **単一責任** - 1つの関数/クラスは1つのことだけを行う
- **早期リターン** - ネストを浅く保つ
- **型ヒント必須** - すべての関数に型アノテーション
- **英語でコーディング** - 変数名，関数名，コメント，docstringはすべて英語

### ライブラリ管理
- 各ライブラリの機能・制約を `docs/libraries/` に文書化
- バージョン固定は `requirements.txt` または `pyproject.toml` で管理
- ライブラリ間の依存関係・競合に注意

### 情報収集
- **最新情報はWeb検索を活用** - ライブラリの仕様変更，ベストプラクティスは常に確認
- 公式ドキュメント，GitHub Issues，Discussionsを参照
- 不明点は推測せず，必ず調査する

## ライブラリドキュメント

@.claude/docs/libraries/ を参照（各ライブラリの機能・制約・使用パターン）

## よく使うコマンド

```bash
# 仮想環境
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# 依存関係
pip install -r requirements.txt
pip install -e .

# テスト
pytest
pytest -v --tb=short

# リント・フォーマット
ruff check .
ruff format .

# 型チェック
mypy src/
```

## ディレクトリ構造

```
src/
├── agents/        # エージェント実装
├── llm/           # LLMラッパー・クライアント
├── tools/         # ツール定義
├── prompts/       # プロンプトテンプレート
└── utils/         # ユーティリティ

docs/
└── libraries/     # ライブラリごとのドキュメント

tests/
└── ...
```

## 注意事項

- APIキーは環境変数で管理（`.env`はコミットしない）
- トークン消費に注意（特に長いコンテキスト）
- Rate limitに注意（リトライロジック実装推奨）
