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
                   obstruction_doc: dict | None = None, obstruction_md: str = "",
                   meta_fields: dict | None = None,
                   certify_fixture_proofs: bool = True) -> Path:
        path = self.research / relative / "ledger.yaml"
        path.parent.mkdir(parents=True, exist_ok=True)
        meta = {"program": program}
        if meta_fields:
            meta.update(meta_fields)
        fixture_nodes = [dict(item) for item in nodes]
        if certify_fixture_proofs:
            bare_proved = [
                item for item in fixture_nodes
                if item.get("status") == "proved" and "solution" not in item
            ]
            if bare_proved:
                solution = f"solutions/fixture-{relative.replace('/', '-')}.tex"
                solution_path = self.root / solution
                solution_path.parent.mkdir(parents=True, exist_ok=True)
                covered = "; ".join(str(item.get("id")) for item in bare_proved)
                solution_path.write_text(
                    f"% ledger-nodes: {covered}\nstandalone fixture proofs\n"
                )
                for item in bare_proved:
                    item["solution"] = solution
                    item.setdefault("checked_by", "human")
        path.write_text(
            CHECKER.yaml.safe_dump({"meta": meta, "nodes": fixture_nodes}, sort_keys=False)
        )
        if obstruction_doc is not None:
            path.with_name("obstructions.yaml").write_text(
                CHECKER.yaml.safe_dump(obstruction_doc, sort_keys=False)
            )
            path.with_name("obstructions.md").write_text(obstruction_md)
        return path

    def add_artifact(self, name: str, *, valid: bool = True) -> str:
        relative = f"research/runs/{name}.jsonl"
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if valid:
            params = {"target": "fixture"}
            header = {"_provenance": {"params": params}}
            record = {"kind": "diagnostic"}
            path.write_text(json.dumps(header) + "\n" + json.dumps(record) + "\n")
        else:
            path.write_text("{not-json}\n")
        return relative

    def add_solution(self, name: str, *, node_ids: tuple[str, ...] = ()) -> str:
        relative = f"solutions/{name}.tex"
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        covered = "; ".join(node_ids)
        path.write_text(f"% ledger-nodes: {covered}\nstandalone proof fixture\n")
        return relative

    def add_review(self, name: str, *, verdict: str = "pass",
                   node_ids: tuple[str, ...] = (), reviewer: str = "/root/reviewer") -> str:
        relative = f"research/reviews/{name}.md"
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        covered = " ".join(f"`{node_id}`" for node_id in node_ids)
        path.write_text(
            f"- **Independent reviewer:** `{reviewer}`\n"
            f"- **Verdict:** {verdict} for {covered or 'fixture scope'}\n"
        )
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

    def test_unlocks_is_an_obsolete_field_even_when_empty(self):
        nodes = [
            node("lem:base", unlocks=["thm:uses"]),
            node("q:empty", status="open", kind="question", unlocks=[]),
            node("thm:uses", depends_on=["lem:base"]),
        ]
        self.add_ledger("main", "kls", nodes)

        errors = "\n".join(self.check()["errors"])

        self.assertIn("lem:base.unlocks: obsolete field", errors)
        self.assertIn("q:empty.unlocks: obsolete field", errors)
        self.assertNotIn("already declares", errors)

    def test_ab_conjectured_status_is_rejected_but_open_conjecture_is_valid(self):
        self.add_ledger(
            "main",
            "ab",
            [
                node("conj:open", status="open", kind="conjecture"),
                node("conj:legacy", status="conjectured", kind="conjecture"),
            ],
        )

        errors = "\n".join(self.check()["errors"])

        self.assertNotIn("conj:open: status", errors)
        self.assertIn(
            "conj:legacy: status 'conjectured' is obsolete; use status 'open'",
            errors,
        )

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

    def test_artifacts_are_validated_without_git_metadata(self):
        artifact = self.add_artifact("run")
        nodes = [
            node("obs:history", kind="obstruction", evidence_run=artifact),
            node(
                "conj:directional",
                status="open",
                kind="conjecture",
                evidence="numerical-directional",
                evidence_run=artifact,
                evidence_target="fixture",
            ),
        ]
        self.add_ledger("main", "ab", nodes)

        errors = "\n".join(self.check()["errors"])

        self.assertNotIn("evidence", errors)

    def test_evidence_run_must_exist_and_be_valid_jsonl(self):
        malformed = self.add_artifact("malformed", valid=False)
        nodes = [
            node("obs:missing", kind="obstruction", evidence_run="research/runs/missing.jsonl"),
            node("obs:malformed", kind="obstruction", evidence_run=malformed),
        ]
        self.add_ledger("main", "ab", nodes)

        errors = "\n".join(self.check()["errors"])

        self.assertIn("research/runs/missing.jsonl' does not exist", errors)
        self.assertIn("invalid JSON on line 1", errors)

    def test_numerical_strong_is_rejected(self):
        self.add_ledger(
            "main",
            "ab",
            [
                node(
                    "conj:strong",
                    status="open",
                    kind="conjecture",
                    evidence="numerical-strong",
                ),
            ],
        )

        errors = "\n".join(self.check()["errors"])

        self.assertIn("conj:strong: bad evidence 'numerical-strong'", errors)

    def test_numerical_directional_requires_artifact_and_matching_target(self):
        artifact = self.add_artifact("directional")
        malformed = self.add_artifact("directional-malformed", valid=False)
        nodes = [
            node(
                "conj:missing-run",
                status="open",
                kind="conjecture",
                evidence="numerical-directional",
            ),
            node(
                "conj:missing-target",
                status="open",
                kind="conjecture",
                evidence="numerical-directional",
                evidence_run=artifact,
            ),
            node(
                "conj:mismatched-target",
                status="open",
                kind="conjecture",
                evidence="numerical-directional",
                evidence_run=artifact,
                evidence_target="other-target",
            ),
            node(
                "conj:malformed-run",
                status="open",
                kind="conjecture",
                evidence="numerical-directional",
                evidence_run=malformed,
                evidence_target="fixture",
            ),
        ]
        self.add_ledger("main", "ab", nodes)

        errors = "\n".join(self.check()["errors"])

        self.assertIn("conj:missing-run: evidence eligibility requires evidence_run", errors)
        self.assertIn("conj:missing-target: evidence eligibility requires evidence_target", errors)
        self.assertIn(
            "conj:mismatched-target.evidence_run: target 'fixture' "
            "does not match evidence_target 'other-target'",
            errors,
        )
        self.assertIn("conj:malformed-run.evidence_run: invalid JSON on line 1", errors)

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

    def test_independent_agent_certification_requires_provenance(self):
        solution = self.add_solution(
            "agent-proof",
            node_ids=(
                "thm:agent-pass",
                "thm:agent-self-review",
                "thm:agent-missing-review",
            ),
        )
        review = self.add_review(
            "agent-proof-audit",
            node_ids=("thm:agent-pass", "thm:agent-self-review"),
        )
        nodes = [
            node(
                "thm:agent-pass",
                solution=solution,
                checked_by="agent",
                authored_by="/root/prover",
                reviewed_by="/root/reviewer",
                review=review,
            ),
            node(
                "thm:agent-self-review",
                solution=solution,
                checked_by="agent",
                authored_by="/root/same",
                reviewed_by="/root/same",
                review=review,
            ),
            node(
                "thm:agent-missing-review",
                solution=solution,
                checked_by="agent",
                authored_by="/root/prover",
                reviewed_by="/root/reviewer",
                review="research/reviews/missing.md",
            ),
        ]
        self.add_ledger("main", "ab", nodes)

        errors = "\n".join(self.check()["errors"])

        self.assertNotIn("thm:agent-pass", errors)
        self.assertIn("thm:agent-self-review: agent author and reviewer must be distinct", errors)
        self.assertIn("thm:agent-missing-review.review", errors)

    def test_agent_certification_rejects_partial_or_out_of_scope_review(self):
        solution = self.add_solution(
            "agent-proof",
            node_ids=("thm:partial", "thm:wrong-scope", "thm:wrong-reviewer"),
        )
        partial = self.add_review(
            "partial-audit",
            verdict="partial pass",
            node_ids=("thm:partial",),
        )
        wrong_scope = self.add_review(
            "wrong-scope-audit",
            node_ids=("thm:wrong-scope-extra",),
        )
        wrong_reviewer = self.add_review(
            "wrong-reviewer-audit",
            node_ids=("thm:wrong-reviewer",),
            reviewer="/root/reviewer-extra",
        )
        self.add_ledger(
            "main",
            "ab",
            [
                node(
                    "thm:partial",
                    solution=solution,
                    checked_by="agent",
                    authored_by="/root/prover",
                    reviewed_by="/root/reviewer",
                    review=partial,
                ),
                node(
                    "thm:wrong-scope",
                    solution=solution,
                    checked_by="agent",
                    authored_by="/root/prover",
                    reviewed_by="/root/reviewer",
                    review=wrong_scope,
                ),
                node(
                    "thm:wrong-reviewer",
                    solution=solution,
                    checked_by="agent",
                    authored_by="/root/prover",
                    reviewed_by="/root/reviewer",
                    review=wrong_reviewer,
                ),
            ],
        )

        errors = "\n".join(self.check()["errors"])

        self.assertIn("thm:partial.review: report lacks an unqualified", errors)
        self.assertIn("thm:wrong-scope.review: report does not name", errors)
        self.assertIn("thm:wrong-reviewer.review: report does not name reviewed_by", errors)

    def test_every_proved_node_requires_a_solution_and_no_other_signal_bypasses(self):
        directional = self.add_artifact("directional-proof-substitute")
        self.add_ledger(
            "main",
            "ab",
            [
                node("thm:missing"),
                node("thm:narrative-only", proof_provenance="inline manuscript argument"),
                node(
                    "thm:numerics-only",
                    evidence="numerical-directional",
                    evidence_run=directional,
                    evidence_target="fixture",
                ),
            ],
            certify_fixture_proofs=False,
        )

        errors = "\n".join(self.check()["errors"])

        self.assertIn("thm:missing: proved node requires a certified solution", errors)
        self.assertIn(
            "thm:narrative-only: proved node requires a certified solution", errors
        )
        self.assertIn(
            "thm:numerics-only: proved node requires a certified solution", errors
        )
        self.assertNotIn("proof_provenance: must be", errors)

    def test_legacy_proof_exception_fields_are_forbidden(self):
        for field in ("legacy_r2_debt", "legacy_proved_without_solution"):
            with self.subTest(field=field):
                self.add_ledger(
                    "main",
                    "ab",
                    [node("thm:certified")],
                    meta_fields={field: {}},
                )

                errors = "\n".join(self.check()["errors"])

                self.assertIn(f"meta.{field}: legacy proof exceptions are forbidden", errors)

    def test_kls_defined_status_requires_definition_kind(self):
        self.add_ledger(
            "main",
            "kls",
            [
                node("def:valid", status="defined", kind="definition"),
                node("thm:not-a-definition", status="defined", kind="theorem"),
            ],
        )

        errors = "\n".join(self.check()["errors"])

        self.assertNotIn("def:valid", errors)
        self.assertIn(
            "thm:not-a-definition: status defined is only valid for kind definition",
            errors,
        )

    def test_proved_definition_requires_r2_unless_changed_to_defined(self):
        self.add_ledger(
            "main",
            "kls",
            [
                node("def:proved", kind="definition"),
                node("def:defined", status="defined", kind="definition"),
            ],
            certify_fixture_proofs=False,
        )

        errors = "\n".join(self.check()["errors"])

        self.assertIn("def:proved: proved node requires a certified solution", errors)
        self.assertNotIn("def:defined", errors)

    def test_route_policy_checks_vocabulary_default_and_explicit_routes(self):
        self.add_ledger(
            "main",
            "ab",
            [
                node("thm:default-route"),
                node("thm:allowed-route", route="shared"),
                node("thm:bad-route", route="unlisted"),
            ],
            meta_fields={
                "route_policy": {
                    "default": "eldan-localization",
                    "allowed": ["eldan-localization", "shared"],
                }
            },
        )

        errors = "\n".join(self.check()["errors"])

        self.assertNotIn("thm:allowed-route.route", errors)
        self.assertIn("thm:bad-route.route: 'unlisted' is not", errors)

        self.add_ledger(
            "main",
            "ab",
            [node("thm:bad-policy")],
            meta_fields={
                "route_policy": {
                    "default": "missing",
                    "allowed": ["shared", "shared", ""],
                }
            },
        )
        errors = "\n".join(self.check()["errors"])
        self.assertIn("route_policy.allowed: duplicate route 'shared'", errors)
        self.assertIn("route_policy.allowed: entries must be non-empty strings", errors)
        self.assertIn("route_policy.default: 'missing' is not in allowed", errors)

    def test_optional_proof_file_must_be_safe_existing_repo_relative_file(self):
        (self.root / "modules/proof.tex").write_text("fixture proof\n")
        self.add_ledger(
            "main",
            "ab",
            [
                node("thm:located", proof_file="modules/proof.tex"),
                node("thm:escaping", proof_file="../outside.tex"),
            ],
        )

        errors = "\n".join(self.check()["errors"])

        self.assertNotIn("thm:located.proof_file", errors)
        self.assertIn("thm:escaping.proof_file: path escapes repository root", errors)

    def test_solution_header_must_enumerate_shared_dossier_node(self):
        solution = self.add_solution(
            "shared-proof", node_ids=("thm:missing-from-header-extra",)
        )
        self.add_ledger(
            "main",
            "ab",
            [node("thm:missing-from-header", solution=solution, checked_by="human")],
        )

        errors = "\n".join(self.check()["errors"])

        self.assertIn("dossier header does not enumerate", errors)

    def test_clean_conditional_evidence_and_warning_contract_passes(self):
        clean = self.add_artifact("clean")
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
