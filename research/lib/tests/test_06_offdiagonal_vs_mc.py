"""The surrogate guard: off-diagonal conditional covariance vs independent MC.

The retracted energy-shell result came from a Gaussian-regression surrogate for
Cov(x_i, x_j | E). This test pins the leave-two-out computation against an
INDEPENDENT inverse-CDF Monte-Carlo sampler (not the quadrature atoms) for a
genuinely anisotropic tilted product and a multi-coordinate energy-shell cut --
exactly the regime the surrogate got wrong.
"""

import numpy as np

from numerics.localization import cuts
from numerics.localization.state import ProductState
from numerics.localization.tilt1d import LAPLACE


def _inverse_cdf_sampler(c_i, t, rng, N):
    u = np.linspace(-32.0, 32.0, 300_000)
    logd = LAPLACE.neg_potential(u) + c_i * u - 0.5 * t * u * u
    logd -= logd.max()
    d = np.exp(logd)
    cdf = np.cumsum(d)
    cdf /= cdf[-1]
    return np.interp(rng.random(N), cdf, u)


def test_offdiagonal_conditional_covariance_matches_mc():
    rng = np.random.default_rng(0)
    n, t = 4, 0.6
    c = np.array([1.2, -0.7, 0.4, 0.0])
    st = ProductState(LAPLACE, c, t)

    theta = cuts.balanced_threshold(st, range(n), psi=cuts.PSI_SQ, side="ge", p_target=0.5)
    cut = cuts.block_sum(range(n), theta, psi=cuts.PSI_SQ, side="ge")
    cm = cuts.conditional_moments(st, cut, n_bins=131072)

    N = 3_000_000
    X = np.stack([_inverse_cdf_sampler(c[i], t, rng, N) for i in range(n)], axis=1)
    inE = (X**2).sum(1) >= theta
    XE = X[inE]
    mE_mc = XE.mean(0)
    SE_mc = np.cov(XE, rowvar=False)

    # p within MC error (+ background-binning floor).
    assert abs(cm.p - inE.mean()) < 3e-3
    # conditional means.
    assert np.max(np.abs(cm.mE - mE_mc)) < 8e-3
    # FULL conditional covariance incl. off-diagonal (the surrogate guard).
    assert np.max(np.abs(cm.SigmaE - SE_mc)) < 8e-3
    # the off-diagonals are genuinely non-zero (so this is a real test).
    offdiag = cm.SigmaE - np.diag(np.diag(cm.SigmaE))
    assert np.max(np.abs(offdiag)) > 0.03
