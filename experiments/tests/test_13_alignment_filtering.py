"""Filtering representation and stopped interval integration for q:alignment."""

import numpy as np

from finum.localization.alignment import (
    filtering_trajectory,
    grid_intervals,
    integrate_alignment_path,
)
from finum.localization.tail_union import balanced_tail_radius, observe_tail_union


def test_filtering_trajectory_is_reproducible_and_coarsens_exactly():
    a = filtering_trajectory(8, 0.4, 0.01, np.random.default_rng(123))
    b = filtering_trajectory(8, 0.4, 0.01, np.random.default_rng(123))
    assert np.array_equal(a.signal, b.signal)
    assert np.array_equal(a.tilts, b.tilts)
    coarse = a.subsample(2)
    assert np.array_equal(coarse.tilts, a.tilts[::2])
    assert np.array_equal(coarse.times, a.times[::2])


def test_filtering_mass_has_correct_ensemble_mean():
    n, T, paths = 6, 0.35, 240
    radius = balanced_tail_radius(n)
    values = []
    children = np.random.SeedSequence(91).spawn(paths)
    for child in children:
        tr = filtering_trajectory(n, T, T, np.random.default_rng(child))
        values.append(observe_tail_union(tr.tilts[-1], T, radius).p)
    values = np.asarray(values)
    stderr = values.std(ddof=1) / np.sqrt(paths)
    assert abs(values.mean() - 0.5) < 5.0 * stderr + 2e-3


def test_stopped_interval_integral_invariants_and_reproducibility():
    n, T, dt = 24, 0.3, 0.01
    intervals = grid_intervals(T, dt, (0.02, 0.05, 0.1, T))
    radius = balanced_tail_radius(n)
    tr1 = filtering_trajectory(n, T, dt, np.random.default_rng(77))
    tr2 = filtering_trajectory(n, T, dt, np.random.default_rng(77))
    a = integrate_alignment_path(tr1, radius, intervals)
    b = integrate_alignment_path(tr2, radius, intervals)
    assert np.array_equal(a.S_high, b.S_high)
    assert np.array_equal(a.r, b.r)
    assert np.array_equal(a.D, b.D)
    assert a.max_source_decomposition_error < 1e-10
    assert a.max_high_excess < 1e-12
    assert a.min_damping_gap > -1e-10
    assert a.max_bl_excess < 1e-9
    assert np.all(a.S_high >= -1e-14)
    assert np.all(a.S_high <= a.S + 1e-12)


def test_fine_path_provides_paired_time_step_refinement():
    n, T = 16, 0.2
    radius = balanced_tail_radius(n)
    intervals = np.array([[0.0, T]])
    fine = filtering_trajectory(n, T, 0.0025, np.random.default_rng(8))
    coarse = fine.subsample(2)
    fi = integrate_alignment_path(fine, radius, intervals)
    co = integrate_alignment_path(coarse, radius, intervals)
    # This is a deterministic paired convergence check, not a theorem-level tolerance.
    scale = max(abs(fi.S_high[0]), 1e-8)
    assert abs(fi.S_high[0] - co.S_high[0]) <= 0.25 * scale + 2e-3

