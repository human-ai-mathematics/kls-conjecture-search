"""Analytic reference (upper) bounds for cross-checks and assumption audits.

These are classical *upper* bounds on the Poincare constant. They are used in two ways:

  1. **as a rigorous claim in an analytic assumption check** — ``finum.verdict.falsify`` may be
     used only when the competing lower bound is itself rigorous;
  2. **as a calibration cross-check** — a directional estimate near a known exact value (e.g.
     Gaussian ``lambda_max(Sigma)``) tests the numerical pipeline but proves nothing.

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
    loose. It is an analytic comparison oracle; a raw sampled or grid estimate cannot refute it.
    """
    return float(reference_cp) * math.exp(float(osc_W))
