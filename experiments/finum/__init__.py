"""finum — the numerical channel for the functional-inequalities open targets.

Role (see ../research/README.md, complementary refinement and proof channels):
  * Part II  — refine and stress-test *statements* (A1-A5): produce a provenance-stamped
               diagnostic artifact. Numerics NEVER promote a statement to proved.
  * Part III — the same core later refines KLS *sub-statements* and gates/refutes proof
               *routes* (research/kls/routes.md).

Soundness contract: uppercase ``REFUTED`` is reserved for an exact or rigorously certified
analytic lower bound. Raw Monte Carlo, MCMC, FEM, and grid estimates are directional only.
Corroboration is bounded evidence, never proof.

The headline primitive ``constants.poincare_lower`` estimates the exact linear-test quantity
``lambda_max(Cov) <= C_P``; the finite-sample output is not itself certified.
"""
from __future__ import annotations

from .constants import poincare_lower, poincare_lower_basis
from .verdict import Verdict, calibration_ok, compare_directional, falsify

__all__ = [
    "poincare_lower",
    "poincare_lower_basis",
    "Verdict",
    "falsify",
    "compare_directional",
    "calibration_ok",
]
