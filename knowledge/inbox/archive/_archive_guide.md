---
created: 2025-12-27
type: guide
---

# Inbox Archive

inboxで処理済み・保留にしたメモを保存する場所です。

## 使い方

- zettelkastenに移す程ではないが、捨てたくないメモ
- 一時的に保留にしたアイデア
- 参考として残しておきたい情報

## 整理のタイミング

inboxのレビュー時に：
1. zettelkastenに移動 → 知識として残す
2. tasksに移動 → タスクにする（**tasks側へコピーして、元inboxはarchiveへ**）
3. **archiveに移動** → 保留・参考用
4. 削除 → 不要なもの

## タスク確定時のログの残し方（推奨）

タスク候補メモを `knowledge/tasks/` に昇格させた場合、`archive/` 側に最低限の“追跡情報”を残すと後で便利：

```yaml
promoted_to: task-YYYYMMDDHHMMSS
```

または Obsidianリンクで：

- `promoted_to: [[task-YYYYMMDDHHMMSS|確定タスク]]`



