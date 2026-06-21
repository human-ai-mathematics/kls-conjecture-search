"""A1 — data-informed GLM Poincare constant. Obstruction: obs:flat-direction.

Mirrors the A1 tier of research/knowledge/instances.md. Calibration instances have exact
ground truth (the pipeline must reproduce them or it emits NO verdict); the stress tier is the
near-separable / wide / anisotropic logistic battery that demonstrates obs:flat-direction:
a *tail-free* (bulk-only) bound is FALSIFIED while the data-free prior bound lambda_max(Sigma0)
holds. Bounds carried on each Instance:
  * prior_bound = lambda_max(Sigma0)                      Part I theorem  C_P <= lambda_max(Sigma0)
  * bulk_bound  = lambda_max((Sigma0^{-1}+X^T diag(w) X)^{-1})   the TAIL-FREE candidate
"""
from __future__ import annotations

import numpy as np

from ..constants import poincare_lower, poincare_1d_fem
from ..instance import Instance, sigmoid
from ..sampling import mala_adaptive
from ..verdict import calibration_ok, falsify, two_seed_lower

OBSTRUCTION = "obs:flat-direction"


# ---- calibration tier (exact ground truth) -------------------------------------

def cal_gauss(seed: int = 10, d: int = 6) -> Instance:
    rng = np.random.default_rng(seed)
    diag = rng.uniform(0.5, 4.0, size=d)
    lam = float(diag.max())
    sd = np.sqrt(diag)
    return Instance(
        id="cal-gauss", tier="calibration", obstruction=None,
        sampler=lambda n, r: r.standard_normal((n, d)) * sd,
        exact=lam, prior_bound=lam, bulk_bound=lam,
        note="anisotropic N(0,Sigma): C_P = lambda_max(Sigma); linear test must hit it exactly.",
        meta={"d": d, "diag": diag.tolist()},
    )


def cal_glm_linear(seed: int = 11, n_data: int = 200, d: int = 5) -> Instance:
    """Gaussian-linear GLM (W = I): posterior is Gaussian, A1 bound is exact (tightness~1)."""
    rng = np.random.default_rng(seed)
    X = rng.standard_normal((n_data, d))
    s0 = 3.0
    prec = np.eye(d) / s0**2 + X.T @ X
    cov = np.linalg.inv(prec)
    cov = 0.5 * (cov + cov.T)
    lam = float(np.linalg.eigvalsh(cov)[-1])
    L = np.linalg.cholesky(cov)
    return Instance(
        id="cal-glm-linear", tier="calibration", obstruction=None,
        sampler=lambda n, r: r.standard_normal((n, d)) @ L.T,
        exact=lam, prior_bound=s0**2, bulk_bound=lam,
        note="Gaussian-linear GLM: Cov=(Sigma0^{-1}+X^TX)^{-1}; A1 bulk bound is exact.",
        meta={"d": d, "n_data": n_data, "sigma0": s0},
    )


def cal_1d_eigen(seed: int = 12, sigma: float = 1.3) -> Instance:
    """1D Gaussian with sigma known: ground truth C_P=sigma^2 also recovered by the FEM eigensolve."""
    xs = np.linspace(-12 * sigma, 12 * sigma, 1601)
    U = lambda x: x**2 / (2 * sigma**2)
    fem = poincare_1d_fem(U, xs)               # must reproduce sigma^2
    return Instance(
        id="cal-1d-eigen", tier="calibration", obstruction=None,
        sampler=lambda n, r: (r.standard_normal((n, 1)) * sigma),
        exact=sigma**2, prior_bound=sigma**2, bulk_bound=sigma**2,
        note="1D Gaussian: FEM gap eigensolve is the two-sided ground truth.",
        meta={"sigma2": sigma**2, "fem_estimate": fem},
    )


CALIBRATION = [cal_gauss, cal_glm_linear, cal_1d_eigen]


# ---- stress tier (obs:flat-direction) ------------------------------------------

def _logistic_posterior(X, y, Sigma0):
    """Return (logp, grad_logp, mode, bulk_bound, prior_bound, Ainv) for the GLM posterior."""
    Sig0inv = np.linalg.inv(Sigma0)
    prior_bound = float(np.linalg.eigvalsh(Sigma0)[-1])

    def neg_grad_U(theta):
        s = X @ theta
        return X.T @ (y - sigmoid(s)) - Sig0inv @ theta

    def logp(theta):
        s = X @ theta
        ll = np.sum(y * s - np.logaddexp(0.0, s))
        return float(ll - 0.5 * theta @ Sig0inv @ theta)

    # crude posterior-mode estimate (a few Newton steps) for the bulk curvature
    theta = np.zeros(X.shape[1])
    for _ in range(50):
        s = X @ theta
        w = sigmoid(s) * (1 - sigmoid(s))
        H = X.T @ (w[:, None] * X) + Sig0inv
        g = neg_grad_U(theta)
        theta = theta + np.linalg.solve(H, g)
    s = X @ theta
    wbar = sigmoid(s) * (1 - sigmoid(s))
    A = X.T @ (wbar[:, None] * X) + Sig0inv
    Ainv = np.linalg.inv(A)
    bulk_bound = float(np.linalg.eigvalsh(Ainv)[-1])
    return logp, neg_grad_U, theta, bulk_bound, prior_bound, Ainv


def _logistic_instance(iid, obstruction, X, y, Sigma0, note):
    logp, grad, mode, bulk_bound, prior_bound, Ainv = _logistic_posterior(X, y, Sigma0)

    def sampler(n, rng):
        return mala_adaptive(grad, logp, mode, n, rng, init_precond=Ainv)

    return Instance(
        id=iid, tier="stress", obstruction=obstruction, sampler=sampler,
        exact=None, prior_bound=prior_bound, bulk_bound=bulk_bound, note=note,
        meta={"d": int(X.shape[1]), "n_data": int(X.shape[0])},
    )


def stress_logit_separable(seed: int = 20, n_data: int = 30, d: int = 3, margin: float = 9.0) -> Instance:
    """Near-separable logistic: bulk stays small while lambda_max(Cov) inflates => a tail-free
    (bulk-only) bound is FALSIFIED; the prior bound lambda_max(Sigma0) still holds."""
    rng = np.random.default_rng(seed)
    X = rng.standard_normal((n_data, d))
    theta_star = rng.standard_normal(d)
    theta_star /= np.linalg.norm(theta_star)
    y = (X @ theta_star > 0).astype(float)
    X = X * margin                                # inflate scale => near-separable
    Sigma0 = 8.0 * np.eye(d)
    return _logistic_instance(
        "stress-logit-separable", OBSTRUCTION, X, y, Sigma0,
        "near-separable logistic; tail-free bound must fail, prior bound must hold.",
    )


def stress_anisotropic_prior(seed: int = 21, n_data: int = 120, d: int = 4) -> Instance:
    rng = np.random.default_rng(seed)
    X = rng.standard_normal((n_data, d))
    y = (rng.random(n_data) < sigmoid(X @ rng.standard_normal(d))).astype(float)
    Sigma0 = np.diag(np.geomspace(0.2, 20.0, d))
    return _logistic_instance(
        "stress-anisotropic-prior", OBSTRUCTION, X, y, Sigma0,
        "strongly anisotropic Sigma0: scalar floor vs matrix bound.",
    )


def stress_wide(seed: int = 22, n_data: int = 8, d: int = 20) -> Instance:
    """D > n: rank-deficient X^TWX; bound must revert to prior scale on data-blind directions."""
    rng = np.random.default_rng(seed)
    X = rng.standard_normal((n_data, d))
    y = (rng.random(n_data) < 0.5).astype(float)
    Sigma0 = 5.0 * np.eye(d)
    return _logistic_instance(
        "stress-wide", OBSTRUCTION, X, y, Sigma0,
        "wide D>n: prior scale governs the rank-deficient subspace.",
    )


def stress_logit_bulk(seed: int = 23, n_data: int = 400, d: int = 4) -> Instance:
    """Well-identified, bulk-dominated logistic: the tail-free bound SHOULD be valid and tight."""
    rng = np.random.default_rng(seed)
    X = rng.standard_normal((n_data, d))
    y = (rng.random(n_data) < sigmoid(X @ (0.8 * rng.standard_normal(d)))).astype(float)
    Sigma0 = 10.0 * np.eye(d)
    return _logistic_instance(
        "stress-logit-bulk", OBSTRUCTION, X, y, Sigma0,
        "well-identified logistic: tail-free bound valid; prior bound loose.",
    )


STRESS = [stress_logit_separable, stress_anisotropic_prior, stress_wide, stress_logit_bulk]


# ---- run + selftest ------------------------------------------------------------

def run_records(seed: int = 0, n_cal: int = 20000, n_stress: int = 4000):
    """A1 calibration gate + obs:flat-direction stress battery. Returns (records, extra_header)."""
    rng = np.random.default_rng(seed)
    records: list[dict] = []

    cal_ok = True
    for gen in CALIBRATION:
        inst = gen()
        est = poincare_lower(inst.sample(n_cal, rng))
        ok = calibration_ok(est, inst.exact)
        cal_ok = cal_ok and ok
        rec = {"kind": "calibration", "instance": inst.id, "exact": inst.exact,
               "linear_test": est, "rel_err": abs(est - inst.exact) / abs(inst.exact),
               "passed": ok, "note": inst.note}
        if "fem_estimate" in inst.meta:
            rec["fem_estimate"] = inst.meta["fem_estimate"]
        records.append(rec)

    for gen in STRESS:
        inst = gen()
        if not cal_ok:
            records.append({"kind": "stress", "instance": inst.id, "status": "no-verdict",
                            "reason": "calibration gate red", "obstruction": inst.obstruction})
            continue
        lower, conv, (la, lb) = two_seed_lower(inst, n_stress, seed + 1, seed + 2)
        if not conv:
            records.append({"kind": "stress", "instance": inst.id, "status": "no-verdict",
                            "reason": "convergence gate red (chains disagree)",
                            "lower_a": la, "lower_b": lb, "obstruction": inst.obstruction})
            continue
        v_bulk = falsify("C_P <= bulk_bound (tail-free)", inst.id, inst.bulk_bound, lower,
                         note="obs:flat-direction: tail-free bound expected to FAIL on separable")
        v_prior = falsify("C_P <= prior_bound = lambda_max(Sigma0)", inst.id, inst.prior_bound,
                          lower, note="Part I theorem; must stay consistent (sanity)")
        # sanity gate: C_P <= lambda_max(Sigma0) is a theorem (Brascamp-Lieb on the GLM
        # posterior), so a "refuted" prior bound can only mean the chain is NOT equilibrated.
        if v_prior.status == "REFUTED":
            records.append({"kind": "stress", "instance": inst.id, "status": "no-verdict",
                            "reason": "sanity gate red: prior bound lambda_max(Sigma0) exceeded "
                                      "(impossible by theorem => sampler not equilibrated)",
                            "lower": lower, "prior_bound": inst.prior_bound,
                            "obstruction": inst.obstruction})
            continue
        records.append({
            "kind": "stress", "instance": inst.id, "obstruction": inst.obstruction,
            "lower": lower, "lower_a": la, "lower_b": lb,
            "bulk_bound": inst.bulk_bound, "prior_bound": inst.prior_bound,
            "verdict_bulk": v_bulk.dict(), "verdict_prior": v_prior.dict(),
            "sanity_prior_consistent": v_prior.status == "consistent",
            "note": inst.note,
        })

    return records, {"n_cal": n_cal, "n_stress": n_stress, "calibration_passed": cal_ok}


def selftest(rng):
    checks = []
    for gen in CALIBRATION:
        inst = gen()
        est = poincare_lower(inst.sample(40000, rng))
        checks.append((f"A1 {inst.id}: linear test = exact ({est:.4f} vs {inst.exact:.4f})",
                       calibration_ok(est, inst.exact)))
    c1 = cal_1d_eigen()
    checks.append((f"A1 cal-1d-eigen: FEM gap = sigma^2 ({c1.meta['fem_estimate']:.4f} vs {c1.exact:.4f})",
                   calibration_ok(c1.meta["fem_estimate"], c1.exact)))
    g = cal_gauss()
    lower = poincare_lower(g.sample(40000, rng))
    checks.append(("A1 cal-gauss: claim C_P <= 0.7 lambda_max is REFUTED",
                   falsify("c", g.id, 0.7 * g.exact, lower).status == "REFUTED"))
    checks.append(("A1 cal-gauss: claim C_P <= 0.01 is REFUTED",
                   falsify("c", g.id, 0.01, lower).status == "REFUTED"))
    checks.append(("A1 cal-gauss: claim C_P <= lambda_max is consistent",
                   falsify("c", g.id, g.exact, lower).status == "consistent"))
    return checks
