"""MALA sampler (numpy-only) for posteriors without a closed-form draw (the GLM stress cases).

Plain MALA mixes badly on anisotropic / near-flat posteriors (exactly the obs:flat-direction
stress cases), so we provide *preconditioned* MALA and an adaptive wrapper: a pilot run under a
curvature preconditioner estimates the covariance, then the main run is preconditioned by that
estimate — which can capture flat directions a fixed-metric chain misses. The two-seed agreement
check in ``numerics.comparison`` is a diagnostic gate, not a mixing proof or confidence certificate;
if it fails, no downstream sampled diagnostic is emitted.
"""
from __future__ import annotations

from typing import Callable

import numpy as np


def sigmoid(s):
    """Numerically stable logistic function used by the GLM diagnostics."""
    return 0.5 * (1.0 + np.tanh(0.5 * s))


def mala(
    grad_logp: Callable[[np.ndarray], np.ndarray],
    logp: Callable[[np.ndarray], float],
    x0: np.ndarray,
    n_samples: int,
    rng: np.random.Generator,
    step: float = 1e-2,
    burn: int = 2000,
    thin: int = 5,
    precond: np.ndarray | None = None,
) -> np.ndarray:
    """Metropolis-adjusted Langevin with optional SPD preconditioner P (proposal metric).

    Proposal: x' = x + step*P*grad + sqrt(2 step) * chol(P) z ; accept with the P-metric
    Hastings correction. Returns (n_samples, d) post-burn, thinned draws.
    """
    x = np.asarray(x0, dtype=float).copy()
    d = x.size
    if precond is None:
        P = np.eye(d)
        Lp = np.eye(d)
        Pinv = np.eye(d)
    else:
        P = np.asarray(precond, dtype=float)
        Lp = np.linalg.cholesky(P)
        Pinv = np.linalg.inv(P)

    def logq(b, a, ga):
        r = b - a - step * (P @ ga)
        return -(r @ Pinv @ r) / (4 * step)

    lp = logp(x)
    g = grad_logp(x)
    out = np.empty((n_samples, d))
    got = it = 0
    total = burn + n_samples * thin
    while got < n_samples:
        z = rng.standard_normal(d)
        prop = x + step * (P @ g) + np.sqrt(2 * step) * (Lp @ z)
        gp = grad_logp(prop)
        lpp = logp(prop)
        log_alpha = lpp - lp + logq(x, prop, gp) - logq(prop, x, g)
        if np.log(rng.random()) < log_alpha:
            x, lp, g = prop, lpp, gp
        it += 1
        if it > burn and (it - burn) % thin == 0:
            out[got] = x
            got += 1
        if it > total + 20 * n_samples:   # safety valve
            out[got:] = x
            break
    return out


def mala_adaptive(
    grad_logp: Callable[[np.ndarray], np.ndarray],
    logp: Callable[[np.ndarray], float],
    x0: np.ndarray,
    n_samples: int,
    rng: np.random.Generator,
    init_precond: np.ndarray,
    pilot_frac: float = 0.4,
) -> np.ndarray:
    """Pilot under `init_precond` (curvature), estimate Cov, main run preconditioned by it."""
    d = x0.size
    n_pilot = max(800, int(pilot_frac * n_samples))
    pilot = mala(grad_logp, logp, x0, n_pilot, rng,
                 step=0.4 / d, burn=2000, thin=4, precond=init_precond)
    C = np.cov(pilot, rowvar=False)
    C = np.atleast_2d(C)
    C = C + 1e-6 * np.trace(C) / d * np.eye(d)        # ridge for SPD
    x_start = pilot[-1]
    return mala(grad_logp, logp, x_start, n_samples, rng,
                step=0.5 / d, burn=3000, thin=8, precond=C)
