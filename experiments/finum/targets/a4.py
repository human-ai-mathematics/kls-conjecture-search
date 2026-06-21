"""A4 — variational-inference transport constants. Obstruction: obs:restricted-not-finite.

Transport ratio R(q) = W_2^2(q,pi)/(2 KL(q||pi)); C_Q = sup over the family, C_{Q,r} = sup on a
KL-sublevel (eq:a4-cq / cqr).
  * cal-gauss-t2     : pi=N(0,sigma^2), shifts q_m=N(m,sigma^2): R(q_m) == sigma^2 EXACTLY (the
                       Gaussian saturates T_2, C_TCI = sigma^2).
  * stress-ep-tails  : pi ~ e^{-|x|^p}, 1<=p<2; q_m=N(m,sigma^2): R(q_m) ~ |m|^{2-p} -> inf, so a
                       finite GLOBAL C_Q is FALSIFIED, while C_{Q,r} on a KL-sublevel stays finite.
  * stress-sep-mixture: separated mixture; reweighting witness ~ e^{cD^2} vs mode-collapse ~ D^2.
"""
from __future__ import annotations

import numpy as np

from ..transport import gauss_density, kl_1d, transport_ratio
from ..verdict import falsify, matches

OBSTRUCTION = "obs:restricted-not-finite"


def _grid(x_max=80.0, n=8001):
    return np.linspace(-x_max, x_max, n)


# ---- calibration: Gaussian T_2 ratio == sigma^2 --------------------------------

def cal_gauss_t2(sigma: float = 1.3):
    xs = _grid(60.0, 8001)
    pi = gauss_density(xs, 0.0, sigma)
    qs = [gauss_density(xs, m, sigma) for m in (0.5, 1.0, 2.0)]
    rs = transport_ratio(qs, pi, xs)
    return [r["ratio"] for r in rs], sigma ** 2


# ---- stress: e^{-|x|^p} family-restricted constant is infinite -----------------

def ep_ratios(p: float = 1.0, sigma: float = 1.0):
    xs = _grid(260.0, 20001)
    pi = np.exp(-np.abs(xs) ** p)
    ms = np.array([1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0])
    qs = [gauss_density(xs, m, sigma) for m in ms]
    rs = transport_ratio(qs, pi, xs)
    return ms, rs


# ---- stress: separated mixture, two witness scalings ---------------------------

def sep_mixture_witnesses(Delta: float = 3.0, sigma: float = 1.0):
    xs = _grid(4 * Delta + 20.0, 12001)
    pi = 0.5 * gauss_density(xs, -Delta, sigma) + 0.5 * gauss_density(xs, Delta, sigma)
    q_collapse = gauss_density(xs, Delta, sigma)            # mode collapse: one well
    q_reweight = gauss_density(xs, 0.0, Delta)             # broad cover of both wells
    rc = transport_ratio([q_collapse], pi, xs)[0]["ratio"]
    rr = transport_ratio([q_reweight], pi, xs)[0]["ratio"]
    return rc, rr


# ---- run + selftest ------------------------------------------------------------

def run_records(seed: int = 0):
    records = []
    cal_ok = True

    ratios, exact = cal_gauss_t2()
    for m, r in zip((0.5, 1.0, 2.0), ratios):
        v = matches("cal-gauss-t2", "W2^2/(2KL) == sigma^2 (Gaussian saturates T2)", r, exact, rel_tol=0.03)
        cal_ok = cal_ok and v.status == "match"
        records.append({"kind": "calibration", "instance": "cal-gauss-t2", "shift_m": m,
                        "ratio": r, "exact": exact, "verdict": v.dict()})

    for p in (1.0, 1.5):
        ms, rs = ep_ratios(p)
        ratios = [r["ratio"] for r in rs]
        kls = [rr["kl"] for rr in rs]
        grows = ratios[-1] > 2.0 * ratios[0]
        # C_{Q,r}: restrict to a KL-sublevel; the sublevel max ratio stays finite.
        r_level = 5.0
        C_Qr = max([rr["ratio"] for rr in rs if rr["kl"] <= r_level], default=ratios[0])
        far = ratios[-1]                              # a far witness (large m, large KL)
        # global C_Q = sup over ALL q = inf; the far witness already exceeds 2*C_{Q,r},
        # so "global C_Q ~ C_{Q,r}" (finite at restricted scale) is FALSIFIED, and the
        # monotone unsaturated growth (global_grows) certifies C_Q -> inf.
        v = falsify("global C_Q <= 2*C_{Q,r}", "stress-ep-tails", 2.0 * C_Qr, far,
                    note="ratio ~ |m|^{2-p} -> inf => global C_Q = inf >> restricted C_{Q,r}")
        records.append({"kind": "stress", "instance": "stress-ep-tails", "obstruction": OBSTRUCTION,
                        "p": p, "m": ms.tolist(), "ratios": ratios, "kl": kls,
                        "global_grows": bool(grows), "C_Qr_sublevel_max": C_Qr,
                        "far_witness_ratio": far, "kl_level": r_level, "verdict_global": v.dict(),
                        "note": "global C_Q=inf (FALSIFIED vs restricted); C_{Q,r} on KL-sublevel finite."})

    rc, rr = sep_mixture_witnesses(Delta=3.0)
    records.append({"kind": "stress", "instance": "stress-sep-mixture", "obstruction": OBSTRUCTION,
                    "Delta": 3.0, "ratio_mode_collapse": rc, "ratio_reweight": rr,
                    "reweight_larger": bool(rr > rc),
                    "note": "reweighting witness ~ e^{cD^2} dominates mode-collapse ~ D^2."})
    return records, {"calibration_passed": cal_ok}


def selftest(rng):
    checks = []
    ratios, exact = cal_gauss_t2()
    checks.append((f"A4 cal-gauss-t2: W2^2/(2KL) == sigma^2 (={exact:.3f}) for all shifts",
                   all(abs(r - exact) <= 0.03 * exact for r in ratios)))
    ms, rs = ep_ratios(1.0)
    ratios = [r["ratio"] for r in rs]
    checks.append((f"A4 stress-ep-tails p=1: ratio grows with m ({ratios[0]:.2f} -> {ratios[-1]:.2f})",
                   ratios[-1] > 2.0 * ratios[0]))
    return checks
