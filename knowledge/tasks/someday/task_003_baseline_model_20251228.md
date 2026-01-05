---
type: task
id: task-003
title: ベースラインモデルの構築
author: takeikumi
status: someday
priority: medium
project: kaggle
mode: experiment
context:
- kaggle_basics_20240101
- model_selection_20240103
due_date: null
tags:
- kaggle
- model
- baseline
- xgboost
related_notes: []
assignee: null
assigned_agent: planner
dependencies:
- task-001
- task-002
created: 2025-12-28
updated: 2025-12-28
expected_outcome:
  type: experiment
  metrics:
  - RMSE
  target: <0.15
---

# ベースラインモデルの構築

## 目的

シンプルなXGBoostベースラインを構築し、今後の実験の基準を作る。

## 手順

1. [ ] データ読み込みとEDA
2. [ ] 基本的な前処理
3. [ ] XGBoostモデル訓練
4. [ ] 5-fold CVで評価
5. [ ] 結果を記録

## 期待される成果

- RMSE < 0.15
- CV Score の標準偏差 < 0.01

## 結果

（完了後に記入）

## 学び

（完了後に記入）

<!-- AUTO:project:start -->
- [[project_kaggle|project: kaggle]]
<!-- AUTO:project:end -->
