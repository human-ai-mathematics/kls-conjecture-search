"""Oracle suite for the CMH anisotropic-bootstrap target ``cmh-ab``.

The battery computes ``N = int H^2``, ``D = int H^{ab}(d_a H)(d_b H)`` and ``R = N - D`` for
moment maps, and a Galerkin lower bound for the CMH Rayleigh quotient under perturbations of the
saturating product.  These tests pin the two things a reader cannot check by inspection:

1.  the *index placement* of ``D`` under the source/target change of variables, via three
    independent oracles (an exact one-dimensional identity, the certified ``cmh-gate-zero``
    battery, and an independently assembled differentiated Monge-Ampere identity); and
2.  the evidence boundary -- exact rational Loewner verdicts carry a self-contained certificate,
    every quadrature value is directional, and an inadmissible instance (non-convex source
    potential, or a target shown to have left the log-concave class) contributes to no verdict.
"""

import json
import math
from fractions import Fraction

import numpy as np
import pytest

from finum.targets import REGISTRY
from finum.targets.kls import cmh_ab
from finum.targets.kls.cmh_ab import dirichlet as dir_channel
from finum.targets.kls.cmh_ab import exact_forms as ex
from finum.targets.kls.cmh_ab import jets, m9, onedim, sourcemap


# --- jet arithmetic: derivatives are analytic, so they must be exact on polynomials ----

def test_jet_multiplication_reproduces_the_leibniz_rule():
    y = np.linspace(-1.5, 2.0, 9)
    z = np.linspace(0.3, 1.7, 9)
    j1, j2 = jets.Jet.variable(y, 0), jets.Jet.variable(z, 1)
    product = (j1 * j1 * j1) * (j2 * j2)              # y^3 z^2, kept to total order four
    assert (3, 2) not in product.c                    # order five is truncated by design
    assert np.allclose(product.c[(0, 0)], y ** 3 * z ** 2)
    assert np.allclose(product.c[(3, 1)], 6.0 * 2.0 * z)
    assert np.allclose(product.c[(2, 2)], 6.0 * y * 2.0)
    assert np.allclose(product.c[(2, 1)], 6.0 * y * 2.0 * z)
    assert np.allclose(product.c[(4, 0)], 0.0)


def test_jet_exponential_and_logarithm_are_exact():
    y = np.linspace(-2.0, 2.0, 11)
    j = jets.Jet.variable(y, 0)
    e = jets.jexp(j * 2.0)
    for order in range(5):
        assert np.allclose(e.c[(order, 0)], 2.0 ** order * np.exp(2.0 * y))
    lg = jets.jlog(jets.jexp(j))                        # log(exp(y)) = y
    assert np.allclose(lg.c[(0, 0)], y)
    assert np.allclose(lg.c[(1, 0)], 1.0)
    assert np.allclose(lg.c[(2, 0)], 0.0, atol=1e-12)


def test_jet_gaussian_bump_matches_the_hermite_derivative_formula():
    y = np.linspace(-2.0, 3.0, 13)
    bump = jets.jgaussian_bump(jets.Jet.variable(y, 0), 0.5, 0.8)
    base = np.exp(-((y - 0.5) / 0.8) ** 2 / 2.0)
    assert np.allclose(bump.c[(0, 0)], base)
    assert np.allclose(bump.c[(1, 0)], -(y - 0.5) / 0.8 ** 2 * base)


# --- channel 1(a): exact one-dimensional -----------------------------------------------

def test_one_dimensional_anchors_are_the_hand_derived_values():
    rows = {row["name"]: row for row in onedim.one_d_instances()}
    assert (rows["gaussian"]["N"], rows["gaussian"]["D"]) == (Fraction(1), Fraction(0))
    # centred one-sided exponential: N = E[(X+1)^2] = 2, D = E[H (H')^2] = E[X+1] = 1
    assert (rows["gamma-a1"]["N"], rows["gamma-a1"]["D"]) == (Fraction(2), Fraction(1))
    assert rows["gamma-a1"]["R"] == Fraction(1)
    assert rows["gamma-a1"]["sharp_margin"] == 0                 # R = N/2 exactly
    assert rows["uniform"]["N"] == Fraction(6, 5)
    assert rows["uniform"]["D"] == Fraction(3, 5)
    assert rows["uniform"]["sharp_margin"] == 0
    assert rows["laplace"]["N"] == Fraction(5, 4)
    assert rows["laplace"]["D"] == Fraction(1, 2)
    for shape in (1, 2, 5, 20):
        row = rows[f"gamma-a{shape}"]
        assert row["N"] == Fraction(shape + 1, shape)
        assert row["D"] == Fraction(1, shape)
        assert row["R"] == 1                                     # R = 1 for every Gamma


def test_one_dimensional_monge_ampere_identity_is_exact():
    """``N = 2 D + E[H^3 V'']`` pins the index placement of ``D`` on the line."""
    for row in onedim.one_d_instances():
        assert row["identity_residual"] == 0, row["name"]
        assert isinstance(row["identity_residual"], Fraction)


def test_one_dimensional_brascamp_lieb_and_sharp_candidate_hold_exactly():
    for row in onedim.one_d_instances():
        assert row["brascamp_lieb_margin"] >= 0, row["name"]      # N - I <= D
        assert row["sharp_margin"] >= 0, row["name"]              # R >= N/2 on the line
        assert row["rho_star"]["0"] == row["R"] / row["N"]


def test_one_dimensional_N_equals_the_certified_gate_zero_R1():
    for name, here, there in onedim.gate_zero_r1_crosscheck():
        assert here == there, name


# --- channel 1(b): exact Dirichlet -----------------------------------------------------

def test_dirichlet_delta_one_reproduces_the_beta_channel():
    for a, b in ((1, 1), (1, 2), (1, 5), (2, 2), (2, 5), (3, 7)):
        n_here, n_there, d_here, d_there = dir_channel.one_dimensional_crosscheck(a, b)
        assert abs(n_here - n_there) <= 1e-12, (a, b)
        assert abs(d_here - d_there) <= 1e-12, (a, b)


def test_dirichlet_lambda_max_N_equals_the_certified_gate_zero_ratio():
    for alpha in ((1, 1, 1), (1, 1, 10), (1, 5, 25), (1, 2, 3, 4, 5)):
        here, there = dir_channel.gate_zero_crosscheck(alpha)
        assert abs(here - there) <= 1e-10, alpha


def test_dirichlet_matrices_are_exact_symmetric_rationals():
    sigma, n_mat, d_mat = dir_channel.bootstrap_matrices((1, 2, 4))
    for matrix in (sigma, n_mat, d_mat):
        assert ex.check_symmetric(matrix) == 2
    # Sigma^{-1} closed form must invert Sigma exactly
    _, inverse = dir_channel.chart_covariance((1, 2, 4))
    product = ex.matmul(sigma, inverse)
    for i in range(2):
        for j in range(2):
            assert product[i][j] == Fraction(int(i == j))


def test_dirichlet_D_is_positive_semidefinite_exactly():
    for alpha in ((1, 1, 1), (1, 1, 100), (1, 2, 3, 4, 5)):
        _, _, d_mat = dir_channel.bootstrap_matrices(alpha)
        verdict, _ = ex.loewner_verdict(d_mat, "D")
        assert verdict in {"pd", "psd_singular"}, alpha


def test_dirichlet_rho_star_at_beta_zero_is_one_minus_lambda_max_D_over_N():
    row = dir_channel.analyse((1, 1, 100), betas=(Fraction(0),))
    identity = 1.0 - row["lambda_max_D_over_N_directional"]
    assert abs(row["rho_star"]["0"]["floating"] - identity) <= 1e-12


def test_dirichlet_exact_certificates_are_independently_recheckable():
    row = dir_channel.analyse((1, 5, 25), betas=(Fraction(0),))
    certificate = row["lambda_max_D_over_N_certificate"]
    vector = [ex.frac_from_payload(v) for v in certificate["vector"]]
    n_mat = [[ex.frac_from_payload(v) for v in r] for r in row["N"]]
    d_mat = [[ex.frac_from_payload(v) for v in r] for r in row["D"]]
    num = ex.quadratic_form(d_mat, vector)
    den = ex.quadratic_form(n_mat, vector)
    assert den > 0
    assert num / den == ex.frac_from_payload(certificate["lower_bound"])
    assert num / den <= Fraction(1, 2)          # the sharp candidate holds on this instance

    ldl = row["sharp_candidate_certificate"]
    assert ldl["verdict"] in {"pd", "psd_singular"}
    assert all(ex.frac_from_payload(p) >= 0 for p in ldl["pivots"])


def test_exact_psd_machinery_detects_an_indefinite_matrix_with_a_rational_witness():
    matrix = [[Fraction(1), Fraction(2)], [Fraction(2), Fraction(1)]]
    verdict, _ = ex.loewner_verdict(matrix, "test")
    assert verdict == "indefinite"
    witness = ex.negativity_witness(matrix, "test")
    assert witness is not None
    vector = [ex.frac_from_payload(v) for v in witness["vector"]]
    assert ex.quadratic_form(matrix, vector) < 0
    assert ex.frac_from_payload(witness["value"]) < 0


def test_exact_psd_machinery_accepts_a_singular_psd_matrix():
    matrix = [[Fraction(1), Fraction(1)], [Fraction(1), Fraction(1)]]
    verdict, certificate = ex.loewner_verdict(matrix, "test")
    assert verdict == "psd_singular"
    assert ex.negativity_witness(matrix, "test") is None
    assert all(ex.frac_from_payload(p) >= 0 for p in certificate["pivots"])


# --- channel 1(c): the source-potential engine -----------------------------------------

@pytest.mark.parametrize("name,first,second,expected", [
    ("exp-gauss", "gamma:1", "gaussian", ((2.0, 1.0), (1.0, 0.0))),
    ("exp-exp", "gamma:1", "gamma:1", ((2.0, 1.0), (2.0, 1.0))),
    ("gam2-gauss", "gamma:2", "gaussian", ((1.5, 0.5), (1.0, 0.0))),
    ("unif-gauss", "uniform", "gaussian", ((1.2, 0.6), (1.0, 0.0))),
])
def test_engine_reproduces_the_exact_one_dimensional_blocks_on_products(
        name, first, second, expected):
    geometry = sourcemap.ProductGeometry(name, first, second)
    row = sourcemap.analyse(geometry, geometry.resolution(160))
    assert row["status"] == "ok"
    assert np.allclose(row["N"], np.diag([expected[0][0], expected[1][0]]), atol=1e-9)
    assert np.allclose(row["D"], np.diag([expected[0][1], expected[1][1]]), atol=1e-9)


def test_engine_reproduces_the_exact_rational_dirichlet_matrices():
    for alpha in ((1, 1, 1), (1, 2, 4), (2, 3, 4)):
        geometry = sourcemap.DirichletGeometry(alpha)
        row = sourcemap.analyse(geometry, (40, 40))
        assert row["status"] == "ok", alpha
        sigma, n_mat, d_mat = dir_channel.bootstrap_matrices(alpha)
        values, vectors = np.linalg.eigh(ex.to_float_matrix(sigma))
        whiten = (vectors / np.sqrt(values)) @ vectors.T
        assert np.allclose(row["N"], whiten @ ex.to_float_matrix(n_mat) @ whiten, atol=1e-8)
        assert np.allclose(row["D"], whiten @ ex.to_float_matrix(d_mat) @ whiten, atol=1e-8)


def test_engine_differentiated_monge_ampere_identity_holds_on_every_geometry():
    """``N - D`` and ``(1/2) int {H, A + Q}`` share no code path; they must agree."""
    geometries = [
        sourcemap.ProductGeometry("exp-gauss", "gamma:1", "gaussian"),
        sourcemap.ProductGeometry("gam1.5-gauss", "gamma:1.5", "gaussian"),
        sourcemap.DirichletGeometry((1, 2, 4)),
        sourcemap.ProductGeometry(
            "coupled", "gamma:1", "gaussian",
            coupling=sourcemap.make_coupling(sourcemap.exponential_bump(1.2, 0.8),
                                             sourcemap.damped_hermite(2)),
            epsilon=0.05),
    ]
    for geometry in geometries:
        row = sourcemap.analyse(geometry, geometry.resolution(160))
        assert row["status"] == "ok", geometry.name
        assert row["residuals"]["monge_ampere_identity_relative"] <= 1e-7, geometry.name
        assert np.allclose(np.array(row["R"]),
                           np.array(row["R_A"]) + np.array(row["R_Q"]), atol=1e-7)


def test_engine_reproduces_the_certified_chen_klartag_trace_inequality():
    """Cyclic symmetry of ``D^3 psi`` gives ``Tr R_Q >= Tr D``; the matrix form is the open one."""
    geometries = [
        sourcemap.ProductGeometry("exp-gauss", "gamma:1", "gaussian"),
        sourcemap.DirichletGeometry((1, 2, 4)),
        sourcemap.ProductGeometry(
            "gauss-gauss", "gaussian", "gaussian",
            coupling=sourcemap.make_coupling(sourcemap.coordinate_bump(2.5, 1.2),
                                             sourcemap.damped_hermite(2)),
            epsilon=-0.1),
    ]
    for geometry in geometries:
        row = sourcemap.analyse(geometry, geometry.resolution(160))
        assert row["status"] == "ok", geometry.name
        assert row["trace_R_Q_minus_D_relative"] >= -1e-9, geometry.name
    # ... while the Loewner form fails on the last, fully admissible, instance
    assert row["target_log_concavity"] == "consistent"
    assert row["lambda_min_R_Q_minus_D_relative"] < -1e-3
    assert row["worst_residual"] <= 1e-7


def test_engine_A_matches_the_closed_form_dirichlet_target_hessian():
    error, dropped = sourcemap.dirichlet_target_hessian_error((2, 3, 4), (48, 48))
    assert error <= 1e-6
    assert dropped <= 1e-9


def test_engine_stein_residuals_are_the_requested_moment_map_checks():
    geometry = sourcemap.ProductGeometry("exp-gauss", "gamma:1", "gaussian")
    row = sourcemap.analyse(geometry, geometry.resolution(160))
    assert row["residuals"]["barycentre_norm"] <= 1e-9         # centred target
    assert row["residuals"]["stein_EH_minus_Sigma"] <= 1e-9    # E_mu H = Cov
    assert row["residuals"]["stein_div_quadratic"] <= 1e-9     # Div_mu H = -x


def test_engine_aborts_a_source_potential_that_is_not_convex():
    coupling = sourcemap.make_coupling(sourcemap.coordinate_bump(0.0, 0.4),
                                       sourcemap.damped_hermite(2))
    geometry = sourcemap.ProductGeometry("gauss-gauss", "gaussian", "gaussian",
                                         coupling=coupling, epsilon=8.0)
    row = sourcemap.analyse(geometry, (48, 48))
    assert row["status"] == "aborted"
    assert "N" not in row


def test_engine_flags_a_target_that_has_left_the_log_concave_class():
    """The saturating product sits on the boundary: both signs must be flagged."""
    coupling = sourcemap.make_coupling(sourcemap.exponential_bump(1.2, 0.8),
                                       sourcemap.damped_hermite(1))
    for epsilon in (0.05, -0.05):
        geometry = sourcemap.ProductGeometry("exp-gauss", "gamma:1", "gaussian",
                                             coupling=coupling, epsilon=epsilon)
        row = sourcemap.analyse(geometry, geometry.resolution(160))
        assert row["status"] == "ok"
        assert row["target_log_concavity"] == "violated"
        assert row["target_log_concave"] is False
    # a Gaussian product is strictly inside the class and survives the same coupling
    gaussian_coupling = sourcemap.make_coupling(sourcemap.coordinate_bump(1.2, 0.8),
                                                sourcemap.damped_hermite(1))
    geometry = sourcemap.ProductGeometry("gauss-gauss", "gaussian", "gaussian",
                                         coupling=gaussian_coupling, epsilon=0.05)
    row = sourcemap.analyse(geometry, geometry.resolution(160))
    assert row["target_log_concavity"] == "consistent"
    assert row["target_log_concavity_bulk_margin"] > 0.0


# --- channel 2: the M9 Galerkin quotient -----------------------------------------------

def test_m9_degree_one_galerkin_is_the_exact_linear_test_value():
    for shape in (1.0, 1.5, 3.0):
        geometry = m9.saturating_geometry(shape=shape)
        row = m9.galerkin_quotient(geometry, (140, 24), 1)
        assert abs(row["q"] - m9.degree_one_anchor(shape)) <= 1e-8, shape


def test_m9_galerkin_ladder_is_monotone_and_matches_the_continuous_edge_formula():
    geometry = m9.saturating_geometry()
    previous = 0.0
    for degree in range(1, 7):
        row = m9.galerkin_quotient(geometry, (160, 24), degree)
        assert row["q"] >= previous - 1e-9
        assert row["q"] <= m9.CMH_CEILING + 1e-9
        # the exponential endpoint is a continuous-spectrum edge, not an eigenvalue
        assert abs(row["q"] - 2.0 * (1.0 + math.cos(math.pi / (degree + 1)))) <= 1e-7, degree
        previous = row["q"]


def test_m9_enrichment_narrows_the_gap_to_four_without_crossing_it():
    geometry = m9.saturating_geometry()
    plain = m9.galerkin_quotient(geometry, (180, 24), 6)["q"]
    enriched = m9.galerkin_quotient(geometry, (180, 24), 6,
                                    enrichment_rates=(0.3, 0.4, 0.45, 0.475))["q"]
    assert enriched >= plain - 1e-9
    assert enriched < m9.CMH_CEILING


def test_m9_skips_a_perturbation_that_breaks_convexity():
    coupling = sourcemap.make_coupling(sourcemap.coordinate_bump(0.0, 0.4),
                                       sourcemap.damped_hermite(2))
    geometry = sourcemap.ProductGeometry("gauss-gauss", "gaussian", "gaussian",
                                         coupling=coupling, epsilon=8.0)
    row = m9.galerkin_quotient(geometry, (48, 48), 3)
    assert row["status"] == "skipped"
    assert "q" not in row


# --- target wiring and the evidence boundary -------------------------------------------

def test_target_is_registered_and_deterministic():
    assert REGISTRY["cmh-ab"].module is cmh_ab
    assert REGISTRY["cmh-ab"].stochastic is False
    a = cmh_ab.run_records(0, run_sourcemap=False, run_m9=False,
                           dirichlet_alphas=((1, 1), (1, 1, 10)))
    b = cmh_ab.run_records(4321, run_sourcemap=False, run_m9=False,
                           dirichlet_alphas=((1, 1), (1, 1, 10)))
    assert json.dumps(a.records) == json.dumps(b.records)


def test_run_records_are_json_serializable_and_carry_the_thresholds():
    result = cmh_ab.run_records(0, run_sourcemap=False, run_m9=False,
                               dirichlet_alphas=((1, 1, 1), (1, 1, 1000)))
    json.dumps(result.records)
    json.dumps(result.config)
    summary = result.records[-1]
    assert summary["kind"] == "summary"
    assert summary["calibration_passed"] is True
    assert summary["monte_carlo_used"] is False
    assert summary["status_effect"].startswith("none")
    thresholds = summary["thresholds"]
    assert thresholds["directional_against_AB_rho_star_beta_one"] == 0.05
    assert thresholds["directional_support_AB_rho_star_beta_zero"] == 0.3
    assert thresholds["m9_refutation_candidate_q"] == 4.05
    assert "_fields" not in json.dumps(result.records)


def test_only_exact_channels_get_an_analytic_verdict():
    result = cmh_ab.run_records(0, run_m9=False,
                                dirichlet_alphas=((1, 1, 1),),
                                sourcemap_base_nodes=120,
                                dirichlet_engine_base_nodes=96,
                                sourcemap_epsilons=(0.05,),
                                sourcemap_dirichlet_alphas=((1, 1, 1),),
                                m9_longitudinal=(("u-bump", 1.2, 0.8),),
                                m9_transverse=(1,))
    seen_exact = seen_directional = 0
    for record in result.records:
        if record["kind"] == "ab-one-dimensional":
            assert record["sharp_candidate_comparison"]["evidence"] == "exact"
            seen_exact += 1
        if record["kind"] == "ab-dirichlet":
            assert record["sharp_candidate_comparison"]["evidence"] == "exact"
            assert record["sharp_candidate_certificate"]["arithmetic"] == "fractions.Fraction"
            seen_exact += 1
        if record["kind"] == "ab-sourcemap" and record["status"] == "ok":
            assert record["sharp_candidate_comparison"]["evidence"] == "directional"
            seen_directional += 1
    assert seen_exact >= 13 and seen_directional >= 4


def test_selftest_checks_all_pass():
    for name, ok in cmh_ab.selftest(np.random.default_rng(11)):
        assert ok, name
