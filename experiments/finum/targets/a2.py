"""A2 — Bernstein-von Mises constants. Obstruction: obs:tv-insufficient.

Sharp target (conj:a2): n*C_P(pi_n) -> lambda_max(I(theta0)^{-1}) = 1/lambda_min(I(theta0)).
  * cal-bvm-gausslinear : Gaussian-linear model where n*C_P = 1/lambda_min(Sigma_x) EXACTLY
                          (validates the n-scaling bookkeeping).
  * stress-contamination: (1-eps)N(0,1)+eps N(a,1), eps*a^2 -> inf. C_P -> inf (linear test)
                          while ||.||_TV <= eps -> 0, so "BvM (TV) => constants" is FALSIFIED.
  * stress-bvm-sweep    : regular logistic n-sweep; n*C_P_lower trends toward lambda_max(I^{-1}).
"""
from __future__ import annotations

import numpy as np

from ..constants import poincare_lower
from ..instance import sigmoid
from ..sampling import mala_adaptive
from ..verdict import falsify, matches

OBSTRUCTION = "obs:tv-insufficient"


# ---- calibration: Gaussian-linear n-scaling is exact ---------------------------

def cal_bvm_gausslinear(seed: int = 30, d: int = 2):
    """Deterministic population design: posterior Cov = (n Sigma_x)^{-1}, so
    n*C_P = lambda_max(Sigma_x^{-1}) = 1/lambda_min(Sigma_x) for every n. Returns
    (list of (n, nCp), exact)."""
    rng = np.random.default_rng(seed)
    B = rng.standard_normal((d, d))
    Sigma_x = B @ B.T + 0.5 * np.eye(d)             # SPD Fisher / design second moment
    exact = 1.0 / float(np.linalg.eigvalsh(Sigma_x)[0])
    out = []
    for n in (50, 100, 200, 400):
        cov = np.linalg.inv(n * Sigma_x)
        nCp = n * float(np.linalg.eigvalsh(cov)[-1])
        out.append((n, nCp))
    return out, exact


# ---- stress: contamination (TV -> 0 but C_P -> inf) ----------------------------

def contamination_variance(eps: float, a: float) -> float:
    """Var of (1-eps)N(0,1)+eps N(a,1) = 1 + eps*a^2 - (eps*a)^2 (a sound C_P lower bound)."""
    mean = eps * a
    second = (1 - eps) * 1.0 + eps * (1.0 + a * a)
    return second - mean * mean


# ---- stress: regular-logistic BvM sweep ----------------------------------------

def _fisher_logistic(theta0, d, n_mc=200000, seed=31):
    rng = np.random.default_rng(seed)
    X = rng.standard_normal((n_mc, d))
    w = sigmoid(X @ theta0) * (1 - sigmoid(X @ theta0))
    I = (X * w[:, None]).T @ X / n_mc
    return I


def _logistic_nCp(n, theta0, d, rng, n_samples=3000):
    X = rng.standard_normal((n, d))
    y = (rng.random(n) < sigmoid(X @ theta0)).astype(float)
    Sig0inv = np.eye(d) / 100.0                      # weak prior ~ flat
    def grad(t): return X.T @ (y - sigmoid(X @ t)) - Sig0inv @ t
    def logp(t):
        s = X @ t
        return float(np.sum(y * s - np.logaddexp(0.0, s)) - 0.5 * t @ Sig0inv @ t)
    # mode (Newton) + bulk preconditioner
    t = np.zeros(d)
    for _ in range(50):
        s = X @ t; w = sigmoid(s) * (1 - sigmoid(s))
        H = X.T @ (w[:, None] * X) + Sig0inv
        t = t + np.linalg.solve(H, grad(t))
    s = X @ t; w = sigmoid(s) * (1 - sigmoid(s))
    Ainv = np.linalg.inv(X.T @ (w[:, None] * X) + Sig0inv)
    samples = mala_adaptive(grad, logp, t, n_samples, rng, init_precond=Ainv)
    return n * poincare_lower(samples)


# ---- run + selftest ------------------------------------------------------------

def run_records(seed: int = 0):
    records = []
    cal_ok = True

    sweep, exact = cal_bvm_gausslinear()
    for n, nCp in sweep:
        v = matches("cal-bvm-gausslinear", "n*C_P == 1/lambda_min(Sigma_x)", nCp, exact, rel_tol=0.02)
        cal_ok = cal_ok and v.status == "match"
        records.append({"kind": "calibration", "instance": "cal-bvm-gausslinear",
                        "n": n, "nCp": nCp, "exact": exact, "verdict": v.dict()})

    # contamination: eps_n = n^{-1/2}, a_n = n^{0.4}  => eps*a^2 = n^{0.3} -> inf, TV<=eps -> 0
    for n in (100, 1000, 10000):
        eps = n ** -0.5
        a = n ** 0.4
        var = contamination_variance(eps, a)
        v = falsify("C_P <= 3 (BvM Gaussian scale)", "stress-contamination", 3.0, var,
                    note="TV<=eps->0 but C_P>=Var->inf; BvM(TV)=>constants is false")
        records.append({"kind": "stress", "instance": "stress-contamination", "obstruction": OBSTRUCTION,
                        "n": n, "eps": eps, "a": a, "tv_upper": eps, "C_P_lower": var,
                        "verdict": v.dict()})

    # bvm-sweep (directional): n*C_P_lower should trend toward lambda_max(I(theta0)^{-1})
    d = 2
    theta0 = np.array([0.8, -0.5])
    I = _fisher_logistic(theta0, d)
    target = 1.0 / float(np.linalg.eigvalsh(I)[0])
    rng = np.random.default_rng(seed + 7)
    sweep_vals = []
    for n in (60, 120, 240, 480):
        sweep_vals.append((n, _logistic_nCp(n, theta0, d, rng)))
    trend_up = sweep_vals[-1][1] > sweep_vals[0][1]
    records.append({"kind": "stress", "instance": "stress-bvm-sweep", "obstruction": OBSTRUCTION,
                    "target_lambda_max_Iinv": target,
                    "n_Cp_lower": [{"n": n, "nCp_lower": v} for n, v in sweep_vals],
                    "trend_toward_target": bool(trend_up),
                    "note": "directional: n*C_P_lower (<= n*C_P) increases toward lambda_max(I^{-1})."})

    records.append({"kind": "stress", "instance": "stress-non-fisher-local", "status": "deferred",
                    "obstruction": OBSTRUCTION,
                    "note": "shallow remote near-minimizer => n*C_LS -> 1/mu_PL != lambda_max(I^{-1}); "
                            "exercises q:a2-lsi (deferred — needs an LSI estimator)."})
    return records, {"calibration_passed": cal_ok}


def selftest(rng):
    checks = []
    sweep, exact = cal_bvm_gausslinear()
    ok = all(abs(nCp - exact) <= 0.02 * exact for _, nCp in sweep)
    checks.append((f"A2 cal-bvm-gausslinear: n*C_P == 1/lambda_min (={exact:.4f}) for all n", ok))
    # contamination: C_P lower bound grows without bound while TV -> 0
    v_small = contamination_variance(100 ** -0.5, 100 ** 0.4)
    v_big = contamination_variance(10000 ** -0.5, 10000 ** 0.4)
    checks.append((f"A2 stress-contamination: C_P_lower grows ({v_small:.2f} -> {v_big:.2f}) while TV->0",
                   v_big > v_small > 3.0))
    return checks
