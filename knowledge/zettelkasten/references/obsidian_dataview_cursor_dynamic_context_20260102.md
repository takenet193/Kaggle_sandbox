---
id: 20260102160000
title: Obsidian Dataview×Cursorで「動的プロジェクトコンテキスト」を作る手順
type: reference
source_author: ITアライグマ
source: https://it-araiguma.com/obsidian-dataview-cursor-dynamic-context/#index_id0
tags: [reference, obsidian, dataview, cursor, project-management, context]
created_by: takeikumi
created: 2026-01-02
---

# Obsidian Dataview×Cursorで「動的プロジェクトコンテキスト」を作る手順

## 要旨（短く）

DataviewでVault内の断片情報（タスク・議事録・仕様など）を自動集約し、常に最新の「プロジェクトコンテキスト」を作る。  
そのコンテキストをCursor AIに渡すことで、手動コピペの手間と情報の陳腐化を減らし、抜け漏れを防ぐ。

## 概要

ObsidianのDataviewで複数ノートから情報を自動集約し、「常に最新のコンテキスト」を作ってCursor AIに渡す、という考え方と実装手順を解説した記事。

## 重要な主張（要点）

- **静的コンテキスト（コピペ）**はすぐ古くなる／準備が手間／抜け漏れが出る
- **動的コンテキスト（Dataviewクエリ）**は、元ノート更新に追随して常に最新で、準備コストが下がる
- そのために、各ノートに **Frontmatter（YAML）やインラインフィールド**でメタデータを付ける

## なぜ効くのか（記事の問題設定）

- AIコーディングが普及した今、性能を引き出す鍵は「**良質なコンテクスト（背景情報）**」を与えること
- 仕様書・議事録・タスクリスト等を毎回手でコピペする方式は、手間に加えて「古い情報を渡すリスク」が大きい
- Dataviewで自動集約した「生きたドキュメント」を作ると、更新が追随しやすくなる

## 記事内の具体例（メタデータ）

- 議事録ノートに `type: meeting`, `date`, `participants`, `tags` など
- タスクノートに `type: task`, `status` など

（＝Dataviewが拾える「機械可読な目印」を増やす）

## 実装の骨格（このプロジェクト向けに読み替え）

- **SSOT（真実の源）**：`knowledge/` 配下のノート（特に `knowledge/tasks/` と `knowledge/zettelkasten/`）
- **抽出**：frontmatterやpathで対象を絞る（例：activeだけ、references除外 など）
- **集約先**：AIに渡す「context pack」ノート（人間も読む）
- **更新**：元ノートを更新すれば、集約は常に最新（＝動的）

## 自分の適用メモ（このプロジェクト）

- `knowledge/tasks/` をSSOTとして運用しつつ、将来的に
  - `gtd_implementation_plan_20260101.md` の内容を「動的」に可視化
  - タスクの状況・関連ノート・直近の意思決定を一枚に集約
  - それをAIに渡す
 という構成に繋げられる。

## 関連ノート

- [[obsidian_gtd_dataview_20251228|GTD with Obsidian（DataviewベースのGTDシステム紹介）]]
- [[design_philosophy_20251228|本プロジェクトの設計思想（Context Engineering）]]
- [[context_engineering_human_role_ssot_20260104183000|コンテクストエンジニアリングにおける「人間の役割＝SSOT整備」という再定義]]


