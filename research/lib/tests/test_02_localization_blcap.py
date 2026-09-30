"""Oracle 3-4: Gaussian deterministic covariance and the pathwise BL cap.

- Gaussian model (prop:gaussian-model): A_t = (1+t)^{-1} I on EVERY path,
  to machine precision -- a strong end-to-end check of the integrator.
- Brascamp-Lieb cap (eq:BL-cap): lambda_max(A_t) <= 1/t pathwise; the
  integrator asserts it every step, so a clean Laplace run not raising is the
  test (covariance genuinely inflates, so the cap is non-trivial).
"""

import numpy as np

from numerics.localization.state import ProductState
from numerics.localization.sde import localization_path, make_rng
from numerics.localization.tilt1d import GAUSSIAN, LAPLACE


def test_gaussian_covariance_deterministic():
    rng = make_rng(12345)
    max_err = 0.0
    for st in localization_path(GAUSSIAN, n=6, T=2.0, dt=0.01, rng=rng):
        if st.t == 0.0:
            continue
        err = np.max(np.abs(st.A_diag() - 1.0 / (1.0 + st.t)))
        max_err = max(max_err, err)
    assert max_err < 1e-12


def test_bl_cap_holds_on_laplace_path():
    # check_bl=True inside localization_path raises on violation; reaching the
    # end is the assertion. Also verify the cap is genuinely active (inflation).
    rng = make_rng(7)
    lam = []
    for st in localization_path(LAPLACE, n=40, T=1.0, dt=0.005, rng=rng):
        if st.t > 0:
            assert st.lambda_max() <= 1.0 / st.t + 1e-6
        lam.append(st.lambda_max())
    assert max(lam) > 1.5  # covariance really does inflate past 1


def test_isotropic_initial_state():
    st = ProductState.isotropic(LAPLACE, n=5)
    assert st.t == 0.0
    assert np.allclose(st.A_diag(), 1.0, atol=1e-7)  # isotropic
    assert np.allclose(st.mean(), 0.0, atol=1e-10)
