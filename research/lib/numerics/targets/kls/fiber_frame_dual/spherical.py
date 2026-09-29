"""Directional (Monte Carlo) estimator for the uniform spherical frame on H_0 = 1^perp.

The rotation-invariant frame rho = sigma_{S(H_0)} is admissible.  Its frame matrix
A_sph = d * E_theta[B_{m,k}(theta)] is estimated by seeded double Monte Carlo over
(theta, p): theta uniform on the unit sphere of H_0, p ~ Dir(1,...,1).  For each sample the
chord through p in direction theta is computed exactly (the conditional law is uniform on the
segment), and all degree-<=2k chord moments are integrated EXACTLY per sample by
Gauss-Legendre with k+1 nodes; only the outer (theta, p) average is sampled.  The integrand
(the normalized quotient matrix) is bounded on the simplex, so the plain average converges;
convergence is gated by a two-seed agreement check and by the exact linear-sector anchor
(the linear block of A_sph equals the linear block of G for every admissible frame).

Everything in this module is DIRECTIONAL evidence only.
"""
from __future__ import annotations

import numpy as np


def _leg_nodes(k: int):
    nodes, wts = np.polynomial.legendre.leggauss(k + 1)
    return nodes, wts / 2.0                      # weights of Unif[-1, 1] -> sum 1


def estimate_direction_form(m: int, k: int, basis, u, n_samples: int, rng) -> np.ndarray:
    """MC estimate of the single-direction normalized form matrix q_u on `basis`.

    `u` is a fixed direction in the sum-zero hyperplane of p-space (any nonzero scale).
    Used as an independent cross-check of the exact chamber machinery.
    """
    u = np.asarray(u, dtype=float)
    E = np.array([[a[v] for v in range(m - 1)] for a in basis], dtype=float)  # (n, m-1)
    n = len(basis)
    nodes, wts = _leg_nodes(k)
    speed_sq = m * (m + 1) * float(u @ u)        # (dT/dtau)^2, T isotropic coordinate
    acc = np.zeros((n, n))
    for _ in range(n_samples):
        p = rng.exponential(size=m)
        p /= p.sum()
        acc += _chord_quotient_matrix(p, u, E, nodes, wts, speed_sq)
    return acc / n_samples


def _chord_quotient_matrix(p, u, E, nodes, wts, speed_sq) -> np.ndarray:
    pos = u > 0
    neg = u < 0
    t_lo = np.max(-p[pos] / u[pos])              # both exist: u sums to zero, u != 0
    t_hi = np.min(-p[neg] / u[neg])
    mid = 0.5 * (t_lo + t_hi)
    half = 0.5 * (t_hi - t_lo)
    ts = mid + half * nodes                      # (k+1,)
    P = p[None, :] + ts[:, None] * u[None, :]    # (k+1, m); interior nodes: strictly positive
    V = np.exp(E @ np.log(np.maximum(P[:, :-1], 1e-300)).T)   # (n, k+1) monomial values
    meanv = V @ wts
    M2 = (V * wts[None, :]) @ V.T
    cov = M2 - np.outer(meanv, meanv)
    # Var(T | chord) = speed_sq * Var(tau) with Var(tau) = (t_hi - t_lo)^2 / 12 = half^2/3
    var_T = speed_sq * half * half / 3.0
    return cov / var_T


def spherical_frame_estimate(m: int, k: int, basis, n_samples: int, seed: int) -> np.ndarray:
    """MC estimate of A_sph = d * E_theta E_p [normalized chord quotient matrix]."""
    rng = np.random.default_rng(seed)
    E = np.array([[a[v] for v in range(m - 1)] for a in basis], dtype=float)
    n = len(basis)
    nodes, wts = _leg_nodes(k)
    speed_sq = m * (m + 1) * 1.0                 # unit direction in p-space
    acc = np.zeros((n, n))
    for _ in range(n_samples):
        p = rng.exponential(size=m)
        p /= p.sum()
        z = rng.standard_normal(m)
        u = z - z.mean()
        nrm = np.linalg.norm(u)
        if nrm < 1e-12:
            continue
        u /= nrm
        acc += _chord_quotient_matrix(p, u, E, nodes, wts, speed_sq)
    return (m - 1) * acc / n_samples
