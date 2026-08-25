"""Part III (KLS) route-gating — focused & self-contained (NO localization SDE engine).

KLS asserts a universal K with C_P(mu) <= K * lambda_max(Cov_mu) for EVERY isotropic log-concave
mu (= the A1-bis bridge, ledger node ``kls/conj:kls``). The SDE-free numerical signal here is a
finite-domain FEM estimate of **K = C_P / lambda_max(Cov)** on isotropic log-concave test
geometries, plus a rank-one bridge sanity check. Each 1D factor's C_P is approximated by FEM
(calibrated on the Gaussian); products use tensorization at the discretized-factor level.

This calibrates the route-agnostic analytic facts stated in the Part III manuscript:
  * exact isotropic linear test: lambda_max(Cov) = 1 implies every universal KLS bound has K>=1;
  * K = O(1) across this small battery, including single-coordinate Gaussian inflation, is
    directional non-refutation of the bridge. It does not test the cut-specific dynamic
    obstruction ``obs:rank-one-refuted``.
The localization quantities (source occupation for q:upgrade, q:alignment, weighted Stein) live in the companion
target `kls-loc` (finum/targets/kls_localization.py) on top of finum.localization — see
experiments/README.md.
"""
from __future__ import annotations

import numpy as np

from ..constants import poincare_1d_fem
from ..verdict import compare_directional, falsify, matches

K_O1_CEILING = 5.0   # "O(1)" ceiling for the realized K on these benign geometries


# ---- 1D factors: (C_P via FEM, variance) ---------------------------------------

def gauss_factor(var: float = 1.0):
    s = np.sqrt(var)
    cp = poincare_1d_fem(lambda x: x ** 2 / (2 * var), np.linspace(-12 * s, 12 * s, 2001))
    return float(cp), float(var)


def laplace_factor_unit():
    """Laplace e^{-|x|/b} scaled to unit variance (var=2b^2=1 => b=1/sqrt2); C_P=4b^2=2."""
    b = 1.0 / np.sqrt(2.0)
    cp = poincare_1d_fem(lambda x: np.abs(x) / b, np.linspace(-30 * b, 30 * b, 4001))
    return float(cp), float(2 * b ** 2)


def uniform_factor_unit():
    """Uniform[-h,h] scaled to unit variance (var=h^2/3=1 => h=sqrt3); C_P=4h^2/pi^2."""
    h = np.sqrt(3.0)
    cp = poincare_1d_fem(lambda x: np.zeros_like(x), np.linspace(-h, h, 4001))
    return float(cp), float(h ** 2 / 3.0)


def geometry_K(factors):
    """factors: list of (C_P_i, var_i). Returns (C_P, lambda_max_cov, K) as python floats."""
    C_P = float(max(c for c, _ in factors))   # tensorization
    lam = float(max(v for _, v in factors))
    return C_P, lam, C_P / lam


# ---- run + selftest ------------------------------------------------------------

def run_records(seed: int = 0, d: int = 4):
    records = []
    cal_ok = True

    # calibration: the Gaussian factor C_P must be 1 (FEM correctness; the K-denominator anchor)
    cp_g, _ = gauss_factor(1.0)
    vcal = matches("cal-kls-gauss", "C_P(N(0,1)) == 1 (FEM)", cp_g, 1.0, rel_tol=0.03)
    cal_ok = cal_ok and vcal.status == "match"
    records.append({"kind": "calibration", "instance": "cal-kls-gauss",
                    "C_P": cp_g, "exact": 1.0, "verdict": vcal.dict()})

    # isotropic log-concave test geometries: realized K = C_P / lambda_max(Cov)
    geoms = {
        "gauss-iso": [gauss_factor(1.0)] * d,
        "laplace-iso": [laplace_factor_unit()] * d,
        "uniform-iso": [uniform_factor_unit()] * d,
    }
    Ks = []
    for name, fac in geoms.items():
        C_P, lam, K = geometry_K(fac)
        Ks.append(K)
        records.append({"kind": "geometry", "instance": name, "C_P": C_P,
                        "lambda_max_cov": lam, "realized_K": K,
                        "isotropic": bool(abs(lam - 1.0) < 1e-6)})

    # Rank-one bridge sanity: one Gaussian coordinate has variance Lambda.
    # C_P = max = Lambda, lambda_max = Lambda => K = 1. This is not a cut/source-budget test.
    for Lam in (10.0, 100.0, 1000.0):
        fac = [gauss_factor(Lam)] + [gauss_factor(1.0)] * (d - 1)
        C_P, lam, K = geometry_K(fac)
        Ks.append(K)
        records.append({"kind": "geometry", "instance": "rank-one-bridge-sanity",
                        "Lambda": Lam, "C_P": C_P, "lambda_max_cov": lam, "realized_K": K,
                        "note": "Gaussian tensorization sanity only; no cut or dynamic source is tested."})

    K_max = max(Ks)
    # Directional signal only: this finite benign battery does not refute the KLS / A1-bis bridge.
    v_bridge = compare_directional(
        "FEM K estimate <= K_O1_CEILING", "kls-bridge", K_O1_CEILING, K_max,
        note="finite-domain FEM battery; directional comparison only",
    )
    # verdict 2: isotropic linear-test refuter — lambda_max(Cov)=1 kills any sub-1 upper claim
    v_refuter = falsify("KLS upper bound C_P <= 0.5 (too small)", "kls-isotropic", 0.5, 1.0,
                        note="universal lower bound C_P >= lambda_max(Cov) = 1 for isotropic mu")
    records.append({"kind": "analytic-verdict-and-directional-diagnostic",
                    "estimated_K_max_fem": K_max,
                    "bridge_directionally_within_ceiling":
                        bool(v_bridge.status == "directional-consistent"),
                    "verdict_bridge": v_bridge.dict(), "verdict_isotropic_refuter": v_refuter.dict(),
                    "companion": "localization quantities (q:upgrade source, q:alignment, weighted Stein) "
                                 "=> target 'kls-loc' on finum.localization; see experiments/README.md"})
    return records, {"d": d, "calibration_passed": cal_ok, "realized_K_max": K_max}


def selftest(rng):
    checks = []
    cp_g, _ = gauss_factor(1.0)
    checks.append((f"KLS cal: C_P(N(0,1)) == 1 (FEM) ({cp_g:.4f})", abs(cp_g - 1.0) <= 0.03))
    # rank-one: K == 1 independent of inflation
    Ks = []
    for Lam in (10.0, 1000.0):
        fac = [gauss_factor(Lam)] + [gauss_factor(1.0)] * 3
        _, _, K = geometry_K(fac)
        Ks.append(K)
    checks.append((f"KLS rank-one bridge sanity: K==1 for Lambda in (10,1000) ({Ks[0]:.3f},{Ks[1]:.3f})",
                   all(abs(k - 1.0) <= 0.05 for k in Ks)))
    # all benign isotropic geometries have K = O(1)
    Kgauss = geometry_K([gauss_factor(1.0)] * 4)[2]
    Klap = geometry_K([laplace_factor_unit()] * 4)[2]
    checks.append((f"KLS K=O(1): gauss K={Kgauss:.2f}, laplace K={Klap:.2f} both <= {K_O1_CEILING}",
                   Kgauss <= K_O1_CEILING and Klap <= K_O1_CEILING))
    return checks
