---
id: 20260104223000
type: permanent
title: "GTDシステム（Obsidian/Dataview中心・SSOT=Markdown）の要点"
created: 2026-01-04
tags:
  - gtd
  - obsidian
  - dataview
  - ssot
  - workflow
---

# GTDシステム（Obsidian/Dataview中心・SSOT=Markdown）の要点

参照元（アーカイブ済み計画書）: [[gtd_implementation_plan_20260101|GTD実装計画書（Obsidian/Dataview中心）]]

## 結論（設計の核）
- **SSOTはMarkdown**：タスクの真実は `knowledge/tasks/**/task_*.md`
- **見える化/レビューはObsidianで完結**：Dataviewで一覧・分類・点検
- **Pythonは最小**：AI連携用に `tasks/current_sprint.json` を生成するだけ

## フォルダ運用（GTDフロー）
- **収集（共通Inbox）**：`knowledge/inbox/`
  - タスク候補は `type: task` を推奨
  - 知識/アイデアは `type: idea|note` など
- **確定（コピー→アーカイブ）**：
  - 確定タスクは `knowledge/tasks/{active|waiting|someday|completed}/` に**コピーしてSSOT化**
  - 元のInboxメモは `knowledge/inbox/archive/` に移動（入力ログとして残す）
- **保管（タスク側アーカイブ）**：`knowledge/tasks/archive/`（ステータスではなく置き場）

## ステータス語彙（人間向け）
- `status: active | waiting | someday | completed`
- inboxはステータスではなく「置き場所」（`knowledge/inbox/` にある＝未整理）

## タスクノートのメタデータ（要点）
- **ID**：`task-YYYYMMDDHHMMSS`（同秒衝突時は `-a` 等のサフィックス）
- **type**：`type: task`（Dataviewで括るため）
- **project**：タスクの「まとまり」（同じprojectに複数statusが共存してよい）
- **mode**：実行モード/状況ラベル（例：`setup`, `development`, `experiment`, `writing`, `review`）
- **context**：実行時に参照すべきノート（リンク/IDの配列推奨）
- **related_notes**：周辺・補助の関連（任意）
- **assignee**：人間担当（任意）／ **assigned_agent**：AI担当（任意）

## ダッシュボード（Dataview）
- マスターノート：`knowledge/tasks/_MASTER_TASKS.md`
  - Inbox（`knowledge/inbox/` の `type: task`）
  - Active / Waiting / Someday / Overdue / Completed
  - Projects集計（projectごとのstatus件数、active無しprojectの検出）

## AI連携（JSON生成）
- 生成物：`tasks/current_sprint.json`
- 入力：`knowledge/tasks/{active,waiting,someday,completed}/**/*.md`（archiveは除外）
- statusマッピング（AI向け語彙）：
  - `active -> in_progress`
  - `waiting -> waiting`
  - `someday -> someday`
  - `completed -> completed`

## プロジェクト・ハブ（情報の束ね）
- `knowledge/tasks/projects/` に projectハブノートを置く
- ハブは「タスク一覧」だけでなく、関連ZKノート/運用メモへのリンクも集約して**情報ハブ**として機能させる
- アーカイブ：`knowledge/tasks/projects/archive/`

## この設計がCE（Context Engineering）に合う点
- **生成（コンテクスト作り）**と**実行（AI実装）**を分離し、人間はSSOTを整備する役割に集中できる  
  参照：[[context_engineering_human_role_ssot_20260104183000|CE: 人はSSOT整備／実行はAI]]

## 関連リンク
- 実装の入口（ダッシュボード）：[[../tasks/_MASTER_TASKS|_MASTER_TASKS]]
- projectハブ：[[../tasks/projects/project_gtd_next|GTD運用（次フェーズ）]]
- 参考：[[obsidian_gtd_dataview_20251228|Obsidian×GTD×Dataview参考]]



