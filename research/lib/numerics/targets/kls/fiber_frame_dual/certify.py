"""Exact rational certification for generalized eigenvalue lower/upper bounds.

For an exact rational symmetric pencil (K, G) with G positive definite,

    lambda_min(K, G) >= lam    <=>    K - lam * G  is positive semidefinite,

so a rational `lam` for which `K - lam G` passes an EXACT positive-definiteness test is a
rigorous certified lower bound, and any exact rational Rayleigh quotient x'Kx / x'Gx is a
rigorous certified upper bound.  Floating eigensolvers only *select* the candidates.

The PD test clears denominators to integers and runs symmetric one-step Bareiss
(fraction-free) elimination; the successive pivots are the leading principal minors, and by
Sylvester's criterion the matrix is PD iff all of them are positive.  Multiplying by the
positive common denominator does not change definiteness.  The test asserts PD only when the
elimination completes with all pivots > 0; any nonpositive pivot returns False (which is a
"retry with a smaller lam", never a certified claim of indefiniteness).
"""
from __future__ import annotations

from fractions import Fraction
from math import gcd

import numpy as np
from scipy.linalg import eigh


def _lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b


def to_integer_matrix(M) -> list[list[int]]:
    """Scale a rational symmetric matrix by the positive lcm of denominators."""
    den = 1
    for row in M:
        for v in row:
            den = _lcm(den, v.denominator)
    return [[int(v * den) for v in row] for row in M]


def bareiss_positive_definite(M) -> bool:
    """Exact PD test (Sylvester via fraction-free Bareiss). True is a certificate; False is
    only "no certificate at this lam"."""
    A = [row[:] for row in to_integer_matrix(M)]
    n = len(A)
    prev = 1
    for k in range(n):
        piv = A[k][k]
        if piv <= 0:
            return False
        for i in range(k + 1, n):
            aik = A[k][i]                       # symmetric intermediate: A[i][k] == A[k][i]
            rowi = A[i]
            rowk = A[k]
            for j in range(i, n):
                rowi[j] = (piv * rowi[j] - aik * rowk[j]) // prev
        prev = piv
    return True


def quadratic_form(M, x) -> Fraction:
    n = len(x)
    tot = Fraction(0)
    for i in range(n):
        xi = x[i]
        if xi == 0:
            continue
        row = M[i]
        tot += xi * xi * row[i]
        acc = Fraction(0)
        for j in range(i + 1, n):
            if x[j]:
                acc += row[j] * x[j]
        tot += 2 * xi * acc
    return tot


def pencil_min_eig_float(K_ex, G_ex):
    """Floating minimal generalized eigenvalue and eigenvector of the exact pencil."""
    Kf = np.array([[float(v) for v in row] for row in K_ex])
    Gf = np.array([[float(v) for v in row] for row in G_ex])
    dsc = 1.0 / np.sqrt(np.diag(Gf))
    Ks = 0.5 * (Kf * dsc[:, None] * dsc[None, :] + (Kf * dsc[:, None] * dsc[None, :]).T)
    Gs = 0.5 * (Gf * dsc[:, None] * dsc[None, :] + (Gf * dsc[:, None] * dsc[None, :]).T)
    vals, vecs = eigh(Ks, Gs)
    return float(vals[0]), dsc * vecs[:, 0]


RAYLEIGH_MAX_DENOMINATOR = 10 ** 8
LOWER_MAX_DENOMINATOR = 10 ** 8
LOWER_DELTA_LADDER = (1e-9, 1e-7, 1e-5, 1e-3, 1e-2, 5e-2)


def rationalize_vector(v) -> list[Fraction]:
    v = np.asarray(v, dtype=float)
    pivot = int(np.argmax(np.abs(v)))
    if v[pivot] == 0.0:
        raise ArithmeticError("zero eigenvector from the floating solver")
    return [Fraction(float(x / v[pivot])).limit_denominator(RAYLEIGH_MAX_DENOMINATOR)
            for x in v]


def certify_lambda_min(K_ex, G_ex, g_known_pd: bool = False) -> dict:
    """Certified enclosure of lambda_min(K, G).

    Returns a dict with the floating value, an exact Rayleigh upper bound, and (when the PD
    ladder succeeds) an exact certified lower bound.  `g_known_pd=True` skips re-certifying G.
    """
    if not g_known_pd and not bareiss_positive_definite(G_ex):
        raise ArithmeticError("Gram matrix failed the exact PD test; pencil is ill-posed")
    lam_f, vec = pencil_min_eig_float(K_ex, G_ex)
    x = rationalize_vector(vec)
    upper = quadratic_form(K_ex, x) / quadratic_form(G_ex, x)

    lower = None
    attempts = []
    for delta in LOWER_DELTA_LADDER:
        cand = Fraction(lam_f * (1.0 - delta)).limit_denominator(LOWER_MAX_DENOMINATOR)
        if cand <= 0 or cand >= upper:
            attempts.append({"delta": delta, "candidate": str(cand), "tried": False})
            continue
        shifted = [[K_ex[i][j] - cand * G_ex[i][j] for j in range(len(K_ex))]
                   for i in range(len(K_ex))]
        ok = bareiss_positive_definite(shifted)
        attempts.append({"delta": delta, "candidate": str(cand), "tried": True, "pd": ok})
        if ok:
            lower = cand
            break
    return {
        "lambda_float": lam_f,
        "lambda_upper_exact": upper,
        "lambda_lower_exact": lower,
        "certificate": {
            "upper": {"type": "exact-rational-rayleigh",
                      "arithmetic": "fractions.Fraction",
                      "witness_max_denominator": RAYLEIGH_MAX_DENOMINATOR,
                      "value": str(upper)},
            "lower": (None if lower is None else
                      {"type": "exact-bareiss-sylvester-PD of K - lam*G",
                       "arithmetic": "integer fraction-free Bareiss",
                       "lam": str(lower)}),
            "ladder": attempts,
        },
    }
