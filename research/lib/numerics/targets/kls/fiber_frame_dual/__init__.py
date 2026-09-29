"""Part III (KLS, `conditional-fiber-frame` route) — the all-frame simplex min-max, probed
through a frame LIBRARY on the fixed-degree quotient.

For the isotropic uniform simplex (X = R_m(P - 1/m), P ~ Dir(1,...,1), d = m-1,
R_m = sqrt(m(m+1))) the route's decisive finite object (probe w1f01, eq. 43) is

    Lambda_{m,k} = sup_{admissible even frames rho}
                   lambda_min( d * int B_{m,k}(theta) drho(theta),  G_{m,k} )

on the degree-<=k polynomial quotient V_{m,k}.  The route needs inf_m Lambda_{m,k} > 0 for
every fixed k; Lambda_{m,k} -> 0 at one fixed k >= 2 refutes it.

**What this target computes.**

(A) Exact root-frame degree-k gaps lambda^root_{m,k} = lambda_min(K_root, G): certified
    rational enclosures [lambda_lo, lambda_hi] (exact Bareiss/Sylvester PD test of
    K - lam G, exact rational Rayleigh upper bound), k = 2, 3.
(B) Frame-library certified LOWER bounds on Lambda_{m,k}: root orbit, vertex orbit
    (X-images of e_i - (1/m)1), rational mixtures alpha*root + (1-alpha)*vertex (the frame
    constraint is linear, so every mixture is admissible), and the uniform spherical frame
    on H_0 (floating MC with two-seed convergence gating; DIRECTIONAL only).  Every
    exactly-assembled frame gives Lambda_{m,k} >= lambda_lo via an exact PD certificate.
(C) Cap-descent probe: exact normalized quotients of the polynomial cap proxies
    f_j = P_1^j (centered), j = 2..k, per frame — a fixed-degree shadow of the vertex-cap
    indicator that analytically kills the root frame in L^2.
(D) Best rational mixture: the concave 1-parameter frame-weight optimization over the
    exactly-computable orbit union, rationalized and re-certified exactly — an exact
    certified lower bound for Lambda_{m,2} (and _{m,3}) at each computed m.

**Calibration anchors (the run ABORTS on any failure).**  Linear sector has quotient
exactly 1 for every admissible frame (exact block identity K_lin == G_lin, root and vertex,
every computed m); the radial quadratic F = |X|^2 - d has exact root quotient
(m+2)(m+3)/(5 m^2) (probe eq. 36; checked for every computed m); the closed Dirichlet-
neutrality root formula (probe eq. 29) agrees EXACTLY with the independent chord/chamber
integration machinery that is then trusted for the vertex orbit.

**What this target cannot decide** (q:conditional-fiber-frame, and the objective of the
approach that carries it in research/program/portfolio.yaml): the
all-frame gate.  Library lower bounds never bound Lambda from above; a decaying library gap
is directional evidence only; even an exact certificate is a *candidate* requiring a prover
and an independent proof-checker before any logical status changes.  No Monte Carlo enters
any exact channel; the spherical channel is sampled and explicitly directional.
"""
from __future__ import annotations

from fractions import Fraction

import numpy as np

from ....contract import RunResult, lift_observations
from ....comparison import compare_directional
from . import certify, frames, spherical

# ---- pre-registered thresholds (fixed before any run; echoed into the artifact) ---------
PREREGISTERED_THRESHOLDS = {
    "directional_against_route": (
        "gap_lib(m,2) decreases monotonically from m=4 to the largest computed m by a total "
        "factor >= 3 AND gap_lib(m_max,2) < 0.1"),
    "constructive_lead": (
        "some single frame family (root, vertex, or spherical) keeps its degree-2 gap >= 0.2 "
        "for all computed m"),
    "exact_certificate_escalation": (
        "only an exact rational witness (frame weights + PD certificate) proving "
        "Lambda_{m,2} >= c for all computed m, or an exact dual certificate proving "
        "Lambda_{m,2} <= eps_m with eps_m decreasing, is a prover-escalable candidate; "
        "neither is a status change"),
    "directional_against_factor": 3.0,
    "directional_against_top_gap": 0.1,
    "constructive_lead_gap": 0.2,
}

SPHERICAL_CONVERGENCE_REL_TOL = 0.10
SPHERICAL_SEED_OFFSET = 999983
MIXTURE_REFINE_ITERS = 24
MIXTURE_ALPHA_MAX_DENOMINATOR = 64


# =====================================================================================
# helpers
# =====================================================================================

def _floatm(M):
    return np.array([[float(v) for v in row] for row in M])


def _pencil_lambda_min(Kf, Gf):
    dsc = 1.0 / np.sqrt(np.diag(Gf))
    Ks = Kf * dsc[:, None] * dsc[None, :]
    Gs = Gf * dsc[:, None] * dsc[None, :]
    from scipy.linalg import eigh
    vals = eigh(0.5 * (Ks + Ks.T), 0.5 * (Gs + Gs.T), eigvals_only=True)
    return float(vals[0])


def _exact_quotient(K, G, c) -> Fraction:
    num = certify.quadratic_form(K, c)
    den = certify.quadratic_form(G, c)
    return num / den


def _cap_proxy_indices(m: int, k: int, basis):
    out = {}
    for j in range(2, k + 1):
        e = [0] * m
        e[0] = j
        out[j] = basis.index(tuple(e))
    return out


def _cap_proxies_exact(K, G, idxs):
    return {f"P1^{j}": {"exact": str(K[t][t] / G[t][t]), "float": float(K[t][t] / G[t][t])}
            for j, t in idxs.items()}


def _assert_anchor(ok: bool, label: str):
    if not ok:
        raise RuntimeError(f"calibration anchor failed, run aborted: {label}")


def _check_root_machinery(m: int, k: int):
    """Closed root formula (eq. 29) vs independent chord/moment machinery: exact equality."""
    mons = frames.monomial_basis(m, k)
    closed = frames.root_single_direction_closed(m, mons)
    chord = frames.root_single_direction_matrix(m, k, mons)
    return closed == chord


def _radial_anchor(m: int, K_root, G, basis) -> tuple[bool, Fraction]:
    c = frames.radial_quadratic_vector(m, basis)
    got = _exact_quotient(K_root, G, c)
    want = frames.radial_root_anchor_exact(m)
    return got == want, got


# =====================================================================================
# per-(m, k) exact sweep
# =====================================================================================

def _certified_record(kind_frame: str, m: int, k: int, n: int, K, G, do_certify: bool,
                      cap_idxs, alpha_star=None):
    if do_certify:
        cert = certify.certify_lambda_min(K, G, g_known_pd=True)
        lam_f = cert["lambda_float"]
        rec_cert = {
            "lambda_float": lam_f,
            "lambda_upper_exact": str(cert["lambda_upper_exact"]),
            "lambda_upper_float": float(cert["lambda_upper_exact"]),
            "lambda_lower_exact": (None if cert["lambda_lower_exact"] is None
                                   else str(cert["lambda_lower_exact"])),
            "lambda_lower_float": (None if cert["lambda_lower_exact"] is None
                                   else float(cert["lambda_lower_exact"])),
            "certificate": cert["certificate"],
        }
    else:
        lam_f = _pencil_lambda_min(_floatm(K), _floatm(G))
        rec_cert = {"lambda_float": lam_f, "lambda_upper_exact": None,
                    "lambda_lower_exact": None, "certificate": None}
    rec = {"kind": "exact-frame-gap", "k": k, "m": m, "n_basis": n, "frame": kind_frame,
           "method": "exact-pencil-assembly; certified enclosure where present",
           "cap_proxies": _cap_proxies_exact(K, G, cap_idxs), **rec_cert}
    if alpha_star is not None:
        rec["alpha_star"] = str(alpha_star)
        rec["alpha_star_float"] = float(alpha_star)
    return rec


def _mixture_scan(m: int, k: int, Kr, Kv, G, grid_denominator: int):
    Krf, Kvf, Gf = _floatm(Kr), _floatm(Kv), _floatm(G)

    def lam(alpha: float) -> float:
        return _pencil_lambda_min(alpha * Krf + (1.0 - alpha) * Kvf, Gf)

    alphas = [Fraction(t, grid_denominator) for t in range(grid_denominator + 1)]
    lams = [lam(float(a)) for a in alphas]
    best = int(np.argmax(lams))
    lo = float(alphas[max(best - 1, 0)])
    hi = float(alphas[min(best + 1, len(alphas) - 1)])
    # golden-section refinement of the concave lambda_min(alpha)
    phi = (np.sqrt(5.0) - 1.0) / 2.0
    a, b = lo, hi
    x1 = b - phi * (b - a)
    x2 = a + phi * (b - a)
    f1, f2 = lam(x1), lam(x2)
    for _ in range(MIXTURE_REFINE_ITERS):
        if f1 < f2:
            a, x1, f1 = x1, x2, f2
            x2 = a + phi * (b - a)
            f2 = lam(x2)
        else:
            b, x2, f2 = x2, x1, f1
            x1 = b - phi * (b - a)
            f1 = lam(x1)
    alpha_star = Fraction((a + b) / 2.0).limit_denominator(MIXTURE_ALPHA_MAX_DENOMINATOR)
    alpha_star = min(max(alpha_star, Fraction(0)), Fraction(1))
    scan = {"kind": "mixture-scan", "k": k, "m": m,
            "alphas": [str(x) for x in alphas], "lambda_floats": lams,
            "alpha_star": str(alpha_star), "alpha_star_float": float(alpha_star),
            "note": "lambda_min(alpha) is concave; frame constraint is linear so every "
                    "alpha in [0,1] is admissible"}
    return scan, alpha_star


# =====================================================================================
# run
# =====================================================================================

def run_records(seed: int = 0,
                k2_ms=(3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
                k2_root_extra_ms=(13, 14, 15),
                k3_ms=(3, 4, 5, 6, 7),
                k3_root_extra_ms=(8,),
                mixture_grid_denominator: int = 8,
                spherical_k2_ms=(3, 4, 5, 6, 7, 8, 9, 10, 12),
                spherical_k3_ms=(3, 4, 5, 6),
                spherical_samples: int = 20000,
                do_certify: bool = True):
    """Deterministic exact channels (A)-(D) plus the seeded directional spherical channel.

    The seed drives ONLY the spherical Monte Carlo; every exact channel is
    seed-independent.
    """
    records: list[dict] = []

    # ---- calibration preamble: independent machinery cross-check ---------------------
    for (m, k) in ((3, 2), (4, 2), (3, 3)):
        ok = _check_root_machinery(m, k)
        records.append({"kind": "calibration", "channel": "root-machinery",
                        "instance": f"cal-root-closed-vs-chord-m{m}-k{k}",
                        "exact_equal": bool(ok),
                        "note": "closed Dirichlet-neutrality formula (probe eq. 29) vs the "
                                "independent chord/chamber integration machinery, exact "
                                "Fraction equality entry by entry"})
        _assert_anchor(ok, f"root closed form != chord machinery at m={m}, k={k}")

    plans = [
        (2, tuple(k2_ms), tuple(k2_root_extra_ms), tuple(spherical_k2_ms)),
        (3, tuple(k3_ms), tuple(k3_root_extra_ms), tuple(spherical_k3_ms)),
    ]

    gap_tables: dict[int, dict[int, dict]] = {2: {}, 3: {}}
    exact_lib_lower: dict[int, dict[int, Fraction | None]] = {2: {}, 3: {}}

    for k, ms_all, ms_root_only, sph_ms in plans:
        for m in ms_all + ms_root_only:
            root_only = m in ms_root_only
            basis = frames.monomial_basis(m, k)
            n = len(basis)
            G = frames.gram_matrix(m, basis)
            if do_certify:
                _assert_anchor(certify.bareiss_positive_definite(G),
                               f"Gram matrix not PD at m={m}, k={k}")
            cap_idxs = _cap_proxy_indices(m, k, basis)

            Kr = frames.root_K(m, basis)
            _assert_anchor(frames.linear_block_equals_gram(Kr, G, m),
                           f"root linear sector != 1 at m={m}, k={k}")
            rad_ok, rad_got = _radial_anchor(m, Kr, G, basis)
            records.append({"kind": "calibration", "channel": "root-anchors",
                            "instance": f"cal-root-anchors-m{m}-k{k}",
                            "linear_block_exact_equal": True,
                            "radial_quotient": str(rad_got),
                            "radial_anchor": str(frames.radial_root_anchor_exact(m)),
                            "radial_exact_equal": bool(rad_ok)})
            _assert_anchor(rad_ok, f"radial root quotient anchor failed at m={m}, k={k}")

            rec_root = _certified_record("root", m, k, n, Kr, G, do_certify, cap_idxs)
            records.append(rec_root)
            row = {"root": rec_root["lambda_float"]}
            lower_candidates = [None if rec_root["lambda_lower_exact"] is None
                                else Fraction(rec_root["lambda_lower_exact"])]

            if not root_only:
                Kv = frames.vertex_K(m, k, basis)
                _assert_anchor(frames.linear_block_equals_gram(Kv, G, m),
                               f"vertex linear sector != 1 at m={m}, k={k}")
                rec_vert = _certified_record("vertex", m, k, n, Kv, G, do_certify, cap_idxs)
                records.append(rec_vert)
                row["vertex"] = rec_vert["lambda_float"]
                if rec_vert["lambda_lower_exact"] is not None:
                    lower_candidates.append(Fraction(rec_vert["lambda_lower_exact"]))

                scan, alpha_star = _mixture_scan(m, k, Kr, Kv, G, mixture_grid_denominator)
                records.append(scan)
                Kmix = frames.mixture_K(Kr, Kv, alpha_star)
                rec_mix = _certified_record("mixture", m, k, n, Kmix, G, do_certify,
                                            cap_idxs, alpha_star=alpha_star)
                records.append(rec_mix)
                row["mixture"] = rec_mix["lambda_float"]
                row["alpha_star"] = float(alpha_star)
                if rec_mix["lambda_lower_exact"] is not None:
                    lower_candidates.append(Fraction(rec_mix["lambda_lower_exact"]))

            gap_tables[k][m] = row
            finite = [c for c in lower_candidates if c is not None]
            exact_lib_lower[k][m] = max(finite) if finite else None

        # ---- spherical directional channel ------------------------------------------
        for m in sph_ms:
            basis = frames.monomial_basis(m, k)
            G = frames.gram_matrix(m, basis)
            Gf = _floatm(G)
            seeds = (int(seed) + 1, int(seed) + 1 + SPHERICAL_SEED_OFFSET)
            estimates, lams = [], []
            for s in seeds:
                A = spherical.spherical_frame_estimate(m, k, basis, spherical_samples, s)
                estimates.append(A)
                lams.append(_pencil_lambda_min(A, Gf))
            scale = max(abs(lams[0]), abs(lams[1]), 1e-12)
            converged = abs(lams[0] - lams[1]) <= SPHERICAL_CONVERGENCE_REL_TOL * scale
            A_avg = 0.5 * (estimates[0] + estimates[1])
            nlin = m - 1
            lin_dev = float(np.max(np.abs(A_avg[:nlin, :nlin] - Gf[:nlin, :nlin]))
                            / np.max(np.abs(Gf[:nlin, :nlin])))
            lam_avg = _pencil_lambda_min(A_avg, Gf)
            cap = {}
            for j, t in _cap_proxy_indices(m, k, basis).items():
                cap[f"P1^{j}"] = float(A_avg[t, t] / Gf[t, t])
            cmp_lin = compare_directional(
                "spherical linear block == Gram linear block (admissible-frame anchor)",
                f"sph-m{m}-k{k}", 0.05, lin_dev, rel_tol=0.0,
                note="max relative deviation of the MC linear block from the exact anchor")
            records.append({"kind": "spherical-directional", "k": k, "m": m,
                            "n_samples_per_seed": spherical_samples, "seeds": list(seeds),
                            "lambda_by_seed": lams, "lambda_avg": lam_avg,
                            "two_seed_converged": bool(converged),
                            "linear_anchor_max_rel_dev": lin_dev,
                            "linear_anchor_comparison": cmp_lin.dict(),
                            "cap_proxies_float": cap,
                            "method": "directional (Monte Carlo); never certifies"})
            if m in gap_tables[k]:
                gap_tables[k][m]["spherical"] = lam_avg if converged else None

    # ---- gap tables and pre-registered threshold evaluation --------------------------
    for k in (2, 3):
        rows = []
        for m in sorted(gap_tables[k]):
            row = gap_tables[k][m]
            lib = [v for key, v in row.items()
                   if key in ("root", "vertex", "mixture", "spherical") and v is not None]
            row_out = {"m": m, **row, "gap_lib_float": max(lib),
                       "gap_lib_exact_lower": (None if exact_lib_lower[k][m] is None
                                               else str(exact_lib_lower[k][m])),
                       "gap_lib_exact_lower_float": (None if exact_lib_lower[k][m] is None
                                                     else float(exact_lib_lower[k][m]))}
            rows.append(row_out)
        records.append({"kind": "gap-table", "k": k, "rows": rows})

    k2_rows = [r for r in records if r["kind"] == "gap-table" and r["k"] == 2][0]["rows"]
    full = [r for r in k2_rows if "vertex" in r and r["m"] >= 4]
    evaluation = {"kind": "threshold-evaluation", "k": 2,
                  "thresholds": PREREGISTERED_THRESHOLDS}
    if len(full) >= 2:
        gaps = [r["gap_lib_float"] for r in full]
        monotone = all(gaps[t + 1] < gaps[t] for t in range(len(gaps) - 1))
        factor = gaps[0] / gaps[-1] if gaps[-1] > 0 else float("inf")
        top = gaps[-1]
        against = bool(monotone and factor >= PREREGISTERED_THRESHOLDS[
            "directional_against_factor"] and top < PREREGISTERED_THRESHOLDS[
            "directional_against_top_gap"])
        lead_families = []
        for fam in ("root", "vertex", "spherical"):
            vals = [r.get(fam) for r in k2_rows]
            vals = [v for v in vals if v is not None]
            if vals and min(vals) >= PREREGISTERED_THRESHOLDS["constructive_lead_gap"]:
                lead_families.append(fam)
        evaluation.update({
            "m_range_evaluated": [full[0]["m"], full[-1]["m"]],
            "gap_lib_first": gaps[0], "gap_lib_last": gaps[-1],
            "monotone_decreasing": bool(monotone), "total_decay_factor": float(factor),
            "directional_against_route": against,
            "constructive_lead_families": lead_families,
            "constructive_lead": bool(lead_families),
        })
    records.append(evaluation)

    summary = {
        "no_status_change": True,
        "gate": "q:conditional-fiber-frame: library lower bounds "
                "and directional decay decide nothing; the all-frame gate needs an exact "
                "dual certificate or a uniform lower bound, independently proved",
        "threshold_evaluation": {kk: vv for kk, vv in evaluation.items() if kk != "kind"},
        "gap_table_k2": k2_rows,
        "gap_table_k3": [r for r in records
                         if r["kind"] == "gap-table" and r["k"] == 3][0]["rows"],
        "monte_carlo_used": True,
        "monte_carlo_scope": "spherical channel only; every exact channel is deterministic",
    }
    config = {
        "k2_ms": list(k2_ms), "k2_root_extra_ms": list(k2_root_extra_ms),
        "k3_ms": list(k3_ms), "k3_root_extra_ms": list(k3_root_extra_ms),
        "mixture_grid_denominator": int(mixture_grid_denominator),
        "spherical_k2_ms": list(spherical_k2_ms), "spherical_k3_ms": list(spherical_k3_ms),
        "spherical_samples": int(spherical_samples), "do_certify": bool(do_certify),
        "preregistered_thresholds": PREREGISTERED_THRESHOLDS,
        "basis": "monomials in p_1..p_{m-1}, degrees 1..k (quotient V_{m,k} basis)",
        "certification": {
            "lower": "exact integer Bareiss/Sylvester PD test of K - lam*G",
            "upper": "exact rational Rayleigh quotient of the rationalized eigenvector",
            "lambda_rationalization_max_denominator": certify.LOWER_MAX_DENOMINATOR,
        },
    }
    return RunResult(lift_observations(records), config=config, summary=summary)


# =====================================================================================
# selftest (fast lane)
# =====================================================================================

def selftest(rng):
    checks = []

    # root closed form vs independent chord machinery, exact equality
    checks.append(("fiber-frame cal: root closed form == chord machinery (m=3, k=2)",
                   _check_root_machinery(3, 2)))

    # per-direction radial anchor (probe eq. 35): q_theta[F] == 4/5 for F = |X|^2 - d.
    # The basis vector c represents sum_i P_i^2 = F/R_m^4-scale, so
    # c' B^{12} c == (4/5) / (m^2 (m+1)^2) exactly.
    ok35 = True
    for m in (3, 4):
        basis = frames.monomial_basis(m, 2)
        B12 = frames.root_single_direction_closed(m, basis)
        c = frames.radial_quadratic_vector(m, basis)
        num = certify.quadratic_form(B12, c)
        ok35 = ok35 and (num == Fraction(4, 5 * m * m * (m + 1) * (m + 1)))
    checks.append(("fiber-frame cal: single root direction radial energy == "
                   "(4/5)/R_m^4 exactly (eq. 35; m=3,4)", ok35))

    # aggregate anchors at m=3..5, k=2
    ok_lin, ok_rad = True, True
    for m in (3, 4, 5):
        basis = frames.monomial_basis(m, 2)
        G = frames.gram_matrix(m, basis)
        Kr = frames.root_K(m, basis)
        ok_lin = ok_lin and frames.linear_block_equals_gram(Kr, G, m)
        ok_rad = ok_rad and _radial_anchor(m, Kr, G, basis)[0]
        Kv = frames.vertex_K(m, 2, basis)
        ok_lin = ok_lin and frames.linear_block_equals_gram(Kv, G, m)
    checks.append(("fiber-frame cal: root+vertex linear sector == 1 exactly (m=3..5, k=2)",
                   ok_lin))
    checks.append(("fiber-frame cal: root radial quotient == (m+2)(m+3)/(5m^2) (m=3..5)",
                   ok_rad))

    # m=2 degeneracy: the vertex direction IS the root direction
    basis2 = frames.monomial_basis(2, 2)
    same = frames.root_K(2, basis2) == frames.vertex_K(2, 2, basis2)
    checks.append(("fiber-frame cal: vertex frame == root frame at m=2 (exact)", same))

    # certified enclosure sanity at m=4, k=2 root
    basis = frames.monomial_basis(4, 2)
    G = frames.gram_matrix(4, basis)
    Kr = frames.root_K(4, basis)
    cert = certify.certify_lambda_min(Kr, G)
    lo, hi = cert["lambda_lower_exact"], cert["lambda_upper_exact"]
    ok_cert = (lo is not None and Fraction(0) < lo < hi
               and float(hi) - float(lo) <= 0.05 * float(hi))
    checks.append((f"fiber-frame cert: exact enclosure around float lambda_min "
                   f"({cert['lambda_float']:.6f})", bool(ok_cert)))

    # Bareiss PD oracle
    pd = certify.bareiss_positive_definite(
        [[Fraction(2), Fraction(1)], [Fraction(1), Fraction(2)]])
    npd = certify.bareiss_positive_definite(
        [[Fraction(1), Fraction(2)], [Fraction(2), Fraction(1)]])
    checks.append(("fiber-frame cert: Bareiss PD test (PD yes, indefinite no)",
                   pd and not npd))
    return checks
