"""Exact rational Loewner-order primitives for the anisotropic-bootstrap battery.

Everything here is `fractions.Fraction` arithmetic.  Two kinds of self-contained certificate are
emitted, both re-checkable by a reader who has only the artifact:

* ``psd_certificate`` -- a symmetric-pivot LDL^T factorization.  All pivots ``>= 0`` proves
  ``M >= 0``; a strictly negative pivot proves ``M`` indefinite.  The permutation, the unit lower
  triangular factor, and the pivots are recorded, so ``P M P^T = L D L^T`` can be recomputed.
* ``negativity_witness`` -- an explicit rational vector ``v`` together with the exact value
  ``v^T M v < 0``.  This is the cheapest possible independent refutation certificate and is the
  only artifact field a refutation dossier should quote.

Exactness of the arithmetic is *not* a proof of anything mathematical: it certifies only that the
displayed number is the displayed quantity for the displayed instance.  Whether that instance is
an admissible member of the mathematical class, and what a sign means for a conjecture, is
decided in the proof/refutation workflow, never here.
"""
from __future__ import annotations

from fractions import Fraction

import numpy as np


WITNESS_MAX_DENOMINATOR = 1_000_000


# ---------------------------------------------------------------------------------------
# conversions
# ---------------------------------------------------------------------------------------

def frac_payload(value: Fraction) -> dict[str, int]:
    if not isinstance(value, Fraction):
        raise TypeError("exact payloads must be fractions.Fraction instances")
    return {"numerator": value.numerator, "denominator": value.denominator}


def frac_from_payload(payload) -> Fraction:
    return Fraction(int(payload["numerator"]), int(payload["denominator"]))


def matrix_payload(matrix) -> list[list[dict[str, int]]]:
    return [[frac_payload(x) for x in row] for row in matrix]


def to_float_matrix(matrix) -> np.ndarray:
    return np.array([[float(x) for x in row] for row in matrix], dtype=float)


def check_symmetric(matrix) -> int:
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("matrix must be square")
        for x in row:
            if not isinstance(x, Fraction):
                raise TypeError("matrix entries must be fractions.Fraction instances")
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                raise ValueError("matrix must be exactly symmetric")
    return n


# ---------------------------------------------------------------------------------------
# exact algebra
# ---------------------------------------------------------------------------------------

def add(a, b, scale: Fraction = Fraction(1)):
    return [[a[i][j] + scale * b[i][j] for j in range(len(a))] for i in range(len(a))]


def scale_matrix(a, scale: Fraction):
    return [[scale * x for x in row] for row in a]


def matmul(a, b):
    n, k, m = len(a), len(b), len(b[0])
    out = [[Fraction(0)] * m for _ in range(n)]
    for i in range(n):
        ai = a[i]
        oi = out[i]
        for p in range(k):
            c = ai[p]
            if c:
                bp = b[p]
                for j in range(m):
                    if bp[j]:
                        oi[j] += c * bp[j]
    return out


def quadratic_form(matrix, vector) -> Fraction:
    n = len(vector)
    total = Fraction(0)
    for i in range(n):
        vi = vector[i]
        if not vi:
            continue
        row = matrix[i]
        acc = Fraction(0)
        for j in range(n):
            if vector[j]:
                acc += row[j] * vector[j]
        total += vi * acc
    return total


def symmetric_inverse(matrix):
    """Exact inverse by Gauss-Jordan; raises if singular."""
    n = check_symmetric(matrix)
    aug = [[matrix[i][j] for j in range(n)] + [Fraction(int(i == j)) for j in range(n)]
           for i in range(n)]
    for col in range(n):
        pivot_row = next((r for r in range(col, n) if aug[r][col] != 0), None)
        if pivot_row is None:
            raise ValueError("matrix is exactly singular")
        aug[col], aug[pivot_row] = aug[pivot_row], aug[col]
        pivot = aug[col][col]
        aug[col] = [x / pivot for x in aug[col]]
        for r in range(n):
            if r != col and aug[r][col] != 0:
                factor = aug[r][col]
                aug[r] = [x - factor * y for x, y in zip(aug[r], aug[col])]
    inverse = [[aug[i][n + j] for j in range(n)] for i in range(n)]
    return [[(inverse[i][j] + inverse[j][i]) / 2 for j in range(n)] for i in range(n)]


# ---------------------------------------------------------------------------------------
# exact Loewner verdicts
# ---------------------------------------------------------------------------------------

def psd_certificate(matrix, name: str = "") -> dict:
    """Symmetric-pivot LDL^T. Verdict is exact: 'pd', 'psd_singular', or 'indefinite'."""
    n = check_symmetric(matrix)
    work = [[matrix[i][j] for j in range(n)] for i in range(n)]
    perm = list(range(n))
    pivots: list[Fraction] = []
    lower = [[Fraction(0)] * n for _ in range(n)]
    verdict = "pd"
    fail_index = None
    for step in range(n):
        choice = None
        for r in range(step, n):
            if work[r][r] > 0:
                choice = r
                break
        if choice is None:
            # every remaining diagonal entry is <= 0
            neg = next((r for r in range(step, n) if work[r][r] < 0), None)
            if neg is not None:
                verdict, fail_index = "indefinite", perm[neg]
                break
            # all remaining diagonals are zero: PSD iff the whole remaining block is zero
            offdiag = next(((r, c) for r in range(step, n) for c in range(r + 1, n)
                            if work[r][c] != 0), None)
            verdict = "psd_singular" if offdiag is None else "indefinite"
            if offdiag is not None:
                fail_index = [perm[offdiag[0]], perm[offdiag[1]]]
            pivots.extend(Fraction(0) for _ in range(step, n))
            break
        if choice != step:
            work[step], work[choice] = work[choice], work[step]
            for row in work:
                row[step], row[choice] = row[choice], row[step]
            lower[step], lower[choice] = lower[choice], lower[step]
            for row in lower:
                row[step], row[choice] = row[choice], row[step]
            perm[step], perm[choice] = perm[choice], perm[step]
        pivot = work[step][step]
        pivots.append(pivot)
        lower[step][step] = Fraction(1)
        for r in range(step + 1, n):
            factor = work[r][step] / pivot
            lower[r][step] = factor
            if factor:
                for c in range(step, n):
                    work[r][c] -= factor * work[step][c]
                for c in range(step, n):
                    work[c][r] = work[r][c]
    certificate = {
        "certificate_type": "exact-symmetric-pivot-ldl",
        "arithmetic": "fractions.Fraction",
        "quantity": name,
        "dimension": n,
        "verdict": verdict,
        "permutation": list(perm),
        "pivots": [frac_payload(p) for p in pivots],
        "unit_lower_triangular": matrix_payload(lower) if verdict != "indefinite" else None,
        "failure_index": fail_index,
    }
    return certificate


def loewner_verdict(matrix, name: str = "") -> tuple[str, dict]:
    cert = psd_certificate(matrix, name)
    return cert["verdict"], cert


def negativity_witness(matrix, name: str = "",
                       max_denominator: int = WITNESS_MAX_DENOMINATOR) -> dict | None:
    """A rational ``v`` with ``v^T M v < 0``, found from a floating eigenvector and then
    verified in exact arithmetic.  Returns ``None`` when no such exact witness is produced."""
    n = check_symmetric(matrix)
    floating = to_float_matrix(matrix)
    values, vectors = np.linalg.eigh(0.5 * (floating + floating.T))
    for column in range(n):
        raw = vectors[:, column]
        pivot = int(np.argmax(np.abs(raw)))
        if raw[pivot] == 0.0:
            continue
        vector = [Fraction.from_float(float(x / raw[pivot])).limit_denominator(max_denominator)
                  for x in raw]
        value = quadratic_form(matrix, vector)
        if value < 0:
            return {
                "certificate_type": "exact-rational-negativity-witness",
                "arithmetic": "fractions.Fraction",
                "quantity": name,
                "vector": [frac_payload(x) for x in vector],
                "value": frac_payload(value),
                "value_float": float(value),
                "floating_eigenvalue_used": float(values[column]),
                "rationalization_max_denominator": int(max_denominator),
            }
    return None


def generalized_min_ratio_float(numerator, denominator) -> float:
    """Smallest generalized eigenvalue of the rational pencil, as a floating estimate."""
    from scipy.linalg import eigh

    a = to_float_matrix(numerator)
    b = to_float_matrix(denominator)
    a, b = 0.5 * (a + a.T), 0.5 * (b + b.T)
    return float(eigh(a, b, eigvals_only=True)[0])


def generalized_max_ratio_float(numerator, denominator) -> float:
    from scipy.linalg import eigh

    a = to_float_matrix(numerator)
    b = to_float_matrix(denominator)
    a, b = 0.5 * (a + a.T), 0.5 * (b + b.T)
    return float(eigh(a, b, eigvals_only=True)[-1])


def rational_upper_bound_for_min_ratio(numerator, denominator,
                                       max_denominator: int = WITNESS_MAX_DENOMINATOR) -> dict:
    """Exact ``rho_upper`` with ``lambda_min(numerator, denominator) <= rho_upper``.

    The bottom generalized eigenvector is rationalized; the exact Rayleigh quotient of that
    rational vector is then, by the variational principle, an upper bound.  Any rational vector
    would do -- the floating eigensolver only chooses a good one.
    """
    from scipy.linalg import eigh

    n = check_symmetric(numerator)
    check_symmetric(denominator)
    a, b = to_float_matrix(numerator), to_float_matrix(denominator)
    _, vectors = eigh(0.5 * (a + a.T), 0.5 * (b + b.T))
    raw = vectors[:, 0]
    pivot = int(np.argmax(np.abs(raw)))
    vector = [Fraction.from_float(float(x / raw[pivot])).limit_denominator(max_denominator)
              for x in raw]
    den = quadratic_form(denominator, vector)
    if den <= 0:
        raise ValueError("rational witness has a nonpositive denominator form")
    num = quadratic_form(numerator, vector)
    ratio = num / den
    return {
        "certificate_type": "exact-rational-generalized-rayleigh",
        "arithmetic": "fractions.Fraction",
        "dimension": n,
        "vector": [frac_payload(x) for x in vector],
        "numerator_value": frac_payload(num),
        "denominator_value": frac_payload(den),
        "upper_bound": frac_payload(ratio),
        "upper_bound_float": float(ratio),
        "rationalization_max_denominator": int(max_denominator),
    }


def rational_lower_bound_for_max_ratio(numerator, denominator,
                                       max_denominator: int = WITNESS_MAX_DENOMINATOR) -> dict:
    """Exact ``r`` with ``lambda_max(numerator, denominator) >= r``.

    The top generalized eigenvector is rationalized and its exact Rayleigh quotient returned.
    This is the quantity that can *refute* an upper bound on the pencil, so it is the one the
    battery reports as exact evidence.
    """
    from scipy.linalg import eigh

    n = check_symmetric(numerator)
    check_symmetric(denominator)
    a, b = to_float_matrix(numerator), to_float_matrix(denominator)
    _, vectors = eigh(0.5 * (a + a.T), 0.5 * (b + b.T))
    raw = vectors[:, -1]
    pivot = int(np.argmax(np.abs(raw)))
    vector = [Fraction.from_float(float(x / raw[pivot])).limit_denominator(max_denominator)
              for x in raw]
    den = quadratic_form(denominator, vector)
    if den <= 0:
        raise ValueError("rational witness has a nonpositive denominator form")
    num = quadratic_form(numerator, vector)
    ratio = num / den
    return {
        "certificate_type": "exact-rational-generalized-rayleigh",
        "arithmetic": "fractions.Fraction",
        "dimension": n,
        "vector": [frac_payload(x) for x in vector],
        "numerator_value": frac_payload(num),
        "denominator_value": frac_payload(den),
        "lower_bound": frac_payload(ratio),
        "lower_bound_float": float(ratio),
        "rationalization_max_denominator": int(max_denominator),
    }


def rational_lower_bound_for_min_ratio(numerator, denominator, candidate: Fraction) -> dict:
    """Exact verdict for ``numerator - candidate * denominator >= 0``.

    A ``pd``/``psd_singular`` verdict proves ``lambda_min(numerator, denominator) >= candidate``
    when ``denominator`` is positive definite.
    """
    shifted = add(numerator, denominator, -candidate)
    cert = psd_certificate(shifted, f"pencil - ({candidate}) * denominator")
    cert["candidate"] = frac_payload(candidate)
    cert["candidate_float"] = float(candidate)
    cert["proves_lower_bound"] = cert["verdict"] in {"pd", "psd_singular"}
    return cert


def certified_min_ratio_bracket(numerator, denominator, grid_denominator: int = 4096) -> dict:
    """Bracket ``lambda_min(numerator, denominator)`` between two exact rational bounds."""
    upper = rational_upper_bound_for_min_ratio(numerator, denominator)
    estimate = generalized_min_ratio_float(numerator, denominator)
    upper_value = frac_from_payload(upper["upper_bound"])
    candidate = Fraction(int(np.floor(min(estimate, float(upper_value)) * grid_denominator)),
                         grid_denominator)
    lower = rational_lower_bound_for_min_ratio(numerator, denominator, candidate)
    tries = 0
    while not lower["proves_lower_bound"] and tries < 24:
        candidate -= Fraction(1, grid_denominator) * (2 ** tries)
        lower = rational_lower_bound_for_min_ratio(numerator, denominator, candidate)
        tries += 1
    return {
        "floating_estimate": estimate,
        "exact_upper_bound": upper,
        "exact_lower_bound": lower,
        "bracket": [float(candidate) if lower["proves_lower_bound"] else None,
                    float(upper_value)],
    }
