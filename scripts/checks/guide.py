"""The editorial guide: what a new reader sees first, validated as navigation.

``research/program/editorial.yaml`` is the one input this website needed that no existing
domain held. The ledger knows every claim and cannot say which fifteen a stranger should
read; the portfolio knows every approach and does not know that the manuscript groups
them into four routes called E, S, C and F; the manuscript knows both and says so in
LaTeX prose, where ``scripts/site.py`` cannot reach it and should not try.

So this file records selection, naming and order --- and *only* those. The danger it
carries is obvious and is the reason the checks below are as blunt as they are: a
presentation file is exactly where a copied gloss or a hand-maintained status would go to
live, and it would be the prettiest copy in the repository. ``FORBIDDEN`` refuses those
keys outright rather than trusting a convention. What is left is identifiers, and an
identifier that does not resolve is an error, so this file cannot describe a repository
that does not exist.

The lane is ``editorial``, shared with ``editorial.py``: both answer "what does a reader
see", and one lane for that question is easier to hold in the head than two.
"""
from __future__ import annotations

from pathlib import Path

try:
    import yaml
except ModuleNotFoundError:                                    # pragma: no cover
    yaml = None

GUIDE_PATH = Path("research/program/editorial.yaml")

#: The whole schema. Anything else is a typo or a new idea, and both should be said out
#: loud rather than silently ignored --- the same discipline `ledger.py` applies to nodes.
TOP_LEVEL = {"site", "routes", "probes", "frontier", "featured", "reading"}
SITE_KEYS = {"name", "tagline"}
ROUTE_KEYS = {"code", "name", "families", "anchor"}
PROBE_KEYS = {"name", "families"}
FEATURED_KEYS = {"id", "role", "route"}
READING_KEYS = {"label", "anchor"}

#: Constraint 7, made mechanical. Every one of these names a field that is canonical
#: somewhere else: a statement in the manuscript, a status in the ledger, an objective or
#: a blocker in the portfolio. A file that may not spell them cannot quietly become their
#: second home, whatever anyone later intends.
FORBIDDEN = frozenset({
    "summary", "statement", "gloss", "status", "provenance", "import_class",
    "objective", "blocker", "mechanism", "reopen_if", "proofs", "depends_on",
    "assumes", "implies", "bounded_by", "state",
})

#: What a featured claim is *for*. Closed, because the grouping on the results page is
#: these words and a reader can only learn a vocabulary that stays still.
ROLES = ("bridge", "advance", "bottleneck", "obstruction", "refuted", "model")

#: Sanity bounds on the selection. A curated list of two is not curation, and one of
#: eighty is the full inventory again under a friendlier name.
MIN_FEATURED, MAX_FEATURED = 6, 24


def _forbidden(value: object, path: str, errors: list[str]) -> None:
    """Refuse a canonical field name anywhere in the tree, at any depth."""
    if isinstance(value, dict):
        for key, item in value.items():
            if isinstance(key, str) and key.lower() in FORBIDDEN:
                errors.append(
                    f"{GUIDE_PATH}: {path}{key} is canonical elsewhere and may not be "
                    "written here; this file holds identifiers and navigation only"
                )
            _forbidden(item, f"{path}{key}.", errors)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            _forbidden(item, f"{path}[{index}].", errors)


def _keys(entry: dict, allowed: set[str], required: set[str], context: str,
          errors: list[str]) -> None:
    for key in sorted(set(entry) - allowed):
        errors.append(f"{GUIDE_PATH}: {context} has unknown field '{key}'")
    for key in sorted(required - set(entry)):
        errors.append(f"{GUIDE_PATH}: {context} is missing '{key}'")


def load(root: Path, errors: list[str]) -> dict | None:
    """Parse the guide, or ``None`` when there is none. Absent is a valid answer."""
    path = root / GUIDE_PATH
    if not path.is_file():
        return None
    if yaml is None:                                           # pragma: no cover
        errors.append(f"{GUIDE_PATH}: PyYAML is required to read this file")
        return None
    try:
        document = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        errors.append(f"{GUIDE_PATH}: cannot read: {exc}")
        return None
    if document is None:
        return None
    if not isinstance(document, dict):
        errors.append(f"{GUIDE_PATH}: expected a mapping at the top level")
        return None
    return document


def check(root: Path, guide: dict | None, node_ids: set[str], family_ids: set[str],
          labels: dict[str, dict], errors: list[str]) -> None:
    """Every id resolves, every anchor exists, the families partition, nothing is copied."""
    if guide is None:
        return

    _forbidden(guide, "", errors)
    for key in sorted(set(guide) - TOP_LEVEL):
        errors.append(f"{GUIDE_PATH}: unknown top-level section '{key}'")

    def anchor(value: object, context: str) -> None:
        if not isinstance(value, str) or not value:
            errors.append(f"{GUIDE_PATH}: {context} needs a manuscript anchor")
        elif value not in labels:
            errors.append(
                f"{GUIDE_PATH}: {context} points at '{value}', which is not a \\label "
                "in modules/; the site would link a reader to nothing"
            )

    def claim(value: object, context: str) -> None:
        if not isinstance(value, str) or not value:
            errors.append(f"{GUIDE_PATH}: {context} needs a ledger node id")
        elif value not in node_ids:
            errors.append(f"{GUIDE_PATH}: {context} names '{value}', which is no ledger node")

    site = guide.get("site")
    if site is not None:
        if isinstance(site, dict):
            _keys(site, SITE_KEYS, {"name"}, "site", errors)
        else:
            errors.append(f"{GUIDE_PATH}: 'site' must be a mapping")

    # --- the four routes, and the families they account for -------------------------
    claimed: dict[str, str] = {}
    codes: set[str] = set()
    routes = guide.get("routes") or []
    if not isinstance(routes, list):
        errors.append(f"{GUIDE_PATH}: 'routes' must be a list")
        routes = []
    for index, route in enumerate(routes):
        context = f"routes[{index}]"
        if not isinstance(route, dict):
            errors.append(f"{GUIDE_PATH}: {context} must be a mapping")
            continue
        _keys(route, ROUTE_KEYS, {"code", "name", "families", "anchor"}, context, errors)
        code = route.get("code")
        if isinstance(code, str) and code:
            context = f"route {code}"
            if code in codes:
                errors.append(f"{GUIDE_PATH}: route code '{code}' is used twice")
            codes.add(code)
        anchor(route.get("anchor"), context)
        for family in route.get("families") or []:
            if family in claimed:
                errors.append(
                    f"{GUIDE_PATH}: {context} and {claimed[family]} both contain "
                    f"'{family}'; a family belongs to one route"
                )
            elif family not in family_ids:
                errors.append(
                    f"{GUIDE_PATH}: {context} contains '{family}', which is no "
                    "portfolio family"
                )
            claimed[family] = context

    probes = guide.get("probes")
    if isinstance(probes, dict):
        _keys(probes, PROBE_KEYS, {"name", "families"}, "probes", errors)
        for family in probes.get("families") or []:
            if family in claimed:
                errors.append(
                    f"{GUIDE_PATH}: probes and {claimed[family]} both contain '{family}'"
                )
            elif family not in family_ids:
                errors.append(f"{GUIDE_PATH}: probes contains '{family}', which is no "
                              "portfolio family")
            claimed[family] = "probes"
    elif probes is not None:
        errors.append(f"{GUIDE_PATH}: 'probes' must be a mapping")

    # A family nobody placed is a family that silently vanishes from the public site
    # while staying live in the portfolio, which is the one failure this partition
    # exists to prevent.
    for family in sorted(family_ids - set(claimed)):
        errors.append(
            f"{GUIDE_PATH}: portfolio family '{family}' belongs to no route and is not "
            "listed under 'probes'; it would not appear on the site at all"
        )

    # --- the curated claims ----------------------------------------------------------
    for index, entry in enumerate(guide.get("frontier") or []):
        claim(entry, f"frontier[{index}]")

    featured = guide.get("featured") or []
    if not isinstance(featured, list):
        errors.append(f"{GUIDE_PATH}: 'featured' must be a list")
        featured = []
    elif not MIN_FEATURED <= len(featured) <= MAX_FEATURED:
        errors.append(
            f"{GUIDE_PATH}: 'featured' selects {len(featured)} claims; keep it between "
            f"{MIN_FEATURED} and {MAX_FEATURED}, or it stops being a selection"
        )
    seen: set[str] = set()
    for index, entry in enumerate(featured):
        context = f"featured[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{GUIDE_PATH}: {context} must be a mapping")
            continue
        _keys(entry, FEATURED_KEYS, {"id", "role"}, context, errors)
        claim(entry.get("id"), context)
        if entry.get("id") in seen:
            errors.append(f"{GUIDE_PATH}: {context} features '{entry['id']}' twice")
        seen.add(entry.get("id"))
        if entry.get("role") not in ROLES:
            errors.append(
                f"{GUIDE_PATH}: {context} has role '{entry.get('role')}'; "
                f"one of {', '.join(ROLES)}"
            )
        route = entry.get("route")
        if route is not None and route not in codes:
            errors.append(f"{GUIDE_PATH}: {context} names route '{route}', which is not "
                          "one of the routes above")

    # --- the reading path ------------------------------------------------------------
    reading = guide.get("reading") or []
    if not isinstance(reading, list):
        errors.append(f"{GUIDE_PATH}: 'reading' must be a list")
        reading = []
    for index, entry in enumerate(reading):
        context = f"reading[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{GUIDE_PATH}: {context} must be a mapping")
            continue
        _keys(entry, READING_KEYS, {"label", "anchor"}, context, errors)
        anchor(entry.get("anchor"), context)
