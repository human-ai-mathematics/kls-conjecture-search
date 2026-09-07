"""The published site: a derived view, and nothing else.

``scripts/site.py`` has no lane in ``check.py`` and cannot have one — the checker
validates repository state, and a built site is a build artifact under ``build/``. This
file is therefore the only thing standing between the exporter and the failure mode the
whole design exists to avoid:

    a beautiful second source of truth.

So the tests below are mostly about *boundaries* rather than about rendering. That the
frontend holds no mathematics, that the two modes of certification are not presented as
equal evidence, that a candidate is never dressed as a claim, that supersession is
applied, and that an invalid revision is never published at all.

    python3 -m unittest discover -s scripts/tests -p 'test_*.py'
"""
from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from checks import ledger  # noqa: E402
from fixtures import REPO, CheckerFixture, node  # noqa: E402

# Loaded by path rather than by name. `import site` would return the standard library's
# module, which the interpreter imports at startup and caches long before scripts/ is on
# sys.path — so the name is taken, and the collision would be silent rather than loud.
_spec = importlib.util.spec_from_file_location("harness_site", REPO / "scripts/site.py")
site_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(site_module)

#: ``id:`` values anywhere in a document, plus the keys of a mapping of them. Blunt on
#: purpose: this is used to prove an *absence*, so over-collecting is the safe direction.
def _identifiers(value: object):
    if isinstance(value, dict):
        for key, item in value.items():
            if isinstance(key, str) and ":" in key:
                yield key
            if key == "id" and isinstance(item, str) and ":" in item:
                yield item
            yield from _identifiers(item)
    elif isinstance(value, list):
        for item in value:
            if isinstance(item, str) and ":" in item and " " not in item:
                yield item
            yield from _identifiers(item)


EXAMPLE = REPO / "example"
FRONTEND = REPO / "site"
PAGES_WORKFLOW = REPO / ".github/workflows/pages.yml"
CHECK_WORKFLOW = REPO / ".github/workflows/check.yml"


class SiteFixture(CheckerFixture):
    """A fixture tree plus a throwaway output directory."""

    def setUp(self):
        super().setUp()
        self.out = self.root / "build/site"

    def publish(self, **kwargs):
        return site_module.build(self.root, self.out, **kwargs)

    def data(self, **kwargs) -> dict:
        data, errors = self.publish(**kwargs)
        self.assertEqual(errors, [], "fixture was expected to validate")
        return data


class RefusesInvalidRevisions(SiteFixture):
    """A structurally invalid revision is not this repository's research state."""

    def test_a_red_repository_is_not_published(self):
        self.add_ledger("program", "test", [node("thm:a", depends_on=["thm:missing"])])

        data, errors = self.publish()

        self.assertTrue(errors)
        self.assertEqual(data, {})

    def test_a_refusal_writes_nothing_at_all(self):
        """Not even a stale shell. A half-written site is worse than no site."""
        self.add_ledger("program", "test", [node("thm:a", depends_on=["thm:missing"])])

        self.publish()

        self.assertFalse(self.out.exists())

    def test_an_uninstantiated_template_is_published_and_says_so(self):
        """A fresh clone is correct and not ready; refusing it would make that red."""
        self.add_ledger("program", "program", [])

        data = self.data()

        self.assertFalse(data["program"]["instantiated"])
        self.assertEqual(data["claims"], {})
        self.assertIsNone(data["search"])


class ClaimExport(SiteFixture):
    def test_both_directions_of_a_relation_are_derived(self):
        self.add_ledger("program", "test", [
            node("lem:base"),
            node("thm:top", depends_on=["lem:base"]),
        ])

        claims = self.data()["claims"]

        self.assertEqual(claims["thm:top"]["edges"]["depends_on"], ["lem:base"])
        self.assertEqual(claims["lem:base"]["reverse"]["used_by"], ["thm:top"])

    def test_the_one_line_summary_is_exported_as_a_gloss(self):
        """`summary` is a gloss, not the statement (research/program/ledger-schema.md).

        The field is renamed on the way out so that no view can present it as canonical
        by accident, and the anchor travels with it so a reader can reach the real text.
        The statement is exported *beside* it and never merged into it: the two are
        different things, and a page that showed one under the other's name would be
        making a claim about the manuscript that the manuscript did not make.
        """
        self.add_ledger("program", "test", [node("thm:a")])

        claim = self.data()["claims"]["thm:a"]

        self.assertIn("gloss", claim)
        # Whatever the fixture writes, verbatim: node() deliberately keeps the address
        # out of its gloss, because the bare-id prose rule is enforced for summaries.
        self.assertEqual(claim["gloss"], node("thm:a")["summary"])
        self.assertNotIn(claim["gloss"], json.dumps(claim["statement"]))
        self.assertEqual(claim["source"]["file"], "modules/test.tex")
        self.assertIsInstance(claim["source"]["line"], int)

    def test_hard_and_advisory_fences_are_different_classes(self):
        """A proved obstruction fences; an open one advises. Drawing them alike lies."""
        self.add_ledger("program", "test", [
            node("obs:hard", kind="obstruction"),
            node("obs:soft", kind="obstruction", status="open"),
            node("thm:a", bounded_by=["obs:hard"], heuristic_barriers=["obs:soft"]),
        ])

        data = self.data()
        classes = {relation["field"]: relation["class"]
                   for relation in data["vocabulary"]["relations"]}

        self.assertEqual(classes["bounded_by"], "hard-fence")
        self.assertEqual(classes["heuristic_barriers"], "soft-fence")
        self.assertNotEqual(classes["assumes"], classes["depends_on"])
        claim = data["claims"]["thm:a"]
        self.assertEqual(claim["edges"]["bounded_by"], ["obs:hard"])
        self.assertEqual(claim["edges"]["heuristic_barriers"], ["obs:soft"])

    def test_an_applicability_blocked_proof_is_marked_without_losing_its_status(self):
        self.add_ledger("program", "test", [
            node("asm:open", status="open", kind="assumption"),
            node("thm:conditional", assumes=["asm:open"]),
        ])

        claim = self.data()["claims"]["thm:conditional"]

        self.assertEqual(claim["status"], "proved")
        self.assertEqual(claim["applicability_blocked_by"], ["asm:open"])

    def test_a_refuter_is_not_a_dependency_of_what_it_refutes(self):
        self.add_ledger("program", "test", [
            node("prop:refuter"),
            node("conj:target", status="refuted", kind="conjecture",
                 refuted_by=["prop:refuter"]),
        ])

        claims = self.data()["claims"]

        self.assertEqual(claims["conj:target"]["edges"]["depends_on"], [])
        self.assertEqual(claims["conj:target"]["edges"]["refuted_by"], ["prop:refuter"])
        self.assertEqual(claims["prop:refuter"]["reverse"]["refutes"], ["conj:target"])


class ReaderFacingProjections(SiteFixture):
    """Titles, standings and the guide: what the frontend is allowed to render."""

    def test_the_manuscript_title_is_exported_as_the_claim_s_name(self):
        """The heading a mathematician reads, taken from the claim's own environment."""
        self.add_ledger("program", "test", [node("thm:a")])
        # Rewritten after add_ledger, which plants an untitled anchor of its own; two
        # would be a duplicate label, which the core lane correctly refuses.
        self.module.write_text(
            "\\begin{theorem}[All-cut Carleson implies KLS]\n"
            "\\label{thm:a}\nfixture\n\\end{theorem}\n")

        claim = self.data()["claims"]["thm:a"]

        self.assertEqual(claim["title"], "All-cut Carleson implies KLS")
        self.assertEqual(claim["id"], "thm:a", "the identifier is demoted, never dropped")

    def test_a_claim_without_a_title_exports_null_rather_than_its_id(self):
        """The fallback belongs to the frontend, which knows it is falling back."""
        self.add_ledger("program", "test", [node("thm:a")])

        self.assertIsNone(self.data()["claims"]["thm:a"]["title"])

    def test_the_standing_is_exported_beside_the_schema_status(self):
        """Both, not one. The badge shows the standing; the status stays auditable."""
        self.add_ledger("program", "test", [
            node("thm:published", status="proved", provenance="literature",
                 import_class="published", references=["FixtureReference"]),
        ], certify_fixture_proofs=False)

        claim = self.data()["claims"]["thm:published"]

        self.assertEqual(claim["status"], "proved")
        self.assertEqual(claim["standing"], "Published result")
        self.assertEqual(claim["standing_tone"], "published")
        self.assertFalse(claim["standing_conditional"])

    def test_a_literature_import_is_never_labelled_certified_here(self):
        """The homepage used to say every proved node had a certified dossier. Ten did not."""
        self.add_ledger("program", "test", [
            node("thm:import", status="proved", provenance="literature",
                 import_class="published", references=["FixtureReference"]),
        ], certify_fixture_proofs=False)

        claim = self.data()["claims"]["thm:import"]

        self.assertEqual(claim["proofs"], [])
        self.assertNotEqual(claim["standing_tone"], "certified")

    def test_a_conditional_result_keeps_its_status_and_says_it_is_conditional(self):
        self.add_ledger("program", "test", [
            node("asm:open", status="open", kind="assumption"),
            node("thm:conditional", assumes=["asm:open"]),
        ])

        claim = self.data()["claims"]["thm:conditional"]

        self.assertEqual(claim["status"], "proved")
        self.assertTrue(claim["standing_conditional"])
        self.assertIn("conditional", claim["standing"])

    def test_a_tree_with_no_guide_exports_null_and_still_publishes(self):
        """Every Explore view degrades to the audit views it indexes."""
        self.add_ledger("program", "test", [node("thm:a")])

        self.assertIsNone(self.data()["guide"])

    def test_a_guide_reaches_the_frontend_through_data_json(self):
        """The one route by which route names and featured ids may reach site.js."""
        self.add_ledger("program", "test", [
            node("conj:target", status="open", kind="conjecture"),
            *(node(f"thm:{letter}") for letter in "abcdef"),
        ])
        self.add_portfolio({
            "target": "conj:target",
            "families": [{"id": "fam:one", "mechanism": "m", "state": "active"}],
            "approaches": [{"id": "ap:one", "family": "fam:one", "objective": "o",
                            "state": "active"}],
        })
        (self.research / "program/editorial.yaml").write_text(
            "site:\n  name: Test programme\n"
            "routes:\n"
            "  - code: E\n    name: One mechanism\n"
            "    families: [fam:one]\n    anchor: conj:target\n"
            "featured:\n"
            + "".join(f"  - {{id: thm:{letter}, role: advance}}\n"
                      for letter in "abcdef")
        )

        guide = self.data()["guide"]

        self.assertEqual(guide["site"]["name"], "Test programme")
        self.assertEqual(guide["routes"][0]["code"], "E")
        self.assertEqual(len(guide["featured"]), 6)

    def test_a_guide_that_does_not_validate_is_not_published_at_all(self):
        """It is checked in the editorial lane, so site.py refuses the whole revision."""
        self.add_ledger("program", "test", [node("thm:a")])
        (self.research / "program/editorial.yaml").write_text(
            "featured:\n  - {id: thm:ghost, role: bridge}\n")

        data, errors = self.publish()

        self.assertTrue(any("thm:ghost" in error for error in errors))
        self.assertEqual(data, {})


class CertificationIsNotFlattened(SiteFixture):
    """The two proof modes are not equally evidenced, and the export says which is which."""

    def test_an_agent_certification_carries_its_persisted_review(self):
        solution = self.add_solution("thm-a", node_ids=("thm:a",))
        review = self.add_review("a-review", node_ids=("thm:a",), solutions=(solution,))
        self.add_ledger("program", "test", [
            node("thm:a", proofs=[{"artifact": solution, "mode": "agent", "review": review}]),
        ], certify_fixture_proofs=False)

        proof = self.data()["claims"]["thm:a"]["proofs"][0]

        self.assertEqual(proof["evidence"], "persisted-review")
        self.assertEqual(proof["review_detail"]["verdict"], "pass")
        self.assertEqual(proof["review_detail"]["reviewer"], "/root/reviewer")
        self.assertEqual(proof["review_detail"]["authors"], ["/root/researcher"])

    def test_a_human_acceptance_is_marked_an_attestation(self):
        """It carries a name and no artifact. That is honest, and honestly weaker."""
        self.add_ledger("program", "test", [node("thm:a")])  # fixture writes mode: human

        proof = self.data()["claims"]["thm:a"]["proofs"][0]

        self.assertEqual(proof["mode"], "human")
        self.assertEqual(proof["evidence"], "attestation")
        self.assertNotIn("review_detail", proof)


class SearchStateStaysSearchState(SiteFixture):
    def test_a_route_carries_no_status_and_no_statement(self):
        self.add_ledger("program", "test", [node("conj:target", kind="conjecture",
                                                 status="open")])
        self.add_portfolio({
            "target": "conj:target",
            "families": [{"id": "fam:one", "mechanism": "try it", "state": "active"}],
            "approaches": [{"id": "ap:one", "family": "fam:one", "state": "active"}],
        })

        route = self.data()["search"]["routes"]["ap:one"]

        self.assertNotIn("status", route)
        self.assertNotIn("gloss", route)
        self.assertIn("objective", route)

    def test_what_a_route_is_blocked_on_is_named_from_the_claim_side_too(self):
        """The portfolio names a blocker and never restates it, so the join is derived."""
        self.add_ledger("program", "test", [
            node("conj:target", kind="conjecture", status="open"),
            node("lem:blocker", status="open", kind="lemma"),
        ])
        self.add_portfolio({
            "target": "conj:target",
            "families": [{"id": "fam:one", "mechanism": "try it", "state": "active"}],
            "approaches": [{
                "id": "ap:one", "family": "fam:one", "state": "blocked",
                "blocker": "lem:blocker", "reopen_if": "someone proves it",
                "checkpoints": [self.add_checkpoint("stuck", approach="ap:one")],
            }],
        })

        data = self.data()

        self.assertEqual(data["claims"]["lem:blocker"]["blocks_routes"], ["ap:one"])
        self.assertEqual(data["search"]["routes"]["ap:one"]["blocker"], "lem:blocker")

    def test_route_ancestry_is_derived_rather_than_stored(self):
        self.add_ledger("program", "test", [node("conj:target", kind="conjecture",
                                                 status="open")])
        self.add_portfolio({
            "target": "conj:target",
            "families": [{"id": "fam:one", "mechanism": "try it", "state": "active"}],
            "approaches": [
                {"id": "ap:parent", "family": "fam:one", "state": "active"},
                {"id": "ap:child", "family": "fam:one", "state": "active",
                 "parent": "ap:parent"},
            ],
        })

        routes = self.data()["search"]["routes"]

        self.assertEqual(routes["ap:parent"]["children"], ["ap:child"])


class DurableMemory(SiteFixture):
    def test_a_candidate_is_exported_with_its_canonical_statement(self):
        """The asymmetry with a node's gloss is the point: nothing else holds this text."""
        self.add_ledger("program", "test", [node("thm:a")])
        source = self.add_checkpoint("found", outcome="candidate", candidates=(
            {"id": "cand:x", "statement": "A precise statement."},
        ))

        candidates = self.data()["memory"]["candidates"]

        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0]["statement"], "A precise statement.")
        self.assertEqual(candidates[0]["source"], source)

    def test_a_promoted_candidate_is_no_longer_live(self):
        self.add_ledger("program", "test", [node("thm:a"), node("lem:x")])
        self.add_checkpoint("propose", date="2026-08-26", outcome="candidate", candidates=(
            {"id": "cand:x", "statement": "A precise statement."},
        ))
        self.add_checkpoint("promote", date="2026-08-27", outcome="proposed",
                            nodes=("lem:x",),
                            promotes=({"candidate": "cand:x", "node": "lem:x"},))

        memory = self.data()["memory"]

        self.assertEqual(memory["candidates"], [])
        self.assertEqual(memory["promoted"]["cand:x"]["node"], "lem:x")

    def test_a_superseded_checkpoint_names_its_heir(self):
        """An append-only archive keeps provenance; naming the heir supplies a reading."""
        self.add_ledger("program", "test", [node("thm:a")])
        old = self.add_checkpoint("old", date="2026-08-26", nodes=("thm:a",))
        self.add_checkpoint("new", date="2026-08-27", nodes=("thm:a",), supersedes=(old,))

        records = {record["path"]: record for record in self.data()["memory"]["checkpoints"]}

        self.assertEqual(records[old]["superseded_by"],
                         ["research/explorations/2026-08-27-new.md"])

    def test_a_run_artifact_is_exported_without_being_attached_to_a_status(self):
        self.add_ledger("program", "test", [node("thm:a")])
        self.add_run("2026-08-26T000000.000000Z-fixture.jsonl", target="fixture")

        runs = self.data()["memory"]["runs"]

        self.assertEqual(len(runs), 1)
        self.assertEqual(runs[0]["target"], "fixture")
        self.assertNotIn("certifies", json.dumps(runs))


class StatementExtraction(unittest.TestCase):
    """Slicing the claim out of the manuscript, which is what makes a claim page useful.

    A build-time projection of the canonical source, exactly as the gloss is — not a
    second home for the statement (CLAUDE.md constraint 7). The bytes come out of
    ``modules/`` on every build and are checked back against it before anything is
    published.
    """

    def spans(self, source: str, label: str = "thm:a") -> tuple[int, int]:
        return ledger.claim_bodies(source)[label]

    def body(self, source: str, label: str = "thm:a") -> str:
        start, end = self.spans(source, label)
        return source[start:end]

    def test_the_body_starts_after_the_title_and_stops_at_the_end(self):
        source = ("prose before\n\\begin{theorem}[A named claim]\n\\label{thm:a}\n"
                  "The statement.\n\\end{theorem}\nprose after\n")

        self.assertEqual(self.body(source), "\n\\label{thm:a}\nThe statement.\n")

    def test_an_untitled_claim_still_yields_its_body(self):
        source = "\\begin{lemma}\\label{thm:a}Bare.\\end{lemma}"

        self.assertEqual(self.body(source), "\\label{thm:a}Bare.")

    def test_a_nested_environment_does_not_end_the_claim(self):
        source = ("\\begin{theorem}\n\\label{thm:a}\nBefore.\n"
                  "\\begin{enumerate}\\item one\\end{enumerate}\nAfter.\n\\end{theorem}")

        self.assertIn("After.", self.body(source))

    def test_a_structural_label_has_no_statement(self):
        """A section anchor states nothing, and must not be handed one."""
        self.assertEqual(ledger.claim_bodies("\\section{S}\\label{sec:a}"), {})

    def test_an_equation_label_inside_a_claim_states_nothing_of_its_own(self):
        """The equation names itself; the theorem around it is what holds a statement."""
        source = ("\\begin{theorem}\\label{thm:a}\n"
                  "\\begin{equation}\\label{eq:a}x=1\\end{equation}\n\\end{theorem}")

        self.assertEqual(sorted(ledger.claim_bodies(source)), ["thm:a"])
        self.assertIn("x=1", self.body(source))

    def test_a_commented_out_claim_is_not_sliced_into_a_live_one(self):
        """`strip_comments` preserves offsets, so slicing the original stays exact."""
        source = ("% \\begin{theorem}\n\\begin{theorem}\\label{thm:a}Live."
                  "\\end{theorem}\n")
        stripped = ledger.strip_comments(source)
        start, end = ledger.claim_bodies(stripped)["thm:a"]

        self.assertEqual(source[start:end], "\\label{thm:a}Live.")

    def test_the_statement_travels_with_the_label_from_disk(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "modules").mkdir()
            (root / "modules/one.tex").write_text(
                "\\begin{theorem}[Named]\n\\label{thm:a}\\klsstatus{thm:a}\n"
                "If $x>0$ then $x^2>0$.\n\\end{theorem}\n", encoding="utf-8")

            labels = ledger.manuscript_labels(root)

        self.assertIn("If $x>0$ then $x^2>0$.", labels["thm:a"]["statement"])
        self.assertEqual(labels["thm:a"]["statement_line"], 1)
        self.assertNotIn("Named", labels["thm:a"]["statement"])


class StatementRendering(unittest.TestCase):
    """The LaTeX subset the manuscript's 138 statements actually use, and no more."""

    def blocks(self, source: str, **kwargs) -> list[dict]:
        return site_module.Prose(**kwargs).statement(source)

    def kinds(self, source: str, **kwargs) -> list[str]:
        return [block["type"] for block in self.blocks(source, **kwargs)]

    def text(self, blocks: list[dict]) -> str:
        return json.dumps(blocks, ensure_ascii=False)

    def test_the_anchor_and_the_standing_badge_are_dropped(self):
        """Both are already on the page in their own right; printing them again is noise."""
        blocks = self.blocks("\\label{thm:a}\\klsstatus{thm:a}\nA claim.\n")

        self.assertEqual(self.text(blocks).count("thm:a"), 0)
        self.assertIn("A claim.", self.text(blocks))

    def test_display_mathematics_is_normalized_to_what_the_page_declares(self):
        """index.html declares `$$…$$` and nothing else."""
        blocks = self.blocks("Before.\n\\[\n  x=1\n\\]\nAfter.\n")

        self.assertEqual([block["type"] for block in blocks],
                         ["paragraph", "math", "paragraph"])
        self.assertEqual(blocks[1]["tex"], "$$x=1$$")

    def test_an_equation_environment_becomes_display_mathematics(self):
        blocks = self.blocks("\\begin{equation}\\label{eq:a}x=1\\end{equation}")

        self.assertEqual(blocks[0]["tex"], "$$x=1$$")

    def test_an_align_environment_keeps_its_alignment(self):
        blocks = self.blocks("\\begin{align}a&=b\\\\c&=d\\end{align}")

        self.assertTrue(blocks[0]["tex"].startswith("$$\\begin{aligned}"))

    def test_inline_mathematics_is_carried_verbatim(self):
        """MathJax may never load. The source has to be readable when it does not."""
        spans = self.blocks("Let $\\mu$ be log-concave.")[0]["spans"]

        self.assertIn({"t": "math", "v": "$\\mu$"}, spans)

    def test_a_list_becomes_a_list(self):
        blocks = self.blocks("\\begin{enumerate}[label=(\\roman*)]\n"
                             "\\item first\n\\item second\n\\end{enumerate}")

        self.assertEqual(blocks[0]["type"], "list")
        self.assertTrue(blocks[0]["ordered"])
        self.assertEqual(len(blocks[0]["items"]), 2)

    def test_a_cross_reference_is_kept_as_an_address(self):
        spans = self.blocks("See Theorem~\\ref{thm:b}.")[0]["spans"]

        self.assertIn({"t": "ref", "v": "thm:b"}, spans)

    def test_a_citation_survives_its_optional_argument(self):
        spans = self.blocks("As in \\cite[Thm.~1.2]{Letwin2026}.")[0]["spans"]

        self.assertIn({"t": "cite", "v": "Letwin2026"}, spans)

    def test_text_mode_markup_becomes_markup(self):
        spans = self.blocks("\\emph{any fixed} cut")[0]["spans"]

        self.assertEqual(spans[0]["t"], "em")

    def test_latex_spellings_become_the_characters_they_stand_for(self):
        spans = self.blocks("Poincar\\'e--Wirtinger, 100\\% of it.")[0]["spans"]

        self.assertIn("Poincaré–Wirtinger, 100% of it.", self.text(spans))

    def test_an_identifier_in_a_statement_is_linked(self):
        """Issue 18's site half: an id in derived prose is navigation, not a token."""
        spans = self.blocks("Consequently def:qcts holds.",
                            ids={"def:qcts"})[0]["spans"]

        self.assertIn({"t": "id", "v": "def:qcts"}, spans)


class StatementFreshness(SiteFixture):
    """A copy of the manuscript is honest only while it is known to agree with it."""

    def claims(self) -> dict:
        self.add_ledger("program", "test", [node("thm:a")])
        return self.data()["claims"]

    def test_a_statement_is_exported_and_digested(self):
        claim = self.claims()["thm:a"]

        self.assertTrue(claim["statement"]["blocks"])
        self.assertEqual(len(claim["statement"]["sha256"]), 64)

    def test_a_copy_that_no_longer_matches_the_manuscript_is_caught(self):
        claims = self.claims()
        claims["thm:a"]["statement"]["sha256"] = "0" * 64

        errors = site_module.statement_failures(self.root, claims)

        self.assertEqual(len(errors), 1)
        self.assertIn("does not match", errors[0])

    def test_a_claim_whose_anchor_yields_nothing_is_caught(self):
        claims = self.claims()
        claims["thm:a"]["statement"] = None

        errors = site_module.statement_failures(self.root, claims)

        self.assertEqual(len(errors), 1)
        self.assertIn("no statement", errors[0])

    def test_a_structural_anchor_is_not_asked_for_a_statement(self):
        claims = self.claims()
        claims["thm:a"]["source"]["environment"] = None
        claims["thm:a"]["statement"] = None

        self.assertEqual(site_module.statement_failures(self.root, claims), [])

    def test_a_stale_copy_refuses_the_whole_build(self):
        """Publishing a wrong statement under a label saying it is the manuscript's is
        worse than publishing none, so it is a build failure and nothing is written."""
        self.add_ledger("program", "test", [node("thm:a")])
        original = site_module.statement_failures
        site_module.statement_failures = lambda root, claims: ["fixture staleness"]
        try:
            data, errors = self.publish()
        finally:
            site_module.statement_failures = original

        self.assertEqual(errors, ["fixture staleness"])
        self.assertEqual(data, {})
        self.assertFalse(self.out.exists())


class MarkdownRendering(unittest.TestCase):
    """The Markdown subset the 92 durable records actually use, counted rather than
    guessed: headings, paragraphs, `$$` display mathematics, lists, tables, fenced code,
    block quotes, rules, and inline code, mathematics, emphasis and links."""

    def blocks(self, source: str, **kwargs) -> list[dict]:
        return site_module.Prose(**kwargs).markdown(source)

    def kinds(self, source: str, **kwargs) -> list[str]:
        return [block["type"] for block in self.blocks(source, **kwargs)]

    def test_headings_paragraphs_and_rules(self):
        self.assertEqual(self.kinds("# Title\n\ntext\n\n---\n"),
                         ["heading", "paragraph", "rule"])

    def test_a_paragraph_joins_its_wrapped_lines(self):
        spans = self.blocks("one\ntwo\n")[0]["spans"]

        self.assertEqual(spans[0]["v"], "one two")

    def test_display_mathematics_on_its_own_lines(self):
        blocks = self.blocks("before\n\n$$\n\\Var(X)\\le 1\n$$\n\nafter\n")

        self.assertEqual([block["type"] for block in blocks],
                         ["paragraph", "math", "paragraph"])
        self.assertEqual(blocks[1]["tex"], "$$\\Var(X)\\le 1$$")

    def test_a_fenced_code_block_keeps_its_language_and_its_text(self):
        block = self.blocks("```yaml\n- id: x\n  kind: y\n```\n")[0]

        self.assertEqual(block["type"], "code")
        self.assertEqual(block["language"], "yaml")
        self.assertEqual(block["text"], "- id: x\n  kind: y")

    def test_a_list_inside_a_fence_is_code_and_not_a_list(self):
        self.assertEqual(self.kinds("```\n- not a list\n```\n"), ["code"])

    def test_nested_lists(self):
        block = self.blocks("- outer\n  - inner\n- second\n")[0]

        self.assertEqual(block["type"], "list")
        self.assertFalse(block["ordered"])
        self.assertEqual(len(block["items"]), 2)
        self.assertEqual([inner["type"] for inner in block["items"][0]],
                         ["paragraph", "list"])

    def test_an_ordered_list_is_ordered(self):
        block = self.blocks("1. first\n2. second\n")[0]

        self.assertTrue(block["ordered"])

    def test_a_table_keeps_its_header_and_its_alignment(self):
        block = self.blocks("| a | b |\n|---|:-:|\n| 1 | 2 |\n")[0]

        self.assertEqual(block["type"], "table")
        self.assertEqual(block["align"], [None, "center"])
        self.assertEqual(len(block["rows"]), 1)

    def test_a_block_quote_holds_blocks(self):
        block = self.blocks("> quoted\n")[0]

        self.assertEqual(block["type"], "quote")
        self.assertEqual(block["blocks"][0]["type"], "paragraph")

    def test_inline_code_mathematics_and_emphasis(self):
        spans = self.blocks("`code`, $x$, **bold**, *italic*.\n")[0]["spans"]
        kinds = [span["t"] for span in spans]

        self.assertEqual(kinds[:1], ["code"])
        self.assertIn("math", kinds)
        self.assertIn("strong", kinds)
        self.assertIn("em", kinds)

    def test_an_underscore_inside_mathematics_is_not_emphasis(self):
        """One left-to-right pass, so nothing is matched across a token."""
        spans = self.blocks("$x_1$ and $y_2$\n")[0]["spans"]

        self.assertEqual([span["t"] for span in spans], ["math", "text", "math"])

    def test_a_repository_identifier_is_linked_wherever_it_is_written(self):
        spans = self.blocks("`q:upgrade` blocks q:upgrade.\n",
                            ids={"q:upgrade"})[0]["spans"]

        self.assertEqual([span for span in spans if span["t"] == "id"],
                         [{"t": "id", "v": "q:upgrade"}] * 2)

    def test_an_identifier_that_resolves_to_nothing_is_left_alone(self):
        spans = self.blocks("`q:upgrade` here.\n")[0]["spans"]

        self.assertEqual(spans[0], {"t": "code", "v": "q:upgrade"})

    def test_a_link_to_another_record_becomes_navigation(self):
        spans = self.blocks(
            "see [that](2026-08-20-other.md)\n",
            records={"research/explorations/2026-08-20-other.md": "2026-08-20-other"},
        )[0]["spans"]
        link = [span for span in spans if span["t"] == "link"][0]

        self.assertEqual(link["record"], "2026-08-20-other")

    def test_a_link_to_a_repository_file_becomes_a_source_link(self):
        spans = self.blocks("see [a run](../runs/x.jsonl)\n")[0]["spans"]
        link = [span for span in spans if span["t"] == "link"][0]

        self.assertEqual(link["path"], "research/runs/x.jsonl")

    def test_an_external_link_stays_external(self):
        spans = self.blocks("see [it](https://arxiv.org/abs/1)\n")[0]["spans"]
        link = [span for span in spans if span["t"] == "link"][0]

        self.assertEqual(link["href"], "https://arxiv.org/abs/1")


class RenderedRecords(SiteFixture):
    """Durable records reach a reader as pages, not as raw Markdown on a code host.

    Rendering is derivation and rewrites nothing, so ``research/explorations/`` stays
    append-only (CLAUDE.md constraint 6).
    """

    def test_a_record_carries_a_slug_a_title_and_a_document(self):
        self.add_ledger("program", "test", [node("thm:a")])
        self.add_checkpoint("audit", nodes=("thm:a",),
                            body="# A dated record\n\nWith a body.\n")

        record = self.data()["memory"]["checkpoints"][0]

        self.assertEqual(record["slug"], "2026-08-26-audit")
        self.assertEqual(record["title"], "A dated record")
        self.assertEqual(record["document"], "records/2026-08-26-audit.json")

    def test_the_body_is_written_beside_the_data_and_not_inside_it(self):
        """92 rendered records dwarf everything else the site knows, and a reader opening
        the front page should not pay for all of them to read one."""
        self.add_ledger("program", "test", [node("thm:a")])
        self.add_checkpoint("audit", nodes=("thm:a",), body=(
            "# A dated record\n\nAn opening paragraph long enough to be the excerpt.\n\n"
            "## A later section\n\nA sentence nobody else holds.\n"))

        data = self.data()
        document = json.loads((self.out / "records/2026-08-26-audit.json")
                              .read_text(encoding="utf-8"))

        self.assertNotIn("A sentence nobody else holds.",
                         (self.out / "data.json").read_text(encoding="utf-8"))
        self.assertIn("A sentence nobody else holds.", json.dumps(document))
        self.assertNotIn("records", data)

    def test_the_opening_heading_becomes_the_title_and_not_a_second_heading(self):
        self.add_ledger("program", "test", [node("thm:a")])
        self.add_checkpoint("audit", nodes=("thm:a",), body="# Only once\n\nBody.\n")

        self.data()
        document = json.loads((self.out / "records/2026-08-26-audit.json")
                              .read_text(encoding="utf-8"))

        self.assertEqual(document["title"], "Only once")
        self.assertNotIn("Only once", json.dumps(document["blocks"]))

    def test_a_stale_record_page_is_removed_on_rebuild(self):
        """A rebuild that only ever added would keep an unreachable page published."""
        self.add_ledger("program", "test", [node("thm:a")])
        self.add_checkpoint("audit", nodes=("thm:a",))
        self.data()
        orphan = self.out / "records/gone.json"
        orphan.write_text("{}", encoding="utf-8")

        self.data()

        self.assertFalse(orphan.exists())

    def test_the_excerpt_skips_a_metadata_opening_line(self):
        self.add_ledger("program", "test", [node("thm:a")])
        self.add_checkpoint("audit", nodes=("thm:a",), body=(
            "# A record\n\nDate: 2026-08-26\n\n"
            "The paragraph that actually says what happened and why it mattered.\n"))

        record = self.data()["memory"]["checkpoints"][0]

        self.assertTrue(record["excerpt"].startswith("The paragraph"))


class MacroSeam(SiteFixture):
    """Statements are LaTeX against `preamble.tex`; the macro table comes from outside.

    Generating it from the preamble belongs to the HTML manuscript conversion. Building a
    second extractor here would be the duplicate parser `site.py` exists to avoid, so
    this file only carries the table and the frontend installs it.
    """

    def test_a_build_without_a_table_says_so_rather_than_inventing_one(self):
        self.add_ledger("program", "test", [node("thm:a")])

        self.assertIsNone(self.data()["macros"])

    def test_an_attached_table_reaches_the_frontend(self):
        self.add_ledger("program", "test", [node("thm:a")])

        data = self.data(macros={"R": "\\mathbb{R}"})

        self.assertEqual(data["macros"], {"R": "\\mathbb{R}"})

    def test_a_table_that_is_not_a_table_is_refused_rather_than_ignored(self):
        path = self.root / "macros.json"
        path.write_text("[1, 2]", encoding="utf-8")

        macros, errors = site_module.read_macros(path)

        self.assertIsNone(macros)
        self.assertTrue(errors)


class Layout(SiteFixture):
    def test_every_claim_is_placed(self):
        self.add_ledger("program", "test", [node("lem:base"),
                                            node("thm:top", depends_on=["lem:base"])])

        layout = self.data()["layout"]["claims"]

        self.assertEqual(sorted(layout), ["lem:base", "thm:top"])

    def test_a_dependency_is_laid_out_below_what_rests_on_it(self):
        """Layout is navigation only, but it must not assert the reverse of the truth."""
        self.add_ledger("program", "test", [node("lem:base"),
                                            node("thm:top", depends_on=["lem:base"])])

        layout = self.data()["layout"]["claims"]

        self.assertGreater(layout["thm:top"]["y"], layout["lem:base"]["y"])

    def test_only_proof_dependencies_set_the_layering(self):
        """An antecedent is not a dependency; letting it layer would say it was."""
        self.add_ledger("program", "test", [
            node("asm:a", status="open", kind="assumption"),
            node("thm:b", assumes=["asm:a"]),
        ])

        layout = self.data()["layout"]["claims"]

        self.assertEqual(layout["asm:a"]["y"], layout["thm:b"]["y"])


class Output(SiteFixture):
    def test_the_frontend_and_the_data_are_written(self):
        self.add_ledger("program", "test", [node("thm:a")])

        self.publish()

        for name in ("index.html", "site.css", "site.js", "data.json"):
            self.assertTrue((self.out / name).is_file(), name)

    def test_data_json_is_valid_json_and_matches_what_build_returned(self):
        self.add_ledger("program", "test", [node("thm:a")])

        data, _errors = self.publish()

        self.assertEqual(json.loads((self.out / "data.json").read_text()), data)

    def test_publishing_a_subtree_records_the_prefix_its_links_need(self):
        """`--root example` publishes paths that are only addressable with a prefix."""
        prefix = site_module._source_prefix(EXAMPLE)

        self.assertEqual(prefix, "example/")
        self.assertEqual(site_module._source_prefix(REPO), "")


class TheFrontendHoldsNoMathematics(unittest.TestCase):
    """The invariant that keeps this a derived view rather than a second home.

    Everything substantive is derived at build time. A statement, a status, a route
    objective or a blocker typed into site/ would drift from the ledger and the portfolio
    the first time either changed, and the prettier copy would win the argument.
    """

    @classmethod
    def setUpClass(cls):
        if not EXAMPLE.is_dir():  # pragma: no cover - fixture tree always ships
            raise unittest.SkipTest("no worked example to publish")
        cls.out = Path(REPO / "build/site-selftest")
        shutil.rmtree(cls.out, ignore_errors=True)
        cls.data, cls.errors = site_module.build(EXAMPLE, cls.out)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.out, ignore_errors=True)

    def setUp(self):
        self.assertEqual(self.errors, [], "the worked example must stay publishable")

    #: Exactly the suffixes ``build()`` copies into the site. The scope is deliberate:
    #: only these files become the page, so only these can leak a second copy of a
    #: statement to a reader. ``README.md`` and ``tex4ht.cfg`` are prose *about* the
    #: frontend and name ids freely — a documentation example is not a source of truth,
    #: and forbidding it would be a rule with no failure behind it.
    DEPLOYED = {".html", ".css", ".js"}

    def frontend_text(self) -> str:
        return "\n".join(path.read_text(encoding="utf-8")
                         for path in sorted(FRONTEND.iterdir())
                         if path.is_file() and path.suffix in self.DEPLOYED)

    def test_the_scope_of_these_checks_is_what_actually_ships(self):
        """If build() starts copying a suffix, this class must start reading it."""
        published = {path.suffix for path in (self.out).iterdir() if path.is_file()}

        self.assertLessEqual(published - {".json"}, self.DEPLOYED)

    def test_no_claim_gloss_appears_in_the_frontend(self):
        text = self.frontend_text()
        for claim in self.data["claims"].values():
            self.assertNotIn(claim["gloss"], text, claim["id"])

    def test_no_candidate_statement_or_route_objective_appears_in_the_frontend(self):
        text = self.frontend_text()
        for candidate in self.data["memory"]["candidates"]:
            self.assertNotIn(candidate["statement"], text, candidate["id"])
        for route in self.data["search"]["routes"].values():
            if route["objective"]:
                self.assertNotIn(route["objective"], text, route["id"])

    def test_no_node_or_route_id_is_hard_coded_in_the_frontend(self):
        text = self.frontend_text()
        for identifier in [*self.data["claims"], *self.data["search"]["routes"],
                           *self.data["search"]["families"]]:
            self.assertNotIn(identifier, text, identifier)

    def test_this_repository_s_own_identifiers_are_not_hard_coded_either(self):
        """The example names five nodes; this repository names 138.

        The check above can only catch an id the *worked example* happens to use, so a
        curated selection typed straight into site.js would sail past it untouched. The
        Explore views do select claims by id and do name families, and every one of those
        choices belongs in research/program/editorial.yaml where the editorial lane can
        validate it against the ledger and the portfolio. This is the test that says so.
        """
        text = self.frontend_text()
        for relative in ("research/program/ledger.yaml",
                         "research/program/portfolio.yaml",
                         "research/program/editorial.yaml"):
            path = REPO / relative
            if not path.is_file():
                continue
            document = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
            for identifier in _identifiers(document):
                self.assertNotIn(identifier, text, f"{relative}: {identifier}")

    def test_the_worked_example_exercises_every_genre_the_site_renders(self):
        """If this fails, the fixture stopped covering a path the site draws."""
        statuses = {claim["status"] for claim in self.data["claims"].values()}
        states = {route["state"] for route in self.data["search"]["routes"].values()}
        modes = {proof["mode"] for claim in self.data["claims"].values()
                 for proof in claim["proofs"]}

        self.assertLessEqual({"proved", "open", "refuted"}, statuses)
        self.assertLessEqual({"completed", "blocked", "duplicate"}, states)
        self.assertIn("agent", modes)
        self.assertTrue(self.data["memory"]["candidates"])
        self.assertTrue(self.data["memory"]["promoted"])
        self.assertTrue(self.data["memory"]["reviews"])


class FrontendSyntax(unittest.TestCase):
    """A syntax error in site.js is a blank page, and nothing else would catch it."""

    def test_the_script_parses(self):
        if shutil.which("node") is None:
            self.skipTest("node not installed")
        finished = subprocess.run(["node", "--check", str(FRONTEND / "site.js")],
                                  capture_output=True, text=True, check=False)

        self.assertEqual(finished.returncode, 0, finished.stderr)


class PagesWorkflow(unittest.TestCase):
    """Pin the deployment details that otherwise fail only on GitHub's runner."""

    def test_make4ht_comes_from_the_ubuntu_package_that_ships_it(self):
        text = PAGES_WORKFLOW.read_text(encoding="utf-8")
        install = text.split("sudo apt-get install", 1)[1].split("command -v make4ht", 1)[0]

        self.assertIn("texlive-extra-utils", install)
        self.assertNotRegex(install, r"(?:^|\s)make4ht(?:\s|$)")

    def test_deployment_follows_the_configured_default_branch(self):
        text = PAGES_WORKFLOW.read_text(encoding="utf-8")

        self.assertIn("github.event.repository.default_branch", text)
        self.assertNotIn("refs/heads/main", text)
        self.assertNotIn("branches: [main]", text)

    def test_publishing_happens_only_when_a_human_asks(self):
        # Restoring `push:` here would republish the site from every commit on the
        # default branch, which is the behaviour this repository decided against.
        text = PAGES_WORKFLOW.read_text(encoding="utf-8")
        triggers = text.split("\non:", 1)[1].split("\npermissions:", 1)[0]

        self.assertIn("workflow_dispatch", triggers)
        self.assertNotIn("push", triggers)
        self.assertNotIn("pull_request", triggers)


class CheckWorkflow(unittest.TestCase):
    """The cheap checks are the ones that may run unattended."""

    def test_pull_requests_are_validated(self):
        text = CHECK_WORKFLOW.read_text(encoding="utf-8")
        triggers = text.split("\non:", 1)[1].split("\npermissions:", 1)[0]

        self.assertIn("pull_request", triggers)
        self.assertIn("scripts/check.py", text)
        self.assertIn("unittest discover", text)

    def test_the_expensive_half_stays_out_of_it(self):
        # If TeX Live ever reappears here, every pull request pays minutes for a
        # document nobody asked to build. The comments name those tools to say where
        # they live, so this reads the steps and not the prose around them.
        steps = "\n".join(line for line in CHECK_WORKFLOW.read_text(encoding="utf-8").splitlines()
                          if not line.lstrip().startswith("#"))

        self.assertNotIn("texlive", steps)
        self.assertNotIn("latexmk", steps)
        self.assertNotIn("make4ht", steps)
        self.assertNotIn("deploy-pages", steps)


if __name__ == "__main__":
    unittest.main()
