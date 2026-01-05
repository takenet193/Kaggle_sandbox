"""
タスクをMarkdown（Obsidian形式）からJSONに変換するスクリプト

Zettelkasten + GTD形式のタスクをマルチエージェントシステムが
読み取れるJSON形式に変換します。
"""

import json
import re
from pathlib import Path
from datetime import date, datetime, time
from typing import Any, Dict, Iterable, List, Optional, Tuple
import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]

# Human-facing folder status -> AI-facing JSON status vocabulary
STATUS_DIR_TO_JSON_STATUS: Dict[str, str] = {
    "active": "in_progress",
    "waiting": "waiting",
    "someday": "someday",
    "completed": "completed",
}

STATUS_SORT_ORDER: Dict[str, int] = {
    "in_progress": 0,
    "waiting": 1,
    "someday": 2,
    "completed": 3,
}

PRIORITY_RANK: Dict[str, int] = {
    "critical": 0,
    "high": 1,
    "medium": 2,
    "low": 3,
}


def _normalize_list(value: Any) -> List[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def _to_iso_date(value: Any) -> Optional[str]:
    """
    due_date / completed_date などが date/datetime/str で来てもISO文字列に揃える。
    - date -> YYYY-MM-DD
    - datetime -> YYYY-MM-DDTHH:MM:SS
    - str -> そのまま（ISOっぽい前提）
    """
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.replace(microsecond=0).isoformat()
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, str):
        return value.strip() or None
    return str(value)


def _to_datetime(value: Any, fallback: datetime) -> datetime:
    if value is None:
        return fallback
    if isinstance(value, datetime):
        return value
    if isinstance(value, date):
        return datetime.combine(value, time.min)
    if isinstance(value, str):
        try:
            # datetime.fromisoformat can parse YYYY-MM-DD and YYYY-MM-DDTHH:MM:SS
            parsed = datetime.fromisoformat(value)
            if isinstance(parsed, datetime):
                return parsed
        except ValueError:
            return fallback
    return fallback


def parse_task_markdown(file_path: Path, json_status: str) -> Dict[str, Any]:
    """
    Markdownファイルからタスク情報を抽出
    
    Args:
        file_path: タスクのMarkdownファイルパス
        json_status: AI向けJSONのstatus（pending|in_progress|waiting|someday|completed）
        
    Returns:
        タスク情報の辞書
    """
    metadata, content = _load_markdown_with_frontmatter(file_path)
    
    # タスクIDを生成（ファイル名から、またはメタデータから）
    task_id = metadata.get('id', file_path.stem)
    
    # タイトルを抽出（メタデータまたは最初の見出しから）
    title = metadata.get('title', '')
    if not title:
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if title_match:
            title = title_match.group(1)
    if not title:
        title = task_id
    
    # メタデータから情報を取得
    task_type = metadata.get("type", "task")
    priority = metadata.get('priority', 'medium')
    project = metadata.get('project', None)
    mode = metadata.get('mode', None)
    context_notes = _normalize_list(metadata.get('context', []))
    due_date = _to_iso_date(metadata.get('due_date', None))
    tags = _normalize_list(metadata.get('tags', []))
    related_notes = _normalize_list(metadata.get('related_notes', []))
    dependencies = _normalize_list(metadata.get('dependencies', []))
    assignee = metadata.get('assignee', None)
    assigned_agent = metadata.get('assigned_agent', None)

    # updated_at: frontmatter優先。無ければmtime。
    mtime_dt = datetime.fromtimestamp(file_path.stat().st_mtime)
    updated_raw = metadata.get('updated', None)
    updated_dt = _to_datetime(updated_raw, fallback=mtime_dt)
    updated_at = updated_dt.replace(microsecond=0).isoformat()

    task_json: Dict[str, Any] = {
        "type": task_type,
        "id": task_id,
        "title": title,
        "status": json_status,
        "priority": priority,
        "project": project,
        "mode": mode,
        "context": [c for c in context_notes if c],
        "due_date": due_date,
        "tags": [t for t in tags if t],
        "related_notes": [n for n in related_notes if n],
        "dependencies": [d for d in dependencies if d],
        "assignee": assignee,
        "assigned_agent": assigned_agent,
        "source_file": str(file_path.relative_to(REPO_ROOT)),
        "updated_at": updated_at,
    }
    
    return task_json


def _load_markdown_with_frontmatter(file_path: Path) -> Tuple[Dict[str, Any], str]:
    """
    Obsidian互換のYAML frontmatter（--- ... ---）を最低限パースする。
    依存を減らすため `python-frontmatter` は使わない。
    """
    text = file_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, text

    # Find the second '---' delimiter
    lines = text.splitlines(True)  # keepends
    if not lines or not lines[0].strip() == "---":
        return {}, text

    yaml_lines: List[str] = []
    i = 1
    while i < len(lines):
        if lines[i].strip() == "---":
            # content starts after this line
            content = "".join(lines[i + 1 :])
            raw_yaml = "".join(yaml_lines)
            try:
                meta = yaml.safe_load(raw_yaml) or {}
                if not isinstance(meta, dict):
                    meta = {}
            except Exception:
                meta = {}
            return meta, content
        yaml_lines.append(lines[i])
        i += 1

    # No closing delimiter -> treat as normal markdown
    return {}, text


def _iter_task_files(status_dir: Path) -> Iterable[Path]:
    for md_file in status_dir.glob("**/*.md"):
        if md_file.name.startswith("_"):
            continue
        yield md_file


def _task_sort_key(task: Dict[str, Any]) -> Tuple:
    status = task.get("status") or "someday"
    status_order = STATUS_SORT_ORDER.get(status, 99)

    deps = task.get("dependencies") or []
    blocked_rank = 0 if (status != "completed" and len(deps) > 0) else 1

    priority = (task.get("priority") or "medium").lower()
    pr_rank = PRIORITY_RANK.get(priority, 9)

    due_date = task.get("due_date")
    due_missing = 1 if not due_date else 0
    due_value = due_date or "9999-12-31"

    updated_at = task.get("updated_at")
    updated_dt = _to_datetime(updated_at, fallback=datetime(1970, 1, 1))
    updated_ts = updated_dt.timestamp()

    task_id = task.get("id") or ""

    # blocked first -> priority -> due_date asc (missing last) -> updated desc -> id
    return (status_order, blocked_rank, pr_rank, due_missing, due_value, -updated_ts, task_id)


def convert_tasks_to_current_sprint_json(
    knowledge_tasks_dir: Path = REPO_ROOT / "knowledge" / "tasks",
    output_file: Path = REPO_ROOT / "tasks" / "current_sprint.json",
) -> List[Dict[str, Any]]:
    """
    `knowledge/tasks/{active,waiting,someday,completed}/` を走査して `tasks/current_sprint.json` を生成する
    
    Args:
        knowledge_tasks_dir: タスクのMarkdownファイルがあるディレクトリ
        output_file: 生成するJSONファイルパス
        
    Returns:
        変換されたタスクのリスト
    """
    tasks: List[Dict[str, Any]] = []

    for status_dir_name, json_status in STATUS_DIR_TO_JSON_STATUS.items():
        status_dir = knowledge_tasks_dir / status_dir_name
        if not status_dir.exists():
            continue

        for md_file in _iter_task_files(status_dir):
            try:
                task_json = parse_task_markdown(md_file, json_status=json_status)
                tasks.append(task_json)
            except Exception as e:
                print(f"Error processing {md_file}: {e}")

    tasks.sort(key=_task_sort_key)

    output_file.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now().replace(microsecond=0).isoformat(),
        "total_tasks": len(tasks),
        "tasks": tasks,
    }
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")

    return tasks


if __name__ == "__main__":
    tasks = convert_tasks_to_current_sprint_json()
    print(f"Generated tasks/current_sprint.json with {len(tasks)} tasks")

