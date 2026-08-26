"""KLS Part III — LOCALIZATION ENGINE DIAGNOSTICS (target id ``loc-engine``).

The SDE-free target ``kls`` gates the route-agnostic, Poincare-level facts. This target exercises
the Eldan stochastic-localization engine (``finum.localization``) on source-occupation diagnostics
``Xi_S(T) = E int_0^{T wedge tau} S dt``.  It does **not** yet compute either route observable:

* ``q:alignment`` needs the occupation restricted to inflated coordinates together with the
  absorptive ``r`` and ``D`` terms;
* ``q:taming`` needs the cut-free covariance input ``h_mu Xi_T`` on near-worst measures,
  whereas this target uses product measures and a fixed cut.

Accordingly every run reports an unavailable route assessment even when all numerical gates pass.

Epistemic status (see the numerical-validity policy in experiments/README.md): these numbers
NEVER certify. A thin-shell occupation number is eligible to be inspected only behind all passing
gates:
  * calibration — the Gaussian model oracle ``A_t = (1+t)^{-1} I`` reproduces to ~1e-12
    (a bug in the integrator/quadrature breaks this);
  * ``initial_n_bins_convergence`` — the gridded background has converged at the initial state;
  * ``initial_fft_vs_mc`` — FFT agrees with independent Monte Carlo at the initial state;
  * time-step refinement — the occupation mean is stable under ``dt -> dt/2`` within Monte-Carlo
    uncertainty.
Tilted-state quadrature convergence is not yet implemented and is recorded separately as missing.
Missing gates (the default ``heavy=False`` omits the FFT/MC and time-refinement gates) and red gates are explicit. They
always produce an unavailable assessment.

Diagnostic read off the occupation sweep:
  * proved fact (thm:budget): ``Xi_S <= k`` for a k-coordinate cut — a gross violation REFUTES
    the engine/assembly, not the conjecture;
  * the normalized budget ``Xi_S / n`` is reported only as an engine trend. It is not a
    ``q:alignment`` or ``q:taming`` conclusion.
"""
from __future__ import annotations

import numpy as np

from ...contract import RunResult
from ...localization import (
    LAPLACE,
    ProductState,
    balanced_threshold,
    block_sum,
    make_rng,
    n_bins_convergence,
    single_coord,
    spawn_rngs,
)
from ...localization.cuts import PSI_ID, PSI_SQ
from ...localization.observables import ensemble_mean, integrate_path
from ...localization.sde import localization_path
from ...localization.tilt1d import GAUSSIAN

OBSTRUCTION = "obs:rank-one-refuted"  # the budget facts this channel exercises

_COV_ORACLE_TOL = 1e-10  # absolute tol on |A_t - 1/(1+t)| (deterministic Gaussian model)
_DT_REL_TOL = 0.20       # refinement tolerance, augmented by 3 combined standard errors


# ---- gate: the Gaussian-model covariance oracle A_t = 1/(1+t) -------------------

def _gaussian_covariance_max_err(T: float = 1.0, dt: float = 0.02, n: int = 5,
                                 seed: int = 12345) -> float:
    """Max |A_t - 1/(1+t)| over a Gaussian path (deterministic; should be ~1e-12)."""
    rng = make_rng(seed)
    err = 0.0
    for st in localization_path(GAUSSIAN, n=n, T=T, dt=dt, rng=rng):
        if st.t == 0.0:
            continue
        err = max(err, float(np.max(np.abs(st.A_diag() - 1.0 / (1.0 + st.t)))))
    return err


# ---- the balanced thin-shell occupation sweep ----------------------------------

def _balanced_thinshell(n: int):
    state0 = ProductState.isotropic(LAPLACE, n)
    theta = balanced_threshold(state0, range(n), psi=PSI_SQ, side="ge", p_target=0.5)
    return state0, block_sum(range(n), theta, psi=PSI_SQ, side="ge")


def _occupation_xi_S(n: int, cut, *, T: float, dt: float, seed: int, n_paths: int,
                     n_bins: int):
    rngs = spawn_rngs(seed, n_paths)
    xi = np.array([
        integrate_path(LAPLACE, n, cut, T, dt, rg, stop_at_tau=True,
                       cm_kw={"n_bins": n_bins}).xi_S
        for rg in rngs
    ])
    return ensemble_mean(xi, f"xi_S(n={n})")


def _gate_record(name: str, passed: bool, measured, tol, detail: str, *, status: str = "run"):
    """JSON-ready gate record, including an explicit status for gates that were not run."""
    return {
        "gate": name,
        "passed": bool(passed),
        "status": status,
        "measured": measured,
        "tol": tol,
        "detail": detail,
    }


def _missing_gate(name: str, reason: str):
    return _gate_record(name, False, None, None, reason, status="not-run")


def _dt_refinement_gate(n: int, cut, *, T: float, dt: float, seed: int, n_paths: int,
                        n_bins: int, rel_tol: float = _DT_REL_TOL):
    """Compare the occupation mean at ``dt`` and ``dt/2``.

    The two ensembles use disjoint deterministic seed schedules, so the pass threshold uses the
    independent-ensemble combined standard error in addition to a relative tolerance. Returns
    ``(gate_record, fine_result)`` so the caller reports the more refined diagnostic.
    """
    coarse = _occupation_xi_S(n, cut, T=T, dt=dt, seed=seed, n_paths=n_paths, n_bins=n_bins)
    fine = _occupation_xi_S(
        n, cut, T=T, dt=dt / 2.0, seed=seed + 1_000_003,
        n_paths=n_paths, n_bins=n_bins,
    )
    diff = abs(coarse.mean - fine.mean)
    scale = max(abs(fine.mean), 1e-12)
    se_coarse = coarse.stderr if np.isfinite(coarse.stderr) else 0.0
    se_fine = fine.stderr if np.isfinite(fine.stderr) else 0.0
    combined_se = float(np.hypot(se_coarse, se_fine))
    allowance = rel_tol * scale + 3.0 * combined_se
    detail = (
        f"|mean(dt)-mean(dt/2)|={diff:.3e} <= {allowance:.3e} "
        f"(rel_tol={rel_tol:.2f}, 3se={3.0 * combined_se:.3e}); "
        f"coarse={coarse.mean:.6g}, fine={fine.mean:.6g}"
    )
    return _gate_record("dt_refinement", diff <= allowance, diff, allowance, detail), fine


def _required_gates_pass(*records: dict) -> bool:
    """True only when every required gate is present, ran, and passed."""
    return bool(records) and all(g.get("status") == "run" and g.get("passed") is True
                                 for g in records)


def _unavailable_assessment(reason: str, *, gates_passed: bool):
    return {
        "evidence": "directional",
        "outcome": "unavailable",
        "gates_passed": bool(gates_passed),
        "route_observable_available": False,
        "dynamic_quadrature_available": False,
        "reason": reason,
        "scope": "engine diagnostic only; route observables are not implemented",
    }


def run_records(seed: int = 0, ns=(2, 3, 4), T: float = 0.5, dt: float = 0.1,
                n_paths: int = 12, n_bins: int = 1 << 15, heavy: bool = False):
    records = []

    # calibration gate (shared by every n): the Gaussian covariance oracle A_t = 1/(1+t) I.
    cov_err = _gaussian_covariance_max_err()
    cal_ok = cov_err < _COV_ORACLE_TOL
    cal_gate = _gate_record(
        "gaussian_covariance",
        cal_ok,
        cov_err,
        _COV_ORACLE_TOL,
        "A_t == 1/(1+t) I (Gaussian model)",
    )
    records.append({"kind": "calibration", "instance": "cal-kls-loc-gaussian",
                    "claim": "A_t == 1/(1+t) I (Gaussian model)", "max_abs_err": cov_err,
                    "abs_tol": _COV_ORACLE_TOL, "status": "match" if cal_ok else "mismatch",
                    "gate": cal_gate})

    # rank-one budget sanity: single-coordinate cut has E int_0^inf S dt <= 1 (cor:refutation).
    rank_one = {"kind": "diagnostic", "instance": "rank-one", "obstruction": OBSTRUCTION,
                "diagnostic_only": True, "gate_calibration": cal_gate,
                "note": "single-coordinate cut: E int S dt <= 1 (cor:refutation)"}
    if cal_ok:
        cut1 = single_coord(0, 0.0, psi=PSI_ID, side="ge")
        res1 = _occupation_xi_S(8, cut1, T=4.0, dt=0.04, seed=seed + 11,
                                n_paths=n_paths, n_bins=n_bins)
        rank_one.update({"xi_S_mean": res1.mean, "xi_S_stderr": res1.stderr, "budget_k": 1,
                         "within_budget": bool(res1.mean <= 1.0 + 3 * (res1.stderr or 0.0)),
                         "assessment": _unavailable_assessment(
                             "settled-fact engine check, not a route test", gates_passed=False)})
    else:
        rank_one["assessment"] = _unavailable_assessment(
            "calibration gate failed; diagnostic not run", gates_passed=False)
    records.append(rank_one)

    # the n-sweep on the balanced thin-shell energy cut.
    sweep = []
    gate_summary = {}
    for n in ns:
        rec = {"kind": "diagnostic", "instance": f"thinshell-n{n}", "n": n,
               "diagnostic_only": True, "gate_calibration": cal_gate}

        if not cal_ok:
            bins_gate = _missing_gate("initial_n_bins_convergence",
                                      "not run because calibration failed")
            fft_gate = _missing_gate("initial_fft_vs_mc", "not run because calibration failed")
            dt_gate = _missing_gate("dt_refinement", "not run because calibration failed")
            rec.update({"gate_n_bins": bins_gate, "gate_fft_vs_mc": fft_gate,
                        "gate_dt_refinement": dt_gate,
                        "assessment": _unavailable_assessment(
                            "required calibration gate failed", gates_passed=False)})
            gate_summary[str(n)] = False
            records.append(rec)
            continue

        state0, cut = _balanced_thinshell(n)
        gate = n_bins_convergence(state0, cut,
                                  n_bins_list=(n_bins >> 2, n_bins >> 1, n_bins))
        bins_gate = gate.as_record()
        bins_gate["gate"] = "initial_n_bins_convergence"
        bins_gate["status"] = "run"
        rec["gate_n_bins"] = bins_gate

        if not gate.passed:
            fft_gate = _missing_gate("initial_fft_vs_mc", "not run because n_bins convergence failed")
            dt_gate = _missing_gate("dt_refinement", "not run because n_bins convergence failed")
            rec.update({"gate_fft_vs_mc": fft_gate, "gate_dt_refinement": dt_gate,
                        "assessment": _unavailable_assessment(
                            "required n_bins gate failed", gates_passed=False)})
            gate_summary[str(n)] = False
            records.append(rec)
            continue

        if heavy:
            from ...localization import fft_vs_mc
            g2 = fft_vs_mc(state0, cut, make_rng(seed + 7), N=500_000, n_bins=n_bins)
            fft_gate = g2.as_record()
            fft_gate["gate"] = "initial_fft_vs_mc"
            fft_gate["status"] = "run"
        else:
            fft_gate = _missing_gate("initial_fft_vs_mc", "heavy=False; independent cross-check omitted")
        rec["gate_fft_vs_mc"] = fft_gate

        if not fft_gate["passed"]:
            reason = ("required fft_vs_mc gate failed" if fft_gate["status"] == "run"
                      else "required fft_vs_mc gate missing")
            rec["gate_dt_refinement"] = _missing_gate(
                "dt_refinement", "not run because fft_vs_mc did not pass"
            )
            rec["assessment"] = _unavailable_assessment(reason, gates_passed=False)
            gate_summary[str(n)] = False
            records.append(rec)
            continue

        dt_gate, res = _dt_refinement_gate(
            n, cut, T=T, dt=dt, seed=seed + n, n_paths=n_paths, n_bins=n_bins
        )
        rec["gate_dt_refinement"] = dt_gate
        gates_passed = _required_gates_pass(cal_gate, bins_gate, fft_gate, dt_gate)
        gate_summary[str(n)] = gates_passed
        norm_budget = res.mean / n
        rec.update({"xi_S_mean": res.mean, "xi_S_stderr": res.stderr,
                    "budget_k": n, "normalized_budget": norm_budget,
                    "within_budget": bool(res.mean <= n + 1e-9),
                    "assessment": _unavailable_assessment(
                        "all numerical gates passed, but q:alignment/q:taming observables are absent"
                        if gates_passed else "required dt-refinement gate failed",
                        gates_passed=gates_passed,
                    )})
        if gates_passed:
            sweep.append((n, norm_budget))
        records.append(rec)

    # Diagnostic summary only. Xi_S/n is neither the q:alignment nor the q:taming observable.
    records.append({
        "kind": "diagnostic-summary",
        "instance": "thinshell-source-occupation",
        "gated_normalized_budget_by_n": {str(n): b for n, b in sweep},
        "required_gates_passed_by_n": gate_summary,
        "assessment": _unavailable_assessment(
            "Xi_S/n is an engine diagnostic; actual q:alignment and q:taming observables are not built",
            gates_passed=bool(gate_summary) and all(gate_summary.values()),
        ),
    })

    return RunResult(
        records,
        config={"ns": list(ns), "T": T, "dt": dt, "n_paths": n_paths,
                "n_bins": n_bins, "heavy": heavy},
        summary={"calibration_passed": cal_ok,
                 "route_observable_available": False,
                 "dynamic_quadrature_available": False,
                 "route_comparison_available": False,
                 "diagnostic_only": True},
    )


def selftest(rng):
    checks = []
    # calibration: Gaussian covariance oracle to machine precision.
    err = _gaussian_covariance_max_err(T=0.5, dt=0.02, n=4)
    checks.append((f"loc-engine cal: A_t==1/(1+t) ({err:.1e})", err < 1e-10))
    # rank-one budget: single-coordinate occupation E int S dt <= 1.
    cut1 = single_coord(0, 0.0, psi=PSI_ID, side="ge")
    res1 = _occupation_xi_S(8, cut1, T=4.0, dt=0.04, seed=11, n_paths=24, n_bins=1 << 14)
    m, se = res1.mean, (res1.stderr or 0.0)
    checks.append((f"loc-engine rank-one budget <= 1 (mean={m:.3f}+-{se:.3f})", m <= 1.0 + 3 * se))
    # n_bins gate passes on a small thin shell.
    state0, cut = _balanced_thinshell(3)
    g = n_bins_convergence(state0, cut, n_bins_list=(1 << 13, 1 << 14, 1 << 15))
    checks.append((f"loc-engine n_bins gate passes (n=3): {g.detail}", g.passed))
    return checks
