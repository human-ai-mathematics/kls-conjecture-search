"""A5 — quotient & reparameterization. Obstruction: obs:symmetry-vs-physical.

  * cal-neal-ncp     : Neal non-centered (u,z) is a product Gaussian, so by tensorization
                       C_P = max{s^2, 1} EXACTLY (verified by the 1D FEM factors).
  * stress-folded-well: mu_a = 1/2 N(-a,s^2)+1/2 N(a,s^2); raw C_P ~ e^{a^2/2s^2} (symmetry-induced
                       slow mode) but the folded (quotient) C_P = O(s^2). Ratio is exponential.
  * stress-neal-funnel: centered C_P >= Var(theta_j) = e^{2 s^2} -> inf vs non-centered max{s^2,1}
                       (the centered<->non-centered map is only one-way Lipschitz, lem:a5-lipschitz).
"""
from __future__ import annotations

import numpy as np

from ..constants import poincare_1d_fem
from ..verdict import falsify, matches

OBSTRUCTION = "obs:symmetry-vs-physical"


# ---- calibration: Neal non-centered C_P = max{s^2,1} (tensorization) -----------

def neal_ncp_factors(s: float = 1.5):
    cu = poincare_1d_fem(lambda u: u ** 2 / (2 * s ** 2), np.linspace(-12 * s, 12 * s, 2001))
    cz = poincare_1d_fem(lambda z: z ** 2 / 2.0, np.linspace(-12.0, 12.0, 2001))
    return cu, cz, max(s ** 2, 1.0)


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
    """A sound C_P lower bound for the CENTERED funnel: Var(theta_j) = E[e^{2u}] = e^{2 s^2}
    (theta_j = e^u z, u~N(0,s^2), z~N(0,1)); the linear test on theta_j certifies C_P >= e^{2 s^2}."""
    return float(np.exp(2 * s ** 2))


# ---- run + selftest ------------------------------------------------------------

def run_records(seed: int = 0):
    records = []
    cal_ok = True

    for s in (0.7, 1.5):
        cu, cz, exact = neal_ncp_factors(s)
        got = max(cu, cz)
        v = matches("cal-neal-ncp", "C_P(non-centered) == max{s^2,1} (tensorization)", got, exact, rel_tol=0.03)
        cal_ok = cal_ok and v.status == "match"
        records.append({"kind": "calibration", "instance": "cal-neal-ncp", "s": s,
                        "C_P_u": cu, "C_P_z": cz, "C_P_product": got, "exact": exact, "verdict": v.dict()})

    for a in (2.0, 3.0):
        s = 1.0
        raw, folded = folded_well(a, s)
        ratio = raw / folded
        predicted = np.exp(a ** 2 / (2 * s ** 2))
        records.append({"kind": "stress", "instance": "stress-folded-well", "obstruction": OBSTRUCTION,
                        "a": a, "sigma": s, "C_P_raw": raw, "C_P_folded": folded,
                        "ratio_raw_over_folded": ratio, "predicted_exp_barrier": float(predicted),
                        "quotient_helps": bool(ratio > 0.3 * predicted),
                        "folded_is_O_sigma2": bool(folded < 5 * s ** 2),
                        "note": "raw C_P ~ e^{a^2/2s^2} (symmetry slow mode); folded O(s^2)."})

    for s in (1.5, 2.0):
        centered_lb = neal_funnel_centered_lower(s)
        ncp = max(s ** 2, 1.0)
        v = falsify("centered C_P <= 10*max{s^2,1}", "stress-neal-funnel", 10 * ncp, centered_lb,
                    note="centered C_P >= e^{2 s^2} >> non-centered; funnel geometry (one-way Lipschitz)")
        records.append({"kind": "stress", "instance": "stress-neal-funnel", "obstruction": OBSTRUCTION,
                        "s": s, "C_P_centered_lower": centered_lb, "C_P_noncentered": ncp,
                        "verdict": v.dict(),
                        "note": "centered ~ inf (e^{2 s^2}) vs non-centered max{s^2,1}."})
    return records, {"calibration_passed": cal_ok}


def selftest(rng):
    checks = []
    for s in (0.7, 1.5):
        cu, cz, exact = neal_ncp_factors(s)
        checks.append((f"A5 cal-neal-ncp s={s}: max(C_P_u,C_P_z) == max(s^2,1) ({max(cu,cz):.3f} vs {exact:.3f})",
                       abs(max(cu, cz) - exact) <= 0.03 * exact))
    raw, folded = folded_well(3.0, 1.0)
    checks.append((f"A5 stress-folded-well a=3: raw >> folded ({raw:.1f} vs {folded:.2f}), folded=O(s^2)",
                   raw > 10 * folded and folded < 5.0))
    return checks
