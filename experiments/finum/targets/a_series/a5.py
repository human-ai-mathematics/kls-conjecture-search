"""A5 — quotient & reparameterization directional diagnostics.

  * cal-neal-ncp     : Neal non-centered (u,z) is a product Gaussian, so by tensorization
                       C_P = max{s^2, 1} EXACTLY (verified by the 1D FEM factors).
  * stress-folded-well: mu_a = 1/2 N(-a,s^2)+1/2 N(a,s^2); the open asymptotic target asks for
                       log(C_P/s^2)=a^2/(2s^2)+O(log(1+a/s)) and folded C_P of order s^2.
  * stress-neal-funnel: Var(theta_j)=e^{2s^2} is a finite linear-test lower bound for fixed s.
                       The proved analytic tail argument gives centered C_P=infinity; both
                       directions of the centered/non-centered map fail to be globally Lipschitz.
  * cal-partial-ncp : exact scalar Gaussian partial noncentring, alpha*=1/(1+rB).
  * cal-orbit-height: distinguishes the easiest pairwise edge from the orbit-connectivity height.
"""
from __future__ import annotations

import numpy as np

from ...contract import RunResult
from ...constants import poincare_1d_fem
from ...comparison import matches

SYMMETRY_OBSTRUCTION = "obs:symmetry-vs-physical"
FUNNEL_OBSTRUCTION = "obs:heavy-tail-no-classical"


# ---- calibration: Neal non-centered C_P = max{s^2,1} (tensorization) -----------

def neal_ncp_factors(s: float = 1.5):
    cu = poincare_1d_fem(lambda u: u ** 2 / (2 * s ** 2), np.linspace(-12 * s, 12 * s, 2001))
    cz = poincare_1d_fem(lambda z: z ** 2 / 2.0, np.linspace(-12.0, 12.0, 2001))
    return cu, cz, max(s ** 2, 1.0)


# ---- calibration: exact scalar partial noncentring ----------------------------

def partial_noncentering_precision(A: float, B: float, r: float, alpha: float) -> np.ndarray:
    """Posterior precision in ``(u, z_alpha=theta-alpha*u)`` coordinates."""
    if A <= 0.0 or B <= 0.0 or r < 0.0:
        raise ValueError("A and B must be positive and r must be nonnegative")
    off_diagonal = -(1.0 - alpha) / B + r * alpha
    return np.array([
        [1.0 / A + (1.0 - alpha) ** 2 / B + r * alpha ** 2, off_diagonal],
        [off_diagonal, 1.0 / B + r],
    ])


def gaussian_precision_objectives(precision: np.ndarray) -> tuple[float, float]:
    """Return exact ``(C_P, condition number)`` for a Gaussian precision."""
    eigenvalues = np.linalg.eigvalsh(np.asarray(precision, dtype=float))
    if eigenvalues[0] <= 0.0:
        raise ValueError("precision must be positive definite")
    return float(1.0 / eigenvalues[0]), float(eigenvalues[-1] / eigenvalues[0])


def partial_noncentering_optimum(A: float, B: float, r: float) -> dict:
    """Exact optimum shared by Gaussian ``C_P`` and its spectral condition number."""
    if A <= 0.0 or B <= 0.0 or r < 0.0:
        raise ValueError("A and B must be positive and r must be nonnegative")
    alpha = 1.0 / (1.0 + r * B)
    precision = partial_noncentering_precision(A, B, r, alpha)
    cp, condition = gaussian_precision_objectives(precision)
    return {"alpha": alpha, "precision": precision, "C_P": cp, "kappa_P": condition}


# ---- calibration: connectivity rather than the easiest orbit edge ------------

def orbit_connectivity_height(pair_heights: np.ndarray) -> dict:
    """Connectivity threshold of a finite symmetric pair-height matrix.

    This is a diagnostic for the exact finite-graph definition, not a posterior metastability
    estimator.  Diagonal entries are ignored.
    """
    heights = np.asarray(pair_heights, dtype=float)
    if heights.ndim != 2 or heights.shape[0] != heights.shape[1] or heights.shape[0] < 2:
        raise ValueError("pair_heights must be a square matrix of size at least two")
    if not np.allclose(heights, heights.T):
        raise ValueError("pair_heights must be symmetric")
    number = heights.shape[0]
    off_diagonal = heights[~np.eye(number, dtype=bool)]
    if np.any(np.isnan(off_diagonal)):
        raise ValueError("off-diagonal heights cannot be NaN")
    if np.any(off_diagonal < 0.0):
        raise ValueError("off-diagonal heights must be nonnegative")
    candidates = np.unique(off_diagonal[np.isfinite(off_diagonal)])

    for threshold in candidates:
        reached = {0}
        frontier = [0]
        while frontier:
            node = frontier.pop()
            neighbours = np.flatnonzero(np.isfinite(heights[node]) & (heights[node] <= threshold))
            for neighbour in neighbours:
                neighbour = int(neighbour)
                if neighbour not in reached:
                    reached.add(neighbour)
                    frontier.append(neighbour)
        if len(reached) == number:
            return {
                "easiest_pair": float(np.min(off_diagonal)),
                "connectivity_height": float(threshold),
            }
    raise ValueError("the finite-height orbit graph is disconnected")


# ---- stress: folded double well (raw vs quotient) ------------------------------

def folded_well(a: float = 3.0, s: float = 1.0):
    """Raw C_P of the symmetric double well vs the folded (|x|) quotient C_P."""
    def mu(x):
        return 0.5 * (np.exp(-0.5 * ((x + a) / s) ** 2) + np.exp(-0.5 * ((x - a) / s) ** 2))
    U = lambda x: -np.log(mu(x))
    half = a + 8 * s
    raw = poincare_1d_fem(U, np.linspace(-half, half, 4001))
    folded = poincare_1d_fem(U, np.linspace(1e-6, half, 3001))   # |x| domain [0, inf)
    return raw, folded


# ---- stress: Neal funnel centered (inf) vs non-centered ------------------------

def neal_funnel_centered_lower(s: float = 1.5) -> float:
    """Finite linear-test lower bound for fixed ``s``: C_P >= Var(theta_j) = exp(2s^2).

    This variance is not infinite. The analytic C_P=infinity conclusion instead uses the lack of
    exponential moments of the centered coordinate and is not established by this number.
    """
    return float(np.exp(2 * s ** 2))


# ---- run + selftest ------------------------------------------------------------

def _partial_connectivity_reference_records() -> list[dict]:
    """Exact scalar partial-noncentring and finite-graph calibrations."""
    A = B = r = 1.0
    partial = partial_noncentering_optimum(A, B, r)
    centered = gaussian_precision_objectives(
        partial_noncentering_precision(A, B, r, 0.0)
    )
    noncentered = gaussian_precision_objectives(
        partial_noncentering_precision(A, B, r, 1.0)
    )
    heights = np.array([
        [0.0, 2.0, 1.0, 2.0],
        [2.0, 0.0, 2.0, 1.0],
        [1.0, 2.0, 0.0, 2.0],
        [2.0, 1.0, 2.0, 0.0],
    ])
    return [
        {
            "kind": "analytic-result",
            "instance": "partial-noncentering-reference",
            "ledger_node": "prop:a5-partial-gaussian",
            "theorem_status": "proved",
            "A": A, "B": B, "r": r,
            "alpha_opt": partial["alpha"],
            "precision_opt": partial["precision"].tolist(),
            "C_P_opt": partial["C_P"],
            "kappa_P_opt": partial["kappa_P"],
            "centered_C_P": centered[0], "centered_kappa_P": centered[1],
            "noncentered_C_P": noncentered[0],
            "noncentered_kappa_P": noncentered[1],
        },
        {
            "kind": "analytic-calibration",
            "instance": "orbit-connectivity-reference",
            "definition_status": "exact",
            **orbit_connectivity_height(heights),
        },
    ]


def run_records(seed: int = 0):
    records = []
    cal_ok = True

    for s in (0.7, 1.5):
        cu, cz, exact = neal_ncp_factors(s)
        got = max(cu, cz)
        v = matches("cal-neal-ncp", "C_P(non-centered) == max{s^2,1} (tensorization)", got, exact, rel_tol=0.03)
        cal_ok = cal_ok and v.outcome == "match"
        records.append({"kind": "calibration", "instance": "cal-neal-ncp", "s": s,
                        "C_P_u_fem": cu, "C_P_z_fem": cz,
                        "C_P_product_fem": got, "exact_C_P": exact,
                        "comparison": v.dict()})

    records.extend(_partial_connectivity_reference_records())

    if cal_ok:
        for a in (2.0, 3.0):
            s = 1.0
            raw, folded = folded_well(a, s)
            ratio = raw / folded
            leading_log_rate = a ** 2 / (2 * s ** 2)
            log_rate_residual = np.log(raw / s ** 2) - leading_log_rate
            records.append({"kind": "directional-diagnostic",
                            "instance": "stress-folded-well",
                            "status": "directional-only",
                            "obstruction": SYMMETRY_OBSTRUCTION,
                            "a": a, "sigma": s,
                            "C_P_raw_fem": raw, "C_P_folded_fem": folded,
                            "ratio_raw_over_folded_fem": ratio,
                            "leading_log_rate": float(leading_log_rate),
                            "log_rate_residual": float(log_rate_residual),
                            "folded_over_sigma2": float(folded / s ** 2),
                            "note": "Finite-domain FEM estimates only. The open folding target "
                                    "still requires certified asymptotic bounds."})
    else:
        records.append({"kind": "directional-diagnostic", "instance": "stress-folded-well",
                        "status": "no-diagnostic", "reason": "calibration gate red"})

    for s in (1.5, 2.0):
        centered_lb = neal_funnel_centered_lower(s)
        ncp = max(s ** 2, 1.0)
        records.append({"kind": "analytic-result", "instance": "stress-neal-funnel",
                        "obstruction": FUNNEL_OBSTRUCTION,
                        "ledger_nodes": ["lem:a5-pi-exp-tail", "ex:a5-neal"],
                        "theorem_status": "proved", "s": s,
                        "centered_C_P": "infinity",
                        "centered_finite_linear_test_lower": centered_lb,
                        "noncentered_C_P": ncp,
                        "map_globally_lipschitz": False,
                        "inverse_map_globally_lipschitz": False,
                        "note": "The finite variance witness does not prove infinity; the proved "
                                "exponential-integrability argument does."})
    return RunResult(records, summary={"calibration_passed": cal_ok,
                                       "fem_diagnostics_gated": bool(cal_ok)})


def selftest(rng):
    checks = []
    for s in (0.7, 1.5):
        cu, cz, exact = neal_ncp_factors(s)
        checks.append((f"A5 cal-neal-ncp s={s}: max(C_P_u,C_P_z) == max(s^2,1) ({max(cu,cz):.3f} vs {exact:.3f})",
                       abs(max(cu, cz) - exact) <= 0.03 * exact))
    raw, folded = folded_well(3.0, 1.0)
    checks.append((f"A5 stress-folded-well a=3: raw >> folded ({raw:.1f} vs {folded:.2f}), folded=O(s^2)",
                   raw > 10 * folded and folded < 5.0))
    partial = partial_noncentering_optimum(1.0, 1.0, 1.0)
    centered_cp, centered_kappa = gaussian_precision_objectives(
        partial_noncentering_precision(1.0, 1.0, 1.0, 0.0)
    )
    checks.append(("A5 cal-partial-ncp: alpha*=1/2 strictly improves both tied endpoints at rB=1",
                   abs(partial["alpha"] - 0.5) <= 1e-12
                   and partial["C_P"] < centered_cp
                   and partial["kappa_P"] < centered_kappa))
    z4_heights = np.array([
        [0.0, 2.0, 1.0, 2.0],
        [2.0, 0.0, 2.0, 1.0],
        [1.0, 2.0, 0.0, 2.0],
        [2.0, 1.0, 2.0, 0.0],
    ])
    orbit = orbit_connectivity_height(z4_heights)
    checks.append(("A5 cal-orbit-height: easiest Z4 edge 1 does not connect orbit; Gamma_conn=2",
                   orbit["easiest_pair"] == 1.0 and orbit["connectivity_height"] == 2.0))
    return checks
