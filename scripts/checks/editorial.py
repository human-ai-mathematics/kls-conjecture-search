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
from pathlib import Path

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
