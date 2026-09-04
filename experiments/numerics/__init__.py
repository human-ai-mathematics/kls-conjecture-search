"""numerics — the numerical channel for the KLS program.

Role (see ../research/README.md, complementary refinement and proof channels):
  * Refine KLS *sub-statements* and gate or refute proof *approaches*
    (research/program/portfolio.yaml): produce a provenance-stamped diagnostic artifact.
    Numerics NEVER promote a statement to proved.

Soundness contract: artifacts label comparisons as exact, directional, or calibration evidence.
Their neutral outcomes are not ledger statuses. Raw Monte Carlo, MCMC, FEM, and grid estimates
are directional only; corroboration is never proof.

The headline primitive ``constants.poincare_lower`` estimates the exact linear-test quantity
``lambda_max(Cov) <= C_P``; the finite-sample output is not itself certified.
"""
from __future__ import annotations

from .constants import poincare_lower, poincare_lower_basis
from .comparison import Comparison, calibration_ok, compare_directional, compare_exact

__all__ = [
    "poincare_lower",
    "poincare_lower_basis",
    "Comparison",
    "compare_exact",
    "compare_directional",
    "calibration_ok",
]
