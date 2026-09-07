"""Exact rational linear algebra: inverse, LDL^T, and a Loewner (PSD) certificate.

Everything here is ``fractions.Fraction`` arithmetic on symmetric matrices.  The point of
:func:`psd_certificate` is that it *decides* ``A >= 0``: a complete symmetric-pivot LDL^T
with nonnegative pivots proves ``A >= 0``, while the first negative pivot -- or a zero
diagonal facing a nonzero off-diagonal entry, whose 2x2 principal minor is then strictly
negative -- proves a negative direction and returns the exact rational vector realising
it.  Applied to ``c Sigma - E[tau Sigma^{-1} tau]`` this decides the gate inequality on
one instance in exact arithmetic, in both directions.

An exact verdict is still only a *candidate* until an independently reviewed dossier
states it (CLAUDE.md constraint 2).
"""
from __future__ import annotations

from fractions import Fraction


def eye(n: int):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def matmul(A, B):
    n, k, p = len(A), len(B), len(B[0])
    return [[sum((A[i][t] * B[t][j] for t in range(k)), Fraction(0)) for j in range(p)]
            for i in range(n)]


def matsub(A, B, scale=1):
    """``A - scale * B``, exact."""
    scale = Fraction(scale)
    return [[A[i][j] - scale * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def is_symmetric(A) -> bool:
    n = len(A)
    return all(A[i][j] == A[j][i] for i in range(n) for j in range(i + 1, n))


def inverse(A):
    """Exact Gauss-Jordan inverse of a rational matrix."""
    n = len(A)
    identity = eye(n)
    work = [list(map(Fraction, row)) + identity[i] for i, row in enumerate(A)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if work[r][col] != 0), None)
        if pivot is None:
            raise ValueError("matrix is exactly singular")
        work[col], work[pivot] = work[pivot], work[col]
        piv = work[col][col]
        work[col] = [x / piv for x in work[col]]
        for r in range(n):
            if r != col and work[r][col]:
                factor = work[r][col]
                work[r] = [x - factor * y for x, y in zip(work[r], work[col])]
    return [row[n:] for row in work]


def ldl(A):
    """``A = L D L^T`` with unit-lower ``L`` and rational pivots ``D``; ``A`` must be PD.

    Used to split ``<v, A v> = sum_a D_a (L^T v)_a^2`` into squares without taking a
    square root, which is what keeps the CMH numerator assembly rational.
    """
    n = len(A)
    work = [list(map(Fraction, row)) for row in A]
    L = eye(n)
    pivots: list[Fraction] = []
    for step in range(n):
        piv = work[step][step]
        if piv <= 0:
            raise ValueError("ldl requires a positive definite matrix")
        pivots.append(piv)
        for i in range(step + 1, n):
            factor = work[i][step] / piv
            L[i][step] = factor
            if factor:
                for j in range(step, n):
                    work[i][j] -= factor * work[step][j]
    return L, pivots


def psd_certificate(A):
    """Decide ``A >= 0`` exactly; return ``(is_psd, pivots, witness)``.

    ``witness`` is ``None`` when ``A >= 0``; otherwise it is an exact rational vector
    ``v`` in the original coordinates with ``v^T A v < 0``.
    """
    n = len(A)
    if not is_symmetric(A):
        raise ValueError("psd_certificate input is not exactly symmetric")
    work = [list(map(Fraction, row)) for row in A]
    basis = eye(n)                    # basis[i]^T A basis[j] == work[i][j] at every step
    pivots: list[Fraction] = []
    for step in range(n):
        best = max(range(step, n), key=lambda r: work[r][r])
        if best != step:
            work[step], work[best] = work[best], work[step]
            for row in work:
                row[step], row[best] = row[best], row[step]
            basis[step], basis[best] = basis[best], basis[step]
        piv = work[step][step]
        pivots.append(piv)
        if piv < 0:
            return False, pivots, basis[step]
        if piv == 0:
            bad = next((j for j in range(step + 1, n) if work[step][j] != 0), None)
            if bad is None:
                continue              # this direction and all it meets are in the kernel
            x, d = work[step][bad], work[bad][bad]
            t = -(d + 1) / (2 * x)    # v^T A v = 2 t x + d = -1 < 0
            return False, pivots, [t * a + b for a, b in zip(basis[step], basis[bad])]
        for i in range(step + 1, n):
            factor = work[i][step] / piv
            if factor:
                for j in range(step, n):
                    work[i][j] -= factor * work[step][j]
                basis[i] = [bi - factor * bs for bi, bs in zip(basis[i], basis[step])]
        for i in range(step + 1, n):
            work[step][i] = work[i][step] = Fraction(0)
    return True, pivots, None


def quadratic(A, v):
    """``v^T A v`` in exact arithmetic."""
    n = len(v)
    return sum((v[i] * A[i][j] * v[j] for i in range(n) for j in range(n)), Fraction(0))


def to_float(A):
    return [[float(x) for x in row] for row in A]
