---
type: task
id: task-20260104171000
title: Dataviewクエリ詳細（表示項目/並び順）を確定する
author: takeikumi
status: someday
priority: medium
project: gtd_next
mode: writing
context:
- gtd_implementation_plan_20260101
- obsidian_gtd_dataview_20251228
- obsidian_dataview_cursor_dynamic_context_20260102
tags:
- gtd
- obsidian
- dataview
related_notes: []
assignee: null
assigned_agent: null
dependencies: []
created: 2026-01-04
updated: 2026-01-04
---

# Dataviewクエリ詳細（表示項目/並び順）を確定する

## 目的
`_MASTER_TASKS.md` と projectハブノートのDataviewを、運用しやすい形に磨き込む（列・並び順・フィルタの最終決定）。

## 検討観点
- 表示列: id/title/status/priority/due_date/project/mode/context/assignee など
- 並び順: priority → due_date → updated のようなルールを固定
- 例外: due_date未設定の扱い、completedの表示順

## 完了条件
- `_MASTER_TASKS.md` の各セクションのクエリが「迷いなく使える」形で確定している
- 必要なら `knowledge/tasks/_gtd_guide.md` に運用ルールを追記している

<!-- AUTO:project:start -->
- [[project_gtd_next|project: gtd_next]]
<!-- AUTO:project:end -->

