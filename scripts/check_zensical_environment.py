#!/usr/bin/env python3
"""Check the reproducible Zensical environment and temporary fixtures."""

from __future__ import annotations

import importlib
import importlib.metadata
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib


ROOT = Path(__file__).resolve().parent.parent
VENV = (ROOT / ".venv").resolve()
ZENSICAL_VERSION = "0.0.67"


def fail(message: str) -> None:
    raise RuntimeError(message)


def check_interpreter() -> None:
    if sys.version_info < (3, 11):
        fail(f"Python 3.11+ requerido; detectado {sys.version.split()[0]}")
    if Path(sys.prefix).resolve() != VENV:
        fail(f"la ejecución no procede de {VENV} (sys.prefix={sys.prefix})")
    print(f"✅ Python {sys.version.split()[0]} desde .venv")


def check_installation() -> None:
    version = importlib.metadata.version("zensical")
    if version != ZENSICAL_VERSION:
        fail(f"Zensical {ZENSICAL_VERSION} requerido; detectado {version}")
    executable = VENV / "bin" / "zensical"
    if not executable.is_file() or not os.access(executable, os.X_OK):
        fail(f"no existe el ejecutable esperado: {executable}")
    result = subprocess.run([str(executable), "--version"], text=True, capture_output=True)
    if result.returncode != 0 or ZENSICAL_VERSION not in result.stdout:
        fail(f"{executable} --version no confirma {ZENSICAL_VERSION}")
    for module in ("pymdownx.superfences", "pymdownx.tabbed"):
        importlib.import_module(module)
    print("✅ Zensical 0.0.67 y extensiones SuperFences/Tabbed disponibles")


def check_configuration() -> None:
    data = tomllib.loads((ROOT / "zensical.toml").read_text(encoding="utf-8"))
    extensions = data["project"]["markdown_extensions"]["pymdownx"]
    fence = extensions["superfences"]["custom_fences"]
    if {item.get("name") for item in fence} != {"mermaid"}:
        fail("zensical.toml no declara exactamente el custom fence Mermaid")
    if fence[0].get("class") != "mermaid":
        fail("el custom fence Mermaid no declara class = mermaid")
    tabbed = extensions["tabbed"]
    if tabbed != {"alternate_style": True, "combine_header_slug": True}:
        fail("la configuración Tabbed no coincide con la sintaxis soportada")
    print("✅ configuración explícita validada contra Zensical 0.0.67")


def check_fixtures() -> None:
    config = """[project]\nsite_name = \"Fixture\"\nnav = [{\"Inicio\" = \"index.md\"}]\n\n[project.markdown_extensions.pymdownx.superfences]\ncustom_fences = [{ name = \"mermaid\", class = \"mermaid\" }]\n\n[project.markdown_extensions.pymdownx.tabbed]\nalternate_style = true\ncombine_header_slug = true\n"""
    markdown = """# Fixtures\n\n=== \"Primera alternativa\"\n\n    Contenido de la primera alternativa.\n\n=== \"Segunda alternativa\"\n\n    Contenido de la segunda alternativa.\n\n```mermaid\ngraph TD\n    A-->B\n```\n\n```text\ngraph TD\n```\n"""
    with tempfile.TemporaryDirectory(prefix="zensical-fixture-") as directory:
        project = Path(directory)
        (project / "docs").mkdir()
        (project / "docs/index.md").write_text(markdown, encoding="utf-8")
        (project / "zensical.toml").write_text(config, encoding="utf-8")
        result = subprocess.run(
            [str(VENV / "bin" / "zensical"), "build", "--clean", "--strict"],
            cwd=project,
            text=True,
            capture_output=True,
        )
        if result.returncode != 0:
            fail(f"fixture no compila:\n{result.stdout}\n{result.stderr}")
        html = (project / "site/index.html").read_text(encoding="utf-8")

    required = ("tabbed-set", "tabbed-content", "Primera alternativa", "Contenido de la primera alternativa")
    if not all(item in html for item in required):
        fail("fixture tabs no produce la estructura HTML esperada")
    mermaid = re.search(r'<pre class="mermaid"><code>(.*?)</code></pre>', html, re.S)
    ordinary = re.search(r'<div class="highlight"><pre>(.*?)</pre></div>', html, re.S)
    if not mermaid or "graph TD" not in mermaid.group(1):
        fail("fixture Mermaid no produce pre.mermaid con contenido")
    if not ordinary or "mermaid" in ordinary.group(0):
        fail("el code block ordinario no se distingue del fence Mermaid")
    print("✅ fixture tabs: HTML estructural verificado")
    print("✅ fixture Mermaid: HTML estructural verificado; runtime visual no verificado")


def report_browser_runtime() -> None:
    browsers = [name for name in ("chromium", "google-chrome", "firefox", "safari") if shutil.which(name)]
    if browsers:
        print("⚠️ navegador local detectado (" + ", ".join(browsers) + "); no se declara verificación visual sin driver/automatización")
    else:
        print("ℹ️ sin runtime visual de navegador detectable; Mermaid visual queda pendiente")


def main() -> int:
    try:
        check_interpreter()
        check_installation()
        check_configuration()
        check_fixtures()
        report_browser_runtime()
    except (OSError, KeyError, ValueError, importlib.metadata.PackageNotFoundError, RuntimeError) as error:
        print(f"❌ check-environment: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
