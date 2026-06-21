"""finum.localization — the Eldan stochastic-localization engine.

This is the **localization** regime of the KLS route-gating (research/kls/gating.md): the
per-route stochastic-localization quantities (occupation budget Xi_S, per-direction alignment,
weighted Stein source/damping) that the SDE-free `finum/targets/kls.py` defers to. It produces
**directional** evidence only — it never certifies (see research/kls/shared/target.md and the
finum soundness contract).

Numerics discipline: exact deterministic quadrature for the 1D
tilted marginals (never a Gaussian surrogate — that surrogate produced the retracted
energy-shell result), a seeded Euler-Maruyama tilt SDE, surrogate-free two-color conditional
moments (incl. the off-diagonal block), and the pathwise Brascamp-Lieb cap asserted every step.

A DIRECTIONAL number is read only after the gates pass: `gates.n_bins_convergence` (the gridded
k>=2 background has converged) and `gates.fft_vs_mc` (the FFT background agrees with independent
Monte-Carlo). A verdict behind a red gate is discarded, not scored.
"""
from __future__ import annotations

from . import cuts, gates, observables
from .cuts import (
    CutSpec,
    Psi,
    PSI_ID,
    PSI_SQ,
    balanced_threshold,
    block_sum,
    conditional_moments,
    energy_shell,
    halfspace,
    single_coord,
)
from .gates import fft_vs_mc, n_bins_convergence
from .observables import (
    Observables,
    PathIntegrals,
    R0_diag,
    ensemble_mean,
    integrate_path,
    observe,
)
from .sde import localization_path, make_rng, spawn_rngs
from .state import ProductState
from .tilt1d import GAUSSIAN, LAPLACE, Base1D, Tilted1D, tilted, tilted_variance

__all__ = [
    # bases & 1D tilted marginals
    "Base1D", "Tilted1D", "GAUSSIAN", "LAPLACE", "tilted", "tilted_variance",
    # product localization state + SDE
    "ProductState", "localization_path", "make_rng", "spawn_rngs",
    # cuts & conditional moments
    "CutSpec", "Psi", "PSI_ID", "PSI_SQ", "conditional_moments", "balanced_threshold",
    "halfspace", "single_coord", "block_sum", "energy_shell",
    # observables & occupation integrals
    "Observables", "PathIntegrals", "observe", "integrate_path", "ensemble_mean", "R0_diag",
    # gates
    "n_bins_convergence", "fft_vs_mc",
    # submodules
    "cuts", "gates", "observables",
]
