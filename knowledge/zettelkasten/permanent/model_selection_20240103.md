---
id: 20240103
title: モデル選択
author: takeikumi
tags: [model, kaggle, xgboost, lightgbm]
links: 
  - kaggle_basics_20240101
  - feature_engineering_20240102
created: 2024-01-03
updated: 2024-01-12
---

# モデル選択

## 内容

Kaggleで使われる主要なモデルとその選択基準。

### Gradient Boosting系（最も人気）
1. **XGBoost**: 安定性が高い、ハイパーパラメータ調整が重要
2. **LightGBM**: 高速、大規模データ向け
3. **CatBoost**: カテゴリカル変数の自動処理

### ニューラルネットワーク
- TabNet: テーブルデータ専用
- Transformer系: 最近のトレンド

### アンサンブル
- スタッキング: 複数モデルの組み合わせ
- ブレンディング: シンプルな加重平均

## 関連ノート
- [[kaggle_basics_20240101|Kaggle基本戦略]]
- [[feature_engineering_20240102|特徴量エンジニアリング]]

## 学び
単一モデルよりも、複数モデルのアンサンブルが安定して高スコアを出せる。



