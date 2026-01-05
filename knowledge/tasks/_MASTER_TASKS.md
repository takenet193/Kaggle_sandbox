---
id: master-tasks
title: MASTER TASKS
type: dashboard
created: 2026-01-04
updated: 2026-01-04
---

# MASTER TASKS

このノートは **Obsidian（Dataview）上で開く**ことを前提としたタスクダッシュボードです。  
SSOTは `knowledge/tasks/` のタスクノートで、ここは「表示（生成物）」です。

---

## Projects（プロジェクト一覧）

```dataview
TABLE WITHOUT ID
  project,
  length(filter(rows, (r) => r.status = "active")) AS active,
  length(filter(rows, (r) => r.status = "waiting")) AS waiting,
  length(filter(rows, (r) => r.status = "someday")) AS someday,
  length(filter(rows, (r) => r.status = "completed")) AS completed,
  length(rows) AS total
FROM "knowledge/tasks"
WHERE type = "task" AND project != null
GROUP BY project
SORT active DESC, waiting DESC, someday DESC, completed DESC, project ASC
```

## Projects（activeが無いもの）

```dataview
TABLE WITHOUT ID
  project,
  length(rows) AS total,
  length(filter(rows, (r) => r.status = "waiting")) AS waiting,
  length(filter(rows, (r) => r.status = "someday")) AS someday
FROM "knowledge/tasks"
WHERE type = "task" AND project != null
GROUP BY project
WHERE length(filter(rows, (r) => r.status = "active")) = 0
SORT waiting DESC, someday DESC, project ASC
```

---

## Inbox（未整理タスク候補 / type: task）

```dataview
TABLE WITHOUT ID
  default(id, file.name) AS id,
  link(file.path, default(title, file.name)) AS item,
  type,
  created,
  updated
FROM "knowledge/inbox"
WHERE type = "task"
SORT updated DESC
```

---

## Active（Ready / 依存なし）

```dataview
TABLE WITHOUT ID
  default(id, file.name) AS id,
  link(file.path, default(title, file.name)) AS task,
  priority,
  due_date,
  project,
  mode,
  context,
  assignee,
  updated
FROM "knowledge/tasks/active"
WHERE status = "active"
WHERE length(default(dependencies, [])) = 0
SORT choice(priority = "critical", 0,
  choice(priority = "high", 1,
    choice(priority = "medium", 2, 3))) ASC,
  due_date ASC,
  updated DESC
```

## Active（Blocked / dependenciesあり）

> 注: 依存タスクが「完了済みかどうか」まで厳密に判定するには DataviewJS が必要です。  
> まずは **dependenciesがあるもの**をBlockedとして別枠に出します（運用で整える）。

```dataview
TABLE WITHOUT ID
  default(id, file.name) AS id,
  link(file.path, default(title, file.name)) AS task,
  priority,
  due_date,
  project,
  mode,
  context,
  dependencies,
  assignee,
  updated
FROM "knowledge/tasks/active"
WHERE status = "active"
WHERE length(default(dependencies, [])) > 0
SORT choice(priority = "critical", 0,
  choice(priority = "high", 1,
    choice(priority = "medium", 2, 3))) ASC,
  due_date ASC,
  updated DESC
```

---

## Waiting

```dataview
TABLE WITHOUT ID
  default(id, file.name) AS id,
  link(file.path, default(title, file.name)) AS task,
  priority,
  due_date,
  project,
  waiting_for,
  assignee,
  updated
FROM "knowledge/tasks/waiting"
WHERE status = "waiting"
SORT choice(priority = "critical", 0,
  choice(priority = "high", 1,
    choice(priority = "medium", 2, 3))) ASC,
  due_date ASC,
  updated DESC
```

---

## Someday

```dataview
TABLE WITHOUT ID
  default(id, file.name) AS id,
  link(file.path, default(title, file.name)) AS task,
  priority,
  project,
  mode,
  context,
  assignee,
  updated
FROM "knowledge/tasks/someday"
WHERE status = "someday"
SORT choice(priority = "critical", 0,
  choice(priority = "high", 1,
    choice(priority = "medium", 2, 3))) ASC,
  updated DESC
```

---

## Overdue（期限切れ / 未完了）

```dataview
TABLE WITHOUT ID
  default(id, file.name) AS id,
  link(file.path, default(title, file.name)) AS task,
  status,
  priority,
  due_date,
  project,
  assignee,
  updated
FROM "knowledge/tasks"
WHERE due_date != null
  AND due_date < date(today)
  AND status != "completed"
SORT choice(priority = "critical", 0,
  choice(priority = "high", 1,
    choice(priority = "medium", 2, 3))) ASC,
  due_date ASC,
  updated DESC
```

---

## Completed

```dataview
TABLE WITHOUT ID
  default(id, file.name) AS id,
  link(file.path, default(title, file.name)) AS task,
  completed_date,
  project,
  assignee,
  updated
FROM "knowledge/tasks/completed"
WHERE status = "completed"
SORT default(completed_date, updated) DESC
```


