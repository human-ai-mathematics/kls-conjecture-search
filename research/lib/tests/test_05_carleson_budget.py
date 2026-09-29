"""Oracles 6-8: per-direction Carleson, coordinate budget, rank-one extinction.

These are the proved upper bounds on the source occupation. Because they are
*inequalities* obeyed by E int_0^infty S dt, any finite-horizon Monte-Carlo
estimate must also satisfy them (within sampling error) -- so modest params
suffice. A gross violation would mean the source S = s||G||^2 is mis-assembled.
"""

import numpy as np
import pytest

from numerics.localization import cuts, observables as obs
from numerics.localization.state import ProductState
from numerics.localization.sde import spawn_rngs
from numerics.localization.tilt1d import LAPLACE

FAST = {"n_bins": 16384}
pytestmark = pytest.mark.slow


def _occupation(cut, n, *, T, dt, seed, n_paths, direction=None):
    rngs = spawn_rngs(seed, n_paths)
    s_vals, dir_vals = [], []
    for rg in rngs:
        pi = obs.integrate_path(LAPLACE, n, cut, T, dt, rg, direction=direction, cm_kw=FAST)
        s_vals.append(pi.xi_S)
        dir_vals.append(pi.xi_dir)
    return np.array(s_vals), np.array(dir_vals)


def test_rank_one_budget_below_one():
    # cor:refutation: single-coordinate cut has E int_0^infty S dt <= 1.
    cut = cuts.single_coord(0, 0.0, psi=cuts.PSI_ID, side="ge")
    s_vals, _ = _occupation(cut, n=8, T=6.0, dt=0.03, seed=11, n_paths=48)
    mean = s_vals.mean()
    stderr = s_vals.std(ddof=1) / np.sqrt(s_vals.size)
    assert mean + 3 * stderr <= 1.0  # comfortably under the rank-one budget
    assert s_vals.max() <= 1.0       # even pathwise here


def test_per_direction_carleson():
    # cor:per-direction: E int s |G e_i|^2 dt <= (R0)_ii <= 1.
    n = 4
    cut = cuts.block_sum([0, 1, 2], theta=0.0, psi=cuts.PSI_ID, side="ge")
    R0_00 = obs.R0_diag(ProductState.isotropic(LAPLACE, n), cut, coord=0, **FAST)
    assert R0_00 <= 1.0 + 1e-6
    _, dir_vals = _occupation(cut, n, T=3.0, dt=0.06, seed=5, n_paths=16, direction=0)
    mean = dir_vals.mean()
    stderr = dir_vals.std(ddof=1) / np.sqrt(dir_vals.size)
    assert mean - 3 * stderr <= R0_00 + 0.05  # within R0_00 (<=1) up to MC error


def test_coordinate_budget_below_k():
    # thm:budget: k-coordinate cut has E int_0^infty S dt <= k.
    k = 3
    n = 4
    cut = cuts.block_sum(range(k), theta=0.0, psi=cuts.PSI_ID, side="ge")
    s_vals, _ = _occupation(cut, n, T=3.0, dt=0.06, seed=3, n_paths=16)
    mean = s_vals.mean()
    stderr = s_vals.std(ddof=1) / np.sqrt(s_vals.size)
    assert mean + 3 * stderr <= k
