"""Geometry zoo + reference-bound cross-checks.

These pin the geometry kernels against closed forms and against finum's own sound refuter:
  * Gaussian: the linear-test lower bound (finum.constants.poincare_lower) reproduces the exact
    C_P = ||Sigma||_op, and the Bakry-Emery reference upper bound equals it (exact cross-check);
  * a metastable double well: the smooth mode indicator is a far tighter Rayleigh witness than a
    linear test (its lower bound is much larger) -- the whole point of carrying that witness;
  * Holley-Stroock is an UPPER bound that sits above the certified lower bound (sanity of its
    repurposing as a refutation target, never a proof).
"""

import numpy as np

from finum.constants import poincare_lower
from finum.geometries import (
    DoubleWell1D,
    GaussianDistribution,
    LinearFunction,
    PerturbedGaussian1D,
    SmoothModeIndicator1D,
    bakry_emery_cp,
    holley_stroock_cp,
    rayleigh_grid_1d,
)


def test_gaussian_linear_lower_bound_matches_operator_norm():
    cov = np.diag([0.5, 2.0, 1.3])
    g = GaussianDistribution(cov)
    rng = np.random.default_rng(0)
    lb = poincare_lower(g.sample(200_000, rng))
    assert abs(lb - g.covariance_operator_norm) < 0.05  # certified LB approaches the exact C_P


def test_bakry_emery_exact_for_gaussian():
    g = GaussianDistribution(np.diag([0.5, 2.0, 1.3]))
    # Bakry-Emery 1/m with m = lambda_min(Hess U) is EXACT for a Gaussian: equals ||Sigma||_op.
    assert abs(bakry_emery_cp(g.hessian_lower_bound) - g.covariance_operator_norm) < 1e-9


def test_mode_indicator_beats_linear_on_double_well():
    dw = DoubleWell1D(a=2.0)
    lin = rayleigh_grid_1d(dw, LinearFunction(np.array([1.0])), radius=8.0)
    mode = rayleigh_grid_1d(dw, SmoothModeIndicator1D(sharpness=4.0), radius=8.0)
    assert mode > lin            # the near-eigenfunction gives a much tighter lower bound
    assert mode <= 1e6           # finite


def test_holley_stroock_is_an_upper_bound_above_the_lower_bound():
    pg = PerturbedGaussian1D(sigma=1.0, eps=0.2, freq=1.0)
    ub = holley_stroock_cp(pg.sigma**2, pg.perturbation_oscillation_bound)
    lb = rayleigh_grid_1d(pg, LinearFunction(np.array([1.0])), radius=8.0)
    assert ub >= lb              # the (loose) analytic upper bound sits above the certified LB
    assert ub > pg.sigma**2      # the exp(osc) loss is genuinely > 1
