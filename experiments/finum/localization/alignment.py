"""Filtering-path simulation and interval occupation for product ``q:alignment``.

If ``X`` has the initial law and ``B_t`` is an independent Brownian motion, then

    c_t = t X + B_t

has the same observation-filtration law as Eldan's tilt process
``dc_t=dW_t+E[X|c_t]dt``.  Sampling this filtering representation eliminates the
Euler drift error from path experiments.  Only the deterministic time integral
is discretised.

This module is deliberately specific to the isotropic Laplace product and the
tail-union cut implemented in :mod:`finum.localization.tail_union`.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .tail_union import TailUnionObservables, observe_tail_union


@dataclass(frozen=True)
class FilteringTrajectory:
    """One exact-on-grid filtering trajectory ``c_t=tX+B_t``."""

    times: np.ndarray
    tilts: np.ndarray
    signal: np.ndarray

    @property
    def n(self) -> int:
        return int(self.signal.size)

    def subsample(self, stride: int) -> "FilteringTrajectory":
        """Select every ``stride``-th node, retaining the terminal node."""

        if stride < 1:
            raise ValueError("stride must be positive")
        idx = np.arange(0, self.times.size, int(stride), dtype=int)
        if idx[-1] != self.times.size - 1:
            idx = np.append(idx, self.times.size - 1)
        return FilteringTrajectory(self.times[idx], self.tilts[idx], self.signal)


def filtering_trajectory(
    n: int,
    T: float,
    dt: float,
    rng: np.random.Generator,
) -> FilteringTrajectory:
    """Sample a product-Laplace localization trajectory without Euler drift error."""

    if int(n) != n or n < 1:
        raise ValueError("n must be a positive integer")
    if T <= 0.0 or dt <= 0.0:
        raise ValueError("T and dt must be positive")
    n_steps = int(np.ceil(T / dt - 1.0e-14))
    times = np.minimum(np.arange(n_steps + 1, dtype=float) * dt, T)
    times[-1] = T
    increments = np.diff(times)

    signal = rng.laplace(loc=0.0, scale=1.0 / np.sqrt(2.0), size=int(n))
    dB = rng.standard_normal((n_steps, int(n))) * np.sqrt(increments)[:, None]
    brownian = np.vstack([np.zeros((1, int(n))), np.cumsum(dB, axis=0)])
    tilts = times[:, None] * signal[None, :] + brownian
    return FilteringTrajectory(times=times, tilts=tilts, signal=signal)


@dataclass(frozen=True)
class AlignmentPathIntegrals:
    """Stopped occupation integrals over a deterministic list of intervals."""

    intervals: np.ndarray
    S_high: np.ndarray
    S: np.ndarray
    r: np.ndarray
    D: np.ndarray
    high_count: np.ndarray
    tau: float
    tau_hit: bool
    p_terminal: float
    max_lambda: float
    max_source_decomposition_error: float
    max_high_excess: float
    min_damping_gap: float
    max_bl_excess: float


def _add_linear_segment(
    accum: np.ndarray,
    intervals: np.ndarray,
    t0: float,
    t1: float,
    y0: np.ndarray,
    y1: np.ndarray,
) -> None:
    """Integrate a linearly interpolated vector over all interval intersections."""

    if t1 <= t0:
        return
    left = np.maximum(intervals[:, 0], t0)
    right = np.minimum(intervals[:, 1], t1)
    active = right > left
    if not np.any(active):
        return
    h = t1 - t0
    al = ((left[active] - t0) / h)[:, None]
    ar = ((right[active] - t0) / h)[:, None]
    yl = y0[None, :] + al * (y1 - y0)[None, :]
    yr = y0[None, :] + ar * (y1 - y0)[None, :]
    accum[active] += 0.5 * (yl + yr) * (right[active] - left[active])[:, None]


def integrate_alignment_path(
    trajectory: FilteringTrajectory,
    radius: float,
    intervals: np.ndarray,
    *,
    high_threshold: float = 2.0,
    balanced_window: tuple[float, float] = (1.0 / 3.0, 2.0 / 3.0),
) -> AlignmentPathIntegrals:
    """Integrate ``(S_high,S,r,D,#high)`` until the balanced exit time.

    The crossing inside the last grid step and its integrands are linearly
    interpolated, matching the stopping convention of the pre-existing engine.
    """

    intervals = np.asarray(intervals, dtype=float)
    if intervals.ndim != 2 or intervals.shape[1] != 2:
        raise ValueError("intervals must have shape (k,2)")
    if np.any(intervals[:, 0] < 0.0) or np.any(intervals[:, 1] <= intervals[:, 0]):
        raise ValueError("intervals must satisfy 0 <= left < right")
    if np.any(intervals[:, 1] > trajectory.times[-1] + 1.0e-12):
        raise ValueError("intervals must lie inside the trajectory horizon")

    accum = np.zeros((intervals.shape[0], 5), dtype=float)
    lo, hi = balanced_window
    previous: TailUnionObservables | None = None
    previous_y = None
    previous_t = 0.0
    tau = float(trajectory.times[-1])
    tau_hit = False
    max_lambda = 0.0
    max_decomp = 0.0
    max_high_excess = 0.0
    min_damping_gap = np.inf
    max_bl_excess = 0.0
    terminal_p = 0.5

    for t, c in zip(trajectory.times, trajectory.tilts):
        obs = observe_tail_union(c, float(t), radius, high_threshold=high_threshold)
        terminal_p = obs.p
        y = np.array([obs.S_high, obs.S, obs.r, obs.D, float(obs.high_count)])
        max_lambda = max(max_lambda, obs.lambda_max)
        max_decomp = max(max_decomp, abs(obs.S - obs.S_high - obs.S_low))
        max_high_excess = max(max_high_excess, obs.S_high - obs.S)
        min_damping_gap = min(min_damping_gap, obs.D - obs.r * obs.r)
        if t > 0.0:
            max_bl_excess = max(max_bl_excess, obs.lambda_max - 1.0 / t)

        if previous is not None:
            outside = not (lo <= obs.p <= hi)
            if outside:
                boundary = lo if obs.p < lo else hi
                denom = obs.p - previous.p
                fraction = 1.0 if denom == 0.0 else (boundary - previous.p) / denom
                fraction = min(max(float(fraction), 0.0), 1.0)
                crossing_t = previous_t + fraction * (float(t) - previous_t)
                crossing_y = previous_y + fraction * (y - previous_y)
                _add_linear_segment(
                    accum, intervals, previous_t, crossing_t, previous_y, crossing_y,
                )
                tau = crossing_t
                tau_hit = True
                terminal_p = boundary
                break

            _add_linear_segment(accum, intervals, previous_t, float(t), previous_y, y)

        previous = obs
        previous_y = y
        previous_t = float(t)

    return AlignmentPathIntegrals(
        intervals=intervals.copy(),
        S_high=accum[:, 0], S=accum[:, 1], r=accum[:, 2], D=accum[:, 3],
        high_count=accum[:, 4], tau=tau, tau_hit=tau_hit, p_terminal=terminal_p,
        max_lambda=max_lambda, max_source_decomposition_error=max_decomp,
        max_high_excess=max_high_excess, min_damping_gap=min_damping_gap,
        max_bl_excess=max_bl_excess,
    )


def grid_intervals(T: float, dt: float, widths: tuple[float, ...]) -> np.ndarray:
    """All deterministic grid-aligned intervals of the requested widths."""

    if T <= 0.0 or dt <= 0.0:
        raise ValueError("T and dt must be positive")
    items: list[tuple[float, float]] = []
    for width in widths:
        steps = max(1, int(round(float(width) / dt)))
        actual = steps * dt
        if actual > T + 1.0e-12:
            continue
        last_start = int(np.floor((T - actual) / dt + 1.0e-12))
        for j in range(last_start + 1):
            items.append((j * dt, j * dt + actual))
    if not items:
        raise ValueError("no requested width fits inside the horizon")
    return np.array(sorted(set(items)), dtype=float)

