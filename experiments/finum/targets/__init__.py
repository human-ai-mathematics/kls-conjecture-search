"""Per-target batteries, keyed by target id. Each module exposes:
  run_records(seed, **cfg) -> (records: list[dict], extra_header: dict)
  selftest(rng)           -> list[(name: str, ok: bool)]

A1-A5 are the Part II statement targets. KLS (Part III route-gating) has two channels:
  "kls"     SDE-free, sound bridge/Poincare-level signals (targets/kls.py)
  "kls-loc" the localization SDE engine: directional occupation/alignment signals, gated
            (targets/kls_localization.py, on top of finum.localization)
"""
from __future__ import annotations

from . import a1, a2, a3, a4, a5, kls, kls_localization

REGISTRY = {
    "A1": a1,
    "A2": a2,
    "A3": a3,
    "A4": a4,
    "A5": a5,
    "kls": kls,
    "kls-loc": kls_localization,
}
