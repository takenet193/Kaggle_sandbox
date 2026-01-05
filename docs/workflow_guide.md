# ワークフローガイド

このドキュメントでは、知識管理から実験実行までの全体的なワークフローを説明します。

## 全体フロー

```
知識収集 → タスク生成 → タスク変換 → エージェント実行 → 結果記録 → フィードバック
```

## ステップ1: 知識収集（Obsidian）

### Zettelkastenノートの作成

1. `knowledge/zettelkasten/` ディレクトリに新しいノートを作成
2. タイムスタンプベースのIDで命名（例: `20240101000000_kaggle_basics.md`）
3. ノートに知識を記録し、関連ノートへのリンクを追加

### ノートの例

```markdown
---
id: 20240101000000
title: ターゲットエンコーディング
tags: [feature-engineering, encoding]
links: [20240102000000]
created: 2024-01-01
updated: 2024-01-15
---

# ターゲットエンコーディング

## 内容
カテゴリカル変数を数値に変換する手法。
各カテゴリの平均ターゲット値を特徴量として使用。

## 関連ノート
- [[20240102000000]] クロスバリデーション

## 実装アイディア
- sklearnのTargetEncoderを使用
- クロスバリデーションでリークを防ぐ
```

## ステップ2: タスク生成（GTD）

### タスクの作成

1. 知識ノートから実装可能なタスクを特定
2. `knowledge/inbox/` にタスク/アイデア/メモを追加（共通Inbox）
3. タスクとして採用する場合は `knowledge/tasks/{active|waiting|someday}/` に **コピーしてSSOT化**し、元のInboxファイルは `knowledge/inbox/archive/` に移動（入力ログとして保持）。必要に応じてメタデータに `related_notes` を記録

> 運用ルールの詳細（レビュー・モード、SSOT、コピー→アーカイブ等）は `.cursor/docs_manager_rules.mdc` を参照してください。

### タスクの例

```markdown
---
id: task-001
title: ターゲットエンコーディングの実装
status: active
priority: high
project: feature_engineering
context: experiment
due_date: 2024-01-20
tags: [feature-engineering, encoding]
related_notes: [20240101000000]
assigned_agent: planner
dependencies: []
created: 2024-01-15
updated: 2024-01-15
expected_outcome:
  type: experiment
  metrics: [RMSE]
  target_improvement: "0.15 -> 0.12"
---

# ターゲットエンコーディングの実装

## 目的
カテゴリカル変数にターゲットエンコーディングを適用し、モデル性能を向上させる。

## 手順
1. カテゴリカル変数を特定
2. TargetEncoderを実装
3. クロスバリデーションで評価
4. 結果を記録
```

## ステップ3: タスク変換（JSON）

### MarkdownからJSONへの変換

```bash
python src/task_converter.py
```

このスクリプトは：
- `knowledge/tasks/` 内のMarkdownファイルを読み込み
- JSON形式に変換
- `tasks/` ディレクトリに保存

### 変換後のJSON構造

```json
{
  "id": "task-001",
  "title": "ターゲットエンコーディングの実装",
  "description": "カテゴリカル変数にターゲットエンコーディングを適用...",
  "status": "pending",
  "priority": "high",
  "project": "feature_engineering",
  "context": "experiment",
  "due_date": "2024-01-20",
  "tags": ["feature-engineering", "encoding"],
  "related_notes": ["20240101000000"],
  "assigned_agent": "planner",
  "dependencies": [],
  "metadata": {
    "created": "2024-01-15T10:00:00Z",
    "updated": "2024-01-15T10:00:00Z",
    "source": "knowledge/tasks/active/task-001.md"
  },
  "expected_outcome": {
    "type": "experiment",
    "metrics": ["RMSE"],
    "target_improvement": "0.15 -> 0.12"
  }
}
```

## ステップ4: エージェント実行

### Plannerエージェントの動作

1. **タスク読み取り**: `src/task_loader.py` を使用して未処理タスクを読み込む
2. **計画立案**: タスクを具体的な実装ステップに分解
3. **エージェント割り当て**: 各ステップを適切なエージェントに割り当て

### 実行フロー

```
Planner → Developer → Validator → Docs Manager → Version Controller
```

各エージェントの詳細は `.cursor/kaggle_team.mdc` と `.cursor/experiment_flow_instructions.mdc` を参照。

## ステップ5: 結果記録

### 実験結果の記録

1. **実験ディレクトリ**: `experiments/experiment{N}_{description}/` に結果を保存
2. **知識ノートへの反映**: 実験結果を元の知識ノートに追加
3. **タスクの完了**: タスクを `knowledge/tasks/completed/` に移動

### 結果記録の例

```markdown
## 実験結果（2024-01-15）

### 実装内容
- TargetEncoderを使用してカテゴリカル変数をエンコーディング
- 5-foldクロスバリデーションで評価

### 結果
- RMSE: 0.12（改善: 0.15 → 0.12）
- クロスバリデーションスコア: 0.118 ± 0.008

### 学び
- ターゲットエンコーディングは効果的
- クロスバリデーションが重要
```

## ステップ6: フィードバックループ

### 知識の更新

1. **新しい知識ノート**: 実験から得られた学びを新しいノートとして記録
2. **既存ノートの更新**: 関連する既存ノートにリンクを追加
3. **新しいタスク**: 学びから新しい実装アイディアをタスクとして生成

### 循環の完成

```
知識 → タスク → 実験 → 学び → 知識 → ...
```

この循環により、知識とタスクが有機的に成長していきます。

## 実践例

### 例1: 新しい特徴量エンジニアリング手法の実装

1. **知識収集**: Kaggleのディスカッションから新しい手法を発見
2. **ノート作成**: `knowledge/zettelkasten/20240115000000_polynomial_features.md` を作成
3. **タスク生成**: `knowledge/inbox/` にメモとして追加 → タスク化して `knowledge/tasks/active/` 等へ移動
4. **タスク変換**: `python src/task_converter.py` を実行
5. **エージェント実行**: Plannerがタスクを読み取り、実装を開始
6. **結果記録**: 実験結果を記録し、知識ノートを更新

### 例2: モデルアンサンブルの実験

1. **知識収集**: アンサンブル手法について調査
2. **ノート作成**: 複数のノートを作成し、相互にリンク
3. **タスク生成**: アンサンブル実装のタスクを作成
4. **タスク変換**: JSON形式に変換
5. **エージェント実行**: 複数のモデルを訓練し、アンサンブル
6. **結果記録**: アンサンブルの効果を記録

## ベストプラクティス

### 知識管理
- ノートは小さく、焦点を絞る
- 関連ノートへのリンクを積極的に作成
- 定期的にノートをレビューし、整理

### タスク管理
- タスクは具体的で実装可能なものにする
- 依存関係を明確に記録
- 期待される成果を定量化

### 実験管理
- 各実験の目的を明確にする
- 結果を詳細に記録
- 失敗した実験からも学びを抽出

