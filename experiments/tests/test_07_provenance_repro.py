"""Oracle 9 (machinery): provenance recording and bit-for-bit reproducibility.

The original failure was "two agents' MC disagreed, neither's code in the repo." Committed code
is necessary but not sufficient: the run must reproduce exactly from its recorded seed. These
tests pin both the provenance header (numerics.artifact) and the determinism of the seeded path
integral (numerics.localization).
"""

import numpy as np

from numerics import artifact as provenance
from numerics.localization import cuts, observables as obs
from numerics.localization.sde import make_rng, spawn_rngs
from numerics.localization.tilt1d import LAPLACE


def test_provenance_header_fields():
    h = provenance.provenance(target="test", profile="standard",
                              stochastic=True, config={"seed": 7, "dt": 0.01, "n": 16})
    assert set(h) >= {"schema_version", "git_commit", "git_dirty", "git_diff_sha256",
                      "target", "profile", "stochastic", "config", "environment"}
    assert h["schema_version"] == 1
    assert h["environment"]["scipy"] is not None
    assert h["config"]["seed"] == 7
    assert h["environment"]["numpy"] == np.__version__


def test_spawned_streams_are_independent_and_reproducible():
    a1, a2 = spawn_rngs(123, 2)
    b1, b2 = spawn_rngs(123, 2)
    x1 = a1.standard_normal(5)
    y1 = b1.standard_normal(5)
    assert np.array_equal(x1, y1)              # reproducible from the same seed
    assert not np.array_equal(x1, a2.standard_normal(5))  # independent streams


def test_path_integral_bit_for_bit():
    cut = cuts.single_coord(0, 0.0, psi=cuts.PSI_ID, side="ge")
    r1 = obs.integrate_path(LAPLACE, 6, cut, 1.0, 0.05, make_rng(2024))
    r2 = obs.integrate_path(LAPLACE, 6, cut, 1.0, 0.05, make_rng(2024))
    assert r1.xi_S == r2.xi_S           # exact float equality, same seed
    assert r1.xi_r == r2.xi_r
    assert r1.t_stop == r2.t_stop
