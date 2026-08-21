"""Per-target batteries, keyed by target id. Each module exposes:
  run_records(seed, **cfg) -> (records: list[dict], extra_header: dict)
  selftest(rng)           -> list[(name: str, ok: bool)]

A1-A5 are the Part II statement targets. KLS (Part III route-gating) has three channels:
  "kls"     SDE-free, sound bridge/Poincare-level signals (targets/kls.py)
  "kls-loc" localization SDE engine diagnostics; always no-verdict until the open-node
            observables are implemented (targets/kls_localization.py)
  "kls-align" the product tail-union q:alignment stress test; model-diagnostic only
              (targets/kls_alignment.py)
"""
from __future__ import annotations

from . import a1, a2, a3, a4, a5, kls, kls_alignment, kls_localization

REGISTRY = {
    "A1": a1,
    "A2": a2,
    "A3": a3,
    "A4": a4,
    "A5": a5,
    "kls": kls,
    "kls-loc": kls_localization,
    "kls-align": kls_alignment,
}
