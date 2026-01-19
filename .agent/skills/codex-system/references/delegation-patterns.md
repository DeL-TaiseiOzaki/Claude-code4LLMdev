# 委譲パターン詳細

## 委譲判断フローチャート

```
タスク受信
    │
    ▼
┌─────────────────────────┐
│ 明示的な Codex 指示？    │
└───────────┬─────────────┘
    ┌───────┴───────┐
    │ Yes          │ No
    ▼              ▼
  委譲        ┌─────────────────────────┐
              │ 複雑度チェック           │
              └───────────┬─────────────┘
              ┌───────────┴───────────┐
              │ Yes                   │ No
              ▼                       ▼
            委譲              ┌─────────────────────────┐
                              │ 失敗チェック（2回以上）  │
                              └───────────┬─────────────┘
                              ┌───────────┴───────────┐
                              │ Yes                   │ No
                              ▼                       ▼
                            委譲              ┌─────────────────────────┐
                                              │ 品質・セキュリティ要件  │
                                              └───────────┬─────────────┘
                                              ┌───────────┴───────────┐
                                              │ Yes                   │ No
                                              ▼                       ▼
                                            委譲              Claude Code で実行
```

## パターン別実行例

### Pattern 1: アーキテクチャレビュー

```bash
codex exec \
  --model gpt-5-codex \
  --config model_reasoning_effort="high" \
  --sandbox read-only \
  --full-auto \
  "Review the architecture of src/auth/ module. Focus on:
   1. Single Responsibility adherence
   2. Dependency direction (should flow inward)
   3. Interface design clarity
   4. Extensibility for future auth providers

   Related files: src/auth/**/*.py
   Constraints: Must maintain backward compatibility" 2>/dev/null
```

### Pattern 2: 失敗ベース委譲

```bash
codex exec \
  --model gpt-5-codex \
  --config model_reasoning_effort="high" \
  --sandbox read-only \
  --full-auto \
  "This bug has resisted 2 fix attempts:

   Symptom: Race condition in user session handling

   Previous attempts:
   1. Added mutex lock → Deadlock in high concurrency
   2. Switched to RWLock → Still intermittent failures

   Please analyze from fresh perspective:
   - What root cause might we be missing?
   - Are there architectural issues causing this?
   - What alternative approaches should we consider?" 2>/dev/null
```

### Pattern 3: パフォーマンス最適化

```bash
codex exec \
  --model gpt-5-codex \
  --config model_reasoning_effort="xhigh" \
  --sandbox read-only \
  --full-auto \
  "Optimize the algorithm in src/data/aggregator.py:

   Current: O(n²) nested loops for data aggregation
   Target: O(n log n) or better

   Constraints:
   - Must handle 100K+ records
   - Memory limit: 512MB
   - Cannot change public API

   Provide:
   1. Optimized implementation
   2. Complexity analysis
   3. Benchmark comparison approach" 2>/dev/null
```

### Pattern 4: セキュリティ監査

```bash
codex exec \
  --model gpt-5-codex \
  --config model_reasoning_effort="xhigh" \
  --sandbox read-only \
  --full-auto \
  "Security audit of src/api/auth.py:

   Check for:
   - SQL injection vulnerabilities
   - XSS attack vectors
   - CSRF protection
   - Proper input validation
   - Secure password handling
   - Session management issues

   Output format:
   - CRITICAL: Must fix immediately
   - HIGH: Fix before release
   - MEDIUM: Address in next sprint
   - LOW: Tech debt" 2>/dev/null
```

## 委譲しないケース

| ケース | 理由 |
|--------|------|
| 単純な CRUD 操作 | 定型作業，深い分析不要 |
| 小規模なバグ修正（初回） | まず Claude Code で試行 |
| ドキュメント更新のみ | 創造性より正確性重視 |
| フォーマット・リント修正 | 機械的な処理 |
