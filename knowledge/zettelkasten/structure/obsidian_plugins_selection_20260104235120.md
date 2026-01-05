---
id: 20260104235120
title: Obsidianプラグイン選定（GTD + Zettelkasten + マルチエージェント連携）
type: permanent
tags:
  - obsidian
  - plugin
  - gtd
  - zettelkasten
  - workflow
created_by: takeikumi
created: 2026-01-04
updated: 2026-01-04
---

# Obsidianプラグイン選定（GTD + Zettelkasten + マルチエージェント連携）

## 目的

このVault（GTD + Zettelkasten + マルチエージェント連携）において、どのプラグインを導入するかを検討し、導入方針を決める。

## 前提（現状）

- ノートはYAML frontmatterを活用している
- グラフビューはフィルターで対象を絞って使う
- GTDは `knowledge/tasks/` 配下をSSOTにする方針

## 候補プラグイン（まず検討）

### 1) Dataview（最有力）

- 目的：frontmatterや場所（path）に基づいてノート/タスクを一覧化（＝マスターノート）
- 想定用途：
  - `knowledge/tasks/active/` のタスク一覧
  - `waiting` や `someday` の一覧
  - `references/` を除外した“知識ネットワーク”の可視化補助

### 2) Tasks

- 目的：チェックボックス型タスクの強化（期限、繰り返し等）
- 想定用途：
  - 繰り返しタスク（週次レビューなど）
  - 期限の通知/検索

### 3) Templater

- 目的：テンプレートの自動化（作成日時・ID・author等の自動挿入）
- 想定用途：
  - Zettelkastenの新規ノート生成を高速化
  - GTDタスク雛形の統一

### 4) Obsidian Git

- 目的：自動コミット/プッシュで履歴管理を楽にする
- 想定用途：
  - 日次の更新を勝手に履歴化
  - チーム共有（やるなら）

### 5) Calendar（任意）

- 目的：日次ノート運用が必要なら便利

### 6) QuickAdd（任意）

- 目的：ホットキーで “inboxに追加” を徹底しやすい

## 選定基準

- 学習コストが低い
- SSOT（`knowledge/tasks/`）を崩さない
- 自動化が「やりすぎ」にならない（最初は手動→慣れたら自動化）
- 将来、マルチエージェントやスクリプト連携に繋げやすい

## 決めたいこと（未決）

- [ ] 最小構成は何にする？（例：Dataviewのみ）
- [ ] 繰り返しタスクはTasksでやる？それともカレンダー運用？
- [ ] Templaterはいつ導入する？（最初から/後から）
- [ ] Gitプラグインで自動コミットするか（手動運用か）

## Tips（導入・運用のコツ）

### Templaterは「まず最小」で入れる

- **最初に自動化するのはこれだけ**：`created / updated / author`
- **やりすぎ注意**：ID生成やファイル移動まで全部自動化すると、運用が重くなりやすい

### テンプレは「ノート種別ごと」に分ける

- `inbox`（アイデアメモ）
- `tasks`（GTDタスク）
- `zettelkasten/permanent`（恒久ノート）
- `zettelkasten/references`（文献ノート）
- `zettelkasten/structure`（構造ノート）

### メタデータの名前を揃える（あとで一覧化が楽）

- 製作者：`author`（ノート） / `created_by`（文献ノート）
- 日付：`created`, `updated`
- 種別：`type`

### Dataviewと相性が良い書き方

- **pathで分類**（フォルダ運用）を基本にする
- 追加で `type/status/priority` を使うと、マスターノートが作りやすい



