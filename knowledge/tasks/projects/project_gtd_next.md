---
type: project
id: project-gtd-next
title: GTD運用（次フェーズ）
project: gtd_next
created: 2026-01-04
updated: 2026-01-04
tags:
- project
- gtd
- obsidian
- dataview
---

# GTD運用（次フェーズ）

## このprojectの役割（ハブ）
- **未実施タスクの束ね**（このproject配下の `status: someday` タスクを進める）
- **関連知識の束ね**（GTD/Dataview/CEのノートにすぐ飛べる）

## 参照（アーカイブ済み計画書）
- [[gtd_implementation_plan_20260101|GTD実装計画書（Obsidian/Dataview中心）]]

## 関連ZK/アイデアノート（情報ハブ）
- [[context_engineering_human_role_ssot_20260104183000|CE: 人はSSOT整備／実行はAI]]
- [[obsidian_gtd_dataview_20251228|Obsidian×GTD×Dataview参考]]
- [[obsidian_dataview_cursor_dynamic_context_20260102|Obsidian/Dataview/Cursorで動的コンテクスト]]
- [[design_philosophy_20251228|Design Philosophy]]
- [[idea_docs_manager_review_mode_20260102|Docs Manager: レビュー・モード案]]
- [[idea_obsidian_plugins_selection_20260102|Obsidianプラグイン選定メモ]]

## タスク一覧（gtd_next）

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

<!-- AUTO:tasks:start -->
## タスク一覧（AUTO）

### someday
- [[task_gtd_next_master_note_name_20260104170000|task-20260104170000: マスターノートのファイル名/配置を確定する]]
- [[task_gtd_next_dataview_query_polish_20260104171000|task-20260104171000: Dataviewクエリ詳細（表示項目/並び順）を確定する]]

### completed
- [[task_gtd_next_master_note_name_20260104170000|task-20260104170000: マスターノートのファイル名/配置を確定する]]
<!-- AUTO:tasks:end -->

