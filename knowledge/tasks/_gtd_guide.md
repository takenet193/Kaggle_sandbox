# タスク管理（GTD形式）

このディレクトリは、Getting Things Done (GTD) の方法論に基づいてタスクを管理します。

## ディレクトリ構造

- `active/`: 現在進行中のタスク
- `waiting/`: 他のタスクや外部要因を待っているタスク
- `someday/`: いつかやるタスク
- `completed/`: 完了したタスク
- `archive/`: 意識に入れる必要がなくなったタスクの保管（ステータスではない）
- `projects/`: project単位のハブノート（任意だが推奨）

※ 未整理の情報（タスク候補/アイデア/メモ）は `knowledge/inbox/`（共通Inbox）に集める。

## タスクファイルの形式

各タスクはMarkdownファイルとして保存され、以下の構造を持ちます：

```markdown
---
type: task
id: task-001
title: 特徴量エンジニアリングの実験
status: active
priority: high
project: feature_engineering
mode: experiment
context: [kaggle_basics_20240101000000] # 実行時に参照すべきノート（最小セット）
due_date: 2024-01-20
tags: [feature-engineering, experiment]
related_notes: [feature_engineering_20240102000000] # 補助的な関連ノート（任意）
assignee: null  # 人間の担当者（任意。未決定なら空/省略でOK）
assigned_agent: planner
dependencies: []
created: 2024-01-15
updated: 2024-01-15
expected_outcome:
  type: experiment
  metrics: [RMSE]
  target_improvement: "0.15 -> 0.12"
---

# 特徴量エンジニアリングの実験

## 目的
カテゴリカル変数のターゲットエンコーディングを実装し、モデルの性能を向上させる。

## 手順
1. カテゴリカル変数を特定
2. ターゲットエンコーディングを実装
3. クロスバリデーションで評価
4. 結果を記録

## 結果
（実験後に記入）

## 学び
（実験後に記入）
```

### フィールドの意図（重要）
- `mode`: 実行モード/状況ラベル（例: `setup`, `development`, `experiment`, `writing`, `review`）
- `context`: **そのタスクを実行するにあたって参照すべきノート**（Obsidianリンク/ノートIDを推奨。単体 or リスト）
- `related_notes`: 周辺・補助的な関連ノート（任意）

## タスクのライフサイクル

1. **収集**: `knowledge/inbox/` にタスク候補を追加（共通Inbox）
2. **確定**: タスクとして確定したら `knowledge/tasks/{active|waiting|someday}/` に **コピーしてSSOT化**し、元inboxファイルは `knowledge/inbox/archive/` に移動
3. **実行**: マルチエージェントシステムにJSON形式で引き渡し
4. **完了**: タスクを `completed/` に移動（必要なら `completed_date` を記入）
5. **退避（任意）**: しばらく経って「もう意識に入れる必要がない」ものは `archive/` に移動

## JSONへの変換

タスクをマルチエージェントシステムに引き渡す際は、`src/task_converter.py` を使用してJSON形式に変換します。

```bash
python src/task_converter.py
```

変換されたJSONファイルは `tasks/` ディレクトリに保存されます。


