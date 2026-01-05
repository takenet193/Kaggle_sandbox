"""
Project <-> Task link synchronizer (Obsidian / Markdown).

Goal:
- Ensure every task note links to its project hub note.
- Ensure every project hub note lists links to all tasks in that project.

No Obsidian plugins required. This script edits Markdown files in-place.

Conventions:
- Task notes live under: knowledge/tasks/{active,waiting,someday,completed,archive}/
- Project hub notes live under: knowledge/tasks/projects/project_<project>.md
- A task belongs to a project via frontmatter: project: <project>

Markers:
- Project hub notes get an auto-generated section between:
    <!-- AUTO:tasks:start --> and <!-- AUTO:tasks:end -->
- Task notes get an auto-generated section between:
    <!-- AUTO:project:start --> and <!-- AUTO:project:end -->
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
TASKS_ROOT = REPO_ROOT / "knowledge" / "tasks"
PROJECTS_DIR = TASKS_ROOT / "projects"

TASK_STATUS_DIRS = ["active", "waiting", "someday", "completed", "archive"]

AUTO_TASKS_START = "<!-- AUTO:tasks:start -->"
AUTO_TASKS_END = "<!-- AUTO:tasks:end -->"
AUTO_PROJECT_START = "<!-- AUTO:project:start -->"
AUTO_PROJECT_END = "<!-- AUTO:project:end -->"


@dataclass(frozen=True)
class TaskNote:
    path: Path
    stem: str
    meta: Dict[str, Any]
    project: str
    title: str
    task_id: str
    status_dir: str


def _load_markdown_with_frontmatter(file_path: Path) -> Tuple[Dict[str, Any], str]:
    text = file_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, text

    lines = text.splitlines(True)  # keepends
    if not lines or lines[0].strip() != "---":
        return {}, text

    yaml_lines: List[str] = []
    i = 1
    while i < len(lines):
        if lines[i].strip() == "---":
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

    return {}, text


def _dump_frontmatter(meta: Dict[str, Any]) -> str:
    # Keep it readable and stable
    return "---\n" + yaml.safe_dump(meta, sort_keys=False, allow_unicode=True) + "---\n\n"


def _iter_task_files() -> Iterable[Tuple[str, Path]]:
    for status_dir in TASK_STATUS_DIRS:
        dir_path = TASKS_ROOT / status_dir
        if not dir_path.exists():
            continue
        for md_file in dir_path.glob("**/*.md"):
            if md_file.name.startswith("_"):
                continue
            yield status_dir, md_file


def _extract_task(status_dir: str, md_path: Path) -> Optional[TaskNote]:
    meta, body = _load_markdown_with_frontmatter(md_path)
    # Ignore non-task notes by convention
    note_type = (meta.get("type") or "task").strip() if isinstance(meta.get("type"), str) else meta.get("type")
    if note_type not in (None, "", "task"):
        return None

    project = meta.get("project")
    if not isinstance(project, str) or not project.strip():
        return None

    title = meta.get("title")
    if not isinstance(title, str) or not title.strip():
        # fallback to first heading if present
        title = md_path.stem

    task_id = meta.get("id")
    if not isinstance(task_id, str) or not task_id.strip():
        task_id = md_path.stem

    return TaskNote(
        path=md_path,
        stem=md_path.stem,
        meta=meta,
        project=project.strip(),
        title=title.strip(),
        task_id=task_id.strip(),
        status_dir=status_dir,
    )


def _replace_or_append_block(text: str, start_marker: str, end_marker: str, new_block: str) -> Tuple[str, bool]:
    """
    Replace the first occurrence of a marked block, or append it at the end.
    Returns (new_text, changed)
    """
    if start_marker in text and end_marker in text:
        before, rest = text.split(start_marker, 1)
        _, after = rest.split(end_marker, 1)
        replaced = before + start_marker + "\n" + new_block.rstrip() + "\n" + end_marker + after
        return replaced, replaced != text

    appended = text.rstrip() + "\n\n" + start_marker + "\n" + new_block.rstrip() + "\n" + end_marker + "\n"
    return appended, True


def _ensure_task_links_to_project(task: TaskNote, dry_run: bool) -> bool:
    """
    Ensures a task note contains an auto block linking to its project hub note.
    Returns whether the file would be changed / was changed.
    """
    project_note_stem = f"project_{task.project}"
    project_link = f"[[{project_note_stem}|project: {task.project}]]"
    block = f"- {project_link}\n"

    meta, body = _load_markdown_with_frontmatter(task.path)
    new_body, changed = _replace_or_append_block(body, AUTO_PROJECT_START, AUTO_PROJECT_END, block)
    if not changed:
        return False

    new_text = _dump_frontmatter(meta) + new_body.lstrip("\n")
    if dry_run:
        return True
    task.path.write_text(new_text, encoding="utf-8")
    return True


def _ensure_project_hub(project: str, tasks: List[TaskNote], dry_run: bool) -> bool:
    """
    Ensures the project hub exists and contains an auto-generated tasks list.
    Returns whether the file would be changed / was changed.
    """
    project_note = PROJECTS_DIR / f"project_{project}.md"
    project_note_stem = project_note.stem

    # Build tasks list grouped by status folder
    groups: Dict[str, List[TaskNote]] = {k: [] for k in TASK_STATUS_DIRS}
    for t in tasks:
        groups.get(t.status_dir, groups["someday"]).append(t)

    def fmt_task(t: TaskNote) -> str:
        # Use stem-only link for robustness (file names include unique ids)
        return f"- [[{t.stem}|{t.task_id}: {t.title}]]"

    lines: List[str] = []
    lines.append(f"## タスク一覧（AUTO）")
    lines.append("")
    for status_dir in TASK_STATUS_DIRS:
        bucket = groups.get(status_dir, [])
        if not bucket:
            continue
        lines.append(f"### {status_dir}")
        for t in sorted(bucket, key=lambda x: (x.task_id, x.title)):
            lines.append(fmt_task(t))
        lines.append("")
    block = "\n".join(lines).rstrip() + "\n"

    if not project_note.exists():
        meta = {
            "type": "project",
            "id": f"project-{project}",
            "title": project,
            "project": project,
            "created": None,
            "updated": None,
            "tags": ["project", project],
        }
        # leave timestamps empty intentionally; user can fill or templater can later.
        body = f"# {project}\n\n{AUTO_TASKS_START}\n{block}{AUTO_TASKS_END}\n"
        new_text = _dump_frontmatter(meta) + body
        if dry_run:
            return True
        project_note.parent.mkdir(parents=True, exist_ok=True)
        project_note.write_text(new_text, encoding="utf-8")
        return True

    meta, body = _load_markdown_with_frontmatter(project_note)
    new_body, changed = _replace_or_append_block(body, AUTO_TASKS_START, AUTO_TASKS_END, block)
    if not changed:
        return False

    # Keep meta as-is, but ensure it has project field for sanity
    if isinstance(meta, dict) and meta.get("project") != project:
        meta["project"] = project
    new_text = _dump_frontmatter(meta) + new_body.lstrip("\n")
    if dry_run:
        return True
    project_note.write_text(new_text, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Do not write files; just report what would change.")
    args = parser.parse_args()

    # Collect tasks grouped by project
    by_project: Dict[str, List[TaskNote]] = {}
    all_tasks: List[TaskNote] = []
    for status_dir, md_path in _iter_task_files():
        t = _extract_task(status_dir, md_path)
        if t is None:
            continue
        all_tasks.append(t)
        by_project.setdefault(t.project, []).append(t)

    changed_files: List[str] = []

    # Ensure task -> project link
    for t in all_tasks:
        if _ensure_task_links_to_project(t, dry_run=args.dry_run):
            changed_files.append(str(t.path.relative_to(REPO_ROOT)))

    # Ensure project hub -> tasks list
    for project, tasks in sorted(by_project.items(), key=lambda x: x[0]):
        if _ensure_project_hub(project, tasks, dry_run=args.dry_run):
            changed_files.append(str((PROJECTS_DIR / f"project_{project}.md").relative_to(REPO_ROOT)))

    if args.dry_run:
        print("[DRY RUN] Would update:")
    else:
        print("Updated:")
    for p in sorted(set(changed_files)):
        print(f"- {p}")
    print(f"Projects: {len(by_project)} / Tasks: {len(all_tasks)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


