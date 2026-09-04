"""Product tail-union stress test for KLS ``q:alignment`` (target ``kls-align``).

This target computes the *actual* model observable

    int_{I cap [0,tau]} S_t^H dt,

together with ``r`` and ``D`` for the balanced cut
``E={max_i |x_i|>=a_n}`` in an isotropic product of two-sided exponentials.  It
uses exact O(n) conditional-moment formulas and the filtering representation
``c_t=tX+B_t``.  It scans deterministic intervals past ``1/log(n)`` and reports
the sampled constant required by

    E int_I S^H <= C0 |I| + C1 E int_I r + alpha E int_I D.

Epistemic contract: every output is a refutation-seeking **product-model
diagnostic**.  Passing every numerical gate does not prove the all-product
estimate, the all-cut Carleson estimate, or KLS.
"""

from __future__ import annotations

import numpy as np

from ...contract import RunResult, lift_observations
from ...localization.alignment import (
    filtering_trajectory,
    grid_intervals,
    integrate_alignment_path,
)
from ...localization.tail_union import (
    balanced_tail_radius,
    observe_tail_union,
    tilted_laplace_symmetric_truncation,
)
from ...localization.tilt1d import LAPLACE, tilted


TARGET = "q:alignment"
_MODEL = "isotropic-laplace-product/tail-union"


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


def _dynamic_moment_gate(trajectory, radius: float, *, tol: float = 2.0e-7) -> dict:
    """Cross-check closed forms against independent high-order quadrature along a path."""

    time_indices = sorted(set([0, trajectory.times.size // 2, trajectory.times.size - 1]))
    worst = 0.0
    checks = 0
    for ti in time_indices:
        c = trajectory.tilts[ti]
        coord_indices = sorted(set([0, int(np.argmax(np.abs(c))), c.size // 2]))
        for ci in coord_indices:
            exact = tilted_laplace_symmetric_truncation(float(c[ci]), float(trajectory.times[ti]), radius)
            quad = tilted(
                LAPLACE, float(c[ci]), float(trajectory.times[ti]),
                order=900, half_width=36.0, passes=3,
                extra_breaks=(-radius, radius),
            )
            mask = np.abs(quad.nodes) < radius
            z = float(quad.weights[mask].sum())
            u = float(np.dot(quad.weights[mask], quad.nodes[mask]) / z)
            second = float(np.dot(quad.weights[mask], quad.nodes[mask] ** 2) / z)
            w = max(second - u * u, 0.0)
            errors = [
                abs(exact.probability - z),
                abs(exact.mean - u) / max(1.0, abs(exact.mean)),
                abs(exact.variance - w) / max(1.0, abs(exact.variance)),
                abs(exact.full_mean - quad.mean) / max(1.0, abs(exact.full_mean)),
                abs(exact.full_variance - quad.var) / max(1.0, abs(exact.full_variance)),
            ]
            worst = max(worst, *errors)
            checks += 1
    return _gate(
        "dynamic_closed_form_vs_quadrature", worst <= tol, worst, tol,
        f"max absolute/scale-normalized moment discrepancy over {checks} tilted marginals",
    )


def _interval_labels(intervals: np.ndarray) -> list[str]:
    return [f"[{a:.8g},{b:.8g}]" for a, b in intervals]


def _paired_refinement_gate(
    fine: dict[str, np.ndarray],
    coarse: dict[str, np.ndarray],
    intervals: np.ndarray,
    fine_tau: np.ndarray,
    coarse_tau: np.ndarray,
    fine_hits: np.ndarray,
    coarse_hits: np.ndarray,
    *,
    dt: float,
    alphas: tuple[float, ...],
    C1: float,
) -> dict:
    """Gate every reported integral combination and the grid-detected stopping time."""

    lengths = intervals[:, 1] - intervals[:, 0]
    labels = _interval_labels(intervals)
    components: dict[str, dict] = {}
    worst = 0.0

    def add_integral_component(name: str, fine_values: np.ndarray, coarse_values: np.ndarray,
                               scale: np.ndarray) -> None:
        nonlocal worst
        paired = fine_values - coarse_values
        paired_mean, paired_se = _mean_se(paired)
        allowance = 0.12 * np.maximum(scale, lengths * 1e-6) + 3.0 * paired_se
        active = scale > lengths * 1e-9
        normalized = np.zeros_like(scale)
        normalized[active] = np.abs(paired_mean[active]) / np.maximum(allowance[active], 1e-15)
        idx = int(np.argmax(normalized))
        value = float(normalized[idx])
        worst = max(worst, value)
        components[name] = {
            "worst_normalized_drift": value,
            "worst_interval": labels[idx],
            "paired_mean_drift": float(paired_mean[idx]),
            "paired_mean_drift_stderr": float(paired_se[idx]),
            "allowance": float(allowance[idx]),
        }

    mean_SH, _ = _mean_se(fine["S_high"])
    coarse_mean_SH, _ = _mean_se(coarse["S_high"])
    mean_r, _ = _mean_se(fine["r"])
    coarse_mean_r, _ = _mean_se(coarse["r"])
    mean_D, _ = _mean_se(fine["D"])
    coarse_mean_D, _ = _mean_se(coarse["D"])
    symmetric_SH = np.maximum(np.abs(mean_SH), np.abs(coarse_mean_SH))
    symmetric_r = np.maximum(np.abs(mean_r), np.abs(coarse_mean_r))
    symmetric_D = np.maximum(np.abs(mean_D), np.abs(coarse_mean_D))
    add_integral_component("S_high", fine["S_high"], coarse["S_high"], symmetric_SH)
    add_integral_component("r", fine["r"], coarse["r"], symmetric_r)
    add_integral_component("D", fine["D"], coarse["D"], symmetric_D)
    for alpha in alphas:
        fine_margin = fine["S_high"] - C1 * fine["r"] - alpha * fine["D"]
        coarse_margin = coarse["S_high"] - C1 * coarse["r"] - alpha * coarse["D"]
        # Scale by the non-cancelling component sum, not the possibly tiny margin.
        scale = symmetric_SH + C1 * symmetric_r + alpha * symmetric_D
        add_integral_component(
            f"S_high-C1*r-{alpha:.3g}*D", fine_margin, coarse_margin, scale,
        )

    tau_abs = np.abs(fine_tau - coarse_tau)
    tau_mean_abs = float(tau_abs.mean())
    tau_se = float(tau_abs.std(ddof=1) / np.sqrt(tau_abs.size))
    # Linear interpolation does not detect an exit and re-entry occurring entirely
    # between nodes.  This is an empirical nested-grid tolerance, not a bridge bound.
    tau_allowance = 2.0 * dt + 3.0 * tau_se
    tau_normalized = tau_mean_abs / max(tau_allowance, 1e-15)
    hit_disagreement = np.asarray(fine_hits, dtype=bool) != np.asarray(coarse_hits, dtype=bool)
    hit_fraction = float(hit_disagreement.mean())
    hit_se = float(np.sqrt(max(hit_fraction * (1.0 - hit_fraction), 0.0) / hit_disagreement.size))
    hit_allowance = 0.05 + 3.0 * hit_se
    hit_normalized = hit_fraction / max(hit_allowance, 1e-15)
    stopping_normalized = max(tau_normalized, hit_normalized)
    worst = max(worst, stopping_normalized)
    components["tau_and_stop"] = {
        "worst_normalized_drift": float(stopping_normalized),
        "mean_absolute_tau_drift": tau_mean_abs,
        "tau_drift_stderr": tau_se,
        "tau_drift_allowance": tau_allowance,
        "stop_hit_disagreement_fraction": hit_fraction,
        "stop_hit_disagreement_allowance": hit_allowance,
        "limitation": (
            "exit is detected only at nested grid nodes with a linearly interpolated crossing; "
            "an exit-and-reentry between fine nodes is not controlled"
        ),
    }

    gate = _gate(
        "paired_dt_refinement", worst <= 1.0, worst, 1.0,
        f"dt={dt:g} versus dt/2={dt/2:g}; S_high, r, D, all alpha margins, and stopping",
    )
    gate["components"] = components
    gate["stopping_control"] = "empirical nested-dt only; no Brownian-bridge crossing correction"
    return gate


def _scan_records(
    n: int,
    intervals: np.ndarray,
    fine: dict[str, np.ndarray],
    *,
    alphas: tuple[float, ...],
    C1: float,
) -> tuple[list[dict], dict[str, dict]]:
    """Select adverse intervals on half the paths and estimate them on the other half."""

    lengths = intervals[:, 1] - intervals[:, 0]
    split = fine["S_high"].shape[0] // 2
    discovery = {key: value[:split] for key, value in fine.items()}
    heldout = {key: value[split:] for key, value in fine.items()}
    disc_SH, _ = _mean_se(discovery["S_high"])
    disc_r, _ = _mean_se(discovery["r"])
    disc_D, _ = _mean_se(discovery["D"])
    mean_SH, se_SH = _mean_se(heldout["S_high"])
    mean_S, se_S = _mean_se(heldout["S"])
    mean_r, se_r = _mean_se(heldout["r"])
    mean_D, se_D = _mean_se(heldout["D"])
    mean_high_count, se_high_count = _mean_se(heldout["high_count"])
    labels = _interval_labels(intervals)
    records: list[dict] = []

    widths = np.unique(np.round(lengths, 12))
    for width in widths:
        mask = np.isclose(lengths, width, atol=1.0e-12, rtol=0.0)
        idxs = np.flatnonzero(mask)
        discovery_source_density = disc_SH[idxs] / width
        source_idx = int(idxs[np.argmax(discovery_source_density)])
        rec = {
            "kind": "alignment-window-scan",
            "model": _MODEL,
            "target": TARGET,
            "n": int(n),
            "width": float(width),
            "interval_selection": "first-half discovery; second-half heldout evaluation",
            "discovery_paths": int(split),
            "heldout_paths": int(fine["S_high"].shape[0] - split),
            "selected_source_interval": labels[source_idx],
            "discovery_source_density": float(disc_SH[source_idx] / width),
            "heldout_source_density": float(mean_SH[source_idx] / width),
            "heldout_source_integral": float(mean_SH[source_idx]),
            "heldout_source_stderr": float(se_SH[source_idx]),
            "heldout_total_source_integral": float(mean_S[source_idx]),
            "heldout_total_source_stderr": float(se_S[source_idx]),
            "heldout_r_integral": float(mean_r[source_idx]),
            "heldout_r_stderr": float(se_r[source_idx]),
            "heldout_D_integral": float(mean_D[source_idx]),
            "heldout_D_stderr": float(se_D[source_idx]),
            "heldout_high_count_time_integral": float(mean_high_count[source_idx]),
            "heldout_high_count_time_integral_stderr": float(se_high_count[source_idx]),
            "heldout_mean_simultaneous_high_coordinates": float(
                mean_high_count[source_idx] / width
            ),
            "heldout_source_to_full_budget_ratio": float(
                mean_SH[source_idx] / max(width + C1 * mean_r[source_idx] + mean_D[source_idx], 1e-15)
            ),
            "diagnostic_only": True,
        }
        alpha_margins = {}
        for alpha in alphas:
            discovery_required = (disc_SH - C1 * disc_r - alpha * disc_D) / lengths
            local = int(idxs[np.argmax(discovery_required[idxs])])
            heldout_margin_samples = (
                heldout["S_high"][:, local]
                - C1 * heldout["r"][:, local]
                - alpha * heldout["D"][:, local]
            ) / lengths[local]
            heldout_margin = float(heldout_margin_samples.mean())
            heldout_margin_se = float(
                heldout_margin_samples.std(ddof=1) / np.sqrt(heldout_margin_samples.size)
            )
            discovery_positive_ratio = np.maximum(disc_SH - alpha * disc_D, 0.0) / (
                lengths + disc_r
            )
            ratio_local = int(idxs[np.argmax(discovery_positive_ratio[idxs])])
            heldout_positive_ratio = float(
                max(mean_SH[ratio_local] - alpha * mean_D[ratio_local], 0.0)
                / max(lengths[ratio_local] + mean_r[ratio_local], 1e-15)
            )
            # C0=1 normalized slack: positive means the sampled inequality is violated
            # for this *candidate* triple (C0,C1,alpha), not for q:alignment itself.
            candidate_excess = (
                mean_SH[local] - lengths[local] - C1 * mean_r[local] - alpha * mean_D[local]
            )
            candidate_scale = lengths[local] + C1 * mean_r[local] + alpha * mean_D[local]
            alpha_margins[f"{alpha:.3g}"] = {
                "selected_interval": labels[local],
                "discovery_raw_margin_density": float(discovery_required[local]),
                "heldout_raw_margin_density": heldout_margin,
                "heldout_raw_margin_density_stderr": heldout_margin_se,
                "heldout_required_C0": float(max(heldout_margin, 0.0)),
                "ratio_selected_interval": labels[ratio_local],
                "discovery_positive_source_minus_alpha_D_over_length_plus_r": float(
                    discovery_positive_ratio[ratio_local]
                ),
                "heldout_positive_source_minus_alpha_D_over_length_plus_r": heldout_positive_ratio,
                "heldout_C0_1_relative_excess": float(
                    candidate_excess / max(candidate_scale, 1e-15)
                ),
            }
        rec["alpha_margins_C1_fixed"] = alpha_margins
        rec["C1"] = float(C1)
        records.append(rec)

    # One global discovery selection per alpha.  These held-out values feed the
    # cross-dimension summary, avoiding a second maximum on the evaluation half.
    global_margins: dict[str, dict] = {}
    for alpha in alphas:
        discovery_required = (disc_SH - C1 * disc_r - alpha * disc_D) / lengths
        idx = int(np.argmax(discovery_required))
        samples = (
            heldout["S_high"][:, idx]
            - C1 * heldout["r"][:, idx]
            - alpha * heldout["D"][:, idx]
        ) / lengths[idx]
        mean = float(samples.mean())
        se = float(samples.std(ddof=1) / np.sqrt(samples.size))
        global_margins[f"{alpha:.3g}"] = {
            "selected_interval": labels[idx],
            "discovery_raw_margin_density": float(discovery_required[idx]),
            "heldout_raw_margin_density": mean,
            "heldout_raw_margin_density_stderr": se,
            "heldout_required_C0": float(max(mean, 0.0)),
        }
    return records, global_margins


def run_records(
    seed: int = 0,
    ns=(16, 32, 64),
    T: float = 0.5,
    dt: float = 0.01,
    n_paths: int = 24,
    widths=(0.02, 0.05, 0.1, 0.2),
    alphas=(0.0, 0.5, 0.75, 0.9),
    C1: float = 1.0,
    high_threshold: float = 2.0,
):
    """Run the gated adversarial interval sweep.

    Each fine path uses step ``dt/2``; its exact subsample is the paired ``dt``
    path used by the time-refinement gate.
    """

    ns = tuple(int(n) for n in ns)
    if not ns or any(n < 2 for n in ns):
        raise ValueError("ns must contain dimensions >=2")
    if n_paths < 4:
        raise ValueError("n_paths must be >=4 for discovery/heldout uncertainty diagnostics")
    if T <= 0.0 or dt <= 0.0:
        raise ValueError("T and dt must be positive")
    records: list[dict] = []
    top_seed_sequences = np.random.SeedSequence(int(seed)).spawn(len(ns))

    all_gates_passed = True
    heldout_required_by_n: dict[str, dict] = {}
    for n, n_seed in zip(ns, top_seed_sequences):
        radius = balanced_tail_radius(n)
        t_log = float(1.0 / np.log(float(n)))
        snapped_t_log = min(T, max(dt, round(t_log / dt) * dt))
        sharp_width = t_log * t_log
        snapped_sharp_width = min(T, max(dt, round(sharp_width / dt) * dt))
        requested_widths = tuple(float(w) for w in widths) + (
            snapped_t_log, snapped_sharp_width, T,
        )
        if 2.0 * snapped_t_log <= T + 1.0e-12:
            requested_widths += (2.0 * snapped_t_log,)
        if 2.0 * snapped_sharp_width <= T + 1.0e-12:
            requested_widths += (2.0 * snapped_sharp_width,)
        intervals = grid_intervals(T, dt, tuple(sorted(set(requested_widths))))

        fine_values = {k: [] for k in ("S_high", "S", "r", "D", "high_count")}
        coarse_values = {k: [] for k in ("S_high", "S", "r", "D", "high_count")}
        final_masses = []
        tau_values = []
        coarse_tau_values = []
        tau_hits = []
        coarse_tau_hits = []
        max_lambdas = []
        invariant_worst = {
            "source_decomposition": 0.0,
            "high_excess": 0.0,
            "negative_damping_gap": 0.0,
            "bl_excess": 0.0,
        }
        path_children = n_seed.spawn(n_paths)
        first_fine = None
        for child in path_children:
            fine_trajectory = filtering_trajectory(n, T, dt / 2.0, np.random.default_rng(child))
            coarse_trajectory = fine_trajectory.subsample(2)
            if first_fine is None:
                first_fine = fine_trajectory
            fine_result = integrate_alignment_path(
                fine_trajectory, radius, intervals, high_threshold=high_threshold,
            )
            coarse_result = integrate_alignment_path(
                coarse_trajectory, radius, intervals, high_threshold=high_threshold,
            )
            for key in fine_values:
                fine_values[key].append(getattr(fine_result, key))
                coarse_values[key].append(getattr(coarse_result, key))
            final_masses.append(
                observe_tail_union(
                    fine_trajectory.tilts[-1], T, radius,
                    high_threshold=high_threshold,
                ).p
            )
            tau_values.append(fine_result.tau)
            coarse_tau_values.append(coarse_result.tau)
            tau_hits.append(fine_result.tau_hit)
            coarse_tau_hits.append(coarse_result.tau_hit)
            max_lambdas.append(fine_result.max_lambda)
            invariant_worst["source_decomposition"] = max(
                invariant_worst["source_decomposition"], fine_result.max_source_decomposition_error,
            )
            invariant_worst["high_excess"] = max(
                invariant_worst["high_excess"], fine_result.max_high_excess,
            )
            invariant_worst["negative_damping_gap"] = max(
                invariant_worst["negative_damping_gap"], -fine_result.min_damping_gap,
            )
            invariant_worst["bl_excess"] = max(
                invariant_worst["bl_excess"], fine_result.max_bl_excess,
            )

        fine_arrays = {k: np.asarray(v) for k, v in fine_values.items()}
        coarse_arrays = {k: np.asarray(v) for k, v in coarse_values.items()}
        final_masses = np.asarray(final_masses)

        initial = observe_tail_union(np.zeros(n), 0.0, radius, high_threshold=high_threshold)
        balance_error = abs(initial.p - 0.5)
        balance_gate = _gate(
            "initial_balance", balance_error < 2e-11, balance_error, 2e-11,
            "closed-form tail-union mass at t=0",
        )
        dynamic_gate = _dynamic_moment_gate(first_fine, radius)

        martingale_error = abs(final_masses.mean() - 0.5)
        martingale_se = float(final_masses.std(ddof=1) / np.sqrt(n_paths))
        martingale_tol = 5.0 * martingale_se + 0.01
        martingale_gate = _gate(
            "mass_martingale", martingale_error <= martingale_tol,
            martingale_error, martingale_tol,
            f"E p_T={final_masses.mean():.6g}, stderr={martingale_se:.3g}, target=0.5",
        )

        invariant_measure = max(invariant_worst.values())
        invariant_gate = _gate(
            "pathwise_identities", invariant_measure <= 2e-8,
            invariant_measure, 2e-8,
            "max of |S-S_H-S_L|, (S_H-S)+, (r^2-D)+, and BL-cap excess",
        )

        dt_gate = _paired_refinement_gate(
            fine_arrays, coarse_arrays, intervals,
            np.asarray(tau_values), np.asarray(coarse_tau_values),
            np.asarray(tau_hits), np.asarray(coarse_tau_hits),
            dt=dt, alphas=tuple(alphas), C1=C1,
        )

        gates = [balance_gate, dynamic_gate, martingale_gate, invariant_gate, dt_gate]
        gates_pass = all(g["passed"] for g in gates)
        all_gates_passed = all_gates_passed and gates_pass
        records.append({
            "kind": "alignment-configuration",
            "model": _MODEL,
            "target": TARGET,
            "n": n,
            "radius": radius,
            "T": T,
            "dt_reported": dt / 2.0,
            "dt_refinement_pair": [dt, dt / 2.0],
            "n_paths": n_paths,
            "high_threshold": high_threshold,
            "one_over_log_n": t_log,
            "snapped_one_over_log_n": snapped_t_log,
            "one_over_log_n_squared": sharp_width,
            "snapped_one_over_log_n_squared": snapped_sharp_width,
            "interval_count": int(intervals.shape[0]),
            "discovery_paths": n_paths // 2,
            "heldout_paths": n_paths - n_paths // 2,
            "tau_hit_fraction": float(np.mean(tau_hits)),
            "mean_tau_wedge_T": float(np.mean(tau_values)),
            "max_lambda_across_paths": float(np.max(max_lambdas)),
            "final_mass_mean": float(final_masses.mean()),
            "final_mass_stderr": martingale_se,
            "gates": gates,
            "gates_passed": gates_pass,
            "diagnostic_only": True,
            "proof_status": "no-proof/no-universal-conclusion",
            "stopping_limitation": (
                "balanced exit is node-detected with linear crossing interpolation; nested dt "
                "tests this empirically but does not control exit-and-reentry between fine nodes"
            ),
        })
        scan, global_margins = _scan_records(
            n, intervals, fine_arrays, alphas=tuple(alphas), C1=C1,
        )
        records.extend(scan)
        heldout_required_by_n[str(n)] = global_margins

    records.append({
        "kind": "alignment-summary",
        "model": _MODEL,
        "target": TARGET,
        "all_numerical_gates_passed": all_gates_passed,
        "global_discovery_selected_heldout_margins_by_n": heldout_required_by_n,
        "C1": float(C1),
        "diagnostic_only": True,
        "proof_status": "no-proof/no-universal-conclusion",
        "stopping_limitation": (
            "node-only stop detection is controlled empirically by paired nested dt; "
            "there is no Brownian-bridge missed-crossing bound"
        ),
        "interpretation": (
            "Intervals are selected on half the paths and evaluated on the held-out half. "
            "A statistically resolved growing held-out C0 requirement can refute a proposed "
            "fixed constant tuple; bounded values cannot establish the all-interval/all-cut estimate."
        ),
    })

    config = {
        "ns": list(ns), "T": T, "dt": dt,
        "n_paths": n_paths, "widths": list(widths), "alphas": list(alphas),
        "C1": C1, "high_threshold": high_threshold,
    }
    return RunResult(
        lift_observations(records),
        config=config,
        summary={"model": _MODEL, "route_observable_available": True,
                 "dynamic_quadrature_available": True, "diagnostic_only": True,
                 "proof_status": "no-proof/no-universal-conclusion"},
    )


def selftest(rng):
    records = run_records(
        seed=1701, ns=(8,), T=0.12, dt=0.02, n_paths=4,
        widths=(0.04, 0.08), alphas=(0.5,),
    ).records
    config = next(r for r in records if r["kind"] == "alignment-configuration")
    return [
        ("kls-align initial balance", config["gates"][0]["passed"]),
        ("kls-align pathwise identities", config["gates"][3]["passed"]),
    ]
