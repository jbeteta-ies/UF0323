#!/usr/bin/env python3
"""Focused regression tests for navigation scope and target validation."""

from __future__ import annotations

from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import validate_zensical_nav as nav


class ValidateZensicalNavTests(unittest.TestCase):
    def test_in_scope_parent_target_is_normalized_before_probe_and_duplicates(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            docs_dir = Path(tmp)
            probes: list[Path] = []

            def probe(path: Path) -> bool:
                probes.append(path)
                return True

            with patch.object(nav, "DOCS_DIR", docs_dir):
                with patch.object(Path, "is_file", probe):
                    errors = nav.validate_targets(["nivelacion/../index.md", "index.md"])

        self.assertEqual(probes, [docs_dir / "index.md", docs_dir / "index.md"])
        self.assertTrue(all(path.is_relative_to(docs_dir) for path in probes))
        self.assertTrue(any("[duplicate]" in error and "'index.md'" in error for error in errors))
        self.assertFalse(any("[escaping]" in error for error in errors))

    def test_absolute_and_parent_targets_do_not_probe_filesystem(self) -> None:
        with patch.object(Path, "is_file", side_effect=AssertionError("unexpected probe")):
            errors = nav.validate_targets(
                ["/outside.md", " /outside.md", "../outside.md", "nested/../../outside.md"]
            )

        self.assertEqual(sum("[escaping]" in error for error in errors), 5)
        self.assertFalse(any("[missing]" in error for error in errors))

    def test_git_failure_is_reported_by_nav_main_path(self) -> None:
        with patch.object(nav, "markdown_files_in_docs", side_effect=RuntimeError("git ls-files failed")):
            with patch.object(nav, "CONFIG_FILE") as config_file, patch.object(nav, "DOCS_DIR") as docs_dir:
                config_file.is_file.return_value = True
                docs_dir.is_dir.return_value = True
                with patch.object(nav, "load_nav_targets", return_value=([], [])):
                    self.assertEqual(nav.main(), 2)


if __name__ == "__main__":
    unittest.main()
