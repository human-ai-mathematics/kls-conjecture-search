"""Oracle: the thin-shell (P6 / q:alignment) family respects the proved facts.

Before trusting any DIRECTIONAL thin-shell run (runs/2026-06-18-thinshell-alignment.py)
the machinery must reproduce settled facts on the permutation-symmetric thin-shell cut
``E = {sum_i x_i^2 >= theta}``:

  * ``balanced_threshold`` pins the cut at mass 1/2 (``cuts.balanced_threshold``);
  * the source occupation respects the coordinate budget ``E int_0^inf S <= k``
    (``thm:budget``) -- here the tau-stopped finite-horizon mean is well under ``k=n``;
  * the ``n_bins`` convergence gate passes on this family;
  * the path integral is bit-for-bit reproducible from its seed.

Small ``n`` and a short horizon keep this in the suite; the deferred large-``n`` run is
gated on these plus the FFT-vs-MC cross-check (``finum.localization.gates.fft_vs_mc``).
"""

import numpy as np

from finum.localization import cuts, gates
from finum.localization.state import ProductState
from finum.localization.observables import ensemble_mean, integrate_path
from finum.localization.sde import make_rng
from finum.localization.tilt1d import LAPLACE


def _balanced_thinshell(n: int):
    state0 = ProductState.isotropic(LAPLACE, n)
    theta = cuts.balanced_threshold(state0, range(n), psi=cuts.PSI_SQ, side="ge", p_target=0.5)
    cut = cuts.block_sum(range(n), theta, psi=cuts.PSI_SQ, side="ge")
    return state0, cut


def test_thinshell_is_balanced_at_t0():
    n = 3
    state0, cut = _balanced_thinshell(n)
    cm = cuts.conditional_moments(state0, cut, n_bins=1 << 16)
    assert abs(cm.p - 0.5) < 2e-2


def test_thinshell_respects_coordinate_budget():
    n = 3
    state0, cut = _balanced_thinshell(n)
    T, dt, paths = 0.5, 0.1, 6
    xi = np.array([
        integrate_path(LAPLACE, n, cut, T, dt, make_rng(1234 + j),
                       stop_at_tau=True, cm_kw={"n_bins": 1 << 16}).xi_S
        for j in range(paths)
    ])
    res = ensemble_mean(xi, "xi_S")
    # thm:budget: E int_0^inf S <= k = n; the tau-stopped finite-horizon mean is below it.
    assert res.mean <= n + 1e-9
    # and the source is genuinely active (not a trivially-zero test).
    assert res.mean > 0.0


def test_thinshell_n_bins_gate_passes():
    n = 3
    state0, cut = _balanced_thinshell(n)
    g = gates.n_bins_convergence(state0, cut, n_bins_list=(1 << 14, 1 << 15, 1 << 16))
    assert g.passed, str(g)


def test_thinshell_path_is_reproducible():
    n = 3
    _, cut = _balanced_thinshell(n)
    a = integrate_path(LAPLACE, n, cut, 0.4, 0.1, make_rng(777),
                       stop_at_tau=True, cm_kw={"n_bins": 1 << 15}).xi_S
    b = integrate_path(LAPLACE, n, cut, 0.4, 0.1, make_rng(777),
                       stop_at_tau=True, cm_kw={"n_bins": 1 << 15}).xi_S
    assert a == b
