#!/usr/bin/env python3
"""Integrity checker for the research/ control plane (program-aware).

Validates every research/**/ledger.yaml:
  - A-series (program: ab)  — refinement phase; status/evidence vocabulary;
                              obstructions are in-ledger `kind: obstruction` nodes.
  - KLS      (program: kls) — proof phase; richer status; machine-enforced no-go set
                              in a sibling obstructions.yaml (+ obstructions.md parity).

Cross-program `bridges: [program/id, ...]` links are resolved against all loaded ledgers.

Optional Phase-2 fields (any program): `solution:` points at a standalone proof file under
solutions/; if present, the file must exist and `checked_by:` must be `human` or `lean`
(a proof with checked_by=none is not yet a proof). Symmetric with evidence_run/numerical-strong.

Run from the repo root:   python3 research/check_ledger.py
Exit 0 = clean, 1 = errors. Requires PyYAML.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")

RESEARCH = Path(__file__).resolve().parent
ROOT = RESEARCH.parent

KIND = {
    "theorem", "lemma", "proposition", "corollary", "definition", "assumption",
    "hypothesis", "question", "program", "remark", "heuristic",
    "conjecture", "obstruction", "baseline", "example", "imported",
}
EVIDENCE = {"none", "numerical-directional", "numerical-strong"}
CHECKED_BY = {"none", "human", "lean"}  # Phase-2 proof certification ladder

# per-program config: allowed statuses, and which statuses count as "unproved"
# for the "no proved node rests on an unproved one" rule.
PROGRAMS = {
    "ab": {
        "status": {"open", "conjectured", "proved", "imported", "refuted"},
        "unproved": {"open", "conjectured", "refuted"},
    },
    "kls": {
        "status": {"proved", "conditional", "open", "heuristic", "refuted", "imported"},
        "unproved": {"open", "refuted"},
    },
}

# edge fields whose entries resolve to a node / obstruction / \label / external free-text
RESOLVE_FIELDS = ("depends_on", "unlocks", "assuming", "discharged_by", "entry_point", "related")


def is_external(ref: str) -> bool:
    """Internal refs have the exact shape 'kind:slug'. Anything else (free text like
    'perimeter supermartingale') is an allowed external and skipped."""
    return re.fullmatch(r"[a-z]+:[A-Za-z0-9\-]+", ref) is None


def as_list(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def all_labels() -> set[str]:
    labs: set[str] = set()
    for f in (ROOT / "modules").rglob("*.tex"):
        labs |= set(re.findall(r"\\label\{([^}]+)\}", f.read_text()))
    return labs


def load_obstructions_yaml(ledger_path: Path):
    """(vocab, forbids) from a sibling obstructions.yaml, or (None, None) if absent."""
    p = ledger_path.with_name("obstructions.yaml")
    if not p.exists():
        return None, None
    data = yaml.safe_load(p.read_text()) or {}
    vocab = set(data.get("mechanisms") or [])
    forbids = {o["id"]: set(o.get("forbids") or []) for o in (data.get("obstructions") or [])}
    return vocab, forbids


def obstruction_ids_md(ledger_path: Path) -> set[str]:
    p = ledger_path.with_name("obstructions.md")
    if not p.exists():
        return set()
    return set(re.findall(r"\bobs:[A-Za-z0-9\-]+", p.read_text()))


def main() -> int:
    labs = all_labels()
    errors: list[str] = []
    warnings: list[str] = []

    # ---- load every ledger, keyed by program -----------------------------
    ledgers = {}  # program -> {"path", "nodes", "cfg", "vocab", "forbids", "obs_ids"}
    for path in sorted(RESEARCH.rglob("ledger.yaml")):
        doc = yaml.safe_load(path.read_text())
        meta = doc.get("meta", {}) or {}
        program = meta.get("program") or ("kls" if "kls" in path.parts else "ab")
        nodes = {n["id"]: n for n in doc.get("nodes", []) if "id" in n}
        vocab, forbids = load_obstructions_yaml(path)
        if forbids is not None:                       # KLS-style: obstructions in yaml
            obs_ids = set(forbids)
        else:                                          # A-series: obstruction nodes
            obs_ids = {nid for nid, n in nodes.items() if n.get("kind") == "obstruction"}
        ledgers[program] = dict(path=path, nodes=nodes, cfg=PROGRAMS.get(program),
                                vocab=vocab, forbids=forbids, obs_ids=obs_ids,
                                obs_md=obstruction_ids_md(path))
        if program not in PROGRAMS:
            errors.append(f"{path}: unknown program '{program}'")

    qualified = {f"{prog}/{nid}" for prog, L in ledgers.items() for nid in L["nodes"]}

    # ---- per-program validation ------------------------------------------
    for program, L in ledgers.items():
        nodes, obs_ids = L["nodes"], L["obs_ids"]
        cfg = L["cfg"] or PROGRAMS["ab"]
        vocab, forbids = L["vocab"], L["forbids"]

        def resolve(ref: str) -> bool:
            return is_external(ref) or ref in nodes or ref in obs_ids or ref in labs

        for nid, n in nodes.items():
            for f in ("kind", "status", "file", "statement"):
                if f not in n:
                    errors.append(f"[{program}] {nid}: missing '{f}'")
            if n.get("kind") not in KIND:
                errors.append(f"[{program}] {nid}: bad kind '{n.get('kind')}'")
            if n.get("status") not in cfg["status"]:
                errors.append(f"[{program}] {nid}: status '{n.get('status')}' not allowed for program {program}")

            # file must exist (this is what catches module-path drift)
            if "file" in n and not (ROOT / n["file"]).exists():
                errors.append(f"[{program}] {nid}.file: '{n['file']}' does not exist")

            # evidence (A-series)
            ev = n.get("evidence", "none")
            if ev not in EVIDENCE:
                errors.append(f"[{program}] {nid}: bad evidence '{ev}'")
            if ev == "numerical-strong" and not n.get("evidence_run"):
                errors.append(f"[{program}] {nid}: evidence=numerical-strong requires evidence_run")

            # Phase-2 solution artifact (any program; optional, symmetric with evidence_run)
            sol = n.get("solution")
            cb = n.get("checked_by")
            if cb is not None and cb not in CHECKED_BY:
                errors.append(f"[{program}] {nid}: bad checked_by '{cb}' (want one of {sorted(CHECKED_BY)})")
            if sol:
                if not (ROOT / sol).exists():
                    errors.append(f"[{program}] {nid}.solution: '{sol}' does not exist")
                if cb not in ("human", "lean"):
                    errors.append(f"[{program}] {nid}: solution present but checked_by is '{cb}' "
                                  f"(an unchecked proof is not proved; want human or lean)")

            # resolvable edges
            for field in RESOLVE_FIELDS:
                for ref in as_list(n.get(field)):
                    if not resolve(ref):
                        errors.append(f"[{program}] {nid}.{field}: unknown id '{ref}'")

            # bounded_by -> obstruction ids
            for ref in as_list(n.get("bounded_by")):
                if ref not in obs_ids:
                    errors.append(f"[{program}] {nid}.bounded_by: '{ref}' is not a declared obstruction")

            # refines -> a single manuscript \label (not a ledger node)
            if isinstance(n.get("refines"), list):
                errors.append(f"[{program}] {nid}: 'refines' must be a single \\label, not a list")
            elif n.get("refines") and n["refines"] not in labs:
                warnings.append(f"[{program}] {nid}.refines: '{n['refines']}' not found as a \\label")

            # bridges -> program/id in some loaded ledger
            for ref in as_list(n.get("bridges")):
                if ref not in qualified:
                    errors.append(f"[{program}] {nid}.bridges: '{ref}' not found (want program/id)")

            # mechanism vocabulary
            if vocab is not None:
                for t in as_list(n.get("mechanism")):
                    if t not in vocab:
                        errors.append(f"[{program}] {nid}.mechanism: '{t}' not in obstructions.yaml vocabulary")

            # drift: node id should be a real \label (warn; skip synthesized nodes)
            if (nid not in labs and n.get("kind") not in ("obstruction", "baseline")
                    and not n.get("refines")):
                warnings.append(f"[{program}] {nid}: no matching \\label in modules/ (synthesized or drift?)")

        # acyclicity of depends_on (within program)
        errors.extend(_acyclic(program, nodes))

        # no proved node rests on an unproved one
        for nid, n in nodes.items():
            if n.get("status") == "proved":
                for d in as_list(n.get("depends_on")):
                    if d in nodes and nodes[d].get("status") in cfg["unproved"]:
                        errors.append(f"[{program}] {nid} (proved) depends_on '{d}' ({nodes[d]['status']})")

        # no-go enforcement + parity (programs with an obstructions.yaml)
        if forbids is not None:
            used = set()
            for n in nodes.values():
                used |= set(as_list(n.get("bounded_by")))
            md_ids = L["obs_md"]
            for o in sorted(set(forbids) - md_ids):
                errors.append(f"[{program}] parity: '{o}' in obstructions.yaml but not obstructions.md")
            for o in sorted(md_ids - set(forbids)):
                errors.append(f"[{program}] parity: '{o}' in obstructions.md but not obstructions.yaml")
            for o in sorted(used - set(forbids)):
                errors.append(f"[{program}] parity: bounded_by uses '{o}' absent from obstructions.yaml")
            for nid, n in nodes.items():
                mech = set(as_list(n.get("mechanism")))
                if not mech:
                    continue
                bounded = set(as_list(n.get("bounded_by")))
                cleared = bool((n.get("clearance") or "").strip())
                for oid, ftags in forbids.items():
                    hit = mech & ftags
                    if not hit:
                        continue
                    if oid not in bounded:
                        errors.append(f"[{program}] {nid}: mechanism {sorted(hit)} forbidden by {oid} not in bounded_by (uncleared)")
                    elif not cleared:
                        errors.append(f"[{program}] {nid}: mechanism {sorted(hit)} forbidden by {oid} lacks a clearance note")

    # ---- report ----------------------------------------------------------
    for w in warnings:
        print("WARN:", w)
    for e in errors:
        print("FAIL:", e)
    total = sum(len(L["nodes"]) for L in ledgers.values())
    print(f"\n{len(ledgers)} ledger(s), {total} nodes, {len(labs)} labels. "
          f"{len(errors)} error(s), {len(warnings)} warning(s).")
    for program, L in sorted(ledgers.items()):
        from collections import Counter
        st = Counter(n["status"] for n in L["nodes"].values())
        print(f"  [{program}] {len(L['nodes'])} nodes — " + ", ".join(f"{k}={v}" for k, v in sorted(st.items())))
    return 1 if errors else 0


def _acyclic(program: str, nodes: dict) -> list[str]:
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {nid: WHITE for nid in nodes}
    errors: list[str] = []

    def visit(u, stack):
        color[u] = GRAY
        for v in as_list(nodes[u].get("depends_on")):
            if v not in nodes:
                continue
            if color[v] == GRAY:
                errors.append(f"[{program}] CYCLE: " + " -> ".join(stack[stack.index(v):] + [v]))
            elif color[v] == WHITE:
                visit(v, stack + [v])
        color[u] = BLACK

    for nid in nodes:
        if color[nid] == WHITE:
            visit(nid, [nid])
    return errors


if __name__ == "__main__":
    raise SystemExit(main())
