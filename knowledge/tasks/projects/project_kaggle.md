---
type: project
id: project-kaggle
title: Kaggle
project: kaggle
created: 2026-01-04
updated: 2026-01-04
tags:
- project
- kaggle
---

# Kaggle

## 目的 / 成果物
- （ここに書く）

## 状態メモ
- （ここに書く）

## タスク一覧（kaggle）

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
SORT choice(status="active",0, choice(status="waiting",1, choice(status="someday",2, 3))) ASC,
  choice(priority="critical",0, choice(priority="high",1, choice(priority="medium",2, 3))) ASC,
  due_date ASC,
  updated DESC
```

---
type: project
project: kaggle
title: kaggle
created: 2026-01-04
updated: 2026-01-04
tags: [project, kaggle]
---

# kaggle

## 概要
Kaggle関連（実験・特徴量・モデル選定・提出）のプロジェクト。

## タスク（未完了）

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
WHERE type = "task"
  AND project = this.project
  AND status != "completed"
SORT choice(priority = "critical", 0,
  choice(priority = "high", 1,
    choice(priority = "medium", 2, 3))) ASC,
  due_date ASC,
  updated DESC
```

## タスク（完了）

```dataview
TABLE WITHOUT ID
  default(id, file.name) AS id,
  link(file.path, default(title, file.name)) AS task,
  completed_date,
  updated
FROM "knowledge/tasks/completed"
WHERE type = "task"
  AND project = this.project
  AND status = "completed"
SORT default(completed_date, updated) DESC
```

<!-- AUTO:tasks:start -->
## タスク一覧（AUTO）

### someday
- [[task_003_baseline_model_20251228|task-003: ベースラインモデルの構築]]
<!-- AUTO:tasks:end -->
