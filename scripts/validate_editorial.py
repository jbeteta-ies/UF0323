#!/usr/bin/env python3
"""Validador editorial estructural para contenido Markdown en docs/.

Comprueba de forma automática convenciones del patrón canónico de ejercicios:

- `!!! question "Ejercicio N. ..."`
- solución interna con `??? success "Solución ejercicio N"`
- coherencia de numeración ejercicio/solución
- ausencia de anidaciones extra de admonitions dentro de ejercicio→solución

No evalúa calidad pedagógica ni semántica del texto.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import sys

from markdown_scope import markdown_files as scoped_markdown_files


REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"

ADMONITION_RE = re.compile(
    r'^(?P<indent>\s*)(?P<marker>!!!|\?\?\?)\s+(?P<kind>[A-Za-z][\w-]*)\s+"(?P<title>[^"]+)"\s*$'
)
ADMONITION_BASE_RE = re.compile(
    r'^(?P<indent>\s*)(?P<marker>!!!|\?\?\?)\s+(?P<kind>[A-Za-z][\w-]*)(?P<rest>.*)$'
)
FENCE_RE = re.compile(r"^\s*(?P<fence>`{3,}|~{3,})")
EXERCISE_TITLE_RE = re.compile(r"^Ejercicio\s+(\d+)\.\s+.+$")
SOLUTION_TITLE_RE = re.compile(r"^Solución ejercicio\s+(\d+)$")


@dataclass
class Node:
    kind: str
    marker: str
    title: str
    indent: int
    line_no: int
    file_path: Path
    exercise_number: int | None = None
    has_solution: bool = False


@dataclass
class ParsedAdmonition:
    line_no: int
    indent: int
    marker: str
    kind: str
    title: str | None
    raw_tail: str


def markdown_files() -> list[Path]:
    return scoped_markdown_files(REPO_ROOT)


def parse_markdown(file_path: Path) -> list[ParsedAdmonition]:
    matches: list[ParsedAdmonition] = []
    in_fence = False
    fence_char = ""
    fence_len = 0

    for idx, line in enumerate(file_path.read_text(encoding="utf-8").splitlines(), start=1):
        fence_match = FENCE_RE.match(line)
        if fence_match:
            current_fence = fence_match.group("fence")
            current_char = current_fence[0]
            current_len = len(current_fence)

            if not in_fence:
                in_fence = True
                fence_char = current_char
                fence_len = current_len
                continue

            if current_char == fence_char and current_len >= fence_len:
                in_fence = False
                fence_char = ""
                fence_len = 0
                continue

        if in_fence:
            continue

        match = ADMONITION_RE.match(line)
        if match:
            indent = len(match.group("indent").replace("\t", "    "))
            matches.append(
                ParsedAdmonition(
                    line_no=idx,
                    indent=indent,
                    marker=match.group("marker"),
                    kind=match.group("kind"),
                    title=match.group("title").strip(),
                    raw_tail="",
                )
            )
            continue

        base_match = ADMONITION_BASE_RE.match(line)
        if base_match and base_match.group("kind") in {"question", "success"}:
            indent = len(base_match.group("indent").replace("\t", "    "))
            matches.append(
                ParsedAdmonition(
                    line_no=idx,
                    indent=indent,
                    marker=base_match.group("marker"),
                    kind=base_match.group("kind"),
                    title=None,
                    raw_tail=base_match.group("rest").strip(),
                )
            )
    return matches


def is_exercise_question_candidate(item: ParsedAdmonition) -> bool:
    if item.kind != "question":
        return False
    if item.title is not None:
        return item.title.startswith("Ejercicio ")
    return item.raw_tail.startswith("Ejercicio ")


def is_solution_candidate(item: ParsedAdmonition) -> bool:
    if item.kind != "success":
        return False
    if item.title is not None:
        return item.title.startswith("Solución ejercicio ")
    return item.raw_tail.startswith("Solución ejercicio ")


def display_path(file_path: Path) -> str:
    try:
        return file_path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return file_path.as_posix()


def close_node(node: Node, errors: list[str]) -> None:
    if node.kind == "question" and node.exercise_number is not None and not node.has_solution:
        rel = display_path(node.file_path)
        errors.append(
            f"[{rel}:{node.line_no}] [exercise-solution] el ejercicio {node.exercise_number} no tiene solución success interna"
        )


def validate_file(file_path: Path) -> list[str]:
    diagnostics: list[str] = []
    stack: list[Node] = []
    rel = display_path(file_path)

    for item in parse_markdown(file_path):
        line_no = item.line_no
        indent = item.indent
        marker = item.marker
        kind = item.kind
        title = item.title or ""

        while stack and indent <= stack[-1].indent:
            close_node(stack.pop(), diagnostics)

        ancestors = stack.copy()

        in_exercise = any(node.kind == "question" and node.exercise_number is not None for node in ancestors)
        in_solution = any(node.kind == "success" for node in ancestors)

        if in_solution:
            diagnostics.append(
                f"WARN [{rel}:{line_no}] [exercise-nesting] admonition extra dentro de solución; evitar anidaciones adicionales"
            )
        elif in_exercise and kind != "success":
            diagnostics.append(
                f"WARN [{rel}:{line_no}] [exercise-nesting] admonition no canónica dentro de ejercicio; usar solo solución success salvo necesidad didáctica justificada"
            )

        if kind == "question" and is_exercise_question_candidate(item):
            if marker != "!!!":
                diagnostics.append(
                    f"[{rel}:{line_no}] [exercise-marker] el ejercicio debe usar '!!! question'"
                )

            exercise_match = EXERCISE_TITLE_RE.fullmatch(title) if item.title is not None else None
            exercise_number = int(exercise_match.group(1)) if exercise_match else None
            if exercise_match is None:
                diagnostics.append(
                    f"[{rel}:{line_no}] [exercise-title] título inválido; esperado: 'Ejercicio N. Título'"
                )

            stack.append(
                Node(
                    kind=kind,
                    marker=marker,
                    title=title,
                    indent=indent,
                    line_no=line_no,
                    file_path=file_path,
                    exercise_number=exercise_number,
                )
            )
            continue

        if kind == "success" and (in_exercise or is_solution_candidate(item)):
            if marker != "???":
                diagnostics.append(
                    f"[{rel}:{line_no}] [solution-marker] la solución debe usar admonition colapsable '??? success'"
                )

            if not stack or stack[-1].kind != "question" or stack[-1].exercise_number is None:
                diagnostics.append(
                    f"[{rel}:{line_no}] [solution-placement] solución success fuera de un ejercicio question"
                )
                stack.append(
                    Node(
                        kind=kind,
                        marker=marker,
                        title=title,
                        indent=indent,
                        line_no=line_no,
                        file_path=file_path,
                    )
                )
                continue

            solution_match = SOLUTION_TITLE_RE.fullmatch(title) if item.title is not None else None
            solution_number = int(solution_match.group(1)) if solution_match else None
            if solution_match is None:
                diagnostics.append(
                    f"[{rel}:{line_no}] [solution-title] título inválido; esperado: 'Solución ejercicio N'"
                )
            else:
                exercise_number = stack[-1].exercise_number
                if exercise_number != solution_number:
                    diagnostics.append(
                        f"[{rel}:{line_no}] [solution-number] la solución indica ejercicio {solution_number} y debería ser {exercise_number}"
                    )

            stack[-1].has_solution = True
            stack.append(
                Node(
                    kind=kind,
                    marker=marker,
                    title=title,
                    indent=indent,
                    line_no=line_no,
                    file_path=file_path,
                )
            )
            continue

        stack.append(
            Node(
                kind=kind,
                marker=marker,
                title=title,
                indent=indent,
                line_no=line_no,
                file_path=file_path,
            )
        )

    while stack:
        close_node(stack.pop(), diagnostics)

    return diagnostics


def main() -> int:
    if not DOCS_DIR.is_dir():
        print(f"ERROR: no se encuentra {DOCS_DIR}", file=sys.stderr)
        return 2

    try:
        files = markdown_files()
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    errors: list[str] = []
    warnings: list[str] = []

    for file_path in files:
        for diagnostic in validate_file(file_path):
            if diagnostic.startswith("WARN "):
                warnings.append(diagnostic.removeprefix("WARN "))
            else:
                errors.append(diagnostic)

    if errors:
        print("❌ Validación editorial: FALLIDA")
        for error in sorted(errors):
            print(f" - {error}")
        if warnings:
            print("⚠️ Advertencias no bloqueantes:")
            for warning in sorted(warnings):
                print(f" - {warning}")
        return 1

    if warnings:
        print("✅ Validación editorial: OK (con advertencias no bloqueantes)")
        for warning in sorted(warnings):
            print(f" - {warning}")
        print(f"   - Markdown revisados en docs/: {len(files)}")
        return 0

    print("✅ Validación editorial: OK")
    print(f"   - Markdown revisados en docs/: {len(files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
