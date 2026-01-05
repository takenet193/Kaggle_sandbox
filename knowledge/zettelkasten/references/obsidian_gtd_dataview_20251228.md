---
id: 20251228150000
title: GTD with Obsidian（DataviewベースのGTDシステム紹介）
type: reference
source_author: AlanG（Obsidian Forum）
source: https://forum.obsidian.md/t/gtd-with-obsidian-a-ready-to-go-gtd-system-with-task-sequencing-quick-add-template-waiting-on-someday-maybe-and-more/65502
tags: [reference, obsidian, gtd, dataview, task-management]
created_by: takeikumi
created: 2025-12-28
---

# GTD with Obsidian（DataviewベースのGTDシステム紹介）

## 概要

Obsidian上でGTD（Getting Things Done）を実現するための「出来合いの仕組み」を紹介した投稿。
中核はDataviewのスクリプト（`tasks.js`）で、Vault内のタスクを集約・分類し、マスターリストを生成する。

## 主要ポイント（投稿の主張）

- Vault内のどこに書いたタスクでも集約できる
- プロジェクト内タスクの順序付け（Sequencing）を扱える
- Waiting-on / Someday などの分類が可能
- Next Actionがないプロジェクトを見つけられる
- 「プラグインではなくDataviewスクリプト」にする理由：各自のGTD流儀に合わせてカスタムしやすい
- Tasksプラグインとも併用可能

## セットアップ概要

1. デモVaultで動作を確認
2. Dataviewスクリプト（`tasks.js`）をVault内に配置
3. 必要ならTemplater（テンプレ＋ホットキー）でクイック操作を追加

## 自分の考え（適用メモ）

- 本プロジェクトの `knowledge/tasks/`（GTD）と相性が良い
- 「マスタータスクノート（Dataviewで一覧生成）」を1枚作ると運用が楽になる

## 関連ノート

- [[gtd_team_book_20251228|GTDでチームを強化する]]




