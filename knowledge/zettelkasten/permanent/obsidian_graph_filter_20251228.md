---
id: 20251228
title: Obsidianグラフビューのフィルター使い方
author: takeikumi
tags: [obsidian, graph-view, tips]
links: []
created: 2025-12-28
updated: 2025-12-28
---

# Obsidianグラフビューのフィルター使い方

## 📋 コピペ用：おすすめフィルター

```
path:knowledge/ -path:inbox/ -path:archive/ -path:references/ -file:_guide
```

↑ これをグラフビューのFiltersにそのまま貼り付け

---

## フィルターの開き方

1. グラフビューを開く（左サイドバーのグラフアイコン）
2. 左上の設定アイコン ⚙️ をクリック
3. **Filters** セクションにフィルターを入力

---

## 基本記法

| 記法 | 意味 |
|------|------|
| `path:フォルダ/` | そのフォルダのみ表示 |
| `-path:フォルダ/` | そのフォルダを除外 |
| `file:ファイル名` | 特定ファイルのみ表示 |
| `-file:ファイル名` | 特定ファイルを除外 |
| `tag:#タグ名` | 特定タグのみ表示 |
| `-tag:#タグ名` | 特定タグを除外 |

---

## 組み合わせ

### OR（どちらか）
```
tag:#kaggle OR tag:#model
```

### AND（両方）
```
tag:#kaggle tag:#model
```

---

## よく使うフィルター例

### knowledgeからinboxを除外
```
path:knowledge/ -path:inbox/
```

### knowledgeからinboxとarchiveを除外
```
path:knowledge/ -path:inbox/ -path:archive/
```

### zettelkastenだけ表示
```
path:zettelkasten/
```

### ガイドファイルを除外
```
-file:_guide
```

### 特定タグだけ表示
```
tag:#kaggle
```

### 文献ノートフォルダを除外
```
-path:references/
```

### 複合：knowledge内の特定タグ、inboxとガイドを除外
```
path:knowledge/ tag:#kaggle -path:inbox/ -file:_guide
```

---

## 補足

- フィルター設定はグラフビューごとに保存される
- Vault全体ではなく、グラフ表示だけに影響
- ファイル検索やリンクは引き続き機能する



