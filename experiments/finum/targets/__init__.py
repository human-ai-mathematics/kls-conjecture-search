"""Public target registry, keyed by stable CLI target id.

Each implementation module exposes:
  run_records(seed, **cfg) -> RunResult
  selftest(rng)           -> list[(name: str, ok: bool)]

A1--A5 live in ``targets.a_series``. KLS (Part III route-gating) lives in ``targets.kls``:
  "kls"     SDE-free, sound bridge/Poincare-level signals (kls/bridge.py)
  "loc-engine" legacy localization SDE diagnostics; no route observable or claim conclusion
            observables are implemented (kls/loc_engine.py)
  "kls-align" the product tail-union q:alignment stress test; model-diagnostic only
              (kls/alignment.py)
  "cmh-gate-zero" the deterministic moment-map/CMH gate-zero battery
              E[H Sigma^{-1} H] <= 4 Sigma (kls/cmh_gate_zero/) -- exact 1D Stein kernels
              and Dirichlet moment matrices, an exact algebraic countermodel, and directional
              floating generalized-eigenvalue/Galerkin diagnostics. No Monte Carlo; gate zero is
              NECESSARY, never sufficient, and an exact emitted certificate still requires
              independent proof/refutation review.
"""
from __future__ import annotations

from ..contract import TargetSpec
from .a_series import a1, a2, a3, a4, a5
from .kls import alignment, bridge, cmh_gate_zero, loc_engine

REGISTRY = {
    "A1": TargetSpec(
        "A1", a1, "GLM curvature and flat-direction diagnostics", True,
        {"standard": {"n_cal": 20_000, "n_stress": 4_000}},
    ),
    "A2": TargetSpec(
        "A2", a2, "Bernstein-von Mises transfer diagnostics", True,
        {"standard": {}},
    ),
    "A3": TargetSpec(
        "A3", a3, "weighted Poincare heavy-tail diagnostics", False,
        {"standard": {}},
    ),
    "A4": TargetSpec(
        "A4", a4, "restricted transport diagnostics", False,
        {"standard": {}},
    ),
    "A5": TargetSpec(
        "A5", a5, "quotient and reparameterization diagnostics", False,
        {"standard": {}},
    ),
    "kls": TargetSpec(
        "kls", bridge, "SDE-free Poincare/KLS bridge diagnostics", False,
        {"standard": {"d": 4}},
    ),
    "loc-engine": TargetSpec(
        "loc-engine", loc_engine, "legacy localization-engine regression", True,
        {
            "standard": {"ns": (2, 3, 4), "T": 0.5, "dt": 0.1,
                         "n_paths": 12, "n_bins": 1 << 15, "heavy": False},
            "full": {"ns": (2, 3, 4), "T": 0.5, "dt": 0.1,
                     "n_paths": 12, "n_bins": 1 << 15, "heavy": True},
        },
    ),
    "kls-align": TargetSpec(
        "kls-align", alignment, "product tail-union alignment diagnostic", True,
        {
            "standard": {"ns": (16, 32, 64), "T": 0.5, "dt": 0.01,
                         "n_paths": 24, "widths": (0.02, 0.05, 0.1, 0.2),
                         "alphas": (0.0, 0.5, 0.75, 0.9), "C1": 1.0,
                         "high_threshold": 2.0},
            "high-n": {"ns": (128, 256, 512, 1024), "T": 0.5, "dt": 0.01,
                       "n_paths": 32, "widths": (0.01, 0.02, 0.05, 0.1, 0.2),
                       "alphas": (0.0, 0.1, 0.25, 0.5, 0.75, 0.9), "C1": 1.0,
                       "high_threshold": 2.0},
        },
    ),
    "cmh-gate-zero": TargetSpec(
        "cmh-gate-zero", cmh_gate_zero, "deterministic CMH gate-zero battery", False,
        {"standard": {}},
    ),
}
