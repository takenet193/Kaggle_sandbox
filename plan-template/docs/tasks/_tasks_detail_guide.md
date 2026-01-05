# タスク詳細ドキュメント

このディレクトリには、各タスクの詳細仕様を記述したMarkdownファイルを配置します。

## ファイル命名規則

- ファイル名は `plan.json` の `id` フィールドと一致させることを推奨します
- 例: `plan.json` の `id` が `"io-safety"` の場合 → `io-safety.md`

## ファイル構造の例

```markdown
# タスク名

## 概要
タスクの概要を記述します。

## 要件
- 要件1
- 要件2

## 実装方針
実装の方針を記述します。

## 参考資料
関連する資料へのリンクなど。
```

## 使用方法

1. `plan.json` の各タスク項目に `detail_markdown` フィールドを追加
2. このディレクトリに該当するMarkdownファイルを作成
3. 例: `"detail_markdown": "docs/tasks/io-safety.md"`




