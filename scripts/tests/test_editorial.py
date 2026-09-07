"""The editorial lane: what a reader is shown, and why it can be trusted.

Three things reach a reader that the ledger does not literally contain: the standing
badge beside a statement, the human title used as a heading, and the curated selection
the public views open with. Each is a projection of validated state, and each is exactly
where a second source of truth would grow if nobody were watching.

    python3 -m unittest discover -s scripts/tests -p 'test_*.py'
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from checks import editorial, guide, ledger  # noqa: E402
from fixtures import REPO, CheckerFixture, node  # noqa: E402


class TitleExtraction(unittest.TestCase):
    """The amsthm optional argument, found without a LaTeX parser."""

    def title(self, source: str) -> str | None:
        found = ledger._labels_with_environments(source)
        return found[0][3] if found else None

    def test_a_plain_title_is_taken(self):
        self.assertEqual(
            self.title("\\begin{theorem}[All-cut Carleson implies KLS]\\label{thm:a}\\end{theorem}"),
            "All-cut Carleson implies KLS")

    def test_a_claim_without_a_title_reports_none(self):
        self.assertIsNone(self.title("\\begin{theorem}\\label{thm:a}\\end{theorem}"))

    def test_a_newline_between_the_environment_and_its_title_is_allowed(self):
        self.assertEqual(
            self.title("\\begin{lemma}\n  [Profile bound]\\label{lem:a}\\end{lemma}"),
            "Profile bound")

    def test_a_citation_inside_braces_does_not_end_the_title(self):
        """The live shape at modules/kls/15-covariance-technology.tex.

        A ``[^\\]]*`` regex stops at the ``]`` of ``\\cite[Thm.~61]``, which truncates the
        title mid-sentence and leaves ``{KLnotes}}]`` in the document as prose.
        """
        self.assertEqual(
            self.title("\\begin{theorem}[{K--L; the form is \\cite[Thm.~61]{KLnotes}}]"
                       "\\label{thm:a}\\end{theorem}"),
            "{K--L; the form is \\cite[Thm.~61]{KLnotes}}")

    def test_a_citation_outside_braces_does_not_either(self):
        self.assertEqual(
            self.title("\\begin{theorem}[K--L \\cite[Thm.~61]{KLnotes}]"
                       "\\label{thm:a}\\end{theorem}"),
            "K--L \\cite[Thm.~61]{KLnotes}")

    def test_an_unbalanced_bracket_is_untitled_rather_than_a_guess(self):
        self.assertIsNone(
            self.title("\\begin{theorem}[open forever\\label{thm:a}\\end{theorem}"))

    def test_a_structural_label_carries_no_title(self):
        found = ledger._labels_with_environments("\\section{S}\\label{sec:a}")
        self.assertEqual(found[0][1:], (None, 1, None))


class TitleDisplay(unittest.TestCase):
    """What a heading may show, and what must fail loudly instead."""

    def shown(self, raw: str) -> str | None:
        display, problem = editorial.title_display(raw)
        self.assertIsNone(problem, problem)
        return display

    def test_mathematics_survives_verbatim_for_mathjax(self):
        self.assertEqual(self.shown("Isoperimetric $\\log n$ frontier"),
                         "Isoperimetric $\\log n$ frontier")

    def test_dashes_and_nonbreaking_spaces_become_characters(self):
        self.assertEqual(self.shown("Klartag--Lehec~bound"), "Klartag\u2013Lehec\u00a0bound")

    def test_an_accent_composes_to_one_character(self):
        self.assertEqual(self.shown("Poincar\\'e"), "Poincar\u00e9")
        self.assertEqual(self.shown("Poincar\\'{e}"), "Poincar\u00e9")

    def test_emphasis_is_unwrapped_rather_than_dropped(self):
        self.assertEqual(self.shown("An \\emph{exact} case"), "An exact case")

    def test_a_trailing_citation_clause_goes_with_the_citation(self):
        """A heading ending "the sup-over-time form is" is worse than one that stops."""
        self.assertEqual(
            self.shown("{K--L; the sup-over-time form is \\cite[Thm.~61]{KLnotes}}"),
            "K\u2013L")

    def test_a_dangling_reference_noun_goes_too(self):
        self.assertEqual(self.shown("Endpoint reduction; answers Question~\\ref{q:x}"),
                         "Endpoint reduction")

    def test_a_semicolon_clause_with_real_content_is_kept(self):
        """The trim must fire on provenance only, never on the second half of a title."""
        self.assertEqual(self.shown("Product structure under localization; KLS for products"),
                         "Product structure under localization; KLS for products")

    def test_a_clause_carrying_mathematics_is_kept(self):
        self.assertEqual(self.shown("Frontier; the $\\log n$ bound \\cite{X}"),
                         "Frontier; the $\\log n$ bound")

    def test_an_unsupported_macro_is_refused_rather_than_leaked(self):
        display, problem = editorial.title_display("Red \\textcolor{red}{alert}")
        self.assertIsNone(display)
        self.assertIn("textcolor", problem)

    def test_every_title_in_this_manuscript_reduces(self):
        """The whole point: no heading on the live site can contain raw TeX."""
        labels = ledger.manuscript_labels(REPO)
        titled = [entry for entry in labels.values() if entry.get("title")]
        self.assertGreater(len(titled), 0, "the manuscript titles its claims")
        for entry in titled:
            display, problem = editorial.title_display(entry["title"])
            self.assertIsNone(problem, f"{entry['file']}:{entry['line']}: {problem}")
            self.assertTrue(display, f"{entry['file']}:{entry['line']} reduces to nothing")


class Standing(unittest.TestCase):
    """The projection, and the distinctions it exists to keep."""

    def detail(self, **fields) -> dict:
        item = {"id": "thm:a", "status": "proved", "provenance": "internal", **fields}
        nodes = dict(fields.pop("_nodes", {}))
        nodes["thm:a"] = item
        return editorial.standing_detail(item, nodes)

    def test_a_published_import_is_not_certified_here(self):
        """10 of this repository's 86 proved nodes are literature with no dossier."""
        detail = self.detail(provenance="literature", import_class="published")

        self.assertEqual(detail["standing"], "Published result")
        self.assertEqual(detail["standing_tone"], "published")

    def test_a_certified_result_and_a_published_one_are_drawn_differently(self):
        certified = self.detail(proofs=[{"artifact": "s.tex", "mode": "agent",
                                         "review": "r.md"}])
        published = self.detail(provenance="literature", import_class="published")

        self.assertEqual(certified["standing_tone"], "certified")
        self.assertNotEqual(certified["standing_tone"], published["standing_tone"])

    def test_an_attestation_is_weaker_than_a_persisted_review(self):
        attested = self.detail(proofs=[{"artifact": "s.tex", "mode": "human",
                                        "accepted_by": "someone"}])

        self.assertEqual(attested["standing"], "Proved here, attested")
        self.assertEqual(attested["standing_tone"], "attested")

    def test_open_is_told_apart_by_kind(self):
        """An open premise is something an argument rests on; a barrier only advises."""
        premise = self.detail(status="open", kind="assumption")
        barrier = self.detail(status="open", kind="obstruction")

        self.assertEqual(premise["standing_tone"], "premise")
        self.assertEqual(barrier["standing_tone"], "barrier")

    def test_a_conditional_result_keeps_its_tone_and_gains_a_qualifier(self):
        """Constraint 8 and P2: still proved, still not progress on the target."""
        nodes = {
            "asm:open": {"id": "asm:open", "status": "open", "kind": "assumption"},
            "thm:a": {"id": "thm:a", "status": "proved", "provenance": "internal",
                      "assumes": ["asm:open"],
                      "proofs": [{"artifact": "s.tex", "mode": "agent", "review": "r.md"}]},
        }

        detail = editorial.standing_detail(nodes["thm:a"], nodes)

        self.assertEqual(detail["standing"], "Certified here, conditional")
        self.assertEqual(detail["standing_tone"], "certified")
        self.assertTrue(detail["standing_conditional"])

    def test_every_tone_is_from_the_closed_set(self):
        """The frontend styles these by name; an unstyled one would render as nothing."""
        self.assertEqual(set(editorial.STANDING_TONES.values()),
                         {"published", "preprint", "certified", "attested",
                          "proved-elsewhere", "open", "premise", "barrier",
                          "refuted", "definition"})


class GuideValidation(CheckerFixture):
    """Navigation only, and every identifier in it must resolve."""

    def setUp(self):
        super().setUp()
        self.add_ledger("program", "test", [node("thm:a"), node("thm:b")])
        self.add_portfolio({
            "target": "thm:a",
            "families": [{"id": "fam:one", "mechanism": "m", "state": "active"}],
            "approaches": [{"id": "ap:one", "family": "fam:one", "objective": "o",
                            "state": "active"}],
        })
        self.labels = ledger.manuscript_labels(self.root)
        self.nodes = {"thm:a", "thm:b"}
        self.families = {"fam:one"}

    def verdict(self, document: dict) -> list[str]:
        errors: list[str] = []
        guide.check(self.root, document, self.nodes, self.families, self.labels, errors)
        return errors

    def sound(self) -> dict:
        """A guide with everything resolving. Its `featured` list is deliberately below
        the floor — this fixture ledger has two nodes and ids must be unique — so the
        tests below assert on the error they are about rather than on an empty list."""
        return {
            "site": {"name": "Test"},
            "routes": [{"code": "E", "name": "One", "families": ["fam:one"],
                        "anchor": "thm:a"}],
            "featured": [{"id": "thm:a", "role": "bridge", "route": "E"},
                         {"id": "thm:b", "role": "advance"}],
        }

    def test_a_short_selection_is_the_only_complaint_about_a_sound_guide(self):
        errors = self.verdict(self.sound())

        self.assertEqual(len(errors), 1, errors)
        self.assertIn("stops being a selection", errors[0])

    def test_an_absent_guide_is_not_an_error(self):
        """A repository that publishes no guide is complete, not degraded."""
        self.assertEqual(self.verdict(None), [])
        self.assertIsNone(guide.load(self.root, []))

    def test_a_featured_id_that_is_no_node_is_refused(self):
        document = self.sound()
        document["featured"].append({"id": "thm:ghost", "role": "model"})

        self.assertTrue(any("thm:ghost" in error for error in self.verdict(document)))

    def test_an_anchor_that_is_no_label_is_refused(self):
        document = self.sound()
        document["reading"] = [{"label": "Start", "anchor": "sec:ghost"}]

        self.assertTrue(any("sec:ghost" in error for error in self.verdict(document)))

    def test_a_family_in_two_routes_is_refused(self):
        document = self.sound()
        document["routes"].append({"code": "S", "name": "Two",
                                   "families": ["fam:one"], "anchor": "thm:a"})

        self.assertTrue(any("belongs to one route" in error
                            for error in self.verdict(document)))

    def test_a_family_nobody_placed_is_refused(self):
        """It would stay live in the portfolio and vanish from the public site."""
        document = self.sound()
        document["routes"][0]["families"] = []

        self.assertTrue(any("belongs to no route" in error
                            for error in self.verdict(document)))

    def test_a_canonical_field_may_not_be_written_here(self):
        """Constraint 7, made mechanical rather than left to good intentions."""
        for field in ("summary", "statement", "status", "objective", "blocker"):
            document = self.sound()
            document["featured"][0][field] = "a tempting copy"

            self.assertTrue(
                any("canonical elsewhere" in error for error in self.verdict(document)),
                field)

    def test_a_canonical_field_is_caught_however_deeply_it_is_buried(self):
        document = self.sound()
        document["routes"][0]["extra"] = {"deeper": [{"mechanism": "a copy"}]}

        self.assertTrue(any("canonical elsewhere" in error
                            for error in self.verdict(document)))

    def test_an_unknown_role_is_refused(self):
        document = self.sound()
        document["featured"][0]["role"] = "headline"

        self.assertTrue(any("headline" in error for error in self.verdict(document)))

    def test_a_featured_claim_may_not_name_a_route_that_is_not_there(self):
        document = self.sound()
        document["featured"][0]["route"] = "Z"

        self.assertTrue(any("Z" in error for error in self.verdict(document)))

    def test_the_live_guide_validates_against_the_live_repository(self):
        """The one that matters: this repository's own editorial.yaml is sound."""
        document = guide.load(REPO, [])
        if document is None:
            self.skipTest("this repository publishes no editorial guide")
        labels = ledger.manuscript_labels(REPO)
        errors: list[str] = []
        ledger_doc = yaml.safe_load((REPO / "research/program/ledger.yaml").read_text())
        portfolio_doc = yaml.safe_load(
            (REPO / "research/program/portfolio.yaml").read_text())
        guide.check(
            REPO, document,
            {item["id"] for item in ledger_doc["nodes"]},
            {item["id"] for item in portfolio_doc["families"]},
            labels, errors,
        )

        self.assertEqual(errors, [])


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
