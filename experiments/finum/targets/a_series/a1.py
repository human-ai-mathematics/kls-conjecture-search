"""A1 — data-informed GLM Poincare constant. Obstruction: obs:flat-direction.

Mirrors the A1 tier of research/knowledge/instances.md. Calibration instances have exact
ground truth; the stress tier is the near-separable / wide / anisotropic logistic battery that
illustrates ``obs:flat-direction``. Its MCMC covariance estimates are directional and cannot by
themselves refute a bound. Bounds carried on each ``Instance`` are:
  * prior_bound = lambda_max(Sigma0)                      Part I theorem  C_P <= lambda_max(Sigma0)
  * bulk_bound  = lambda_max((Sigma0^{-1}+X^T diag(w) X)^{-1})   the TAIL-FREE candidate
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable

import numpy as np

from ...contract import RunResult
from ...constants import poincare_lower, poincare_1d_fem
from ...sampling import mala_adaptive, sigmoid
from ...comparison import calibration_ok, compare_directional, two_seed_lower

OBSTRUCTION = "obs:flat-direction"


@dataclass
class Instance:
    """A1's sample-based calibration/stress case."""

    id: str
    tier: str
    obstruction: str | None
    sampler: Callable[[int, np.random.Generator], np.ndarray]
    exact: float | None = None
    prior_bound: float | None = None
    bulk_bound: float | None = None
    note: str = ""
    meta: dict = field(default_factory=dict)

    def sample(self, n: int, rng: np.random.Generator) -> np.ndarray:
        return self.sampler(n, rng)


# ---- proved deterministic mode-leverage quantities ---------------------------

def mode_leverage_g_minus(r, eta: float):
    """Lower radial potential ``g_-(r; eta)`` from log-Hessian Lipschitzness.

    The continuous value at ``eta=0`` is ``r**2 / 2``.  ``expm1`` avoids the
    cancellation in ``exp(-eta*r) + eta*r - 1`` for small leverage.
    """
    r = np.asarray(r, dtype=float)
    eta = float(eta)
    if eta < 0:
        raise ValueError("eta must be nonnegative")
    if eta == 0:
        return 0.5 * r * r
    a = eta * r
    return (np.expm1(-a) + a) / (eta * eta)


def mode_leverage_g_plus(r, eta: float):
    """Upper radial potential ``g_+(r; eta)`` from log-Hessian Lipschitzness."""
    r = np.asarray(r, dtype=float)
    eta = float(eta)
    if eta < 0:
        raise ValueError("eta must be nonnegative")
    if eta == 0:
        return 0.5 * r * r
    a = eta * r
    with np.errstate(over="ignore", invalid="ignore"):
        return (np.expm1(a) - a) / (eta * eta)


def _radial_integral(d: int, exponent, lower: float = 0.0) -> float:
    """Integrate ``r**(d-1) exp(exponent(r))`` on ``[lower, infinity)``."""
    if int(d) != d or d < 1:
        raise ValueError("d must be a positive integer")
    if lower < 0:
        raise ValueError("lower radius must be nonnegative")
    try:
        from scipy.integrate import quad
    except ImportError as exc:  # pragma: no cover - scipy is a project dependency
        raise RuntimeError("mode-leverage quadrature requires scipy") from exc

    def integrand(r):
        value = float(exponent(r))
        if not np.isfinite(value) or value < -745.0:
            return 0.0
        if value > 700.0:
            return float("inf")
        return (r ** (d - 1)) * np.exp(value)

    value, _ = quad(integrand, lower, np.inf, epsabs=2e-11, epsrel=2e-10, limit=300)
    return float(value)


def mode_leverage_tail_bound(d: int, eta: float, radius: float) -> float:
    """Explicit radial upper bound for ``P(||Hhat^(1/2)(theta-mode)|| > radius)``.

    This is the proved deterministic ratio ``N_d(radius, eta) / D_d(eta)`` from
    ``prop:a1-mode-leverage``.  It is a potential-comparison bound, not sampled evidence.
    """
    eta = float(eta)
    radius = float(radius)
    if eta < 0 or radius < 0:
        raise ValueError("eta and radius must be nonnegative")
    denominator = _radial_integral(
        d, lambda r: -mode_leverage_g_plus(r, eta)
    )
    numerator = _radial_integral(
        d, lambda r: -mode_leverage_g_minus(r, eta), lower=radius
    )
    return float(min(1.0, numerator / denominator))


def mode_leverage_factor(d: int, eta: float) -> float:
    """Factor-one inverse-curvature multiplier ``K_d(eta)`` for ``0 <= eta < 1``.

    Finiteness of this particular radial majorant requires ``eta < 1``.  A value
    at or above one is the intended high-leverage failure signal; it does not mean
    that the posterior itself lacks a Poincare inequality.
    """
    eta = float(eta)
    if not 0 <= eta < 1:
        raise ValueError("the radial K_d majorant requires 0 <= eta < 1")
    denominator = _radial_integral(
        d, lambda r: -mode_leverage_g_plus(r, eta)
    )
    numerator = _radial_integral(
        d, lambda r: eta * r - mode_leverage_g_minus(r, eta)
    )
    return float(numerator / denominator)


def logistic_mode_leverage(X, mode, hessian_at_mode):
    """Return logistic row leverages and their maximum in mode-Hessian geometry."""
    X = np.asarray(X, dtype=float)
    mode = np.asarray(mode, dtype=float)
    hessian_at_mode = np.asarray(hessian_at_mode, dtype=float)
    if X.ndim != 2 or mode.shape != (X.shape[1],):
        raise ValueError("incompatible X and mode dimensions")
    if hessian_at_mode.shape != (X.shape[1], X.shape[1]):
        raise ValueError("incompatible mode Hessian dimension")
    solved = np.linalg.solve(hessian_at_mode, X.T).T
    alpha2 = np.einsum("ij,ij->i", X, solved)
    alpha = np.sqrt(np.maximum(alpha2, 0.0))
    return alpha, float(alpha.max(initial=0.0))


def mode_leverage_weight_floor(weights_at_mode, alpha, radius: float):
    """The computable rowwise floor ``wbar_i(R)=exp(-alpha_i R) w_i(mode)``."""
    weights_at_mode = np.asarray(weights_at_mode, dtype=float)
    alpha = np.asarray(alpha, dtype=float)
    radius = float(radius)
    if weights_at_mode.shape != alpha.shape:
        raise ValueError("weights and row leverages must have the same shape")
    if radius < 0 or np.any(weights_at_mode < 0) or np.any(alpha < 0):
        raise ValueError("radius, weights, and row leverages must be nonnegative")
    return np.exp(-alpha * radius) * weights_at_mode


def mode_leverage_split_candidate(X, prior_covariance, weights_at_mode, alpha,
                                  eta: float, radius: float) -> dict:
    """Evaluate the still-unproved A1 bulk-plus-tail candidate.

    ``prop:a1-bulk-tail`` is open.  The returned expression is deliberately named
    a candidate and must not be reported as a certified upper bound.  ``eta`` may
    conservatively exceed ``max(alpha)`` but may not be smaller.
    """
    X = np.asarray(X, dtype=float)
    prior_covariance = np.asarray(prior_covariance, dtype=float)
    weights_at_mode = np.asarray(weights_at_mode, dtype=float)
    alpha = np.asarray(alpha, dtype=float)
    eta = float(eta)
    if X.ndim != 2 or weights_at_mode.shape != (X.shape[0],):
        raise ValueError("incompatible X and weights dimensions")
    if prior_covariance.shape != (X.shape[1], X.shape[1]):
        raise ValueError("incompatible prior covariance dimension")
    max_alpha = float(alpha.max(initial=0.0))
    tolerance = 1e-12 * max(1.0, max_alpha)
    if eta < 0.0 or eta + tolerance < max_alpha:
        raise ValueError("eta must be nonnegative and dominate max(alpha)")
    wbar = mode_leverage_weight_floor(weights_at_mode, alpha, radius)
    prior_precision = np.linalg.inv(prior_covariance)
    bulk_precision = prior_precision + X.T @ (wbar[:, None] * X)
    bulk_scale = 1.0 / float(np.linalg.eigvalsh(bulk_precision)[0])
    tail = mode_leverage_tail_bound(X.shape[1], eta, radius)
    prior_scale = float(np.linalg.eigvalsh(prior_covariance)[-1])
    return {
        "status": "unproved-candidate",
        "ledger_node": "prop:a1-bulk-tail",
        "eta": eta,
        "radius": float(radius),
        "wbar": wbar,
        "bulk_scale": bulk_scale,
        "tail_probability_bound": tail,
        "candidate_probability_tail_term": prior_scale * tail,
        "candidate_split_value": bulk_scale + prior_scale * tail,
    }


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
    """Gaussian ground truth with a finite-domain FEM calibration approximation."""
    xs = np.linspace(-12 * sigma, 12 * sigma, 1601)
    U = lambda x: x**2 / (2 * sigma**2)
    fem = poincare_1d_fem(U, xs)               # must reproduce sigma^2
    return Instance(
        id="cal-1d-eigen", tier="calibration", obstruction=None,
        sampler=lambda n, r: (r.standard_normal((n, 1)) * sigma),
        exact=sigma**2, prior_bound=sigma**2, bulk_bound=sigma**2,
        note="1D Gaussian: compare the finite-domain FEM approximation with exact sigma^2.",
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
    """Near-separable logistic directional stress case for a tail-free proposal."""
    rng = np.random.default_rng(seed)
    X = rng.standard_normal((n_data, d))
    theta_star = rng.standard_normal(d)
    theta_star /= np.linalg.norm(theta_star)
    y = (X @ theta_star > 0).astype(float)
    X = X * margin                                # inflate scale => near-separable
    Sigma0 = 8.0 * np.eye(d)
    return _logistic_instance(
        "stress-logit-separable", OBSTRUCTION, X, y, Sigma0,
        "near-separable logistic; compare the tail-free proposal directionally with the prior scale.",
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
    """Well-identified logistic directional comparison for the bulk proposal."""
    rng = np.random.default_rng(seed)
    X = rng.standard_normal((n_data, d))
    y = (rng.random(n_data) < sigmoid(X @ (0.8 * rng.standard_normal(d)))).astype(float)
    Sigma0 = 10.0 * np.eye(d)
    return _logistic_instance(
        "stress-logit-bulk", OBSTRUCTION, X, y, Sigma0,
        "well-identified logistic: assess whether the bulk proposal is close to the sampled scale.",
    )


STRESS = [stress_logit_separable, stress_anisotropic_prior, stress_wide, stress_logit_bulk]


# ---- run + selftest ------------------------------------------------------------

def _mode_leverage_reference_record() -> dict:
    """Deterministic evaluation of the proved mode-leverage formulas."""
    X = 0.5 * np.array([[1.0, 0.0], [0.0, 1.0], [1.0, -1.0]])
    mode = np.zeros(2)
    weights = np.full(X.shape[0], 0.25)
    prior_precision = np.eye(2)
    hessian = prior_precision + X.T @ (weights[:, None] * X)
    alpha, eta = logistic_mode_leverage(X, mode, hessian)
    radius = 2.0
    return {
        "kind": "analytic-diagnostic",
        "instance": "mode-leverage-reference",
        "ledger_node": "prop:a1-mode-leverage",
        "theorem_status": "proved",
        "eta": eta,
        "radius": radius,
        "K_d": mode_leverage_factor(X.shape[1], eta),
        "tail_probability_upper": mode_leverage_tail_bound(X.shape[1], eta, radius),
        "row_leverages": alpha.tolist(),
        "rowwise_weight_floor": mode_leverage_weight_floor(weights, alpha, radius).tolist(),
    }


def run_records(seed: int = 0, n_cal: int = 20000, n_stress: int = 4000):
    """A1 analytic formula check plus calibration-gated directional stress battery."""
    rng = np.random.default_rng(seed)
    records: list[dict] = []

    cal_ok = True
    for gen in CALIBRATION:
        inst = gen()
        est = poincare_lower(inst.sample(n_cal, rng))
        ok = calibration_ok(est, inst.exact)
        cal_ok = cal_ok and ok
        rec = {"kind": "calibration", "instance": inst.id, "exact": inst.exact,
               "empirical_linear_test": est,
               "rel_err": abs(est - inst.exact) / abs(inst.exact),
               "passed": ok, "note": inst.note}
        if "fem_estimate" in inst.meta:
            rec["fem_approximation"] = inst.meta["fem_estimate"]
        records.append(rec)

    records.append(_mode_leverage_reference_record())

    for gen in STRESS:
        inst = gen()
        if not cal_ok:
            records.append({"kind": "directional-diagnostic", "instance": inst.id,
                            "status": "no-diagnostic",
                            "reason": "calibration gate red", "obstruction": inst.obstruction})
            continue
        lower, conv, (la, lb) = two_seed_lower(inst, n_stress, seed + 1, seed + 2)
        if not conv:
            records.append({"kind": "directional-diagnostic", "instance": inst.id,
                            "status": "no-diagnostic",
                            "reason": "two-seed agreement gate red",
                            "estimate_a": la, "estimate_b": lb,
                            "obstruction": inst.obstruction})
            continue
        bulk_comparison = compare_directional(
            "C_P <= bulk_bound (tail-free proposal)", inst.id, inst.bulk_bound, lower,
            note="raw MCMC covariance comparison; not a certified refutation",
        )
        prior_comparison = compare_directional(
            "C_P <= prior_bound = lambda_max(Sigma0)", inst.id, inst.prior_bound, lower,
            note="the prior theorem is used only as a sampler sanity check",
        )
        if prior_comparison.outcome == "exceeds":
            records.append({"kind": "directional-diagnostic", "instance": inst.id,
                            "status": "no-diagnostic",
                            "reason": "sanity gate red: prior bound lambda_max(Sigma0) exceeded "
                                      "by the empirical estimate",
                            "empirical_covariance_scale": lower,
                            "prior_bound": inst.prior_bound,
                            "obstruction": inst.obstruction})
            continue
        records.append({
            "kind": "directional-diagnostic", "instance": inst.id,
            "status": "directional-only", "obstruction": inst.obstruction,
            "empirical_covariance_scale": lower,
            "estimate_a": la, "estimate_b": lb,
            "bulk_bound": inst.bulk_bound, "prior_bound": inst.prior_bound,
            "bulk_comparison": bulk_comparison.dict(),
            "prior_sanity_comparison": prior_comparison.dict(),
            "note": inst.note,
        })

    return RunResult(records, config={"n_cal": n_cal, "n_stress": n_stress},
                     summary={"calibration_passed": cal_ok})


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
    checks.append(("A1 cal-gauss: empirical scale distinguishes 0.7 lambda_max",
                   lower > 0.7 * g.exact * 1.1))
    checks.append(("A1 cal-gauss: empirical scale distinguishes 0.01",
                   lower > 0.01 * 1.1))
    checks.append(("A1 cal-gauss: empirical scale is near lambda_max",
                   abs(lower - g.exact) <= 0.05 * g.exact))
    return checks
