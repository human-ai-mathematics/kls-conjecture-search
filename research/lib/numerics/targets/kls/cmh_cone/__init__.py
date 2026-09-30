"""Part III (KLS, moment-map/CMH route) -- **exponential cones**, the second solvable family.

`def:exponential-cone`: for a centered convex body ``K`` in ``R^{n-1}`` and ``beta >= n``,
``mu_{K,beta}`` is the law of ``X = S(1,U)`` with ``S ~ Gamma(beta,1)`` and ``U ~ Unif(K)``
independent -- density proportional to ``x_1^{beta-n} e^{-x_1}`` on the cone over ``K``.
Its covariance is ``Sigma = beta e_1 e_1^T (+) beta(beta+1) Cov(U)``
(eq:cone-covariance) and, by `prop:cone-moment-map`, its canonical Stein kernel at
``x = (x_1, x_1 u)`` is

    tau = x_1 [[1, u^T], [u, u u^T + beta tau_K(u)]]              (eq:cone-stein-kernel)

with ``tau_K`` the canonical Stein kernel of ``Unif(K)``.  Four channels probe the two
statements that formula makes testable.

1. **cube cones, exact.**  ``K = [-1,1]^{n-1}``.  The gate matrix
   ``M = E[tau Sigma^{-1} tau]`` is assembled in exact rational arithmetic from the Gamma
   moments ``E S^k = beta (beta+1) ... (beta+k-1)`` and the uniform moments ``1/3, 1/5,
   1/7``, and matched against the closed form of `cor:cube-cone-gate-zero`,
   ``(1 + n/beta) (+) ((6 beta^2 + 11 beta + 5n + 4)/(5 beta(beta+1))) Id``.
2. **products of simplices and intervals, exact.**  ``K = Delta_{k_1} x ... x [-1,1]^s``.
   ``lambda_max`` of the pencil ``(M, Sigma)`` is *decided* exactly: a symmetric-pivot
   LDL^T of ``c Sigma - M`` proves ``<= c``, and a negative pivot returns the exact
   rational direction that violates it.  Anchor: the cone over ``Delta_{n-1}`` at
   ``beta = n`` is a linear image of ``n`` i.i.d. exponentials, so ``M = 2 Sigma`` exactly.
3. **ball cones, directional.**  ``K`` a Euclidean ball: the radial moment-map ODE
   ``Lambda'(s)^m = nu(B_s)`` is integrated numerically, giving ``tau_B`` and the
   transverse gate value by quadrature.  Quadrature is `directional`, always.
4. **CMH Galerkin, exact matrices + floating eigenvalue + exact witness.**  The full CMH
   quotient of `def:cmh` on polynomials of ``x`` of total degree ``<= d``.  Both moment
   matrices are exact; the largest generalized eigenvalue is floating, and its
   rationalized eigenvector is re-evaluated exactly to give one certified test function.

**Thresholds, fixed before the run.**  An exact rational Rayleigh lower bound above ``2``
for the gate pencil would contradict `conj:gate-zero-sharp`; above ``4`` it would
contradict `conj:gate-zero` and hence ``CMH(4)``.  An exact Galerkin lower bound above
``4`` at ``n >= 3``, stable under one degree refinement, would be a refutation candidate
for ``CMH(4)`` itself (`cor:cmh-product-saturation`, `conj:cmh-second-variation`).

**What this target cannot decide.**  Everything is computed *from* eq:cone-stein-kernel,
whose ledger node `prop:cone-moment-map` is `open`: a disagreement is as likely to
indict the formula as the conjecture.  Gate zero is necessary for ``CMH(4)`` and never
sufficient; passing a finite family of bases supports no universal statement; and an
exact contradiction emitted here is a candidate for the proof/refutation channel, never
a status change (CLAUDE.md constraint 2).  There is no Monte Carlo anywhere in this
module, and determinism is not a rigor certificate.
"""
from __future__ import annotations

import itertools
from fractions import Fraction

from ....comparison import compare_directional, matches
from ....contract import RunResult, lift_observations
from . import ball as ball_mod
from . import bases
from . import gate
from . import galerkin as galerkin_mod
from . import linalg as la
from . import polys
from .exact import (
    compare_exact_fraction as _compare_exact_fraction,
    pencil_certificate as _pencil_certificate,
    test_function_certificate as _test_function_certificate,
)

SHARP_GATE_BOUND = Fraction(2)
GATE_ZERO_BOUND = Fraction(4)
CMH_BOUND = Fraction(4)

RATIONAL_WITNESS_MAX_DENOMINATOR = 1_000_000

#: channel 1 -- cube cones, and the beta values swept for each ambient dimension.
CUBE_NS = (2, 3, 4, 5, 8)
CUBE_BETA_RULES = ("n", "n+1", "2n", "5n")

#: channel 2 -- product bases Delta_{k_1} x ... x Delta_{k_r} x [-1,1]^s.
PRODUCT_SIMPLEX_DIMS = (1, 2, 3)
PRODUCT_MAX_BLOCKS = 3
PRODUCT_MAX_INTERVALS = 3
PRODUCT_MAX_M = 7
PRODUCT_BETA_RULES = ("n", "n+1", "2n", "5n")
#: single-block simplex bases beyond the product box, where the transverse sector is
#: furthest from the axis value and the beta -> infinity limit is the base's own gate ratio.
PRODUCT_EXTRA_SIMPLEX_DIMS = (4, 5, 6, 8, 12)

#: channel 3 -- ball cones (quadrature).
BALL_MS = (1, 2, 3, 5, 10)

#: channel 4 -- (base kind, base parameter, beta rule, degrees).
GALERKIN_SPECS = (
    ("cube", 1, "n", (2, 3, 4, 5, 6, 7, 8, 9, 10)),
    ("simplex", 1, "n", (2, 3, 4, 5)),
    ("cube", 2, "n", (2, 3, 4, 5, 6)),
    ("simplex", 2, "n", (2, 3, 4, 5, 6)),
    ("cube", 2, "n+1", (2, 3, 4, 5)),
    ("cube", 2, "2n", (2, 3, 4)),
    ("simplex", 3, "n", (2, 3, 4, 5)),
    ("cube", 3, "n", (2, 3, 4, 5)),
)

BALL_DIRECTIONAL_REL_TOL = 1e-9
GALERKIN_DIRECTIONAL_REL_TOL = 1e-9
GALERKIN_CHEBYSHEV_REL_TOL = 1e-9


def is_exponential_product(base_kind: str, parameter: int, beta: int, n: int) -> bool:
    """Is this cone a linear image of ``n`` i.i.d. centered exponentials?

    Exactly the ``beta = n`` cones over a simplex: ``S ~ Gamma(n)`` and
    ``P ~ Dir(1,...,1)`` make ``S P_i`` i.i.d. ``Exp(1)``.  The one-dimensional interval
    base is the same body as ``Delta_1``, so the ``m = 1`` cube at ``beta = 2`` qualifies
    too.
    """
    if beta != n:
        return False
    return base_kind == "simplex" or (base_kind == "cube" and parameter == 1)


def _beta_for(rule: str, n: int) -> int:
    return {"n": n, "n+1": n + 1, "2n": 2 * n, "5n": 5 * n}[rule]


def cube_closed_form(n: int, beta: int):
    """`cor:cube-cone-gate-zero`, exactly: the axis and transverse normalized gate values."""
    return (Fraction(beta + n, beta),
            Fraction(6 * beta * beta + 11 * beta + 5 * n + 4, 5 * beta * (beta + 1)))


def product_bases(max_m=PRODUCT_MAX_M, simplex_dims=PRODUCT_SIMPLEX_DIMS,
                  max_blocks=PRODUCT_MAX_BLOCKS, max_intervals=PRODUCT_MAX_INTERVALS,
                  extra_simplex_dims=PRODUCT_EXTRA_SIMPLEX_DIMS):
    """Every base ``Delta_{k_1} x ... x Delta_{k_r} x [-1,1]^s`` inside the stated box."""
    out = [bases.simplex(k) for k in extra_simplex_dims]
    for blocks in range(max_blocks + 1):
        for dims in itertools.combinations_with_replacement(simplex_dims, blocks):
            for intervals in range(max_intervals + 1):
                m = sum(dims) + intervals
                if not 1 <= m <= max_m:
                    continue
                out.append(bases.product_base(simplex_dims=dims, intervals=intervals))
    return out


def gate_instance(base, beta: int, family: str, instance: str):
    """Exact gate pencil of one cone, with the decided Loewner verdicts at 2 and at 4."""
    M, Sigma = gate.gate_pencil(base, beta)
    n = base.m + 1
    vals, top = gate.pencil_spectrum(M, Sigma)
    rational_top = gate.rationalize(top, RATIONAL_WITNESS_MAX_DENOMINATOR)
    source = {"instance": instance, "base": base.describe(), "beta": int(beta),
              "n": n, "family": family,
              "stein_kernel": "eq:cone-stein-kernel (prop:cone-moment-map, ledger status open)",
              "rationalization_max_denominator": RATIONAL_WITNESS_MAX_DENOMINATOR}
    verdicts = {}
    for label, bound in (("sharp", SHARP_GATE_BOUND), ("gate_zero", GATE_ZERO_BOUND)):
        lower, is_psd, certificate = _pencil_certificate(
            M, Sigma, bound, rational_top, dict(source),
            inline_matrices=(label == "sharp"))
        verdicts[label] = {"bound": str(bound), "loewner_psd": bool(is_psd),
                           "exact_rayleigh_lower": float(lower),
                           "exact_rayleigh_lower_fraction": str(lower),
                           "lower": lower, "certificate": certificate}
    axis_exact = M[0][0] / Sigma[0][0]
    return {"instance": instance, "family": family, "base": base.describe(),
            "beta": int(beta), "n": n, "m": base.m,
            "axis_exact_fraction": str(axis_exact), "axis_exact": float(axis_exact),
            "axis_matches_one_plus_n_over_beta": axis_exact == Fraction(beta + n, beta),
            "pencil_spectrum_directional": [float(v) for v in vals],
            "lambda_max_directional": float(vals[-1]),
            "M": M, "Sigma": Sigma, "verdicts": verdicts}


def _gate_records(row):
    """One comparison record per bound, with the exact verdict lifted to the contract fields."""
    out = []
    for label, bound, node in (("sharp", SHARP_GATE_BOUND, "conj:gate-zero-sharp"),
                               ("gate_zero", GATE_ZERO_BOUND, "conj:gate-zero")):
        verdict = row["verdicts"][label]
        comparison = _compare_exact_fraction(
            f"cone gate lambda_max(E[tau Sigma^-1 tau], Sigma) <= {bound} ({node})",
            row["instance"], bound, verdict["lower"], verdict["certificate"],
            note="Exact rational pencil. A complete LDL^T of bound*Sigma - M with "
                 "nonnegative pivots decides the inequality; the recorded lower bound is "
                 "the Rayleigh quotient of the certificate's witness.")
        record = comparison.observation("cone-gate-pencil")
        record["detail"].update({
            "family": row["family"], "base": row["base"], "beta": row["beta"],
            "n": row["n"], "m": row["m"], "node": node,
            "axis_exact_fraction": row["axis_exact_fraction"],
            "axis_matches_one_plus_n_over_beta": row["axis_matches_one_plus_n_over_beta"],
            "loewner_psd": verdict["loewner_psd"],
            "beta_rule": row.get("beta_rule"),
            "closed_form_transverse_fraction": row.get("closed_form_transverse_fraction"),
            "closed_form_exact_match": row.get("closed_form_exact_match"),
            "lambda_max_directional": row["lambda_max_directional"],
            "pencil_spectrum_directional": row["pencil_spectrum_directional"],
            "exact_rayleigh_lower_fraction": verdict["exact_rayleigh_lower_fraction"],
            "certificate": verdict["certificate"],
        })
        out.append(record)
    return out


def galerkin_instance(base, beta: int, degree: int, instance: str):
    """One Galerkin space: exact matrices, floating eigenvalue, exact certified witness."""
    mom = polys.ConeMoments(base, beta)
    built = galerkin_mod.assemble(base, beta, degree, mom)
    vals, top, condition = galerkin_mod.top_eigenpair(built["N"], built["D"])
    vector = gate.rationalize(top, RATIONAL_WITNESS_MAX_DENOMINATOR)
    source = {"instance": instance, "base": base.describe(), "beta": int(beta),
              "degree": int(degree), "basis": "monomials of x of total degree 1..d",
              "exponents": [list(e) for e in built["exponents"]],
              "rationalization_max_denominator": RATIONAL_WITNESS_MAX_DENOMINATOR}
    lower, certificate = _test_function_certificate(built["N"], built["D"], vector, source)
    basis_residual = max(
        abs(galerkin_mod.bochner_residual(
            built, mom, [Fraction(int(k == i)) for k in range(built["basis_size"])]))
        for i in range(built["basis_size"]))
    witness_residual = abs(galerkin_mod.bochner_residual(built, mom, vector))
    axis = built["exponents"].index(tuple([1] + [0] * base.m))
    axis_vector = [Fraction(int(k == axis)) for k in range(built["basis_size"])]
    axis_value = (la.quadratic(built["N"], axis_vector)
                  / la.quadratic(built["D"], axis_vector))
    return {"instance": instance, "base": base.describe(), "beta": int(beta),
            "n": base.m + 1, "degree": int(degree), "basis_size": built["basis_size"],
            "q_max_directional": float(vals[-1]),
            "q_min_directional": float(vals[0]),
            "exact_test_function_lower": float(lower),
            "exact_test_function_lower_fraction": str(lower),
            "axis_test_function_exact_fraction": str(axis_value),
            "axis_matches_one_plus_n_over_beta":
                axis_value == Fraction(beta + base.m + 1, beta),
            "bochner_residual_basis_max_is_zero": basis_residual == 0,
            "bochner_residual_witness_is_zero": witness_residual == 0,
            "denominator_condition_number": condition,
            "lower": lower, "certificate": certificate}


def run_records(seed: int = 0, cube_ns=CUBE_NS, cube_beta_rules=CUBE_BETA_RULES,
                product_max_m: int = PRODUCT_MAX_M,
                product_beta_rules=PRODUCT_BETA_RULES,
                ball_ms=BALL_MS, galerkin_specs=GALERKIN_SPECS,
                run_ball: bool = True):
    """Deterministic exponential-cone battery. ``seed`` is recorded for provenance only."""
    cube_ns = tuple(int(n) for n in cube_ns)
    ball_ms = tuple(int(m) for m in ball_ms)
    records: list[dict] = []
    calibration_ok = True

    # ---- channel 1: cube cones, exact -----------------------------------------------
    cube_rows, cube_mismatch = [], 0
    for n in cube_ns:
        base = bases.cube(n - 1)
        for rule in cube_beta_rules:
            beta = _beta_for(rule, n)
            row = gate_instance(base, beta, "cube", f"cone-cube-n{n}-b{beta}")
            axis, transverse = cube_closed_form(n, beta)
            M, Sigma = row["M"], row["Sigma"]
            ok = M[0][0] == axis * Sigma[0][0]
            for i in range(1, n):
                ok = ok and M[0][i] == 0 and M[i][0] == 0
                for j in range(1, n):
                    ok = ok and M[i][j] == transverse * Sigma[i][j]
            cube_mismatch += 0 if ok else 1
            row["closed_form_axis_fraction"] = str(axis)
            row["closed_form_transverse_fraction"] = str(transverse)
            row["closed_form_transverse"] = float(transverse)
            row["closed_form_exact_match"] = bool(ok)
            row["beta_rule"] = rule
            cube_rows.append(row)

    v = matches("cal-cmh-cone-cube-closed-form",
                "exact gate matrix of every cube cone == cor:cube-cone-gate-zero",
                1.0 + cube_mismatch, 1.0, rel_tol=0.0)
    calibration_ok = calibration_ok and v.outcome == "match"
    records.append({"kind": "calibration", "channel": "cube",
                    **v.observation("calibration"),
                    "instances_checked": len(cube_rows), "mismatches": cube_mismatch,
                    "note": "Fraction-exact matrix identity, entry by entry, against "
                            "(1+n/beta) (+) ((6b^2+11b+5n+4)/(5b(b+1))) Id."})

    # ---- channel 2: products of simplices and intervals, exact -----------------------
    product_rows = []
    for base in product_bases(max_m=product_max_m):
        n = base.m + 1
        for rule in product_beta_rules:
            beta = _beta_for(rule, n)
            row = gate_instance(base, beta, "product",
                                f"cone-{base.name}-n{n}-b{beta}")
            row["beta_rule"] = rule
            product_rows.append(row)

    simplex_mismatch = 0
    simplex_checked = []
    for k in range(1, 6):
        n = k + 1
        M, Sigma = gate.gate_pencil(bases.simplex(k), n)
        exact_double = all(M[i][j] == 2 * Sigma[i][j]
                           for i in range(n) for j in range(n))
        simplex_mismatch += 0 if exact_double else 1
        simplex_checked.append({"k": k, "n": n, "beta": n,
                                "M_equals_two_Sigma": bool(exact_double)})
    v = matches("cal-cmh-cone-simplex-product",
                "cone over Delta_{n-1} at beta = n has M == 2 Sigma exactly",
                1.0 + simplex_mismatch, 1.0, rel_tol=0.0)
    calibration_ok = calibration_ok and v.outcome == "match"
    records.append({"kind": "calibration", "channel": "product-base",
                    **v.observation("calibration"), "rows": simplex_checked,
                    "note": "S P_i are i.i.d. Exp(1) when S ~ Gamma(n) and P ~ Dir(1,..,1), "
                            "so the cone is a linear image of n centered exponentials and "
                            "saturates eq:gate-zero-sharp in every direction."})

    axis_mismatch = sum(0 if row["axis_matches_one_plus_n_over_beta"] else 1
                        for row in cube_rows + product_rows)
    v = matches("cal-cmh-cone-axis",
                "axis gate value == 1 + n/beta for every base (prop:cone-linear-sector)",
                1.0 + axis_mismatch, 1.0, rel_tol=0.0)
    calibration_ok = calibration_ok and v.outcome == "match"
    records.append({"kind": "calibration", "channel": "cube+product-base",
                    **v.observation("calibration"),
                    "instances_checked": len(cube_rows) + len(product_rows),
                    "mismatches": axis_mismatch,
                    "note": "the axis column of tau is the position vector, so this value "
                            "is base-independent; it is the oracle for both exact channels."})

    exceeded_sharp, exceeded_gate_zero = [], []
    max_exact_lower = 0.0
    for row in cube_rows + product_rows:
        for record in _gate_records(row):
            records.append(record)
            if record["outcome"] == "contradicts":
                (exceeded_sharp if record["detail"]["node"] == "conj:gate-zero-sharp"
                 else exceeded_gate_zero).append(record["instance"])
        max_exact_lower = max(max_exact_lower,
                              row["verdicts"]["sharp"]["exact_rayleigh_lower"])

    # ---- channel 3: ball cones, quadrature (directional) -----------------------------
    ball_rows: list[dict] = []
    ball_exceeded: list[str] = []
    if run_ball:
        profiles = {m: ball_mod.radial_profile(m) for m in ball_ms}
        trace_worst = max(ball_mod.stein_trace_residual(p) for p in profiles.values())
        v = matches("cal-cmh-cone-ball-trace",
                    "E[alpha] + (m-1) E[beta_perp] == E|U|^2 for the ball moment map",
                    1.0 + trace_worst, 1.0, rel_tol=1e-8)
        calibration_ok = calibration_ok and v.outcome == "match"
        records.append({"kind": "calibration", "channel": "ball",
                        **v.observation("calibration"),
                        "m_values": list(ball_ms),
                        "max_relative_residual": float(trace_worst),
                        "note": "the Stein normalisation E tau_K = Cov(U), traced; it is the "
                                "only closed form available for m >= 2."})

        if 1 in profiles:
            kernel_residual = ball_mod.one_dimensional_kernel_residual(profiles[1])
            v = matches("cal-cmh-cone-ball-1d",
                        "m = 1 radial moment map reproduces tau = (R^2 - r^2)/2, R = 2",
                        1.0 + kernel_residual, 1.0, rel_tol=1e-8)
            calibration_ok = calibration_ok and v.outcome == "match"
            records.append({"kind": "calibration", "channel": "ball",
                            **v.observation("calibration"),
                            "R": float(profiles[1]["R"]),
                            "max_relative_residual": float(kernel_residual),
                            "note": "Lambda' = 2 tanh s solves the m = 1 radial ODE."})

            cross = max(abs(ball_mod.gate_ratios(profiles[1], b)["transverse"]
                            - float(cube_closed_form(2, b)[1])) for b in (2, 3, 5, 10))
            v = matches("cal-cmh-cone-ball-vs-cube",
                        "m = 1 ball cone == n = 2 cube cone (cor:cube-cone-gate-zero)",
                        1.0 + cross, 1.0, rel_tol=1e-8)
            calibration_ok = calibration_ok and v.outcome == "match"
            records.append({"kind": "calibration", "channel": "ball",
                            **v.observation("calibration"),
                            "max_abs_error": float(cross),
                            "note": "cross-channel: the m = 1 ball IS a centered interval, so "
                                    "the quadrature channel must reproduce the exact channel."})

        for m in ball_ms:
            profile = profiles[m]
            n = m + 1
            for beta in (n, n + 1, 2 * n):
                ratios = ball_mod.gate_ratios(profile, beta)
                instance = f"cone-ball-m{m}-b{beta}"
                comparison = compare_directional(
                    "cone gate lambda_max <= 2 (conj:gate-zero-sharp)", instance,
                    float(SHARP_GATE_BOUND), ratios["lambda_max"],
                    rel_tol=BALL_DIRECTIONAL_REL_TOL,
                    note="radial moment-map ODE integrated by adaptive Runge-Kutta; "
                         "quadrature, hence directional only.")
                if comparison.outcome == "contradicts":
                    ball_exceeded.append(instance)
                record = comparison.observation("cone-ball-gate")
                record["detail"].update({
                    "m": m, "n": n, "beta": beta, "R": float(profile["R"]),
                    "axis": ratios["axis"], "transverse": ratios["transverse"],
                    "transverse_margin_below_two": 2.0 - ratios["transverse"],
                    "sigma_sq": ratios["sigma_sq"],
                    "ode_rtol": profile["rtol"], "ode_atol": profile["atol"],
                    "ode_s_max": profile["s_max"],
                    "ode_tail_estimate": profile["tail_estimate"],
                    "node": "conj:gate-zero-sharp"})
                records.append(record)
                ball_rows.append({"m": m, "beta": beta, **{k: ratios[k] for k in
                                                           ("axis", "transverse",
                                                            "lambda_max")}})

    # ---- channel 4: CMH Galerkin ------------------------------------------------------
    galerkin_rows = []
    galerkin_exact_exceeded, galerkin_directional_exceeded = [], []
    for kind, parameter, rule, degrees in galerkin_specs:
        base = bases.cube(parameter) if kind == "cube" else bases.simplex(parameter)
        n = base.m + 1
        beta = _beta_for(rule, n)
        for degree in degrees:
            instance = f"cone-{base.name}-n{n}-b{beta}-d{degree}"
            row = galerkin_instance(base, beta, degree, instance)
            row["base_kind"] = kind
            row["is_exponential_product"] = is_exponential_product(kind, parameter, beta, n)
            galerkin_rows.append(row)
            exact_comparison = _compare_exact_fraction(
                f"cone CMH quotient <= {CMH_BOUND} (rem:cmh-normalization / CMH(4))",
                instance, CMH_BOUND, row["lower"], row["certificate"],
                note="one explicit rational test function evaluated from exact moment "
                     "matrices; a lower bound for C_CMH provided the polynomial span lies "
                     "in the operator core, which the Bochner residual tests.")
            record = exact_comparison.observation("cone-cmh-galerkin")
            record["detail"].update({
                "base": row["base"], "base_kind": kind, "beta": beta, "n": n,
                "degree": degree, "basis_size": row["basis_size"],
                "q_max_directional": row["q_max_directional"],
                "exact_test_function_lower_fraction":
                    row["exact_test_function_lower_fraction"],
                "axis_test_function_exact_fraction":
                    row["axis_test_function_exact_fraction"],
                "bochner_residual_basis_max_is_zero":
                    row["bochner_residual_basis_max_is_zero"],
                "bochner_residual_witness_is_zero": row["bochner_residual_witness_is_zero"],
                "denominator_condition_number": row["denominator_condition_number"],
                "is_exponential_product": row["is_exponential_product"],
                "exponential_product_closed_form":
                    galerkin_mod.exponential_product_galerkin_value(degree)
                    if row["is_exponential_product"] else None,
                "certificate": row["certificate"], "node": "rem:cmh-normalization"})
            records.append(record)
            if exact_comparison.outcome == "contradicts":
                galerkin_exact_exceeded.append(instance)
            directional = compare_directional(
                f"cone CMH Galerkin q_max <= {CMH_BOUND}", instance,
                float(CMH_BOUND), row["q_max_directional"],
                rel_tol=GALERKIN_DIRECTIONAL_REL_TOL,
                note="largest generalized eigenvalue from scipy.linalg.eigh on exactly "
                     "assembled matrices; the eigenvalue itself is uncertified.")
            if directional.outcome == "contradicts":
                galerkin_directional_exceeded.append(instance)
            records.append({"kind": "cone-cmh-galerkin-directional", "channel": "galerkin",
                            **directional.observation("cone-cmh-galerkin-directional"),
                            "degree": degree, "beta": beta, "n": n})

    axis_galerkin_mismatch = sum(0 if row["axis_matches_one_plus_n_over_beta"] else 1
                                 for row in galerkin_rows)
    v = matches("cal-cmh-cone-galerkin-axis",
                "CMH quotient at g = x_1 equals 1 + n/beta exactly",
                1.0 + axis_galerkin_mismatch, 1.0, rel_tol=0.0)
    calibration_ok = calibration_ok and v.outcome == "match"
    records.append({"kind": "calibration", "channel": "galerkin",
                    **v.observation("calibration"),
                    "instances_checked": len(galerkin_rows),
                    "mismatches": axis_galerkin_mismatch,
                    "note": "prop:cone-linear-sector (ii); it also ties channel 4 to the "
                            "exact gate channels."})

    bochner_bad = sum(0 if (row["bochner_residual_basis_max_is_zero"]
                            and row["bochner_residual_witness_is_zero"]) else 1
                      for row in galerkin_rows)
    v = matches("cal-cmh-cone-bochner",
                "prop:cmh-bochner holds exactly on every polynomial test space used",
                1.0 + bochner_bad, 1.0, rel_tol=0.0)
    calibration_ok = calibration_ok and v.outcome == "match"
    records.append({"kind": "calibration", "channel": "galerkin",
                    **v.observation("calibration"),
                    "instances_checked": len(galerkin_rows), "mismatches": bochner_bad,
                    "note": "E(L_mu g)^2 == E[<tau grad g, grad g> + Tr(tau D^2g tau D^2g)] "
                            "in exact arithmetic; a nonzero residual would mean the "
                            "polynomial span leaves the operator core and the Galerkin "
                            "value would not be a lower bound."})

    product_endpoint = [row for row in galerkin_rows if row["is_exponential_product"]]
    endpoint_ok = all(row["exact_test_function_lower"] <= 4.0 + 1e-12
                      for row in product_endpoint)
    v = matches("cal-cmh-cone-product-endpoint",
                "exponential-product cones stay at or below the exact CMH value 4",
                1.0 + (0 if endpoint_ok else 1), 1.0, rel_tol=0.0)
    calibration_ok = calibration_ok and v.outcome == "match"
    records.append({"kind": "calibration", "channel": "galerkin",
                    **v.observation("calibration"),
                    "rows": [{"instance": row["instance"], "degree": row["degree"],
                              "q_max_directional": row["q_max_directional"],
                              "exact_test_function_lower": row["exact_test_function_lower"]}
                             for row in product_endpoint],
                    "note": "thm:cmh-product gives C_CMH = 4 exactly there; the Galerkin "
                            "values must climb toward 4 from below with the degree."})

    chebyshev_worst = max(
        [abs(row["q_max_directional"]
             - galerkin_mod.exponential_product_galerkin_value(row["degree"]))
         / galerkin_mod.exponential_product_galerkin_value(row["degree"])
         for row in product_endpoint], default=0.0)
    v = matches("cal-cmh-cone-galerkin-chebyshev",
                "degree-d Galerkin CMH of an exponential product == 2 + 2 cos(pi/(d+1))",
                1.0 + chebyshev_worst, 1.0, rel_tol=GALERKIN_CHEBYSHEV_REL_TOL)
    calibration_ok = calibration_ok and v.outcome == "match"
    records.append({"kind": "calibration", "channel": "galerkin",
                    **v.observation("calibration"),
                    "instances_checked": len(product_endpoint),
                    "max_relative_error": float(chebyshev_worst),
                    "rows": [{"instance": row["instance"], "degree": row["degree"],
                              "q_max_directional": row["q_max_directional"],
                              "closed_form":
                                  galerkin_mod.exponential_product_galerkin_value(
                                      row["degree"])}
                             for row in product_endpoint],
                    "note": "Laguerre closed form: on span{L_1..L_d} the CMH quotient of a "
                            "centered exponential is 2 - 2 (sum w_k w_{k-1})/(sum w_k^2), "
                            "whose maximum is 2 + 2 cos(pi/(d+1)) -> 4. C_CMH and the "
                            "total-degree spaces are affine invariant, so the same number "
                            "anchors every exponential-product cone in every dimension."})

    # ---- summary ----------------------------------------------------------------------
    max_galerkin_exact = max([row["exact_test_function_lower"] for row in galerkin_rows],
                             default=0.0)
    max_galerkin_directional = max([row["q_max_directional"] for row in galerkin_rows],
                                   default=0.0)
    max_ball_transverse = max([row["transverse"] for row in ball_rows], default=0.0)
    summary = {
        "calibration_passed": bool(calibration_ok),
        "deterministic": True, "monte_carlo_used": False,
        "sharp_gate_bound": float(SHARP_GATE_BOUND),
        "gate_zero_bound": float(GATE_ZERO_BOUND),
        "cmh_bound": float(CMH_BOUND),
        "n_cube_instances": len(cube_rows),
        "n_product_instances": len(product_rows),
        "n_ball_instances": len(ball_rows),
        "n_galerkin_instances": len(galerkin_rows),
        "max_gate_exact_rayleigh_lower": max_exact_lower,
        "gate_sharp_exact_exceedance_instances": exceeded_sharp,
        "gate_zero_exact_exceedance_instances": exceeded_gate_zero,
        "gate_sharp_decided_by_loewner_for_every_instance": True,
        "max_ball_transverse_directional": max_ball_transverse,
        "ball_directional_exceedance_instances": ball_exceeded,
        "max_galerkin_exact_test_function_lower": max_galerkin_exact,
        "max_galerkin_q_directional": max_galerkin_directional,
        "galerkin_exact_exceedance_instances": galerkin_exact_exceeded,
        "galerkin_directional_exceedance_instances": galerkin_directional_exceeded,
        "proof_status": "no-proof; gate zero is NECESSARY for CMH(4), never sufficient, and "
                        "every value here is computed from the open node prop:cone-moment-map",
    }
    records.append({"kind": "summary", "target": "cmh-cone", **summary,
                    "note": "Exact arithmetic decides each stated inequality on each stated "
                            "instance and nothing more: a finite family of bases supports no "
                            "universal statement, and an exact exceedance is a refutation "
                            "CANDIDATE for the proof/review channel (CLAUDE.md constraint 2)."})

    config = {
        "cube_ns": list(cube_ns), "cube_beta_rules": list(cube_beta_rules),
        "product_max_m": int(product_max_m),
        "product_beta_rules": list(product_beta_rules),
        "product_simplex_dims": list(PRODUCT_SIMPLEX_DIMS),
        "product_extra_simplex_dims": list(PRODUCT_EXTRA_SIMPLEX_DIMS),
        "product_max_blocks": PRODUCT_MAX_BLOCKS,
        "product_max_intervals": PRODUCT_MAX_INTERVALS,
        "ball_ms": list(ball_ms) if run_ball else [],
        "run_ball": bool(run_ball),
        "galerkin_specs": [[kind, parameter, rule, list(degrees)]
                           for kind, parameter, rule, degrees in galerkin_specs],
        "battery": {
            "schema_version": 1,
            "stein_kernel_source": "eq:cone-stein-kernel (prop:cone-moment-map, open)",
            "exact_arithmetic": "fractions.Fraction throughout channels 1, 2, 4",
            "rational_witness_max_denominator": RATIONAL_WITNESS_MAX_DENOMINATOR,
            "floating_eigensolver": "scipy.linalg.eigh (generalized, diagonally prescaled)",
            "ball_quadrature": {"method": "DOP853", "rtol": 1e-12, "atol": 1e-14,
                                "s0": 1e-6, "tail_tol": 1e-15},
            "thresholds": {"sharp_gate": 2, "gate_zero": 4, "cmh": 4},
        },
    }
    return RunResult(lift_observations(records), config=config, summary=summary)


def selftest(rng):
    """Closed-form anchors only; a green list calibrates the code, never a claim."""
    checks = []

    worst = 0
    for m in (1, 2, 3, 4):
        for base in (bases.cube(m), bases.simplex(m),
                     bases.product_base(simplex_dims=(m,), intervals=1)):
            tau, cov = base.tau(), base.cov()
            for i in range(base.m):
                for j in range(base.m):
                    got = sum((c * base.moment(b) for (_, b), c in tau[i][j].items()),
                              Fraction(0))
                    worst += 0 if got == cov[i][j] else 1
    checks.append(("cone base: E[tau_K] == Cov(U) exactly for every block type", worst == 0))

    bad = 0
    for n in (2, 3, 4, 5):
        base = bases.cube(n - 1)
        for beta in (n, n + 1, 2 * n):
            M, Sigma = gate.gate_pencil(base, beta)
            axis, transverse = cube_closed_form(n, beta)
            bad += 0 if M[0][0] == axis * Sigma[0][0] else 1
            for i in range(1, n):
                bad += 0 if M[0][i] == 0 else 1
                for j in range(1, n):
                    bad += 0 if M[i][j] == transverse * Sigma[i][j] else 1
    checks.append(("cone cube: exact gate matrix == cor:cube-cone-gate-zero", bad == 0))

    bad = 0
    for k in (1, 2, 3, 4):
        n = k + 1
        M, Sigma = gate.gate_pencil(bases.simplex(k), n)
        bad += 0 if all(M[i][j] == 2 * Sigma[i][j]
                        for i in range(n) for j in range(n)) else 1
    checks.append(("cone simplex: beta = n gives M == 2 Sigma exactly (exponential product)",
                   bad == 0))

    _, _, witness = la.psd_certificate([[Fraction(1), Fraction(2)],
                                        [Fraction(2), Fraction(1)]])
    checks.append(("cone Loewner: an indefinite matrix returns a negative witness",
                   witness is not None
                   and la.quadratic([[Fraction(1), Fraction(2)],
                                     [Fraction(2), Fraction(1)]], witness) < 0))

    profile = ball_mod.radial_profile(1)
    residual = ball_mod.one_dimensional_kernel_residual(profile)
    cross = max(abs(ball_mod.gate_ratios(profile, b)["transverse"]
                    - float(cube_closed_form(2, b)[1])) for b in (2, 3, 5))
    checks.append((f"cone ball: m = 1 ODE reproduces tau = (4 - r^2)/2 and the cube cone "
                   f"(residuals {residual:.2e}, {cross:.2e})",
                   residual <= 1e-8 and cross <= 1e-8))

    worst = 0.0
    for base, beta in ((bases.cube(1), 2), (bases.simplex(1), 2), (bases.simplex(2), 3)):
        for degree in (2, 3, 4):
            built = galerkin_mod.assemble(base, beta, degree,
                                          polys.ConeMoments(base, beta))
            vals, _, _ = galerkin_mod.top_eigenpair(built["N"], built["D"])
            want = galerkin_mod.exponential_product_galerkin_value(degree)
            worst = max(worst, abs(float(vals[-1]) - want) / want)
    checks.append((f"cone CMH: exponential-product cones give 2 + 2 cos(pi/(d+1)) "
                   f"(max rel err {worst:.2e})", worst <= 1e-9))

    mom = polys.ConeMoments(bases.cube(1), 2)
    built = galerkin_mod.assemble(bases.cube(1), 2, 3, mom)
    axis = built["exponents"].index((1, 0))
    v = [Fraction(int(k == axis)) for k in range(built["basis_size"])]
    q_axis = la.quadratic(built["N"], v) / la.quadratic(built["D"], v)
    residuals = max(abs(galerkin_mod.bochner_residual(
        built, mom, [Fraction(int(k == i)) for k in range(built["basis_size"])]))
        for i in range(built["basis_size"]))
    vals, _, _ = galerkin_mod.top_eigenpair(built["N"], built["D"])
    checks.append((f"cone CMH: g = x_1 gives exactly 1 + n/beta = {q_axis}, Bochner exact, "
                   f"degree-3 q_max = {float(vals[-1]):.4f} <= 4",
                   q_axis == Fraction(2) and residuals == 0
                   and float(vals[-1]) <= 4.0 + 1e-9))
    return checks
