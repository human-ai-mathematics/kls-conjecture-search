"""Focused regressions for A3's standard-horseshoe diagnostic."""

import numpy as np

from finum.targets.a_series.a3 import (
    _scaled_exp1,
    horseshoe_bracket,
    horseshoe_density_shape,
    horseshoe_e1_rational_upper,
    horseshoe_odd_barta_residual_lower,
)


def test_exact_horseshoe_density_is_a_scale_family():
    xs = np.array([0.05, 0.5, 2.0])
    base = horseshoe_density_shape(xs, 1.0)

    for tau in (0.5, 2.0):
        scaled = tau * horseshoe_density_shape(tau * xs, tau)
        np.testing.assert_allclose(scaled, base, rtol=2e-14, atol=0.0)


def test_horseshoe_hardy_and_fem_diagnostics_are_scale_invariant():
    reference = horseshoe_bracket(1.0, x_max=100.0, n=2001)[:2]

    for tau in (0.5, 2.0):
        observed = horseshoe_bracket(tau, x_max=100.0, n=2001)[:2]
        np.testing.assert_allclose(observed, reference, rtol=1e-9, atol=1e-12)


def test_horseshoe_e1_rational_upper_regression():
    """Numerical regression only; the proof uses the positive integral remainder."""
    a = np.geomspace(1e-8, 40.0, 2001)
    slack = horseshoe_e1_rational_upper(a) - _scaled_exp1(a)
    assert np.all(slack > 0.0)


def test_horseshoe_odd_barta_residual_certificate_is_positive():
    """The sampled check guards the closed algebraic residual, not the theorem's status."""
    y = np.linspace(0.0, 12.0, 2401)
    residual = horseshoe_odd_barta_residual_lower(y)
    assert residual[0] == 0.5
    assert np.all(residual > 0.0)
