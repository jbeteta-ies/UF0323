#!/usr/bin/env python3
"""Validaciones locales de navegación/documentación para zensical.toml.

Comprobaciones implementadas:
- Targets de navegación inexistentes.
- Targets que requieren escape (espacios/caracteres fuera del set permitido).
- Targets no Markdown.
- Targets duplicados.
- Páginas Markdown huérfanas (presentes en docs/ y no referenciadas en nav).
- Convenciones de nombres de archivo documentadas en CONTRIBUTING-CONVENTIONS.md.
"""

from __future__ import annotations

from collections import Counter
import os
from pathlib import Path
import shutil
import re
import subprocess
import sys

from markdown_scope import markdown_files as scoped_markdown_files

try:
    import tomllib
except ModuleNotFoundError:  # Python < 3.11
    tomllib = None


REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"
CONFIG_FILE = REPO_ROOT / "zensical.toml"
MIN_PYTHON = (3, 11)
EDITORIAL_VALIDATOR = REPO_ROOT / "scripts" / "validate_editorial.py"

ALLOWED_TARGET_RE = re.compile(r"^[A-Za-z0-9._/-]+$")
GENERAL_FILENAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
CONTENIDOS_FILENAME_RE = re.compile(r"^\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*\.md$")

# Excepciones editoriales aprobadas para las rutas públicas y estables de las píldoras IA01 e IA02.
# Se limitan a esas rutas exactas; no modifican las convenciones generales de nombres.
APPROVED_FILENAME_EXCEPTIONS = {
    "README.md",
    "recursos/pildoras_ia_01.md",
    "recursos/pildoras_ia_02.md",
    "recursos/pildoras_ia_03.md",
}


def load_nav_targets(config_path: Path) -> tuple[list[str], list[str]]:
    data = tomllib.loads(config_path.read_text(encoding="utf-8"))
    nav = data.get("project", {}).get("nav", [])
    targets: list[str] = []
    errors: list[str] = []

    def walk(node: object) -> None:
        # Supuesto soportado: zensical.toml usa nav como estructura compuesta
        # de listas/diccionarios y hojas de tipo str con paths relativos a docs/.
        if isinstance(node, str):
            targets.append(node)
            return
        if isinstance(node, list):
            for item in node:
                walk(item)
            return
        if isinstance(node, dict):
            for value in node.values():
                walk(value)
            return

        errors.append(
            f"[nav-schema] nodo de nav no soportado ({type(node).__name__}); "
            "se esperaban str/list/dict"
        )

    walk(nav)
    return targets, errors


def normalize_rel_path(path: str) -> str:
    """Normalize a nav target lexically, without touching the filesystem."""
    target = path.strip()
    absolute = target.startswith("/")
    parts: list[str] = []

    for part in target.split("/"):
        if not part or part == ".":
            continue
        if part == ".." and parts and parts[-1] != "..":
            parts.pop()
        else:
            parts.append(part)

    normalized = "/".join(parts)
    return f"/{normalized}" if absolute else normalized


def is_in_docs_scope(target: str) -> bool:
    """Return whether a normalized target is relative and cannot escape docs/."""
    return not target.startswith("/") and ".." not in target.split("/")


def validate_targets(targets: list[str]) -> list[str]:
    errors: list[str] = []
    normalized = [normalize_rel_path(t) for t in targets]

    for raw, target in zip(targets, normalized, strict=True):
        if not target.endswith(".md"):
            errors.append(f"[non-markdown] '{raw}' no termina en .md")

        absolute = target.startswith("/")
        path_traversal = ".." in target.split("/")
        escaping = "\\" in raw or absolute or path_traversal

        if "\\" in raw or absolute:
            errors.append(f"[escaping] '{raw}' usa separadores/ruta no válidos para nav")

        if path_traversal:
            errors.append(f"[escaping] '{raw}' contiene '..' (path traversal)")

        if not ALLOWED_TARGET_RE.fullmatch(raw):
            errors.append(
                f"[escaping] '{raw}' contiene caracteres que requieren escape "
                "(permitidos: a-z, 0-9, ., _, -, /)"
            )

        # Probe only after lexical normalization and scope validation. This
        # also prevents absolute targets from making Path discard DOCS_DIR.
        if escaping or not is_in_docs_scope(target):
            continue

        file_path = DOCS_DIR / target
        if not file_path.is_file():
            errors.append(f"[missing] '{raw}' no existe en docs/")

    duplicates = [item for item, count in Counter(normalized).items() if count > 1]
    for dup in sorted(duplicates):
        errors.append(f"[duplicate] target repetido en nav: '{dup}'")

    return errors


def markdown_files_in_docs() -> list[Path]:
    return scoped_markdown_files(REPO_ROOT)


def validate_orphans(nav_targets: list[str], markdown_files: list[Path]) -> list[str]:
    errors: list[str] = []
    nav_set = {normalize_rel_path(t) for t in nav_targets}

    for file_path in markdown_files:
        relative = file_path.relative_to(DOCS_DIR).as_posix()
        if relative not in nav_set:
            errors.append(f"[orphan] '{relative}' existe en docs/ pero no aparece en nav")

    return errors


def validate_filename_conventions(markdown_files: list[Path]) -> list[str]:
    errors: list[str] = []

    for file_path in markdown_files:
        relative = file_path.relative_to(DOCS_DIR)
        rel_posix = relative.as_posix()
        filename = file_path.name

        if filename == "index.md":
            continue

        if rel_posix in APPROVED_FILENAME_EXCEPTIONS:
            continue

        if not GENERAL_FILENAME_RE.fullmatch(filename):
            errors.append(
                f"[naming] '{rel_posix}' no cumple kebab-case en minúsculas "
                "(sin espacios/tildes/caracteres especiales)"
            )

        if relative.parent.as_posix() == "bloques-formativos" and not CONTENIDOS_FILENAME_RE.fullmatch(
            filename
        ):
            errors.append(
                f"[naming] '{rel_posix}' debe usar prefijo numérico de dos dígitos "
                "(ej: 01-tema.md)"
            )

    return errors


def locate_zensical_executable() -> str | None:
    candidates = [
        Path(sys.executable).resolve().with_name("zensical"),
        Path(sys.executable).with_name("zensical"),
        Path(sys.prefix) / "bin" / "zensical",
    ]

    for candidate in candidates:
        if candidate.is_file() and os.access(candidate, os.X_OK):
            return str(candidate)

    return shutil.which("zensical")


def run_strict_build() -> int:
    zensical_executable = locate_zensical_executable()
    if zensical_executable is None:
        print("❌ Validación completa (issue #1): FALLIDA")
        print(
            " - [strict-build] No se encontró 'zensical' junto a sys.executable "
            "ni en PATH"
        )
        print(" - Activa el entorno virtual del proyecto e instala dependencias")
        return 2

    print("▶ Ejecutando build estricto: zensical build --clean --strict")
    result = subprocess.run(
        [zensical_executable, "build", "--clean", "--strict"],
        cwd=REPO_ROOT,
        check=False,
    )

    if result.returncode != 0:
        print("❌ Validación completa (issue #1): FALLIDA")
        print(
            " - [strict-build] 'zensical build --clean --strict' terminó con "
            f"código {result.returncode}"
        )
        return 1

    return 0


def run_editorial_validator() -> int:
    if not EDITORIAL_VALIDATOR.is_file():
        print("❌ Validación completa: FALLIDA")
        print(f" - [editorial] No se encontró validador editorial: {EDITORIAL_VALIDATOR}")
        return 2

    print("▶ Ejecutando validador editorial: scripts/validate_editorial.py")
    result = subprocess.run(
        [sys.executable, str(EDITORIAL_VALIDATOR)],
        cwd=REPO_ROOT,
        check=False,
    )

    if result.returncode != 0:
        print("❌ Validación completa: FALLIDA")
        print(
            " - [editorial] 'scripts/validate_editorial.py' terminó con "
            f"código {result.returncode}"
        )
        return 1 if result.returncode == 1 else 2

    return 0


def main() -> int:
    if sys.version_info < MIN_PYTHON:
        current = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        required = f"{MIN_PYTHON[0]}.{MIN_PYTHON[1]}+"
        print("❌ Validación de navegación/documentación: FALLIDA")
        print(f" - [python-version] Se requiere Python {required}; detectado: {current}")
        return 2

    if tomllib is None:
        print("❌ Validación de navegación/documentación: FALLIDA")
        print(" - [python-version] No está disponible 'tomllib'; usa Python 3.11+")
        return 2

    if not CONFIG_FILE.is_file():
        print(f"ERROR: no se encuentra {CONFIG_FILE}", file=sys.stderr)
        return 2
    if not DOCS_DIR.is_dir():
        print(f"ERROR: no se encuentra {DOCS_DIR}", file=sys.stderr)
        return 2

    try:
        targets, nav_schema_errors = load_nav_targets(CONFIG_FILE)
    except tomllib.TOMLDecodeError as exc:
        print("❌ Validación de navegación/documentación: FALLIDA")
        print(f" - [toml] zensical.toml malformado: {exc}")
        return 2

    try:
        markdown_files = markdown_files_in_docs()
    except RuntimeError as exc:
        print("❌ Validación de navegación/documentación: FALLIDA")
        print(f" - [git] {exc}")
        return 2

    errors: list[str] = [*nav_schema_errors]
    errors.extend(validate_targets(targets))
    errors.extend(validate_orphans(targets, markdown_files))
    errors.extend(validate_filename_conventions(markdown_files))

    if errors:
        print("❌ Validación de navegación/documentación: FALLIDA")
        for error in sorted(errors):
            print(f" - {error}")
        return 1

    print("✅ Validación de navegación/documentación: OK")
    print(f"   - Targets en nav: {len(targets)}")
    print(f"   - Markdown en docs/: {len(markdown_files)}")

    editorial_status = run_editorial_validator()
    if editorial_status != 0:
        return editorial_status

    build_status = run_strict_build()
    if build_status != 0:
        return build_status

    print("✅ Validación completa: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
