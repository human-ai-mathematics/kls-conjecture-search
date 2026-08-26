"""finum.localization — the Eldan stochastic-localization engine.

This is the numerical engine beneath the **localization diagnostic** channels. The legacy
``loc-engine`` target provides source occupation and two-color engine checks but does not assemble
the open-node observables. The separate ``kls-align`` target now assembles ``S_high,r,D`` for the
specific product-Laplace tail-union stress model. Both remain diagnostics, not proof evidence.

Numerics discipline: exact deterministic quadrature for the 1D
tilted marginals (never a Gaussian surrogate — that surrogate produced the retracted
energy-shell result), a seeded Euler-Maruyama tilt SDE, surrogate-free two-color conditional
moments (incl. the off-diagonal block), and the pathwise Brascamp-Lieb cap asserted every step.

A thin-shell occupation number is inspectable only behind the target's full gate set: Gaussian
calibration, `gates.n_bins_convergence`, `gates.fft_vs_mc`, and time-step refinement. Missing or
red gates make the assessment unavailable; all-green output remains diagnostic until a route
observable is implemented.
"""
from __future__ import annotations

from . import alignment, cuts, gates, observables, tail_union
from .alignment import (
    AlignmentPathIntegrals,
    FilteringTrajectory,
    filtering_trajectory,
    grid_intervals,
    integrate_alignment_path,
)
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
from .tail_union import (
    SymmetricTruncationMoments,
    TailUnionObservables,
    balanced_tail_radius,
    observe_tail_union,
    tilted_laplace_symmetric_truncation,
)
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
    # product tail-union q:alignment diagnostic
    "SymmetricTruncationMoments", "TailUnionObservables", "balanced_tail_radius",
    "tilted_laplace_symmetric_truncation", "observe_tail_union",
    "FilteringTrajectory", "AlignmentPathIntegrals", "filtering_trajectory",
    "integrate_alignment_path", "grid_intervals",
    # submodules
    "alignment", "cuts", "gates", "observables", "tail_union",
]
