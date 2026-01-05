---
type: task
id: task-002
title: task_converter.py の実装
author: takeikumi
status: completed
completed_date: 2026-01-04
priority: high
project: infrastructure
mode: development
context: []
due_date: 2026-01-05
tags:
- python
- automation
- gtd
related_notes: []
assignee: null
assigned_agent: developer
dependencies: []
created: 2025-12-28
updated: 2026-01-04
expected_outcome:
  type: script
  deliverables:
  - src/task_converter.py（動作するスクリプト）
  - tasks/current_sprint.json（出力サンプル）
---

# task_converter.py の実装

## 目的

GTDのMarkdownタスクをJSON形式に変換し、マルチエージェントシステムに引き渡せるようにする。

## 手順

1. [ ] YAMLフロントマター解析機能
2. [ ] タスクの本文解析
3. [ ] JSON形式への変換
4. [ ] current_sprint.json 生成
5. [ ] テスト

## 仕様

### 入力
```
knowledge/tasks/active/*.md
```

### 出力
```json
{
  "version": "1.0",
  "items": [
    {
      "id": "task-001",
      "title": "タスク名",
      "status": "active",
      "priority": "high",
      ...
    }
  ]
}
```

## 結果

（完了後に記入）

## 学び

（完了後に記入）

<!-- AUTO:project:start -->
- [[project_infrastructure|project: infrastructure]]
<!-- AUTO:project:end -->
