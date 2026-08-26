"""Exact-arithmetic certificates and neutral comparisons for the CMH battery."""
from __future__ import annotations

from fractions import Fraction

from ....comparison import compare_exact


def fraction_payload(value: Fraction) -> dict[str, int]:
    if not isinstance(value, Fraction):
        raise TypeError("exact certificate values must be fractions.Fraction instances")
    return {"numerator": value.numerator, "denominator": value.denominator}


def fraction_from_payload(payload: dict[str, int]) -> Fraction:
    return Fraction(int(payload["numerator"]), int(payload["denominator"]))


def compare_exact_fraction(claim: str, instance: str, bound: Fraction, lower: Fraction,
                           certificate: dict, note: str = ""):
    """Compare Fractions only after checking a matching exact certificate."""
    if not isinstance(bound, Fraction) or not isinstance(lower, Fraction):
        raise TypeError("exact comparison requires Fraction bound and lower value")
    if not isinstance(certificate, dict) or certificate.get("arithmetic") != "fractions.Fraction":
        raise ValueError("exact comparison requires a Fraction-arithmetic certificate")
    if certificate.get("lower_bound") != fraction_payload(lower):
        raise ValueError("certificate lower_bound does not match the exact lower value")
    if certificate.get("certificate_type") not in {
            "closed-form-rational", "exact-rational-rayleigh"}:
        raise ValueError("unrecognized exact certificate type")

    result = compare_exact(
        claim, instance, float(bound), float(lower), rel_tol=0.0,
        note=f"{note} Exact comparison: {lower} <=/> {bound}; "
             f"certificate={certificate['certificate_type']}.",
    )
    if result.outcome == "exceeds" and not lower > bound:
        raise AssertionError("exact comparison exceeded without an exact strict inequality")
    return result


def exact_rayleigh_certificate(numerator_matrix, denominator_matrix, vector):
    """Evaluate a rational Rayleigh witness and emit a self-contained certificate."""
    matrices = (numerator_matrix, denominator_matrix)
    if not vector or any(not isinstance(x, Fraction) for x in vector):
        raise TypeError("Rayleigh witness coordinates must be nonempty Fractions")
    n = len(vector)
    if any(len(matrix) != n or any(len(row) != n for row in matrix) for matrix in matrices):
        raise ValueError("Rayleigh matrices and witness vector must have matching dimensions")
    if any(not isinstance(x, Fraction) for matrix in matrices for row in matrix for x in row):
        raise TypeError("Rayleigh matrices must contain only Fractions")
    if any(matrix[i][j] != matrix[j][i]
           for matrix in matrices for i in range(n) for j in range(n)):
        raise ValueError("Rayleigh matrices must be exactly symmetric")

    ldl = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    pivots: list[Fraction] = []
    for j in range(n):
        pivot = denominator_matrix[j][j] - sum(
            (ldl[j][k] * ldl[j][k] * pivots[k] for k in range(j)), Fraction(0))
        if pivot <= 0:
            raise ValueError("Rayleigh denominator matrix must be positive definite")
        pivots.append(pivot)
        for i in range(j + 1, n):
            ldl[i][j] = (denominator_matrix[i][j] - sum(
                (ldl[i][k] * ldl[j][k] * pivots[k] for k in range(j)), Fraction(0))) / pivot

    def quadratic(matrix):
        return sum((vector[i] * matrix[i][j] * vector[j]
                    for i in range(n) for j in range(n)), Fraction(0))

    numerator = quadratic(numerator_matrix)
    denominator = quadratic(denominator_matrix)
    if denominator <= 0:
        raise ValueError("Rayleigh certificate denominator must be strictly positive")
    lower = numerator / denominator
    certificate = {
        "certificate_type": "exact-rational-rayleigh",
        "arithmetic": "fractions.Fraction",
        "basis": "columns e_i-e_m, i=1,...,m-1",
        "vector": [fraction_payload(x) for x in vector],
        "numerator_matrix": [[fraction_payload(x) for x in row]
                             for row in numerator_matrix],
        "denominator_matrix": [[fraction_payload(x) for x in row]
                               for row in denominator_matrix],
        "denominator_ldl_positive_pivots": [fraction_payload(x) for x in pivots],
        "quadratic_numerator": fraction_payload(numerator),
        "quadratic_denominator": fraction_payload(denominator),
        "lower_bound": fraction_payload(lower),
    }
    return lower, certificate
