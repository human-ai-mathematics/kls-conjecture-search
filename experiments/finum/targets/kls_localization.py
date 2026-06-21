"""KLS Part III — the LOCALIZATION channel (target id ``kls-loc``).

The SDE-free target ``kls`` gates the route-agnostic, Poincare-level facts. This target runs the
Eldan stochastic-localization engine (``finum.localization``) to produce the per-route
DIRECTIONAL signals research/kls/gating.md defers here: the source occupation budget
``Xi_S(T) = E int_0^{T wedge tau} S dt`` on balanced cuts across an n-sweep (q:upgrade / q:taming
/ thm:budget) and the per-direction budget (cor:per-direction / q:alignment).

Epistemic status (see finum soundness contract + research/kls/shared/target.md): these numbers
NEVER certify. They are read only behind passing gates:
  * calibration — the Gaussian model oracle ``A_t = (1+t)^{-1} I`` reproduces to ~1e-12
    (a bug in the integrator/quadrature breaks this);
  * ``n_bins_convergence`` — the gridded k>=2 background has converged on the thin-shell cut.
A verdict behind a red gate is recorded as ``no-verdict``, not scored. The expensive
``fft_vs_mc`` cross-check (independent MC) runs only when ``heavy=True``.

Direction read off the occupation sweep:
  * proved fact (thm:budget): ``Xi_S <= k`` for a k-coordinate cut — a gross violation REFUTES
    the engine/assembly, not the conjecture;
  * the NORMALIZED budget ``Xi_S / n`` flat or decreasing in n SUPPORTS taming (Route A);
    growth in n is directional evidence AGAINST.
"""
from __future__ import annotations

import numpy as np

from ..localization import (
    LAPLACE,
    ProductState,
    balanced_threshold,
    block_sum,
    make_rng,
    n_bins_convergence,
    single_coord,
    spawn_rngs,
)
from ..localization.cuts import PSI_ID, PSI_SQ
from ..localization.observables import ensemble_mean, integrate_path
from ..localization.sde import localization_path
from ..localization.tilt1d import GAUSSIAN

OBSTRUCTION = "obs:rank-one-refuted"  # the budget facts this channel exercises

_COV_ORACLE_TOL = 1e-10  # absolute tol on |A_t - 1/(1+t)| (deterministic Gaussian model)


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


def run_records(seed: int = 0, ns=(2, 3, 4), T: float = 0.5, dt: float = 0.1,
                n_paths: int = 12, n_bins: int = 1 << 15, heavy: bool = False):
    records = []

    # calibration gate (shared by every n): the Gaussian covariance oracle A_t = 1/(1+t) I.
    cov_err = _gaussian_covariance_max_err()
    cal_ok = cov_err < _COV_ORACLE_TOL
    records.append({"kind": "calibration", "instance": "cal-kls-loc-gaussian",
                    "claim": "A_t == 1/(1+t) I (Gaussian model)", "max_abs_err": cov_err,
                    "abs_tol": _COV_ORACLE_TOL, "status": "match" if cal_ok else "mismatch"})

    # rank-one budget sanity: single-coordinate cut has E int_0^inf S dt <= 1 (cor:refutation).
    cut1 = single_coord(0, 0.0, psi=PSI_ID, side="ge")
    res1 = _occupation_xi_S(8, cut1, T=4.0, dt=0.04, seed=seed + 11, n_paths=n_paths,
                            n_bins=n_bins)
    records.append({"kind": "budget", "instance": "rank-one", "obstruction": OBSTRUCTION,
                    "xi_S_mean": res1.mean, "xi_S_stderr": res1.stderr, "budget_k": 1,
                    "within_budget": bool(res1.mean <= 1.0 + 3 * (res1.stderr or 0.0)),
                    "note": "single-coordinate cut: E int S dt <= 1 (cor:refutation)"})

    # the n-sweep on the balanced thin-shell energy cut.
    sweep = []
    for n in ns:
        state0, cut = _balanced_thinshell(n)
        gate = n_bins_convergence(state0, cut,
                                  n_bins_list=(n_bins >> 2, n_bins >> 1, n_bins))
        rec = {"kind": "occupation", "instance": f"thinshell-n{n}", "n": n,
               "gate_n_bins": gate.as_record()}
        if heavy:
            from ..localization import fft_vs_mc
            g2 = fft_vs_mc(state0, cut, make_rng(seed + 7), N=500_000, n_bins=n_bins)
            rec["gate_fft_vs_mc"] = g2.as_record()
            gate_ok = gate.passed and g2.passed
        else:
            gate_ok = gate.passed
        if not gate_ok:
            rec["verdict"] = {"status": "no-verdict", "reason": "convergence gate red"}
            records.append(rec)
            continue
        res = _occupation_xi_S(n, cut, T=T, dt=dt, seed=seed + n, n_paths=n_paths,
                               n_bins=n_bins)
        norm_budget = res.mean / n
        rec.update({"xi_S_mean": res.mean, "xi_S_stderr": res.stderr,
                    "budget_k": n, "normalized_budget": norm_budget,
                    "within_budget": bool(res.mean <= n + 1e-9)})
        sweep.append((n, norm_budget))
        records.append(rec)

    # directional verdict on the normalized budget across n (only over gated points).
    if len(sweep) >= 2:
        nb = [b for _, b in sweep]
        grew = nb[-1] > nb[0] * 1.25  # >25% growth across the sweep
        records.append({"kind": "verdict", "instance": "thinshell-budget-sweep",
                        "normalized_budget_by_n": {str(n): b for n, b in sweep},
                        "supports_taming": bool(not grew),
                        "note": "Xi_S/n flat-or-decreasing in n SUPPORTS taming (Route A); "
                                "growth is directional evidence against. Direction only — never proof."})

    extra = {"ns": list(ns), "T": T, "dt": dt, "n_paths": n_paths, "n_bins": n_bins,
             "heavy": heavy, "calibration_passed": cal_ok}
    return records, extra


def selftest(rng):
    checks = []
    # calibration: Gaussian covariance oracle to machine precision.
    err = _gaussian_covariance_max_err(T=0.5, dt=0.02, n=4)
    checks.append((f"kls-loc cal: A_t==1/(1+t) ({err:.1e})", err < 1e-10))
    # rank-one budget: single-coordinate occupation E int S dt <= 1.
    cut1 = single_coord(0, 0.0, psi=PSI_ID, side="ge")
    res1 = _occupation_xi_S(8, cut1, T=4.0, dt=0.04, seed=11, n_paths=24, n_bins=1 << 14)
    m, se = res1.mean, (res1.stderr or 0.0)
    checks.append((f"kls-loc rank-one budget <= 1 (mean={m:.3f}+-{se:.3f})", m <= 1.0 + 3 * se))
    # n_bins gate passes on a small thin shell.
    state0, cut = _balanced_thinshell(3)
    g = n_bins_convergence(state0, cut, n_bins_list=(1 << 13, 1 << 14, 1 << 15))
    checks.append((f"kls-loc n_bins gate passes (n=3): {g.detail}", g.passed))
    return checks
