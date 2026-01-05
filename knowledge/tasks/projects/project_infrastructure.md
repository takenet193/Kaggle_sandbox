---
type: project
id: project-infrastructure
title: Infrastructure
project: infrastructure
created: 2026-01-04
updated: 2026-01-04
tags:
- project
- infrastructure
---

# Infrastructure

## 目的 / 成果物


## 状態メモ


## タスク一覧（infrastructure）

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
project: infrastructure
title: infrastructure
created: 2026-01-04
updated: 2026-01-04
tags: [project, infrastructure]
---

# infrastructure

## 概要
このリポジトリの基盤（タスク運用・自動化・環境整備）を整えるプロジェクト。

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

### active
- [[task_001_git_setup_20251228|task-001: Git初期設定とブランチ戦略策定]]

### completed
- [[task_002_task_converter_20251228|task-002: task_converter.py の実装]]
<!-- AUTO:tasks:end -->
