"""Public target registry, keyed by stable CLI target id.

Each implementation module exposes:
  run_records(seed, **cfg) -> RunResult
  selftest(rng)           -> list[(name: str, ok: bool)]

The KLS route-gating batteries live in ``targets.kls``:
  "kls"     SDE-free, sound bridge/Poincare-level signals (kls/bridge.py)
  "loc-engine" legacy localization SDE diagnostics; no route observable or claim conclusion
            observables are implemented (kls/loc_engine.py)
  "kls-align" the product tail-union conj:product-alignment stress test; model-diagnostic only
              (kls/alignment.py)
  "kls-screen" the cut-local screened-supply conj:weighted-excess-rate diagnostic on the same tail-union
              localization engine: lambda_cut, W_cut, Q, the aligned set A_kappa, the
              screened supply, and the spectator-cylinder control (kls/screening.py). Its
              excess is a competitor-based SURROGATE that understates the true excess.
  "cmh-cone" the exponential-cone battery of def:exponential-cone (kls/cmh_cone/): exact
              rational gate matrices E[tau Sigma^{-1} tau] for cube cones and for cones over
              products of simplices and intervals, each stated gate inequality DECIDED in
              exact arithmetic by a symmetric-pivot LDL^T of c Sigma - M, a directional
              quadrature channel for ball cones via the radial moment-map ODE, and an exactly
              assembled CMH Galerkin quotient with one certified rational test function. Every
              value is computed FROM eq:cone-stein-kernel, whose node prop:cone-moment-map is
              open, so a disagreement indicts the formula as readily as the conjecture.
  "cmh-gate-zero" the deterministic moment-map/CMH gate-zero battery
              E[H Sigma^{-1} H] <= 4 Sigma (kls/cmh_gate_zero/) -- exact 1D Stein kernels
              and Dirichlet moment matrices, an exact algebraic countermodel, and directional
              floating generalized-eigenvalue/Galerkin diagnostics. No Monte Carlo; gate zero is
              NECESSARY, never sufficient, and an exact emitted certificate still requires
              independent proof/refutation review.
  "fiber-frame-dual" the conditional-fiber-frame all-frame simplex min-max Lambda_{m,k}
              probed by a frame library on the degree-<=k quotient (kls/fiber_frame_dual/):
              exact rational pencils and certified lower/upper bounds for root, vertex, and
              mixture frames, exact cap-descent proxies, plus a seeded directional spherical
              channel. Library lower bounds never decide the all-frame gate.
  "cmh-ab"  the anisotropic-bootstrap matrices N = int H^2, D = int H^{ab}(d_a H)(d_b H),
              R = N - D of the CMH linear-recovery probe, plus the M9 second-variation probe at
              the saturating exponential-Gaussian product (kls/cmh_ab/). Exact rational Loewner
              verdicts on one-dimensional and Dirichlet moment maps; directional quadrature on
              two-dimensional moment maps and on the perturbed CMH Rayleigh quotient. An exact
              indefinite verdict is a refutation CANDIDATE for one stated matrix inequality on
              one stated instance, never a status change.
"""
from __future__ import annotations

from ..contract import TargetSpec
from .kls import (alignment, bridge, cmh_ab, cmh_cone, cmh_gate_zero, fiber_frame_dual,
                  loc_engine, screening)

REGISTRY = {
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
    "kls-screen": TargetSpec(
        "kls-screen", screening, "cut-local screened-supply conj:weighted-excess-rate diagnostic", True,
        {
            # A uniform snapshot grid of spacing 0.05 or 0.02 fails this target's own
            # paired snapshot-refinement gate, because the surrogate excess has a steep
            # initial layer.  The run profiles use spacing 0.005 on [0,0.06] and 0.02 after.
            "smoke": {"ns": (64,), "T": 0.2, "dt": 0.005, "snapshot_stride": 4,
                      "n_paths": 4, "kappas": (0.05,), "widths": (0.04, 0.1),
                      "dense_until": 0.06,
                      "spectator_ns": (64, 128), "spectator_n0": 8,
                      "spectator_paths": 2, "spectator_stride": 4},
            "standard": {"ns": (256, 1024), "T": 0.4, "dt": 0.005, "snapshot_stride": 4,
                         "n_paths": 16, "kappas": (0.01, 0.05, 0.1, 0.25, 0.5, 1.0),
                         "widths": (0.04, 0.1, 0.2), "dense_until": 0.06,
                         "spectator_ns": (256, 1024), "spectator_n0": 32,
                         "spectator_paths": 8, "spectator_stride": 8},
            "high-n": {"ns": (1024, 4096), "T": 0.4, "dt": 0.005, "snapshot_stride": 4,
                       "n_paths": 16, "kappas": (0.01, 0.05, 0.1, 0.25, 0.5, 1.0),
                       "widths": (0.04, 0.1, 0.2), "dense_until": 0.06,
                       "spectator_ns": (256, 4096), "spectator_n0": 32,
                       "spectator_paths": 8, "spectator_stride": 8},
        },
    ),
    "cmh-cone": TargetSpec(
        "cmh-cone", cmh_cone, "exponential-cone gate matrices and CMH Galerkin battery", False,
        {
            "standard": {},
            "exact-only": {"run_ball": False},
        },
    ),
    "cmh-gate-zero": TargetSpec(
        "cmh-gate-zero", cmh_gate_zero, "deterministic CMH gate-zero battery", False,
        {"standard": {}},
    ),
    "fiber-frame-dual": TargetSpec(
        "fiber-frame-dual", fiber_frame_dual,
        "conditional-fiber-frame all-frame simplex pencil library", True,
        {
            "standard": {
                "k2_ms": (3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
                "k2_root_extra_ms": (13, 14, 15),
                "k3_ms": (3, 4, 5, 6, 7),
                "k3_root_extra_ms": (8,),
                "mixture_grid_denominator": 8,
                "spherical_k2_ms": (3, 4, 5, 6, 7, 8, 9, 10, 12),
                "spherical_k3_ms": (3, 4, 5, 6),
                "spherical_samples": 20000,
                "do_certify": True,
            },
            "deep": {
                "k2_ms": (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
                "k2_root_extra_ms": (15,),
                "k3_ms": (3, 4, 5, 6, 7, 8),
                "k3_root_extra_ms": (),
                "mixture_grid_denominator": 8,
                "spherical_k2_ms": (3, 4, 5, 6, 7, 8, 9, 10, 12, 14),
                "spherical_k3_ms": (3, 4, 5, 6, 7),
                "spherical_samples": 40000,
                "do_certify": True,
            },
        },
    ),
    "cmh-ab": TargetSpec(
        "cmh-ab", cmh_ab, "CMH anisotropic-bootstrap (N, D, R) and M9 probe", False,
        {
            "standard": {},
            "exact-only": {"run_sourcemap": False, "run_m9": False},
            "fast": {"dirichlet_alphas": ((1, 1), (1, 1, 1), (1, 1, 10)),
                     "sourcemap_base_nodes": 120,
                     "dirichlet_engine_base_nodes": 96,
                     "sourcemap_epsilons": (0.05,),
                     "sourcemap_dirichlet_alphas": ((1, 1, 1),),
                     "m9_resolution": (140, 24), "m9_degree": 4,
                     "m9_epsilons": (0.05,), "m9_enrichment": (0.4,),
                     "m9_refine_degree": 5, "m9_refine_resolution": (180, 32),
                     "m9_longitudinal": (("u-bump", 1.2, 0.8),),
                     "m9_transverse": (1, 2), "m9_shapes": (1.0, 1.5)},
        },
    ),
}
