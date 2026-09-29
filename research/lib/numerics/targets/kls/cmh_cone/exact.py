"""Self-contained exact certificates for the exponential-cone battery.

Two genres are emitted, both in ``fractions.Fraction`` arithmetic.

``exact-rational-loewner-pencil``
    decides ``lambda_max(M, Sigma) <= c`` outright on one instance.  A complete
    symmetric-pivot LDL^T of ``c Sigma - M`` with nonnegative pivots proves the
    inequality; a negative pivot returns the exact rational direction ``v`` that violates
    it, and the certificate then also carries ``v^T M v / v^T Sigma v > c``.  Either way
    the recorded ``lower_bound`` is an exact rational Rayleigh quotient of the pencil, so
    the neutral comparison of :mod:`..cmh_gate_zero.exact` applies unchanged.

``exact-rational-test-function``
    is a lower bound for ``C_CMH`` from one explicit rational test function: the vector of
    coefficients in the stated monomial basis, together with the exact numerator and
    denominator.  It needs no spectral claim -- ``den > 0`` and the two rationals are the
    whole argument -- so the large Galerkin matrices are recorded by digest and
    reproduction recipe rather than inlined.

Neither genre is a proof.  CLAUDE.md constraint 2: an exact witness emitted here is a
candidate until a researcher states it analytically and a distinct reviewer certifies a
dossier.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction

from ..cmh_gate_zero.exact import (
    compare_exact_fraction as _base_compare,
    fraction_from_payload,
    fraction_payload,
)
from . import linalg as la

CERTIFICATE_TYPES = frozenset({
    "closed-form-rational",
    "exact-rational-loewner-pencil",
    "exact-rational-test-function",
})


def compare_exact_fraction(claim, instance, bound: Fraction, lower: Fraction,
                           certificate: dict, note: str = ""):
    """The shared exact-comparison guard, widened to this target's certificate genres."""
    return _base_compare(claim, instance, bound, lower, certificate, note=note,
                         allowed_types=CERTIFICATE_TYPES)


def _payload_matrix(A):
    return [[fraction_payload(x) for x in row] for row in A]


def matrix_digest(*matrices) -> str:
    """SHA-256 of a canonical serialization of exact matrices."""
    blob = json.dumps([[[[x.numerator, x.denominator] for x in row] for row in A]
                       for A in matrices], separators=(",", ":"))
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def pencil_certificate(M, Sigma, bound: Fraction, fallback_vector, source: dict,
                       inline_matrices: bool = True):
    """Decide ``lambda_max(M, Sigma) <= bound`` exactly and package the witness.

    ``fallback_vector`` is the rationalized floating top eigenvector, used only when the
    Loewner test succeeds and the certificate merely reports how close the instance is.
    ``inline_matrices=False`` records the pencil by digest instead of by value, for the
    second bound on an instance whose first certificate already carries it verbatim.
    """
    bound = Fraction(bound)
    gap = [[bound * Sigma[i][j] - M[i][j] for j in range(len(M))]
           for i in range(len(M))]                        # bound * Sigma - M, exactly
    is_psd, pivots, witness = la.psd_certificate(gap)
    vector = list(fallback_vector) if is_psd else list(witness)
    numerator = la.quadratic(M, vector)
    denominator = la.quadratic(Sigma, vector)
    if denominator <= 0:
        raise ValueError("pencil certificate needs a strictly positive Sigma-norm witness")
    lower = numerator / denominator
    if not is_psd and not lower > bound:
        raise AssertionError("Loewner failure must produce a strictly exceeding witness")
    if is_psd and lower > bound:
        raise AssertionError("Loewner success contradicts its own Rayleigh witness")
    certificate = {
        "certificate_type": "exact-rational-loewner-pencil",
        "arithmetic": "fractions.Fraction",
        "bound": fraction_payload(bound),
        "loewner_psd": bool(is_psd),
        "loewner_pivots": [fraction_payload(x) for x in pivots],
        "witness_source": "loewner-negative-direction" if not is_psd
                          else "rationalized floating top eigenvector",
        "vector": [fraction_payload(x) for x in vector],
        "matrix_digest_sha256": matrix_digest(M, Sigma),
        "matrix_inline": bool(inline_matrices),
        **({"gate_matrix": _payload_matrix(M), "covariance": _payload_matrix(Sigma)}
           if inline_matrices else
           {"reproduction": "numerics.targets.kls.cmh_cone.gate.gate_pencil(base, beta)"}),
        "quadratic_numerator": fraction_payload(numerator),
        "quadratic_denominator": fraction_payload(denominator),
        "lower_bound": fraction_payload(lower),
        **source,
    }
    return lower, is_psd, certificate


def test_function_certificate(N, D, vector, source: dict):
    """An exact CMH lower bound from one rational test function in a Galerkin basis."""
    numerator = la.quadratic(N, vector)
    denominator = la.quadratic(D, vector)
    if denominator <= 0:
        raise ValueError("a CMH test function needs E(L_mu g)^2 > 0")
    lower = numerator / denominator
    certificate = {
        "certificate_type": "exact-rational-test-function",
        "arithmetic": "fractions.Fraction",
        "vector": [fraction_payload(x) for x in vector],
        "quadratic_numerator": fraction_payload(numerator),
        "quadratic_denominator": fraction_payload(denominator),
        "lower_bound": fraction_payload(lower),
        "matrix_digest_sha256": matrix_digest(N, D),
        "matrix_inline": False,
        "reproduction": "numerics.targets.kls.cmh_cone.galerkin.assemble(base, beta, degree)",
        **source,
    }
    return lower, certificate


__all__ = ["CERTIFICATE_TYPES", "compare_exact_fraction", "fraction_from_payload",
           "fraction_payload", "matrix_digest", "pencil_certificate",
           "test_function_certificate"]
