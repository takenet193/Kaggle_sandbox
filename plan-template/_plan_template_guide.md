# タスク管理テンプレート

このテンプレートは、`plan.json` を使ったタスク管理システムを他のプロジェクトに転用するためのものです。

## 構成

```
plan-template/
├── .cursor/
│   └── plan.json              # タスク管理のメインファイル（テンプレート）
├── docs/
│   ├── ROADMAP.md             # 自動生成されるロードマップ（説明のみ）
│   ├── tasks/                 # タスク詳細ドキュメント用ディレクトリ
│   │   └── _tasks_detail_guide.md
│   └── reports/               # タスクレポート用ディレクトリ
│       └── _reports_guide.md
├── scripts/
│   └── generate_roadmap.py    # plan.jsonからROADMAP.mdを生成するスクリプト
└── _plan_template_guide.md    # このファイル
```

## セットアップ手順

1. **このテンプレートをプロジェクトにコピー**
   ```bash
   cp -r plan-template/.cursor your-project/
   cp -r plan-template/docs your-project/
   cp -r plan-template/scripts your-project/
   ```

2. **plan.jsonを編集**
   - `.cursor/plan.json` を開いて、プロジェクトに合わせてタスクを追加・編集
   - サンプルタスクは削除して、実際のタスクに置き換えてください

3. **ROADMAP.mdを生成**
   ```bash
   python scripts/generate_roadmap.py
   ```

## plan.jsonの構造

### 基本構造

```json
{
  "version": "1.0",
  "schema_version": 2,
  "description": "説明文",
  "items": [
    {
      "id": "タスクID（一意）",
      "title": "タスク名",
      "summary": "タスクの概要",
      "status": "pending|in_progress|completed",
      "category": "core|stretch（任意）",
      "start_date": "YYYY-MM-DD（任意）",
      "end_date": "YYYY-MM-DD（任意）",
      "actual_start_date": "YYYY-MM-DD（任意）",
      "actual_end_date": "YYYY-MM-DD（任意）",
      "progress_perc": 0-100,
      "deps": ["依存タスクIDの配列"],
      "detail_markdown": "docs/tasks/タスクID.md（任意）",
      "report_markdown": "docs/reports/タスクID.md（任意）"
    }
  ],
  "notes": {
    "strategy": "任意のメモ",
    "base_branch": "任意のブランチ名"
  }
}
```

### フィールドの説明

- **id**: タスクの一意識別子（必須）
- **title**: タスクの表示名（必須）
- **summary**: タスクの概要説明（推奨）
- **status**: タスクの状態
  - `pending`: 未着手
  - `in_progress`: 進行中
  - `completed`: 完了
- **category**: タスクのカテゴリ（任意）
  - `core`: コアタスク（必須）
  - `stretch`: ストレッチタスク（任意）
- **start_date / end_date**: 計画日付（任意）
- **actual_start_date / actual_end_date**: 実績日付（任意）
- **progress_perc**: 進捗率（0-100、任意）
- **deps**: 依存タスクのID配列（任意）
- **detail_markdown**: タスク詳細ドキュメントのパス（任意）
- **report_markdown**: タスクレポートのパス（任意、完了時のみ）

## 使用方法

### 1. タスクの追加

`plan.json` の `items` 配列に新しいタスクオブジェクトを追加します。

```json
{
  "id": "new-task",
  "title": "新しいタスク",
  "summary": "タスクの概要",
  "status": "pending"
}
```

### 2. タスク詳細ドキュメントの作成

タスクの詳細仕様を記述する場合は、`docs/tasks/` ディレクトリにMarkdownファイルを作成し、`plan.json` の `detail_markdown` フィールドにパスを指定します。

### 3. タスクレポートの作成

タスク完了時は、`docs/reports/` ディレクトリにレポートを作成し、`plan.json` の `report_markdown` フィールドにパスを指定します。

### 4. ROADMAP.mdの更新

タスクの状態を更新したら、以下のコマンドで `ROADMAP.md` を再生成します。

```bash
python scripts/generate_roadmap.py
```

## カテゴリの自動分類

`category` フィールドが指定されていない場合、以下のルールで自動分類されます：

- **Core**: 
  - `status` が `completed` のタスク
  - `start_date` が設定されているタスク
- **Stretch**: 
  - `status` が `pending` で `start_date` が設定されていないタスク

## 注意事項

- `plan.json` は手動で編集します
- `ROADMAP.md` は自動生成されるため、手動で編集しないでください
- タスクの `id` は一意である必要があります
- 依存関係（`deps`）は循環参照を避けてください

## カスタマイズ

`generate_roadmap.py` を編集することで、ROADMAP.mdの生成形式をカスタマイズできます。




