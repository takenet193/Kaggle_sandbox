---
created: 2026-01-04
type: guide
---

# Projects（プロジェクト・ハブ）

`knowledge/tasks/projects/` は、**project単位の“ハブノート”**を置く場所です。

## ディレクトリ構造
- `projects/`: 現行のprojectハブノート
- `projects/archive/`: 役目を終えた/当面追わないprojectハブノートの保管（ステータスではない）

## 目的
- `project` ごとに「何を目指しているか」「次にやるべきことは何か」を1枚で把握する
- Dataviewで、そのprojectに属するタスク（active/waiting/someday/completed）を一覧できるようにする

## ルール（推奨）
- タスク側（SSOT）は `knowledge/tasks/**/task_*.md`（frontmatter付き）
  - `project: <slug>` を入れる
- projectノートは **任意だが強く推奨**
  - 新しいprojectを作ったら `projects/` に1枚追加する

## projectノートの最小テンプレ（例）
```markdown
---
type: project
id: project-infrastructure
title: Infrastructure
project: infrastructure
created: 2026-01-04
updated: 2026-01-04
---

# Infrastructure

## 目的 / 成果物
- （ここに書く）

## 状態メモ
- （ここに書く）

## タスク一覧（このproject）
```dataview
TABLE WITHOUT ID
  default(id, file.name) AS id,
  link(file.path, default(title, file.name)) AS task,
  status,
  priority,
  due_date,
  mode,
  updated
FROM "knowledge/tasks"
WHERE type = "task" AND project = this.project
SORT status ASC, priority DESC, due_date ASC, updated DESC
```
```

---
created: 2026-01-04
type: guide
---

# Projects（プロジェクト・ハブ）

`knowledge/tasks/projects/` は、**プロジェクトのハブノート（司令塔）**を置く場所です。

## 目的
- 各 `project` の「目的・前提・成果物・関連ノート」を1箇所に集約する
- Dataviewで **そのプロジェクトに属するタスク一覧**を自動表示する
- 週次レビューで「どのプロジェクトが動いているか」を素早く把握する

## 最小ルール
- プロジェクトノートは frontmatter に以下を持つ：
  - `type: project`
  - `project: <project_name>`（タスク側の `project` と同じ文字列）

## 推奨ファイル名
- `project_<project_name>.md`（例: `project_infrastructure.md`）

## 運用
- 新しいプロジェクトを始めたら、まずここにプロジェクトノートを作る
- タスクは `knowledge/tasks/*` に作り、`project: <project_name>` で紐付ける


