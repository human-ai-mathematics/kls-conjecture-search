"""The gate matrix of an exponential cone measure, in exact rational arithmetic.

For ``X = S(1,U)`` with ``S ~ Gamma(beta,1)``, ``U ~ Unif(K)`` independent, write
``tau(x - beta e_1) = s T(u)`` with

    T(u) = [[1, u^T], [u, u u^T + beta tau_K(u)]]                 (eq:cone-stein-kernel)

and ``Sigma = beta e_1 e_1^T (+) beta(beta+1) Cov(U)``            (eq:cone-covariance).

Since ``s`` and ``u`` are independent and ``E[s^2] = beta(beta+1)``, the gate matrix is

    M = E[tau Sigma^{-1} tau] = beta(beta+1) E_u[ T Sigma^{-1} T ],

every entry of which is a polynomial moment of ``u`` of degree at most four -- rational
for every base this package implements.  The reported quantity is the largest eigenvalue
of the pencil ``(M, Sigma)``, equal to ``lambda_max(Sigma^{-1/2} M Sigma^{-1/2})`` and
invariant under every invertible linear change of coordinates, so no square root is ever
taken.  ``conj:gate-zero-sharp`` asserts it is at most 2 and ``conj:gate-zero`` at most 4.

The gate matrix is computed from eq:cone-stein-kernel, which is Proposition
prop:cone-moment-map -- an *open* ledger node.  Everything here therefore tests the
conjecture *given* that formula; it does not verify the formula.
"""
from __future__ import annotations

from fractions import Fraction

import numpy as np
from scipy.linalg import eigh

from . import linalg as la
from . import polys as P


def stein_matrix(base, beta: int):
    """``T(u)`` as an ``n x n`` matrix of polynomials in ``u``, ``n = base.m + 1``."""
    m = base.m
    n = m + 1
    tau_K = base.tau()
    T = [[dict() for _ in range(n)] for _ in range(n)]
    zeros = (0,) * m
    T[0][0] = {(0, zeros): Fraction(1)}
    for j in range(m):
        e = [0] * m
        e[j] = 1
        T[0][j + 1] = T[j + 1][0] = {(0, tuple(e)): Fraction(1)}
    for i in range(m):
        for j in range(m):
            e = [0] * m
            e[i] += 1
            e[j] += 1
            entry = {(0, tuple(e)): Fraction(1)}
            entry = P.padd(entry, tau_K[i][j], Fraction(beta))
            T[i + 1][j + 1] = entry
    return T


def gate_pencil(base, beta: int):
    """Exact ``(M, Sigma)`` for the cone over ``base`` with radial exponent ``beta``."""
    m = base.m
    n = m + 1
    beta = int(beta)
    if beta < n:
        raise ValueError(f"log-concavity needs beta >= n; got beta={beta}, n={n}")
    cov_u = base.cov()
    Sigma = [[Fraction(0)] * n for _ in range(n)]
    Sigma[0][0] = Fraction(beta)
    for i in range(m):
        for j in range(m):
            Sigma[i + 1][j + 1] = Fraction(beta) * (beta + 1) * cov_u[i][j]
    Sigma_inv = la.inverse(Sigma)

    T = stein_matrix(base, beta)
    # M = beta(beta+1) E[ T Sigma^{-1} T ], assembled entrywise on polynomials in u.
    half = [[dict() for _ in range(n)] for _ in range(n)]      # T Sigma^{-1}
    for i in range(n):
        for j in range(n):
            acc: dict = {}
            for t in range(n):
                if Sigma_inv[t][j]:
                    acc = P.padd(acc, T[i][t], Sigma_inv[t][j])
            half[i][j] = acc
    M = [[Fraction(0)] * n for _ in range(n)]
    scale = Fraction(beta) * (beta + 1)
    for i in range(n):
        for j in range(i, n):
            acc: dict = {}
            for t in range(n):
                acc = P.padd(acc, P.pmul(half[i][t], T[t][j]))
            value = scale * sum((c * base.moment(b) for (_, b), c in acc.items()),
                                Fraction(0))
            M[i][j] = M[j][i] = value
    return M, Sigma


def pencil_spectrum(M, Sigma):
    """Floating generalized eigenvalues of ``(M, Sigma)`` -- directional cross-check."""
    Mf = np.array(la.to_float(M))
    Sf = np.array(la.to_float(Sigma))
    scale = 1.0 / np.sqrt(np.diag(Sf))
    Mf = Mf * scale[:, None] * scale[None, :]
    Sf = Sf * scale[:, None] * scale[None, :]
    vals, vecs = eigh(0.5 * (Mf + Mf.T), 0.5 * (Sf + Sf.T))
    top = scale * vecs[:, -1]
    return vals, top


def rationalize(vector, max_denominator: int):
    pivot = int(np.argmax(np.abs(vector)))
    if vector[pivot] == 0:
        raise ArithmeticError("floating eigensolver returned the zero vector")
    return [Fraction.from_float(float(x / vector[pivot])).limit_denominator(max_denominator)
            for x in vector]
