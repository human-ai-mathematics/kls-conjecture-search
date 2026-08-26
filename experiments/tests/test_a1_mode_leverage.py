import numpy as np
from scipy.optimize import brentq
from scipy.special import gammaincc

from finum.targets.a_series.a1 import (
    logistic_mode_leverage,
    mode_leverage_factor,
    mode_leverage_g_minus,
    mode_leverage_g_plus,
    mode_leverage_split_candidate,
    mode_leverage_tail_bound,
    mode_leverage_weight_floor,
)


def test_radial_potential_bounds_bracket_the_gaussian_quadratic():
    radii = np.linspace(0.0, 8.0, 101)
    quadratic = 0.5 * radii**2

    for eta in (0.0, 0.02, 0.2, 0.8):
        assert np.all(mode_leverage_g_minus(radii, eta) <= quadratic + 1e-12)
        assert np.all(mode_leverage_g_plus(radii, eta) >= quadratic - 1e-12)


def test_zero_leverage_recovers_gaussian_radial_tail_and_factor_one():
    d = 4
    radius = 2.3
    expected_tail = gammaincc(d / 2.0, radius**2 / 2.0)

    assert np.isclose(mode_leverage_tail_bound(d, 0.0, radius), expected_tail, rtol=2e-9)
    assert np.isclose(mode_leverage_factor(d, 0.0), 1.0, rtol=2e-9)


def test_mode_leverage_factor_converges_to_one_and_flags_high_leverage():
    factor_medium = mode_leverage_factor(d=2, eta=0.12)
    factor_small = mode_leverage_factor(d=2, eta=0.02)

    assert factor_medium > factor_small > 1.0
    assert abs(factor_small - 1.0) < 0.15

    try:
        mode_leverage_factor(d=2, eta=1.0)
    except ValueError as exc:
        assert "requires" in str(exc)
    else:  # pragma: no cover - protects the theorem's explicit failure gate
        raise AssertionError("eta >= 1 must not produce a finite K_d certificate")


def test_logistic_rowwise_weight_floor_on_mode_ellipsoid():
    rng = np.random.default_rng(20260821)
    X = rng.standard_normal((200, 3))
    mode = 0.4 * rng.standard_normal(3)
    prior_precision = np.diag([0.7, 1.1, 1.6])
    scores = X @ mode
    weights = 1.0 / (4.0 * np.cosh(scores / 2.0) ** 2)
    hessian = prior_precision + X.T @ (weights[:, None] * X)
    alpha, eta = logistic_mode_leverage(X, mode, hessian)

    radius = 0.8
    z = rng.standard_normal(3)
    z *= 0.75 * radius / np.linalg.norm(z)
    # np.linalg.cholesky returns L with H=L L^T; solve L^T delta=z.
    delta = np.linalg.solve(np.linalg.cholesky(hessian).T, z)
    shifted_scores = X @ (mode + delta)
    shifted_weights = 1.0 / (4.0 * np.cosh(shifted_scores / 2.0) ** 2)
    certified_floor = mode_leverage_weight_floor(weights, alpha, radius)

    assert eta < 1.0
    assert np.all(shifted_weights >= certified_floor - 1e-14)

    candidate = mode_leverage_split_candidate(
        X,
        np.linalg.inv(prior_precision),
        weights,
        alpha,
        eta,
        radius,
    )
    assert candidate["status"] == "unproved-candidate"
    assert np.allclose(candidate["wbar"], certified_floor)
    assert candidate["candidate_split_value"] >= candidate["bulk_scale"] > 0.0
    assert 0.0 <= candidate["tail_probability_bound"] <= 1.0


def test_split_candidate_rejects_understated_eta():
    X = np.eye(2)
    weights = np.full(2, 0.25)
    alpha = np.array([0.4, 0.7])

    try:
        mode_leverage_split_candidate(
            X, np.eye(2), weights, alpha, eta=0.6, radius=1.0
        )
    except ValueError as exc:
        assert "dominate" in str(exc)
    else:  # pragma: no cover - protects the candidate's conservative eta gate
        raise AssertionError("eta below max(alpha) must be rejected")


def test_one_observation_separable_family_triggers_high_leverage_gate():
    etas = []
    for a in (5.0, 20.0, 100.0):
        # At prior variance one, s=a*theta_hat solves s(1+exp(s))=a^2.
        s = brentq(lambda value: value * (1.0 + np.exp(value)) - a * a, 0.0, 20.0)
        sigmoid_s = 1.0 / (1.0 + np.exp(-s))
        weight = sigmoid_s * (1.0 - sigmoid_s)
        hessian = 1.0 + a * a * weight
        etas.append(a / np.sqrt(hessian))

    assert etas[0] > 1.0
    assert etas[0] < etas[1] < etas[2]


def test_replicated_separable_intercept_has_vanishing_row_leverage():
    etas = []
    for n in (100.0, 10_000.0):
        # With n positive unit-covariate observations, theta_hat solves
        # theta_hat(1+exp(theta_hat))=n and Hhat=1+theta_hat*sigmoid(theta_hat).
        mode = brentq(lambda value: value * (1.0 + np.exp(value)) - n, 0.0, 20.0)
        eta = 1.0 / np.sqrt(1.0 + mode / (1.0 + np.exp(-mode)))
        etas.append(eta)

    assert 0.0 < etas[1] < etas[0] < 1.0
