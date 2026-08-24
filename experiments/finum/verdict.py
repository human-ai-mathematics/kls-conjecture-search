"""Analytic verdicts, directional comparisons, and numerical gates.

``falsify`` is reserved for rigorous analytic lower bounds.  Finite-sample and
finite-grid estimates use ``compare_directional``: agreement across seeds is a
useful diagnostic but is not a proof of mixing or a confidence certificate.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict

import numpy as np

from .constants import poincare_lower


@dataclass
class Verdict:
    instance: str
    claim: str                # what upper bound was tested, e.g. "C_P <= bulk_bound"
    bound: float              # B
    lower: float              # rigorous lower bound or explicitly directional estimate
    status: str               # analytic or directional status; see constructors below
    tightness: float | None   # lower / B  (how close the LB is to the claim)
    note: str = ""

    def dict(self):
        return asdict(self)


def falsify(claim: str, instance: str, bound: float, lower: float, rel_tol: float = 0.10,
            note: str = "") -> Verdict:
    """Return ``REFUTED`` only for a caller-supplied rigorous lower bound.

    This function does not certify ``lower``.  Do not pass a raw Monte Carlo, MCMC,
    FEM, or grid estimate; use :func:`compare_directional` for those quantities.
    """
    if bound is None or not np.isfinite(bound):
        status = "no-verdict"
        tight = None
    elif lower > bound * (1 + rel_tol):
        status = "REFUTED"
        tight = float(lower / bound)
    else:
        status = "consistent"
        tight = float(lower / bound)
    return Verdict(instance, claim, float(bound) if bound is not None else float("nan"),
                   float(lower), status, tight, note)


def compare_directional(claim: str, instance: str, bound: float, estimate: float,
                        rel_tol: float = 0.10, note: str = "") -> Verdict:
    """Compare a numerical estimate with a proposal without issuing a verdict."""
    if bound is None or not np.isfinite(bound):
        status = "no-comparison"
        tight = None
    elif estimate > bound * (1 + rel_tol):
        status = "directional-exceeds"
        tight = float(estimate / bound)
    else:
        status = "directional-consistent"
        tight = float(estimate / bound)
    return Verdict(instance, claim, float(bound) if bound is not None else float("nan"),
                   float(estimate), status, tight, note)


def calibration_ok(estimate: float, exact: float, rel_tol: float = 0.05) -> bool:
    """The pipeline reproduces an exact instance, or the whole run emits no verdict."""
    return abs(estimate - exact) <= rel_tol * abs(exact)


def matches(instance: str, claim: str, value: float, exact: float, rel_tol: float = 0.05) -> Verdict:
    """Calibration against a CLOSED FORM: status 'match' iff value == exact within rel_tol,
    else 'mismatch'. Used where the ground truth is an exact formula (e.g. lambda_{beta,d},
    Neal non-centered max{s^2,1}), not a falsification."""
    rel = abs(value - exact) / max(abs(exact), 1e-300)
    status = "match" if rel <= rel_tol else "mismatch"
    return Verdict(instance, claim, float(exact), float(value), status, float(value / exact)
                   if exact else None, f"rel_err={rel:.3g}")


def convergence_ok(a: float, b: float, rel_tol: float = 0.15) -> bool:
    """Two independent estimates (different seeds) must agree, else the chain is untrusted."""
    scale = max(abs(a), abs(b), 1e-12)
    return abs(a - b) <= rel_tol * scale


def two_seed_lower(instance, n: int, seed_a: int, seed_b: int):
    """Estimate the linear-test quantity twice; agreement is a directional gate only."""
    la = poincare_lower(instance.sample(n, np.random.default_rng(seed_a)))
    lb = poincare_lower(instance.sample(n, np.random.default_rng(seed_b)))
    return 0.5 * (la + lb), convergence_ok(la, lb), (la, lb)
