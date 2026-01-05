---
id: 20251228140000
title: 本プロジェクトの設計思想 - 情報の内的経済圏
author: takeikumi
type: structure
tags:
  - structure
  - zettelkasten
  - design
  - context-engineering
links:
  - lichtenberg_notebooks_20251228
  - krajewski_portrait_20251228
  - obsidian_dataview_cursor_dynamic_context_20260102
created: 2025-12-28
updated: 2025-12-28
---

# 本プロジェクトの設計思想

## 情報の内的経済圏

リヒテンベルクが手本にしていたのは、商人がビジネスという不確実性に満ちた環境の中で、自分の取引を記録したり、コントロールしたりするやり方だった。

私たちのプロジェクトにあっても重要なのは、このような**情報の内的な経済圏**（"paper slip economy" - Krajewski）を確立することであり、それによって私たちが環境がもたらす偶然的な入力に適切に反応できるようにすることなのだ。

---

## AIと知識管理の連続性

リヒテンベルクは計り知れない人物で、この計画のもとなる原理を多分知っていたように思える。まだ当時はAIもコンピュータもカードボックスもなかったのだが、彼は推論や発見のプロセスの中で、そうした手段がいかに機能すべきかを知っていたように見える。

AIとこうした最古の知識マネジメントを、Krajewskiのようにある種の連続性の下で見ることは正しい。

```
リヒテンベルク → カードボックス → コンピュータ → AI
        ↓              ↓              ↓           ↓
     雑記帳      Zettelkasten    データベース   LLM
```

技術は変わっても、本質は同じ：
- 知識を外部化する
- 構造化する
- 検索可能にする
- 新しい発見を促す

---

## 本プロジェクトへの適用

### コンテキストエンジニアリングとしての再定義

このシステムは、人間にとってわかりやすい知識管理であるだけでなく、**AIに与える「動的コンテクスト」を生成する源泉**としても捉え直す必要がある。

しかし、その具体的な実施方法（どの情報を、どの粒度で、どの規則で抽出・圧縮してAIに渡すか）は自明ではない。  
したがって本プロジェクトは、知識管理・タスク管理の設計に加えて、**コンテキストエンジニアリング（Context Engineering）の設計問題**として扱うのが妥当である。

### Inboxの役割
環境からの「偶然的な入力」を受け止める：
- Kaggleディスカッション
- 論文・記事
- 思いつき
- 実験結果

### Zettelkastenの役割
入力を「然るべきコンテクスト」に置き直す：
- 永続的な知識として構造化
- 相互リンクによるネットワーク形成
- 新しい発見・洞察の創発

### マルチエージェントシステムの役割
知識を「行動」に変換する：
- タスクの自動実行
- 実験の遂行
- 結果のフィードバック

---

## 関連ノート

- [[lichtenberg_notebooks_20251228|リヒテンベルクの雑記帳]]
- [[krajewski_portrait_20251228|Markus Krajewski]]
- [[ruminant_machines_20251228|Ruminant Machines]]
- [[obsidian_dataview_cursor_dynamic_context_20260102|Dataview×Cursorの動的コンテクスト（文献）]]

### 実装・運用に直結する関連

- [[obsidian_gtd_dataview_20251228|GTD with Obsidian（DataviewベースのGTDシステム紹介）]]
- [[luhmann_communicating_with_slip_boxes_20260104|Communicating with Slip Boxes（ルーマン：スリップボックスとのコミュニケーション）]]
- [[dla_marbach_zettelkasten_maschinen_der_phantasie_20260104|Zettelkästen. Maschinen der Phantasie（DLA Marbach 展示案内 2013）]]
- [[context_engineering_human_role_ssot_20260104183000|コンテクストエンジニアリングにおける「人間の役割＝SSOT整備」という再定義]]

### 運用アイデア（要改訂メモあり）

- [[idea_docs_manager_review_mode_20260102|Docs Manager 機能案：レビュー・モード + Inbox運用指示]]
  - 注: 共通Inbox（`knowledge/inbox/`）＋「確定タスクは `knowledge/tasks/` にコピーしてSSOT化、元はarchiveへ」の方針に合わせて運用を整える
- [[idea_obsidian_plugins_selection_20260102|Obsidianプラグイン導入検討ノート]]

