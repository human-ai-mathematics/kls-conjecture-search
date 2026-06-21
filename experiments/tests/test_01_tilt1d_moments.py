"""Oracle 1-2: 1D tilted-moment correctness and quadrature convergence.

The most foundational test: if the 1D moments are wrong, everything downstream
is the original retracted bug. In particular the isotropic two-sided exponential
must give Var(x^2) = 5 (the retraction used the Gaussian surrogate's 4/pi).
"""

import numpy as np

from finum.localization.tilt1d import GAUSSIAN, LAPLACE, tilted


def test_laplace_isotropic_moments():
    # exp(-sqrt(2)|x|)/sqrt(2): E x^2 = 1, E x^4 = 6, Var(x^2) = 5.
    m = tilted(LAPLACE, 0.0, 0.0)
    assert abs(m.mean) < 1e-10
    assert abs(m.moment(2) - 1.0) < 1e-8
    assert abs(m.moment(4) - 6.0) < 1e-7
    assert abs((m.moment(4) - m.moment(2) ** 2) - 5.0) < 1e-7  # the retraction guard


def test_gaussian_variance_is_exact_one_over_one_plus_t():
    # Gaussian base: Var(mu_{0,t}) = 1/(1+t) in closed form (machine precision).
    for t in [0.0, 0.5, 2.0, 10.0, 50.0]:
        m = tilted(GAUSSIAN, 0.0, t)
        assert abs(m.var - 1.0 / (1.0 + t)) < 1e-12


def test_gaussian_tilted_mean():
    for c, t in [(1.0, 0.0), (3.0, 2.0), (5.0, 10.0)]:
        m = tilted(GAUSSIAN, c, t)
        assert abs(m.mean - c / (1.0 + t)) < 1e-10


def test_weights_normalized():
    for base in (LAPLACE, GAUSSIAN):
        for c, t in [(0.0, 0.0), (1.5, 0.7), (0.0, 5.0)]:
            m = tilted(base, c, t)
            assert abs(m.weights.sum() - 1.0) < 1e-13
            assert m.nodes.dtype == np.float64


def test_moment_convergence_order_and_width():
    # Var(x^2) for Laplace stable under order-doubling and wider truncation.
    ref = tilted(LAPLACE, 0.0, 0.0, order=800, half_width=34).moment(4)
    coarse = tilted(LAPLACE, 0.0, 0.0, order=300, half_width=26).moment(4)
    assert abs(ref - 6.0) < 1e-9
    assert abs(coarse - ref) < 1e-6


def test_bl_cap_respected_by_single_marginal():
    # Var(mu_{c,t}) <= 1/t for the tilted Laplace (BL cap at the 1D level).
    for c in [0.0, 2.0, -3.0]:
        for t in [0.2, 1.0, 5.0]:
            assert tilted(LAPLACE, c, t).var <= 1.0 / t + 1e-9
