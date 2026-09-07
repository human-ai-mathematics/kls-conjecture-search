#!/usr/bin/env python3
"""Render this repository's derived views as a static, human-facing website.

    python3 scripts/site.py                         # -> build/site/
    python3 scripts/site.py --root example          # the worked example
    python3 scripts/site.py --out /tmp/preview      # anywhere
    python3 scripts/site.py --pdf-dir build         # attach the compiled PDFs
    python3 scripts/site.py --html-dir build/html   # attach the make4ht conversion
    python3 scripts/site.py --serve                 # build, then serve it locally

The governing rule, and the reason this file exists at all:

> The site is a derived view of the repository, never another source of mathematical or
> search state.

Everything it publishes is computed from ``checks.analyze`` — the same parsed, resolved
report ``scripts/check.py`` prints from. Nothing here re-reads YAML, re-parses LaTeX, or
re-implements a rule: two parsers of the same files eventually disagree, and the one that
is prettier wins the argument. ``site/`` holds the frontend and contains no mathematical
content; ``data.json`` holds the mathematics and contains no presentation.

**It refuses to build a repository that does not validate.** A structurally invalid
revision is not the current research state, and publishing one as though it were is worse
than publishing nothing. It does *not* refuse an uninstantiated template: a fresh clone is
correctly green and correctly not ready, and the site says so on its front page rather
than failing.

This is the third script in ``scripts/``, and the split is deliberate. ``check.py`` reads
and never writes. ``new.py`` creates hand-authored scaffolds without overwriting them and
regenerates explicitly derived agent files. This one writes, and overwrites freely, because
everything it produces is a *build artifact* under ``build/`` — gitignored, reproducible
from the tree, and never cited by anything in the repository. No lane of ``check.py``
validates its output, because its output is not repository state;
``scripts/tests/test_site.py`` is what keeps it honest.

Standard library plus PyYAML, which the checker already requires. No frontend framework,
bundler, or graph library: layouts are computed here, in Python, and drawn as plain SVG in
the browser. MathJax is the one optional CDN dependency; without it the LaTeX source remains
visible. A research program's claim graph has tens of nodes, not thousands, and the
deterministic layout works offline and cannot silently fail to load.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import unicodedata
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from checks import analyze, failures  # noqa: E402
from checks.common import LANES, as_list  # noqa: E402
from checks.ledger import (LEDGER_PATH, applicability_blockers,  # noqa: E402
                           manuscript_labels)
from checks.editorial import standing_detail, title_display  # noqa: E402

#: Where the frontend lives, and where a build lands. Both repo-relative. ``build/`` is
#: already gitignored, so a built site is never committed by accident.
FRONTEND = Path("site")
DEFAULT_OUT = Path("build/site")

#: Where a rendered durable record is written, one JSON document apiece, fetched by the
#: frontend only when a reader opens that record.
RECORDS_DIRECTORY = "records"

#: Relations, in the order a reader should meet them, with what each one *means*. The
#: gloss travels with the data so the frontend never has to know mathematics — and so the
#: legend cannot drift from ``research/program/ledger-schema.md`` in a second place.
#:
#: ``class`` separates truth from applicability from fencing, which is the distinction
#: CLAUDE.md constraints 5 and 8 exist to protect. Drawing them alike would erase it.
RELATIONS: tuple[tuple[str, str, str, str], ...] = (
    ("depends_on", "proof", "depends on",
     "Claims this proof actually used. This is the acyclic proof DAG."),
    ("assumes", "applicability", "assumes",
     "Antecedents of an implication. They affect applicability, not whether the "
     "implication was proved."),
    ("implies", "applicability", "implies",
     "Conclusions advertised by a proved implication."),
    ("refines", "refinement", "refines",
     "Statements this one makes more precise or stronger."),
    ("bounded_by", "hard-fence", "bounded by",
     "A proved obstruction: a hard mathematical fence. A statement violating one is "
     "wrong by construction."),
    ("heuristic_barriers", "soft-fence", "heuristic barrier",
     "An open obstruction: an advisory method barrier. It guides work; it fences "
     "nothing logically."),
    ("refuted_by", "refutation", "refuted by",
     "Proved refuters of a refuted node. Never a proof dependency: a refuted statement "
     "has no proof."),
)

#: The reverse reading of each relation, derived on demand and stored nowhere — the same
#: rule ``checks/views.py`` follows, for the same reason.
REVERSE = {
    "depends_on": ("used_by", "used by"),
    "assumes": ("assumed_by", "assumed by"),
    "implies": ("implied_by", "implied by"),
    "refines": ("refined_by", "refined by"),
    "refuted_by": ("refutes", "refutes"),
}

#: Where the durable records live, so a relative link inside one can be resolved.
EXPLORATIONS_DIRECTORY = "research/explorations"

#: Front matter fence, so a checkpoint excerpt starts at the prose.
FRONT_MATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)
HEADING_RE = re.compile(r"^#{1,6}\s")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)

#: ``git@github.com:owner/name.git`` and ``https://github.com/owner/name`` alike.
REMOTE_RE = re.compile(r"github\.com[:/]+([^/]+)/([^/]+?)(?:\.git)?/?$")


# --------------------------------------------------------------------------------------
# prose — one block model, two producers, one consumer
# --------------------------------------------------------------------------------------
#
# Two bodies of writing on this site are neither a gloss nor a field: the *statement* a
# manuscript claim environment holds, and the *body* of a durable checkpoint. Both were
# previously reachable only by leaving the site — 138 anchors into a LaTeX module and 92
# links to a GitHub blob view — which made an index that would not say what it indexes.
#
# Both are derived here, at build time, into the same small block model, and `site.js`
# knows how to draw exactly that model and nothing else. Neither is a second home for
# anything (CLAUDE.md constraint 7): a statement is sliced verbatim out of `modules/`
# every build and re-verified against it, and a checkpoint body is the append-only record
# itself, rendered rather than rewritten (constraint 6).
#
# The model, deliberately narrow — this is not CommonMark and not LaTeX:
#
#     block  := {type: paragraph|heading|math|list|quote|code|table|rule, …}
#     span   := {t: text|math|code|id|ref|cite|em|strong|link, …}
#
# `math` spans and `math` blocks carry their `$…$`/`$$…$$` delimiters and their LaTeX
# source unaltered, because the site's contract is that the source goes into the DOM
# first and is typeset afterwards: with MathJax blocked, a reader still sees the
# mathematics as it was written.

#: What the renderers accept, and the reason the list is short: it is the constructs the
#: 93 records under ``research/explorations/`` and the 138 statements in ``modules/``
#: actually use, counted rather than guessed. Anything else is passed through as text,
#: which is the failure mode that loses the least.
LIST_MARKER_RE = re.compile(r"^(\s*)(?:([-*+])|(\d+)[.)])\s+(.*)$")
FENCE_RE = re.compile(r"^\s*(`{3,})\s*([A-Za-z0-9_+-]*)\s*$")
TABLE_RULE_RE = re.compile(r"^\s*\|?(?:\s*:?-+:?\s*\|)+\s*(?::?-+:?\s*\|?)?\s*$")
RULE_RE = re.compile(r"^\s*(?:-{3,}|\*{3,}|_{3,})\s*$")
ATX_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")

#: One left-to-right alternation, so nothing is ever matched *across* a token. A `_` or a
#: `*` inside `$x_1$` is consumed with the mathematics before emphasis is considered,
#: which is the whole reason this is one pass and not five substitutions.
MD_INLINE_RE = re.compile(
    r"(?P<code>``[^`]+``|`[^`\n]+`)"
    r"|(?P<math>\$(?:\\\$|[^$\n])+?\$)"
    r"|(?P<link>\[(?P<link_text>[^\]\n]*)\]\((?P<link_href>[^)\s]*)(?:\s+\"[^\"]*\")?\))"
    r"|(?P<autolink><(?P<url>[a-z][a-z0-9+.-]*://[^>\s]+)>)"
    r"|(?P<strong>\*\*(?P<strong_text>(?:[^*]|\*(?!\*))+)\*\*)"
    r"|(?P<em>\*(?P<em_text>[^*\n]+)\*)"
    r"|(?P<emu>(?<![\w\\])_(?P<emu_text>[^_\n]+)_(?![\w]))"
)

#: A repository identifier as it is written in prose: ``q:upgrade``, ``cand:foo``,
#: ``ap:bar``. Only tokens that actually resolve are linked — the set comes from the
#: ledger, the portfolio and the live candidates, never from a list typed here.
ID_TOKEN_RE = re.compile(r"(?<![\w:/-])([a-z][a-z0-9]*:[a-z0-9][a-z0-9-]*)(?![\w:-])")

#: LaTeX text-mode niceties, resolved so a reader meets prose rather than markup.
LATEX_TEXT_RE = re.compile(
    r"(?P<accent>\\(['`^\"~=.])\{?([A-Za-z])\}?)"
    r"|(?P<escape>\\[%&_#$}{])"
    r"|(?P<dots>\\l?dots\b|\\ldots\b)"
    r"|(?P<section>\\S(?![A-Za-z]))"
    r"|(?P<thin>\\[,;:!]|\\q?quad\b|\\ (?=\S))"
    r"|(?P<dash>---|--)"
    r"|(?P<nbsp>~)"
)
COMBINING = {"'": "\u0301", "`": "\u0300", "^": "\u0302", '"': "\u0308",
             "~": "\u0303", "=": "\u0304", ".": "\u0307"}

#: Display mathematics, mapped to what MathJax is configured for. ``site/index.html``
#: declares ``$$…$$`` and nothing else, so every display form is normalized to it rather
#: than relying on environment processing that the page does not promise.
DISPLAY_MATH_ENVIRONMENTS = {
    "equation": ("", ""), "equation*": ("", ""), "displaymath": ("", ""),
    "align": ("\\begin{aligned}", "\\end{aligned}"),
    "align*": ("\\begin{aligned}", "\\end{aligned}"),
    "eqnarray": ("\\begin{aligned}", "\\end{aligned}"),
    "eqnarray*": ("\\begin{aligned}", "\\end{aligned}"),
    "gather": ("\\begin{gathered}", "\\end{gathered}"),
    "gather*": ("\\begin{gathered}", "\\end{gathered}"),
    "multline": ("\\begin{gathered}", "\\end{gathered}"),
    "multline*": ("\\begin{gathered}", "\\end{gathered}"),
}
LATEX_LIST_ENVIRONMENTS = {"itemize": False, "enumerate": True, "description": False}

#: Emphasis in text mode. The rest of a claim's mathematics is inside ``$…$`` and is
#: never touched.
LATEX_STYLE = {"emph": "em", "textit": "em", "textsl": "em", "textbf": "strong",
               "text": None, "textup": None, "textrm": None, "textnormal": None,
               "mbox": None}

#: Commands that contribute nothing a reader can see, and their argument with them.
#: ``\label`` and ``\klsstatus`` are the anchor and the badge; both are already on the
#: page in their own right, and printing them inside the statement would be noise.
LATEX_DROPPED = {"label", "klsstatus", "leavevmode", "noindent", "smallskip",
                 "medskip", "bigskip", "par", "hfill", "centering"}

LATEX_BLOCK_RE = re.compile(r"\\\[|\\begin\{([A-Za-z][A-Za-z0-9*]*)\}")
LATEX_COMMAND_RE = re.compile(r"\\([A-Za-z]+)\*?")
LATEX_LABEL_RE = re.compile(r"\\label\{[^}]*\}")


def _braced(text: str, position: int) -> tuple[str, int]:
    """The brace group beginning at or after ``position``, and where it ends.

    Brace-counting rather than a regex, because a real argument nests:
    ``\\emph{a {b} c}``. Returns ``("", position)`` when no group is there, so a caller
    can treat a bare command as having no argument instead of swallowing the rest.
    """
    index = position
    while index < len(text) and text[index] in " \t\r\n":
        index += 1
    if index >= len(text) or text[index] != "{":
        return "", position
    depth, start = 0, index + 1
    while index < len(text):
        character = text[index]
        if character == "\\":
            index += 2
            continue
        if character == "{":
            depth += 1
        elif character == "}":
            depth -= 1
            if depth == 0:
                return text[start:index], index + 1
        index += 1
    return text[start:], len(text)


def _bracketed(text: str, position: int) -> int:
    """Past an optional ``[…]`` argument, if one starts here. Used to skip, never to read."""
    if position < len(text) and text[position] == "[":
        depth = 0
        for index in range(position, len(text)):
            if text[index] == "[":
                depth += 1
            elif text[index] == "]":
                depth -= 1
                if depth == 0:
                    return index + 1
    return position


def _latex_text(text: str) -> str:
    """LaTeX text-mode source as the characters it stands for."""
    def replace(match: re.Match) -> str:
        if match.group("accent"):
            mark = COMBINING.get(match.group(2), "")
            return unicodedata.normalize("NFC", match.group(3) + mark)
        if match.group("escape"):
            return match.group(0)[1]
        if match.group("dots"):
            return "…"
        if match.group("section"):
            return "§"
        if match.group("thin"):
            return "" if match.group(0) == "\\!" else " "
        if match.group("dash"):
            return "—" if match.group(0) == "---" else "–"
        return "\u00a0"
    return LATEX_TEXT_RE.sub(replace, text)


class Prose:
    """Both renderers, sharing what they need to link an identifier to its page.

    ``ids`` is every identifier the site can resolve — ledger nodes, portfolio
    approaches and families, live candidates — derived from the data being published and
    never listed by hand. ``records`` maps a checkpoint's repository path to its slug, so
    a record that cites another record becomes navigation between two pages instead of a
    filename. This is the site half of "ids in prose should be links".
    """

    def __init__(self, ids: set[str] | None = None, records: dict[str, str] | None = None):
        self.ids = ids or set()
        self.records = records or {}
        self._id_re = None
        if self.ids:
            alternation = "|".join(re.escape(item) for item in
                                   sorted(self.ids, key=len, reverse=True))
            self._id_re = re.compile(rf"(?<![\w:/-])({alternation})(?![\w:-])")

    # --- spans ------------------------------------------------------------------------

    def _text(self, text: str) -> list[dict]:
        """A run of plain text, with any resolvable identifier lifted out as a link."""
        if not text:
            return []
        if self._id_re is None:
            return [{"t": "text", "v": text}]
        spans: list[dict] = []
        position = 0
        for match in self._id_re.finditer(text):
            if match.start() > position:
                spans.append({"t": "text", "v": text[position:match.start()]})
            spans.append({"t": "id", "v": match.group(1)})
            position = match.end()
        if position < len(text):
            spans.append({"t": "text", "v": text[position:]})
        return spans

    def _link(self, href: str, spans: list[dict]) -> dict:
        """One link, classified by where it points.

        A sibling ``.md`` under ``research/explorations/`` is another checkpoint and
        becomes an internal page link; any other repository-relative path becomes a
        source link the frontend resolves against the published revision; everything else
        is left as the absolute URL it already was.
        """
        target = href.split("#", 1)[0]
        for path, slug in self.records.items():
            if target and (path.endswith("/" + target) or path == target):
                return {"t": "link", "record": slug, "spans": spans}
        if re.match(r"^[a-z][a-z0-9+.-]*:", href) or href.startswith("//"):
            return {"t": "link", "href": href, "spans": spans}
        resolved = self._repository_path(href)
        if resolved:
            return {"t": "link", "path": resolved, "spans": spans}
        return {"t": "link", "spans": spans}

    @staticmethod
    def _repository_path(href: str) -> str | None:
        """``../runs/x.jsonl`` in a checkpoint, as a path from the repository root."""
        parts = (EXPLORATIONS_DIRECTORY + "/" + href).split("/")
        stack: list[str] = []
        for part in parts:
            if part in ("", "."):
                continue
            if part == "..":
                if not stack:
                    return None
                stack.pop()
            else:
                stack.append(part)
        return "/".join(stack) or None

    def inline(self, text: str) -> list[dict]:
        """Markdown inline constructs, in one left-to-right pass."""
        spans: list[dict] = []
        position = 0
        for match in MD_INLINE_RE.finditer(text):
            if match.start() > position:
                spans.extend(self._text(text[position:match.start()]))
            position = match.end()
            if match.group("code"):
                body = match.group("code").strip("`")
                spans.append({"t": "id", "v": body} if body in self.ids
                             else {"t": "code", "v": body})
            elif match.group("math"):
                spans.append({"t": "math", "v": match.group("math")})
            elif match.group("link"):
                spans.append(self._link(match.group("link_href"),
                                        self.inline(match.group("link_text"))))
            elif match.group("autolink"):
                url = match.group("url")
                spans.append({"t": "link", "href": url, "spans": [{"t": "text", "v": url}]})
            elif match.group("strong"):
                spans.append({"t": "strong", "spans": self.inline(match.group("strong_text"))})
            elif match.group("em"):
                spans.append({"t": "em", "spans": self.inline(match.group("em_text"))})
            else:
                spans.append({"t": "em", "spans": self.inline(match.group("emu_text"))})
        if position < len(text):
            spans.extend(self._text(text[position:]))
        return spans

    def inline_latex(self, text: str) -> list[dict]:
        """A run of LaTeX text mode: mathematics kept verbatim, markup resolved."""
        spans: list[dict] = []
        buffer: list[str] = []

        def flush() -> None:
            if buffer:
                spans.extend(self._text(_latex_text("".join(buffer))))
                buffer.clear()

        index, length = 0, len(text)
        while index < length:
            character = text[index]
            if character == "$":
                end = index + 1
                while end < length and (text[end] != "$" or text[end - 1] == "\\"):
                    end += 1
                if end < length:
                    flush()
                    spans.append({"t": "math", "v": text[index:end + 1]})
                    index = end + 1
                    continue
            if character == "\\" and text.startswith("\\(", index):
                end = text.find("\\)", index)
                if end > 0:
                    # ``site/index.html`` declares \( \) an inline delimiter too, so this
                    # form goes through untouched rather than being rewritten into $…$.
                    flush()
                    spans.append({"t": "math", "v": text[index:end + 2]})
                    index = end + 2
                    continue
            if character == "\\":
                match = LATEX_COMMAND_RE.match(text, index)
                name = match.group(1) if match else None
                if name in LATEX_STYLE:
                    argument, end = _braced(text, match.end())
                    if end > match.end():
                        flush()
                        role = LATEX_STYLE[name]
                        inner = self.inline_latex(argument)
                        if role:
                            spans.append({"t": role, "spans": inner})
                        else:
                            spans.extend(inner)   # \text, \textup: a wrapper, not a style
                        index = end
                        continue
                elif name in ("ref", "eqref", "cref", "Cref"):
                    argument, end = _braced(text, match.end())
                    if end > match.end():
                        flush()
                        spans.append({"t": "ref", "v": argument})
                        index = end
                        continue
                elif name in ("cite", "citep", "citet"):
                    after = _bracketed(text, match.end())
                    argument, end = _braced(text, after)
                    if end > after:
                        flush()
                        spans.append({"t": "cite", "v": argument})
                        index = end
                        continue
                elif name in LATEX_DROPPED:
                    _argument, end = _braced(text, match.end())
                    index = max(end, match.end())
                    continue
            buffer.append(character)
            index += 1
        flush()
        return [span for span in spans if span]

    # --- blocks: LaTeX ----------------------------------------------------------------

    def statement(self, latex: str) -> list[dict]:
        """One claim environment's body, as blocks.

        The text is a verbatim slice of ``modules/``. What happens to it here is
        presentation and nothing else: display mathematics is normalized to the ``$$…$$``
        the page declares, ``\\item`` becomes a list, the anchor and the standing badge
        are dropped because both are already on the page, and every remaining character
        is kept.
        """
        return self._latex_blocks(latex)

    def _latex_blocks(self, text: str) -> list[dict]:
        blocks: list[dict] = []
        pending: list[str] = []

        def flush() -> None:
            joined = "".join(pending)
            pending.clear()
            for chunk in re.split(r"\n[ \t]*\n", joined):
                spans = self.inline_latex(chunk.strip())
                if any(span.get("v", "").strip() if span["t"] in ("text", "math", "code")
                       else True for span in spans):
                    blocks.append({"type": "paragraph", "spans": spans})

        index = 0
        while index < len(text):
            match = LATEX_BLOCK_RE.search(text, index)
            if match is None:
                pending.append(text[index:])
                break
            name = match.group(1)
            if name is None:                       # a bare \[ … \]
                end = text.find("\\]", match.end())
                stop = len(text) if end < 0 else end
                pending.append(text[index:match.start()])
                flush()
                blocks.append(_math_block(text[match.end():stop]))
                index = len(text) if end < 0 else end + 2
            elif name in DISPLAY_MATH_ENVIRONMENTS:
                body, after = _environment_body(text, name, match.end())
                pending.append(text[index:match.start()])
                flush()
                opener, closer = DISPLAY_MATH_ENVIRONMENTS[name]
                blocks.append(_math_block(f"{opener}{body}{closer}"))
                index = after
            elif name in LATEX_LIST_ENVIRONMENTS:
                body, after = _environment_body(text, name, match.end())
                pending.append(text[index:match.start()])
                flush()
                blocks.append({"type": "list",
                               "ordered": LATEX_LIST_ENVIRONMENTS[name],
                               "items": [self._latex_blocks(item)
                                         for item in _latex_items(body)]})
                index = after
            else:                                  # cases, pmatrix …: inline, not a block
                pending.append(text[index:match.end()])
                index = match.end()
        flush()
        return blocks

    # --- blocks: Markdown -------------------------------------------------------------

    def markdown(self, text: str) -> list[dict]:
        """A checkpoint body, as blocks. Front matter and HTML comments are already gone."""
        return self._markdown_blocks(text.replace("\r\n", "\n").split("\n"))

    def _markdown_blocks(self, lines: list[str]) -> list[dict]:
        blocks: list[dict] = []
        index, total = 0, len(lines)
        while index < total:
            line = lines[index]
            if not line.strip():
                index += 1
                continue

            fence = FENCE_RE.match(line)
            if fence:
                marker = fence.group(1)
                index += 1
                body: list[str] = []
                while index < total and not lines[index].strip().startswith(marker):
                    body.append(lines[index])
                    index += 1
                blocks.append({"type": "code", "language": fence.group(2) or None,
                               "text": "\n".join(body)})
                index += 1
                continue

            if line.strip().startswith("$$"):
                body, index = _display_math(lines, index)
                blocks.append(_math_block(body))
                continue

            heading = ATX_RE.match(line)
            if heading:
                blocks.append({"type": "heading", "level": len(heading.group(1)),
                               "spans": self.inline(heading.group(2))})
                index += 1
                continue

            if RULE_RE.match(line):
                blocks.append({"type": "rule"})
                index += 1
                continue

            if line.lstrip().startswith(">"):
                quoted: list[str] = []
                while index < total and (lines[index].lstrip().startswith(">")
                                         or (quoted and lines[index].strip())):
                    stripped = lines[index].lstrip()
                    quoted.append(stripped[1:].lstrip() if stripped.startswith(">")
                                  else stripped)
                    index += 1
                blocks.append({"type": "quote", "blocks": self._markdown_blocks(quoted)})
                continue

            if (line.lstrip().startswith("|") and index + 1 < total
                    and TABLE_RULE_RE.match(lines[index + 1])):
                table, index = self._table(lines, index)
                blocks.append(table)
                continue

            if LIST_MARKER_RE.match(line):
                listing, index = self._list(lines, index)
                blocks.append(listing)
                continue

            paragraph: list[str] = []
            while index < total and lines[index].strip():
                candidate = lines[index]
                if paragraph and (LIST_MARKER_RE.match(candidate)
                                  or ATX_RE.match(candidate)
                                  or FENCE_RE.match(candidate)
                                  or RULE_RE.match(candidate)
                                  or candidate.lstrip().startswith((">", "|", "$$"))):
                    break
                paragraph.append(candidate.strip())
                index += 1
            blocks.append({"type": "paragraph", "spans": self.inline(" ".join(paragraph))})
        return blocks

    def _table(self, lines: list[str], index: int) -> tuple[dict, int]:
        def cells(row: str) -> list[str]:
            return [cell.strip() for cell in row.strip().strip("|").split("|")]

        head = [self.inline(cell) for cell in cells(lines[index])]
        align = [("center" if cell.startswith(":") and cell.endswith(":")
                  else "right" if cell.endswith(":") else None)
                 for cell in cells(lines[index + 1])]
        index += 2
        rows = []
        while index < len(lines) and lines[index].lstrip().startswith("|"):
            rows.append([self.inline(cell) for cell in cells(lines[index])])
            index += 1
        return {"type": "table", "head": head, "align": align, "rows": rows}, index

    def _list(self, lines: list[str], index: int) -> tuple[dict, int]:
        """One list, and everything indented under it, as nested blocks."""
        first = LIST_MARKER_RE.match(lines[index])
        indent = len(first.group(1))
        ordered = first.group(3) is not None
        start = int(first.group(3)) if ordered else None
        items: list[list[str]] = []
        total = len(lines)
        while index < total:
            line = lines[index]
            if not line.strip():
                # A blank line continues the list only if something still belongs to it.
                lookahead = index + 1
                while lookahead < total and not lines[lookahead].strip():
                    lookahead += 1
                if lookahead >= total:
                    break
                following = LIST_MARKER_RE.match(lines[lookahead])
                deeper = len(lines[lookahead]) - len(lines[lookahead].lstrip()) > indent
                if not deeper and not (following and len(following.group(1)) == indent):
                    break
                if items:
                    items[-1].append("")
                index = lookahead
                continue
            marker = LIST_MARKER_RE.match(line)
            level = len(line) - len(line.lstrip())
            if marker and len(marker.group(1)) == indent:
                items.append([marker.group(4)])
            elif level > indent and items:
                items[-1].append(line[indent:])
            elif items and not marker and level >= indent:
                items[-1].append(line.strip())      # a lazy continuation line
            else:
                break
            index += 1
        blocks = {"type": "list", "ordered": ordered,
                  "items": [self._markdown_blocks(item) for item in items]}
        if ordered and start not in (None, 1):
            blocks["start"] = start
        return blocks, index


def _math_block(tex: str) -> dict:
    """Display mathematics, carrying the delimiters the page is configured for.

    The equation's own ``\\label`` comes out: it is a LaTeX cross-reference anchor, this
    page has no equation numbering to anchor, and left in it prints as an unknown command
    in the middle of the formula.
    """
    stripped = LATEX_LABEL_RE.sub("", tex).strip()
    return {"type": "math", "tex": f"$${stripped}$$"}


def _display_math(lines: list[str], index: int) -> tuple[str, int]:
    """A ``$$`` display block, opened and closed on their own lines or on one."""
    first = lines[index].strip()
    if first != "$$" and first.endswith("$$") and len(first) > 4:
        return first[2:-2], index + 1
    body = [first[2:]] if first != "$$" else []
    index += 1
    while index < len(lines):
        line = lines[index]
        index += 1
        if line.strip().endswith("$$"):
            body.append(line.strip()[:-2])
            break
        body.append(line)
    return "\n".join(body), index


def _environment_body(text: str, name: str, position: int) -> tuple[str, int]:
    """The body of ``\\begin{name}`` opened at ``position``, and the offset past its end.

    Counts nested opens of the *same* environment, so a list inside a list closes in the
    right place. An unclosed environment ends the slice, which is what the surrounding
    code already does with unbalanced prose.
    """
    start = _bracketed(text, position)
    depth, index = 1, start
    opener, closer = f"\\begin{{{name}}}", f"\\end{{{name}}}"
    while index < len(text):
        next_open = text.find(opener, index)
        next_close = text.find(closer, index)
        if next_close < 0:
            return text[start:], len(text)
        if 0 <= next_open < next_close:
            depth += 1
            index = next_open + len(opener)
            continue
        depth -= 1
        if depth == 0:
            return text[start:next_close], next_close + len(closer)
        index = next_close + len(closer)
    return text[start:], len(text)


def _latex_items(body: str) -> list[str]:
    """Split a list environment on its own ``\\item``s, ignoring any nested list's."""
    items: list[str] = []
    depth, cut = 0, None
    for match in re.finditer(r"\\begin\{([A-Za-z*]+)\}|\\end\{([A-Za-z*]+)\}|\\item\b",
                             body):
        if match.group(1) in LATEX_LIST_ENVIRONMENTS:
            depth += 1
        elif match.group(2) in LATEX_LIST_ENVIRONMENTS:
            depth = max(0, depth - 1)
        elif match.group(0).startswith("\\item") and depth == 0:
            if cut is not None:
                items.append(body[cut:match.start()])
            cut = _bracketed(body, match.end())
    if cut is not None:
        items.append(body[cut:])
    return [item for item in items if item.strip()]


# --------------------------------------------------------------------------------------
# provenance — which revision is on screen
# --------------------------------------------------------------------------------------

def _git(root: Path, *arguments: str) -> str | None:
    """One git query, or ``None`` when this is not a checkout and git cannot answer."""
    try:
        finished = subprocess.run(
            ["git", "-C", str(root), *arguments],
            capture_output=True, text=True, timeout=15, check=False,
        )
    except (OSError, subprocess.SubprocessError):  # pragma: no cover - environment guard
        return None
    return finished.stdout.strip() if finished.returncode == 0 else None


def provenance(root: Path, repository: str | None) -> dict:
    """What revision this build came from, so a reader can tell what they are looking at.

    Every page shows it. A site build that fails leaves the previous one online while the
    repository moves on, and a page that cannot say which commit it is displaying is
    indistinguishable from a page that is current (audit: *stale publication*).
    """
    root = root.resolve()
    commit = _git(root, "rev-parse", "HEAD")
    if repository is None:
        remote = _git(root, "remote", "get-url", "origin") or ""
        match = REMOTE_RE.search(remote)
        repository = f"{match.group(1)}/{match.group(2)}" if match else None
    return {
        "built_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "commit": commit,
        "short_commit": commit[:12] if commit else None,
        "dirty": bool(_git(root, "status", "--porcelain")),
        "branch": _git(root, "rev-parse", "--abbrev-ref", "HEAD"),
        "repository": repository,
        "source_prefix": _source_prefix(root),
    }


def _source_prefix(root: Path) -> str:
    """What to put in front of a repo-relative path to address it in the checkout.

    Every path in the report is relative to ``--root``, which is not always the checkout:
    ``--root example`` publishes the worked example, whose ``modules/00-overview.tex`` is
    ``example/modules/00-overview.tex`` to anyone following a link. Without this every
    source link on that build is a 404 that looks like a missing file rather than a
    mis-built site.
    """
    toplevel = _git(root, "rev-parse", "--show-toplevel")
    if not toplevel:
        return ""
    try:
        relative = root.relative_to(Path(toplevel).resolve())
    except ValueError:  # pragma: no cover - root outside its own checkout
        return ""
    return "" if relative == Path(".") else f"{relative.as_posix()}/"


# --------------------------------------------------------------------------------------
# derived data — the normalized artifact the frontend reads
# --------------------------------------------------------------------------------------

def _excerpt(path: Path, limit: int = 420) -> str | None:
    """The first prose paragraph of a dated record, for a card that must fit on screen.

    Deliberately an *excerpt* and labelled as one in the interface. Rendering a whole
    checkpoint would need a Markdown engine, which is a second renderer of repository
    prose and therefore a second place for it to be wrong; the record itself is one click
    away and GitHub already renders it.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):  # pragma: no cover - unreadable record
        return None
    text = HTML_COMMENT_RE.sub("", FRONT_MATTER_RE.sub("", text))
    for block in text.split("\n\n"):
        block = block.strip()
        if not block or HEADING_RE.match(block) or block.startswith(("---", "|", ">")):
            continue
        block = " ".join(block.split())
        return block if len(block) <= limit else block[:limit].rsplit(" ", 1)[0] + "…"
    return None


def _proof_record(proof: dict, archive: dict) -> dict:
    """One certification record, with what actually backs it.

    The two modes are *not* equally evidenced and the site must not draw them alike.
    ``mode: agent`` points at a persisted report whose front matter names distinct
    authors and reviewer, and that report is on disk. ``mode: human`` carries a name and
    no artifact — an honest record of a human acceptance, and honestly weaker evidence.
    """
    reference = proof.get("review")
    report = archive.get(reference) if isinstance(reference, str) else None
    record = {
        "artifact": proof.get("artifact"),
        "mode": proof.get("mode"),
        "review": reference,
        "accepted_by": proof.get("accepted_by"),
        "evidence": "persisted-review" if proof.get("mode") == "agent" else "attestation",
    }
    if report is not None:
        record["review_detail"] = {
            "date": report.get("date"),
            "verdict": report.get("verdict"),
            "reviewer": report.get("reviewer"),
            "authors": sorted(report.get("authors") or []),
        }
    return record


def _statement(anchor: dict) -> dict | None:
    """The manuscript statement behind one anchor, digested but not yet rendered.

    ``blocks`` is filled in later, once the identifier set the whole site can link is
    known; the digest is taken here, of the bytes as they sit in ``modules/``, because it
    is what ``statement_failures`` re-checks against a second, independent read.
    """
    statement = (anchor or {}).get("statement")
    if not isinstance(statement, str) or not statement.strip():
        return None
    return {
        "sha256": sha256(statement.encode("utf-8")).hexdigest(),
        "line": anchor.get("statement_line"),
        "blocks": [],
    }


def _claims(report: dict, archive: dict) -> dict[str, dict]:
    """Every ledger node, with both directions of every relation and its certification."""
    labels = report["labels"]
    claims: dict[str, dict] = {}
    for ledger in report["ledgers"]:
        nodes = ledger["nodes"]
        for nid, node in nodes.items():
            anchor = labels.get(nid) or {}
            edges = {field: [item for item in as_list(node.get(field)) if isinstance(item, str)]
                     for field, _class, _label, _gloss in RELATIONS}
            reverse = {
                name: sorted(other for other, candidate in nodes.items()
                             if nid in as_list(candidate.get(field)))
                for field, (name, _label) in REVERSE.items()
            }
            claims[nid] = {
                "id": nid,
                "program": ledger["program"],
                "kind": node.get("kind"),
                "status": node.get("status"),
                "provenance": node.get("provenance"),
                "import_class": node.get("import_class"),
                # The reader-facing projection of the four fields above, derived by the
                # same `checks.editorial` the manuscript badges come from. Exported, not
                # recomputed here: two implementations of one taxonomy is one too many.
                **standing_detail(node, nodes),
                # The heading a mathematician reads. It is the amsthm optional argument
                # of the claim's own environment, so the site and the manuscript name a
                # theorem the same way; `id` stays exported beside it, and stays visible
                # in the interface, because that is what cross-references are quoted by.
                "title": title_display(anchor.get("title"))[0],
                # Named `gloss`, not `statement`. The canonical text is the \label in
                # modules/ and nowhere else (CLAUDE.md constraint 7); this one line is
                # what `ledger-schema.md` calls a gloss, and the interface says so next
                # to every occurrence of it.
                "gloss": node.get("summary"),
                # The statement itself, sliced verbatim out of the manuscript on this
                # build and labelled on the page as a copy of it. This is the projection
                # constraint 7 permits and the gloss already is — the same permission the
                # problem brief uses to quote its target — not a second home: nothing
                # here is authored, `statement_failures` re-reads `modules/` and refuses
                # to publish a copy that no longer matches, and if the two ever disagree
                # the manuscript is right and this build is broken.
                "statement": _statement(anchor),
                "source": {"file": node.get("file") or anchor.get("file"),
                           "line": anchor.get("line"),
                           "environment": anchor.get("environment")},
                "references": [item for item in as_list(node.get("references"))
                               if isinstance(item, str)],
                "edges": edges,
                "reverse": reverse,
                "applicability_blocked_by": applicability_blockers(nid, nodes),
                "proofs": [_proof_record(proof, archive)
                           for proof in as_list(node.get("proofs"))
                           if isinstance(proof, dict)],
            }
    return claims


def _search(report: dict) -> dict | None:
    """The portfolio, with route ancestry derived rather than stored."""
    live = report.get("portfolio")
    if live is None:
        return None
    routes = {}
    for route_id, approach in live["approaches"].items():
        routes[route_id] = {
            "id": route_id,
            "family": approach.get("family"),
            "objective": (approach.get("objective") or "").strip() or None,
            "parent": approach.get("parent"),
            "state": approach.get("state"),
            "blocker": approach.get("blocker"),
            "reopen_if": (approach.get("reopen_if") or "").strip() or None,
            "related": [{"to": other, "relation": kind}
                        for other, kind in approach.get("_related", [])],
            "checkpoints": list(approach.get("_checkpoints", [])),
            "children": [],
        }
    for route_id, route in routes.items():
        parent = route["parent"]
        if isinstance(parent, str) and parent in routes:
            routes[parent]["children"].append(route_id)
    for route in routes.values():
        route["children"].sort()

    families = {}
    for family_id, family in live["families"].items():
        families[family_id] = {
            "id": family_id,
            "mechanism": (family.get("mechanism") or "").strip() or None,
            "state": family.get("state"),
            "closure_checkpoint": family.get("closure_checkpoint"),
            "reopen_if": (family.get("reopen_if") or "").strip() or None,
            "routes": sorted(route_id for route_id, route in routes.items()
                             if route["family"] == family_id),
        }
    return {"target": live["target"], "families": families, "routes": routes}


def _memory(report: dict) -> dict:
    """Durable evidence: checkpoints, candidates, promotions, reviews, audits, runs.

    Supersession is applied here rather than left to the reader. An append-only archive
    keeps provenance and supplies no current reading; naming the heir is what supplies it.
    """
    memory = report.get("checkpoints") or {}
    superseded = memory.get("superseded") or {}
    records = []
    slugs: set[str] = set()
    for record in memory.get("records") or []:
        records.append({
            "path": record["relative"],
            # A stable, readable URL for the record's own page. The dated filename is
            # already unique in one directory and is what every citation of the record
            # quotes, so it is the id — a counter is a fallback that should never fire.
            "slug": _unique_slug(Path(record["relative"]).stem, slugs),
            "date": record["date"],
            "outcome": record["outcome"],
            "approach": record["approach"],
            "nodes": list(record["nodes"]),
            "artifacts": list(record["artifacts"]),
            "candidates": [dict(item) for item in record["candidates"]],
            "retires": list(record["retires"]),
            "promotes": [dict(item) for item in record["promotes"]],
            "superseded_by": sorted(superseded.get(record["relative"], [])),
            "excerpt": _excerpt(record["path"]),
            # Filled in by `_render_records`, once every linkable id is known. The body
            # is fetched on demand rather than inlined: 92 rendered records are an order
            # of magnitude larger than everything else the site knows put together, and
            # a reader opening the front page should not pay for all of them.
            "title": None,
            "document": None,
        })
    records.sort(key=lambda item: (item["date"] or "", item["path"]), reverse=True)

    archive = report.get("archive") or {}
    superseded_audits = memory.get("superseded_audits") or set()
    reviews, audits = {}, {}
    for reference, metadata in archive.items():
        if metadata.get("type") == "proof-review":
            reviews[reference] = {
                "path": reference,
                "date": metadata.get("date"),
                "verdict": metadata.get("verdict"),
                "reviewer": metadata.get("reviewer"),
                "authors": sorted(metadata.get("authors") or []),
                "nodes": sorted(metadata.get("nodes") or []),
                "solutions": sorted(metadata.get("solutions") or []),
            }
        else:
            audits[reference] = {
                "path": reference,
                "date": metadata.get("date"),
                "superseded": reference in superseded_audits,
                "excerpt": _excerpt(metadata["path"]),
            }

    return {
        "checkpoints": records,
        "candidates": [{"id": entry["id"], "statement": entry["statement"],
                        "date": entry["date"], "source": entry["source"]}
                       for entry in report.get("candidates") or []],
        "promoted": {candidate: {"node": promotion["node"],
                                 "date": promotion["date"],
                                 "source": promotion["source"]}
                     for candidate, promotion in (memory.get("promoted") or {}).items()},
        "reviews": reviews,
        "audits": audits,
        "runs": [{"path": artifact["path"],
                  "target": artifact["target"],
                  "observations": artifact["records"]}
                 for artifact in report.get("artifacts") or []],
    }


def _unique_slug(stem: str, taken: set[str]) -> str:
    slug = re.sub(r"[^a-zA-Z0-9._-]+", "-", stem).strip("-") or "record"
    candidate, counter = slug, 2
    while candidate in taken:
        candidate, counter = f"{slug}-{counter}", counter + 1
    taken.add(candidate)
    return candidate


def _plain(spans: list[dict]) -> str:
    """A run of spans as bare text, for a title or a search haystack."""
    out = []
    for span in spans:
        if "spans" in span:
            out.append(_plain(span["spans"]))
        else:
            out.append(str(span.get("v", "")))
    return "".join(out).strip()


def _first_paragraph(blocks: list[dict], limit: int = 420, floor: int = 60) -> str | None:
    """The first paragraph of a rendered record worth putting on a card.

    A one-line ``Date:`` header is a paragraph and is not a summary, so a short opening
    line is skipped in favour of the first one with something in it. If nothing clears
    the bar the first paragraph is used anyway — an excerpt that is thin is better than a
    card that is blank.
    """
    paragraphs = [_plain(block["spans"]) for block in blocks
                  if block["type"] == "paragraph"]
    paragraphs = [" ".join(text.split()) for text in paragraphs if text.strip()]
    if not paragraphs:
        return None
    chosen = next((text for text in paragraphs if len(text) >= floor), paragraphs[0])
    return chosen if len(chosen) <= limit else chosen[:limit].rsplit(" ", 1)[0] + "…"


def _render_statements(claims: dict[str, dict], labels: dict[str, dict],
                       prose: Prose) -> None:
    """Turn each claim's verbatim slice into blocks, in place."""
    for nid, claim in claims.items():
        if claim.get("statement") is None:
            continue
        claim["statement"]["blocks"] = prose.statement(labels[nid]["statement"])


def _render_records(report: dict, memory: dict, prose: Prose) -> dict[str, dict]:
    """Render every durable record, and hand back the documents to be written.

    Rendering is derivation and rewrites nothing, so ``research/explorations/`` stays
    append-only (CLAUDE.md constraint 6). What changes is only who has to read raw
    Markdown: the reader, or this function.
    """
    sources = {record["relative"]: record["path"]
               for record in (report.get("checkpoints") or {}).get("records") or []}
    documents: dict[str, dict] = {}
    for record in memory["checkpoints"]:
        path = sources.get(record["path"])
        blocks: list[dict] = []
        if path is not None:
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError):  # pragma: no cover - unreadable record
                text = ""
            blocks = prose.markdown(
                HTML_COMMENT_RE.sub("", FRONT_MATTER_RE.sub("", text)))
        # The record's own opening heading is its title, and the page shows it as one:
        # keeping it in the body too would print it twice.
        if blocks and blocks[0]["type"] == "heading" and blocks[0]["level"] == 1:
            record["title"] = _plain(blocks[0]["spans"]) or None
            blocks = blocks[1:]
        # Now that the body is parsed, the excerpt can come from the first real
        # paragraph rather than from the first thing that looked like one. Records open
        # with a "Date:" line and with metadata bullets, and a card whose one line of
        # prose was "Date: 2026-08-30" told a reader nothing they could not see already.
        summary = _first_paragraph(blocks)
        if summary:
            record["excerpt"] = summary
        record["document"] = f"{RECORDS_DIRECTORY}/{record['slug']}.json"
        documents[record["slug"]] = {
            "path": record["path"], "slug": record["slug"],
            "title": record["title"], "blocks": blocks,
        }
    return documents


def statement_failures(root: Path, claims: dict[str, dict]) -> list[str]:
    """Re-read ``modules/`` and refuse a statement copy that no longer matches it.

    This is the guarantee that makes printing the statement legitimate rather than
    merely convenient. A build-time projection is only honest while it is *known* to
    agree with its source, so the agreement is checked and not assumed: the manuscript is
    read a second time, independently of the pass that produced the copy, and every
    digest must match. A claim whose anchor names a claim environment must yield a
    statement, and a statement must render to something.

    It is the ``reviewer``'s ``sync`` lens in miniature, mechanized and run on every
    build — the same relation constraint 7 requires of the problem brief's quoted target.
    On any failure ``build`` writes nothing at all: a page that shows a stale statement
    under a label saying it is the manuscript's is worse than one that shows none.
    """
    errors: list[str] = []
    fresh = manuscript_labels(root)
    for nid, claim in sorted(claims.items()):
        anchor = fresh.get(nid) or {}
        source = claim.get("source") or {}
        statement = claim.get("statement")
        if not source.get("environment"):
            continue  # a structural anchor states nothing; the core lane owns that rule
        if statement is None or not statement["blocks"]:
            errors.append(
                f"{nid}: no statement could be read from "
                f"\\begin{{{source['environment']}}} in {source.get('file')}; the site "
                "will not print a claim page with an empty statement"
            )
            continue
        current = anchor.get("statement")
        digest = sha256(current.encode("utf-8")).hexdigest() if current else None
        if digest != statement["sha256"]:
            errors.append(
                f"{nid}: the statement copy does not match {source.get('file')}; "
                "re-reading the manuscript produced different bytes. This is a build "
                "defect, not a manuscript one — the \\label is canonical"
            )
    return errors


# --------------------------------------------------------------------------------------
# layout — computed here, so the browser draws and does not decide
# --------------------------------------------------------------------------------------

#: Grid spacing in the abstract coordinate space the frontend scales. Layout is
#: *navigation only*: geometric proximity and centrality carry no mathematical meaning,
#: which is exactly why it is deterministic and computed once rather than simulated.
COLUMN, ROW = 260, 130


def _depth(node_id: str, edges: dict[str, list[str]], memo: dict[str, int],
           stack: frozenset[str] = frozenset()) -> int:
    """Longest path to a root of the proof DAG. The core lane guarantees acyclicity."""
    if node_id in memo:
        return memo[node_id]
    if node_id in stack:  # pragma: no cover - the core lane rejects cycles first
        return 0
    parents = [item for item in edges.get(node_id, []) if item in edges]
    depth = 0 if not parents else 1 + max(
        _depth(parent, edges, memo, stack | {node_id}) for parent in parents
    )
    memo[node_id] = depth
    return depth


def _place(layers: dict[int, list[str]]) -> dict[str, dict]:
    """Centre each layer over the widest one and hand back abstract coordinates."""
    widest = max((len(members) for members in layers.values()), default=1)
    positions: dict[str, dict] = {}
    for depth, members in layers.items():
        offset = (widest - len(members)) / 2
        for index, member in enumerate(sorted(members)):
            positions[member] = {"x": round((offset + index) * COLUMN),
                                 "y": round(depth * ROW)}
    return positions


def layout_claims(claims: dict[str, dict]) -> dict[str, dict]:
    """Layer the claim graph by proof depth: what a proof rests on sits below it.

    Only ``depends_on`` sets the layering. The other relations are drawn on top of it
    because they mean different things — an antecedent is not a dependency (constraint 8)
    — and letting them pull the layout would quietly assert that they were.
    """
    edges = {nid: [item for item in claim["edges"]["depends_on"] if item in claims]
             for nid, claim in claims.items()}
    memo: dict[str, int] = {}
    layers: dict[int, list[str]] = {}
    for nid in claims:
        layers.setdefault(_depth(nid, edges, memo), []).append(nid)
    return _place(layers)


def layout_search(search: dict | None) -> dict[str, dict]:
    """Lay routes out under their family, and children under their parent."""
    if search is None:
        return {}
    routes, positions = search["routes"], {}
    x = 0
    for family_id in sorted(search["families"]):
        family = search["families"][family_id]
        members = [route_id for route_id in family["routes"]]
        depth = {route_id: 0 for route_id in members}
        for _pass in range(len(members)):
            for route_id in members:
                parent = routes[route_id]["parent"]
                if parent in depth:
                    depth[route_id] = depth[parent] + 1
        rows: dict[int, list[str]] = {}
        for route_id in members:
            rows.setdefault(depth[route_id] + 1, []).append(route_id)
        width = max((len(row) for row in rows.values()), default=1)
        positions[family_id] = {"x": round((x + (width - 1) / 2) * COLUMN), "y": 0}
        for level, row in rows.items():
            for index, route_id in enumerate(sorted(row)):
                positions[route_id] = {"x": round((x + index) * COLUMN),
                                       "y": round(level * ROW)}
        x += width + 1
    return positions


# --------------------------------------------------------------------------------------
# assembly
# --------------------------------------------------------------------------------------

def export(report: dict, root: Path, *, repository: str | None = None,
           pdf_dir: Path | None = None, html_dir: Path | None = None,
           macros: dict | None = None) -> dict:
    """The whole derived artifact: everything the frontend is allowed to know."""
    archive = report.get("archive") or {}
    claims = _claims(report, archive)
    search = _search(report)
    memory = _memory(report)

    # Every identifier the site can resolve, so an id written in prose becomes a link to
    # the page that defines it. Derived from what is being published — the frontend never
    # sees a list of ids and this file never holds one.
    prose = Prose(
        ids=set(claims)
        | set((search or {"routes": {}})["routes"])
        | set((search or {"families": {}})["families"])
        | {candidate["id"] for candidate in memory["candidates"]},
        records={record["path"]: record["slug"] for record in memory["checkpoints"]},
    )
    _render_statements(claims, report["labels"], prose)
    records = _render_records(report, memory, prose)

    ledgers = report["ledgers"]
    program = ledgers[0] if ledgers else None
    brief = report.get("brief")
    target = None
    if search is not None:
        target = search["target"]
    elif brief is not None:
        target = brief.get("target")

    # Which routes a claim or a live candidate is holding up. Derived here because the
    # portfolio names a blocker and never restates it (constraint 11), so this is the
    # only place the two halves are allowed to meet.
    blocked: dict[str, list[str]] = {}
    for route_id, route in (search or {"routes": {}})["routes"].items():
        if isinstance(route.get("blocker"), str):
            blocked.setdefault(route["blocker"], []).append(route_id)
    for nid, claim in claims.items():
        claim["blocks_routes"] = sorted(blocked.get(nid, []))
        claim["checkpoints"] = sorted(record["path"] for record in memory["checkpoints"]
                                      if nid in record["nodes"])
    for candidate in memory["candidates"]:
        candidate["blocks_routes"] = sorted(blocked.get(candidate["id"], []))

    documents = _documents(root, claims, pdf_dir, html_dir)

    return {
        "generated": provenance(root, repository),
        "program": {
            "id": program["program"] if program else None,
            "scope": ((program["meta"] or {}).get("scope") or "").strip() or None
            if program else None,
            "target": target,
            "brief": "research/program/brief.md" if brief is not None else None,
            # A fresh clone is correct and not ready. The site says which it is looking at
            # rather than refusing to build, because refusing would make a correct
            # template's first deploy red.
            "instantiated": bool(claims) and bool(target),
        },
        "claims": claims,
        "search": search,
        "memory": memory,
        "documents": documents,
        # The rendered durable records, keyed by slug. `build` writes one file each under
        # `records/` and pops this key: they are far larger than the rest of the site put
        # together and only ever wanted one at a time.
        "records": records,
        # The seam for issue #13's generated MathJax macro table.
        #
        # Statements are LaTeX written against `preamble.tex`, whose ~60 macros — \R, \E,
        # \dd, \norm, \HS — MathJax does not know. Generating that table from the
        # preamble is the companion fix for the HTML manuscript, and building a second
        # extractor here would be the duplicate parser this file exists to avoid. So the
        # table arrives from outside: `--macros <file.json>` puts it here, `site.js`
        # installs it into `MathJax.tex.macros` before the first typeset, and until one is
        # attached the claim page says plainly that unexpanded macros are a missing build
        # input rather than a defect in the statement.
        "macros": macros or None,
        # Presentation order and selection, straight from the validated editorial guide.
        # It reaches the frontend through this file like everything else, so the four
        # route names and the featured ids stay out of site.js and the frontend still
        # owns no state of its own. `null` when the repository keeps no guide, which is
        # the ordinary case for a template and for the worked example.
        "guide": report.get("guide"),
        "vocabulary": {
            "relations": [{"field": field, "class": relation_class,
                           "label": label, "gloss": gloss}
                          for field, relation_class, label, gloss in RELATIONS],
            "reverse": {field: {"field": name, "label": label}
                        for field, (name, label) in REVERSE.items()},
        },
        "layout": {"claims": layout_claims(claims), "search": layout_search(search)},
    }


def _dossier_artifacts(claims: dict[str, dict]) -> list[str]:
    """Every dossier an active proof record names — the same set ``check.py dossiers``
    hands the LaTeX build, so the site attaches exactly what was compiled."""
    found: list[str] = []
    for claim in claims.values():
        for proof in claim["proofs"]:
            artifact = proof.get("artifact")
            if isinstance(artifact, str) and artifact not in found:
                found.append(artifact)
    return sorted(found)


def _documents(root: Path, claims: dict[str, dict], pdf_dir: Path | None,
               html_dir: Path | None) -> dict:
    """Locate the compiled manuscript and dossiers. Absent is a normal answer.

    Both forms are optional and independent. A site with neither still says everything
    it knows and links the LaTeX source; it simply cannot offer a rendered statement.
    Silently omitting mathematics is the failure to avoid, so a missing document is a
    missing *link*, never a missing claim.
    """
    def resolve(directory: Path | None, suffix: str) -> tuple[Path | None, dict[str, Path]]:
        if directory is None:
            return None, {}
        base = directory if directory.is_absolute() else root / directory
        manuscript = base / f"main.{suffix}"
        found = {}
        for artifact in _dossier_artifacts(claims):
            candidate = base / f"{Path(artifact).stem}.{suffix}"
            if candidate.is_file():
                found[artifact] = candidate
        return (manuscript if manuscript.is_file() else None), found

    pdf_manuscript, pdf_dossiers = resolve(pdf_dir, "pdf")
    html_manuscript, html_dossiers = resolve(html_dir, "html")
    return {
        "pdf": {"manuscript": pdf_manuscript, "dossiers": pdf_dossiers},
        "html": {"manuscript": html_manuscript, "dossiers": html_dossiers},
    }


def _attach(documents: dict, out: Path, form: str, extra_suffixes: tuple[str, ...] = ()
            ) -> dict:
    """Copy one form of compiled document into the site and hand back its URLs."""
    found = documents[form]
    directory = out / form
    # Clear first. A rebuild that only ever adds would keep the PDF of a dossier the
    # ledger has since dropped — unlinked, but present, and published.
    shutil.rmtree(directory, ignore_errors=True)
    if found["manuscript"] is None and not found["dossiers"]:
        return {"manuscript": None, "dossiers": {}}
    directory.mkdir(exist_ok=True)
    attached: dict = {"manuscript": None, "dossiers": {}}

    def copy(path: Path) -> str:
        shutil.copyfile(path, directory / path.name)
        # A TeX4ht conversion emits its stylesheet beside the page; without it the
        # manuscript renders as unstyled runs of text rather than as mathematics.
        for suffix in extra_suffixes:
            sidecar = path.with_suffix(suffix)
            if sidecar.is_file():
                shutil.copyfile(sidecar, directory / sidecar.name)
        return f"{form}/{path.name}"

    if found["manuscript"] is not None:
        attached["manuscript"] = copy(found["manuscript"])
    for artifact, path in sorted(found["dossiers"].items()):
        attached["dossiers"][artifact] = copy(path)
    return attached


def build(root: Path, out: Path, *, repository: str | None = None,
          pdf_dir: Path | None = None, html_dir: Path | None = None,
          frontend: Path | None = None, macros: dict | None = None
          ) -> tuple[dict, list[str]]:
    """Validate, export, and write the site. Returns the data and any blocking errors.

    A non-empty error list means nothing was written: a structurally invalid revision is
    not this repository's research state, and deploying it as though it were would make
    every trust signal on the page a guess. The manuscript statements it copies are held
    to the same rule by ``statement_failures``, and for the same reason.
    """
    report = analyze(root=root, configured_ledger=LEDGER_PATH)
    errors = failures(report, LANES)
    if errors:
        return {}, errors

    data = export(report, root, repository=repository, pdf_dir=pdf_dir,
                  html_dir=html_dir, macros=macros)
    stale = statement_failures(root, data["claims"])
    if stale:
        return {}, stale
    documents = data.pop("documents")
    records = data.pop("records")

    out.mkdir(parents=True, exist_ok=True)
    source = frontend if frontend is not None else Path(__file__).resolve().parent.parent / FRONTEND
    for asset in sorted(source.iterdir()):
        if asset.is_file() and asset.suffix in {".html", ".css", ".js"}:
            shutil.copyfile(asset, out / asset.name)

    data["documents"] = {
        "pdf": _attach(documents, out, "pdf"),
        "html": _attach(documents, out, "html", extra_suffixes=(".css",)),
    }

    # Cleared and rewritten, like the attached documents above: a rebuild that only ever
    # added would keep the page of a record that has since been renamed — unlinked,
    # unreachable, and published.
    rendered = out / RECORDS_DIRECTORY
    shutil.rmtree(rendered, ignore_errors=True)
    if records:
        rendered.mkdir(exist_ok=True)
        for slug, document in sorted(records.items()):
            (rendered / f"{slug}.json").write_text(
                json.dumps(document, indent=1, sort_keys=True, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )

    (out / "data.json").write_text(
        json.dumps(data, indent=1, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return data, []


def read_macros(path: Path) -> tuple[dict | None, list[str]]:
    """A generated MathJax macro table, or the reason it could not be used.

    The contract, so the generator and this file can be written apart: a JSON object
    mapping a macro name without its backslash to what ``MathJax.tex.macros`` accepts —
    a replacement string, or ``[replacement, argument-count]``. Nothing here parses
    ``preamble.tex``; producing the table is the HTML manuscript's job and duplicating it
    would be a second parser of the same file.
    """
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError) as exc:
        return None, [f"{path}: cannot read the MathJax macro table: {exc}"]
    if not isinstance(loaded, dict) or not all(isinstance(key, str) for key in loaded):
        return None, [f"{path}: want an object of macro name -> MathJax definition"]
    return loaded, []


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Render the repository's derived views as a static website",
        epilog="The site is a derived view, never a source. It refuses to build a "
               "repository that does not validate.",
    )
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1],
                        help="repository to publish (default: this script's own)")
    parser.add_argument("--out", type=Path, default=None,
                        help=f"output directory (default: <root>/{DEFAULT_OUT})")
    parser.add_argument("--pdf-dir", type=Path, default=None,
                        help="a LaTeX output directory whose PDFs should be attached, "
                             "e.g. 'build' after latexmk")
    parser.add_argument("--html-dir", type=Path, default=None,
                        help="a directory of make4ht output to attach, so a statement "
                             "can be read as HTML at its own anchor; see site/tex4ht.cfg")
    parser.add_argument("--macros", type=Path, default=None,
                        help="a generated MathJax macro table (JSON: macro name -> "
                             "definition), so statements copied from the manuscript "
                             "typeset the preamble's own macros")
    parser.add_argument("--repository", default=None,
                        help="owner/name for source and contribution links "
                             "(default: inferred from the 'origin' remote)")
    parser.add_argument("--serve", nargs="?", type=int, const=8000, default=None,
                        metavar="PORT", help="after building, serve the site locally")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    out = (args.out if args.out is not None else root / DEFAULT_OUT).resolve()
    macros, errors = (None, [])
    if args.macros is not None:
        macros, errors = read_macros(args.macros)
    data = {}
    if not errors:
        data, errors = build(root, out, repository=args.repository, pdf_dir=args.pdf_dir,
                             html_dir=args.html_dir, macros=macros)
    if errors:
        for error in errors:
            print("FAIL", error, file=sys.stderr)
        print(f"\n{len(errors)} error(s): refusing to publish a revision that does not "
              "validate.\nFix them, or run 'python3 scripts/check.py' to see them in "
              "context.", file=sys.stderr)
        return 1

    generated = data["generated"]
    revision = generated["short_commit"] or "unknown revision"
    print(f"wrote {out}{' (working tree is dirty)' if generated['dirty'] else ''}")
    print(f"  {len(data['claims'])} claim(s), "
          f"{len((data['search'] or {'routes': {}})['routes'])} approach(es), "
          f"{len(data['memory']['checkpoints'])} checkpoint(s) — at {revision}")
    if data["claims"] and not data["macros"]:
        print("  note: no MathJax macro table is attached, so a statement written with "
              "preamble.tex's\n        own macros shows them unexpanded. Pass --macros "
              "<file.json> to fix that.")
    if not data["program"]["instantiated"]:
        print("  note: this repository is still an uninstantiated template; the site "
              "says so.\n        'python3 scripts/check.py ready' lists what is missing.")

    if args.serve is not None:
        from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
        from functools import partial
        handler = partial(SimpleHTTPRequestHandler, directory=str(out))
        with ThreadingHTTPServer(("127.0.0.1", args.serve), handler) as server:
            print(f"\nserving http://127.0.0.1:{args.serve}/ — Ctrl-C to stop")
            try:
                server.serve_forever()
            except KeyboardInterrupt:
                print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
