"""A4 — variational-inference transport diagnostics and exact local calibrations.

Transport ratio R(q) = W_2^2(q,pi)/(2 KL(q||pi)); C_Q = sup over the family, C_{Q,r} = sup on a
KL-sublevel (eq:a4-cq / cqr).
  * cal-gauss-t2     : pi=N(0,sigma^2), shifts q_m=N(m,sigma^2): R(q_m) == sigma^2 EXACTLY (the
                       Gaussian saturates T_2, C_TCI = sigma^2).
  * stress-ep-tails  : pi ~ e^{-|x|^p}, 1<=p<2; q_m=N(m,sigma^2): R(q_m) ~ |m|^{2-p} -> inf, so a
                       finite global C_Q fails analytically. The finite grid records only
                       directional lower witnesses; it does not estimate an upper constant.
  * stress-sep-mixture: separated mixture; an epsilon-reweighted copy of the target probes the
                        metastable small-weight mode, while a component Gaussian probes mode collapse.
  * cal-gauss-local  : exact localized constants for a fixed-covariance Gaussian location family;
                       separates the misspecification baseline from optimizer-centred excess KL.
"""
from __future__ import annotations

import numpy as np

from ...contract import RunResult
from ...transport import gauss_density, kl_1d, transport_ratio
from ...comparison import matches

TAIL_OBSTRUCTION = "obs:restricted-not-finite"
SYMMETRY_OBSTRUCTION = "obs:symmetry-vs-physical"


def _grid(x_max=80.0, n=8001):
    return np.linspace(-x_max, x_max, n)


# ---- calibration: Gaussian T_2 ratio == sigma^2 --------------------------------

def cal_gauss_t2(sigma: float = 1.3):
    xs = _grid(60.0, 8001)
    pi = gauss_density(xs, 0.0, sigma)
    qs = [gauss_density(xs, m, sigma) for m in (0.5, 1.0, 2.0)]
    rs = transport_ratio(qs, pi, xs)
    return [r["ratio"] for r in rs], sigma ** 2


def _as_spd(matrix: np.ndarray, name: str) -> np.ndarray:
    matrix = np.asarray(matrix, dtype=float)
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError(f"{name} must be a square matrix")
    matrix = 0.5 * (matrix + matrix.T)
    if np.min(np.linalg.eigvalsh(matrix)) <= 0.0:
        raise ValueError(f"{name} must be positive definite")
    return matrix


def _sqrt_spd(matrix: np.ndarray) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    return (eigenvectors * np.sqrt(eigenvalues)) @ eigenvectors.T


def gaussian_fixed_cov_local(Sigma: np.ndarray, S: np.ndarray, rho: float) -> dict:
    """Exact A4 constants for ``q_m=N(mu+m,S)`` and ``pi=N(mu,Sigma)``.

    ``rho`` is the excess above the variational gap.  The returned raw constants use the
    localized sublevel ``KL <= delta + rho``.  The excess constants are optimizer-centred and
    therefore only defined for a positive radius.
    """
    if rho < 0.0:
        raise ValueError("rho must be nonnegative")
    Sigma = _as_spd(Sigma, "Sigma")
    S = _as_spd(S, "S")
    if Sigma.shape != S.shape:
        raise ValueError("Sigma and S must have the same shape")

    dimension = Sigma.shape[0]
    inverse_sigma = np.linalg.inv(Sigma)
    _, logdet_sigma = np.linalg.slogdet(Sigma)
    _, logdet_s = np.linalg.slogdet(S)
    delta = 0.5 * (np.trace(inverse_sigma @ S) - dimension + logdet_sigma - logdet_s)

    sqrt_sigma = _sqrt_spd(Sigma)
    middle = sqrt_sigma @ S @ sqrt_sigma
    covariance_w2 = float(np.trace(S + Sigma - 2.0 * _sqrt_spd(middle)))
    delta = float(max(delta, 0.0))
    covariance_w2 = float(max(covariance_w2, 0.0))
    lambda_max = float(np.max(np.linalg.eigvalsh(Sigma)))

    well_specified = delta <= 1e-12 and covariance_w2 <= 1e-12
    if well_specified:
        raw_transport = lambda_max if rho > 0.0 else float("nan")
        raw_mean = lambda_max if rho > 0.0 else float("nan")
        baseline = float("nan")
        endpoint = lambda_max if rho > 0.0 else float("nan")
    else:
        baseline = covariance_w2 / (2.0 * delta)
        endpoint = (covariance_w2 + 2.0 * rho * lambda_max) / (2.0 * (delta + rho))
        raw_transport = max(baseline, endpoint)
        raw_mean = lambda_max * rho / (delta + rho)

    excess = lambda_max if rho > 0.0 else float("nan")
    return {
        "delta": delta,
        "covariance_w2": covariance_w2,
        "lambda_max": lambda_max,
        "well_specified": well_specified,
        "raw_transport": float(raw_transport),
        "raw_mean": float(raw_mean),
        "baseline_transport": float(baseline),
        "endpoint_transport": float(endpoint),
        "excess_transport": float(excess),
        "excess_mean": float(excess),
    }


# ---- stress: e^{-|x|^p} family-restricted constant is infinite -----------------

def ep_ratios(p: float = 1.0, sigma: float = 1.0):
    xs = _grid(260.0, 20001)
    pi = np.exp(-np.abs(xs) ** p)
    ms = np.array([1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0])
    qs = [gauss_density(xs, m, sigma) for m in ms]
    rs = transport_ratio(qs, pi, xs)
    return ms, rs


# ---- stress: separated mixture, two witness scalings ---------------------------

def sep_mixture_witnesses(
    a: float = 3.0,
    sigma: float = 1.0,
    epsilons: np.ndarray | None = None,
):
    """Compare mode collapse with genuine component-weight perturbations.

    The component means are ``-a`` and ``+a`` (so their separation is ``2*a``).
    Each ``q_reweight`` genuinely changes the component weights.
    """
    if a <= 0.0 or sigma <= 0.0:
        raise ValueError("a and sigma must be positive")
    xs = _grid(4 * a + 20.0, 12001)
    left = gauss_density(xs, -a, sigma)
    right = gauss_density(xs, a, sigma)
    pi = 0.5 * left + 0.5 * right
    q_collapse = right                                      # mode collapse: one well
    if epsilons is None:
        epsilons = np.geomspace(1e-3, 0.25, 16)
    epsilons = np.asarray(epsilons, dtype=float)
    if epsilons.ndim != 1 or np.any(epsilons <= 0.0) or np.any(epsilons >= 0.5):
        raise ValueError("epsilons must be a one-dimensional array with entries in (0, 1/2)")
    q_reweights = [(0.5 + eps) * left + (0.5 - eps) * right for eps in epsilons]
    rc = transport_ratio([q_collapse], pi, xs)[0]["ratio"]
    reweight_records = transport_ratio(q_reweights, pi, xs)
    for eps, record in zip(epsilons, reweight_records):
        record["epsilon"] = float(eps)
    return rc, reweight_records


# ---- run + selftest ------------------------------------------------------------

def _gaussian_local_reference_records() -> list[dict]:
    """Exact well-specified and misspecified Gaussian location calibrations."""
    Sigma = np.array([[2.0, 0.4], [0.4, 1.0]])
    cases = (
        ("gaussian-local-wellspecified", Sigma),
        ("gaussian-local-misspecified", np.array([[1.4, 0.2], [0.2, 0.7]])),
    )
    records = []
    for instance, fixed_covariance in cases:
        result = gaussian_fixed_cov_local(Sigma, fixed_covariance, rho=0.35)
        serializable_result = {
            key: None if isinstance(value, float) and not np.isfinite(value) else value
            for key, value in result.items()
        }
        records.append({
            "kind": "analytic-result",
            "instance": instance,
            "ledger_nodes": [
                "prop:a4-local-wellspecified" if result["well_specified"]
                else "prop:a4-local-misspecified",
                "prop:a4-local-excess",
                "ex:a4-gaussian-local",
            ],
            "theorem_status": "proved",
            **serializable_result,
        })
    return records


def run_records(seed: int = 0):
    records = []
    cal_ok = True

    ratios, exact = cal_gauss_t2()
    for m, r in zip((0.5, 1.0, 2.0), ratios):
        v = matches("cal-gauss-t2", "W2^2/(2KL) == sigma^2 (Gaussian saturates T2)", r, exact, rel_tol=0.03)
        cal_ok = cal_ok and v.outcome == "match"
        records.append({"kind": "calibration", "instance": "cal-gauss-t2", "shift_m": m,
                        "ratio": r, "exact": exact, "comparison": v.dict()})

    records.extend(_gaussian_local_reference_records())

    if not cal_ok:
        records.append({"kind": "directional-diagnostic", "instance": "a4-grid-battery",
                        "status": "no-diagnostic", "reason": "calibration gate red"})
        return RunResult(records, summary={"calibration_passed": False,
                                           "grid_diagnostics_gated": False})

    for p in (1.0, 1.5):
        ms, rs = ep_ratios(p)
        ratios = [r["ratio"] for r in rs]
        kls = [rr["kl"] for rr in rs]
        grows = ratios[-1] > 2.0 * ratios[0]
        # A finite grid supplies lower estimates only, including after filtering by KL.
        r_level = 5.0
        localized_witnesses = [rr["ratio"] for rr in rs if rr["kl"] <= r_level]
        C_Qr_grid_lower = max(localized_witnesses)
        far = ratios[-1]
        records.append({"kind": "directional-diagnostic", "instance": "stress-ep-tails",
                        "status": "directional-only", "obstruction": TAIL_OBSTRUCTION,
                        "p": p, "m": ms.tolist(), "ratios": ratios, "kl": kls,
                        "directional_ratio_growth": bool(grows),
                        "C_Qr_grid_lower": C_Qr_grid_lower,
                        "far_witness_ratio": far, "kl_level": r_level,
                        "analytic_expectation": "C_Q=infinity for p<2; localized family sublevels are finite",
                        "note": "Finite-grid lower witnesses only. They illustrate the analytic "
                                "|m|^(2-p) growth but neither certify divergence nor upper-bound C_{Q,r}."})

    a = 3.0
    rc, reweight_sweep = sep_mixture_witnesses(a=a)
    best = max(reweight_sweep, key=lambda record: record["ratio"])
    records.append({"kind": "directional-diagnostic", "instance": "stress-sep-mixture",
                    "status": "directional-only", "obstruction": SYMMETRY_OBSTRUCTION,
                    "a": a, "component_separation": 2.0 * a, "ratio_mode_collapse": rc,
                    "reweight_sweep": reweight_sweep, "ratio_reweight_max": best["ratio"],
                    "epsilon_reweight_max": best["epsilon"],
                    "directional_reweight_exceeds_collapse": bool(best["ratio"] > rc),
                    "note": "Approximate lower witnesses at centers +/-a and separation 2a. "
                            "The epsilon sweep probes a crossover; it supplies neither a matching "
                            "upper bound nor an asymptotic-in-separation conclusion."})
    return RunResult(records, summary={"calibration_passed": cal_ok,
                                       "grid_diagnostics_gated": True})


def selftest(rng):
    checks = []
    ratios, exact = cal_gauss_t2()
    checks.append((f"A4 cal-gauss-t2: W2^2/(2KL) == sigma^2 (={exact:.3f}) for all shifts",
                   all(abs(r - exact) <= 0.03 * exact for r in ratios)))
    ms, rs = ep_ratios(1.0)
    ratios = [r["ratio"] for r in rs]
    checks.append((f"A4 stress-ep-tails p=1: ratio grows with m ({ratios[0]:.2f} -> {ratios[-1]:.2f})",
                   ratios[-1] > 2.0 * ratios[0]))
    Sigma = np.array([[1.7, -0.3], [-0.3, 0.9]])
    local = gaussian_fixed_cov_local(Sigma, Sigma, rho=0.2)
    local_exact = float(np.max(np.linalg.eigvalsh(Sigma)))
    checks.append(("A4 cal-gauss-local: well-specified raw and excess constants equal lambda_max(Sigma)",
                   abs(local["raw_transport"] - local_exact) <= 1e-10
                   and abs(local["excess_transport"] - local_exact) <= 1e-10))
    return checks
