# Kaggle Competition Sandbox

Kaggleコンペ参加のための統合的な開発環境

知識管理（Zettelkasten + GTD）、マルチエージェントシステム、MLOpsパイプラインを統合したワークフローを実現します。

## プロジェクト構成

### 1. 知識とタスクのデータベース
- **Zettelkasten**: 知識ノートの管理（`knowledge/zettelkasten/`）
- **GTD**: タスク管理（`knowledge/tasks/`）
- Obsidianで編集、Gitで管理

### 2. マルチエージェントシステム
- **Planner**: タスク分解・計画立案
- **Developer**: 実装
- **Validator**: 評価
- **Docs Manager**: 文書化
- **Version Controller**: Git管理

### 3. MLOpsパイプライン
- データパイプライン
- モデル訓練・評価
- デプロイメント

## ディレクトリ構造

```
.
├── .cursor/                    # Cursor設定
│   ├── kaggle_team.mdc         # エージェント定義
│   └── experiment_flow_instructions.mdc
│
├── knowledge/                  # Obsidian知識ベース
│   ├── zettelkasten/           # Zettelkasten形式のノート
│   ├── inbox/                  # 収集（共通Inbox: タスク/アイデア/メモ）
│   ├── tasks/                  # GTDタスク管理
│   │   ├── active/             # アクティブなタスク
│   │   ├── waiting/            # 待機中タスク
│   │   ├── someday/            # いつかやるタスク
│   │   ├── completed/          # 完了タスク
│   │   └── archive/            # 意識から外すタスクの保管（ステータスではない）
│   │   └── projects/           # projectハブノート（任意だが推奨）
│   │       └── archive/        # projectハブノートの保管（ステータスではない）
│
├── tasks/                      # タスクJSON（エージェント用・生成物だがGit管理）
│   └── current_sprint.json      # `knowledge/tasks/` を集約したSSOTスナップショット
│
├── data/                       # データ
│   ├── raw/                    # Kaggleからの生データ
│   └── processed/              # 加工済みデータ
│
├── experiments/                # 実験ディレクトリ
│   └── experiment{N}_{description}/
│
├── src/                        # 実行可能なスクリプト
│   ├── task_converter.py       # タスク変換ツール
│   └── task_loader.py          # タスク読み込みツール
│
├── docs/                       # ドキュメント
│   ├── project_architecture.md # プロジェクト全体アーキテクチャ
│   └── workflow_guide.md       # ワークフローガイド
│
└── mcp_setup/                  # MCP設定
```

## ワークフロー

### 1. 知識収集
Obsidianで知識ノートを作成（Zettelkasten形式）

### 2. タスク生成
知識から実装可能なタスクを生成（GTD形式）

### 3. タスク変換
```bash
python src/task_converter.py
```
`knowledge/tasks/` を集約し、`tasks/current_sprint.json` を生成（上書き）します。
（このJSONは**手編集しない**）

### 4. エージェント実行
Plannerが `tasks/current_sprint.json` を読み取り、各エージェントに割り当て

### 5. 結果記録
実験結果を知識ノートに反映

### 6. フィードバックループ
学びから新しい知識ノートを作成

詳細は `docs/workflow_guide.md` を参照してください。

## セットアップ

### 1. 依存関係のインストール
```bash
pip install -r requirements.txt
```

### 2. ディレクトリの作成
```bash
mkdir -p knowledge/{inbox,zettelkasten,tasks/{active,waiting,someday,completed,archive,projects,projects/archive}}
mkdir -p tasks
mkdir -p experiments
```

### 3. Obsidianの設定
`knowledge/` ディレクトリをObsidianのVaultとして開く

## 使い方

### タスクの作成から実行まで

1. **知識ノートの作成**
   - `knowledge/zettelkasten/` に新しいノートを作成
   - タイムスタンプベースのIDで命名（例: `20240101000000_kaggle_basics.md`）

2. **タスクの生成**
   - `knowledge/inbox/` にタスク/アイデア/メモを追加（共通Inbox）
   - タスクとして採用する場合は `knowledge/tasks/{active|waiting|someday}/` に **コピーしてSSOT化**し、元のInboxファイルは `knowledge/inbox/archive/` に移動

3. **タスクの変換**
   ```bash
   python src/task_converter.py
   ```

4. **エージェント実行**
   - Plannerが `tasks/current_sprint.json` からタスクを読み取り
   - タスクを分解し、各エージェントに割り当て

5. **結果の記録**
   - 実験結果を知識ノートに反映
   - タスクを `knowledge/tasks/completed/` に移動

## ドキュメント

- **プロジェクト全体アーキテクチャ**: `docs/project_architecture.md`
- **ワークフローガイド**: `docs/workflow_guide.md`
- **Docs Manager ルール（運用規約）**: `.cursor/docs_manager_rules.mdc`
- **Mermaid図の表示方法**: `docs/MERMAID_VIEWING_GUIDE.md` ⭐ 図が見えない場合はこちら
- **エージェント定義**: `.cursor/kaggle_team.mdc`
- **実験フロー指示**: `.cursor/experiment_flow_instructions.mdc`

## ライセンス

（必要に応じて追加）

