"""Verdicts and gates — the soundness layer.

The only sound verdict is REFUTED: a claimed upper bound C_P <= B is false if a certified
lower bound exceeds it (beyond numerical error). Everything else is direction, capped below a
proof. Gates: calibration must reproduce ground truth, and two independent estimates must agree
(convergence) — a verdict computed behind a red gate is discarded, not scored.
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
    lower: float              # certified C_P lower estimate
    status: str               # "REFUTED" | "consistent" | "no-verdict"
    tightness: float | None   # lower / B  (how close the LB is to the claim)
    note: str = ""

    def dict(self):
        return asdict(self)


def falsify(claim: str, instance: str, bound: float, lower: float, rel_tol: float = 0.10,
            note: str = "") -> Verdict:
    """REFUTED iff lower > bound*(1+rel_tol). Sound: a certified LB above the claim kills it."""
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
    """Estimate the linear-test lower bound on two independent draws; return (mean, ok)."""
    la = poincare_lower(instance.sample(n, np.random.default_rng(seed_a)))
    lb = poincare_lower(instance.sample(n, np.random.default_rng(seed_b)))
    return 0.5 * (la + lb), convergence_ok(la, lb), (la, lb)
