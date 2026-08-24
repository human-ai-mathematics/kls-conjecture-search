"""Directional estimators for Poincare Rayleigh quotients.

For exact expectations, every test function gives the rigorous lower bound
``R[f] <= C_P``.  The routines below replace those expectations by finite-sample
averages.  Their outputs are therefore Monte Carlo estimates of lower-bound
quantities, not certified lower bounds themselves: sampling error and, for MCMC,
mixing bias can move an estimate in either direction.

``poincare_lower(samples)`` estimates the linear-test quantity
``lambda_max(Cov_pi)``; ``poincare_lower_basis(samples)`` estimates a richer
finite-basis Rayleigh quotient.  Both take samples of shape ``(N, d)``.
"""
from __future__ import annotations

import numpy as np


def poincare_lower(samples: np.ndarray) -> float:
    """Estimate ``lambda_max(Cov_pi)``, an exact analytic lower bound on ``C_P``.

    The returned empirical-covariance eigenvalue is directional unless accompanied
    by a rigorous sampling-error and, when relevant, mixing-error bound.
    """
    x = np.asarray(samples, dtype=float)
    if x.ndim != 2:
        raise ValueError("samples must be (N, d)")
    cov = np.cov(x, rowvar=False)
    cov = np.atleast_2d(cov)
    return float(np.linalg.eigvalsh(cov)[-1])


def _quadratic_features(x: np.ndarray):
    """Centered quadratic features and their gradients.

    Features phi_{ij}(theta) = theta_i theta_j (i<=j), centered to zero empirical mean.
    grad phi_{ij} = theta_i e_j + theta_j e_i  (independent of the centering constant).
    Returns (Phi, G) where Phi is (N, k) centered values and G is the (k, d, ...) gradient
    tensor folded into the Dirichlet Gram below.
    """
    N, d = x.shape
    pairs = [(i, j) for i in range(d) for j in range(i, d)]
    Phi = np.empty((N, len(pairs)))
    # gradient of each quadratic feature at each sample: (N, k, d)
    grad = np.zeros((N, len(pairs), d))
    for c, (i, j) in enumerate(pairs):
        Phi[:, c] = x[:, i] * x[:, j]
        grad[:, c, i] += x[:, j]
        grad[:, c, j] += x[:, i]
    Phi -= Phi.mean(axis=0, keepdims=True)
    return Phi, grad


def poincare_lower_basis(samples: np.ndarray, ridge: float = 1e-9) -> float:
    """Estimate a richer linear-plus-quadratic Rayleigh lower-bound quantity.

    Solves the generalized eigenproblem  V c = lambda G c  where
      V = Cov of the (centered) features      [Var of f]
      G = mean of <grad phi_a, grad phi_b>    [E||grad f||^2]
    With exact expectations the largest generalized eigenvalue is at most ``C_P``.
    Its empirical counterpart is directional, for the same reason as
    :func:`poincare_lower`.
    Falls back to poincare_lower() if the (quadratic) Gram is too ill-conditioned.
    """
    x = np.asarray(samples, dtype=float)
    if x.ndim != 2:
        raise ValueError("samples must be (N, d)")
    N, d = x.shape

    # linear block: features theta_i (centered), gradients e_i  => V=Cov, G=I
    lin = x - x.mean(axis=0, keepdims=True)
    Lgrad = np.tile(np.eye(d), (N, 1, 1))  # (N, d, d)

    quad, Qgrad = _quadratic_features(x)
    Phi = np.concatenate([lin, quad], axis=1)            # (N, k)
    grad = np.concatenate([Lgrad, Qgrad], axis=1)        # (N, k, d)

    V = np.cov(Phi, rowvar=False)
    V = np.atleast_2d(V)
    # G_ab = mean_n sum_m grad[n,a,m] grad[n,b,m]
    G = np.einsum("nam,nbm->ab", grad, grad) / N
    k = V.shape[0]
    G = G + ridge * np.trace(G) / k * np.eye(k)
    try:
        L = np.linalg.cholesky(G)
        Linv = np.linalg.inv(L)
        M = Linv @ V @ Linv.T
        M = 0.5 * (M + M.T)
        return float(np.linalg.eigvalsh(M)[-1])
    except np.linalg.LinAlgError:
        return poincare_lower(x)


def poincare_1d_fem(U, xs: np.ndarray, a=None) -> float:
    """Finite-domain FEM approximation to a one-dimensional Poincare constant.

    P1 finite elements: solve the generalized eigenproblem K v = lambda M v with
    M_ij = ∫ phi_i phi_j dmu   (mass, weight e^{-U})
    K_ij = ∫ a phi_i' phi_j' dmu   (stiffness, weight a(x) e^{-U}).
    The smallest eigenvalue is 0 (constant mode); the discretized constant is
    ``1 / lambda_1``.  Without truncation and discretization error bounds this is a
    directional approximation, not a certified two-sided value.

    a=None gives the unweighted Poincare (U = x^2/(2 s^2) reproduces C_P = s^2). For the
    heavy-tail / A3 weighted inequality Var(f) <= C int a |f'|^2 dmu pass a(x) (e.g. 1+x^2):
    then the return value is the sharp weighted constant C_P^w (= lambda_{beta,d}^{-1} for the
    generalized Cauchy family, thm:a3-student).
    """
    xs = np.asarray(xs, dtype=float)
    n = xs.size
    w = np.exp(-np.asarray(U(xs), dtype=float))
    av = np.ones(n) if a is None else np.asarray(a(xs), dtype=float)

    # assemble the TRIDIAGONAL P1 stiffness/mass bands (O(n) memory)
    h = np.diff(xs)
    we = 0.5 * (w[:-1] + w[1:])                    # element-averaged weight e^{-U}
    ae = 0.5 * (av[:-1] + av[1:])                  # element-averaged Dirichlet weight a
    ck = we * ae / h                               # per-element stiffness scale
    cm = we * h / 6.0                              # per-element mass scale
    Kd = np.zeros(n); Ko = -ck                     # K diagonal / off-diagonal
    Kd[:-1] += ck; Kd[1:] += ck
    Md = np.zeros(n); Mo = cm                       # consistent mass diagonal / off-diagonal
    Md[:-1] += 2 * cm; Md[1:] += 2 * cm

    # lumped (row-sum) mass -> reduce to a SYMMETRIC TRIDIAGONAL standard problem
    # S = D^{-1/2} K D^{-1/2}, with D the lumped mass; smallest nonzero eig = spectral gap.
    Dl = Md.copy(); Dl[:-1] += Mo; Dl[1:] += Mo
    dinv = 1.0 / np.sqrt(Dl)
    Sd = Kd * dinv * dinv
    So = Ko * dinv[:-1] * dinv[1:]
    try:
        from scipy.linalg import eigh_tridiagonal
        vals = eigh_tridiagonal(Sd, So, select="i", select_range=(0, 1),
                                eigvals_only=True)
        lam1 = vals[1]
    except ImportError:                            # numpy fallback (dense; small n only)
        T = np.diag(Sd) + np.diag(So, 1) + np.diag(So, -1)
        lam1 = np.linalg.eigvalsh(T)[1]
    return float(1.0 / lam1)


def hardy_1d(p: np.ndarray, a: np.ndarray, xs: np.ndarray, m: float | None = None):
    """1D weighted Hardy/Muckenhoupt criterion (thm:hardy-1d) on the grid `xs`.

    For a density p with weight a in the Dirichlet form Var_mu(f) <= C int a |f'|^2 dmu, the
    optimal constant is pinned up to a factor 4 by
      B_+ = sup_{x>m} ( int_x^inf p ) ( int_m^x dt / (a p) ),
      B_- = sup_{x<m} ( int_-inf^x p ) ( int_x^m dt / (a p) ),
    with max(B_+,B_-) <= C_opt <= 4 max(B_+,B_-). `m` is the median (computed if None).
    Returns (B_plus, B_minus, B_max). Handles the integrable 1/(a p) singularity by trapezoid
    on the grid (refine xs near a pole, e.g. the horseshoe log-pole at 0, for accuracy).
    """
    xs = np.asarray(xs, dtype=float)
    p = np.asarray(p, dtype=float)
    a = np.asarray(a, dtype=float)
    p = p / np.trapezoid(p, xs)                    # normalize to a probability density
    cdf = np.concatenate([[0.0], np.cumsum(0.5 * (p[1:] + p[:-1]) * np.diff(xs))])
    tail_lo = cdf                                   # mu((-inf, x])
    tail_hi = cdf[-1] - cdf                         # mu([x, inf))
    inv = 1.0 / (a * p)                             # 1/(a p)
    # cumulative int_{xs[0]}^x dt/(a p)
    I = np.concatenate([[0.0], np.cumsum(0.5 * (inv[1:] + inv[:-1]) * np.diff(xs))])
    if m is None:
        m = float(np.interp(0.5, cdf, xs))         # median
    Im = float(np.interp(m, xs, I))
    right = xs > m
    left = xs < m
    B_plus = float(np.max(tail_hi[right] * (I[right] - Im))) if right.any() else 0.0
    B_minus = float(np.max(tail_lo[left] * (Im - I[left]))) if left.any() else 0.0
    return B_plus, B_minus, max(B_plus, B_minus)
