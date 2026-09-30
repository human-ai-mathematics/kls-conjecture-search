"""Part III (KLS, moment-map/CMH route) -- the **anisotropic bootstrap** and the **M9 probe**.

Two questions, one target.  Neither can change any status; see "Boundary" below.

**Channel 1 -- the matrices ``N``, ``D``, ``R`` of the linear-recovery bootstrap.**
`2026-08-27-kls-route-prober-cmh-linear-recovery-w3c01.md` reduces the linear part of
`ass:cmh-recovery-envelope` to one missing inequality.  In source coordinates, with source
density ``e^{-psi}``, ``H = D^2 psi``, and ``eta = e^{-psi} dy``,

    N = int H^2 d eta,   D = int H^{ab} (d_a H)(d_b H) d eta,   R = N - D,

and the probe certifies inside itself the identity ``N = D + R`` with
``R = (1/2) int {H, A + Q}`` for the differentiated Monge-Ampere reservoirs ``A``, ``Q``, and the
Brascamp-Lieb bound ``N - I <= D``.  The open candidate is

    (AB)   R >= rho N - beta I,      sharp form   R >= N/2   (rho = 1/2, beta = 0),

which would give ``Q_lin = lambda_max(N) <= (1 + beta)/rho``.  This target computes ``N``, ``D``,
``R`` and the two Loewner verdicts exactly, in ``fractions.Fraction``, on the closed-form
one-dimensional families and on the certified Dirichlet moment maps, and directionally on
two-dimensional moment maps built from analytic source potentials.

Coordinate transport, verified before coding and re-verified by oracle tests.  With
``x = grad psi(y)`` and ``Htilde(x) = H(y(x))``, the chain rule gives
``d_{y_a} H = H_{ab} d_{x_b} Htilde``, hence ``H^{ab}(d_a H)(d_b H) = Htilde_{cd}
(d_c Htilde)(d_d Htilde)`` and therefore

    v^T D v = int sum_{c,d} Htilde_{cd} <(d_c Htilde) v, (d_d Htilde) v> d mu.

The index placement is pinned independently three times: by the exact one-dimensional identity
``N = 2D + E[H^3 V'']``, by the Brascamp-Lieb verdict on every Dirichlet instance, and by the
quadrature identity ``N - D = (1/2) int {H, A+Q}`` on two-dimensional moment maps.

On the two-dimensional geometries the two differentiated Monge-Ampere reservoirs are reported
separately, ``R = R_A + R_Q`` with ``R_X = (1/2) int {H, X}``.  ``R_A >= 0`` is exactly target
log-concavity; ``R_Q >= D`` is the anisotropic form of the Chen-Klartag cyclic square whose
*trace* version ``Tr R_Q >= Tr D`` is what makes the scalar bootstrap work, and which the probe
fenced off as having no pointwise Loewner promotion.  Splitting the two says which reservoir a
proof has to spend.

**Channel 2 -- the M9 second-variation probe (`conj:cmh-second-variation`).**
`thm:cmh-product` puts ``C_CMH = 4`` exactly, with zero slack, at the product of the centred
one-sided exponential and a standard Gaussian.  This channel perturbs its moment potential,
``psi_eps = phi(s) + t^2/2 + eps a(s) b(t)`` with ``phi(s) = e^s - s``, verifies convexity and
target log-concavity, and computes a Galerkin lower bound for ``C_CMH(mu_eps)``.

**Boundary.**  Exact rational output here is a *candidate*: an indefinite Loewner verdict is a
candidate refutation of a stated matrix inequality on a stated instance, and becomes logical
content only after a `prover` restates it and a distinct `proof-checker` certifies it.  Channels
1(c) and 2 are quadrature on finite grids and are directional in every case.  Nothing in this
module bears on `conj:kls`, on `thm:cmh-dirichlet`, or on the certified gate-zero battery, which
is imported read-only for cross-checks and never modified.
"""
from __future__ import annotations

from fractions import Fraction

import numpy as np

from ....contract import RunResult, lift_observations
from ....comparison import compare_directional, compare_exact, matches
from . import dirichlet as dir_channel
from . import exact_forms as ex
from . import m9 as m9_channel
from . import onedim
from . import sourcemap


# =====================================================================================
# pre-registered thresholds -- fixed before any run of this target
# =====================================================================================

SHARP_CANDIDATE = "R - N/2 >= 0  (AB with rho = 1/2, beta = 0)"
AB_DIRECTIONAL_AGAINST_RHO_STAR_BETA_ONE = 0.05
AB_DIRECTIONAL_SUPPORT_RHO_STAR_BETA_ZERO = 0.3
CMH_REFUTATION_CANDIDATE_Q = m9_channel.REFUTATION_CANDIDATE_Q      # 4.05
CMH_CEILING = m9_channel.CMH_CEILING                                # 4.0
MOMENT_MAP_RESIDUAL_ABORT = sourcemap.MOMENT_MAP_RESIDUAL_ABORT     # 1e-6
CROSS_CHANNEL_ABS_TOL = 1e-9
DIRICHLET_ENGINE_CROSSCHECK_TOL = 1e-7

DIRICHLET_ALPHAS: tuple[tuple[int, ...], ...] = (
    # uniform simplices: lambda_max(N) = 2(m+1)/(m+3) increases to 2
    (1, 1), (1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1, 1), (1,) * 6, (1,) * 7, (1,) * 8,
    # asked-for anisotropic sweep
    (1, 1, 10), (1, 1, 100), (1, 5, 25), (1, 2, 3, 4, 5), (2, 2, 2), (1, 1, 1, 50),
    # extreme anisotropy: Dir(1,...,1,K) -> the product of centred one-sided exponentials as
    # K -> infinity, which is exactly where R >= N/2 is TIGHT. These are the adversarial ones.
    (1, 1, 1000), (1, 1, 10000), (1, 1, 1, 1000), (1, 1, 1, 1, 1000), (1, 2, 1000),
    (1,) * 6 + (2000,), (1, 10, 100), (5, 5, 5),
)
RHO_BETAS = (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(1))


# =====================================================================================
# channel 1(a) -- exact one-dimensional
# =====================================================================================

def _one_dimensional_records() -> tuple[list[dict], dict, bool]:
    rows = onedim.one_d_instances()
    by_name = {row["name"]: row for row in rows}
    records: list[dict] = []
    calibration_ok = True

    gauss = by_name["gaussian"]
    v = matches("cal-ab-gauss", "Gaussian: (N, D, R) == (1, 0, 1)",
                float(gauss["N"] - gauss["D"] + gauss["R"]), 2.0, rel_tol=0.0)
    calibration_ok = calibration_ok and (
        gauss["N"] == 1 and gauss["D"] == 0 and gauss["R"] == 1)
    records.append({"kind": "calibration", "channel": "1d-exact", "instance": "cal-ab-gauss",
                    "N": 1.0, "D": 0.0, "R": 1.0, "comparison": v.dict(),
                    "passed": bool(gauss["N"] == 1 and gauss["D"] == 0 and gauss["R"] == 1),
                    "note": "tau = 1, so D = 0 and R/N = 1: the isotropic-Gaussian anchor."})

    expo = by_name["gamma-a1"]
    exponential_ok = (expo["N"] == 2 and expo["D"] == 1 and expo["R"] == 1
                      and expo["sharp_margin"] == 0)
    calibration_ok = calibration_ok and exponential_ok
    records.append({"kind": "calibration", "channel": "1d-exact",
                    "instance": "cal-ab-centred-exponential",
                    "N": 2.0, "D": 1.0, "R": 1.0, "R_over_N": 0.5,
                    "passed": bool(exponential_ok),
                    "comparison": matches("cal-ab-centred-exponential",
                                          "centred exponential: R/N == 1/2 exactly",
                                          float(expo["R"] / expo["N"]), 0.5,
                                          rel_tol=0.0).dict(),
                    "note": "H(x) = x+1: N = E[(X+1)^2] = 2, D = E[H (H')^2] = E[X+1] = 1. "
                            "The sharp candidate R >= N/2 is TIGHT here, and so is N - I <= D."})

    uni = by_name["uniform"]
    uniform_ok = (uni["N"] == Fraction(6, 5) and uni["D"] == Fraction(3, 5)
                  and uni["sharp_margin"] == 0)
    calibration_ok = calibration_ok and uniform_ok
    records.append({"kind": "calibration", "channel": "1d-exact", "instance": "cal-ab-uniform",
                    "N": 1.2, "D": 0.6, "R": 0.6, "passed": bool(uniform_ok),
                    "note": "uniform interval: the second log-affine saturator of R = N/2."})

    crosscheck = onedim.gate_zero_r1_crosscheck()
    worst = max(abs(a - b) for _, a, b in crosscheck)
    calibration_ok = calibration_ok and worst <= CROSS_CHANNEL_ABS_TOL
    records.append({"kind": "cross-channel-consistency", "channel": "1d-exact",
                    "check": "N here == R1 of the certified cmh-gate-zero battery",
                    "max_abs_error": float(worst),
                    "passed": bool(worst <= CROSS_CHANNEL_ABS_TOL),
                    "instances": [name for name, _, _ in crosscheck],
                    "note": "N = E[tau^2]/sigma^4 is literally gate zero's R1; the two "
                            "independent implementations must agree exactly."})

    identity_failures, sharp_failures, bl_failures = [], [], []
    for row in rows:
        payload = onedim.float_row(row)
        if not payload["identity_holds_exactly"]:
            identity_failures.append(row["name"])
        if not payload["sharp_candidate_holds"]:
            sharp_failures.append(row["name"])
        if not payload["brascamp_lieb_holds"]:
            bl_failures.append(row["name"])
        verdict = compare_exact(
            "sharp candidate, as lambda_max(D, N) <= 1/2", row["name"], 0.5,
            float(row["D"] / row["N"]), rel_tol=0.0,
            note="Exact rational scalar D/N; 'exceeds' would mean R < N/2 on the line.")
        records.append({"kind": "ab-one-dimensional", "channel": "1d-exact", **payload,
                        "sharp_candidate_comparison": verdict.dict()})
    summary = {
        "n_instances": len(rows),
        "identity_failures": identity_failures,
        "sharp_candidate_failures": sharp_failures,
        "brascamp_lieb_failures": bl_failures,
        "min_sharp_margin": float(min(row["sharp_margin"] for row in rows)),
        "min_rho_star_beta_0": float(min(row["rho_star"]["0"] for row in rows)),
        "min_rho_star_beta_1": float(min(row["rho_star"]["1"] for row in rows)),
        "max_lambda_max_N": float(max(row["N"] for row in rows)),
    }
    records.append({"kind": "channel-summary", "channel": "1d-exact", **summary,
                    "analytic_note": "On the line R = D + E[H^3 V''] with V'' >= 0 for every "
                                     "log-concave law, so R >= D, i.e. R >= N/2, ALWAYS holds, "
                                     "with equality exactly on the log-affine densities. One "
                                     "dimension therefore cannot refute the sharp candidate."})
    return records, summary, calibration_ok


# =====================================================================================
# channel 1(b) -- exact Dirichlet
# =====================================================================================

def _dirichlet_records(alphas) -> tuple[list[dict], dict, bool]:
    records: list[dict] = []
    calibration_ok = True

    got, expected = dir_channel.gate_zero_crosscheck((1, 5, 25))
    v = matches("cal-ab-dirichlet-gate-zero",
                "lambda_max(N, Sigma) == certified gate-zero ratio for dir(1,5,25)",
                got, expected, rel_tol=1e-10)
    calibration_ok = calibration_ok and v.outcome == "match"
    records.append({"kind": "calibration", "channel": "dirichlet-exact",
                    "instance": "cal-ab-dirichlet-gate-zero", "value": got, "exact": expected,
                    "comparison": v.dict(),
                    "note": "the whitened lambda_max(N) of this channel IS gate zero's G0ratio; "
                            "the two independent assemblies must agree."})

    worst = 0.0
    for a, b in ((1, 1), (1, 2), (2, 5), (3, 7)):
        n_here, n_there, d_here, d_there = dir_channel.one_dimensional_crosscheck(a, b)
        worst = max(worst, abs(n_here - n_there), abs(d_here - d_there))
    calibration_ok = calibration_ok and worst <= CROSS_CHANNEL_ABS_TOL
    records.append({"kind": "cross-channel-consistency", "channel": "dirichlet-exact",
                    "check": "Dir(a,b) on Delta_1 == the standardized Beta(a,b) of channel 1(a)",
                    "max_abs_error": float(worst),
                    "passed": bool(worst <= CROSS_CHANNEL_ABS_TOL),
                    "note": "this pins the chart, the tangent covariance and both Sigma^{-1} "
                            "insertions in N and D."})

    rows = []
    sharp_failures, bl_failures = [], []
    for alpha in alphas:
        row = dir_channel.analyse(alpha, betas=RHO_BETAS)
        rows.append(row)
        if not row["sharp_candidate_holds"]:
            sharp_failures.append(row["instance"])
        if not row["brascamp_lieb_holds"]:
            bl_failures.append(row["instance"])
        verdict = compare_exact(
            "sharp candidate, as lambda_max(D, N) <= 1/2", row["instance"], 0.5,
            row["lambda_max_D_over_N_exact_lower"], rel_tol=0.0,
            note="Exact rational generalized Rayleigh quotient of a rational witness vector: a "
                 "rigorous LOWER bound for lambda_max(D, N). 'exceeds' means R >= N/2 provably "
                 "fails on this instance. The companion symmetric-pivot LDL certificate decides "
                 "the Loewner question outright.")
        records.append({"kind": "ab-dirichlet", "channel": "dirichlet-exact", **row,
                        "sharp_candidate_comparison": verdict.dict()})

    def _rho_min(beta: str, key: str):
        values = [r["rho_star"][beta][key] for r in rows if r["rho_star"][beta][key] is not None]
        return float(min(values)) if values else None

    summary = {
        "n_instances": len(rows),
        "sharp_candidate_failures": sharp_failures,
        "brascamp_lieb_failures": bl_failures,
        "gate_zero_above_two_instances": [r["instance"] for r in rows
                                          if r["gate_zero_exceeds_two"]],
        "max_gate_zero_ratio_directional": float(max(r["gate_zero_ratio_directional"]
                                                    for r in rows)),
        "min_rho_star_beta_0_exact_upper": _rho_min("0", "exact_upper_bound"),
        "min_rho_star_beta_1_exact_upper": _rho_min("1", "exact_upper_bound"),
        "min_rho_star_beta_0_exact_lower": _rho_min("0", "exact_lower_bound"),
        "min_rho_star_beta_1_exact_lower": _rho_min("1", "exact_lower_bound"),
    }
    records.append({"kind": "channel-summary", "channel": "dirichlet-exact", **summary,
                    "analytic_note": "R >= N/2 together with the certified N - I <= D forces "
                                     "N <= 2I. An exact witness for lambda_max(N) > 2 therefore "
                                     "also refutes the sharp candidate on that instance."})
    return records, summary, calibration_ok


# =====================================================================================
# channel 1(c) -- directional two-dimensional moment maps
# =====================================================================================

def _product_calibration_targets():
    exact = {row["name"]: row for row in onedim.one_d_instances()}
    del exact                       # the exact one-dimensional data now comes from sourcemap
    return SOURCEMAP_CALIBRATION_BASES


def _product_calibration_note():
    return ("for a product moment map N and D are block diagonal with the exact "
            "one-dimensional entries: (1 + 1/a, 1/a) for Gamma(a), (1, 0) for the Gaussian, "
            "(6/5, 3/5) for the uniform interval.")


# ``(label, factor_1, factor_2)``.  ``gamma:1`` is the centred one-sided exponential, the
# saturator of both CMH(4) and the sharp (AB) candidate; ``gamma:1.5`` and ``gamma:3`` sit
# strictly inside the log-concave class because their target potential has ``V'' > 0``.
SOURCEMAP_CALIBRATION_BASES = (
    ("exp-gauss", "gamma:1", "gaussian"),
    ("exp-exp", "gamma:1", "gamma:1"),
    ("gam1.5-gauss", "gamma:1.5", "gaussian"),
    ("unif-gauss", "uniform", "gaussian"),
    ("exp-unif", "gamma:1", "uniform"),
)
SOURCEMAP_PERTURBED_BASES = (
    ("exp-exp", "gamma:1", "gamma:1"),
    ("exp-gauss", "gamma:1", "gaussian"),
    ("gam1.5-gauss", "gamma:1.5", "gaussian"),
    ("gam3-gauss", "gamma:3", "gaussian"),
    ("gauss-gauss", "gaussian", "gaussian"),
)


# For each base product, the perturbation dictionary must respect the factor's own degeneracy:
# a Gamma factor has ``psi_ss = e^s -> 0`` as ``s -> -infinity``, so only a bump in ``u = e^s``
# keeps ``D^2 psi_eps > 0``; a Gaussian factor has ``psi_tt = 1`` and admits an ordinary
# coordinate bump.  ``uniform`` is used only unperturbed: its Hessian vanishes at both ends of
# the interval and every coupling tried there fails the convexity gate.
def _perturbation_dictionary(first_factor, second_factor, longitudinal, transverse):
    def side(name):
        if sourcemap.parse_factor(name)[0] in {"gamma", "exponential"}:
            return [sourcemap.exponential_bump(c, w) for _, c, w in longitudinal]
        return [sourcemap.coordinate_bump(c, w) for _, c, w in longitudinal]

    firsts = side(first_factor)
    if sourcemap.parse_factor(second_factor)[0] == "gaussian":
        seconds = [sourcemap.damped_hermite(d) for d in transverse]
    else:
        seconds = side(second_factor)
    return [sourcemap.make_coupling(a, b) for a in firsts for b in seconds]


def _sourcemap_geometries(longitudinal, transverse, epsilons):
    geometries = []
    for base, first, second in SOURCEMAP_PERTURBED_BASES:
        for coupling in _perturbation_dictionary(first, second, longitudinal, transverse):
            for epsilon in epsilons:
                for signed in (epsilon, -epsilon):
                    geometries.append(sourcemap.ProductGeometry(
                        f"{base}+{coupling.label}@{signed:+g}", first, second,
                        coupling=coupling, epsilon=signed,
                        description=("nonproduct moment map: perturbation of the "
                                     f"{base} product moment potential")))
    return geometries


def _sourcemap_records(longitudinal, transverse, epsilons, base_nodes, dirichlet_base_nodes,
                       dirichlet_alphas) -> tuple[list[dict], dict, bool]:
    records: list[dict] = []
    calibration_ok = True
    targets = _product_calibration_targets()

    worst_product = 0.0
    for name, first_factor, second_factor in targets:
        geometry = sourcemap.ProductGeometry(name, first_factor, second_factor,
                                             description="product calibration")
        row = sourcemap.analyse(geometry, geometry.resolution(base_nodes))
        if row["status"] != "ok":
            calibration_ok = False
            records.append({"kind": "calibration", "channel": "sourcemap",
                            "instance": f"cal-ab-product-{name}", "passed": False, **row})
            continue
        first = sourcemap.factor_exact_bootstrap(first_factor)
        second = sourcemap.factor_exact_bootstrap(second_factor)
        expected_n = np.diag([first[0], second[0]])
        expected_d = np.diag([first[1], second[1]])
        err = max(float(np.abs(np.array(row["N"]) - expected_n).max()),
                  float(np.abs(np.array(row["D"]) - expected_d).max()))
        worst_product = max(worst_product, err)
        records.append({"kind": "calibration", "channel": "sourcemap",
                        "instance": f"cal-ab-product-{name}", **row,
                        "expected_N": expected_n.tolist(), "expected_D": expected_d.tolist(),
                        "max_abs_error": err, "passed": bool(err <= 1e-8),
                        "note": "for a product moment map N and D are block diagonal with the "
                                "exact one-dimensional entries of channel 1(a)."})
    calibration_ok = calibration_ok and worst_product <= 1e-8

    worst_dirichlet = 0.0
    for alpha in dirichlet_alphas:
        geometry = sourcemap.DirichletGeometry(alpha)
        row = sourcemap.analyse(geometry, geometry.resolution(dirichlet_base_nodes))
        exact_sigma, exact_n, exact_d = dir_channel.bootstrap_matrices(alpha)
        whiten = np.linalg.inv(_sqrtm(ex.to_float_matrix(exact_sigma)))
        expected_n = whiten @ ex.to_float_matrix(exact_n) @ whiten
        expected_d = whiten @ ex.to_float_matrix(exact_d) @ whiten
        err = float("inf")
        if row["status"] == "ok":
            err = max(float(np.abs(np.array(row["N"]) - expected_n).max()),
                      float(np.abs(np.array(row["D"]) - expected_d).max()))
            worst_dirichlet = max(worst_dirichlet, err)
        records.append({"kind": "calibration", "channel": "sourcemap",
                        "instance": f"cal-ab-engine-vs-exact-{geometry.name}", **row,
                        "expected_N": expected_n.tolist(), "expected_D": expected_d.tolist(),
                        "max_abs_error": err,
                        "passed": bool(err <= DIRICHLET_ENGINE_CROSSCHECK_TOL),
                        "note": "the quadrature engine reproduces the exact rational Dirichlet "
                                "matrices of channel 1(b) on a genuinely nonproduct moment map."})
    calibration_ok = calibration_ok and worst_dirichlet <= DIRICHLET_ENGINE_CROSSCHECK_TOL

    rows = []
    for geometry in _sourcemap_geometries(longitudinal, transverse, epsilons):
        row = sourcemap.analyse(geometry, geometry.resolution(base_nodes))
        rows.append(row)
        payload = {"kind": "ab-sourcemap", "channel": "sourcemap", **row}
        if row["status"] == "ok":
            payload["sharp_candidate_comparison"] = compare_directional(
                "sharp candidate, as lambda_max(D, N) <= 1/2", row["instance"], 0.5,
                row["lambda_max_D_over_N"], rel_tol=0.0,
                note="Quadrature on a finite grid; directional only, never a refutation.").dict()
        records.append(payload)

    usable = [r for r in rows if r["status"] == "ok" and r["target_log_concave"]]
    reservoir = [r["lambda_min_R_Q_minus_D_relative"] for r in usable]
    summary = {
        "n_instances": len(rows), "n_usable": len(usable),
        "min_lambda_min_R_Q_minus_D_relative": float(min(reservoir)) if reservoir else None,
        "reservoir_split_note":
            "R = R_A + R_Q with R_X = (1/2) int {H, X}. R_A >= 0 is exactly target "
            "log-concavity. lambda_min(R_Q - D) < 0 on an admissible instance is directional "
            "evidence that the INTEGRATED anisotropic cyclic-square inequality R_Q >= D is "
            "false, i.e. that any proof of R >= N/2 must consume log-concavity through R_A and "
            "cannot run on the Monge-Ampere third-tensor algebra alone.",
        "n_aborted": sum(1 for r in rows if r["status"] != "ok"),
        "n_not_log_concave": sum(1 for r in rows
                                 if r["status"] == "ok" and not r["target_log_concave"]),
        "product_calibration_max_abs_error": worst_product,
        "dirichlet_engine_max_abs_error": worst_dirichlet,
        "worst_identity_residual": float(max(
            [r["residuals"]["monge_ampere_identity_relative"] for r in rows
             if r["status"] == "ok"], default=float("nan"))),
        "min_lambda_min_sharp_directional": float(min(
            [r["lambda_min_sharp_R_minus_half_N"] for r in usable], default=float("nan"))),
        "min_rho_star_beta_0_directional": float(min(
            [r["rho_star"]["0.0"] for r in usable], default=float("nan"))),
        "min_rho_star_beta_1_directional": float(min(
            [r["rho_star"]["1.0"] for r in usable], default=float("nan"))),
        "max_lambda_max_N_directional": float(max(
            [r["lambda_max_N"] for r in usable], default=float("nan"))),
    }
    records.append({"kind": "channel-summary", "channel": "sourcemap", **summary,
                    "analytic_note": "The prescribed-target Monge-Ampere solve of the original "
                                     "channel (c) design was replaced by prescribing the source "
                                     "potential. The class covered is therefore perturbed "
                                     "products and the certified Dirichlet maps, not arbitrary "
                                     "compact-target bodies. Directional only."})
    return records, summary, calibration_ok


def _factor_names(name: str):
    mapping = {"exp": "exponential", "gauss": "gaussian", "unif": "uniform"}
    first, second = name.split("-")[:2]
    return mapping[first], mapping[second]


def _sqrtm(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(0.5 * (matrix + matrix.T))
    return (vectors * np.sqrt(values)) @ vectors.T


# =====================================================================================
# channel 2 -- M9
# =====================================================================================

def _m9_records(couplings, epsilons, resolution, degree, enrichment_rates,
                refine_degree, refine_resolution,
                shapes=m9_channel.DEFAULT_SHAPES) -> tuple[list[dict], dict, bool]:
    records: list[dict] = []
    calibration_ok = True

    base = m9_channel.saturating_geometry()
    degree_one = m9_channel.galerkin_quotient(base, resolution, 1)
    v = matches("cal-ab-m9-degree-one",
                "degree-one Galerkin at eps = 0 == max(N_exp, N_gauss) == 2",
                degree_one["q"], m9_channel.degree_one_anchor(1.0), rel_tol=1e-8)
    calibration_ok = calibration_ok and v.outcome == "match"
    records.append({"kind": "calibration", "channel": "m9", "instance": "cal-ab-m9-degree-one",
                    **degree_one, "comparison": v.dict(),
                    "note": "linear test functions give exactly lambda_max(E H^2) = 2 for the "
                            "centred exponential factor."})

    ladder = []
    for deg in range(1, degree + 1):
        ladder.append(m9_channel.galerkin_quotient(base, resolution, deg))
    monotone = all(ladder[i + 1]["q"] >= ladder[i]["q"] - 1e-9 for i in range(len(ladder) - 1))
    below = all(row["q"] <= CMH_CEILING + 1e-9 for row in ladder)
    # closed form observed on the pure-Laguerre ladder: q_k = 2(1 + cos(pi/(k+1))) -> 4
    predicted = [2.0 * (1.0 + np.cos(np.pi / (row["degree"] + 1.0))) for row in ladder]
    ladder_formula_error = float(max(abs(row["q"] - p) for row, p in zip(ladder, predicted)))
    calibration_ok = calibration_ok and monotone and below
    records.append({"kind": "calibration", "channel": "m9", "instance": "cal-ab-m9-degree-ladder",
                    "degrees": [row["degree"] for row in ladder],
                    "q": [row["q"] for row in ladder],
                    "predicted_2_1_plus_cos_pi_over_k_plus_1": predicted,
                    "ladder_formula_max_abs_error": ladder_formula_error,
                    "monotone_in_degree": bool(monotone), "all_below_four": bool(below),
                    "passed": bool(monotone and below),
                    "note": "nested Galerkin subspaces give an increasing lower bound for "
                            "C_CMH; the eps = 0 limit is 4 and is approached from below. The "
                            "pure-Laguerre ladder matches 2(1 + cos(pi/(k+1))), which is the "
                            "quantitative statement that the exponential endpoint is a "
                            "continuous-spectrum edge, not an eigenvalue."})

    gaussian_pair = sourcemap.ProductGeometry("gauss-gauss", "gaussian", "gaussian",
                                              description="Gaussian product; C_CMH = 1 exactly")
    gaussian_ladder = [m9_channel.galerkin_quotient(gaussian_pair, (40, 40), deg)["q"]
                       for deg in (1, 2, 4, 6)]
    gaussian_error = max(abs(q - 1.0) for q in gaussian_ladder)
    v = matches("cal-ab-m9-gaussian-product",
                "Galerkin quotient on the Gaussian product == C_CMH == 1 at every degree",
                1.0 + gaussian_error, 1.0, rel_tol=1e-9)
    calibration_ok = calibration_ok and v.outcome == "match"
    records.append({"kind": "calibration", "channel": "m9",
                    "instance": "cal-ab-m9-gaussian-product",
                    "degrees": [1, 2, 4, 6], "q": gaussian_ladder,
                    "max_abs_error": gaussian_error, "comparison": v.dict(),
                    "passed": bool(v.outcome == "match"),
                    "note": "the only absolute anchor in this channel with an ATTAINED constant: "
                            "L He_k = -k He_k gives quotient 1/k, so the Galerkin value is "
                            "exactly 1 at every degree. It calibrates the numerator, the "
                            "denominator and the generator drift simultaneously."})

    enriched_zero = m9_channel.galerkin_quotient(base, resolution, degree,
                                                 enrichment_rates=enrichment_rates)
    records.append({"kind": "calibration", "channel": "m9",
                    "instance": "cal-ab-m9-enriched-baseline", **enriched_zero,
                    "gap_to_four": CMH_CEILING - enriched_zero["q"],
                    "passed": bool(enriched_zero["q"] <= CMH_CEILING + 1e-9),
                    "note": "the exponential endpoint is the bottom of a purely continuous "
                            "spectrum and is not attained in L^2, so this gap is the probe's "
                            "resolution floor: a true second variation smaller than the gap is "
                            "invisible to this channel."})

    rows, candidates = [], []
    for shape in shapes:
        anchor = m9_channel.galerkin_quotient(
            m9_channel.saturating_geometry(shape=shape), resolution, degree,
            enrichment_rates=enrichment_rates)
        for coupling in couplings:
            values = {}
            skipped = []
            for epsilon in (0.0,) + tuple(e for eps in epsilons for e in (eps, -eps)):
                geometry = m9_channel.saturating_geometry(
                    coupling if epsilon != 0.0 else None, epsilon, shape=shape)
                result = m9_channel.galerkin_quotient(
                    geometry, resolution, degree, enrichment_rates=enrichment_rates)
                if result["status"] != "ok":
                    skipped.append(epsilon)
                    continue
                admissibility = sourcemap.analyse(geometry, resolution)
                result["target_log_concavity"] = admissibility.get("target_log_concavity")
                result["target_log_concavity_mean_margin"] = admissibility.get(
                    "target_mean_A_min_eigenvalue_relative")
                result["target_log_concavity_bulk_margin"] = admissibility.get(
                    "target_log_concavity_bulk_margin")
                result["target_log_concavity_bulk_mass"] = admissibility.get(
                    "target_log_concavity_bulk_mass")
                result["target_log_concave"] = admissibility.get("target_log_concave", False)
                result["admissibility_status"] = admissibility["status"]
                result["admissibility_worst_residual"] = admissibility.get("worst_residual")
                result["admissibility"] = {k: v for k, v in admissibility.items()
                                           if k != "_fields"}
                values[epsilon] = result
            if 0.0 not in values:
                continue
            q0 = values[0.0]["q"]
            second_differences, admissible_second = {}, {}
            for epsilon in epsilons:
                if epsilon in values and -epsilon in values:
                    value = ((values[epsilon]["q"] + values[-epsilon]["q"] - 2.0 * q0)
                             / epsilon ** 2)
                    second_differences[str(epsilon)] = value
                    if (values[epsilon]["target_log_concave"]
                            and values[-epsilon]["target_log_concave"]):
                        admissible_second[str(epsilon)] = value
            admissible = {str(eps): row["q"] for eps, row in values.items()
                          if row["target_log_concave"]}
            flagged = [eps for eps, row in values.items()
                       if row["q"] > CMH_REFUTATION_CANDIDATE_Q and row["target_log_concave"]]
            row = {
                "kind": "m9-perturbation", "channel": "m9", "coupling": coupling.label,
                "shape": shape, "endpoint_q": anchor["q"],
                "q0": q0, "degree": degree, "resolution": list(resolution),
                "skipped_epsilons": skipped,
                "q": {str(k): v["q"] for k, v in values.items()},
                "covariance_drift": {str(k): v["covariance_drift"] for k, v in values.items()},
                "target_log_concavity": {str(k): v.get("target_log_concavity")
                                         for k, v in values.items()},
                "target_log_concavity_mean_margin": {
                    str(k): v.get("target_log_concavity_mean_margin") for k, v in values.items()},
                "target_log_concavity_bulk_margin": {
                    str(k): v.get("target_log_concavity_bulk_margin") for k, v in values.items()},
                "admissibility_worst_residual": {
                    str(k): v.get("admissibility_worst_residual") for k, v in values.items()},
                "admissible_q": admissible,
                "max_admissible_q": max(admissible.values()) if admissible else None,
                "second_difference": second_differences,
                "admissible_second_difference": admissible_second,
                "max_second_difference": (max(second_differences.values())
                                          if second_differences else None),
                "max_admissible_second_difference": (max(admissible_second.values())
                                                     if admissible_second else None),
                "flagged_epsilons": [str(e) for e in flagged],
            }
            row["comparison"] = compare_directional(
                f"perturbed Galerkin q <= {CMH_CEILING}", f"{coupling.label}@a={shape:g}",
                CMH_CEILING, max([q for q in admissible.values()] or [q0]), rel_tol=0.0,
                note="Floating Galerkin assembly and generalized eigensolve on a finite "
                     "quadrature grid: directional only. Only perturbations whose target is not "
                     "shown to have left the log-concave class are compared; a refutation "
                     "candidate additionally requires stability under one degree and one grid "
                     "refinement.").dict()
            if flagged:
                refined = {}
                for epsilon in flagged:
                    geometry = m9_channel.saturating_geometry(
                        coupling if epsilon != 0.0 else None, epsilon, shape=shape)
                    refined[f"degree-{refine_degree}"] = m9_channel.galerkin_quotient(
                        geometry, resolution, refine_degree, enrichment_rates=enrichment_rates)
                    refined["finer-grid"] = m9_channel.galerkin_quotient(
                        geometry, refine_resolution, degree, enrichment_rates=enrichment_rates)
                row["refinements"] = {k: v.get("q") for k, v in refined.items()}
                row["flagged_admissibility"] = {
                    str(eps): values[eps]["admissibility"] for eps in flagged}
                candidates.append(f"{coupling.label}@a={shape:g}")
            for value in values.values():
                value.pop("admissibility", None)
            rows.append(row)
            records.append(row)

    all_second = [v for row in rows for v in row["admissible_second_difference"].values()]
    admissible_q = [row["max_admissible_q"] for row in rows
                    if row["max_admissible_q"] is not None]
    summary = {
        "shapes": list(shapes),
        "n_admissible_two_sided_pairs": len(all_second),
        "max_admissible_q": float(max(admissible_q)) if admissible_q else None,
        "n_couplings": len(rows),
        "degree": degree, "resolution": list(resolution),
        "baseline_q0": rows[0]["q0"] if rows else None,
        "enriched_baseline_q": enriched_zero["q"],
        "gap_to_four_at_eps_zero": CMH_CEILING - enriched_zero["q"],
        "max_q": float(max([max(float(x) for x in row["q"].values()) for row in rows],
                           default=float("nan"))),
        "max_admissible_second_difference": float(max(all_second)) if all_second else None,
        "min_admissible_second_difference": float(min(all_second)) if all_second else None,
        "refutation_candidates": candidates,
        "refutation_candidate_threshold": CMH_REFUTATION_CANDIDATE_Q,
    }
    records.append({"kind": "channel-summary", "channel": "m9", **summary,
                    "analytic_note": "A negative or zero second difference is directional "
                                     "support for CMH(4) inside this dictionary only; it is not "
                                     "a second-variation theorem and resolves nothing about "
                                     "conj:cmh-second-variation. At shape a = 1 the target "
                                     "potential is affine on its support, so D^2 V has a zero "
                                     "eigenvalue and a two-sided moment-potential perturbation "
                                     "generically LEAVES the log-concave class; those rows carry "
                                     "target_log_concavity = 'violated' and are excluded from "
                                     "every verdict."})
    return records, summary, calibration_ok


# =====================================================================================
# run + selftest
# =====================================================================================

def run_records(seed: int = 0, dirichlet_alphas=DIRICHLET_ALPHAS,
                sourcemap_base_nodes=200, dirichlet_engine_base_nodes=160,
                sourcemap_epsilons=(0.02, 0.05, 0.1), sourcemap_dirichlet_alphas=((1, 1, 1),
                                                                                  (1, 2, 4)),
                m9_resolution=(180, 40), m9_degree=6, m9_epsilons=(0.02, 0.05, 0.1),
                m9_enrichment=(0.3, 0.4, 0.45, 0.475), m9_refine_degree=8,
                m9_refine_resolution=(260, 60), m9_longitudinal=m9_channel.DEFAULT_LONGITUDINAL,
                m9_transverse=m9_channel.DEFAULT_TRANSVERSE,
                m9_shapes=m9_channel.DEFAULT_SHAPES, run_sourcemap: bool = True,
                run_m9: bool = True):
    """Deterministic battery. ``seed`` is recorded for provenance only; nothing is sampled."""
    dirichlet_alphas = tuple(tuple(int(a) for a in alpha) for alpha in dirichlet_alphas)
    records: list[dict] = []
    calibration_ok = True

    one_d_records, one_d_summary, ok = _one_dimensional_records()
    records.extend(one_d_records)
    calibration_ok = calibration_ok and ok

    dir_records, dir_summary, ok = _dirichlet_records(dirichlet_alphas)
    records.extend(dir_records)
    calibration_ok = calibration_ok and ok

    couplings = m9_channel.make_dictionary(m9_longitudinal, m9_transverse)

    sm_summary: dict = {}
    if run_sourcemap:
        sm_records, sm_summary, ok = _sourcemap_records(
            m9_longitudinal, m9_transverse, sourcemap_epsilons, sourcemap_base_nodes,
            dirichlet_engine_base_nodes, sourcemap_dirichlet_alphas)
        records.extend(sm_records)
        calibration_ok = calibration_ok and ok

    m9_summary: dict = {}
    if run_m9:
        m9_records, m9_summary, ok = _m9_records(
            couplings, m9_epsilons, m9_resolution, m9_degree, m9_enrichment,
            m9_refine_degree, m9_refine_resolution, m9_shapes)
        records.extend(m9_records)
        calibration_ok = calibration_ok and ok

    exact_sharp_failures = (one_d_summary["sharp_candidate_failures"]
                            + dir_summary["sharp_candidate_failures"])
    exact_bl_failures = (one_d_summary["brascamp_lieb_failures"]
                         + dir_summary["brascamp_lieb_failures"])
    rho0_exact = [x for x in (one_d_summary["min_rho_star_beta_0"],
                              dir_summary["min_rho_star_beta_0_exact_upper"]) if x is not None]
    rho1_exact = [x for x in (one_d_summary["min_rho_star_beta_1"],
                              dir_summary["min_rho_star_beta_1_exact_upper"]) if x is not None]
    rho0 = min(rho0_exact) if rho0_exact else None
    rho1 = min(rho1_exact) if rho1_exact else None

    verdict = {
        "exact_sharp_candidate_failures": exact_sharp_failures,
        "exact_sharp_candidate_refuted": bool(exact_sharp_failures),
        "exact_brascamp_lieb_failures": exact_bl_failures,
        "min_rho_star_beta_0_exact": rho0,
        "min_rho_star_beta_1_exact": rho1,
        "directional_against_AB": bool(rho1 is not None
                                       and rho1 < AB_DIRECTIONAL_AGAINST_RHO_STAR_BETA_ONE),
        "directional_support_AB": bool(rho0 is not None
                                       and rho0 >= AB_DIRECTIONAL_SUPPORT_RHO_STAR_BETA_ZERO),
        "m9_refutation_candidates": m9_summary.get("refutation_candidates", []),
        "m9_max_q": m9_summary.get("max_q"),
        "m9_max_admissible_q": m9_summary.get("max_admissible_q"),
        "m9_n_admissible_two_sided_pairs": m9_summary.get("n_admissible_two_sided_pairs"),
        "m9_max_admissible_second_difference":
            m9_summary.get("max_admissible_second_difference"),
        "directional_reservoir_min_lambda_min_R_Q_minus_D_relative":
            sm_summary.get("min_lambda_min_R_Q_minus_D_relative"),
        "directional_against_integrated_cyclic_square": bool(
            (sm_summary.get("min_lambda_min_R_Q_minus_D_relative") or 0.0) < -1e-5),
    }

    records.append({
        "kind": "summary", "target": "cmh-ab",
        "calibration_passed": bool(calibration_ok),
        "deterministic": True, "monte_carlo_used": False,
        **verdict,
        "thresholds": {
            "sharp_candidate": SHARP_CANDIDATE,
            "directional_against_AB_rho_star_beta_one": AB_DIRECTIONAL_AGAINST_RHO_STAR_BETA_ONE,
            "directional_support_AB_rho_star_beta_zero":
                AB_DIRECTIONAL_SUPPORT_RHO_STAR_BETA_ZERO,
            "m9_refutation_candidate_q": CMH_REFUTATION_CANDIDATE_Q,
            "moment_map_residual_abort": MOMENT_MAP_RESIDUAL_ABORT,
        },
        "status_effect": "none; no ledger status, proof step or dossier is affected",
        "note": "Exact Loewner verdicts are candidates for a refutation dossier, not "
                "refutations. Channel 1(c) and channel 2 are quadrature on finite grids and are "
                "directional in every case. The sharp candidate R >= N/2 is a matrix inequality "
                "about ONE regular law; the recovery gate ass:cmh-recovery-envelope only needs "
                "SOME (rho, beta) along SOME recovery sequence, so a failure here does not "
                "refute the gate, gate zero, thm:cmh-dirichlet or conj:kls.",
    })

    config = {
        "dirichlet_alphas": [list(a) for a in dirichlet_alphas],
        "rho_betas": [str(b) for b in RHO_BETAS],
        "sourcemap": {
            "enabled": bool(run_sourcemap), "base_nodes": int(sourcemap_base_nodes),
            "dirichlet_engine_base_nodes": int(dirichlet_engine_base_nodes),
            "node_scale_by_factor": sourcemap.FACTOR_NODE_SCALE,
            "perturbed_bases": list(SOURCEMAP_PERTURBED_BASES),
            "epsilons": list(sourcemap_epsilons),
            "dirichlet_alphas": [list(a) for a in sourcemap_dirichlet_alphas],
            "residual_abort": MOMENT_MAP_RESIDUAL_ABORT,
        },
        "m9": {
            "enabled": bool(run_m9), "resolution": list(m9_resolution), "degree": m9_degree,
            "epsilons": list(m9_epsilons), "enrichment_rates": list(m9_enrichment),
            "refine_degree": m9_refine_degree, "refine_resolution": list(m9_refine_resolution),
            "longitudinal": [list(x) for x in m9_longitudinal],
            "transverse": list(m9_transverse), "shapes": list(m9_shapes),
            "quadrature": "Gauss-Laguerre in u = e^s times Gauss-Hermite in t",
            "keep_rel_tol": m9_channel.KEEP_REL_TOL,
        },
        "thresholds": {
            "directional_against_AB_rho_star_beta_one": AB_DIRECTIONAL_AGAINST_RHO_STAR_BETA_ONE,
            "directional_support_AB_rho_star_beta_zero":
                AB_DIRECTIONAL_SUPPORT_RHO_STAR_BETA_ZERO,
            "m9_refutation_candidate_q": CMH_REFUTATION_CANDIDATE_Q,
        },
    }
    summary = {
        "calibration_passed": bool(calibration_ok), "deterministic": True,
        "monte_carlo_used": False,
        "n_one_dimensional_instances": one_d_summary["n_instances"],
        "n_dirichlet_instances": dir_summary["n_instances"],
        "n_sourcemap_instances": sm_summary.get("n_instances", 0),
        "n_m9_couplings": m9_summary.get("n_couplings", 0),
        **verdict,
        "max_gate_zero_ratio_directional": dir_summary["max_gate_zero_ratio_directional"],
        "gate_zero_above_two_instances": dir_summary["gate_zero_above_two_instances"],
        "sourcemap_worst_identity_residual": sm_summary.get("worst_identity_residual"),
        "m9_gap_to_four_at_eps_zero": m9_summary.get("gap_to_four_at_eps_zero"),
        "proof_status": "no-proof; exact Loewner verdicts are refutation CANDIDATES only",
    }
    return RunResult(lift_observations(records), config=config, summary=summary)


def selftest(rng):
    checks = []

    rows = {row["name"]: row for row in onedim.one_d_instances()}
    checks.append(("AB cal: Gaussian (N,D,R) == (1,0,1)",
                   rows["gaussian"]["N"] == 1 and rows["gaussian"]["D"] == 0
                   and rows["gaussian"]["R"] == 1))
    expo = rows["gamma-a1"]
    checks.append(("AB cal: centred exponential (N,D,R) == (2,1,1), R/N == 1/2 exactly",
                   expo["N"] == 2 and expo["D"] == 1 and expo["R"] == 1
                   and expo["sharp_margin"] == 0))
    checks.append(("AB 1D: N = 2D + E[H^3 V''] exactly on every instance",
                   all(row["identity_residual"] == 0 for row in rows.values())))
    checks.append(("AB 1D: N - I <= D exactly on every instance",
                   all(row["brascamp_lieb_margin"] >= 0 for row in rows.values())))
    worst = max(abs(a - b) for _, a, b in onedim.gate_zero_r1_crosscheck())
    checks.append((f"AB cal: N == cmh-gate-zero R1 (max abs err {worst:.2e})", worst <= 1e-12))

    got, expected = dir_channel.gate_zero_crosscheck((1, 5, 25))
    checks.append((f"AB cal: lambda_max(N,Sigma) == gate-zero G0ratio ({got:.10f})",
                   abs(got - expected) <= 1e-10))
    worst = 0.0
    for a, b in ((1, 1), (2, 5)):
        n_here, n_there, d_here, d_there = dir_channel.one_dimensional_crosscheck(a, b)
        worst = max(worst, abs(n_here - n_there), abs(d_here - d_there))
    checks.append((f"AB cal: Dir(a,b) on Delta_1 == Beta(a,b) 1D data (max abs err {worst:.2e})",
                   worst <= 1e-12))

    row = dir_channel.analyse((1, 1, 1), betas=(Fraction(0),))
    checks.append(("AB Dirichlet: exact Brascamp-Lieb verdict holds on dir(1,1,1)",
                   row["brascamp_lieb_holds"]))

    geometry = sourcemap.ProductGeometry("exp-gauss", "exponential", "gaussian")
    engine = sourcemap.analyse(geometry, (120, 32))
    err = max(abs(engine["N"][0][0] - 2.0), abs(engine["N"][1][1] - 1.0),
              abs(engine["D"][0][0] - 1.0), abs(engine["D"][1][1] - 0.0))
    checks.append((f"AB engine: product moment map reproduces exact 1D N, D "
                   f"(max abs err {err:.2e})", err <= 1e-9 and engine["status"] == "ok"))
    checks.append((f"AB engine: N = D + (1/2) int (H(A+Q)+(A+Q)H) "
                   f"(rel residual {engine['residuals']['monge_ampere_identity_relative']:.2e})",
                   engine["residuals"]["monge_ampere_identity_relative"] <= 1e-8))

    coupled = sourcemap.ProductGeometry(
        "gauss-gauss", "gaussian", "gaussian",
        coupling=sourcemap.make_coupling(sourcemap.coordinate_bump(2.5, 1.2),
                                         sourcemap.damped_hermite(2)),
        epsilon=-0.1)
    row = sourcemap.analyse(coupled, coupled.resolution(160))
    checks.append((f"AB engine: certified Tr R_Q >= Tr D reproduced "
                   f"({row['trace_R_Q_minus_D_relative']:.3e} >= 0), while its Loewner form "
                   f"R_Q >= D fails on the same admissible instance "
                   f"({row['lambda_min_R_Q_minus_D_relative']:.3e})",
                   row["status"] == "ok" and row["trace_R_Q_minus_D_relative"] >= -1e-9
                   and row["target_log_concavity"] == "consistent"
                   and row["lambda_min_R_Q_minus_D_relative"] < -1e-3))

    err, dropped = sourcemap.dirichlet_target_hessian_error((2, 3, 4), (48, 48))
    checks.append((f"AB engine: A == H (D^2 V) H vs the closed-form Dirichlet D^2 V "
                   f"(max rel err {err:.2e} off {dropped:.1e} of the mass)", err <= 1e-6))

    base = m9_channel.saturating_geometry()
    degree_one = m9_channel.galerkin_quotient(base, (140, 24), 1)
    checks.append((f"AB M9 cal: degree-one Galerkin == 2 at eps = 0 ({degree_one['q']:.10f})",
                   abs(degree_one["q"] - 2.0) <= 1e-8))
    ladder = [m9_channel.galerkin_quotient(base, (140, 24), d)["q"] for d in (2, 4)]
    checks.append((f"AB M9 cal: Galerkin increases with degree and stays below 4 "
                   f"({ladder[0]:.4f} -> {ladder[1]:.4f})",
                   ladder[1] >= ladder[0] - 1e-9 and ladder[1] <= 4.0 + 1e-9))
    return checks
