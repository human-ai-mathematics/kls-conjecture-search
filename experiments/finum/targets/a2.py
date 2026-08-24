"""A2 — Bernstein-von Mises constants. Obstruction: obs:tv-insufficient.

Sharp target (conj:a2): n*C_P(pi_n) -> lambda_max(I(theta0)^{-1}) = 1/lambda_min(I(theta0)).
  * cal-bvm-gausslinear : Gaussian-linear model where n*C_P = 1/lambda_min(Sigma_x) EXACTLY
                          (validates the n-scaling bookkeeping).
  * stress-contamination: an exact variance lower bound proves that TV-BvM alone does not
                          control C_P.
  * stress-bvm-sweep    : a single-draw regular-logistic sweep, reported as directional only.
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


def gaussian_prior_tail_tradeoff(n: int, covariance) -> dict[str, float]:
    """Deterministic consequence of the proved Gaussian-tail-rigidity theorem.

    For a subquadratic convex likelihood (in particular finite logistic),
    ``C_LS = C_T2 = lambda_max(covariance)``.  The key names deliberately do not
    assert the corresponding equality for ``C_P``.
    """
    covariance = np.asarray(covariance, dtype=float)
    if n <= 0 or covariance.ndim != 2 or covariance.shape[0] != covariance.shape[1]:
        raise ValueError("n must be positive and covariance must be square")
    eig = np.linalg.eigvalsh(covariance)
    if eig[0] <= 0:
        raise ValueError("covariance must be positive definite")
    precision_over_n = np.linalg.inv(covariance) / float(n)
    return {
        "global_lsi_t2_constant": float(eig[-1]),
        "n_global_lsi_t2_constant": float(n * eig[-1]),
        "relative_precision_min": float(np.linalg.eigvalsh(precision_over_n)[0]),
        "relative_precision_max": float(np.linalg.eigvalsh(precision_over_n)[-1]),
    }


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


def _endpoint_error_summary(sweep_vals, target):
    """Endpoint diagnostic for a noisy convergence-in-probability sweep.

    Convergence to ``target`` need not be monotone, and it can approach from either side.  The
    old diagnostic checked ``last > first``, which encoded neither property.  This deliberately
    weak directional summary only asks whether the final endpoint is closer than the first.
    """
    if len(sweep_vals) < 2:
        raise ValueError("an endpoint diagnostic needs at least two sweep values")
    errors = [abs(float(value) - float(target)) for _, value in sweep_vals]
    return {
        "initial_abs_error": errors[0],
        "final_abs_error": errors[-1],
        "endpoint_closer_to_target": errors[-1] < errors[0],
    }


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

    tradeoff_n = 10_000
    for regime, covariance in (
        ("locally-negligible-prior", tradeoff_n ** -0.5 * np.eye(2)),
        ("fisher-scale-prior", tradeoff_n ** -1.0 * np.eye(2)),
    ):
        records.append({
            "kind": "analytic-result",
            "instance": "gaussian-prior-tail-tradeoff",
            "ledger_node": "prop:a2-subquadratic-global",
            "theorem_status": "proved",
            "regime": regime,
            "n": tradeoff_n,
            **gaussian_prior_tail_tradeoff(tradeoff_n, covariance),
        })

    # contamination: eps_n = n^{-1/2}, a_n = n^{0.4}  => eps*a^2 = n^{0.3} -> inf, TV<=eps -> 0
    for n in (100, 1000, 10000):
        eps = n ** -0.5
        a = n ** 0.4
        var = contamination_variance(eps, a)
        v = falsify("C_P <= 3 (BvM Gaussian scale)", "stress-contamination", 3.0, var,
                    note="TV<=eps->0 but C_P>=Var->inf; BvM(TV)=>constants is false")
        records.append({"kind": "analytic-obstruction", "instance": "stress-contamination",
                        "obstruction": OBSTRUCTION, "theorem_status": "proved",
                        "n": n, "eps": eps, "a": a, "tv_upper": eps,
                        "analytic_C_P_lower": var, "verdict": v.dict()})

    if cal_ok:
        # This is deliberately a single-draw/single-chain diagnostic, not a
        # convergence-in-probability experiment or a lower-bound certificate.
        d = 2
        theta0 = np.array([0.8, -0.5])
        I = _fisher_logistic(theta0, d)
        target = 1.0 / float(np.linalg.eigvalsh(I)[0])
        rng = np.random.default_rng(seed + 7)
        sweep_vals = [
            (n, _logistic_nCp(n, theta0, d, rng))
            for n in (60, 120, 240, 480)
        ]
        endpoint = _endpoint_error_summary(sweep_vals, target)
        records.append({
            "kind": "directional-diagnostic",
            "instance": "stress-bvm-sweep",
            "status": "directional-only",
            "estimated_target_lambda_max_Iinv": target,
            "n_Cp_empirical": [
                {"n": n, "nCp_estimate": value,
                 "abs_error_to_estimated_target": abs(value - target)}
                for n, value in sweep_vals
            ],
            **endpoint,
            "note": "One data set and one MCMC chain per n. Repeated data draws, "
                    "independent-chain gates, and uncertainty bounds are still required.",
        })
    else:
        records.append({"kind": "directional-diagnostic", "instance": "stress-bvm-sweep",
                        "status": "no-diagnostic", "reason": "calibration gate red"})

    return records, {"calibration_passed": cal_ok,
                     "sampled_diagnostics_gated": bool(cal_ok)}


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
    endpoint = _endpoint_error_summary([(60, 12.596), (240, 7.004), (480, 7.649)], 6.603)
    checks.append(("A2 BvM endpoint diagnostic uses distance to target (not increasing/decreasing)",
                   endpoint["endpoint_closer_to_target"]
                   and endpoint["final_abs_error"] < endpoint["initial_abs_error"]))
    return checks
