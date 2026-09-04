"""Oracle 5: the mass p_t = mu_t(E) is a martingale, so E p_t = p_0.

Validates the c-SDE integrator and the conditioning jointly: a bias in either
the drift or the cut probability would break the martingale property.
"""

import numpy as np

from numerics.localization import cuts, observables as obs
from numerics.localization.state import ProductState
from numerics.localization.sde import localization_path, spawn_rngs
from numerics.localization.tilt1d import LAPLACE


def test_mass_is_martingale():
    n = 6
    T = 0.5
    dt = 0.02
    # fixed single-coordinate cut {x_0 >= 0}, balanced p_0 = 1/2 by symmetry.
    cut = cuts.single_coord(0, 0.0, psi=cuts.PSI_ID, side="ge")
    rngs = spawn_rngs(99, 400)

    p0 = obs.observe(ProductState.isotropic(LAPLACE, n), cut).p
    assert abs(p0 - 0.5) < 1e-6

    # E p_T over the ensemble at the final time.
    finals = []
    for rg in rngs:
        last = None
        for st in localization_path(LAPLACE, n, T, dt, rg):
            last = st
        finals.append(obs.observe(last, cut).p)
    finals = np.array(finals)
    mean = finals.mean()
    stderr = finals.std(ddof=1) / np.sqrt(finals.size)
    # E p_T should equal p_0 within a few standard errors.
    assert abs(mean - p0) < 5 * stderr + 1e-3
