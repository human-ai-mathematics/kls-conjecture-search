"""Oracle 4 (two-color core): Gaussian halfspace closed forms.

For a Gaussian posterior N(a, sigma^2) and a halfspace cut, the conditional
moments are truncated-normal closed forms, and the Riccati damping satisfies
(prop:gaussian-model(iv)):  r = sigma^2 phi(alpha)^2 / s,  D = r(2 sigma^2 - r) > 0.
This validates the conditional-moment path AND the observable assembly against
exact answers.
"""

import numpy as np
from scipy.stats import norm

from numerics.localization import cuts, observables as obs
from numerics.localization.state import ProductState
from numerics.localization.tilt1d import GAUSSIAN


def _setup(t=0.7, c0=0.9, x0=1.3, n=3):
    c = np.zeros(n)
    c[0] = c0
    st = ProductState(GAUSSIAN, c, t)
    a = st.mean()[0]
    sig = np.sqrt(st.A_diag()[0])
    return st, a, sig, x0


def test_conditional_moments_vs_truncated_normal():
    st, a, sig, x0 = _setup()
    cm = cuts.conditional_moments(st, cuts.halfspace(0, x0))
    al = (x0 - a) / sig
    phi, Phi = norm.pdf(al), norm.cdf(al)
    p_cf = Phi
    mE_cf = a - sig * phi / Phi
    vE_cf = sig**2 * (1 - al * phi / Phi - (phi / Phi) ** 2)
    mF_cf = a + sig * phi / (1 - Phi)
    vF_cf = sig**2 * (1 + al * phi / (1 - Phi) - (phi / (1 - Phi)) ** 2)
    assert abs(cm.p - p_cf) < 1e-4
    assert abs(cm.mE[0] - mE_cf) < 1e-4
    assert abs(cm.SigmaE[0, 0] - vE_cf) < 1e-4
    assert abs(cm.mF[0] - mF_cf) < 1e-4
    assert abs(cm.SigmaF[0, 0] - vF_cf) < 1e-4


def test_gaussian_damping_closed_form():
    st, a, sig, x0 = _setup()
    o = obs.observe(st, cuts.halfspace(0, x0))
    al = (x0 - a) / sig
    phi, Phi = norm.pdf(al), norm.cdf(al)
    s = Phi * (1 - Phi)
    sigma2 = sig**2
    r_cf = sigma2 * phi**2 / s
    D_cf = r_cf * (2 * sigma2 - r_cf)
    assert abs(o.r - r_cf) < 1e-4
    assert abs(o.D - D_cf) < 1e-4
    assert o.D > 0  # damping strictly active (prop:gaussian-model(iv))
    assert o.D >= o.r**2 - 1e-9  # coercivity D >= r^2


def test_halfspace_centroid_gap_closed_form():
    # A halfspace {x_0 <= 0} at c=0 has OPPOSITE-sign half-means, so the gap is
    # delta = m^E - m^F = -2 sigma sqrt(2/pi) (this is what drives r; not zero).
    st = ProductState(GAUSSIAN, np.zeros(3), 0.5)
    o = obs.observe(st, cuts.halfspace(0, 0.0))
    sig = np.sqrt(o.A_J[0])
    assert abs(o.p - 0.5) < 1e-6
    assert abs(o.delta_J[0] - (-2.0 * sig * np.sqrt(2.0 / np.pi))) < 1e-4
    assert o.r > 0.1  # nonzero information rate


def test_even_cut_has_zero_gap_and_degenerate_damping():
    # An EVEN single-coordinate cut {x_0^2 >= theta} (prop:two-tail(i)): by
    # symmetry m^E = m^F = 0, so delta = 0 and r = D = 0 -- the damping is
    # degenerate exactly where the source can be large.
    st = ProductState(GAUSSIAN, np.zeros(3), 0.5)
    theta = cuts.balanced_threshold(st, [0], psi=cuts.PSI_SQ, side="ge", p_target=0.5)
    cut = cuts.single_coord(0, theta, psi=cuts.PSI_SQ, side="ge")
    o = obs.observe(st, cut)
    assert abs(o.p - 0.5) < 5e-3
    assert abs(o.delta_J[0]) < 1e-6
    assert abs(o.r) < 1e-8
    assert abs(o.D) < 1e-8
