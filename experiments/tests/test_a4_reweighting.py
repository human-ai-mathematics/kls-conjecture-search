"""Focused regression for A4's separated-mixture witnesses."""

import numpy as np

from finum.targets.a_series.a4 import sep_mixture_witnesses


def test_epsilon_reweighting_exercises_a_different_barrier_than_mode_collapse():
    collapse, sweep = sep_mixture_witnesses(
        a=3.0,
        sigma=1.0,
        epsilons=np.array([1e-3, 3e-3, 1e-2, 3e-2, 0.1, 0.25]),
    )

    assert all(record["kl"] > 0.0 for record in sweep)
    assert all(a["kl"] < b["kl"] for a, b in zip(sweep, sweep[1:]))
    assert sweep[0]["ratio"] > collapse
    assert sweep[0]["ratio"] > sweep[-1]["ratio"]
