---
type: project
id: project-<project>
title: ""
project: ""
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [project]
links: []
---

# Project: （project）

## 目的 / 成果物
- 

## 状態メモ
- 

## 関連ノート（情報ハブ）
- 

## タスク一覧（Dataview）

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


