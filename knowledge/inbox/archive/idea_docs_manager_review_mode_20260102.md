---
created: 2026-01-02
type: idea
status: archived
author: takeikumi
tags: [multi-agent, docs-manager, gtd, zettelkasten, review]
promoted_to: .cursor/docs_manager_rules.mdc
promoted_at: 2026-01-04
---

# Docs Manager 機能案：レビュー・モード + Inbox運用指示

いつか作るマルチエージェントシステムの中の **Docs Manager** の機能として、次を実装したい。

## 1) GTD / Zettelkasten のレビュー・モード

### 目的

- レビュー作業を「モード」として切り出し、仕分けを迷わず・漏れなく行えるようにする

### レビュー・モードでやること（仕分け）

- **GTD**
  - `knowledge/inbox/` のタスク候補（`type: task`）をレビュー（共通Inbox）
  - タスクとして確定したら `knowledge/tasks/{active|waiting|someday}/` に **コピーしてSSOT化**し、元ファイルは `knowledge/inbox/archive/` に移動
  - メタデータ（priority, deps, related_notes など）を整える

- **Zettelkasten**
  - `knowledge/inbox/` のメモをレビュー
  - `knowledge/zettelkasten/permanent/`（恒久知）へ昇格するか
  - `knowledge/zettelkasten/references/`（文献ノート）として残すか
  - 不要なら削除、保留なら `knowledge/inbox/archive/` に移動
  - 必要なら `structure/`（構造ノート）や `index/` を更新

## 2) Inbox運用をMarkdownで“明示的に指示”しておく

### 指示内容

- **メモはまず `knowledge/inbox/` に作ること**
  - 書きかけでもOK、断片でもOK
  - 後でレビュー・モードで仕分けして、適切な場所へ移動する

- **リンクは相互（双方向）にすること**
  - 昇格・移動・整理の際にリンクを追加した場合、可能な範囲で **相手側ノートにも逆リンク（関連ノート等）を追記**して相互リンクにする
  - 目的：後から辿れる経路を増やし、コンテクスト（関係性）を強化する



