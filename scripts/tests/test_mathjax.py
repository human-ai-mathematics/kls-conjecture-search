r"""Carrying preamble.tex's macros to MathJax, and the audit that proves they arrived.

The finding this closes: the HTML conversion printed 42 of the manuscript's own macros
as literal red source mid-formula --- ``\Aop``, ``\norm``, ``\inner``, ``\eps`` --- because
``make4ht``'s ``mathjax`` mode hands mathematics to MathJax verbatim and configures
nothing. The PDF was correct throughout, so no LaTeX build and no lane of the checker
could see it.

Two things are under test, and the second is the one that keeps the first honest:

* the parser and the escaping, so the generated block is a *derivation* of preamble.tex
  rather than a transcription of it;
* the audit over a built page, so "no macro reaches the reader as source" is a fact about
  the artifact rather than a claim about the config.

    python3 -m unittest discover -s scripts/tests -p 'test_*.py'
"""
from __future__ import annotations

import io
import json
import re
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from checks import mathjax  # noqa: E402

CONFIG_SKELETON = "\\Preamble{xhtml}\n\n\\begin{document}\n\\EndPreamble\n"


def entries(macros: list[mathjax.Macro]) -> dict[str, object]:
    return {macro.name: macro.as_entry() for macro in macros}


def expand(block: str) -> dict[str, object]:
    r"""What TeX writes when it reads the generated block, decoded as JSON.

    Stands in for a full TeX4ht run, and tests the one thing a run would: that two
    escapings compose correctly. TeX removes the single space that ends each
    ``\harnessbs`` control word, and turns each source newline into a space; what is left
    is a JavaScript object literal whose string escapes must decode to the macro bodies
    the preamble actually wrote.
    """
    source = " ".join(block.splitlines())
    written = source.replace("\\harnessbs ", "\\").replace("\\harnesshash ", "#")
    match = re.search(r"var derived = (\{.*?\}); for \(var name in derived\)", written)
    assert match is not None, "the generated block has no macro table"
    return json.loads(match.group(1))


class ParserTests(unittest.TestCase):
    def parse(self, text: str):
        return mathjax.parse(text)

    def test_a_plain_definition_becomes_a_string_entry(self):
        macros, skipped = self.parse(r"\newcommand{\Aop}{\mathsf A}")

        self.assertEqual(entries(macros), {"Aop": r"\mathsf A"})
        self.assertEqual(skipped, [])

    def test_an_argument_count_becomes_the_second_element(self):
        macros, _ = self.parse(r"\newcommand{\inner}[2]{\left\langle #1,#2\right\rangle}")

        self.assertEqual(entries(macros),
                         {"inner": [r"\left\langle #1,#2\right\rangle", 2]})

    def test_an_optional_argument_default_becomes_the_third(self):
        macros, _ = self.parse(r"\newcommand{\pair}[2][x]{(#1,#2)}")

        self.assertEqual(entries(macros), {"pair": ["(#1,#2)", 2, "x"]})

    def test_the_name_may_be_written_without_braces(self):
        macros, _ = self.parse(r"\newcommand\eps{\varepsilon}")

        self.assertEqual(entries(macros), {"eps": r"\varepsilon"})

    def test_the_starred_short_form_is_the_same_definition(self):
        macros, _ = self.parse(r"\newcommand*{\eps}{\varepsilon}")

        self.assertEqual(entries(macros), {"eps": r"\varepsilon"})

    def test_a_later_renewcommand_wins(self):
        macros, _ = self.parse(
            "\\newcommand{\\R}{\\mathbf{R}}\n\\renewcommand{\\R}{\\mathbb{R}}\n"
        )

        self.assertEqual(entries(macros), {"R": r"\mathbb{R}"})

    def test_a_math_operator_becomes_operatorname(self):
        macros, _ = self.parse(r"\DeclareMathOperator{\Cov}{Cov}")

        self.assertEqual(entries(macros), {"Cov": r"\operatorname{Cov}"})

    def test_a_starred_math_operator_keeps_its_star(self):
        macros, _ = self.parse(r"\DeclareMathOperator*{\argmin}{arg\,min}")

        self.assertEqual(entries(macros), {"argmin": r"\operatorname*{arg\,min}"})

    def test_nested_braces_and_line_breaks_survive(self):
        macros, _ = self.parse(
            "\\newcommand{\\CPaff}{C_{\\mathrm P}^{\n  \\mathrm{aff}}}\n"
        )

        self.assertEqual(entries(macros), {"CPaff": r"C_{\mathrm P}^{ \mathrm{aff}}"})

    def test_a_commented_out_definition_is_not_read(self):
        macros, skipped = self.parse(
            "% \\newcommand{\\Ghost}{\\gamma}\n\\newcommand{\\Real}{\\mathbb{R}} % a set\n"
        )

        self.assertEqual(entries(macros), {"Real": r"\mathbb{R}"})
        self.assertEqual(skipped, [])

    def test_a_definition_nested_in_another_body_is_not_read_twice(self):
        """The scanner consumes a body whole, so an inner ``\\newcommand`` is that body."""
        macros, skipped = self.parse(
            r"\newcommand{\wrapper}{\newcommand{\inner}{x}}"
        )

        self.assertEqual(entries(macros), {})
        self.assertEqual([name for name, _ in skipped], ["wrapper"])


class SkipTests(unittest.TestCase):
    def reason(self, text: str, name: str) -> str:
        macros, skipped = mathjax.parse(text)
        self.assertNotIn(name, entries(macros))
        return dict(skipped)[name]

    def test_a_name_mathjax_cannot_address_is_skipped(self):
        reason = self.reason(r"\newcommand{\l@part}[2]{#1#2}", "l@part")

        self.assertIn("not a MathJax macro name", reason)

    def test_a_text_mode_helper_is_skipped_and_named(self):
        """The real case: ``\\klspart`` is a page divider, not a piece of mathematics."""
        reason = self.reason(
            r"\newcommand{\klspart}[1]{\par\noindent\textbf{#1}\par}", "klspart")

        self.assertIn(r"'\par'", reason)

    def test_an_internal_command_in_the_body_is_skipped(self):
        reason = self.reason(r"\newcommand{\tag}{\hb@xt@ 1em}", "tag")

        self.assertIn("internal command", reason)

    def test_unbalanced_braces_are_skipped_rather_than_emitted(self):
        """Emitting one would break the config file, not just the macro."""
        reason = self.reason(r"\newcommand{\open}{\{}", "open")

        self.assertIn("unbalanced braces", reason)

    def test_a_character_the_config_cannot_transport_is_skipped(self):
        reason = self.reason(r"\newcommand{\pct}{50\%}", "pct")

        self.assertIn("cannot transport", reason)

    def test_an_empty_body_is_skipped(self):
        reason = self.reason(r"\newcommand{\nothing}{}", "nothing")

        self.assertIn("empty", reason)

    def test_a_skipped_definition_is_listed_in_the_generated_block(self):
        macros, skipped = mathjax.parse(
            "\\newcommand{\\R}{\\mathbb{R}}\n"
            "\\newcommand{\\klspart}[1]{\\par #1}\n"
        )
        block = mathjax.render(macros, skipped)

        self.assertIn(r"%   \klspart:", block)
        self.assertIn("Skipped, and why (1 of 2 definitions)", block)


class EscapingTests(unittest.TestCase):
    """The generated block is TeX source that must become a JavaScript object literal."""

    def roundtrip(self, preamble: str) -> dict[str, object]:
        macros, skipped = mathjax.parse(preamble)
        return expand(mathjax.render(macros, skipped))

    def test_a_body_survives_both_escapings_unchanged(self):
        self.assertEqual(
            self.roundtrip(r"\newcommand{\dd}{\,\mathrm{d}}"),
            {"dd": r"\,\mathrm{d}"},
        )

    def test_an_argument_marker_survives(self):
        self.assertEqual(
            self.roundtrip(r"\newcommand{\norm}[1]{\left\lVert #1\right\rVert}"),
            {"norm": [r"\left\lVert #1\right\rVert", 1]},
        )

    def test_subscripts_superscripts_and_nesting_survive(self):
        self.assertEqual(
            self.roundtrip("\\newcommand{\\lmax}{\\lambda_{\\max}}\n"
                           "\\newcommand{\\hstar}{h^{\\star}}\n"),
            {"lmax": r"\lambda_{\max}", "hstar": r"h^{\star}"},
        )

    def test_the_whole_repository_preamble_survives(self):
        """Not a fixture: the real file, because it is the only source that matters."""
        preamble = Path(__file__).resolve().parents[2] / mathjax.PREAMBLE_PATH
        if not preamble.is_file():  # pragma: no cover - a fork may carry no manuscript
            self.skipTest("no preamble.tex in this tree")
        macros, skipped = mathjax.parse(preamble.read_text(encoding="utf-8"))

        self.assertEqual(expand(mathjax.render(macros, skipped)), entries(macros))


class GeneratedBlockTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        (self.root / "site").mkdir()
        self.config = self.root / mathjax.CONFIG_PATH
        self.config.write_text(CONFIG_SKELETON, encoding="utf-8")
        self.preamble = self.root / mathjax.PREAMBLE_PATH
        self.preamble.write_text("\\newcommand{\\R}{\\mathbb{R}}\n", encoding="utf-8")

    def tearDown(self):
        self.tempdir.cleanup()

    def errors(self) -> list[str]:
        found: list[str] = []
        mathjax.check(self.root, found)
        return found

    def test_a_config_with_no_block_is_an_error_naming_the_fix(self):
        self.assertIn(mathjax.REGENERATE, self.errors()[0])

    def test_writing_the_block_puts_it_before_begin_document(self):
        mathjax.write(self.root)
        text = self.config.read_text(encoding="utf-8")

        self.assertLess(text.index(mathjax.BEGIN_MARKER), text.index("\\begin{document}"))
        self.assertEqual(self.errors(), [])

    def test_regenerating_is_idempotent(self):
        mathjax.write(self.root)
        once = self.config.read_text(encoding="utf-8")
        mathjax.write(self.root)

        self.assertEqual(self.config.read_text(encoding="utf-8"), once)

    def test_a_macro_added_to_the_preamble_makes_the_block_stale(self):
        """The whole point: the second source of truth cannot drift quietly."""
        mathjax.write(self.root)
        self.preamble.write_text(
            "\\newcommand{\\R}{\\mathbb{R}}\n\\newcommand{\\Aop}{\\mathsf A}\n",
            encoding="utf-8")

        self.assertIn("disagrees with preamble.tex", self.errors()[0])

        mathjax.write(self.root)
        self.assertEqual(self.errors(), [])

    def test_hand_editing_the_block_is_caught(self):
        mathjax.write(self.root)
        self.config.write_text(
            self.config.read_text(encoding="utf-8").replace('"R"', '"Real"'),
            encoding="utf-8")

        self.assertIn("disagrees with preamble.tex", self.errors()[0])

    def test_a_tree_with_no_config_has_nothing_to_keep_honest(self):
        """Activation is structural: a repository that publishes no site is not failing."""
        self.config.unlink()

        self.assertEqual(self.errors(), [])

    def test_a_tree_with_no_preamble_is_inert(self):
        self.preamble.unlink()

        self.assertEqual(self.errors(), [])


PAGE = """<!DOCTYPE html><html><head>{config}</head><body>
<p>The operator \\(\\Aop x\\) is bounded, and \\begin{{equation}}
\\norm{{\\Aop x}} \\le \\CP (\\mu ) \\label{{eq:one}}
\\end{{equation}} follows.</p>
{extra}</body></html>
"""

CARRIED = ('<script>var mj; var derived = {"Aop": "\\\\mathsf A", '
           '"norm": ["x", 1], "CP": "y"}; for (var name in derived) {}</script>')


class AuditTests(unittest.TestCase):
    """The acceptance test, over a built page rather than over the configuration."""

    def test_a_page_without_the_config_reports_every_macro_it_prints_as_source(self):
        findings = mathjax.audit_page(PAGE.format(config="", extra=""),
                                      {"Aop", "norm", "CP"})

        self.assertEqual(len(findings), 3)
        self.assertIn(r"\Aop is used 2x in mathematics", findings[0])
        self.assertIn("does not carry it", findings[0])

    def test_the_same_page_with_the_config_is_clean(self):
        self.assertEqual(
            mathjax.audit_page(PAGE.format(config=CARRIED, extra=""),
                               {"Aop", "norm", "CP"}),
            [],
        )

    def test_a_numbered_display_counts_as_mathematics(self):
        """A regression: reading only ``\\(...\\)`` made every numbered equation a leak."""
        page = PAGE.format(config=CARRIED, extra="")

        self.assertEqual(mathjax.page_macros(page), {"Aop", "norm", "CP"})
        self.assertEqual(mathjax.audit_page(page, {"Aop", "norm", "CP"}), [])

    def test_a_macro_the_config_refused_to_carry_is_still_reported(self):
        """Skipping a definition is a reason for red text, not an excuse for it."""
        findings = mathjax.audit_page(PAGE.format(config=CARRIED, extra=""),
                                      {"Aop", "norm", "CP", "klsstatus"})
        self.assertEqual(findings, [])

        page = PAGE.format(config=CARRIED, extra=r"<p>\(\klsstatus\)</p>")
        self.assertIn(r"\klsstatus", mathjax.audit_page(page, {"klsstatus"})[0])

    def test_a_backslash_in_prose_is_a_leak_wherever_it_came_from(self):
        page = PAGE.format(config=CARRIED, extra=r"<p>and \Gammaish text</p>")

        self.assertIn(r"survives outside mathematics: \Gammaish",
                      mathjax.audit_page(page, set())[0])

    def test_markup_and_scripts_are_not_prose(self):
        page = PAGE.format(config=CARRIED,
                           extra="<a href='x.html' title='a\\path'></a><!-- \\note -->")

        self.assertEqual(mathjax.audit_page(page, set()), [])


class ReportTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        (self.root / mathjax.PREAMBLE_PATH).write_text(
            "\\newcommand{\\Aop}{\\mathsf A}\n"
            "\\newcommand{\\norm}[1]{x}\n"
            "\\newcommand{\\CP}{y}\n", encoding="utf-8")

    def tearDown(self):
        self.tempdir.cleanup()

    def run_report(self, html_dir: Path, expected: list[str] | None = None):
        stream = io.StringIO()
        with redirect_stdout(stream):
            passed = mathjax.report(self.root, html_dir, expected or [])
        return passed, stream.getvalue()

    def test_an_unbuilt_tree_is_named_as_unbuilt_and_passes(self):
        """A check that fails because nothing was built fails for the wrong reason."""
        passed, output = self.run_report(self.root / "build/html")

        self.assertTrue(passed)
        self.assertIn("nothing to audit", output)

    def test_a_built_page_that_carries_its_macros_passes(self):
        html = self.root / "build/html"
        html.mkdir(parents=True)
        (html / "main.html").write_text(PAGE.format(config=CARRIED, extra=""),
                                        encoding="utf-8")
        passed, output = self.run_report(html, ["solutions/lem-x.tex"])

        self.assertTrue(passed)
        self.assertIn("ok   main.html", output)
        self.assertIn("solutions/lem-x.tex: not converted", output)

    def test_a_built_page_that_does_not_fails_and_names_the_macro(self):
        html = self.root / "build/html"
        html.mkdir(parents=True)
        (html / "main.html").write_text(PAGE.format(config="", extra=""),
                                        encoding="utf-8")
        passed, output = self.run_report(html)

        self.assertFalse(passed)
        self.assertIn(r"FAIL main.html: \Aop", output)


if __name__ == "__main__":
    unittest.main()
