---
created: 2025-12-28
type: guide
---

# References（文献ノート）

読んだ本、論文、記事などの文献ノートを保存する場所です。

## 用途

- 書籍のメモ
- 論文の要約
- Webページ・ブログ記事のメモ
- Kaggle Discussionの要約

## 命名規則

```
著者名_タイトル_YYYYMMDDHHMMSS.md
```

例：`krajewski_paper_machines_20251228143000.md`

## ノート構造

```markdown
---
id: YYYYMMDDHHMMSS
title: 文献タイトル
type: reference
author: 著者名
source: URL or 書籍情報
tags: [reference, topic]
created: YYYY-MM-DD
---

# 文献タイトル

## 概要
（文献の要約）

## 重要なポイント
- ポイント1
- ポイント2

## 引用
> 印象に残った引用

## 自分の考え
（読んで思ったこと）

## 関連ノート
- [[関連するzettelへのリンク]]
```

## グラフビューについて

文献ノートはグラフビューから除外することを推奨：

```
-path:references/
```



