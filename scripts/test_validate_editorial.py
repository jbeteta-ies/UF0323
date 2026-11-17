#!/usr/bin/env python3
"""Pruebas reproducibles del validador editorial.

Objetivo: asegurar cobertura del patrón canónico (casos válidos e inválidos)
y el comportamiento de diagnóstico (errores bloqueantes y advertencias).
"""

from __future__ import annotations

from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import validate_editorial as ve
import markdown_scope


class ValidateEditorialTests(unittest.TestCase):
    def _validate(self, content: str) -> list[str]:
        with tempfile.TemporaryDirectory() as tmp:
            file_path = Path(tmp) / "case.md"
            file_path.write_text(content, encoding="utf-8")
            return ve.validate_file(file_path)

    def test_canonical_positive_case_has_no_diagnostics(self) -> None:
        content = """!!! question \"Ejercicio 1. Comprobar conectividad\"

    Ejecuta una verificación básica de red.

    ??? success \"Solución ejercicio 1\"

        Se usa `ping` y se comprueba respuesta sin pérdida de paquetes.
"""

        self.assertEqual(self._validate(content), [])

    def test_ignores_admonitions_inside_code_fences(self) -> None:
        content = """```md
!!! question \"Ejercicio 1. No debe validar dentro de fence\"

    ??? success \"Solución ejercicio 1\"
```
"""

        self.assertEqual(self._validate(content), [])

    def test_exercise_title_error(self) -> None:
        content = """!!! question \"Ejercicio uno sin formato\"

    ??? success \"Solución ejercicio 1\"

        Texto.
"""

        diagnostics = self._validate(content)
        self.assertTrue(any("[exercise-title]" in d for d in diagnostics))

    def test_solution_title_error(self) -> None:
        content = """!!! question \"Ejercicio 1. Título válido\"

    ??? success \"Solución 1\"

        Texto.
"""

        diagnostics = self._validate(content)
        self.assertTrue(any("[solution-title]" in d for d in diagnostics))

    def test_solution_number_error(self) -> None:
        content = """!!! question \"Ejercicio 2. Título válido\"

    ??? success \"Solución ejercicio 3\"

        Texto.
"""

        diagnostics = self._validate(content)
        self.assertTrue(any("[solution-number]" in d for d in diagnostics))

    def test_solution_marker_error(self) -> None:
        content = """!!! question \"Ejercicio 1. Título válido\"

    !!! success \"Solución ejercicio 1\"

        Texto.
"""

        diagnostics = self._validate(content)
        self.assertTrue(any("[solution-marker]" in d for d in diagnostics))

    def test_solution_placement_error(self) -> None:
        content = """??? success \"Solución ejercicio 1\"

    Texto.
"""

        diagnostics = self._validate(content)
        self.assertTrue(any("[solution-placement]" in d for d in diagnostics))

    def test_exercise_nesting_warning_is_non_blocking_code(self) -> None:
        content = """!!! question \"Ejercicio 1. Título válido\"

    !!! note \"Pista\"

        Considera el contexto.

    ??? success \"Solución ejercicio 1\"

        Texto.
"""

        diagnostics = self._validate(content)
        self.assertTrue(any(d.startswith("WARN ") and "[exercise-nesting]" in d for d in diagnostics))

    def test_detects_missing_solution_in_real_question(self) -> None:
        content = """!!! question \"Ejercicio 2. Falta solución\"

    Enunciado sin bloque success.
"""

        diagnostics = self._validate(content)
        self.assertTrue(any("[exercise-solution]" in d for d in diagnostics))

    def test_missing_quotes_on_question_title_is_detected(self) -> None:
        content = """!!! question Ejercicio 1. Sin comillas

    ??? success \"Solución ejercicio 1\"

        Texto.
"""

        diagnostics = self._validate(content)
        self.assertTrue(any("[exercise-title]" in d for d in diagnostics))

    def test_missing_quotes_on_success_title_is_detected(self) -> None:
        content = """!!! question \"Ejercicio 1. Título válido\"

    ??? success Solución ejercicio 1

        Texto.
"""

        diagnostics = self._validate(content)
        self.assertTrue(any("[solution-title]" in d for d in diagnostics))

    def test_non_exercise_question_is_ignored(self) -> None:
        content = """!!! question \"Pregunta de reflexión\"

    Describe brevemente tu experiencia.
"""

        self.assertEqual(self._validate(content), [])

    def test_non_exercise_success_is_ignored(self) -> None:
        content = """??? success \"Resultado esperado\"

    Texto informativo.
"""

        self.assertEqual(self._validate(content), [])

    def test_solution_like_block_outside_exercise_is_still_reported(self) -> None:
        content = """??? success \"Solución ejercicio 1\"

    Texto.
"""

        diagnostics = self._validate(content)
        self.assertTrue(any("[solution-placement]" in d for d in diagnostics))

    def test_exercise_like_question_without_quotes_is_still_reported(self) -> None:
        content = """!!! question Ejercicio 1. Sin comillas

    Texto.
"""

        diagnostics = self._validate(content)
        self.assertTrue(any("[exercise-title]" in d for d in diagnostics))

    def test_markdown_discovery_uses_git_candidates_and_read_scope(self) -> None:
        repo = Path("/repo")
        output = (
            "docs/tracked.md\n"
            "docs/tracked-ignored.md\n"
            "docs/untracked-nonignored.md\n"
            "site/generated.md\n"
            ".venv/generated.md\n"
            ".cache/generated.md\n"
            "build/generated.md\n"
            "dist/generated.md\n"
            "outside.md\n"
        )
        with patch.object(
            markdown_scope.subprocess,
            "run",
            return_value=type("Result", (), {"returncode": 0, "stdout": output, "stderr": ""})(),
        ) as run:
            with patch.object(Path, "is_file", return_value=True):
                files = markdown_scope.markdown_files(repo)

        self.assertEqual(
            files,
            [
                repo / "docs/tracked-ignored.md",
                repo / "docs/tracked.md",
                repo / "docs/untracked-nonignored.md",
            ],
        )
        self.assertNotIn(repo / "docs/ignored-untracked.md", files)
        run.assert_called_once_with(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
            cwd=repo,
            check=False,
            capture_output=True,
            text=True,
        )

    def test_git_candidate_failure_is_reported(self) -> None:
        result = type("Result", (), {"returncode": 128, "stdout": "", "stderr": "not a repository"})()
        with patch.object(markdown_scope.subprocess, "run", return_value=result):
            with self.assertRaisesRegex(RuntimeError, "git ls-files failed"):
                markdown_scope.markdown_files(Path("/repo"))


if __name__ == "__main__":
    unittest.main()
