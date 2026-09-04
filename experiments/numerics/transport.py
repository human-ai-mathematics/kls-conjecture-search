"""1D transport quantities for A4 (variational-inference transport constants).

Everything is grid-based on a shared `xs`. The transport constants compare a variational family
member q to the target pi via the ratio W_2^2(q,pi) / (2 KL(q||pi)); the supremum over a family
is C_Q (eq:a4-cq), over a KL-sublevel C_{Q,r} (eq:a4-cqr). The obs:restricted-not-finite demo:
for pi ~ e^{-|x|^p}, 1<=p<2, and Gaussians q_m=N(m,sigma^2), W_2^2/KL ~ |m|^{2-p} -> inf, so the
global C_Q is infinite while C_{Q,r} on a KL-sublevel stays finite.
"""
from __future__ import annotations

import numpy as np


def normalize(p: np.ndarray, xs: np.ndarray) -> np.ndarray:
    p = np.clip(np.asarray(p, dtype=float), 0.0, None)
    return p / np.trapezoid(p, xs)


def gauss_density(xs: np.ndarray, m: float, s: float) -> np.ndarray:
    return np.exp(-0.5 * ((xs - m) / s) ** 2) / (s * np.sqrt(2 * np.pi))


def cdf(p: np.ndarray, xs: np.ndarray) -> np.ndarray:
    p = normalize(p, xs)
    return np.concatenate([[0.0], np.cumsum(0.5 * (p[1:] + p[:-1]) * np.diff(xs))])


def kl_1d(q: np.ndarray, pi: np.ndarray, xs: np.ndarray) -> float:
    """KL(q || pi) = int q log(q/pi) dx on the grid (densities need not be pre-normalized)."""
    q = normalize(q, xs)
    pi = normalize(pi, xs)
    mask = q > 1e-300
    integrand = np.zeros_like(q)
    integrand[mask] = q[mask] * np.log(q[mask] / np.clip(pi[mask], 1e-300, None))
    return float(np.trapezoid(integrand, xs))


def w2_sq_1d(q: np.ndarray, pi: np.ndarray, xs: np.ndarray, m_grid: int = 4000) -> float:
    """W_2^2(q, pi) in 1D via the quantile L^2 distance int_0^1 (Q_q(u)-Q_pi(u))^2 du."""
    Fq, Fpi = cdf(q, xs), cdf(pi, xs)
    us = np.linspace(1e-4, 1 - 1e-4, m_grid)
    Qq = np.interp(us, Fq, xs)
    Qpi = np.interp(us, Fpi, xs)
    return float(np.trapezoid((Qq - Qpi) ** 2, us))


def transport_ratio(qs: list[np.ndarray], pi: np.ndarray, xs: np.ndarray):
    """For each q in `qs`: (kl, w2_sq, ratio = w2_sq/(2 kl)). Returns the list of dicts."""
    out = []
    for q in qs:
        kl = kl_1d(q, pi, xs)
        w2 = w2_sq_1d(q, pi, xs)
        ratio = w2 / (2 * kl) if kl > 1e-12 else float("nan")
        out.append({"kl": kl, "w2_sq": w2, "ratio": ratio})
    return out
