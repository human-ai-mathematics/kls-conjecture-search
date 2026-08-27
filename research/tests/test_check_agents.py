"""Regression tests for the cross-client agent-definition checker."""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]


class AgentCheckerFixture(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        shutil.copytree(REPO / ".claude", self.root / ".claude")
        shutil.copytree(REPO / ".codex", self.root / ".codex")
        (self.root / "research").mkdir()
        shutil.copy2(REPO / "research/check_agents.py", self.root / "research/check_agents.py")

    def tearDown(self):
        self.tempdir.cleanup()

    def run_checker(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "research/check_agents.py"],
            cwd=self.root,
            check=False,
            capture_output=True,
            text=True,
        )

    def test_generated_adapters_match_canonical_roles(self):
        result = self.run_checker()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("0 errors (13 roles)", result.stdout)

    def test_stale_codex_adapter_is_rejected(self):
        adapter = self.root / ".codex/agents/scout.toml"
        adapter.write_text(adapter.read_text(encoding="utf-8") + "# stale\n", encoding="utf-8")
        result = self.run_checker()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("stale or hand-edited", result.stdout)

    def test_codex_model_and_effort_policy(self):
        ultra_roles = {
            "kls-route-prober",
            "kls-route-scout",
            "proof-checker",
            "proof-miner",
            "prover",
            "refiner",
            "refutation-seeker",
            "synthesizer",
        }
        for adapter in sorted((self.root / ".codex/agents").glob("*.toml")):
            parsed = tomllib.loads(adapter.read_text(encoding="utf-8"))
            with self.subTest(role=parsed["name"]):
                self.assertEqual(parsed["model"], "gpt-5.6-sol")
                expected_effort = "ultra" if parsed["name"] in ultra_roles else "high"
                self.assertEqual(parsed["model_reasoning_effort"], expected_effort)

    def test_read_only_claude_role_cannot_declare_write_tool(self):
        role = self.root / ".claude/agents/scout.md"
        text = role.read_text(encoding="utf-8")
        role.write_text(
            text.replace("tools: Read, Grep, Glob, Bash", "tools: Read, Grep, Glob, Bash, Write"),
            encoding="utf-8",
        )
        result = self.run_checker()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("read-only role declares a write tool", result.stdout)


if __name__ == "__main__":
    unittest.main()
