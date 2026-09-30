"""Source-screened cut-local supply diagnostic for KLS ``conj:weighted-excess-rate`` (target ``kls-screen``).

Sibling of ``kls-align``: it reuses the same isotropic product-Laplace tail-union localization
engine and the same balanced stopping convention, but computes the objects parked as
Candidates A and B by the ``w3`` route probe
(``research/explorations/2026-08-27-kls-route-prober-cut-local-weighted-replacement-w3.md``):
the cut scale ``lambda_cut``, the weight ``W_cut=(1+lambda_cut)^{5/2}``, the Stein source
``Q_t=s_t||K_t||_HS^2``, the aligned set ``A_{kappa,t}={Q_t >= kappa e_t W_cut}``, the screened
supply, and the complement source fraction ``theta``.

``kls-align`` is not modified and its record schema is untouched.

Epistemic contract
------------------
``e_t = P_t - I_{mu_t}(p_t)`` is not computable, so every excess here is the surrogate
``ehat_t = (P_t - Ihat_t)_+`` built from explicit competitor sets.  Since a competitor gives
an *upper* bound on the profile, ``ehat_t <= e_t``: the surrogate **understates** the excess
and every supply integral reported here is a **lower bound** for the corresponding true
integral.  Consequently

* surrogate growth in ``n`` is directional evidence *against* a bounded supply;
* surrogate boundedness is weak evidence *for* one, and certifies nothing.

Nothing emitted changes a ledger status, certifies a dossier, or justifies a proof step.
"""

from __future__ import annotations

import numpy as np

from ...contract import RunResult, lift_observations
from ...localization.alignment import _add_linear_segment, filtering_trajectory, grid_intervals
from ...localization.screening import (
    cut_mass,
    dense_cut_scale,
    dense_cut_tensor,
    marginals,
    minkowski_perimeter_estimate,
    screened_state,
)
from ...localization.tail_union import balanced_tail_radius, observe_tail_union


TARGET = "conj:weighted-excess-rate"
_MODEL = "isotropic-laplace-product/tail-union/cut-local-screened"

#: Fixed before any run of this target; also emitted verbatim into the artifact.
PREREGISTERED_DECISION = {
    "fixed_before_run": True,
    "screening_kappa_of_record": 0.05,
    "support_theta_hat_max_on_every_selected_interval": 0.5,
    "support_aligned_supply_growth_factor_max": 1.5,
    "against_theta_hat_min_on_pulse_window_at_top_n": 0.8,
    "against_requires_theta_hat_increasing_in_n": True,
    "against_linear_growth_min_fraction_of_dimension_ratio": 0.5,
    "spectator_lambda_cut_block_invariance_tol": 1.0e-10,
    "spectator_pathwise_supply_invariance_tol": 1.0e-12,
    "spectator_supply_stderr_multiple": 3.0,
    "surrogate_direction": "ehat <= e (competitor upper-bounds the profile)",
    "note": (
        "support outcomes are weak because the surrogate understates the excess; "
        "against outcomes are the robust direction"
    ),
}

#: The cut scale above which a time is called an aligned-scale occupation time.
BIG_SCALE_THRESHOLD = 2.0

_BALANCED_WINDOW = (1.0 / 3.0, 2.0 / 3.0)


def _gate(name: str, passed: bool, measured: float, tol: float, detail: str) -> dict:
    return {
        "gate": name,
        "status": "run",
        "passed": bool(passed),
        "measured": float(measured),
        "tol": float(tol),
        "detail": detail,
    }


def _mean_se(values: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    values = np.asarray(values, dtype=float)
    mean = values.mean(axis=0)
    if values.shape[0] > 1:
        se = values.std(axis=0, ddof=1) / np.sqrt(values.shape[0])
    else:
        se = np.full_like(mean, np.nan)
    return mean, se


def _channels(kappas: tuple[float, ...]) -> list[str]:
    base = ["Q", "supply", "supply_halfline", "S_high", "S", "r", "D", "supply_big_scale"]
    base += [f"aligned_supply@{k:.3g}" for k in kappas]
    base += [f"complement_Q@{k:.3g}" for k in kappas]
    return base


def _state_vector(state, kappas: tuple[float, ...]) -> np.ndarray:
    supply = state.surrogate.excess_rich * state.W_cut
    supply_hl = state.surrogate.excess_halfline * state.W_cut
    values = [
        state.Q, supply, supply_hl, state.S_high, state.S, state.r, state.D,
        supply if state.lambda_cut >= BIG_SCALE_THRESHOLD else 0.0,
    ]
    aligned = [supply if state.Q >= k * supply else 0.0 for k in kappas]
    complement = [0.0 if state.Q >= k * supply else state.Q for k in kappas]
    return np.array(values + aligned + complement, dtype=float)


def _balanced_exit(times: np.ndarray, masses: np.ndarray) -> tuple[float, bool]:
    """Linearly interpolated first exit of ``p_t`` from ``[1/3,2/3]`` on the fine grid."""

    lo, hi = _BALANCED_WINDOW
    for k in range(1, times.size):
        p = float(masses[k])
        if lo <= p <= hi:
            continue
        boundary = lo if p < lo else hi
        denom = p - float(masses[k - 1])
        fraction = 1.0 if denom == 0.0 else (boundary - float(masses[k - 1])) / denom
        fraction = min(max(float(fraction), 0.0), 1.0)
        return float(times[k - 1] + fraction * (times[k] - times[k - 1])), True
    return float(times[-1]), False


def _integrate_snapshots(
    times: np.ndarray,
    values: np.ndarray,
    intervals: np.ndarray,
    tau: float,
) -> np.ndarray:
    """Trapezoidal occupation of every channel over each interval, stopped at ``tau``."""

    accum = np.zeros((intervals.shape[0], values.shape[1]), dtype=float)
    for j in range(times.size - 1):
        t0 = float(times[j])
        t1 = float(times[j + 1])
        if t0 >= tau:
            break
        if t1 <= tau:
            _add_linear_segment(accum, intervals, t0, t1, values[j], values[j + 1])
            continue
        fraction = (tau - t0) / (t1 - t0)
        edge = values[j] + fraction * (values[j + 1] - values[j])
        _add_linear_segment(accum, intervals, t0, tau, values[j], edge)
        break
    return accum


def _phi_correlation(x: np.ndarray, y: np.ndarray) -> float:
    """Pearson correlation of two 0/1 sequences; NaN when either is constant."""

    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    if x.size < 3 or x.std() == 0.0 or y.std() == 0.0:
        return float("nan")
    return float(np.corrcoef(x, y)[0, 1])


def _nan_mean_se(values: np.ndarray) -> tuple[float, float, int]:
    values = np.asarray(values, dtype=float)
    finite = values[np.isfinite(values)]
    if finite.size == 0:
        return float("nan"), float("nan"), 0
    mean = float(finite.mean())
    se = float(finite.std(ddof=1) / np.sqrt(finite.size)) if finite.size > 1 else float("nan")
    return mean, se, int(finite.size)


# --------------------------------------------------------------------------------------
# one configuration
# --------------------------------------------------------------------------------------


def _run_configuration(
    n: int,
    seed_sequence,
    *,
    T: float,
    dt: float,
    snapshot_stride: int,
    n_paths: int,
    kappas: tuple[float, ...],
    widths: tuple[float, ...],
    high_threshold: float,
    block_size: int,
    dense_until: float,
):
    radius = balanced_tail_radius(n)
    dt_snapshot = dt * snapshot_stride
    channels = _channels(kappas)
    requested = tuple(sorted(set(tuple(float(w) for w in widths) + (float(T),))))
    intervals = grid_intervals(T, dt_snapshot, requested)

    path_children = seed_sequence.spawn(n_paths)
    # The surrogate excess has a steep initial layer: the coordinate half-line competitor
    # collapses as soon as the extreme tilt appears.  A uniform snapshot grid fails this
    # target's own paired refinement gate there, so the grid is refined on [0, dense_until].
    n_steps_probe = int(np.ceil(T / dt - 1.0e-14))
    probe_times = np.minimum(np.arange(n_steps_probe + 1, dtype=float) * dt, T)
    probe_times[-1] = T
    snap_idx = sorted(set(
        [j for j in range(probe_times.size) if probe_times[j] <= dense_until + 1e-12]
        + list(range(0, probe_times.size, snapshot_stride))
        + [probe_times.size - 1]
    ))
    snapshot_times = probe_times[snap_idx]
    n_snap_max = len(snap_idx)

    fine_integrals = []
    coarse_integrals = []
    taus = []
    tau_hits = []
    terminal_masses = []
    traj = {
        key: np.full((n_paths, n_snap_max), np.nan)
        for key in (
            "lambda_cut", "lambda_max", "lambda_min", "W_cut", "perimeter",
            "profile_bound_rich", "profile_bound_halfline", "excess_rich",
            "excess_halfline", "Q", "S_high", "p",
        )
    }
    joint_correlations = []
    big_scale_fraction = []
    mass_engine_gap = 0.0
    bracket_violation = 0.0
    decomposition_gap = 0.0
    reference_gap = 0.0

    for path_index, child in enumerate(path_children):
        trajectory = filtering_trajectory(n, T, dt, np.random.default_rng(child))
        fine_masses = np.array(
            [cut_mass(marginals(c, float(t)), radius)
             for t, c in zip(trajectory.times, trajectory.tilts)]
        )
        tau, tau_hit = _balanced_exit(trajectory.times, fine_masses)
        taus.append(tau)
        tau_hits.append(tau_hit)
        terminal_masses.append(float(fine_masses[-1]))

        snap_times = snapshot_times
        keep = int(np.searchsorted(snap_times, tau, side="left")) + 1
        keep = min(max(keep + 1, 2), snap_times.size)

        values = np.zeros((keep, len(channels)))
        for j in range(keep):
            t = float(snap_times[j])
            c = trajectory.tilts[snap_idx[j]]
            state = screened_state(
                c, t, radius, block=None,
                high_threshold=high_threshold, block_size=block_size,
            )
            values[j] = _state_vector(state, kappas)
            if j < n_snap_max:
                traj["lambda_cut"][path_index, j] = state.lambda_cut
                traj["lambda_max"][path_index, j] = state.lambda_max
                traj["lambda_min"][path_index, j] = state.lambda_min
                traj["W_cut"][path_index, j] = state.W_cut
                traj["perimeter"][path_index, j] = state.surrogate.perimeter
                traj["profile_bound_rich"][path_index, j] = state.surrogate.rich_bound
                traj["profile_bound_halfline"][path_index, j] = state.surrogate.halfline_bound
                traj["excess_rich"][path_index, j] = state.surrogate.excess_rich
                traj["excess_halfline"][path_index, j] = state.surrogate.excess_halfline
                traj["Q"][path_index, j] = state.Q
                traj["S_high"][path_index, j] = state.S_high
                traj["p"][path_index, j] = state.p

            mass_engine_gap = max(mass_engine_gap, abs(state.p - fine_masses[snap_idx[j]]))
            bracket_violation = max(
                bracket_violation,
                max(state.lambda_min - state.lambda_cut, state.lambda_cut - state.lambda_max, 0.0),
            )
            if path_index == 0 and j == 0:
                reference = observe_tail_union(c, t, radius, high_threshold=high_threshold)
                reference_gap = max(
                    reference_gap,
                    abs(reference.S - state.S) / max(abs(reference.S), 1.0),
                    abs(reference.S_high - state.S_high) / max(abs(reference.S_high), 1.0),
                    abs(reference.r - state.r) / max(abs(reference.r), 1.0),
                    abs(reference.D - state.D) / max(abs(reference.D), 1.0),
                    abs(reference.p - state.p),
                )

        fine_integrals.append(_integrate_snapshots(snap_times[:keep], values, intervals, tau))
        # The coarse partner must span exactly the same time range, otherwise the last
        # interval measures a truncation artefact instead of a quadrature error.
        coarse_positions = list(range(0, keep, 2))
        if coarse_positions[-1] != keep - 1:
            coarse_positions.append(keep - 1)
        if len(coarse_positions) >= 2:
            coarse_integrals.append(_integrate_snapshots(
                snap_times[coarse_positions], values[coarse_positions], intervals, tau,
            ))
        else:
            coarse_integrals.append(fine_integrals[-1])

        active = np.isfinite(traj["lambda_cut"][path_index]) & (
            snapshot_times <= tau + 1.0e-12
        )
        lam = traj["lambda_cut"][path_index][active]
        exc = traj["excess_rich"][path_index][active]
        if lam.size >= 3:
            joint_correlations.append(
                _phi_correlation(
                    (lam > np.median(lam)).astype(float),
                    (exc > np.median(exc)).astype(float),
                )
            )
        else:
            joint_correlations.append(float("nan"))
        total_supply = fine_integrals[-1][-1, channels.index("supply")]
        big_supply = fine_integrals[-1][-1, channels.index("supply_big_scale")]
        big_scale_fraction.append(
            float(big_supply / total_supply) if total_supply > 0.0 else float("nan")
        )

    fine = np.asarray(fine_integrals)
    coarse = np.asarray(coarse_integrals)

    # --- gates -------------------------------------------------------------------------
    initial_mar = marginals(np.zeros(n), 0.0)
    balance_error = abs(cut_mass(initial_mar, radius) - 0.5)
    gates = [
        _gate("initial_balance", balance_error < 2e-11, balance_error, 2e-11,
              "vectorized log-tail balanced mass at t=0"),
        _gate("mass_vectorized_vs_scalar_engine", mass_engine_gap <= 1e-11,
              mass_engine_gap, 1e-11,
              "new log-tail p_t versus the pre-existing scalar truncation engine"),
        _gate("lambda_cut_bracket", bracket_violation <= 1e-12, bracket_violation, 1e-12,
              "lambda_min(A) <= lambda_cut <= lambda_max(A), probe eq. (5)"),
        _gate("two_colour_vs_reference_engine", reference_gap <= 1e-12, reference_gap, 1e-12,
              "S,S_high,r,D,p reproduced from observe_tail_union at the first snapshot"),
    ]

    # exact dense reference for the diagonal-plus-rank-one decomposition (small replica)
    small_n = 8
    small_radius = balanced_tail_radius(small_n)
    small_rng = np.random.default_rng(20260830)
    for t_probe in (0.0, 0.5 * T, T):
        c_probe = small_rng.normal(scale=0.7, size=small_n) if t_probe > 0 else np.zeros(small_n)
        state = screened_state(c_probe, float(t_probe), small_radius)
        dense = dense_cut_scale(
            state.A, dense_cut_tensor(state.k_diagonal, state.delta, state.p)
        )
        decomposition_gap = max(
            decomposition_gap,
            abs(state.lambda_cut - dense) / max(abs(dense), 1.0),
        )
    gates.append(_gate(
        "lambda_cut_decomposition_vs_dense", decomposition_gap <= 1e-12,
        decomposition_gap, 1e-12,
        "O(n) diagonal/cross/rank-one split versus the dense n=8 double sum",
    ))

    # Minkowski oracle for the weighted perimeter
    h = 1.0e-5 * max(radius, 1.0)
    minkowski_worst = 0.0
    for t_probe, c_probe in ((0.0, np.zeros(n)), (float(T), trajectory.tilts[-1])):
        exact = screened_state(c_probe, t_probe, radius).surrogate.perimeter
        estimate = minkowski_perimeter_estimate(c_probe, t_probe, radius, h)
        minkowski_worst = max(minkowski_worst, abs(exact - estimate) / max(abs(exact), 1e-12))
    gates.append(_gate(
        "perimeter_vs_minkowski_finite_difference", minkowski_worst <= 5e-8,
        minkowski_worst, 5e-8,
        f"closed-form P_t versus central difference of mu_t(F_a) with h={h:.3g}",
    ))

    masses = np.asarray(terminal_masses)
    martingale_error = abs(masses.mean() - 0.5)
    martingale_se = float(masses.std(ddof=1) / np.sqrt(masses.size))
    martingale_tol = 5.0 * martingale_se + 0.01
    gates.append(_gate(
        "mass_martingale", martingale_error <= martingale_tol, martingale_error, martingale_tol,
        f"E p_T={masses.mean():.6g}, stderr={martingale_se:.3g}, target=0.5",
    ))

    lengths = intervals[:, 1] - intervals[:, 0]
    worst_drift = 0.0
    drift_detail = {}
    for index, name in enumerate(channels):
        paired = fine[:, :, index] - coarse[:, :, index]
        paired_mean, paired_se = _mean_se(paired)
        scale = np.maximum(
            np.abs(_mean_se(fine[:, :, index])[0]), np.abs(_mean_se(coarse[:, :, index])[0])
        )
        allowance = 0.15 * np.maximum(scale, lengths * 1e-6) + 3.0 * paired_se
        active = scale > lengths * 1e-9
        normalized = np.zeros_like(scale)
        normalized[active] = np.abs(paired_mean[active]) / np.maximum(allowance[active], 1e-15)
        where = int(np.argmax(normalized)) if normalized.size else 0
        worst = float(normalized[where]) if normalized.size else 0.0
        worst_drift = max(worst_drift, worst)
        drift_detail[name] = {
            "worst_normalized_drift": worst,
            "worst_interval": _interval_label(intervals[where]),
            "paired_mean_drift": float(paired_mean[where]),
        }
    gates.append(_gate(
        "snapshot_stride_refinement", worst_drift <= 1.0, worst_drift, 1.0,
        f"snapshot spacing {dt_snapshot:g} versus {2 * dt_snapshot:g} on every channel",
    ))

    configuration = {
        "kind": "screen-configuration",
        "model": _MODEL,
        "target": TARGET,
        "n": int(n),
        "radius": float(radius),
        "T": float(T),
        "dt_path": float(dt),
        "snapshot_spacing_outside_initial_layer": float(dt_snapshot),
        "snapshot_spacing_inside_initial_layer": float(dt),
        "snapshot_dense_until": float(dense_until),
        "snapshot_count": int(n_snap_max),
        "snapshot_stride": int(snapshot_stride),
        "n_paths": int(n_paths),
        "kappas": [float(k) for k in kappas],
        "interval_count": int(intervals.shape[0]),
        "tau_hit_fraction": float(np.mean(tau_hits)),
        "mean_tau_wedge_T": float(np.mean(taus)),
        "final_mass_mean": float(masses.mean()),
        "final_mass_stderr": martingale_se,
        "gates": gates,
        "gates_passed": all(g["passed"] for g in gates),
        "snapshot_stride_worst_drift_by_channel": drift_detail,
        "diagnostic_only": True,
        "proof_status": "no-proof/no-universal-conclusion",
        "surrogate_limitation": (
            "ehat <= e: every excess and supply reported is a lower bound for the true one"
        ),
    }

    trajectory_record = {
        "kind": "screen-trajectory",
        "model": _MODEL,
        "target": TARGET,
        "n": int(n),
        "snapshot_times": [float(v) for v in snapshot_times],
        "diagnostic_only": True,
    }
    for key, array in traj.items():
        with np.errstate(invalid="ignore"):
            mean = np.nanmean(array, axis=0)
            count = np.sum(np.isfinite(array), axis=0)
        trajectory_record[f"mean_{key}"] = [
            float(v) if np.isfinite(v) else None for v in mean
        ]
        trajectory_record[f"count_{key}"] = [int(v) for v in count]

    return {
        "configuration": configuration,
        "trajectory": trajectory_record,
        "intervals": intervals,
        "channels": channels,
        "fine": fine,
        "taus": np.asarray(taus),
        "joint_correlations": np.asarray(joint_correlations, dtype=float),
        "big_scale_fraction": np.asarray(big_scale_fraction, dtype=float),
        "gates_passed": configuration["gates_passed"],
    }


def _interval_label(interval: np.ndarray) -> str:
    return f"[{interval[0]:.8g},{interval[1]:.8g}]"


def _scan_records(result: dict, kappas: tuple[float, ...]) -> tuple[list[dict], dict]:
    """Select adverse windows on the discovery half; evaluate theta on the held-out half."""

    intervals = result["intervals"]
    channels = result["channels"]
    fine = result["fine"]
    lengths = intervals[:, 1] - intervals[:, 0]
    split = fine.shape[0] // 2
    discovery = fine[:split]
    heldout = fine[split:]
    n = result["configuration"]["n"]

    idx_Q = channels.index("Q")
    idx_supply = channels.index("supply")
    idx_supply_hl = channels.index("supply_halfline")
    idx_SH = channels.index("S_high")

    disc_SH = discovery[:, :, idx_SH].mean(axis=0)
    disc_supply = discovery[:, :, idx_supply].mean(axis=0)

    records: list[dict] = []
    selected: dict[str, dict] = {}
    for width in np.unique(np.round(lengths, 12)):
        mask = np.isclose(lengths, width, atol=1e-12, rtol=0.0)
        idxs = np.flatnonzero(mask)
        pulse = int(idxs[np.argmax(disc_SH[idxs] / width)])
        supply_window = int(idxs[np.argmax(disc_supply[idxs] / width)])
        entry = {
            "kind": "screen-window",
            "model": _MODEL,
            "target": TARGET,
            "n": int(n),
            "width": float(width),
            "interval_selection": "first-half discovery; second-half heldout evaluation",
            "discovery_paths": int(split),
            "heldout_paths": int(fine.shape[0] - split),
            "diagnostic_only": True,
        }
        for label, index in (("S_H_pulse", pulse), ("supply_peak", supply_window)):
            mean_Q = float(heldout[:, index, idx_Q].mean())
            se_Q = float(heldout[:, index, idx_Q].std(ddof=1) / np.sqrt(heldout.shape[0]))
            mean_supply = float(heldout[:, index, idx_supply].mean())
            se_supply = float(
                heldout[:, index, idx_supply].std(ddof=1) / np.sqrt(heldout.shape[0])
            )
            block = {
                "selected_interval": _interval_label(intervals[index]),
                "heldout_Q_integral": mean_Q,
                "heldout_Q_integral_stderr": se_Q,
                "heldout_plain_supply_integral": mean_supply,
                "heldout_plain_supply_integral_stderr": se_supply,
                "heldout_plain_supply_integral_halfline_family": float(
                    heldout[:, index, idx_supply_hl].mean()
                ),
                "heldout_S_high_integral": float(heldout[:, index, idx_SH].mean()),
            }
            for kappa in kappas:
                aligned = float(
                    heldout[:, index, channels.index(f"aligned_supply@{kappa:.3g}")].mean()
                )
                aligned_se = float(
                    heldout[:, index, channels.index(f"aligned_supply@{kappa:.3g}")]
                    .std(ddof=1) / np.sqrt(heldout.shape[0])
                )
                complement = float(
                    heldout[:, index, channels.index(f"complement_Q@{kappa:.3g}")].mean()
                )
                block[f"kappa@{kappa:.3g}"] = {
                    "heldout_aligned_supply_integral": aligned,
                    "heldout_aligned_supply_integral_stderr": aligned_se,
                    "heldout_complement_source_integral": complement,
                    "heldout_theta_hat": (
                        float(complement / mean_Q) if mean_Q > 0.0 else None
                    ),
                }
            entry[label] = block
            selected.setdefault(label, {})[f"{width:.8g}"] = block
        records.append(entry)
    return records, selected


# --------------------------------------------------------------------------------------
# spectator cylinder control
# --------------------------------------------------------------------------------------


def _spectator_records(
    seed: int,
    *,
    spectator_ns: tuple[int, ...],
    n0: int,
    T: float,
    dt: float,
    snapshot_stride: int,
    n_paths: int,
    block_size: int,
) -> tuple[list[dict], list[dict]]:
    """Cylinder cut ``E_0 x R^{n-n0}``: direct-sum invariance and supply n-independence."""

    radius = balanced_tail_radius(n0)
    dt_snapshot = dt * snapshot_stride
    n_steps = int(np.ceil(T / dt - 1e-14))
    times = np.minimum(np.arange(n_steps + 1, dtype=float) * dt, T)
    times[-1] = T
    increments = np.diff(times)
    snap_idx = list(range(0, times.size, snapshot_stride))
    if snap_idx[-1] != times.size - 1:
        snap_idx.append(times.size - 1)

    base_children = np.random.SeedSequence(int(seed) + 991).spawn(n_paths)
    spectator_root = np.random.SeedSequence(int(seed) + 992)

    invariance_worst = 0.0
    pathwise_supply_worst = 0.0
    by_n: dict[int, dict[str, list]] = {}

    base_paths = []
    for child in base_children:
        rng = np.random.default_rng(child)
        signal = rng.laplace(loc=0.0, scale=1.0 / np.sqrt(2.0), size=n0)
        dB = rng.standard_normal((n_steps, n0)) * np.sqrt(increments)[:, None]
        brownian = np.vstack([np.zeros((1, n0)), np.cumsum(dB, axis=0)])
        base_paths.append(times[:, None] * signal[None, :] + brownian)

    for n in spectator_ns:
        spectator_children = spectator_root.spawn(n_paths)
        supply_block = []
        supply_all = []
        lambda_cut_full = []
        lambda_cut_base = []
        for path_index, (base, child) in enumerate(zip(base_paths, spectator_children)):
            rng = np.random.default_rng(child)
            extra = int(n) - n0
            signal = rng.laplace(loc=0.0, scale=1.0 / np.sqrt(2.0), size=extra)
            dB = rng.standard_normal((n_steps, extra)) * np.sqrt(increments)[:, None]
            brownian = np.vstack([np.zeros((1, extra)), np.cumsum(dB, axis=0)])
            spectator = times[:, None] * signal[None, :] + brownian
            block_supply = []
            all_supply = []
            for j in snap_idx:
                t = float(times[j])
                c_full = np.concatenate([base[j], spectator[j]])
                full = screened_state(
                    c_full, t, radius, block=n0, block_size=block_size,
                )
                base_only = screened_state(base[j], t, radius, block=None, block_size=block_size)
                invariance_worst = max(
                    invariance_worst, abs(full.lambda_cut - base_only.lambda_cut)
                )
                lambda_cut_full.append(full.lambda_cut)
                lambda_cut_base.append(base_only.lambda_cut)
                block_supply.append(full.surrogate.excess_rich_block * full.W_cut)
                all_supply.append(full.surrogate.excess_rich * full.W_cut)
            supply_block.append(float(np.trapezoid(block_supply, times[snap_idx])))
            supply_all.append(float(np.trapezoid(all_supply, times[snap_idx])))
        by_n[int(n)] = {
            "supply_block_family": supply_block,
            "supply_all_coordinate_family": supply_all,
            "mean_lambda_cut": float(np.mean(lambda_cut_full)),
            "max_lambda_cut": float(np.max(lambda_cut_full)),
        }

    reference = np.asarray(by_n[int(spectator_ns[0])]["supply_block_family"])
    reference_all = np.asarray(by_n[int(spectator_ns[0])]["supply_all_coordinate_family"])
    paired_all: dict[str, dict] = {}
    for n in spectator_ns[1:]:
        other = np.asarray(by_n[int(n)]["supply_block_family"])
        pathwise_supply_worst = max(
            pathwise_supply_worst, float(np.max(np.abs(other - reference)))
        )
        # The base-block tilt path is identical across n by construction, so the
        # all-coordinate competitor family can be compared path by path.
        difference = np.asarray(by_n[int(n)]["supply_all_coordinate_family"]) - reference_all
        paired_all[f"{spectator_ns[0]}->{int(n)}"] = {
            "paired_mean_difference": float(difference.mean()),
            "paired_stderr": float(difference.std(ddof=1) / np.sqrt(difference.size))
            if difference.size > 1 else float("nan"),
            "paired_mean_relative_difference": float(
                difference.mean() / reference_all.mean()
            ) if reference_all.mean() > 0.0 else None,
            "paths_with_increase": int(np.count_nonzero(difference > 0.0)),
            "paths": int(difference.size),
        }

    gates = [
        _gate(
            "spectator_lambda_cut_block_invariance",
            invariance_worst <= PREREGISTERED_DECISION[
                "spectator_lambda_cut_block_invariance_tol"],
            invariance_worst,
            PREREGISTERED_DECISION["spectator_lambda_cut_block_invariance_tol"],
            "lambda_cut on the full cylinder model equals lambda_cut of the base block",
        ),
        _gate(
            "spectator_pathwise_block_supply_invariance",
            pathwise_supply_worst <= PREREGISTERED_DECISION[
                "spectator_pathwise_supply_invariance_tol"],
            pathwise_supply_worst,
            PREREGISTERED_DECISION["spectator_pathwise_supply_invariance_tol"],
            "identical base-block tilt paths across n; block-restricted competitor family",
        ),
    ]
    gates.append({
        "gate": "spectator_all_coordinate_family_paired_drift",
        "status": "reported",
        "passed": None,
        "detail": (
            "not a pass/fail gate: the true excess uses an infimum over sets in the full "
            "space, so more spectator coordinates legitimately lower the profile bound and "
            "raise the excess.  Reported so the effect is not mistaken for an artifact."
        ),
        "paired_statistics": paired_all,
    })

    records = []
    for n, payload in by_n.items():
        block = np.asarray(payload["supply_block_family"])
        allc = np.asarray(payload["supply_all_coordinate_family"])
        records.append({
            "kind": "screen-spectator",
            "model": _MODEL + "/cylinder",
            "target": TARGET,
            "n": int(n),
            "n0": int(n0),
            "radius": float(radius),
            "T": float(T),
            "snapshot_spacing": float(dt_snapshot),
            "n_paths": int(n_paths),
            "mean_block_family_supply_integral": float(block.mean()),
            "block_family_supply_integral_stderr": float(
                block.std(ddof=1) / np.sqrt(block.size)
            ),
            "mean_all_coordinate_family_supply_integral": float(allc.mean()),
            "all_coordinate_family_supply_integral_stderr": float(
                allc.std(ddof=1) / np.sqrt(allc.size)
            ),
            "mean_lambda_cut": payload["mean_lambda_cut"],
            "max_lambda_cut": payload["max_lambda_cut"],
            "diagnostic_only": True,
            "note": (
                "the block-restricted competitor family is spectator-blind by construction; "
                "the all-coordinate family is not, because the true profile is an infimum "
                "over sets in the full space and more spectators supply more competitors"
            ),
        })
    return records, gates


# --------------------------------------------------------------------------------------
# entry point
# --------------------------------------------------------------------------------------


def run_records(
    seed: int = 0,
    ns=(1024, 4096),
    T: float = 0.4,
    dt: float = 0.01,
    snapshot_stride: int = 5,
    n_paths: int = 16,
    kappas=(0.01, 0.05, 0.1, 0.25, 1.0),
    widths=(0.04, 0.1, 0.2),
    dense_until: float = 0.06,
    high_threshold: float = 2.0,
    block_size: int = 512,
    spectator_ns=(256, 4096),
    spectator_n0: int = 32,
    spectator_paths: int = 8,
    spectator_stride: int = 10,
):
    """Run the screened cut-local supply battery and emit its directional records."""

    ns = tuple(int(n) for n in ns)
    kappas = tuple(float(k) for k in kappas)
    if not ns or any(n < 2 for n in ns):
        raise ValueError("ns must contain dimensions >=2")
    if n_paths < 4:
        raise ValueError("n_paths must be >=4 for the discovery/heldout split")
    if snapshot_stride < 1:
        raise ValueError("snapshot_stride must be >=1")
    if T <= 0.0 or dt <= 0.0:
        raise ValueError("T and dt must be positive")

    records: list[dict] = [{
        "kind": "screen-preregistration",
        "model": _MODEL,
        "target": TARGET,
        "decision_rule": dict(PREREGISTERED_DECISION),
        "big_scale_threshold": float(BIG_SCALE_THRESHOLD),
        "diagnostic_only": True,
    }]

    all_gates_passed = True
    per_n: dict[str, dict] = {}
    top_seeds = np.random.SeedSequence(int(seed)).spawn(len(ns))
    for n, stream in zip(ns, top_seeds):
        result = _run_configuration(
            n, stream, T=T, dt=dt, snapshot_stride=snapshot_stride, n_paths=n_paths,
            kappas=kappas, widths=tuple(widths), high_threshold=high_threshold,
            block_size=block_size, dense_until=float(dense_until),
        )
        all_gates_passed = all_gates_passed and result["gates_passed"]
        records.append(result["configuration"])
        records.append(result["trajectory"])
        windows, selected = _scan_records(result, kappas)
        records.extend(windows)

        correlation_mean, correlation_se, correlation_count = _nan_mean_se(
            result["joint_correlations"]
        )
        big_mean, big_se, big_count = _nan_mean_se(result["big_scale_fraction"])
        records.append({
            "kind": "screen-joint-occurrence",
            "model": _MODEL,
            "target": TARGET,
            "n": int(n),
            "indicator_correlation_lambda_cut_vs_excess_mean": correlation_mean,
            "indicator_correlation_stderr": correlation_se,
            "paths_with_defined_correlation": correlation_count,
            "big_scale_threshold": float(BIG_SCALE_THRESHOLD),
            "mean_supply_mass_fraction_at_large_lambda_cut": big_mean,
            "supply_mass_fraction_stderr": big_se,
            "paths_with_positive_supply": big_count,
            "diagnostic_only": True,
        })

        channels = result["channels"]
        full = result["intervals"].shape[0] - 1
        full_idx = int(np.argmax(result["intervals"][:, 1] - result["intervals"][:, 0]))
        heldout = result["fine"][result["fine"].shape[0] // 2:]
        per_n[str(n)] = {
            "selected_windows": selected,
            "full_window": _interval_label(result["intervals"][full_idx]),
            "heldout_plain_supply_integral": float(
                heldout[:, full_idx, channels.index("supply")].mean()
            ),
            "heldout_aligned_supply_integral": {
                f"{k:.3g}": float(
                    heldout[:, full_idx, channels.index(f"aligned_supply@{k:.3g}")].mean()
                )
                for k in kappas
            },
            "heldout_Q_integral": float(heldout[:, full_idx, channels.index("Q")].mean()),
            "heldout_theta_hat": {
                f"{k:.3g}": (
                    float(
                        heldout[:, full_idx, channels.index(f"complement_Q@{k:.3g}")].mean()
                        / heldout[:, full_idx, channels.index("Q")].mean()
                    )
                    if heldout[:, full_idx, channels.index("Q")].mean() > 0.0 else None
                )
                for k in kappas
            },
        }
        del full

    spectator, spectator_gates = _spectator_records(
        seed, spectator_ns=tuple(int(v) for v in spectator_ns), n0=int(spectator_n0),
        T=T, dt=dt, snapshot_stride=int(spectator_stride), n_paths=int(spectator_paths),
        block_size=block_size,
    )
    records.extend(spectator)
    all_gates_passed = all_gates_passed and all(
        g["passed"] for g in spectator_gates if g["passed"] is not None
    )

    kappa_star = float(PREREGISTERED_DECISION["screening_kappa_of_record"])
    key = f"{kappa_star:.3g}"
    verdict = _evaluate_decision(per_n, ns, kappa_star, key)

    records.append({
        "kind": "screen-summary",
        "model": _MODEL,
        "target": TARGET,
        "all_numerical_gates_passed": bool(all_gates_passed),
        "spectator_gates": spectator_gates,
        "decision_rule": dict(PREREGISTERED_DECISION),
        "per_dimension": per_n,
        "verdict": verdict,
        "diagnostic_only": True,
        "proof_status": "no-proof/no-universal-conclusion",
        "interpretation": (
            "ehat_t <= e_t, so every supply integral is a lower bound for the true one. "
            "A bounded surrogate supply is weak support for Candidate B; a growing surrogate "
            "supply, or a theta_hat approaching one, is the robust adverse direction. No "
            "outcome here changes any ledger status."
        ),
    })

    config = {
        "ns": list(ns), "T": T, "dt": dt, "snapshot_stride": int(snapshot_stride),
        "n_paths": int(n_paths), "kappas": list(kappas), "widths": list(widths),
        "dense_until": float(dense_until),
        "high_threshold": high_threshold, "block_size": int(block_size),
        "spectator_ns": list(int(v) for v in spectator_ns),
        "spectator_n0": int(spectator_n0), "spectator_paths": int(spectator_paths),
        "spectator_stride": int(spectator_stride),
        "preregistered_decision": dict(PREREGISTERED_DECISION),
        "big_scale_threshold": float(BIG_SCALE_THRESHOLD),
    }
    return RunResult(
        lift_observations(records),
        config=config,
        summary={
            "model": _MODEL,
            "screened_supply_available": True,
            "excess_is_surrogate": True,
            "surrogate_direction": "understates the true excess",
            "diagnostic_only": True,
            "proof_status": "no-proof/no-universal-conclusion",
        },
    )


def _evaluate_decision(per_n: dict, ns: tuple[int, ...], kappa_star: float, key: str) -> dict:
    """Apply the pre-registered rule to the held-out numbers; report, never conclude."""

    thetas = []
    for n in ns:
        entry = per_n[str(n)]
        values = [entry["heldout_theta_hat"].get(key)]
        for label in ("S_H_pulse", "supply_peak"):
            for block in entry["selected_windows"].get(label, {}).values():
                values.append(block[f"kappa@{kappa_star:.3g}"]["heldout_theta_hat"])
        finite = [v for v in values if v is not None and np.isfinite(v)]
        thetas.append(max(finite) if finite else None)

    supplies = [
        per_n[str(n)]["heldout_aligned_supply_integral"].get(key) for n in ns
    ]
    growth = None
    if len(supplies) >= 2 and supplies[0] and supplies[0] > 0.0:
        growth = float(supplies[-1] / supplies[0])
    dimension_ratio = float(ns[-1]) / float(ns[0])

    support = (
        all(v is not None and v <= PREREGISTERED_DECISION[
            "support_theta_hat_max_on_every_selected_interval"] for v in thetas)
        and growth is not None
        and growth < PREREGISTERED_DECISION["support_aligned_supply_growth_factor_max"]
    )
    theta_increasing = (
        len(thetas) >= 2 and all(v is not None for v in thetas)
        and thetas[-1] > thetas[0]
    )
    against_theta = theta_increasing and thetas[-1] > PREREGISTERED_DECISION[
        "against_theta_hat_min_on_pulse_window_at_top_n"]
    against_supply = (
        growth is not None
        and growth >= PREREGISTERED_DECISION[
            "against_linear_growth_min_fraction_of_dimension_ratio"] * dimension_ratio
    )
    if against_theta or against_supply:
        outcome = "directional-against"
    elif support:
        outcome = "directional-support"
    else:
        outcome = "inconclusive"
    return {
        "kappa": float(kappa_star),
        "worst_theta_hat_by_n": thetas,
        "aligned_supply_by_n": supplies,
        "aligned_supply_growth_factor": growth,
        "dimension_ratio": dimension_ratio,
        "support_criterion_met": bool(support),
        "against_theta_criterion_met": bool(against_theta),
        "against_supply_criterion_met": bool(against_supply),
        "outcome": outcome,
        "status": "directional research evidence only; no claim or proof status changes",
    }


def selftest(rng):
    result = run_records(
        seed=31337, ns=(8,), T=0.1, dt=0.01, snapshot_stride=2, n_paths=4,
        kappas=(0.05,), widths=(0.02,), dense_until=0.02,
        spectator_ns=(12, 20), spectator_n0=4, spectator_paths=2, spectator_stride=5,
    )
    config = next(r for r in result.records if r["kind"] == "screen-configuration")
    summary = result.records[-1]
    named = {g["gate"]: g["passed"] for g in config["gates"]}
    return [
        ("kls-screen lambda_cut decomposition == dense", named["lambda_cut_decomposition_vs_dense"]),
        ("kls-screen perimeter == Minkowski difference",
         named["perimeter_vs_minkowski_finite_difference"]),
        ("kls-screen two-colour == reference engine", named["two_colour_vs_reference_engine"]),
        ("kls-screen lambda_cut bracket", named["lambda_cut_bracket"]),
        ("kls-screen spectator gates",
         all(g["passed"] for g in summary["spectator_gates"] if g["passed"] is not None)),
    ]
