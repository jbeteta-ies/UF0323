"""Git-backed Markdown discovery shared by the documentation validators."""

from __future__ import annotations

from pathlib import Path
import subprocess


READ_SCOPE = "docs"


def git_candidates(repo_root: Path) -> list[Path]:
    """Return Git candidates, including tracked files regardless of ignore rules."""
    try:
        result = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
            cwd=repo_root,
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError as exc:
        raise RuntimeError(f"git ls-files failed: {exc}") from exc
    if result.returncode != 0:
        detail = result.stderr.strip() or f"exit status {result.returncode}"
        raise RuntimeError(f"git ls-files failed: {detail}")

    return [repo_root / Path(name) for name in result.stdout.splitlines() if name]


def read_scope_candidates(repo_root: Path) -> list[Path]:
    """Apply the explicit student-document READ_SCOPE before file filters."""
    scope = repo_root / READ_SCOPE
    candidates: list[Path] = []
    for path in git_candidates(repo_root):
        try:
            path.relative_to(scope)
        except ValueError:
            continue
        candidates.append(path)
    return candidates


def markdown_files(repo_root: Path) -> list[Path]:
    """Return existing Markdown files in the Git-backed READ_SCOPE."""
    return sorted(
        path
        for path in read_scope_candidates(repo_root)
        if path.suffix == ".md" and path.is_file()
    )
