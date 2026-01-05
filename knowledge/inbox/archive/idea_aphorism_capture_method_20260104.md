---
created: 2026-01-04
type: idea
status: archived
tags: [zettelkasten, aphorism, workflow, properties]
promoted_to: aphorism_capture_method_20260104235110
promoted_at: 2026-01-04
---

# アフォリズムの登録方法を検討する

## 目的
- アフォリズムを「フォルダではなくプロパティ」で管理する前提で、最小の摩擦で登録・育成できる方法を決める。

## 論点
- アフォリズムは permanent に置くか、まず inbox/references に置いてから昇格させるか
- 必須プロパティ（最小）を何にするか（例: type/form/status/tags/links/source/quote）
- 孫引き（引用チェーン）をどう表現するか（source_seen / source_claimed / citation_chain など）
- status運用（inbox → seed → evergreen 等）を採用するか、別の粒度にするか

## たたき台（最小案）
- `type: aphorism`
- `status: inbox|seed|evergreen`
- `quote_original` / `quote_translation`（引用の場合のみ）
- `source_seen`（自分が実際に読んだもの）
- `citation_chain`（孫引きの場合のみ）
- `tags` と `links`

## 次アクション
- 既存の zettelkasten frontmatter（id/title/author/tags/links/created/updated）との整合を確認
- Obsidian側のテンプレ/Dataviewでの取り回しを検討



