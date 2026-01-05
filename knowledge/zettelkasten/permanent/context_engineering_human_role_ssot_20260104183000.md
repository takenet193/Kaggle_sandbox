---
id: 20260104183000
title: コンテクストエンジニアリングにおける「人間の役割＝SSOT整備」という再定義
author: takeikumi
type: permanent
tags: [context-engineering, ssot, gtd, obsidian, dataview, ai, workflow, knowledge-management]
links:
  - design_philosophy_20251228
  - obsidian_dataview_cursor_dynamic_context_20260102
  - gtd_implementation_plan_20260101
  - luhmann_communicating_with_slip_boxes_20260104
created: 2026-01-04
updated: 2026-01-04
---

# コンテクストエンジニアリングにおける「人間の役割＝SSOT整備」という再定義

## まとめ（主張）
AI実行が前提のプロジェクトでは、人間の役割は「作業を全部やること」ではなく、**AIが正しく動けるように“真実の源（SSOT）”を整えること**として再定義できる。

この再定義が効くのは、コンテクストエンジニアリング（CE）が本質的に **「コンテクスト生成」と「実行」の分離**を要求するからである。

## 背景：なぜ「分離」が必要か
LLM/AIは、与えられた入力（コンテクスト）に強く依存する。プロジェクトでは次の3つが起きやすい：

- **鮮度の問題**：手作業コピペの「静的コンテクスト」はすぐ古くなる
- **抜け漏れの問題**：都度の編集は漏れや偏りを生む
- **責務の混濁**：誰が何を更新すべきか不明になり、再現性が失われる

したがって、SSOT（更新される原本）を先に定義し、そこからコンテクストを **機械的に抽出・圧縮・整形**して実行に渡す、という分離が合理的になる。

## 再定義：人間が担うべき中核作業
人間が担うべき仕事は、次の2つに収束する：

1) **SSOTを整える（整合・更新・意味付け）**
   - タスクや知識を「機械可読」にする（frontmatter、命名、リンク）
   - 誰が見ても同じ判断ができる粒度に落とす（目的、定義、完了条件）
2) **抽出規則を設計する（何をAIに渡すか）**
   - Dataview等で「動的コンテクスト」を生成する
   - AI向けの派生物（例：`tasks/current_sprint.json`）を決め、決定的に生成する

一方で、実装・分析・整形などの「実行」はAIが担当できる領域が増える。

## このプロジェクトでの具体化（SSOTと派生物）
本プロジェクトの設計は、分離を次のように具体化している：

- **SSOT（人間が整える）**
  - 確定タスク：`knowledge/tasks/`（frontmatter付きタスクノート）
  - 入力ログ：`knowledge/inbox/`（共通Inbox。確定後は tasksへコピー、元はarchive）
  - 知識：`knowledge/zettelkasten/`（permanent/structure/index/references）
- **コンテクスト生成（機械的に作る）**
  - マスターノート：`knowledge/tasks/_MASTER_TASKS.md`（Dataview）
  - AI向け集約：`tasks/current_sprint.json`（status語彙を含めたJSON）
- **実行（AIが担当しやすい）**
  - 生成物を入力に、実装・検証・文書化を進める

## 実務上の効果（運用メリット）
- **鮮度**：SSOTの更新がそのままコンテクストに反映される
- **再現性**：抽出規則が固定され、誰が実行しても同じ入力を作れる
- **合意形成**：チームは「SSOTと規則」に合意すればよく、議論が収束する
- **作業分担**：`assignee`（人間）と `assigned_agent`（AI役割）を分けることで責務が明確になる

## 注意点（落とし穴）
- SSOTが整っていないと、AIは高速に「誤った方向」へ進む（誤加速）
- 生成物（例：JSON）を手でいじると、SSOTが崩れて二重管理になる
- “何を渡すか”の設計が弱いと、情報過多/不足のどちらにも転ぶ

## 関連ノート
- [[design_philosophy_20251228|本プロジェクトの設計思想 - 情報の内的経済圏]]
- [[obsidian_dataview_cursor_dynamic_context_20260102|Obsidian Dataview×Cursorで「動的プロジェクトコンテキスト」を作る手順]]
- [[gtd_implementation_plan_20260101|GTD実装計画書（Obsidian/Dataview中心）]]
- [[luhmann_communicating_with_slip_boxes_20260104|Communicating with Slip Boxes（ルーマン）]]


