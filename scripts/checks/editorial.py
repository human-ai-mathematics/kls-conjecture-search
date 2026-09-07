"""Reader-facing epistemic standing, derived from the ledger and nowhere else.

The manuscript is a research record as well as an exposition, so a reader meets a
published theorem, an unreviewed preprint, an internally certified result and an open
question inside one section, set in the same type. ``research/program/ledger.yaml``
already distinguishes all four; what it did not do was put the distinction next to the
statement, where a mathematician reads it.

This module closes that gap **as a projection**, never as a second taxonomy:

    status + provenance + import_class + proofs[] + assumes  ->  one short label

Nothing new is stored. ``status.tex`` is a generated artifact, written by
``python3 scripts/new.py status`` and checked here for drift exactly the way
``roles.py`` checks the generated agent files: if the ledger and the badge on the page
can disagree, they eventually will, and the prettier one wins the argument.

Two rules are the whole contract, and both are enforced below:

1. ``status.tex`` is byte-identical to what the current ledger renders.
2. Every claim environment in ``modules/`` carries exactly one ``\\klsstatus`` whose
   argument is the ``\\label`` of that same claim.

Rule 2 exists because ``\\klsstatus`` takes the node id explicitly rather than reading
the enclosing label --- LaTeX cannot do the latter reliably, and a silent mismatch would
put one claim's standing on another claim's statement.
"""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

from . import views
from .common import as_list
from .ledger import (
    CLAIM_ENVIRONMENTS,
    ENVIRONMENT_RE,
    LABEL_RE,
    SELF_LABELLING_ENVIRONMENTS,
    applicability_blockers,
    strip_comments,
)

#: The generated file, repo-relative. It sits beside ``preamble.tex`` because that is
#: what inputs it, and outside ``modules/`` because everything under ``modules/`` is
#: scanned for anchors and this file holds none.
STATUS_PATH = "status.tex"

REGENERATE = "run 'python3 scripts/new.py status'"

STATUS_MACRO_RE = re.compile(r"\\klsstatus\{([^}]+)\}")

#: The reader-facing vocabulary. Short, because it is set in small type beside a
#: statement; and closed, because a label nobody can define precisely is a label nobody
#: can trust. Every value here is derived, never stored.
PUBLISHED = "Published result"
PREPRINT_REVIEWED = "Reviewed preprint"
PREPRINT_UNREVIEWED = "Unreviewed preprint"
CERTIFIED = "Certified here"
ATTESTED = "Proved here, attested"
PROVED_ELSEWHERE = "Proved"
REFUTED = "Refuted"
DEFINED = "Definition"

#: Open is not one thing. The schema's `kind` already says which, and a reader who is
#: told "open question" about an assumption learns the wrong thing about it: an open
#: premise is something an argument *rests on*, an advisory barrier is something that
#: guides work without fencing a claim (CLAUDE.md constraint 5), and an open conjecture
#: is a target. Same field, three different warnings.
OPEN_BY_KIND = {
    "assumption": "Open premise",
    "obstruction": "Advisory barrier",
    "conjecture": "Open conjecture",
    "question": "Open question",
}
OPEN_DEFAULT = "Open"


def _open_label(node: dict) -> str:
    return OPEN_BY_KIND.get(node.get("kind"), OPEN_DEFAULT)

#: Appended, never substituted. A proved implication with an open antecedent is still
#: proved (CLAUDE.md constraint 8) and is still not progress on the target (P2); the
#: label has to say both things at once, so it says the first and then qualifies it.
CONDITIONAL = "conditional"


def standing(node: dict, nodes: dict[str, dict]) -> str:
    """The one-line reader-facing standing of ``node``.

    Order matters. ``refuted`` and ``defined`` are terminal and answer first. Provenance
    answers next, because "where did this come from" outranks "what did we do with it"
    for a reader deciding how much to trust a line. Only then does certification, which
    is the one thing this repository can speak to with authority.
    """
    status = node.get("status")
    if status == "refuted":
        return REFUTED
    if status == "defined":
        return DEFINED

    if node.get("provenance") == "literature":
        base = {
            "published": PUBLISHED,
            "preprint-reviewed": PREPRINT_REVIEWED,
            "preprint-unreviewed": PREPRINT_UNREVIEWED,
        }.get(node.get("import_class"),
              PROVED_ELSEWHERE if status == "proved" else _open_label(node))
    elif status == "proved":
        modes = {proof.get("mode") for proof in as_list(node.get("proofs"))
                 if isinstance(proof, dict)}
        base = CERTIFIED if "agent" in modes else (ATTESTED if modes else PROVED_ELSEWHERE)
    else:
        base = _open_label(node)

    # An unreviewed preprint is `open` by schema however plausible it is, so the
    # qualifier below must not be reached for it; only a *proved* node can be
    # applicability-blocked in the sense that matters here.
    if status == "proved" and applicability_blockers(node["id"], nodes):
        return f"{base}, {CONDITIONAL}"
    return base


#: The tone each standing is drawn in. A closed set, exported to the frontend beside the
#: label so the website never has to own a status vocabulary of its own --- the same
#: reason ``site.py`` ships the relation glosses rather than letting the legend invent
#: them. Note that `published`, `certified` and `attested` are three tones and not one:
#: collapsing them is exactly the green-badge-for-everything problem this replaces.
STANDING_TONES = {
    PUBLISHED: "published",
    PREPRINT_REVIEWED: "preprint",
    PREPRINT_UNREVIEWED: "preprint",
    CERTIFIED: "certified",
    ATTESTED: "attested",
    PROVED_ELSEWHERE: "proved-elsewhere",
    REFUTED: "refuted",
    DEFINED: "definition",
    OPEN_BY_KIND["assumption"]: "premise",
    OPEN_BY_KIND["obstruction"]: "barrier",
    OPEN_BY_KIND["conjecture"]: "open",
    OPEN_BY_KIND["question"]: "open",
    OPEN_DEFAULT: "open",
}


def standing_detail(node: dict, nodes: dict[str, dict]) -> dict:
    """``standing()`` split into what a badge needs: the words, a tone, a qualifier.

    The ``label`` is the *whole* string, ``", conditional"`` included, so that a badge on
    the website and the badge ``status.tex`` puts in the PDF cannot say different things.
    The tone is the base standing's, with ``conditional`` carried separately: a proved
    implication resting on an open antecedent is still that kind of result, and the
    qualifier modifies it rather than replacing it (CLAUDE.md constraint 8, P2).
    """
    label = standing(node, nodes)
    suffix = f", {CONDITIONAL}"
    conditional = label.endswith(suffix)
    base = label[:-len(suffix)] if conditional else label
    return {"standing": label,
            "standing_tone": STANDING_TONES[base],
            "standing_conditional": conditional}


#: Macros dropped whole, with their optional and mandatory arguments. A citation or a
#: cross-reference is LaTeX's way of pointing at something a derived view already links
#: structurally --- a claim page shows ``assumes``, ``depends_on`` and ``references`` as
#: real links --- so carrying "Theorem~4.7" into a heading would be a worse copy of a
#: better mechanism. A ``~`` or space immediately before one goes with it, so dropping
#: ``\ref`` out of "Assumption~\ref{hyp:KI}" leaves no trailing gap.
TITLE_DROPPED = frozenset({
    "cite", "citep", "citet", "ref", "eqref", "autoref", "cref", "Cref", "label",
})

#: Macros whose braces come off and whose contents stay. A title is set in one type, so
#: emphasis inside it has nowhere to go, and the frontend builds text nodes rather than
#: markup: the honest rendering is the words themselves.
TITLE_UNWRAPPED = frozenset({
    "emph", "textit", "textbf", "textrm", "textsc", "text", "mbox", "textup",
})

#: Accent macros, as combining marks, composed with NFC afterwards so ``\'e`` becomes one
#: character rather than two --- which is what a browser find box and a sort order want.
TITLE_ACCENTS = {
    "'": "́", "`": "̀", "^": "̂", '"': "̈", "~": "̃",
    "=": "̄", ".": "̇", "u": "̆", "v": "̌", "H": "̋",
    "c": "̧", "k": "̨", "d": "̣", "b": "̱", "r": "̊",
}

#: Escaped literals: a backslash in front of one of these means the character itself.
TITLE_LITERALS = frozenset({"&", "%", "_", "#", "$", "{", "}", " "})

MACRO_RE = re.compile(r"\\([A-Za-z]+|.)", re.DOTALL)


def _skip_argument(raw: str, index: int, opener: str, closer: str) -> int:
    """Past a balanced ``{...}`` or ``[...]`` starting at ``index``, or ``index`` itself."""
    if index >= len(raw) or raw[index] != opener:
        return index
    depth = 0
    while index < len(raw):
        if raw[index] == "\\":
            index += 2
            continue
        if raw[index] == opener:
            depth += 1
        elif raw[index] == closer:
            depth -= 1
            if depth == 0:
                return index + 1
        index += 1
    return index


#: Capitalized in a title, but not a name: what a cross-reference is *called* before its
#: number, and the number is exactly what was just dropped. Without these, "answers
#: Question~\\ref{q:cmh-normalization}" would keep a "Question" that now refers to nothing.
REFERENCE_NOUNS = frozenset({
    "Theorem", "Lemma", "Proposition", "Corollary", "Definition", "Question",
    "Conjecture", "Assumption", "Remark", "Example", "Section", "Appendix",
    "Equation", "Figure", "Table", "Part", "Chapter",
})


#: A clause left over after a citation or reference was dropped is provenance rather than
#: content when it names nothing: no mathematics, and no capitalized word that could be a
#: proper noun or the start of a real second half. "the sup-over-time form is" and
#: "answers Question" qualify; "Klartag--Lehec" and "the $\\log n$ frontier" do not.
def _is_provenance_tail(tail: str) -> bool:
    stripped = tail.strip()
    if "$" in stripped:
        return False
    return not any(word[:1].isupper() and word.strip(".,;:") not in REFERENCE_NOUNS
                   for word in stripped.split())


def title_display(raw: str | None) -> tuple[str | None, str | None]:
    """A manuscript claim title, reduced to what a heading can show.

    Returns ``(display, problem)``. Exactly one is ever set: a title this function does
    not fully understand comes back as ``(None, reason)`` so the editorial lane can say
    so out loud. That refusal is the point --- the alternative to failing here is raw TeX
    leaking into an ``<h1>``, which is the failure nobody notices until a reader does.

    ``$...$`` survives verbatim, because MathJax is downstream and mathematics is the one
    construct a heading really can typeset. Nothing inside it is inspected: ``\\log`` is a
    macro in prose and a function name in mathematics, and only the second is meant here.

    A trailing clause whose only substance was a citation goes with the citation. The
    manuscript writes provenance into titles --- "Klartag--Lehec; the sup-over-time form
    is \\cite[Thm.~61]{KLnotes}" --- and a heading ending "the sup-over-time form is" is
    worse than one that stops at the semicolon. The reference itself is not lost: it is
    on the claim page, in the node's ``references``, as a link.
    """
    if raw is None:
        return None, None
    out: list[str] = []
    index = 0
    clause_start = 0          # index into `out` of the last top-level ';'
    clause_cited = False      # did a citation get dropped from that final clause?
    while index < len(raw):
        character = raw[index]

        if character == "$":                     # mathematics, copied through untouched
            end = raw.find("$", index + 1)
            if end == -1:
                return None, "unbalanced '$'"
            out.append(raw[index:end + 1])
            index = end + 1
            continue

        if character == "\\":
            match = MACRO_RE.match(raw, index)
            if match is None:
                return None, "trailing backslash"
            name = match.group(1)
            index = match.end()
            if name in TITLE_LITERALS:
                out.append(" " if name == " " else name)
            elif name in TITLE_ACCENTS:
                if raw[index:index + 1] == "{":          # \'{e}
                    end = _skip_argument(raw, index, "{", "}")
                    base, index = raw[index + 1:end - 1], end
                else:                                    # \'e
                    base, index = raw[index:index + 1], index + 1
                out.append(unicodedata.normalize("NFC", base + TITLE_ACCENTS[name]))
            elif name in TITLE_DROPPED:
                index = _skip_argument(raw, index, "[", "]")
                index = _skip_argument(raw, index, "{", "}")
                while out and out[-1] in (" ", " "):
                    out.pop()                    # the "Assumption~" left behind by \ref
                clause_cited = clause_cited or name != "label"
            elif name in TITLE_UNWRAPPED:
                end = _skip_argument(raw, index, "{", "}")
                inner, problem = title_display(raw[index + 1:end - 1])
                if problem:
                    return None, problem
                out.append(inner or "")
                index = end
            else:
                return None, f"unsupported macro '\\{name}'"
            continue

        if character in "{}":                    # a group is grouping, not content
            index += 1
        elif character == "~":
            out.append(" ")
            index += 1
        elif raw.startswith("---", index):
            out.append("—")
            index += 3
        elif raw.startswith("--", index):
            out.append("–")
            index += 2
        elif character in " \t\r\n":             # a wrapped source line is one space
            out.append(" ")
            while index < len(raw) and raw[index] in " \t\r\n":
                index += 1
        else:
            if character == ";":
                clause_start, clause_cited = len(out) + 1, False
            out.append(character)
            index += 1

    if clause_start and clause_cited and _is_provenance_tail("".join(out[clause_start:])):
        del out[clause_start - 1:]
    display = "".join(out).strip()
    return (display or None), None


def render(ledgers: list[dict]) -> str:
    """The exact intended contents of ``status.tex``.

    One ``\\gdef`` per node, sorted by id so the file has a stable diff. Node ids contain
    ``:`` and ``-``; both are safe inside ``\\csname…\\endcsname``, which is the whole
    reason the lookup is built that way rather than out of ordinary control sequences.
    """
    lines = [
        "% status.tex --- GENERATED. Do not edit.",
        "%",
        "% One reader-facing standing per ledger node, derived from",
        "% research/program/ledger.yaml by scripts/checks/editorial.py. Regenerate with",
        "%",
        "%     python3 scripts/new.py status",
        "%",
        "% scripts/check.py --lane editorial fails if this file and the ledger disagree,",
        "% so a badge on the page can never outrun the evidence behind it.",
        "",
    ]
    nodes = {nid: node for item in ledgers for nid, node in item["nodes"].items()}
    for nid in sorted(nodes):
        label = standing(nodes[nid], nodes)
        lines.append(
            f"\\expandafter\\gdef\\csname klsstatus@{nid}\\endcsname{{{label}}}"
        )
    lines.append("")
    return "\n".join(lines)


def write(root: Path, ledgers: list[dict]) -> str:
    """Regenerate ``status.tex``. Returns the path written, repo-relative."""
    (root / STATUS_PATH).write_text(render(ledgers), encoding="utf-8")
    return STATUS_PATH


def _claims_with_status(text: str) -> list[tuple[str | None, list[str], str | None]]:
    """For each claim environment in one file: its label, its ``\\klsstatus`` arguments.

    Built on the same event scan as ``ledger._labels_with_environments`` and with the
    same nesting rule --- a self-labelling environment owns what is inside it, a neutral
    wrapper does not --- so the two cannot disagree about what a claim is.
    """
    events = sorted(
        [(m.start(), 0, "env", m.group(1), m.group(2)) for m in ENVIRONMENT_RE.finditer(text)]
        + [(m.start(), 1, "label", m.group(1), None) for m in LABEL_RE.finditer(text)]
        + [(m.start(), 2, "status", m.group(1), None) for m in STATUS_MACRO_RE.finditer(text)]
    )
    stack: list[str] = []
    open_claims: list[list] = []          # [environment, label, [status args], line]
    found: list[tuple[str | None, list[str], str | None]] = []
    for position, _tie, kind, first, second in events:
        if kind == "env":
            if first == "begin":
                stack.append(second)
                if second in CLAIM_ENVIRONMENTS:
                    open_claims.append([second, None, [], text.count("\n", 0, position) + 1])
            elif second in stack:
                if second in CLAIM_ENVIRONMENTS and open_claims:
                    environment, label, statuses, line = open_claims.pop()
                    found.append((label, statuses, f"{environment}:{line}"))
                del stack[stack.index(second):]
            continue
        # A label or a status macro belongs to the innermost *claim* on the stack, unless
        # a self-labelling environment intervenes.
        owner = None
        for name in reversed(stack):
            if name in SELF_LABELLING_ENVIRONMENTS:
                break
            if name in CLAIM_ENVIRONMENTS:
                owner = name
                break
        if owner is None or not open_claims:
            continue
        if kind == "label" and open_claims[-1][1] is None:
            open_claims[-1][1] = first
        elif kind == "status":
            open_claims[-1][2].append(first)
    return found


def check_titles(labels: dict[str, dict], errors: list[str]) -> None:
    """Every claim title must reduce to something a heading can show.

    A title this module cannot reduce is an error rather than a silent fallback to the
    node id. The failure mode being bought off here is a heading that reads
    ``\\textcolor{red}{...}`` on a public mathematics site --- rare, ugly, and invisible
    to everyone except the reader who meets it.
    """
    for label, entry in sorted(labels.items()):
        if entry.get("environment") is None or not entry.get("title"):
            continue
        display, problem = title_display(entry["title"])
        if problem:
            errors.append(
                f"{entry['file']}:{entry['line']}: title of '{label}' has {problem}; "
                "titles are shown as headings, so the display layer must understand them"
            )
        elif display is None:
            errors.append(
                f"{entry['file']}:{entry['line']}: title of '{label}' reduces to nothing; "
                "give it words or remove it"
            )


def ascii_gloss_errors(ledgers: list[dict], errors: list[str]) -> None:
    """Every gloss writes its mathematics in ``$...$``, not in ASCII.

    A gloss is the one line a reader meets before deciding whether to open the claim, on
    the website and in ``check.py status`` alike. Written in ASCII it reads
    ``E[H Sigma^{-1} H] <= 4 Sigma``, which is not what the claim says so much as a
    transcription of it, and the site loads MathJax precisely so that it does not have
    to be read that way.

    This was `check.py glosses`, advisory, until the 103 nodes it listed were rewritten;
    it blocks now because the expensive part is done and the cheap part --- not
    regressing --- is what a checker is for. What it does *not* demand is that a gloss
    contain mathematics: a bridge or an obstruction is often better in plain words, and
    only the ASCII spellings in ``views.ASCII_MATHS`` are errors.
    """
    for item in ledgers:
        for nid, node in sorted(item["nodes"].items()):
            gloss = node.get("summary")
            if not isinstance(gloss, str) or not gloss:
                continue
            found = views.ascii_mathematics(gloss)
            if found:
                errors.append(
                    f"[{item['program']}] {nid}.summary: writes {', '.join(found)} "
                    "outside $...$; a gloss is typeset, so its mathematics goes "
                    "between dollars"
                )


def check(root: Path, ledgers: list[dict], errors: list[str]) -> None:
    """Both rules. Silent when the manuscript does not use the mechanism at all."""
    path = root / STATUS_PATH
    modules = root / "modules"
    uses_macro = False
    if modules.is_dir():
        for module in sorted(modules.rglob("*.tex")):
            try:
                text = strip_comments(module.read_text(encoding="utf-8"))
            except (OSError, UnicodeError):
                continue
            claims = _claims_with_status(text)
            if not any(statuses for _label, statuses, _where in claims):
                continue
            uses_macro = True
            relative = module.relative_to(root).as_posix()
            for label, statuses, where in claims:
                if len(statuses) > 1:
                    errors.append(
                        f"{relative}: {where} carries {len(statuses)} \\klsstatus macros; "
                        "one claim has one standing"
                    )
                elif not statuses:
                    errors.append(
                        f"{relative}: {where} has no \\klsstatus; every claim states its "
                        "standing beside itself"
                    )
                elif label is None:
                    errors.append(
                        f"{relative}: {where} has a \\klsstatus but no \\label"
                    )
                elif statuses[0] != label:
                    errors.append(
                        f"{relative}: {where} labels '{label}' but shows the standing of "
                        f"'{statuses[0]}'; a badge must name its own claim"
                    )

    if not uses_macro and not path.is_file():
        return  # the mechanism is not in use here, and nothing obliges it to be

    intended = render(ledgers)
    if not path.is_file():
        errors.append(f"{STATUS_PATH}: missing but \\klsstatus is used; {REGENERATE}")
        return
    try:
        actual = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        errors.append(f"{STATUS_PATH}: cannot read: {exc}")
        return
    if actual != intended:
        errors.append(f"{STATUS_PATH}: stale or hand-edited; {REGENERATE}")
