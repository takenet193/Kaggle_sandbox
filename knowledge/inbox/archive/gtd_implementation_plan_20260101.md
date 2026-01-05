---
id: plan-gtd-impl-20260101
title: GTD実装計画書（Obsidian/Dataview中心） - Kaggle_sandbox
type: plan
status: draft
project: kaggle_sandbox
created: 2026-01-01
updated: 2026-01-04
tags: [gtd, obsidian, dataview, plan, task-management]
---

# GTD実装計画書（Obsidian/Dataview中心） - Kaggle_sandbox

この計画書は、`knowledge/tasks/` を中核に **GTD（Getting Things Done）を運用できる状態**を、このプロジェクトに実装するための設計・手順をまとめたものです。  
**目的**は「日々の見える化（一覧/分類/レビュー）はObsidianで完結し、Pythonは **AI連携用JSON生成に絞る**ことです。

---

## 0. 前提・方針（重要）

### Single Source of Truth
- **タスクの真実の源（SSOT）は Markdown**（`knowledge/tasks/**/*.md`）
- JSONは **派生物**（自動 or 手動で生成してAIに渡す）

参考（整理ノート）:
- [[context_engineering_human_role_ssot_20260104183000|コンテクストエンジニアリングにおける「人間の役割＝SSOT整備」という再定義]]

### 運用の中心
- 日々の「収集・整理・見える化・レビュー」は **Obsidian + Dataview** で行う
- Pythonは **AI向け出力（例: `tasks/current_sprint.json`）** の生成のみ

### “やらないこと”（非目的）
- 監視スクリプト（watcher）による自動同期（後回し/任意）
- タスクの作成/移動をCLIで必須化（Obsidian編集を阻害しない）
- 過度なスキーマ厳格化（まず運用が回ることを優先）

### DataviewJS（tasks.js）方式の位置付け（参考メモの組み込み）
本計画の「基本形」は **タスクを `knowledge/tasks/` 配下の“タスクノート（frontmatter付き）”として管理**し、Dataview（クエリ or DataviewJS）で一覧化する。

- **採用する部分（推奨）**
  - 「マスターノート1枚でGTDビューを出す」発想（Next/Waiting/Someday/Overdue）
  - 「次のアクションが無いプロジェクトの検出」などの健全性チェック（必要になったらDataviewJSで実装）
- **今すぐ全面採用しない部分（理由）**
  - tasks.js型（Vault内の“どこに書いたタスクでも”集約し、タグ/記法で分類・順序付けまで行う）は強力だが、
    本計画はすでに `status` 等の **frontmatter基盤**と **フォルダ運用**で要件を満たせるため、初期は複雑化を避ける
- **将来の拡張（必要なら採用）**
  - 収集時に会議メモ等へ書いた `- [ ]` タスクも拾いたい場合は、
    追加ルール（例：`#gtd` タグ、または `type: task` を含むページのみ）を決めて DataviewJS 集約に拡張する

---

## 1. 完成形（ユーザー体験）

### 日々（キャプチャ & 実行）
- 思いついた情報（タスク/アイデア/メモ）は **`knowledge/inbox/`** に放り込む（知識とタスクの共通キャプチャ箱）
- Obsidianの **マスターノート**（Markdownノート。例：`knowledge/tasks/_MASTER_TASKS.md`）を見ると、以下が自動で一覧化される
  - **Next Actions（次にやる）**: `status: active`
  - **Waiting（待ち）**: `status: waiting`
  - **Someday/Maybe（いつか）**: `status: someday`
  - **期限切れ（Overdue）**: `due_date < today` かつ未完了

表示方針:
- まずは **Dataview（通常クエリ）**で一覧を出す（シンプルで保守しやすい）
- 集計/検出などが必要になったタイミングで **DataviewJS** を追加する

### 週次レビュー
- 週1でマスターノートを見て
  - inboxの空にする（振り分け）
  - waitingのフォロー
  - somedayの見直し
  - activeの優先順位調整
  - 「次のアクションが無いプロジェクト」を発見して補う（任意）

### AI連携
- `python src/task_converter.py` 等のコマンドで **`tasks/current_sprint.json`** を更新し、AIに渡す

---

## 2. ディレクトリとステータス（確定案）

### 収集（Inbox）
`knowledge/inbox/` を **知識（アイデア/メモ）とタスク**の共通Inboxとして採用する：

- `knowledge/inbox/`：未整理の情報（タスク/アイデア/メモ）
  - 後で `knowledge/tasks/*`（タスク）や `knowledge/zettelkasten/*`（知識）に振り分ける

### タスク保管場所（人間向け / 整理後）
整理後のタスクは `knowledge/tasks/` 配下で運用する：

- `knowledge/tasks/active/`：次にやる（Next Actions）
- `knowledge/tasks/waiting/`：待ち
- `knowledge/tasks/someday/`：いつかやる
- `knowledge/tasks/completed/`：完了
- `knowledge/tasks/archive/`：アーカイブ（意識に入れる必要がなくなったタスクの保管。ステータスではない）

### ステータス語彙（frontmatter）
（運用上の統一語彙）
- `status: active | waiting | someday | completed`

※ **inboxは“ステータス”ではなく“置き場所”**として扱う（`knowledge/inbox/` にあるものが未整理）。
※ 既存タスクに `status: active/someday` 等があり、フォルダとも一致するため採用。

### 既存スクリプト（Python）との整合（重要）
現状の `src/task_converter.py` / `src/task_loader.py` は、ステータスや出力ディレクトリの扱いに揺れがあるため、**実装時にここを統一する**。

- **正（人間向け/SSOT）**: `knowledge/tasks/{active,waiting,someday,completed}`（frontmatterの `status` も同語彙）
- **AI向けJSON（変換ルール案）**:
  - `active` → `in_progress`（AIの「今やる」に相当させる）
  - `waiting` → `waiting`
  - `someday` → `someday`
  - `completed` → `completed`
  - `pending` は `knowledge/inbox/` の **未確定タスク候補**（`type: task`）をJSONに含めたい場合にのみ使用する（任意）

※ ここは「どのJSONをAIに渡すか」（activeのみ/全部）にも依存するので、実装フェーズで確定する。

### アーカイブ（archive）の位置付け（重要）
本計画での `archive` は **タスクのステータスではなく「入力ログの保管」**である。

- `knowledge/inbox/archive/` は、inboxで処理済みになった元メモを保存する（確定タスクの“元”もここに残す）
- `archive` の内容は **AI向けJSONには含めない**（タスクSSOTは `knowledge/tasks/` にあるため）
- 追跡したい場合は、archive側のfrontmatterに `promoted_to:` を残し、確定タスクへ辿れるようにする

補足（tasks側のアーカイブ）:
- `knowledge/tasks/archive/` は、完了後しばらく経って「もう意識に入れる必要がない」タスク等を退避する場所
- ここも **ステータスではなく保管場所**（必要なら後から参照できる）

### プロジェクト（project）とステータス（status）の関係（用語定義）
- **project**: タスクが属する「まとまり」（= 何のためのタスクか / どの成果に向かうか）
  - 例: `infrastructure`, `kaggle`, `house-prices`
- **status**: そのタスクの「状態」（= いま何が起きているか）
  - `active`: 今やれる「次のアクション」
  - `waiting`: 外部要因/依存待ちで止まっている
  - `someday`: いつかやる（今はやらない）
  - `completed`: 完了

重要:
- **同じprojectの中に、複数statusのタスクが同時に存在してよい**（むしろ普通）
- `knowledge/inbox/`（未整理）では、project/statusは**後で決める前提**（決めたら `knowledge/tasks/*` に移動）

推奨ルール（GTD的）:
- 各projectには、原則 **少なくとも1つの `active`（次のアクション）** があるのが理想
  - `waiting` しか無いprojectは、フォローの `active` を追加するか、待ちを明確化する

---

## 3. タスクMarkdown（frontmatter最小仕様）

Dataviewで拾いやすく、かつ既存ファイルとの整合を保つ最小セット。

### 必須（MUST）
- `id`: 例 `task-20260104123045`（推奨：`task-YYYYMMDDHHMMSS`）
- `title`
- `status`: `active|waiting|someday|completed`
- `priority`: `critical|high|medium|low`
- `project`
- `created`
- `updated`

#### id生成規則（提案：プロジェクト全体で統一）
- Zettelkasten側の「固定番地（不変）」思想に合わせ、タスクも **タイムスタンプID**を採用する
- 形式: `task-YYYYMMDDHHMMSS`
- 衝突回避: 同一秒で作成が重なった場合は `task-YYYYMMDDHHMMSS-a` のようにサフィックスを付ける（通常は不要）

※ 既存の `task-001` など連番IDは当面“過去資産”として保持し、新規作成からタイムスタンプ方式に移行する（必要なら後で一括移行）。

### inboxタスクの扱い（重要）
- `knowledge/inbox/` 配下の「タスクとして扱うメモ」は **未整理タスク**として扱う
- inbox内のタスクメモは **`status` を書かない（省略）**（=未整理のまま）とし、タスクとして確定したら `knowledge/tasks/*` 側へ **コピーしてSSOT化**し、元は `knowledge/inbox/archive/` に移動する（詳細は下の「Inboxタスクの確定フロー」参照）

### inbox（共通）で推奨する識別（案）
`knowledge/inbox/` には知識とタスクが混在するため、後段の振り分けを楽にするために最低限の識別を推奨する：

- タスクとして扱う: `type: task`（frontmatter）
- 知識/アイデアとして扱う: `type: idea` or `type: note`（frontmatter）

### Inboxタスクの確定フロー（重要：コピー→アーカイブ）
共通Inbox（`knowledge/inbox/`）は「入力ログ」として残しつつ、タスクのSSOTは `knowledge/tasks/` に置くため、次のフローを採用する：

- 1) `knowledge/inbox/` にタスク候補メモを作成（`type: task` 推奨）
- 2) 内容が「タスクとして確定」したら、**同内容を `knowledge/tasks/{active|waiting|someday}/` に“新規作成（コピー）”**する
  - ここで `status` や `priority` などのタスク用frontmatterを整える
  - タスクIDは原則 `task-YYYYMMDDHHMMSS`（本計画のid規則）
- 3) 元のInboxファイルは **`knowledge/inbox/archive/` に移動**する（= 入力ログとして保持）
  - 推奨: archive側のfrontmatterに `promoted_to:`（昇格先タスクへのリンク/ID）を残す

この方式の狙い:
- `knowledge/tasks/` をSSOTに固定（AI連携やDataview集約が安定）
- `knowledge/inbox/` に「いつ何を思いついたか」の履歴を残せる（後から追跡可能）

※ 既存の `knowledge/inbox/` はガイド/アーカイブがあるため、運用ルールは `knowledge/inbox/_inbox_guide.md` にも反映する。

### 推奨（SHOULD）
- `context`（例: `experiment`, `setup`, `development`）
- `due_date`（ISO日付 or `null`）
- `tags`（配列）
- `related_notes`（配列、ZKノートID等）
- `dependencies`（配列）
- `assignee`（人間の担当者。**任意**：未決定なら省略/空欄）
- `assigned_agent`（AI連携用）

#### 人間担当（assignee）とAI担当（assigned_agent）の違い
- **assignee**: チーム内の「人間の担当者」。基本は未設定でよく、決まっている場合のみ明示する。
- **assigned_agent**: AI実行時に想定する「エージェント役割」（planner/developer/validator/docs_manager 等）。

### Waiting用（待ちの情報）
- `waiting_for`: 何を誰から待っているか（文字列）
- `waiting_since`: 日付

### Completed用
- `completed_date`: 日付

---

## 4. Obsidianマスターノート（Dataviewダッシュボード）

### 追加するファイル（案）
- `knowledge/tasks/_MASTER_TASKS.md`

### マスターノートの見方
- マスターノートは **Obsidian上で開く**（Dataview/DataviewJSが実行され、一覧が表示される）
- Cursorは **編集**には使えるが、Dataview/DataviewJSの実行結果表示はObsidian側で行う

### 「マスターノート」とは何か（定義）
本計画でいうマスターノートは、**`knowledge/tasks/` 配下のタスク状態をまとめて見る“ダッシュボード1枚”**のこと。  
さらに補助として、`knowledge/inbox/` から **`type: task` の未整理タスク候補**も表示し、レビューで確定→コピー→アーカイブに繋げる。

### 目標
- この1枚を見るだけで、GTDの主要ビュー（Next/Waiting/Someday/Overdue）が揃う

### Dataviewで必要なクエリ（要件）
- status別一覧（active/waiting/someday）
- 期限切れ抽出（`due_date` が今日より前、かつ `status != completed`）
- 並び順
  - active: **依存関係（blocked/ready）→ `priority` → `due_date` → `updated`** の順で見たい（詳細は要調整）
    - ルール: `dependencies` に未完了タスク（`status != completed`）が含まれる場合、そのタスクは **blocked（着手不可）**として後回し（または別セクションへ）
    - ready（依存が解消済み）の中で、`critical > high > medium > low` → `due_date` 昇順（未設定は最後）→ `updated` 新しい順
- 表示項目
  - `file.link`, `priority`, `due_date`, `project`, `context`
  - waitingは `waiting_for` も表示

※ 実際のDataviewクエリ文はこの計画書の次版で確定する（まずは要件を固定）。

### Dataviewクエリ vs DataviewJS（tasks.js）的アプローチ
まずは **通常のDataviewクエリ**で要件を満たす（実装が単純・保守が楽）。次が必要になったタイミングで **DataviewJS** に寄せる。

- **Dataview（クエリ）で十分なもの**
  - `knowledge/tasks/` 配下のタスクノートを status/期日/優先度で一覧化
  - overdue抽出、並び替え、表示カラムの調整
- **DataviewJS（tasks.js）的な実装が効くもの**
  - 「プロジェクトごとの“次の1個”」の抽出（sequencing/順序付け）
  - 「Next Actionが無いプロジェクト」の検出
  - 複数フォルダ/複数記法（チェックボックス＋タスクノート）を横断して集約する高度化

---

## 5. AI向けJSON生成（Python側の最小要件）

### 生成物（案）
- `tasks/current_sprint.json`：AIに渡す集約ファイル

### 入力
- `knowledge/tasks/{active,waiting,someday,completed}/**/*.md`
- （任意）`knowledge/inbox/**/*.md` のうち `type: task` のものを `pending` 相当として含める（未確定タスク候補として）

### 出力に含めたいフィールド（案）
- `id`, `title`, `status`, `priority`, `project`, `context`, `due_date`
- `tags`, `related_notes`, `dependencies`, `assignee`, `assigned_agent`
- `source_file`（元mdのパス）
- `updated_at`（生成時刻）

### 変換ルール（案）
- SSOTはMarkdownなので、JSONは常に上書き生成でよい
- `status: active` はAI側の「今スプリント対象」に相当
- **方針（確定）**: active以外（waiting/someday）もJSONに含める（= AIが状況全体を把握できるようにする）
- **方針（確定）**: completedもJSONに含める（= 完了状況も重要なコンテクストとして渡す）

---

## 6. 移行・整備タスク（実装前の準備）

### 6.1 既存タスクの整合
- `knowledge/tasks/someday/task_003_...` が Dataview/変換の両方で扱えること
- `status` とフォルダのズレがあるファイルがあれば修正（例: activeフォルダなのにstatusが違う等）

### 6.2 ガイドの更新
- `knowledge/tasks/_gtd_guide.md` に
  - ステータス語彙
  - inboxの運用（空にする頻度）
  - 週次レビュー手順
  - マスターノートの場所
を追記する

---

## 7. 受け入れ条件（Definition of Done）

- Obsidianで `knowledge/tasks/_MASTER_TASKS.md` を開くと
  - active/waiting/someday/overdue が自動で一覧表示される
- `knowledge/tasks/` に新規タスクを追加しても、一覧に反映される
- Pythonで1コマンド実行し、`tasks/current_sprint.json` が生成/更新できる
- 生成JSONをAIに渡して、最低限「何をすべきか」を理解できる形になっている

---

## 8. 未決事項（一緒に詰める）

- [ ] マスターノートのファイル名/配置（`_MASTER_TASKS.md` で良いか）
- [ ] Dataviewのクエリ詳細（`dv.table`/`dv.list`、並び順、優先度の扱い）
- [x] **タスクのstatus**は「フォルダで判定」運用に固定する（`status: inbox` は使わない） 
- [x] マスターノートに `knowledge/inbox/`（未整理）をどう出すか → `type: task` のみを補助セクションとして表示する
- [x] AI向けJSONに waiting/someday を含める（activeのみにはしない）
- [x] `tasks/` ディレクトリはGit管理する（チーム共有・レビューのため）
- [x] AI向けJSONのステータス語彙は `pending | in_progress | waiting | someday | completed` を採用する

---

## 9. 改訂履歴

- 2026-01-01: 初版（Obsidian/Dataview中心、PythonはJSON生成のみ）
- 2026-01-04: CE観点（SSOT整備/生成と実行の分離）をPermanentノートとして整理し、相互リンクを追加





