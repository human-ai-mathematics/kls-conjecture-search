r"""Carrying ``preamble.tex``'s macros across to the browser, and proving they arrived.

The PDF and the HTML conversion read the same manuscript, but only the PDF reads the
same *preamble*. ``make4ht``'s ``mathjax`` mode hands mathematics to MathJax verbatim and
emits a two-field config of its own, so every ``\newcommand`` this repository defines
arrived at the reader as literal red source mid-formula --- ``\Aop``, ``\norm``,
``\inner``, ``\eps`` --- inside otherwise correctly typeset displays. ``latexmk`` and
``scripts/check.py`` are both blind to it, because nothing they read is wrong.

This module closes that gap the same way ``editorial.py`` closes the status-badge gap:
**as a derivation, never as a second list**.

    preamble.tex  ->  MathJax tex.macros  ->  a generated block in site/tex4ht.cfg

The block is written by ``python3 scripts/new.py mathjax`` and checked here for drift, so
a macro added to the preamble and not carried across fails ``scripts/check.py`` rather
than reaching a reader as red text. A hand-transcribed macro list in the config would be
a second source of truth, and the objection to one is not that it is ugly but that it
drifts; being generated and verified is what answers that mechanically.

Why the block lives *inside* ``site/tex4ht.cfg`` rather than in a file beside it: the
config is passed to ``make4ht`` by an explicit path, but anything it ``\input``s is
resolved by kpathsea from the current directory --- and the dossier builds run
``make4ht`` from each dossier's own directory (docs/PUBLISHING-THE-SITE.md §2). One
self-contained file is the only form that works from every working directory the
documented pipeline uses.

Two things are checked, and they are deliberately different checks:

* :func:`check` --- structural, needs no build. Does the generated block still agree with
  ``preamble.tex``? Runs in the ``editorial`` lane, and contributes nothing to a tree that
  has no ``site/tex4ht.cfg``.
* :func:`audit` --- the acceptance test, and it needs a *built* artifact. Every control
  sequence appearing in a built page's mathematics that ``preamble.tex`` defines must be
  provided by that page's own MathJax configuration, and no ``\``-prefixed token may
  appear in the page's prose. It is reached by ``python3 scripts/check.py html`` and by
  ``scripts/check.sh``, which skips it when nothing has been built --- never by the
  default ``check``, because a validator whose result depends on an untracked build
  artifact is a validator that fails for the wrong reason.

What :func:`audit` cannot do is worth stating plainly: it does not own a copy of
MathJax's own command dictionary, so a *standard* command MathJax happens not to support
would pass it. What it does own is the exact defect class of the bug it was written for
--- this manuscript's own macros failing to reach the page --- and that it decides
completely.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from .ledger import strip_comments

#: The single source of truth. Read, never written.
PREAMBLE_PATH = "preamble.tex"

#: The generated block's home. Hand-authored elsewhere in the file; see the module
#: docstring for why the block is inlined rather than ``\input``.
CONFIG_PATH = "site/tex4ht.cfg"

BEGIN_MARKER = "%%% BEGIN GENERATED --- MathJax macro transport"
END_MARKER = "%%% END GENERATED --- MathJax macro transport"

REGENERATE = "run 'python3 scripts/new.py mathjax'"

#: ``\newcommand``, ``\renewcommand`` and ``\DeclareMathOperator``, each with its
#: starred form. Nothing else defines a macro in this repository's preamble, and a form
#: that is not recognised is reported as skipped rather than guessed at.
DEFINITION_RE = re.compile(
    r"\\(newcommand|renewcommand|providecommand|DeclareMathOperator)(\*)?"
)

#: A MathJax ``tex.macros`` key. MathJax looks macros up by control-word name, so a name
#: LaTeX accepts but MathJax cannot address (``\l@klspart``) is not transportable.
MACRO_NAME_RE = re.compile(r"^[A-Za-z]+$")

#: Control sequences that make a definition a *document* macro rather than a mathematical
#: one. This is a refusal list, not an approval list: a body containing something here is
#: skipped and reported, and anything unrecognised is emitted, because MathJax's own
#: command set is far larger than any list kept here could be and guessing against it
#: would reject correct mathematics. Every entry is a construct with no meaning inside a
#: MathJax expression.
NON_MATH_COMMANDS = frozenset({
    # conditionals, expansion control and the token primitives
    "if", "ifnum", "ifdim", "ifcase", "ifcsname", "ifdefined", "ifx", "ifmmode",
    "else", "or", "fi", "csname", "endcsname", "expandafter", "noexpand", "string",
    "meaning", "the", "number", "romannumeral", "relax",
    # definition and allocation
    "def", "edef", "gdef", "xdef", "let", "newcommand", "renewcommand",
    "providecommand", "newenvironment", "newtheorem", "newcounter", "newlength",
    "newsavebox", "setcounter", "addtocounter", "stepcounter", "value",
    "DeclareMathOperator", "makeatletter", "makeatother",
    # mode, boxes, glue and penalties
    "par", "noindent", "indent", "vskip", "hskip", "vspace", "hspace", "addvspace",
    "penalty", "addpenalty", "nobreak", "break", "hfill", "hfil", "vfill", "hss",
    "vss", "leavevmode", "unskip", "ignorespaces", "hbox", "vbox", "mbox", "makebox",
    "framebox", "parbox", "raisebox", "rule", "strut", "begingroup", "endgroup",
    "bgroup", "egroup", "baselineskip", "parindent", "parskip", "rightskip",
    "leftskip", "parfillskip", "textwidth", "linewidth", "columnwidth", "textheight",
    "setlength", "addtolength", "settowidth",
    # font and colour declarations, which are states rather than expressions
    "bfseries", "itshape", "slshape", "scshape", "upshape", "mdseries", "rmfamily",
    "sffamily", "ttfamily", "normalfont", "tiny", "scriptsize", "footnotesize",
    "small", "normalsize", "large", "Large", "LARGE", "huge", "Huge", "em",
    "color", "textcolor", "colorbox", "fcolorbox",
    # document structure, cross-referencing and input/output
    "input", "include", "usepackage", "documentclass", "part", "chapter", "section",
    "subsection", "subsubsection", "paragraph", "label", "ref", "pageref", "eqref",
    "cite", "footnote", "caption", "item", "addcontentsline", "contentsline",
    "phantomsection", "hypertarget", "hyperlink", "url", "href", "index", "verb",
    "protect", "AtBeginDocument", "PackageWarning", "PackageError", "ClassWarning",
    "typeout", "message", "write", "immediate", "openout", "closeout",
})

#: Characters a macro body may not contain if it is to survive the trip through a TeX4ht
#: configuration into a JavaScript string literal. ``%`` would comment out the rest of
#: the generated line; ``$``, ``&`` and ``~`` carry catcodes the config cannot restore
#: locally; ``^^`` is TeX's character-code escape and is consumed while the file is read.
UNTRANSPORTABLE = ("%", "$", "&", "~", "^^", "\\ ", "\\\n", "\\\t")


@dataclass(frozen=True)
class Macro:
    """One transportable definition, in the shape MathJax's ``tex.macros`` takes."""

    name: str
    body: str
    arity: int = 0
    default: str | None = None

    def as_entry(self) -> object:
        """``"body"``, ``["body", n]`` or ``["body", n, "default"]``."""
        if self.default is not None:
            return [self.body, self.arity, self.default]
        if self.arity:
            return [self.body, self.arity]
        return self.body


def _skip_spaces(text: str, index: int) -> int:
    while index < len(text) and text[index] in " \t\r\n":
        index += 1
    return index


def _delimited(text: str, index: int, opening: str, closing: str) -> tuple[str, int] | None:
    """Read one balanced ``{...}`` or ``[...]`` group starting at ``index``.

    Returns the content and the index just past the closing delimiter, or ``None`` when
    ``index`` is not the opening delimiter or the group never closes. A backslash escapes
    the character after it, so ``\\{`` does not open a group.
    """
    if index >= len(text) or text[index] != opening:
        return None
    depth = 0
    position = index
    while position < len(text):
        character = text[position]
        if character == "\\":
            position += 2
            continue
        if character == opening:
            depth += 1
        elif character == closing:
            depth -= 1
            if depth == 0:
                return text[index + 1:position], position + 1
        position += 1
    return None


def _read_name(text: str, index: int) -> tuple[str, int] | None:
    """The defined control sequence, written either ``{\\name}`` or bare ``\\name``."""
    index = _skip_spaces(text, index)
    group = _delimited(text, index, "{", "}")
    if group is not None:
        inner, after = group
        inner = inner.strip()
        if inner.startswith("\\") and inner[1:]:
            return inner[1:], after
        return None
    match = re.compile(r"\\([A-Za-z@]+)").match(text, index)
    if match is None:
        return None
    return match.group(1), match.end()


def _untransportable(body: str) -> str | None:
    for token in UNTRANSPORTABLE:
        if token in body:
            display = token.replace("\n", "\\n").replace("\t", "\\t")
            return f"body contains '{display}', which a TeX4ht config cannot transport"
    if body.count("{") != body.count("}"):
        return "body has unbalanced braces"
    return None


def _non_math(body: str) -> str | None:
    for name in re.findall(r"\\([A-Za-z@]+)", body):
        if "@" in name:
            return f"body uses the internal command '\\{name}'"
        if name in NON_MATH_COMMANDS:
            return f"body uses the LaTeX-only command '\\{name}'"
    return None


def parse(text: str) -> tuple[list[Macro], list[tuple[str, str]]]:
    """Every macro definition in a preamble, split into transportable and skipped.

    Returns ``(macros, skipped)`` where ``skipped`` pairs a name with the reason it was
    left out. Later definitions of the same name win, which is what ``\\renewcommand``
    means; the emitted order follows first definition, so the generated block has a
    stable diff.
    """
    source = strip_comments(text)
    macros: dict[str, Macro] = {}
    skipped: dict[str, str] = {}
    position = 0
    while True:
        match = DEFINITION_RE.search(source, position)
        if match is None:
            break
        position = match.end()
        operator = match.group(1) == "DeclareMathOperator"
        starred = match.group(2) == "*"
        read = _read_name(source, position)
        if read is None:
            continue
        name, position = read
        arity, default = 0, None
        if not operator:
            for slot in ("arity", "default"):
                bracket = _delimited(source, _skip_spaces(source, position), "[", "]")
                if bracket is None:
                    break
                value, position = bracket
                if slot == "arity":
                    try:
                        arity = int(value.strip())
                    except ValueError:
                        arity = 0
                else:
                    default = value.strip()
        group = _delimited(source, _skip_spaces(source, position), "{", "}")
        if group is None:
            skipped[name] = "definition body could not be read"
            continue
        body, position = group
        body = " ".join(body.split())
        if operator:
            body = f"\\operatorname{'*' if starred else ''}{{{body}}}"

        reason = None
        if not MACRO_NAME_RE.match(name):
            reason = "name is not a MathJax macro name ([A-Za-z]+)"
        elif not body:
            reason = "definition body is empty"
        else:
            reason = _untransportable(body) or _non_math(body)
        if reason is not None:
            skipped[name] = reason
            macros.pop(name, None)
            continue
        skipped.pop(name, None)
        macros[name] = Macro(name, body, arity, default)
    return list(macros.values()), sorted(skipped.items())


def parse_preamble(root: Path) -> tuple[list[Macro], list[tuple[str, str]]]:
    """:func:`parse` applied to a tree's ``preamble.tex``; empty when it has none."""
    path = root / PREAMBLE_PATH
    if not path.is_file():
        return [], []
    return parse(path.read_text(encoding="utf-8"))


def _tex_literal(text: str) -> str:
    r"""One JavaScript string body, written as TeX4ht configuration source.

    Two escapings compose here and both are load-bearing. The value MathJax must receive
    holds single backslashes, so the *JavaScript* literal needs them doubled; and a
    backslash cannot be typed into a TeX file as itself, so each one is written
    ``\harnessbs`` followed by a space TeX removes when it ends the control word. That
    trailing space is the reason a body containing a control space is refused above: the
    space TeX eats there would be one the reader was meant to see.
    """
    out = []
    for character in text:
        if character == "\\":
            out.append("\\harnessbs \\harnessbs ")
        elif character == "#":
            out.append("\\harnesshash ")
        else:
            out.append(character)
    return "".join(out)


def _entry(macro: Macro) -> str:
    """One ``"name": value`` line of the emitted object, in config source."""
    value = macro.as_entry()
    if isinstance(value, str):
        rendered = f'"{_tex_literal(value)}"'
    else:
        parts = [f'"{_tex_literal(value[0])}"', str(value[1])]
        if len(value) > 2:
            parts.append(f'"{_tex_literal(value[2])}"')
        rendered = "[" + ", ".join(parts) + "]"
    return f'"{macro.name}": {rendered}'


#: The head script, split so the generated block reads as prose rather than one long
#: line. Newlines inside a ``\HCode`` argument become single spaces, which is why every
#: JavaScript comment here is ``/* */`` and no line ever breaks inside a string literal.
_PROLOGUE = (
    "<script>/* MathJax macro transport --- generated from preamble.tex. */"
    " (function () { var mj = window.MathJax = window.MathJax || {};"
    " var tex = mj.tex = mj.tex || {};"
    " var macros = tex.macros = tex.macros || {};"
    " var derived = {"
)
_EPILOGUE = (
    "}; for (var name in derived) { if (!(name in macros))"
    " { macros[name] = derived[name]; } } }());</script>"
)


def render(macros: list[Macro], skipped: list[tuple[str, str]]) -> str:
    r"""The exact intended contents of the generated block in ``site/tex4ht.cfg``.

    ``\Configure{@HEAD}`` lands after the config ``make4ht``'s ``mathjax`` mode writes,
    which is why this merges into ``window.MathJax`` instead of assigning it: the mode's
    ``tags: "ams"`` has to survive, and so does anything a later mode adds.
    """
    lines = [
        BEGIN_MARKER,
        "%",
        "% Every macro preamble.tex defines, carried to MathJax so the HTML conversion",
        "% typesets the manuscript's own notation instead of printing it as source.",
        "% Derived by scripts/checks/mathjax.py. Do not edit by hand; regenerate with",
        "%",
        "%     python3 scripts/new.py mathjax",
        "%",
        "% scripts/check.py --lane editorial fails if this block and preamble.tex",
        "% disagree, so a macro added to the manuscript cannot silently stop rendering.",
        "%",
    ]
    if skipped:
        lines.append(f"% Skipped, and why ({len(skipped)} of "
                     f"{len(skipped) + len(macros)} definitions):")
        for name, reason in skipped:
            lines.append(f"%   \\{name}: {reason}")
        lines.append("%")
    lines.extend([
        "% \\harnessbs and \\harnesshash write the one backslash and the one hash that",
        "% cannot be typed literally here. A JavaScript string needs its backslashes",
        "% doubled, so each is written twice.",
        "\\makeatletter",
        "\\edef\\harnessbs{\\expandafter\\@gobble\\string\\\\}",
        "\\edef\\harnesshash{\\string#}",
        "\\makeatother",
        "",
        "\\Configure{@HEAD}{\\HCode{" + _PROLOGUE,
    ])
    for index, macro in enumerate(macros):
        comma = "," if index + 1 < len(macros) else ""
        lines.append(_entry(macro) + comma)
    lines.append(_EPILOGUE + "}}")
    lines.append(END_MARKER)
    return "\n".join(lines) + "\n"


def _split(text: str) -> tuple[str, str, str] | None:
    """``(before, block, after)`` around the generated markers, or ``None`` if absent."""
    start = text.find(BEGIN_MARKER)
    end = text.find(END_MARKER)
    if start < 0 or end < start:
        return None
    end += len(END_MARKER)
    if end < len(text) and text[end] == "\n":
        end += 1
    return text[:start], text[start:end], text[end:]


def write(root: Path) -> tuple[str, list[Macro], list[tuple[str, str]]]:
    """Regenerate the block in ``site/tex4ht.cfg``; return the path and what it carries.

    Appends the block when the config has none yet, so a fork that adopts this file gets
    it in the right place without hand-editing.
    """
    path = root / CONFIG_PATH
    macros, skipped = parse_preamble(root)
    text = path.read_text(encoding="utf-8")
    block = render(macros, skipped)
    split = _split(text)
    if split is None:
        anchor = text.find("\\begin{document}")
        head, tail = (text[:anchor], text[anchor:]) if anchor >= 0 else (text, "")
        text = head.rstrip("\n") + "\n\n" + block + "\n" + tail
    else:
        text = split[0] + block + split[2]
    path.write_text(text, encoding="utf-8")
    return CONFIG_PATH, macros, skipped


def check(root: Path, errors: list[str]) -> None:
    """The generated block agrees with ``preamble.tex``, byte for byte.

    Inert on a tree with no ``site/tex4ht.cfg``: a repository that publishes no site has
    no macro transport to keep honest, which is the same activation rule every other lane
    follows.
    """
    path = root / CONFIG_PATH
    if not path.is_file():
        return
    if not (root / PREAMBLE_PATH).is_file():
        return
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:  # pragma: no cover - environment guard
        errors.append(f"{CONFIG_PATH}: cannot read: {exc}")
        return
    macros, skipped = parse_preamble(root)
    split = _split(text)
    if split is None:
        errors.append(
            f"{CONFIG_PATH}: no generated MathJax macro block; without it the HTML "
            f"conversion prints preamble.tex's macros as source — {REGENERATE}"
        )
        return
    if split[1] != render(macros, skipped):
        errors.append(
            f"{CONFIG_PATH}: the generated MathJax macro block disagrees with "
            f"{PREAMBLE_PATH} — {REGENERATE}"
        )


# --- the acceptance test, over built HTML ------------------------------------------

#: Mathematics as ``make4ht``'s ``mathjax`` mode emits it: ``\(...\)`` inline,
#: ``\[...\]`` unnumbered, and a numbered display left as its own ``amsmath``
#: environment for MathJax to number under ``tags: "ams"``. The environment form is what
#: an early version of this audit missed, and missing it turned every numbered equation
#: in the manuscript into a false report of leaked source.
MATH_RE = re.compile(
    r"\\\(.*?\\\)"
    r"|\\\[.*?\\\]"
    r"|\\begin\s*\{([A-Za-z]+\*?)\}.*?\\end\s*\{\1\}",
    re.S,
)

#: ``window.MathJax``'s macro table as :func:`render` writes it into the page. The page is
#: read back rather than trusted, because what is being audited is the artifact.
DERIVED_RE = re.compile(r"var derived = \{(.*?)\}; for \(var name in derived\)", re.S)

CONTROL_SEQUENCE_RE = re.compile(r"\\([A-Za-z]+)")

#: Everything that is not prose: script and style bodies, comments, and tag markup. A
#: backslash inside any of these is machinery, not something a reader is shown.
NON_PROSE_RE = re.compile(
    r"<script\b.*?</script>|<style\b.*?</style>|<!--.*?-->|<[^>]*>", re.S | re.I
)


def page_macros(html: str) -> set[str]:
    """The macro names a built page's own MathJax configuration provides."""
    match = DERIVED_RE.search(html)
    if match is None:
        return set()
    return set(re.findall(r'"([A-Za-z]+)":', match.group(1)))


def audit_page(html: str, defined: set[str]) -> list[str]:
    """Findings for one built page. Empty means the page renders its own notation.

    Two failures, and they are the two ways a backslash reaches a reader. A control
    sequence used in mathematics that ``preamble.tex`` defines and the page's config does
    not carry is the defect this module exists for. A backslash in prose is the same
    defect one stage further on, where not even MathJax will look at it.
    """
    findings: list[str] = []
    used: dict[str, int] = {}
    for match in MATH_RE.finditer(html):
        for name in CONTROL_SEQUENCE_RE.findall(match.group(0)):
            used[name] = used.get(name, 0) + 1
    carried = page_macros(html)
    missing = sorted(name for name in used if name in defined and name not in carried)
    for name in missing:
        findings.append(
            f"\\{name} is used {used[name]}x in mathematics and defined in "
            f"{PREAMBLE_PATH}, but the page's MathJax config does not carry it"
        )
    prose = NON_PROSE_RE.sub(" ", MATH_RE.sub(" ", html))
    leaked = sorted(set(CONTROL_SEQUENCE_RE.findall(prose)))
    if leaked:
        findings.append(
            "a backslash-prefixed token survives outside mathematics: "
            + ", ".join(f"\\{name}" for name in leaked[:8])
            + (f" (+{len(leaked) - 8} more)" if len(leaked) > 8 else "")
        )
    return findings


def audit(root: Path, html_dir: Path) -> tuple[dict[str, list[str]], list[str]]:
    """Audit every built page under ``html_dir``.

    Returns ``(findings by page, pages read)``. An absent directory is not a failure and
    not a pass: the caller reports it as unbuilt, which is what ``scripts/check.sh``'s
    "all *available* checks passed" already means.
    """
    macros, skipped = parse_preamble(root)
    # A skipped macro counts as defined here on purpose: if one is nonetheless used in
    # mathematics, the reader sees red source, and refusing to carry it is the cause.
    defined = {macro.name for macro in macros} | {name for name, _ in skipped}
    findings: dict[str, list[str]] = {}
    read: list[str] = []
    if not html_dir.is_dir():
        return findings, read
    for path in sorted(html_dir.glob("*.html")):
        read.append(path.name)
        try:
            html = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:  # pragma: no cover - environment guard
            findings[path.name] = [f"cannot read: {exc}"]
            continue
        page = audit_page(html, defined)
        if page:
            findings[path.name] = page
    return findings, read


#: Where docs/PUBLISHING-THE-SITE.md §2 puts the conversion, relative to the tree.
DEFAULT_HTML_DIR = "build/html"

UNBUILT = ("nothing to audit — build the conversion first "
           "(docs/PUBLISHING-THE-SITE.md §2)")


def report(root: Path, html_dir: Path, expected: list[str]) -> bool:
    """Print the acceptance audit of a built conversion. ``True`` when it passes.

    An unbuilt tree is neither a pass nor a failure: it is named as unbuilt and returns
    ``True``, because a checkout that has never run ``make4ht`` has no artifact to be
    wrong about, and failing there would make a correct fresh clone red. ``scripts/check.sh``
    is the caller that turns that into "all *available* checks passed".
    """
    findings, read = audit(root, html_dir)
    if not read:
        print(f"{html_dir}: {UNBUILT}")
        return True
    for name in read:
        problems = findings.get(name)
        if problems:
            for problem in problems:
                print(f"FAIL {name}: {problem}")
        else:
            print(f"ok   {name}")
    for path in expected:
        if Path(path).with_suffix(".html").name not in read:
            print(f"     {path}: not converted; this audit says nothing about it")
    return not findings
