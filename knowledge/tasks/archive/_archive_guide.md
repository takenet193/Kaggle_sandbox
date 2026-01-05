---
created: 2026-01-04
type: guide
---

# Tasks Archive（タスクのアーカイブ）

`knowledge/tasks/archive/` は、**日々の意識・レビュー対象から外したいタスク**を保管する場所です（削除はしないが、いまは追わない）。

## 位置付け
- `archive` は **ステータスではなく保管場所**
- タスクのSSOTは `knowledge/tasks/` 配下のMarkdown（frontmatter付き）

## 使い方（例）
- `knowledge/tasks/completed/` で一定期間レビューした後、必要に応じて `archive/` へ退避する（完了タスクの“保管庫”）
- 完了ではないが、方針変更・凍結・停止などで「いまは追わない」タスクも `archive/` に退避してよい
- 将来参照したくなったら `archive/` から検索・参照できる

## 推奨メタデータ（任意）
保管理由が必要なら frontmatter に以下を追加する：

```yaml
archived: true
archived_date: 2026-01-04
archived_reason: "優先度変更/凍結/方針変更 など"
```



