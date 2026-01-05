# スクリプト一覧と説明

このドキュメントでは、プロジェクト内の各スクリプトの目的、使い方、入出力を説明します。

---

## 1. `src/task_converter.py`

### 目的

タスクをMarkdown（Obsidian形式）からJSONに変換するスクリプト。  
Zettelkasten + GTD形式のタスクをマルチエージェントシステムが読み取れるJSON形式に変換します。

### 使い方

```bash
python src/task_converter.py
```

### 入力

- `knowledge/tasks/{active|waiting|someday|completed}/` 配下のMarkdownファイル（`.md`）
  - ファイル名が `_` で始まるものは除外されます

### 出力

- `tasks/current_sprint.json`
  - 全タスクを集約したJSONファイル
  - タスクは優先度・ステータス・期日・更新日時でソートされます

### 主要機能

- **Markdownパース**: YAML frontmatterからタスク情報を抽出
- **ステータス変換**: ディレクトリ名（`active`等）→ JSONステータス（`in_progress`等）
- **ソート**: ブロック状態 → 優先度 → 期日 → 更新日時 → ID の順でソート
- **エラーハンドリング**: パースエラーが発生したファイルはスキップし、エラーメッセージを表示

### 出力JSONの構造

```json
{
  "generated_at": "2026-01-05T00:00:00",
  "total_tasks": 5,
  "tasks": [
    {
      "type": "task",
      "id": "task-001",
      "title": "タスクタイトル",
      "status": "in_progress",
      "priority": "high",
      "project": "kaggle",
      "mode": "experiment",
      "context": ["note_id_1"],
      "due_date": "2026-01-10",
      "tags": ["kaggle", "experiment"],
      "related_notes": [],
      "dependencies": [],
      "assignee": null,
      "assigned_agent": "planner",
      "source_file": "knowledge/tasks/active/task_001.md",
      "updated_at": "2026-01-05T00:00:00"
    }
  ]
}
```

### 注意事項

- **SSOT（Single Source of Truth）**: `knowledge/tasks/` のMarkdownファイルが真実の源です
- **手編集禁止**: `tasks/current_sprint.json` は自動生成されるため、**手で編集しないでください**
- **実行タイミング**: タスクを追加・更新・移動した後に実行してください

---

## 2. `src/task_loader.py`

### 目的

マルチエージェントシステムがタスクJSONを読み取るためのユーティリティ。  
Plannerエージェントがタスクを読み取り、分解して各エージェントに割り当てる際に使用します。

### 使い方

```python
from src.task_loader import load_pending_tasks, load_task, format_task_for_planner

# 未処理タスクを読み込む
pending = load_pending_tasks()

# 特定のタスクを読み込む
task = load_task("task-001")

# Planner向けにフォーマット
formatted = format_task_for_planner(task)
```

### 主要関数

#### `load_task(task_id: str, tasks_dir: Path = Path("tasks")) -> Optional[Dict]`

特定のタスクを読み込む。

**引数**:
- `task_id`: タスクID
- `tasks_dir`: タスクJSONファイルのディレクトリ（デフォルト: `tasks/`）

**戻り値**: タスク情報の辞書、見つからない場合は `None`

#### `load_pending_tasks(tasks_dir: Path = Path("tasks")) -> List[Dict]`

未処理のタスク（`status: "pending"`）をすべて読み込む。

**戻り値**: 未処理タスクのリスト

#### `load_active_tasks(tasks_dir: Path = Path("tasks")) -> List[Dict]`

進行中のタスク（`status: "in_progress"`）をすべて読み込む。

**戻り値**: 進行中タスクのリスト

#### `load_tasks_by_project(project: str, tasks_dir: Path = Path("tasks")) -> List[Dict]`

特定のプロジェクトのタスクを読み込む。

**引数**:
- `project`: プロジェクト名

**戻り値**: プロジェクトのタスクリスト

#### `load_tasks_index(tasks_dir: Path = Path("tasks")) -> Optional[Dict]`

タスクインデックスファイル（`current_sprint.json`）全体を読み込む。

**戻り値**: インデックス情報の辞書（`generated_at`, `total_tasks`, `tasks` を含む）

#### `format_task_for_planner(task: Dict) -> str`

タスクをPlannerエージェントが読みやすい形式にフォーマット。

**戻り値**: フォーマットされた文字列（Markdown形式）

### 使用例

```bash
# コマンドラインから実行
python src/task_loader.py
```

未処理タスクの最初の3件を表示します。

---

## 3. `src/sync_project_links.py`

### 目的

Project（プロジェクトハブノート）とTask（タスクノート）間のリンクを自動同期するスクリプト。  
Obsidianプラグイン不要で、Markdownファイルを直接編集します。

### 使い方

```bash
# 通常実行（ファイルを更新）
python src/sync_project_links.py

# ドライラン（変更内容を確認のみ、ファイルは更新しない）
python src/sync_project_links.py --dry-run
```

### 動作

1. **タスク → プロジェクトリンク**: 各タスクノートに、所属プロジェクトへのリンクを自動追加
   - マーカー: `<!-- AUTO:project:start -->` と `<!-- AUTO:project:end -->` の間
2. **プロジェクト → タスク一覧**: 各プロジェクトハブノートに、所属タスクの一覧を自動生成
   - マーカー: `<!-- AUTO:tasks:start -->` と `<!-- AUTO:tasks:end -->` の間
   - タスクはステータス（active/waiting/someday/completed/archive）ごとにグループ化

### 前提条件

- タスクノートのfrontmatterに `project: <project名>` が設定されていること
- プロジェクトハブノートは `knowledge/tasks/projects/project_<project名>.md` に配置される

### 注意事項

- **自動生成セクション**: マーカーで囲まれた部分は自動生成されるため、手で編集しても上書きされます
- **プロジェクトハブノートの自動作成**: 存在しないプロジェクトハブノートは自動で作成されます

---

## スクリプト実行のワークフロー

### 典型的な使用フロー

1. **タスク作成・更新**: `knowledge/tasks/` にMarkdownファイルを追加・編集
2. **JSON変換**: `python src/task_converter.py` を実行
3. **エージェント実行**: Plannerが `tasks/current_sprint.json` を読み取り、タスクを分解
4. **タスク完了**: タスクを `knowledge/tasks/completed/` に移動
5. **再変換**: `python src/task_converter.py` を再実行（必要に応じて）

---

## トラブルシューティング

### `task_converter.py` でエラーが出る場合

- **YAML frontmatterの形式を確認**: `---` で囲まれているか、閉じタグがあるか
- **ファイルエンコーディング**: UTF-8で保存されているか確認
- **パス**: スクリプトはリポジトリルートから実行してください

### `task_loader.py` でタスクが見つからない場合

- **`current_sprint.json` が存在するか確認**: 先に `task_converter.py` を実行してください
- **タスクIDの確認**: 大文字小文字・ハイフン/アンダースコアの違いに注意

---

## 関連ドキュメント

- **タスク管理（GTD）**: `knowledge/tasks/_gtd_guide.md`
- **ワークフローガイド**: `docs/workflow_guide.md`
- **Docs Managerルール**: `.cursor/docs_manager_rules.mdc`

