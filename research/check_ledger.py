#!/usr/bin/env python3
"""Integrity checker for the research/ control plane (program-aware).

Validates every ``research/**/ledger.yaml``:

* ledger and node identities are unique (duplicate programs are rejected until
  multi-ledger merging has explicit semantics);
* dependency edges resolve, are acyclic, and do not let a proved node inherit an
  open, conjectured, refuted, heuristic, or conditional dependency/assumption;
* every conditional node declares a non-empty ``assuming`` contract, including
  inherited imports marked ``import_class: preprint-unreviewed``;
* numerical evidence artifacts exist and are valid provenance-stamped JSONL;
* KLS mechanism fences and the reverse
  ``obstructions.yaml.constrains``/ledger ``bounded_by`` map agree exactly.

Cross-program ``bridges: [program/id, ...]`` links are resolved against all
loaded ledgers. Optional proof-plane ``solution:`` files must exist and be certified
by ``checked_by: agent|human|lean``. Agent certification additionally requires
distinct named author/reviewer provenance and a persisted review report.

Run from the repo root: ``python3 research/check_ledger.py``.
Exit 0 = clean, 1 = errors. Requires PyYAML.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

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
CHECKED_BY = {"none", "agent", "human", "lean"}
CERTIFIED_BY = {"agent", "human", "lean"}
IMPORT_CLASSES = {"published", "preprint-unreviewed"}

# A colon following one of these prefixes denotes a repository id/LaTeX label,
# even if the slug is malformed. This prevents e.g. ``thm:misspelled_id`` from
# being silently accepted as free-form external prose.
INTERNAL_PREFIXES = {
    "ass", "conj", "cor", "def", "eq", "ex", "fam", "heur", "hyp", "lem",
    "obs", "prog", "prop", "q", "rem", "sec", "subsec", "thm", "warn",
}

# Which statuses remain unresolved premises for a proved node. Conditional and
# heuristic are deliberately included for KLS; ``assuming`` edges are traversed
# separately, including through intermediate dependencies.
PROGRAMS = {
    "ab": {
        "status": {"open", "conjectured", "proved", "imported", "refuted"},
        "unproved": {"open", "conjectured", "refuted"},
    },
    "kls": {
        "status": {"proved", "conditional", "open", "heuristic", "refuted", "imported"},
        "unproved": {"conditional", "open", "heuristic", "refuted"},
    },
}

RESOLVE_FIELDS = ("depends_on", "unlocks", "assuming", "discharged_by", "entry_point", "related")


def as_list(value: Any) -> list:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def _string_set(value: Any, context: str, errors: list[str]) -> set[str]:
    """Normalize a scalar/list field without letting malformed YAML crash validation."""
    result: set[str] = set()
    for item in as_list(value):
        if not isinstance(item, str) or not item.strip():
            errors.append(f"{context}: entries must be non-empty strings")
            continue
        result.add(item)
    return result


def looks_internal(ref: Any) -> bool:
    """Return whether ``ref`` uses a reserved repository-id prefix."""
    if not isinstance(ref, str) or ":" not in ref:
        return False
    return ref.split(":", 1)[0] in INTERNAL_PREFIXES


def is_external(ref: Any) -> bool:
    """Compatibility helper: external prose does not start with an internal prefix."""
    return not looks_internal(ref)


def all_labels(root: Path = ROOT) -> set[str]:
    labels: set[str] = set()
    modules = root / "modules"
    if not modules.exists():
        return labels
    for path in modules.rglob("*.tex"):
        labels |= set(re.findall(r"\\label\{([^}]+)\}", path.read_text()))
    return labels


def _load_obstructions(ledger_path: Path, errors: list[str]):
    """Load the optional sibling obstruction schema.

    Returns ``(vocabulary, rules)`` or ``(None, None)``. Each rule contains
    ``forbids``, optional ``warns``, and the exact reverse ``constrains`` map.
    Warned mechanisms are allowed, but (like forbidden mechanisms) must be
    acknowledged by ``bounded_by`` plus a non-empty ``clearance`` note.
    """
    path = ledger_path.with_name("obstructions.yaml")
    if not path.exists():
        return None, None
    try:
        data = yaml.safe_load(path.read_text()) or {}
    except yaml.YAMLError as exc:
        errors.append(f"{path}: invalid YAML: {exc}")
        return set(), {}
    if not isinstance(data, dict):
        errors.append(f"{path}: top level must be a mapping")
        return set(), {}

    vocabulary = _string_set(data.get("mechanisms"), f"{path}.mechanisms", errors)
    rules: dict[str, dict[str, set[str]]] = {}
    raw_rules = data.get("obstructions") or []
    if not isinstance(raw_rules, list):
        errors.append(f"{path}: 'obstructions' must be a list")
        return vocabulary, rules

    for index, raw in enumerate(raw_rules):
        if not isinstance(raw, dict) or not raw.get("id"):
            errors.append(f"{path}: obstruction #{index + 1} must be a mapping with an id")
            continue
        oid = raw["id"]
        if not isinstance(oid, str) or not oid.strip():
            errors.append(f"{path}: obstruction #{index + 1} id must be a non-empty string")
            continue
        if oid in rules:
            errors.append(f"{path}: duplicate obstruction id '{oid}'")
            continue
        forbids = _string_set(raw.get("forbids"), f"{path}: {oid}.forbids", errors)
        warns = _string_set(raw.get("warns"), f"{path}: {oid}.warns", errors)
        constrains = _string_set(raw.get("constrains"), f"{path}: {oid}.constrains", errors)
        overlap = forbids & warns
        if overlap:
            errors.append(f"{path}: {oid} tags both forbids and warns: {sorted(overlap)}")
        for tag in sorted((forbids | warns) - vocabulary):
            errors.append(f"{path}: {oid} uses mechanism '{tag}' absent from mechanisms")
        rules[oid] = {"forbids": forbids, "warns": warns, "constrains": constrains}
    return vocabulary, rules


def obstruction_ids_md(ledger_path: Path) -> set[str]:
    path = ledger_path.with_name("obstructions.md")
    if not path.exists():
        return set()
    return set(re.findall(r"\bobs:[A-Za-z0-9\-]+", path.read_text()))


def _load_ledger(path: Path, errors: list[str]) -> dict | None:
    try:
        doc = yaml.safe_load(path.read_text()) or {}
    except yaml.YAMLError as exc:
        errors.append(f"{path}: invalid YAML: {exc}")
        return None
    if not isinstance(doc, dict):
        errors.append(f"{path}: top level must be a mapping")
        return None
    return doc


def _nodes_by_id(path: Path, doc: dict, errors: list[str]) -> dict[str, dict]:
    raw_nodes = doc.get("nodes") or []
    if not isinstance(raw_nodes, list):
        errors.append(f"{path}: 'nodes' must be a list")
        return {}
    nodes: dict[str, dict] = {}
    for index, node in enumerate(raw_nodes):
        if not isinstance(node, dict):
            errors.append(f"{path}: node #{index + 1} must be a mapping")
            continue
        nid = node.get("id")
        if not isinstance(nid, str) or not nid.strip():
            errors.append(f"{path}: node #{index + 1} missing a non-empty string 'id'")
            continue
        if nid in nodes:
            errors.append(f"{path}: duplicate node id '{nid}'")
            continue
        nodes[nid] = node
    return nodes


def _validate_evidence_run(root: Path, program: str, nid: str, node: dict,
                           evidence: str, errors: list[str]) -> None:
    ref = node.get("evidence_run")
    eligible_flag = node.get("evidence_eligible")
    if eligible_flag is not None and not isinstance(eligible_flag, bool):
        errors.append(f"[{program}] {nid}: evidence_eligible must be true or false")
    eligible = evidence != "none" or eligible_flag is True
    if eligible and not ref:
        errors.append(f"[{program}] {nid}: evidence eligibility requires evidence_run")
        return
    if not ref:
        return
    if not isinstance(ref, str):
        errors.append(f"[{program}] {nid}.evidence_run: path must be a string")
        return

    relative = Path(ref)
    if relative.is_absolute():
        errors.append(f"[{program}] {nid}.evidence_run: want a repo-relative path, got '{ref}'")
        return
    artifact = (root / relative).resolve()
    try:
        artifact.relative_to(root.resolve())
    except ValueError:
        errors.append(f"[{program}] {nid}.evidence_run: path escapes repository root: '{ref}'")
        return
    if not artifact.is_file():
        errors.append(f"[{program}] {nid}.evidence_run: '{ref}' does not exist")
        return
    if artifact.suffix != ".jsonl":
        errors.append(f"[{program}] {nid}.evidence_run: '{ref}' must be .jsonl")

    try:
        lines = artifact.read_text().splitlines()
    except OSError as exc:
        errors.append(f"[{program}] {nid}.evidence_run: cannot read '{ref}': {exc}")
        return
    if not lines:
        errors.append(f"[{program}] {nid}.evidence_run: '{ref}' is empty")
        return

    objects: list[dict] = []
    for line_no, line in enumerate(lines, 1):
        if not line.strip():
            errors.append(f"[{program}] {nid}.evidence_run: blank JSONL line {line_no} in '{ref}'")
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"[{program}] {nid}.evidence_run: invalid JSON on line {line_no} of '{ref}': {exc.msg}")
            continue
        if not isinstance(item, dict):
            errors.append(f"[{program}] {nid}.evidence_run: line {line_no} of '{ref}' is not an object")
            continue
        objects.append(item)
    if not objects:
        return

    provenance = objects[0].get("_provenance")
    if not isinstance(provenance, dict):
        errors.append(f"[{program}] {nid}.evidence_run: first line of '{ref}' lacks _provenance object")
        return
    required = {"params"}
    missing = sorted(required - set(provenance))
    if missing:
        errors.append(f"[{program}] {nid}.evidence_run: provenance missing {missing} in '{ref}'")
    params = provenance.get("params")
    if not isinstance(params, dict):
        errors.append(f"[{program}] {nid}.evidence_run: provenance.params must be an object in '{ref}'")
    elif not isinstance(params.get("target"), str) or not params["target"].strip():
        errors.append(f"[{program}] {nid}.evidence_run: provenance.params.target missing in '{ref}'")
    expected_target = node.get("evidence_target")
    if eligible and (not isinstance(expected_target, str) or not expected_target.strip()):
        errors.append(f"[{program}] {nid}: evidence eligibility requires evidence_target")
    elif isinstance(params, dict) and isinstance(expected_target, str):
        if params.get("target") != expected_target:
            errors.append(
                f"[{program}] {nid}.evidence_run: target '{params.get('target')}' "
                f"does not match evidence_target '{expected_target}'"
            )
    if len(objects) < 2:
        errors.append(f"[{program}] {nid}.evidence_run: '{ref}' has provenance but no records")
    if evidence == "numerical-strong":
        if not isinstance(params, dict) or params.get("calibration_passed") is not True:
            errors.append(
                f"[{program}] {nid}: numerical-strong run '{ref}' lacks calibration_passed=true"
            )
        if not isinstance(params, dict) or params.get("shared_battery_passed") is not True:
            errors.append(
                f"[{program}] {nid}: numerical-strong run '{ref}' lacks shared_battery_passed=true"
            )
        if not isinstance(params, dict) or params.get("shared_battery") != "research/knowledge/instances.md":
            errors.append(
                f"[{program}] {nid}: numerical-strong run '{ref}' does not identify "
                "research/knowledge/instances.md as its shared battery"
            )
        if not any(record.get("kind") == "verdict" for record in objects[1:]):
            errors.append(f"[{program}] {nid}: numerical-strong run '{ref}' has no verdict record")


def _inherited_risks(start: str, nodes: dict[str, dict], unproved: set[str]):
    """Return unresolved dependency/assumption risks inherited by ``start``.

    The traversal deliberately crosses intermediate proved/imported/conditional
    nodes. Conditional nodes' explicit ``assuming`` references are therefore not
    hidden from a proved ancestor.
    """
    found: dict[tuple[str, str], list[str]] = {}

    def record(kind: str, target: str, path: list[str]):
        key = (kind, target)
        if key not in found or len(path) < len(found[key]):
            found[key] = path

    def visit(nid: str, path: list[str], stack: set[str]):
        if nid in stack:
            return
        node = nodes[nid]
        next_stack = stack | {nid}
        for assumption in as_list(node.get("assuming")):
            if isinstance(assumption, str):
                record("assumption", assumption, path + [f"assuming:{assumption}"])
        for dep in as_list(node.get("depends_on")):
            if not isinstance(dep, str) or dep not in nodes:
                continue
            dep_path = path + [dep]
            status = nodes[dep].get("status")
            if isinstance(status, str) and status in unproved:
                record(status, dep, dep_path)
            if (status == "imported"
                    and nodes[dep].get("import_class", "published") == "preprint-unreviewed"):
                record("preprint-unreviewed", dep, dep_path)
            visit(dep, dep_path, next_stack)

    visit(start, [start], set())
    return found


def _dependency_assumptions(start: str, nodes: dict[str, dict], unproved: set[str]) -> set[str]:
    """Assumptions a node inherits from its dependency subtree.

    A conditional dependency contributes its declared ``assuming`` contract, not
    its own theorem id. Open/heuristic/refuted/conjectured dependencies contribute
    their ids directly. This lets conditional interfaces compose while preventing
    a parent from silently dropping a child's premise.
    """
    inherited: set[str] = set()

    def visit(nid: str, stack: set[str]):
        if nid in stack:
            return
        next_stack = stack | {nid}
        for dependency in as_list(nodes[nid].get("depends_on")):
            if not isinstance(dependency, str) or dependency not in nodes:
                continue
            dep_node = nodes[dependency]
            dep_status = dep_node.get("status")
            if isinstance(dep_status, str) and dep_status in unproved and dep_status != "conditional":
                inherited.add(dependency)
            if (dep_status == "imported"
                    and dep_node.get("import_class", "published") == "preprint-unreviewed"):
                inherited.add(dependency)
            inherited.update(
                assumption
                for assumption in as_list(dep_node.get("assuming"))
                if isinstance(assumption, str) and assumption.strip()
            )
            visit(dependency, next_stack)

    visit(start, set())
    return inherited


def check_control_plane(research: Path = RESEARCH, root: Path | None = None,
                        expected_programs: set[str] | None = None) -> dict:
    """Validate a control-plane tree and return errors/warnings plus summary data.

    ``research``/``root`` parameters make the checker testable on isolated fixture
    trees without mutating the real repository.
    """
    research = Path(research)
    root = Path(root) if root is not None else research.parent
    labels = all_labels(root)
    errors: list[str] = []
    warnings: list[str] = []
    ledgers: list[dict] = []
    program_paths: dict[str, Path] = {}
    if expected_programs is None:
        expected_programs = set(PROGRAMS)

    for path in sorted(research.rglob("ledger.yaml")):
        doc = _load_ledger(path, errors)
        if doc is None:
            continue
        meta = doc.get("meta") or {}
        if not isinstance(meta, dict):
            errors.append(f"{path}: 'meta' must be a mapping")
            meta = {}
        program = meta.get("program") or ("kls" if "kls" in path.parts else "ab")
        if not isinstance(program, str):
            errors.append(f"{path}: meta.program must be a string")
            program = f"invalid:{path}"
        if program in program_paths:
            errors.append(
                f"{path}: duplicate ledger for program '{program}' "
                f"(already loaded from {program_paths[program]})"
            )
        else:
            program_paths[program] = path
        nodes = _nodes_by_id(path, doc, errors)
        vocabulary, rules = _load_obstructions(path, errors)
        if rules is not None:
            obstruction_ids = set(rules)
        else:
            obstruction_ids = {nid for nid, node in nodes.items() if node.get("kind") == "obstruction"}
        ledgers.append({
            "program": program,
            "path": path,
            "nodes": nodes,
            "cfg": PROGRAMS.get(program),
            "vocab": vocabulary,
            "rules": rules,
            "obs_ids": obstruction_ids,
            "obs_md": obstruction_ids_md(path),
        })
        if program not in PROGRAMS:
            errors.append(f"{path}: unknown program '{program}'")

    for missing_program in sorted(expected_programs - set(program_paths)):
        errors.append(f"missing ledger for configured program '{missing_program}'")

    qualified = {
        f"{ledger['program']}/{nid}"
        for ledger in ledgers
        for nid in ledger["nodes"]
    }

    for ledger in ledgers:
        program = ledger["program"]
        nodes = ledger["nodes"]
        obstruction_ids = ledger["obs_ids"]
        cfg = ledger["cfg"] or PROGRAMS["ab"]
        vocabulary = ledger["vocab"]
        rules = ledger["rules"]

        def resolves(ref: Any) -> bool:
            if not looks_internal(ref):
                return True
            return ref in nodes or ref in obstruction_ids or ref in labels

        for nid, node in nodes.items():
            for field in ("kind", "status", "file", "statement"):
                if field not in node:
                    errors.append(f"[{program}] {nid}: missing '{field}'")
            kind = node.get("kind")
            status = node.get("status")
            if not isinstance(kind, str) or kind not in KIND:
                errors.append(f"[{program}] {nid}: bad kind '{kind}'")
            if not isinstance(status, str) or status not in cfg["status"]:
                errors.append(
                    f"[{program}] {nid}: status '{status}' not allowed for program {program}"
                )
            import_class = node.get("import_class")
            if status == "imported":
                effective_import_class = import_class or "published"
                if effective_import_class not in IMPORT_CLASSES:
                    errors.append(
                        f"[{program}] {nid}: bad import_class '{effective_import_class}' "
                        f"(want one of {sorted(IMPORT_CLASSES)})"
                    )
            elif import_class is not None:
                errors.append(f"[{program}] {nid}: import_class is only valid with status imported")
            assumptions = as_list(node.get("assuming"))
            valid_assumptions = {
                assumption for assumption in assumptions
                if isinstance(assumption, str) and assumption.strip()
            }
            if status == "conditional" and not valid_assumptions:
                errors.append(f"[{program}] {nid}: conditional status requires non-empty assuming")
            if assumptions and len(valid_assumptions) != len(assumptions):
                errors.append(f"[{program}] {nid}.assuming: entries must be non-empty strings")

            file_ref = node.get("file")
            if "file" in node and (not isinstance(file_ref, str) or not file_ref.strip()):
                errors.append(f"[{program}] {nid}.file: must be a non-empty string")
            elif isinstance(file_ref, str) and not (root / file_ref).exists():
                errors.append(f"[{program}] {nid}.file: '{file_ref}' does not exist")
            if "statement" in node and (
                not isinstance(node.get("statement"), str) or not node["statement"].strip()
            ):
                errors.append(f"[{program}] {nid}.statement: must be a non-empty string")

            evidence = node.get("evidence", "none")
            if not isinstance(evidence, str) or evidence not in EVIDENCE:
                errors.append(f"[{program}] {nid}: bad evidence '{evidence}'")
            else:
                _validate_evidence_run(root, program, nid, node, evidence, errors)

            solution = node.get("solution")
            checked_by = node.get("checked_by")
            if checked_by is not None and (
                not isinstance(checked_by, str) or checked_by not in CHECKED_BY
            ):
                errors.append(
                    f"[{program}] {nid}: bad checked_by '{checked_by}' "
                    f"(want one of {sorted(CHECKED_BY)})"
                )
            if checked_by == "agent":
                authored_by = node.get("authored_by")
                reviewed_by = node.get("reviewed_by")
                review = node.get("review")
                if not isinstance(authored_by, str) or not authored_by.strip():
                    errors.append(
                        f"[{program}] {nid}: checked_by agent requires non-empty authored_by"
                    )
                if not isinstance(reviewed_by, str) or not reviewed_by.strip():
                    errors.append(
                        f"[{program}] {nid}: checked_by agent requires non-empty reviewed_by"
                    )
                if (
                    isinstance(authored_by, str)
                    and isinstance(reviewed_by, str)
                    and authored_by.strip() == reviewed_by.strip()
                ):
                    errors.append(
                        f"[{program}] {nid}: agent author and reviewer must be distinct"
                    )
                if not isinstance(review, str) or not review.strip():
                    errors.append(
                        f"[{program}] {nid}: checked_by agent requires a review report"
                    )
                else:
                    review_path = Path(review)
                    if review_path.is_absolute():
                        errors.append(
                            f"[{program}] {nid}.review: want a repo-relative path, got '{review}'"
                        )
                    else:
                        artifact = (root / review_path).resolve()
                        try:
                            artifact.relative_to(root.resolve())
                        except ValueError:
                            errors.append(
                                f"[{program}] {nid}.review: path escapes repository root: '{review}'"
                            )
                        else:
                            if not artifact.is_file():
                                errors.append(
                                    f"[{program}] {nid}.review: '{review}' does not exist"
                                )
                if not solution:
                    errors.append(
                        f"[{program}] {nid}: checked_by agent requires a standalone solution"
                    )
            if solution:
                if not isinstance(solution, str):
                    errors.append(f"[{program}] {nid}.solution: path must be a string")
                elif not (root / solution).exists():
                    errors.append(f"[{program}] {nid}.solution: '{solution}' does not exist")
                if checked_by not in CERTIFIED_BY:
                    errors.append(
                        f"[{program}] {nid}: solution present but checked_by is '{checked_by}' "
                        "(an unchecked proof is not proved; want agent, human, or lean)"
                    )

            for field in RESOLVE_FIELDS:
                for ref in as_list(node.get(field)):
                    if not isinstance(ref, str) or not ref.strip():
                        errors.append(f"[{program}] {nid}.{field}: references must be non-empty strings")
                    elif not resolves(ref):
                        errors.append(f"[{program}] {nid}.{field}: unknown internal id '{ref}'")

            for ref in as_list(node.get("unlocks")):
                target = nodes.get(ref) if isinstance(ref, str) else None
                if target is None:
                    continue
                premises = set()
                for field in ("depends_on", "assuming", "discharged_by"):
                    premises |= {
                        premise for premise in as_list(target.get(field))
                        if isinstance(premise, str)
                    }
                if nid in premises:
                    errors.append(
                        f"[{program}] {nid}.unlocks: '{ref}' already declares {nid} as a premise; "
                        "unlocks must not duplicate depends_on/assuming/discharged_by"
                    )

            for ref in as_list(node.get("bounded_by")):
                if not isinstance(ref, str) or not ref.strip():
                    errors.append(f"[{program}] {nid}.bounded_by: references must be non-empty strings")
                elif ref not in obstruction_ids:
                    errors.append(f"[{program}] {nid}.bounded_by: '{ref}' is not a declared obstruction")

            if isinstance(node.get("refines"), list):
                errors.append(f"[{program}] {nid}: 'refines' must be a single \\label, not a list")
            elif node.get("refines"):
                if not isinstance(node["refines"], str):
                    errors.append(f"[{program}] {nid}.refines: must be a string \\label")
                elif node["refines"] not in labels:
                    warnings.append(
                        f"[{program}] {nid}.refines: '{node['refines']}' not found as a \\label"
                    )

            for ref in as_list(node.get("bridges")):
                if not isinstance(ref, str) or not ref.strip():
                    errors.append(f"[{program}] {nid}.bridges: references must be non-empty strings")
                elif ref not in qualified:
                    errors.append(f"[{program}] {nid}.bridges: '{ref}' not found (want program/id)")

            if vocabulary is not None:
                for tag in as_list(node.get("mechanism")):
                    if not isinstance(tag, str) or not tag.strip():
                        errors.append(f"[{program}] {nid}.mechanism: entries must be non-empty strings")
                    elif tag not in vocabulary:
                        errors.append(
                            f"[{program}] {nid}.mechanism: '{tag}' not in obstructions.yaml vocabulary"
                        )

            if (nid not in labels and node.get("kind") not in ("obstruction", "baseline")
                    and not node.get("refines")):
                warnings.append(f"[{program}] {nid}: no matching \\label in modules/ (synthesized or drift?)")

        errors.extend(_acyclic(program, nodes))

        for nid, node in nodes.items():
            if node.get("status") != "conditional":
                continue
            declared = {
                assumption for assumption in as_list(node.get("assuming"))
                if isinstance(assumption, str) and assumption.strip()
            }
            missing = _dependency_assumptions(nid, nodes, cfg["unproved"]) - declared
            if missing:
                errors.append(
                    f"[{program}] {nid} (conditional) does not propagate inherited assumptions "
                    f"{sorted(missing)} in assuming"
                )

        for nid, node in nodes.items():
            if node.get("status") != "proved":
                continue
            for (kind, target), path in sorted(_inherited_risks(nid, nodes, cfg["unproved"]).items()):
                errors.append(
                    f"[{program}] {nid} (proved) inherits unresolved {kind} '{target}' "
                    f"via {' -> '.join(path)}"
                )

        if rules is not None:
            used_by = {oid: set() for oid in rules}
            for nid, node in nodes.items():
                for oid in as_list(node.get("bounded_by")):
                    if isinstance(oid, str) and oid in used_by:
                        used_by[oid].add(nid)

            markdown_ids = ledger["obs_md"]
            for oid in sorted(set(rules) - markdown_ids):
                errors.append(f"[{program}] parity: '{oid}' in obstructions.yaml but not obstructions.md")
            for oid in sorted(markdown_ids - set(rules)):
                errors.append(f"[{program}] parity: '{oid}' in obstructions.md but not obstructions.yaml")

            for oid, rule in sorted(rules.items()):
                declared = rule["constrains"]
                reverse = used_by[oid]
                for target in sorted(declared - set(nodes)):
                    errors.append(f"[{program}] {oid}.constrains: unknown ledger node '{target}'")
                if declared != reverse:
                    errors.append(
                        f"[{program}] {oid}.constrains reverse parity mismatch: "
                        f"yaml-only={sorted(declared - reverse)}, "
                        f"ledger-only={sorted(reverse - declared)}"
                    )

            for nid, node in nodes.items():
                mechanisms = {
                    mechanism for mechanism in as_list(node.get("mechanism"))
                    if isinstance(mechanism, str) and mechanism.strip()
                }
                if not mechanisms:
                    continue
                bounded = set(as_list(node.get("bounded_by")))
                clearance = node.get("clearance")
                cleared = isinstance(clearance, str) and bool(clearance.strip())
                for oid, rule in rules.items():
                    for relation in ("forbids", "warns"):
                        hit = mechanisms & rule[relation]
                        if not hit:
                            continue
                        descriptor = "forbidden" if relation == "forbids" else "warned about"
                        if oid not in bounded:
                            errors.append(
                                f"[{program}] {nid}: mechanism {sorted(hit)} {descriptor} by {oid} "
                                "not in bounded_by (uncleared)"
                            )
                        elif not cleared:
                            errors.append(
                                f"[{program}] {nid}: mechanism {sorted(hit)} {descriptor} by {oid} "
                                "lacks a clearance note"
                            )

    return {"errors": errors, "warnings": warnings, "ledgers": ledgers, "labels": labels}


def _acyclic(program: str, nodes: dict[str, dict]) -> list[str]:
    white, gray, black = 0, 1, 2
    color = {nid: white for nid in nodes}
    errors: list[str] = []

    def visit(node_id: str, stack: list[str]):
        color[node_id] = gray
        for dependency in as_list(nodes[node_id].get("depends_on")):
            if not isinstance(dependency, str) or dependency not in nodes:
                continue
            if color[dependency] == gray:
                errors.append(
                    f"[{program}] CYCLE: "
                    + " -> ".join(stack[stack.index(dependency):] + [dependency])
                )
            elif color[dependency] == white:
                visit(dependency, stack + [dependency])
        color[node_id] = black

    for node_id in nodes:
        if color[node_id] == white:
            visit(node_id, [node_id])
    return errors


def main() -> int:
    report = check_control_plane()
    for warning in report["warnings"]:
        print("WARN:", warning)
    for error in report["errors"]:
        print("FAIL:", error)
    ledgers = report["ledgers"]
    total = sum(len(ledger["nodes"]) for ledger in ledgers)
    print(
        f"\n{len(ledgers)} ledger(s), {total} nodes, {len(report['labels'])} labels. "
        f"{len(report['errors'])} error(s), {len(report['warnings'])} warning(s)."
    )
    for ledger in sorted(ledgers, key=lambda item: (item["program"], str(item["path"]))):
        counts = Counter(str(node.get("status")) for node in ledger["nodes"].values())
        statuses = ", ".join(f"{key}={value}" for key, value in sorted(counts.items()))
        print(f"  [{ledger['program']}] {len(ledger['nodes'])} nodes — {statuses}")
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
