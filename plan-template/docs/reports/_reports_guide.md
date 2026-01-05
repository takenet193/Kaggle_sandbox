# タスクレポート

このディレクトリには、完了したタスクのレポートを記述したMarkdownファイルを配置します。

## ファイル命名規則

- ファイル名は `plan.json` の `id` フィールドと一致させることを推奨します
- 例: `plan.json` の `id` が `"io-safety"` の場合 → `io-safety.md`

## ファイル構造の例

```markdown
# タスク名 - レポート

## 完了日
YYYY-MM-DD

## 実装内容
実装した内容を記述します。

## 成果物
- 成果物1
- 成果物2

## 課題・改善点
今後の改善点などを記述します。
```

## 使用方法

1. タスク完了時に `plan.json` の該当タスク項目に `report_markdown` フィールドを追加
2. このディレクトリに該当するMarkdownファイルを作成
3. 例: `"report_markdown": "docs/reports/io-safety.md"`

## 注意

- レポートはタスクが完了（`status: "completed"`）した際に作成します
- `generate_roadmap.py` を実行すると、完了したタスクのレポートへのリンクが `ROADMAP.md` に自動的に追加されます




