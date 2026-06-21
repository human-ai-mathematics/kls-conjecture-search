"""Analytic reference (upper) bounds — as cross-checks and refutable claims, NOT proofs.

These are the classical *upper* bounds on the Poincare constant. finum's soundness contract says
numerics certify only LOWER bounds (refutation); an analytic upper bound is therefore used here
in exactly two sound ways:

  1. **as the claim a run tries to refute** — feed the value as ``B`` to ``finum.verdict.falsify``
     against the certified lower bound; if ``poincare_lower > B`` the bound (as stated/applied)
     is REFUTED;
  2. **as a corroboration cross-check** — a lower bound that sits just under a known-correct upper
     bound (e.g. Gaussian: both equal ``lambda_max(Sigma)``) calibrates the estimator.

They are NOT certificates: returning a number here never promotes a node to proved.
"""
from __future__ import annotations

import math


def bakry_emery_cp(hessian_lower_bound: float) -> float:
    """Bakry-Emery upper bound ``C_P <= 1/m`` for a measure with ``Hess U >= m I``, ``m > 0``.

    For ``N(0, Sigma)`` this is ``1/lambda_min(Sigma^{-1}) = lambda_max(Sigma)`` — exact, hence a
    calibration cross-check. For a strongly-log-concave perturbation it is a genuine upper claim
    a stress run can try to refute.
    """
    if hessian_lower_bound <= 0:
        return math.inf
    return 1.0 / hessian_lower_bound


def holley_stroock_cp(reference_cp: float, osc_W: float) -> float:
    """Holley-Stroock bounded-perturbation transfer: ``C_P(pi) <= C_P(nu) * exp(osc(W))``.

    For ``pi propto exp(-W) nu`` with oscillation ``osc(W)``. The ``exp(osc)`` factor is famously
    loose, so this upper bound is a prime *refutation target*: a certified lower bound rarely
    approaches it, and where the transfer is misapplied the lower bound can exceed it.
    """
    return float(reference_cp) * math.exp(float(osc_W))
