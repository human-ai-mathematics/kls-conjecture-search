"""Exact regressions for A5 partial noncentring and orbit connectivity."""

import numpy as np
import pytest

from finum.targets.a_series.a5 import (
    gaussian_precision_objectives,
    orbit_connectivity_height,
    partial_noncentering_optimum,
    partial_noncentering_precision,
)


def test_partial_noncentering_optimum_minimizes_both_gaussian_objectives():
    A, B, r = 2.3, 0.7, 1.8
    result = partial_noncentering_optimum(A, B, r)
    exact_alpha = 1.0 / (1.0 + r * B)
    alphas = np.linspace(0.0, 1.0, 2001)
    objectives = np.array([
        gaussian_precision_objectives(partial_noncentering_precision(A, B, r, alpha))
        for alpha in alphas
    ])

    assert np.isclose(result["alpha"], exact_alpha)
    assert abs(alphas[np.argmin(objectives[:, 0])] - exact_alpha) <= 1.0 / 2000.0
    assert abs(alphas[np.argmin(objectives[:, 1])] - exact_alpha) <= 1.0 / 2000.0

    determinants = np.array([
        np.linalg.det(partial_noncentering_precision(A, B, r, alpha))
        for alpha in (0.0, exact_alpha, 1.0)
    ])
    assert np.allclose(determinants, determinants[0])


def test_unit_endpoint_crossover_has_strictly_better_partial_midpoint():
    centered = gaussian_precision_objectives(partial_noncentering_precision(1.0, 1.0, 1.0, 0.0))
    noncentered = gaussian_precision_objectives(partial_noncentering_precision(1.0, 1.0, 1.0, 1.0))
    partial = partial_noncentering_optimum(1.0, 1.0, 1.0)

    assert np.allclose(centered, noncentered)
    assert np.isclose(partial["alpha"], 0.5)
    assert partial["C_P"] < centered[0]
    assert partial["kappa_P"] < centered[1]


def test_connectivity_height_can_exceed_the_easiest_orbit_edge():
    # Low step-two edges connect parity pairs; height-two edges connect the whole Z4 orbit.
    heights = np.array([
        [0.0, 2.0, 1.0, 2.0],
        [2.0, 0.0, 2.0, 1.0],
        [1.0, 2.0, 0.0, 2.0],
        [2.0, 1.0, 2.0, 0.0],
    ])
    result = orbit_connectivity_height(heights)

    assert result["easiest_pair"] == 1.0
    assert result["connectivity_height"] == 2.0


def test_infinite_heights_do_not_create_edges():
    disconnected = np.array([
        [0.0, 1.0, np.inf],
        [1.0, 0.0, np.inf],
        [np.inf, np.inf, 0.0],
    ])

    with pytest.raises(ValueError, match="disconnected"):
        orbit_connectivity_height(disconnected)


def test_negative_communication_heights_are_rejected():
    invalid = np.array([[0.0, -0.1], [-0.1, 0.0]])

    with pytest.raises(ValueError, match="nonnegative"):
        orbit_connectivity_height(invalid)
