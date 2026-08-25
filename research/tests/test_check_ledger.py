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
        self.module = modules / "test.tex"
        self.module.write_text("fixture\n")
        (self.root / "fi_references.bib").write_text(
            "@article{FixtureReference,\n"
            "  title = {Fixture reference},\n"
            "  year = {2026}\n"
            "}\n"
        )

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
        manuscript_labels = []
        for item in fixture_nodes:
            label = item.get("label", item.get("id"))
            if isinstance(label, str) and label.strip():
                manuscript_labels.append(label)
        if manuscript_labels:
            with self.module.open("a", encoding="utf-8") as stream:
                for label in manuscript_labels:
                    stream.write(f"\\label{{{label}}}\n")
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
                   node_ids: tuple[str, ...] = (), reviewer: str = "/root/reviewer",
                   authors: tuple[str, ...] = ("/root/prover",),
                   solutions: tuple[str, ...] = (), report_type: str = "proof-review",
                   body: str = "fixture review\n") -> str:
        relative = f"research/reviews/2026-08-25-{name}.md"
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        metadata = {"type": report_type, "date": "2026-08-25"}
        if report_type == "proof-review":
            metadata.update({
                "verdict": verdict,
                "authors": list(authors),
                "reviewer": reviewer,
                "nodes": list(node_ids),
                "solutions": list(solutions),
            })
        path.write_text(
            "---\n"
            + CHECKER.yaml.safe_dump(metadata, sort_keys=False)
            + "---\n\n"
            + body
        )
        return relative

    def check(self):
        return CHECKER.check_control_plane(self.research, self.root)


class CheckerHardeningTests(CheckerFixture):
    def test_program_is_never_inferred_from_ledger_directory(self):
        path = self.research / "kls" / "ledger.yaml"
        path.parent.mkdir(parents=True)
        path.write_text(CHECKER.yaml.safe_dump({"meta": {}, "nodes": []}))

        errors = "\n".join(self.check()["errors"])

        self.assertIn("meta.program must be a non-empty string", errors)
        self.assertIn("missing ledger for configured program 'kls'", errors)

    def test_production_configuration_rejects_legacy_or_extra_ledger_paths(self):
        self.add_ledger("legacy", "ab", [node("thm:legacy")])
        self.add_ledger("kls", "kls", [node("thm:kls")])

        report = CHECKER.check_control_plane(
            self.research,
            self.root,
            configured_ledgers={
                "ab": "research/a-series/ledger.yaml",
                "kls": "research/kls/ledger.yaml",
            },
        )
        errors = "\n".join(report["errors"])

        self.assertIn("configured ledger for 'ab' does not exist", errors)
        self.assertIn("unconfigured ledger; add an explicit production program path", errors)

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

    def test_navigation_and_duplicated_assumption_fields_are_obsolete(self):
        self.add_ledger(
            "main",
            "kls",
            [
                node("ass:x", status="open", kind="assumption"),
                node(
                    "thm:conditional",
                    status="conditional",
                    depends_on=["ass:x"],
                    assuming=["ass:x"],
                    related=["ass:x"],
                    entry_point=["ass:x"],
                    discharged_by=["ass:x"],
                ),
            ],
        )

        errors = "\n".join(self.check()["errors"])

        for field in ("assuming", "related", "entry_point", "discharged_by"):
            self.assertIn(f"thm:conditional.{field}: obsolete field", errors)

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

    def test_kind_records_mathematical_form_not_role_or_provenance(self):
        self.add_ledger(
            "main",
            "ab",
            [
                node("thm:baseline", status="open", kind="baseline"),
                node("thm:imported-kind", status="open", kind="imported"),
            ],
        )

        errors = "\n".join(self.check()["errors"])

        self.assertIn("thm:baseline: bad kind 'baseline'", errors)
        self.assertIn("thm:imported-kind: bad kind 'imported'", errors)

    def test_all_imports_require_explicit_class_and_known_bibtex_references(self):
        self.add_ledger(
            "main",
            "kls",
            [
                node(
                    "thm:import-good",
                    status="imported",
                    import_class="published",
                    references=["FixtureReference"],
                ),
                node("thm:import-missing", status="imported", references=[]),
                node(
                    "thm:import-unknown",
                    status="imported",
                    import_class="published",
                    references=["MissingReference"],
                ),
                node(
                    "thm:local-with-reference",
                    status="open",
                    references=["FixtureReference"],
                ),
            ],
        )

        errors = "\n".join(self.check()["errors"])

        self.assertNotIn("thm:import-good", errors)
        self.assertIn("thm:import-missing: imported node requires explicit import_class", errors)
        self.assertIn("thm:import-missing: imported node requires non-empty references", errors)
        self.assertIn(
            "thm:import-unknown.references: unknown BibTeX key 'MissingReference'",
            errors,
        )
        self.assertIn(
            "thm:local-with-reference: references is only valid with status imported",
            errors,
        )

    def test_ab_schema_rejects_unknown_retired_and_non_list_fields(self):
        ledger = self.add_ledger(
            "main",
            "ab",
            [
                node(
                    "q:schema",
                    status="open",
                    kind="question",
                    depends_on="thm:premise",
                    related=["thm:premise"],
                    evidence_eligible=True,
                    mystery="typo",
                ),
                node("thm:premise", status="open"),
            ],
            meta_fields={"mystery_meta": True},
        )
        document = CHECKER.yaml.safe_load(ledger.read_text())
        document["workflow"] = {}
        ledger.write_text(CHECKER.yaml.safe_dump(document, sort_keys=False))

        errors = "\n".join(self.check()["errors"])

        self.assertIn("q:schema.depends_on: must be a list", errors)
        self.assertIn("q:schema.related: obsolete field", errors)
        self.assertIn("q:schema.evidence_eligible: obsolete field", errors)
        self.assertIn("q:schema: unknown field 'mystery'", errors)
        self.assertIn("unknown top-level field 'workflow'", errors)
        self.assertIn("meta: unknown field 'mystery_meta'", errors)

    def test_declared_file_must_contain_effective_manuscript_label(self):
        other = self.root / "modules/other.tex"
        other.write_text("fixture without the anchor\n")
        self.add_ledger(
            "main",
            "ab",
            [
                node(
                    "obs:synthetic",
                    status="open",
                    kind="obstruction",
                    file="modules/other.tex",
                    label="thm:effective-anchor",
                ),
            ],
        )

        errors = "\n".join(self.check()["errors"])

        self.assertIn(
            "obs:synthetic.file: 'modules/other.tex' does not contain effective label "
            "'thm:effective-anchor'",
            errors,
        )

    def test_conditional_contract_is_derived_and_recursive_proved_risks_fail(self):
        nodes = [
            node("ass:x", status="open", kind="assumption"),
            node("thm:empty", status="conditional"),
            node(
                "thm:child",
                status="conditional",
                depends_on=["ass:x"],
            ),
            node(
                "thm:parent",
                status="conditional",
                depends_on=["thm:child"],
            ),
            node("heur:h", status="heuristic", kind="heuristic"),
            node(
                "thm:middle",
                status="imported",
                import_class="published",
                references=["FixtureReference"],
                depends_on=["heur:h"],
            ),
            node("thm:top", depends_on=["thm:middle"]),
            node("thm:direct", depends_on=["thm:child"]),
        ]
        self.add_ledger("main", "kls", nodes)

        errors = "\n".join(self.check()["errors"])

        self.assertIn(
            "thm:empty (conditional) must inherit an unresolved premise through depends_on",
            errors,
        )
        self.assertNotIn("thm:parent (conditional)", errors)
        self.assertIn("thm:top (proved) inherits unresolved heuristic 'heur:h'", errors)
        self.assertIn("thm:direct (proved) inherits unresolved conditional 'thm:child'", errors)
        self.assertIn("thm:direct (proved) inherits unresolved open 'ass:x'", errors)

    def test_unreviewed_preprint_is_an_inherited_assumption(self):
        nodes = [
            node(
                "thm:preprint",
                status="imported",
                import_class="preprint-unreviewed",
                references=["FixtureReference"],
            ),
            node(
                "thm:published",
                status="imported",
                import_class="published",
                references=["FixtureReference"],
            ),
            node(
                "thm:conditional",
                status="conditional",
                depends_on=["thm:preprint"],
            ),
            node("thm:middle", depends_on=["thm:preprint"]),
            node("thm:top", depends_on=["thm:middle"]),
            node("thm:published-use", depends_on=["thm:published"]),
        ]
        self.add_ledger("main", "kls", nodes)

        errors = "\n".join(self.check()["errors"])

        self.assertIn("thm:middle (proved) inherits unresolved preprint-unreviewed 'thm:preprint'", errors)
        self.assertIn("thm:top (proved) inherits unresolved preprint-unreviewed 'thm:preprint'", errors)
        self.assertNotIn("thm:conditional (conditional)", errors)
        self.assertNotIn("thm:published-use (proved) inherits", errors)

    def test_artifacts_are_validated_without_git_metadata(self):
        artifact = self.add_artifact("run")
        nodes = [
            node(
                "obs:history",
                kind="obstruction",
                evidence="numerical-directional",
                evidence_run=artifact,
                evidence_target="fixture",
            ),
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

    def test_bounded_by_is_the_only_reverse_map_and_warn_clearance_is_enforced(self):
        obstructions = {
            "mechanisms": ["direct-excess"],
            "obstructions": [{
                "id": "obs:warning",
                "forbids": [],
                "warns": ["direct-excess"],
                "constrains": ["thm:a"],
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

        self.assertIn("obs:warning: unknown field 'constrains'", errors)
        self.assertIn("warned about by obs:warning lacks a clearance note", errors)
        self.assertNotIn("reverse parity", errors)

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
            node_ids=("thm:agent-pass",),
            solutions=(solution,),
        )
        self_review = self.add_review(
            "agent-self-review-audit",
            node_ids=("thm:agent-self-review",),
            reviewer="/root/same",
            authors=("/root/same",),
            solutions=(solution,),
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
                review=self_review,
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
        self.assertIn("review 'research/reviews/missing.md': report does not exist", errors)

    def test_agent_certification_rejects_partial_or_out_of_scope_review(self):
        solution = self.add_solution(
            "agent-proof",
            node_ids=("thm:partial", "thm:wrong-scope", "thm:wrong-reviewer"),
        )
        partial = self.add_review(
            "partial-audit",
            verdict="changes-requested",
            node_ids=("thm:partial",),
            solutions=(solution,),
        )
        wrong_scope = self.add_review(
            "wrong-scope-audit",
            node_ids=("thm:wrong-scope-extra",),
            solutions=(solution,),
            body="## Explicit exclusions\n\nThis report does not certify `thm:wrong-scope`.\n",
        )
        wrong_reviewer = self.add_review(
            "wrong-reviewer-audit",
            node_ids=("thm:wrong-reviewer",),
            reviewer="/root/reviewer-extra",
            solutions=(solution,),
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

        self.assertIn("partial-audit.md.verdict: a proof-review must have", errors)
        self.assertIn("wrong-scope-audit.md'.nodes: exact ledger parity mismatch", errors)
        self.assertIn("wrong-reviewer-audit.md'.reviewer: exact ledger parity mismatch", errors)

    def test_agent_review_rejects_wrong_author_solution_and_unwired_scope(self):
        solution = self.add_solution("agent-proof", node_ids=("thm:contract",))
        review = self.add_review(
            "wrong-contract-audit",
            node_ids=("thm:contract", "thm:unwired"),
            authors=("/root/not-the-author",),
            solutions=("solutions/not-the-dossier.tex",),
        )
        self.add_ledger(
            "main",
            "ab",
            [node(
                "thm:contract",
                solution=solution,
                checked_by="agent",
                authored_by="/root/prover",
                reviewed_by="/root/reviewer",
                review=review,
            )],
        )

        errors = "\n".join(self.check()["errors"])

        self.assertIn("wrong-contract-audit.md'.nodes: exact ledger parity mismatch", errors)
        self.assertIn("wrong-contract-audit.md'.authors: exact ledger parity mismatch", errors)
        self.assertIn("wrong-contract-audit.md'.solutions: exact ledger parity mismatch", errors)

    def test_audit_pass_prose_cannot_certify_and_review_path_is_confined(self):
        solution = self.add_solution(
            "agent-proof",
            node_ids=("thm:audit", "thm:outside"),
        )
        audit = self.add_review(
            "non-certifying-audit",
            report_type="audit",
            body="- **Verdict:** pass for `thm:audit` by `/root/reviewer`\n",
        )
        outside = "docs/outside-review.md"
        outside_path = self.root / outside
        outside_path.parent.mkdir(parents=True)
        outside_path.write_text(
            "---\n"
            "type: proof-review\n"
            "date: '2026-08-25'\n"
            "verdict: pass\n"
            "authors: [/root/prover]\n"
            "reviewer: /root/reviewer\n"
            "nodes: [thm:outside]\n"
            f"solutions: [{solution}]\n"
            "---\n"
        )
        self.add_ledger(
            "main",
            "ab",
            [
                node(
                    "thm:audit",
                    solution=solution,
                    checked_by="agent",
                    authored_by="/root/prover",
                    reviewed_by="/root/reviewer",
                    review=audit,
                ),
                node(
                    "thm:outside",
                    solution=solution,
                    checked_by="agent",
                    authored_by="/root/prover",
                    reviewed_by="/root/reviewer",
                    review=outside,
                ),
            ],
        )

        errors = "\n".join(self.check()["errors"])

        self.assertIn("type 'audit' cannot certify a proof", errors)
        self.assertIn("agent review reports must be under research/reviews/", errors)

    def test_review_archive_rejects_orphaned_proof_review_and_missing_front_matter(self):
        self.add_review(
            "orphaned-proof-review",
            node_ids=("thm:orphan",),
            solutions=("solutions/orphan.tex",),
        )
        malformed = self.root / "research/reviews/2026-08-25-malformed-audit.md"
        malformed.write_text("# Missing front matter\n")
        self.add_ledger("main", "ab", [node("thm:fixture")])

        errors = "\n".join(self.check()["errors"])

        self.assertIn("orphaned-proof-review.md': proof-review is not referenced", errors)
        self.assertIn("malformed-audit.md: review report must start with YAML front matter", errors)

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
        self.assertIn(
            "thm:narrative-only.proof_provenance: obsolete field",
            errors,
        )

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

    def test_route_policy_requires_explicit_routes_and_checks_vocabulary(self):
        self.add_ledger(
            "main",
            "kls",
            [
                node("thm:default-route"),
                node("thm:allowed-route", route="shared"),
                node("thm:bad-route", route="unlisted"),
            ],
            meta_fields={
                "route_policy": {
                    "allowed": ["eldan-localization", "shared"],
                }
            },
        )

        errors = "\n".join(self.check()["errors"])

        self.assertIn("thm:default-route.route: required", errors)
        self.assertNotIn("thm:allowed-route.route", errors)
        self.assertIn("thm:bad-route.route: 'unlisted' is not", errors)

        self.add_ledger(
            "main",
            "kls",
            [node("thm:bad-policy", route="shared")],
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
        self.assertIn("route_policy: unknown field 'default'", errors)

    def test_legacy_proof_fields_are_rejected(self):
        self.add_ledger(
            "main",
            "ab",
            [
                node("thm:proof-file", proof_file="modules/test.tex"),
                node("thm:narrative", proof_provenance="inline proof"),
            ],
        )

        errors = "\n".join(self.check()["errors"])

        self.assertIn("thm:proof-file.proof_file: obsolete field; use solution", errors)
        self.assertIn(
            "thm:narrative.proof_provenance: obsolete field; use solution plus checked_by",
            errors,
        )

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
            }],
        }
        nodes = [
            node("ass:x", status="open", kind="assumption"),
            node(
                "thm:conditional",
                status="conditional",
                depends_on=["ass:x"],
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
        self.add_ledger("a-series", "ab", [malformed])
        self.add_ledger("kls", "kls", [])
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
