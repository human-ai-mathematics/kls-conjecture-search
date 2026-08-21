"""Exact product tail-union moments and O(n) q:alignment observables."""

import numpy as np

from finum.localization.tail_union import (
    balanced_tail_radius,
    observe_tail_union,
    tilted_laplace_symmetric_truncation,
)
from finum.localization.tilt1d import LAPLACE, tilted


def _quadrature_truncation(c, t, radius):
    marginal = tilted(
        LAPLACE, c, t, order=1200, half_width=36.0, passes=3,
        extra_breaks=(-radius, radius),
    )
    mask = np.abs(marginal.nodes) < radius
    probability = float(marginal.weights[mask].sum())
    mean = float(np.dot(marginal.weights[mask], marginal.nodes[mask]) / probability)
    second = float(np.dot(marginal.weights[mask], marginal.nodes[mask] ** 2) / probability)
    return probability, mean, second - mean * mean, marginal.mean, marginal.var


def test_balanced_radius_is_exact_across_dimensions():
    for n in (1, 2, 10, 100, 10_000):
        radius = balanced_tail_radius(n)
        obs = observe_tail_union(np.zeros(n), 0.0, radius)
        assert abs(obs.p - 0.5) < 2e-12


def test_closed_form_truncation_matches_independent_quadrature():
    cases = [
        (0.0, 0.0, 3.5),
        (1.0, 0.01, 3.5),
        (-1.3, 0.02, 3.5),
        (1.4, 0.01, 3.5),
        (2.0, 0.1, 3.5),
        (-3.0, 0.5, 2.0),
    ]
    for c, t, radius in cases:
        exact = tilted_laplace_symmetric_truncation(c, t, radius)
        probability, mean, variance, full_mean, full_variance = _quadrature_truncation(
            c, t, radius,
        )
        assert abs(exact.probability - probability) < 2e-9
        assert abs(exact.mean - mean) < 2e-8
        assert abs(exact.variance - variance) < 2e-8
        assert abs(exact.full_mean - full_mean) < 2e-8
        assert abs(exact.full_variance - full_variance) < 2e-8


def test_small_time_formula_does_not_suffer_normal_tail_cancellation():
    reference = tilted_laplace_symmetric_truncation(0.0, 0.0, 3.5)
    tiny = tilted_laplace_symmetric_truncation(0.0, 1.0e-12, 3.5)
    assert abs(tiny.full_variance - 1.0) < 5e-11
    assert abs(tiny.probability - reference.probability) < 5e-10
    assert abs(tiny.variance - reference.variance) < 5e-10


def test_incident_high_formula_matches_dense_matrix_definition():
    c = np.array([1.25, -0.4, 0.8, -1.1, 0.2])
    t = 0.08
    radius = balanced_tail_radius(c.size)
    threshold = 2.0
    obs = observe_tail_union(c, t, radius, high_threshold=threshold)

    stats = [tilted_laplace_symmetric_truncation(ci, t, radius) for ci in c]
    z = np.array([x.probability for x in stats])
    u = np.array([x.mean for x in stats])
    w = np.array([x.variance for x in stats])
    m = np.array([x.full_mean for x in stats])
    A = np.array([x.full_variance for x in stats])
    q = float(np.prod(z)); p = 1.0 - q; s = p * q
    delta = (m - u) / p
    G = np.diag((A - w) / p) - q * np.outer(delta, delta)
    high = A >= threshold
    low = ~high
    direct_S = s * float(np.sum(G * G))
    direct_high = s * (
        float(np.sum(G[np.ix_(high, high)] ** 2))
        + 2.0 * float(np.sum(G[np.ix_(low, high)] ** 2))
    )
    direct_D = 2.0 * s * float(np.dot(A, delta * delta)) - (s * np.dot(delta, delta)) ** 2

    assert abs(obs.S - direct_S) < 1e-12
    assert abs(obs.S_high - direct_high) < 1e-12
    assert abs(obs.D - direct_D) < 1e-12
    assert abs(obs.S - obs.S_high - obs.S_low) < 1e-12
    assert obs.D >= obs.r**2 - 1e-12

