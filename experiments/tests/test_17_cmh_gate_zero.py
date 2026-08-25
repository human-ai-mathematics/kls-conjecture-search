"""Exactness and soundness checks for the moment-map/CMH gate-zero target.

Gate zero is the linear-test consequence ``E[H Sigma^{-1} H] <= 4 Sigma`` of the CMH conjecture
``C_CMH <= 4``.  Nothing in this target is sampled, but deterministic floating eigensolves, FEM,
and quadrature are still numerical.  These tests enforce the boundary between their directional
comparisons and the closed-form/rational certificates that alone may emit ``REFUTED``.
"""

import json
import math

import numpy as np
import pytest

from finum.targets import REGISTRY, cmh_gate_zero as cmh


# --- channel 1: one-dimensional closed-form Stein kernels ---------------------------

def test_closed_form_tau_solves_the_defining_ode_and_reproduces_R1():
    for law in cmh.one_d_laws():
        assert cmh.stein_ode_residual(law) <= 1e-7, law["name"]
        m1, m2 = cmh.stein_moments_quadrature(law)
        assert abs(m1 - 1.0) <= 1e-9, law["name"]              # E[tau] = sigma^2 = 1
        assert abs(m2 - law["r1_exact"]) <= 1e-9 * law["r1_exact"], law["name"]


def test_one_dimensional_R1_anchors_are_the_hand_derived_closed_forms():
    by_name = {law["name"]: law["r1_exact"] for law in cmh.one_d_laws()}
    assert by_name["gaussian"] == 1.0                          # CALIBRATION ANCHOR
    assert by_name["exponential-centered"] == 2.0              # E[Y^2], Y ~ Exp(1)
    assert by_name["uniform"] == 1.2
    assert by_name["laplace"] == 1.25                          # 5 b^4 with b = 1/sqrt2
    for a in (1, 2, 5, 20):
        assert abs(by_name[f"gamma-a{a}"] - (1.0 + 1.0 / a)) <= 1e-15
    assert abs(by_name["beta-1-1"] - 1.2) <= 1e-15             # Beta(1,1) IS the uniform law
    assert all(v <= cmh.GATE_ZERO_CEILING for v in by_name.values())
    assert all(isinstance(law["r1_exact_fraction"], cmh.Fraction)
               for law in cmh.one_d_laws())


# --- channel 2: exact Dirichlet gate zero -------------------------------------------

def test_uniform_simplex_reproduces_the_2mp1_over_mp3_ground_truth():
    for m in range(2, 13):
        got = cmh.dirichlet_gate_zero((1,) * m)["g0ratio"]
        assert abs(got - 2.0 * (m + 1) / (m + 3)) <= 1e-10, m


def test_dirichlet_m2_agrees_with_the_uniform_interval():
    # Delta_1 with alpha = (1,1) is exactly the uniform interval: both channels give 1.2.
    assert abs(cmh.dirichlet_gate_zero((1, 1))["g0ratio"] - 1.2) <= 1e-12


def test_dirichlet_gate_zero_is_tangent_basis_independent():
    # The generalized eigenvalue must not depend on how 1^perp is coordinatized; permuting
    # alpha permutes the coordinates and must leave G0ratio invariant.
    a = cmh.dirichlet_gate_zero((1, 5, 25))["g0ratio"]
    b = cmh.dirichlet_gate_zero((25, 1, 5))["g0ratio"]
    assert abs(a - b) <= 1e-10


def test_dirichlet_moments_are_exact_rationals():
    mom = cmh.DirichletMoments((1, 1))                          # P_1 ~ Uniform(0,1)
    assert mom.exact((2, 0)) == cmh.Fraction(1, 3)
    assert mom.exact((1, 1)) == cmh.Fraction(1, 6)
    assert mom.exact((2, 2)) == cmh.Fraction(1, 30)


def test_dirichlet_floating_eigenvalue_has_an_independently_checkable_exact_witness():
    row = cmh.dirichlet_gate_zero((1, 5, 25))
    cert = row["exact_rayleigh_certificate"]

    def frac(payload):
        return cmh.Fraction(payload["numerator"], payload["denominator"])

    x = [frac(v) for v in cert["vector"]]
    M = [[frac(v) for v in matrix_row] for matrix_row in cert["numerator_matrix"]]
    S = [[frac(v) for v in matrix_row] for matrix_row in cert["denominator_matrix"]]
    num = sum((x[i] * M[i][j] * x[j] for i in range(len(x)) for j in range(len(x))),
              cmh.Fraction(0))
    den = sum((x[i] * S[i][j] * x[j] for i in range(len(x)) for j in range(len(x))),
              cmh.Fraction(0))
    exact_lower = frac(cert["lower_bound"])
    assert den > 0
    assert frac(cert["quadratic_numerator"]) == num
    assert frac(cert["quadratic_denominator"]) == den
    assert exact_lower == num / den
    assert float(exact_lower) == row["exact_rayleigh_lower"]
    assert row["exact_rayleigh_lower"] <= row["g0ratio_directional"] + 1e-12


# --- channel 3: the algebraic countermodel ------------------------------------------

def test_countermodel_sector_identities_are_exact():
    for m in (18, 19, 25, 40, 60):
        row = cmh.countermodel_sectors(m)
        assert row["traceless_formula_residual"] <= 1e-12
        assert row["scalar_perfect_square_residual"] <= 1e-12 * m
        assert abs(row["scalar_discriminant"]) <= 1e-12 * m     # d^2 = m^2/(2m-1)
        assert row["all_sectors_at_most_2"]                     # E Tr(BHBH) <= 2 Tr(B^2)
        assert row["EH2_11_exceeds_4"]                          # yet e_1^T E[H^2] e_1 = 1+d > 4


def test_countermodel_closed_form_matches_the_sphere_moment_tensor():
    for m in (18, 20, 24):
        assert cmh.countermodel_tensor_crosscheck(m) <= 1e-9


def test_countermodel_one_plus_d_crosses_four_exactly_at_m18():
    # d = m/sqrt(2m-1) > 3 iff m^2 - 18m + 9 > 0 iff m > 9 + sqrt(72) = 17.485...
    assert cmh.countermodel_sectors(17)["one_plus_d"] < 4.0
    assert cmh.countermodel_sectors(18)["one_plus_d"] > 4.0
    assert abs(cmh.countermodel_sectors(18)["one_plus_d"] - (1.0 + 18 / math.sqrt(35))) <= 1e-12


# --- channel 4: the Dirichlet CMH Galerkin regression -------------------------------

def test_degree_one_galerkin_reproduces_gate_zero():
    for alpha in ((1, 1), (1, 1, 1), (1, 1, 10), (1, 5, 25), (1, 2, 3, 4, 5)):
        q = cmh.dirichlet_galerkin(alpha, 1)["q_max"]
        assert abs(q - cmh.dirichlet_gate_zero(alpha)["g0ratio"]) <= 1e-9, alpha


def test_galerkin_is_monotone_in_degree_and_stays_under_the_ceiling():
    prev = 0.0
    for deg in (1, 2, 3, 4, 5, 6):
        row = cmh.dirichlet_galerkin((1, 1, 100), deg)
        assert row["numerically_reliable"], deg
        assert row["q_max"] >= prev - 1e-9                      # nested Galerkin subspaces
        assert row["q_max"] <= row["ceiling"]
        assert row["q_max"] <= cmh.GATE_ZERO_CEILING
        prev = row["q_max"]


def test_galerkin_recovers_the_uniform_interval_CMH_constant():
    # alpha = (1,1) is the uniform interval, whose exact C_CMH = C_P/Var = 12/pi^2.
    q = cmh.dirichlet_galerkin((1, 1), 6)["q_max"]
    exact = 12.0 / math.pi ** 2
    assert q <= exact + 1e-12                                   # Galerkin is a LOWER bound
    assert abs(q - exact) <= 1e-4


def test_galerkin_conditioning_gate_is_the_exact_lambda_min_identity():
    # L_alpha has eigenvalue -k(k+A-1) on degree-k polynomials, so after whitening by the
    # covariance form lambda_min(N') must be exactly A^2. That is the run's health gate.
    for alpha in ((1, 1, 1), (1, 1, 1000), (1, 1, 1, 1, 50)):
        row = cmh.dirichlet_galerkin(alpha, cmh.GALERKIN_DEGREE[len(alpha)])
        assert abs(row["conditioning_health"] - 1.0) <= 1e-6, alpha
        assert row["numerically_reliable"]


def test_dirichlet_ceiling_formula():
    assert abs(cmh.dirichlet_ceiling(3.0) - 4.0) <= 1e-12       # z_A = 2 <= 4 => s_A = 0
    A = 102.0
    s = math.sqrt((A - 1) * (A - 2)) - 1.5
    assert abs(cmh.dirichlet_ceiling(A) - 4.0 / (1 + 4 * s / (A * (A + 1)))) <= 1e-12


# --- target wiring, soundness contract ----------------------------------------------

def test_target_is_registered_and_deterministic():
    assert REGISTRY["cmh-gate-zero"] is cmh
    a, _ = cmh.run_records(0)
    b, _ = cmh.run_records(12345)                               # seed must not change anything
    assert json.dumps(a) == json.dumps(b)


def test_run_records_reports_calibration_and_realized_maxima():
    records, extra = cmh.run_records(0)
    assert extra["calibration_passed"] is True
    assert extra["monte_carlo_used"] is False
    for key in ("max_R1_1d_exact", "max_G0ratio_dirichlet_directional",
                "max_G0ratio_dirichlet_exact_rayleigh_lower",
                "max_C_CMH_1d_fem_directional", "max_galerkin_Q_over_ceiling"):
        assert np.isfinite(extra[key])
    assert extra["gate_zero_refuted"] is False                  # nothing exceeded 4
    assert extra["dirichlet_theorem_refuted"] is False
    assert extra["countermodel_identities_exact"] is True
    summary = records[-1]
    assert summary["kind"] == "summary"
    assert summary["gate_zero_exceeded_instances"] == []
    assert "NECESSARY" in summary["proof_status"]
    json.dumps(records)                                          # provenance-writer compatible


def test_only_exact_quantities_get_an_analytic_verdict():
    """Only rational R1/Rayleigh certificates may be analytic; all float channels are directional."""
    records, _ = cmh.run_records(0)
    directional = {"directional-consistent", "directional-exceeds", "no-comparison"}
    analytic = {"consistent", "REFUTED", "no-verdict"}
    seen_fem = seen_exact = seen_float_eigenvalue = 0
    for r in records:
        if r["kind"] == "stein-1d":
            assert r["verdict_C_CMH_directional"]["status"] in directional
            assert r["verdict_gate_zero_exact"]["status"] in analytic
            assert r["gate_zero_exact_certificate"]["arithmetic"] == "fractions.Fraction"
            seen_fem += 1
            seen_exact += 1
        if r["kind"] == "dirichlet-gate-zero":
            assert r["verdict_directional"]["status"] in directional
            assert r["verdict_exact_rayleigh"]["status"] in analytic
            assert r["exact_rayleigh_certificate"]["certificate_type"] == \
                "exact-rational-rayleigh"
            seen_float_eigenvalue += 1
            seen_exact += 1
        if r["kind"] == "dirichlet-galerkin":
            assert r["verdict_vs_ceiling"]["status"] in directional
            assert r["verdict_vs_4"]["status"] in directional
            seen_float_eigenvalue += 1
    assert seen_fem >= 12 and seen_exact >= 24 and seen_float_eigenvalue >= 24


def test_exact_verdict_gate_rejects_floats_missing_certificates_and_mismatches():
    lower, certificate = cmh._exact_rayleigh_certificate(
        [[cmh.Fraction(5)]], [[cmh.Fraction(1)]], [cmh.Fraction(1)])
    with pytest.raises(TypeError):
        cmh._falsify_exact_fraction("x <= 4", "x", 4.0, lower, certificate)
    with pytest.raises(TypeError):
        cmh._falsify_exact_fraction("x <= 4", "x", cmh.Fraction(4), 5.0, certificate)
    with pytest.raises(ValueError):
        cmh._falsify_exact_fraction("x <= 4", "x", cmh.Fraction(4), lower, {})
    bad = dict(certificate)
    bad["lower_bound"] = {"numerator": 6, "denominator": 1}
    with pytest.raises(ValueError):
        cmh._falsify_exact_fraction("x <= 4", "x", cmh.Fraction(4), lower, bad)


def test_uppercase_refuted_requires_a_verified_exact_rational_certificate():
    lower, certificate = cmh._exact_rayleigh_certificate(
        [[cmh.Fraction(5)]], [[cmh.Fraction(1)]], [cmh.Fraction(1)])
    verdict = cmh._falsify_exact_fraction(
        "synthetic exact Rayleigh quotient <= 4", "exact-5-over-1",
        cmh.Fraction(4), lower, certificate)
    assert lower == cmh.Fraction(5)
    assert certificate["lower_bound"] == {"numerator": 5, "denominator": 1}
    assert verdict.status == "REFUTED"


def test_injected_floating_galerkin_exceedance_remains_directional(monkeypatch):
    original = cmh.dirichlet_galerkin

    def inflated(alpha, deg):
        row = original(alpha, deg)
        if deg > 1:
            row["q_max"] = max(5.0, 2.0 * row["ceiling"])
        return row

    monkeypatch.setattr(cmh, "dirichlet_galerkin", inflated)
    records, _ = cmh.run_records(
        0, dirichlet_alphas=((1, 1),), countermodel_ms=(18,),
        countermodel_tensor_ms=(18,), galerkin_max_m=2)
    rows = [r for r in records if r["kind"] == "dirichlet-galerkin"]
    assert rows
    assert all(r["verdict_vs_ceiling"]["status"] == "directional-exceeds" for r in rows)
    assert all(r["verdict_vs_4"]["status"] == "directional-exceeds" for r in rows)
    assert records[-1]["dirichlet_theorem_refuted"] is False


def test_future_run_provenance_captures_the_effective_battery_and_tolerances():
    _, extra = cmh.run_records(
        0, dirichlet_alphas=((1, 1), (1, 5, 25)), countermodel_ms=(18, 19),
        countermodel_tensor_ms=(18,), galerkin_max_m=3)
    battery = extra["battery"]
    assert battery["schema_version"] == 2
    assert battery["dirichlet_gate_zero"]["swept_alphas"] == [[1, 1], [1, 5, 25]]
    assert battery["dirichlet_gate_zero"]["uniform_simplex_m_range_inclusive"] == [2, 12]
    assert battery["dirichlet_gate_zero"]["rational_witness_max_denominator"] == 1_000_000
    assert battery["algebraic_countermodel"]["m_values"] == [18, 19]
    assert battery["algebraic_countermodel"]["tensor_crosscheck_m_values"] == [18]
    assert battery["dirichlet_galerkin"]["galerkin_max_m"] == 3
    assert battery["dirichlet_galerkin"]["degree_by_m"] == {"2": 6, "3": 6, "4": 4, "5": 4}
    assert battery["one_dimensional"]["quadrature"] == {
        "limit": 500, "epsabs": 1e-13, "epsrel": 1e-13, "split_points": [0.0]}
    grids = {row["name"]: row["fem_grid"] for row in battery["one_dimensional"]["instances"]}
    assert grids["gaussian"] == {"start": -12.0, "stop": 12.0, "num_points": 4001}
    assert grids["exponential-centered"] == {"start": -1.0, "stop": 39.0,
                                             "num_points": 8001}
    json.dumps(extra)


def test_selftest_checks_all_pass():
    for name, ok in cmh.selftest(np.random.default_rng(7)):
        assert ok, name
