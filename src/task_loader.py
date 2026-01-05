"""
マルチエージェントシステムがタスクJSONを読み取るためのユーティリティ

Plannerエージェントがタスクを読み取り、分解して各エージェントに
割り当てる際に使用します。
"""

import json
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime


def _load_current_sprint(tasks_dir: Path = Path("tasks")) -> Dict:
    sprint_file = tasks_dir / "current_sprint.json"
    if not sprint_file.exists():
        return {"tasks": []}
    with open(sprint_file, "r", encoding="utf-8") as f:
        return json.load(f)


def load_task(task_id: str, tasks_dir: Path = Path("tasks")) -> Optional[Dict]:
    """
    特定のタスクを読み込む
    
    Args:
        task_id: タスクID
        tasks_dir: タスクJSONファイルのディレクトリ
        
    Returns:
        タスク情報の辞書、見つからない場合はNone
    """
    payload = _load_current_sprint(tasks_dir)
    for task in payload.get("tasks", []):
        if task.get("id") == task_id:
            return task
    return None


def load_pending_tasks(tasks_dir: Path = Path("tasks")) -> List[Dict]:
    """
    未処理のタスクをすべて読み込む
    
    Args:
        tasks_dir: タスクJSONファイルのディレクトリ
        
    Returns:
        未処理タスクのリスト
    """
    payload = _load_current_sprint(tasks_dir)
    tasks = [t for t in payload.get("tasks", []) if t.get("status") == "pending"]
    return tasks


def load_active_tasks(tasks_dir: Path = Path("tasks")) -> List[Dict]:
    """
    進行中のタスクをすべて読み込む
    
    Args:
        tasks_dir: タスクJSONファイルのディレクトリ
        
    Returns:
        進行中タスクのリスト
    """
    payload = _load_current_sprint(tasks_dir)
    tasks = [t for t in payload.get("tasks", []) if t.get("status") == "in_progress"]
    return tasks


def load_tasks_by_project(project: str, tasks_dir: Path = Path("tasks")) -> List[Dict]:
    """
    特定のプロジェクトのタスクを読み込む
    
    Args:
        project: プロジェクト名
        tasks_dir: タスクJSONファイルのディレクトリ
        
    Returns:
        プロジェクトのタスクリスト
    """
    payload = _load_current_sprint(tasks_dir)
    return [t for t in payload.get("tasks", []) if t.get("project") == project]


def load_tasks_index(tasks_dir: Path = Path("tasks")) -> Optional[Dict]:
    """
    タスクインデックスファイルを読み込む
    
    Args:
        tasks_dir: タスクJSONファイルのディレクトリ
        
    Returns:
        インデックス情報の辞書
    """
    sprint_file = tasks_dir / "current_sprint.json"
    if not sprint_file.exists():
        return None
    with open(sprint_file, "r", encoding="utf-8") as f:
        return json.load(f)


def format_task_for_planner(task: Dict) -> str:
    """
    タスクをPlannerエージェントが読みやすい形式にフォーマット
    
    Args:
        task: タスク情報の辞書
        
    Returns:
        フォーマットされた文字列
    """
    lines = [
        f"# タスク: {task['title']}",
        f"ID: {task['id']}",
        f"ステータス: {task['status']}",
        f"優先度: {task['priority']}",
        f"プロジェクト: {task['project']}",
        f"モード: {task.get('mode', '')}",
        "",
        f"## 説明",
        task.get('description', '')[:500],
        "",
        f"## 期待される成果",
    ]
    
    if task.get('expected_outcome'):
        outcome = task['expected_outcome']
        if isinstance(outcome, dict):
            lines.append(f"- タイプ: {outcome.get('type', 'N/A')}")
            if 'metrics' in outcome:
                lines.append(f"- 評価指標: {', '.join(outcome['metrics'])}")
            if 'target_improvement' in outcome:
                lines.append(f"- 目標改善: {outcome['target_improvement']}")
        else:
            lines.append(str(outcome))
    
    if task.get('context'):
        lines.extend([
            "",
            "## コンテクスト（参照ノート）",
            ", ".join([str(x) for x in task.get("context", [])]),
        ])

    if task.get('related_notes'):
        lines.extend([
            "",
            f"## 関連ノート",
            ", ".join(task['related_notes'])
        ])
    
    if task.get('dependencies'):
        lines.extend([
            "",
            f"## 依存タスク",
            ", ".join(task['dependencies'])
        ])
    
    return "\n".join(lines)


if __name__ == "__main__":
    # 使用例
    pending_tasks = load_pending_tasks()
    print(f"未処理タスク数: {len(pending_tasks)}")
    
    for task in pending_tasks[:3]:  # 最初の3つを表示
        print("\n" + "="*50)
        print(format_task_for_planner(task))

