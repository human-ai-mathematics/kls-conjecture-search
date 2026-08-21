"""Focused regression tests for the research control-plane checker.

Run from the repository root with::

    python3 -m unittest discover -s research/tests -p 'test_*.py'

The fixtures live in temporary directories, so these tests never modify the real
ledgers or append-only run artifacts.
"""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("research_check_ledger", REPO / "research/check_ledger.py")
CHECKER = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(CHECKER)


def node(node_id: str, *, status: str = "proved", kind: str = "theorem", **fields):
    result = {
        "id": node_id,
        "kind": kind,
        "status": status,
        "file": "modules/test.tex",
        "statement": f"fixture statement for {node_id}",
    }
    result.update(fields)
    return result


class CheckerFixture(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        self.research = self.root / "research"
        self.research.mkdir(parents=True)
        modules = self.root / "modules"
        modules.mkdir()
        (modules / "test.tex").write_text("fixture\n")

    def tearDown(self):
        self.tempdir.cleanup()

    def add_ledger(self, relative: str, program: str, nodes: list[dict], *,
                   obstruction_doc: dict | None = None, obstruction_md: str = "") -> Path:
        path = self.research / relative / "ledger.yaml"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(CHECKER.yaml.safe_dump({"meta": {"program": program}, "nodes": nodes}, sort_keys=False))
        if obstruction_doc is not None:
            path.with_name("obstructions.yaml").write_text(
                CHECKER.yaml.safe_dump(obstruction_doc, sort_keys=False)
            )
            path.with_name("obstructions.md").write_text(obstruction_md)
        return path

    def add_artifact(self, name: str, *, dirty: bool, valid: bool = True,
                     strong: bool = False) -> str:
        relative = f"research/runs/{name}.jsonl"
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if valid:
            params = {"target": "fixture"}
            if strong:
                params.update({
                    "calibration_passed": True,
                    "shared_battery_passed": True,
                    "shared_battery": "research/knowledge/instances.md",
                })
            header = {
                "_provenance": {
                    "git_commit": "a" * 40,
                    "git_dirty": dirty,
                    "params": params,
                }
            }
            record = {"kind": "verdict" if strong else "diagnostic"}
            path.write_text(json.dumps(header) + "\n" + json.dumps(record) + "\n")
        else:
            path.write_text("{not-json}\n")
        return relative

    def check(self):
        return CHECKER.check_control_plane(self.research, self.root)


class CheckerHardeningTests(CheckerFixture):
    def test_duplicate_program_ledgers_and_node_ids_fail(self):
        duplicated = [node("thm:a"), node("thm:a")]
        self.add_ledger("first", "ab", duplicated)
        self.add_ledger("second", "ab", [node("thm:b")])

        errors = "\n".join(self.check()["errors"])

        self.assertIn("duplicate node id 'thm:a'", errors)
        self.assertIn("duplicate ledger for program 'ab'", errors)

    def test_internal_looking_malformed_id_cannot_escape_resolution(self):
        self.add_ledger(
            "main",
            "ab",
            [node("thm:a", depends_on=["thm:missing_slug", "external theorem in prose"])],
        )

        errors = "\n".join(self.check()["errors"])

        self.assertIn("unknown internal id 'thm:missing_slug'", errors)
        self.assertNotIn("external theorem in prose", errors)

    def test_conditional_contract_and_recursive_proved_risks(self):
        nodes = [
            node("ass:x", status="open", kind="assumption"),
            node("ass:y", status="open", kind="assumption"),
            node("thm:empty", status="conditional", depends_on=["ass:x"]),
            node(
                "thm:child",
                status="conditional",
                depends_on=["ass:x"],
                assuming=["ass:x"],
            ),
            node(
                "thm:parent",
                status="conditional",
                depends_on=["thm:child"],
                assuming=["ass:y"],
            ),
            node("heur:h", status="heuristic", kind="heuristic"),
            node("thm:middle", status="imported", depends_on=["heur:h"]),
            node("thm:top", depends_on=["thm:middle"]),
            node("thm:direct", depends_on=["thm:empty"]),
        ]
        self.add_ledger("main", "kls", nodes)

        errors = "\n".join(self.check()["errors"])

        self.assertIn("thm:empty: conditional status requires non-empty assuming", errors)
        self.assertIn(
            "thm:parent (conditional) does not propagate inherited assumptions ['ass:x']",
            errors,
        )
        self.assertIn("thm:top (proved) inherits unresolved heuristic 'heur:h'", errors)
        self.assertIn("thm:direct (proved) inherits unresolved conditional 'thm:empty'", errors)
        self.assertIn("thm:direct (proved) inherits unresolved open 'ass:x'", errors)

    def test_unreviewed_preprint_is_an_inherited_assumption(self):
        nodes = [
            node(
                "thm:preprint",
                status="imported",
                import_class="preprint-unreviewed",
            ),
            node("thm:published", status="imported"),
            node(
                "thm:conditional",
                status="conditional",
                depends_on=["thm:preprint"],
                assuming=["thm:preprint"],
            ),
            node("thm:middle", depends_on=["thm:preprint"]),
            node("thm:top", depends_on=["thm:middle"]),
            node("thm:published-use", depends_on=["thm:published"]),
        ]
        self.add_ledger("main", "kls", nodes)

        errors = "\n".join(self.check()["errors"])

        self.assertIn("thm:middle (proved) inherits unresolved preprint-unreviewed 'thm:preprint'", errors)
        self.assertIn("thm:top (proved) inherits unresolved preprint-unreviewed 'thm:preprint'", errors)
        self.assertNotIn("thm:conditional (conditional) does not propagate", errors)
        self.assertNotIn("thm:published-use (proved) inherits", errors)

    def test_dirty_historical_artifact_is_validated_but_not_evidence_eligible(self):
        dirty = self.add_artifact("dirty", dirty=True)
        clean = self.add_artifact("clean", dirty=False)
        nodes = [
            node("obs:history", kind="obstruction", evidence_run=dirty),
            node(
                "conj:dirty",
                status="conjectured",
                kind="conjecture",
                evidence="numerical-directional",
                evidence_run=dirty,
                evidence_target="fixture",
            ),
            node(
                "conj:clean",
                status="conjectured",
                kind="conjecture",
                evidence="numerical-directional",
                evidence_run=clean,
                evidence_target="fixture",
            ),
        ]
        self.add_ledger("main", "ab", nodes)

        errors = self.check()["errors"]
        dirty_errors = [error for error in errors if "evidence-eligible run" in error]

        self.assertEqual(len(dirty_errors), 1)
        self.assertIn("conj:dirty", dirty_errors[0])

    def test_evidence_run_must_exist_and_be_valid_jsonl(self):
        malformed = self.add_artifact("malformed", dirty=False, valid=False)
        nodes = [
            node("obs:missing", kind="obstruction", evidence_run="research/runs/missing.jsonl"),
            node("obs:malformed", kind="obstruction", evidence_run=malformed),
        ]
        self.add_ledger("main", "ab", nodes)

        errors = "\n".join(self.check()["errors"])

        self.assertIn("research/runs/missing.jsonl' does not exist", errors)
        self.assertIn("invalid JSON on line 1", errors)

    def test_local_git_commit_validation(self):
        head = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=REPO,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.strip()

        self.assertTrue(CHECKER._git_commit_exists(REPO, head))
        self.assertFalse(CHECKER._git_commit_exists(REPO, "f" * 40))

    def test_numerical_strong_requires_calibration_battery_and_verdict(self):
        weak_artifact = self.add_artifact("weak", dirty=False)
        strong_artifact = self.add_artifact("strong", dirty=False, strong=True)
        nodes = [
            node(
                "conj:weak",
                status="conjectured",
                kind="conjecture",
                evidence="numerical-strong",
                evidence_run=weak_artifact,
                evidence_target="fixture",
            ),
            node(
                "conj:strong",
                status="conjectured",
                kind="conjecture",
                evidence="numerical-strong",
                evidence_run=strong_artifact,
                evidence_target="fixture",
            ),
        ]
        self.add_ledger("main", "ab", nodes)

        errors = "\n".join(self.check()["errors"])

        self.assertIn("conj:weak: numerical-strong", errors)
        self.assertIn("lacks calibration_passed=true", errors)
        self.assertIn("lacks shared_battery_passed=true", errors)
        self.assertIn("has no verdict record", errors)
        self.assertNotIn("conj:strong: numerical-strong", errors)

    def test_reverse_constrains_parity_and_warn_clearance_are_enforced(self):
        obstructions = {
            "mechanisms": ["direct-excess"],
            "obstructions": [{
                "id": "obs:warning",
                "forbids": [],
                "warns": ["direct-excess"],
                "constrains": [],
            }],
        }
        self.add_ledger(
            "main",
            "kls",
            [node("thm:a", mechanism=["direct-excess"], bounded_by=["obs:warning"])],
            obstruction_doc=obstructions,
            obstruction_md="## `obs:warning`\n",
        )

        errors = "\n".join(self.check()["errors"])

        self.assertIn("obs:warning.constrains reverse parity mismatch", errors)
        self.assertIn("warned about by obs:warning lacks a clearance note", errors)

    def test_clean_conditional_evidence_and_warning_contract_passes(self):
        clean = self.add_artifact("clean", dirty=False)
        obstructions = {
            "mechanisms": ["direct-excess"],
            "obstructions": [{
                "id": "obs:warning",
                "forbids": [],
                "warns": ["direct-excess"],
                "constrains": ["q:open"],
            }],
        }
        nodes = [
            node("ass:x", status="open", kind="assumption"),
            node(
                "thm:conditional",
                status="conditional",
                depends_on=["ass:x"],
                assuming=["ass:x"],
            ),
            node(
                "q:open",
                status="open",
                kind="question",
                mechanism=["direct-excess"],
                bounded_by=["obs:warning"],
                clearance="The fixture acknowledges the warning.",
                evidence="numerical-directional",
                evidence_run=clean,
                evidence_target="fixture",
            ),
        ]
        self.add_ledger(
            "main",
            "kls",
            nodes,
            obstruction_doc=obstructions,
            obstruction_md="## `obs:warning`\n",
        )
        self.add_ledger("ab", "ab", [node("thm:ab")])

        self.assertEqual(self.check()["errors"], [])

    def test_missing_configured_program_and_malformed_types_report_without_crashing(self):
        malformed = node("thm:bad")
        malformed.update({
            "kind": [],
            "status": [],
            "file": [],
            "evidence": [],
            "checked_by": {},
            "solution": {},
            "depends_on": [{}],
            "bounded_by": [{}],
            "refines": {},
        })
        self.add_ledger("main", "ab", [malformed])

        errors = "\n".join(self.check()["errors"])

        self.assertIn("missing ledger for configured program 'kls'", errors)
        self.assertIn("bad kind '[]'", errors)
        self.assertIn("status '[]' not allowed", errors)
        self.assertIn("references must be non-empty strings", errors)

    def test_cli_reports_malformed_status_instead_of_crashing(self):
        malformed = node("thm:bad")
        malformed["status"] = []
        self.add_ledger("main", "ab", [malformed])
        script = self.research / "check_ledger.py"
        script.write_text((REPO / "research/check_ledger.py").read_text())

        result = subprocess.run(
            [sys.executable, str(script)],
            cwd=self.root,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 1)
        self.assertIn("status '[]' not allowed", result.stdout)
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
