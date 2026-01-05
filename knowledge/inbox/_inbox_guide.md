# Inbox

未整理のアイデアやメモ、タスクを一時的に保存する場所です。

## 使い方
- 思いついたアイデア/メモ/タスク候補をここに新しいファイルとして作成（共通Inbox）
- 定期的にこのフォルダをレビューして「確定」させ、適切な場所へ振り分ける

## 振り分けルール（重要）

### タスクとして確定した場合（コピー→アーカイブ）
- `knowledge/inbox/` のタスク候補メモは、内容が確定したら **`knowledge/tasks/{active|waiting|someday}/` に同内容を“新規作成（コピー）”**する
- コピー先（tasks側）がSSOT（真実の源）になる
- 元のInboxファイルは **`knowledge/inbox/archive/` に移動**して「入力ログ」として残す
  - 推奨: archive側に `promoted_to:`（昇格先タスクのリンク/ID）を残す

### 知識として残す場合
- `knowledge/zettelkasten/`（permanent/references/structure/index）へ移す（必要な形に整形）
- 元のInboxファイルは `archive/` に移動するか削除（運用方針に応じて）

### 不要な場合
- 削除

## 関連

- 運用規約（Docs Manager）: `.cursor/docs_manager_rules.mdc`（レビュー手順のSSOT）




