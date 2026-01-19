---
name: codex-system
description: |
  Delegate tasks to Codex CLI (System 2) for deep analysis, complex reasoning,
  or second opinions. Triggers on: architecture decisions, algorithm optimization,
  persistent bugs (2+ failed attempts), security review, performance analysis,
  multi-file refactoring, or explicit requests like "think deeper", "analyze this",
  "second opinion", "consult codex".
metadata:
  short-description: Claude Code ↔ Codex CLI System 2 collaboration
---

# Codex System — Claude Code の System 2

Claude Code（System 1: 即応・実行）と Codex CLI（System 2: 深い思考・分析）の協調システム．

## 委譲条件（自動トリガー）

以下の条件のいずれかを満たす場合，Codex に委譲する：

### 1. 明示的リクエスト
- `think deeper`, `analyze this`, `second opinion` などのキーワード
- `consult codex`, `ask codex`, `codex で考えて` など直接指示

### 2. 複雑度ベース
- アーキテクチャ決定が必要（新規コンポーネント設計，依存関係変更）
- 10+ ファイルに影響する変更
- 複雑なアルゴリズム設計・最適化（O(n²) 以上）
- 深くネストした条件分岐（3+ レベル）

### 3. 失敗ベース
- 同じ問題を 2 回以上試行しても解決しない
- テストが繰り返し失敗
- エラーの根本原因が不明

### 4. 品質・セキュリティ
- セキュリティに関わる変更（認証，認可，暗号化）
- パフォーマンスクリティカルな処理
- 本番環境に影響するリファクタリング

## 実行方法

### 基本形式

```bash
codex exec \
  --model gpt-5-codex \
  --sandbox read-only \
  --full-auto \
  "{prompt}" 2>/dev/null
```

### reasoning effort を指定

```bash
codex exec \
  --model gpt-5-codex \
  --config model_reasoning_effort="high" \
  --sandbox read-only \
  --full-auto \
  "{prompt}" 2>/dev/null
```

### セッション継続

```bash
# 最後のセッションを継続
codex exec resume --last "{follow_up_prompt}" 2>/dev/null

# 特定のセッションを継続
codex exec resume {SESSION_ID} "{follow_up_prompt}" 2>/dev/null
```

## Agent 種別

タスク内容に応じて以下の役割で Codex を活用：

| Agent | 用途 | reasoning_effort |
|-------|------|------------------|
| Architect | アーキテクチャ設計・レビュー | high |
| Analyzer | 深い問題分析・デバッグ | high |
| Optimizer | パフォーマンス・アルゴリズム最適化 | xhigh |
| Security | セキュリティ監査 | xhigh |

## プロンプト構築

Codex への委譲時は以下の情報を含める：

1. **目的**: 何を達成したいか
2. **コンテキスト**: 関連ファイル，現在の状態
3. **制約**: 守るべきルール，使用可能な技術
4. **過去の試行**（失敗ベースの場合）: 何を試して何が失敗したか

## 注意事項

- `2>/dev/null` で thinking tokens を抑制（コンテキスト節約）
- `--full-auto` は CI/Claude Code 環境で必須
- `--skip-git-repo-check` は Git 管理外ディレクトリでのみ使用
- セッション ID を記録して継続実行を活用
