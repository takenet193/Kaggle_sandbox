---
created: 2026-01-04
type: guide
---

# Projects Archive（プロジェクト・アーカイブ）

`knowledge/tasks/projects/archive/` は、**役目を終えた / 当面追わない projectハブノート**を保管する場所です。

## 位置付け
- `archive` は **ステータスではなく保管場所**
- タスクSSOT（`knowledge/tasks/**/task_*.md`）とは別に、projectハブノート側の整理用

## 使いどころ（例）
- プロジェクトが終了し、今後は参照だけできればよい
- 一時凍結で、日々のレビュー対象から外したい
- project名（slug）を変更して旧ハブを退避したい

## 推奨メタデータ（任意）
必要なら frontmatter に以下を追加：

```yaml
archived: true
archived_date: 2026-01-04
archived_reason: "終了/凍結/名称変更 など"
```



