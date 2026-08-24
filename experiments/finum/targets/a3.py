"""A3 — heavy-tailed posteriors beyond classical LSI. Obstruction: obs:heavy-tail-no-classical.

Heavy (polynomial) tails admit no classical Poincare; the correct object is a WEIGHTED Poincare
Var_mu(f) <= C int a |f'|^2 dmu with a(x) ~ 1+x^2. Two anchors:
  * cal-cauchy   : generalized Cauchy mu_beta ∝ (1+x^2)^{-beta}; the weighted gap equals the
                   closed form C_P^w = 1/lambda_{beta,d} (thm:a3-student). EXACT calibration.
  * stress-student : Student-t_nu; unweighted (classical) gap diverges while the weighted gap is
                     finite and matches 1/lambda_{(nu+1)/2,1}.
  * stress-horseshoe : diagnostics for the proved sharp identity C_HS=4, including exact scale
                       covariance and the parity-separated Barta residual.
"""
from __future__ import annotations

import numpy as np
from scipy.special import exp1

from ..constants import poincare_1d_fem, hardy_1d
from ..verdict import matches

OBSTRUCTION = "obs:heavy-tail-no-classical"


def lambda_beta_d(beta: float, d: int) -> float:
    """Sharp weighted spectral gap of mu_beta ∝ (1+||x||^2)^{-beta} (thm:a3-student)."""
    if d == 1:
        if 0.5 < beta <= 1.5:
            return (beta - 0.5) ** 2
        return 2 * (beta - 1)
    h = d / 2
    if h < beta <= h + 2:
        return (beta - h) ** 2
    if h + 2 <= beta <= d + 1:
        return 4 * (beta - h - 1)
    return 2 * (beta - 1)


def sinh_grid(x_max: float, n: int, k: float = 6.0) -> np.ndarray:
    """Grid dense near 0, wide in the tails (for heavy-tailed densities + log poles)."""
    u = np.linspace(-1.0, 1.0, n)
    return x_max * np.sinh(k * u) / np.sinh(k)


# ---- calibration: generalized Cauchy weighted gap == 1/lambda_{beta,1} ----------

def cal_cauchy_gap(beta: float, x_max: float = 3000.0, n: int = 10001) -> float:
    xs = sinh_grid(x_max, n)
    U = lambda x: beta * np.log1p(x ** 2)
    a = lambda x: 1.0 + x ** 2
    return poincare_1d_fem(U, xs, a=a)


# beta=1.5 is the branch boundary (both formulas give lambda=1); 2.5, 4.0 are branch 2,
# exact to <1%. (Branch-1 interiors beta<1.5 have infinite variance and converge slowly,
# so they are NOT used as exact calibration.)
CAUCHY_BETAS = [1.5, 2.5, 4.0]
CAL_TOL = 0.06


# ---- stress: Student-t classical-vs-weighted -----------------------------------

def student_C_norm(nu: float) -> float:
    """Sharp weighted C_P of 1D Student-t_nu with NORMALIZED weight 1+x^2/nu (thm:a3-student):
    4/nu for 0<nu<=2, nu/(nu-1) for nu>=2."""
    return 4.0 / nu if nu <= 2.0 else nu / (nu - 1.0)


def student_gaps(nu: float):
    """Finite-domain classical/weighted constants and the exact weighted constant.

    Polynomial tails analytically have no classical Poincare inequality.  Growth
    across the two finite domains is only a directional truncation diagnostic.  The
    normalized weight ``a=1+x^2/nu`` has the stated exact finite constant.
    """
    beta = (nu + 1) / 2
    U = lambda x: beta * np.log1p(x ** 2 / nu)
    a = lambda x: 1.0 + x ** 2 / nu
    classical_narrow = poincare_1d_fem(U, sinh_grid(60.0, 4001))
    classical_wide = poincare_1d_fem(U, sinh_grid(240.0, 4001))
    weighted = poincare_1d_fem(U, sinh_grid(3000.0, 10001), a=a)
    return classical_narrow, classical_wide, weighted, student_C_norm(nu)


# ---- stress: exact horseshoe marginal, factor-4 Hardy bracket ------------------

def _scaled_exp1(a: np.ndarray) -> np.ndarray:
    """Return exp(a) E1(a) without overflow in the polynomial-tail regime.

    The standard horseshoe marginal is proportional to
    ``exp(a) E1(a)``, where ``a=x**2/(2*tau**2)``.  Directly forming the
    exponential overflows on the wide grids needed for its Cauchy tail.  For
    ``a>50`` the alternating asymptotic expansion has ample accuracy for this
    diagnostic.
    """
    a = np.asarray(a, dtype=float)
    out = np.empty_like(a)
    small = a <= 50.0
    out[small] = np.exp(a[small]) * exp1(a[small])

    z = a[~small]
    # exp(z) E1(z) ~ z^{-1}(1-z^{-1}+2!z^{-2}-3!z^{-3}+...).
    inv = 1.0 / z
    series = np.ones_like(z)
    power = np.ones_like(z)
    factorial = 1.0
    sign = 1.0
    for k in range(1, 10):
        power *= inv
        factorial *= k
        sign *= -1.0
        series += sign * factorial * power
    out[~small] = inv * series
    return out


def horseshoe_density_shape(theta: np.ndarray, tau: float) -> np.ndarray:
    """Exact standard-horseshoe density up to the universal normalizer.

    If ``theta | lambda,tau ~ N(0,tau**2 lambda**2)`` and
    ``lambda ~ C+(0,1)``, then

        h_tau(theta) = [pi sqrt(2 pi) tau]^{-1} exp(a) E1(a),
        a = theta**2/(2 tau**2).

    The omitted universal factor cancels in both the Hardy functional and the
    FEM Rayleigh quotient.  The explicit ``1/tau`` is retained so that the
    numerical calculation respects the exact scaling law.
    """
    if tau <= 0:
        raise ValueError("tau must be positive")
    theta = np.asarray(theta, dtype=float)
    a = theta ** 2 / (2.0 * tau ** 2)
    return _scaled_exp1(a) / tau


def horseshoe_e1_rational_upper(a: np.ndarray) -> np.ndarray:
    """Global rational upper bound for ``exp(a) E1(a)`` used in the proved theorem.

    For ``a>0``, with ``H(a)=exp(a)E1(a)``, the analytic identity

        (a**2+5a+2) - a(a**2+6a+6) H(a)
          = 2 int_0^inf exp(-t)t**3/(a+t)**3 dt

    makes this a strict upper bound.  This function only evaluates the closed
    form; positivity is analytic, not inferred from the sampled diagnostic.
    """
    a = np.asarray(a, dtype=float)
    if np.any(a <= 0):
        raise ValueError("a must be positive")
    return (a ** 2 + 5.0 * a + 2.0) / (a * (a ** 2 + 6.0 * a + 6.0))


def horseshoe_odd_barta_residual_lower(y: np.ndarray) -> np.ndarray:
    """Certified closed-form lower residual in the odd intrinsic sector.

    In ``y=asinh(theta/tau)``, write ``q=exp(-W)`` and use the positive
    half-line test ``g(y)=sinh(y/2)``.  The quantity returned is the algebraic
    lower bound on

        -L g/g - 1/4 = (1/2)coth(y/2)[W'(y)-tanh(y/2)].

    It follows from the rational E1 bound and equals

        [c^2(c-1)^2+5c^2+2c+1] / [2c(c^4+8c^2-1)],
        c=cosh(|y|),

    which is strictly positive.  The formula extends continuously to 1/2 at
    ``y=0`` and avoids cancellation in the tail.
    """
    y = np.asarray(y, dtype=float)
    c = np.cosh(np.abs(y))
    c2 = c * c
    numerator = c2 * (c - 1.0) ** 2 + 5.0 * c2 + 2.0 * c + 1.0
    denominator = 2.0 * c * (c2 * c2 + 8.0 * c2 - 1.0)
    return numerator / denominator


def horseshoe_bracket(tau: float = 1.0, x_max: float = 400.0, n: int = 6001):
    """Exact horseshoe marginal with weight ``tau**2+theta**2``.

    ``x_max`` is a *standardized* cutoff: the physical grid is ``tau*x_max``.
    With the relative pole cutoff below, this makes the exact identities
    ``B_HS(tau)=B_HS(1)`` and ``C_HS(tau)=C_HS(1)`` visible numerically.  The
    finite-grid FEM value is directional and substantially underestimates the
    infinite-line constant for a Cauchy tail.

    Returns ``(B_HS, weighted_constant_fem, in_bracket)``.
    """
    xs = tau * sinh_grid(x_max, n)
    xs = xs[np.abs(xs) > 1e-6 * tau]                # avoid the exact log pole, scale-covariantly
    p = horseshoe_density_shape(xs, tau)
    a_arr = tau ** 2 + xs ** 2
    B_plus, B_minus, B = hardy_1d(p, a_arr, xs, m=0.0)
    # Weighted Poincare constant via FEM with U = -log p (density given directly).
    logp = np.log(np.clip(p, 1e-300, None))
    U = lambda q: -np.interp(q, xs, logp)
    a = lambda q: tau ** 2 + q ** 2
    constant_fem = poincare_1d_fem(U, xs, a=a)
    in_bracket = B <= constant_fem <= 4 * B + 1e-9
    return B, constant_fem, bool(in_bracket)


# ---- run + selftest ------------------------------------------------------------

def run_records(seed: int = 0):
    records = []
    cal_ok = True
    for beta in CAUCHY_BETAS:
        gap = cal_cauchy_gap(beta)
        exact = 1.0 / lambda_beta_d(beta, 1)
        v = matches("cal-cauchy", f"FEM weighted C_P^w(mu_beta) ~= 1/lambda_(beta={beta},1)",
                    gap, exact, rel_tol=CAL_TOL)
        cal_ok = cal_ok and v.status == "match"
        records.append({"kind": "calibration", "instance": "cal-cauchy", "beta": beta,
                        "weighted_C_P_fem": gap, "exact_weighted_C_P": exact,
                        "verdict": v.dict()})

    if not cal_ok:
        records.append({"kind": "directional-diagnostic", "instance": "a3-grid-battery",
                        "status": "no-diagnostic", "reason": "calibration gate red"})
        return records, {"calibration_passed": False, "grid_diagnostics_gated": False}

    for nu in [1.5, 4.0]:
        cn, cw, wt, wexact = student_gaps(nu)
        grows = cw > 1.3 * cn
        # weighted match is grid-limited for heavy nu<=2 (infinite variance) -> directional tol
        wtol = 0.06 if nu > 2 else 0.20
        v = matches("stress-student", f"FEM weighted C_P ~= exact value, nu={nu}",
                    wt, wexact, rel_tol=wtol)
        records.append({"kind": "directional-diagnostic", "instance": "stress-student",
                        "status": "directional-only", "obstruction": OBSTRUCTION,
                        "nu": nu, "classical_C_P_fem_narrow": cn,
                        "classical_C_P_fem_wide": cw,
                        "directional_classical_growth": bool(grows),
                        "analytic_classical_C_P": "infinity",
                        "weighted_C_P_fem": wt, "exact_weighted_C_P": wexact,
                        "weighted_fem_tolerance": wtol,
                        "weighted_fem_comparison": v.dict(),
                        "note": "Finite-domain FEM values are directional; classical infinity "
                                "and the weighted closed form are analytic results."})

    for tau in [0.5, 1.0]:
        B, gap, ok = horseshoe_bracket(tau)
        records.append({"kind": "directional-diagnostic", "instance": "stress-horseshoe",
                        "status": "directional-only", "obstruction": OBSTRUCTION,
                        "ledger_node": "prop:a3-horseshoe", "theorem_status": "proved",
                        "tau": tau, "B_HS_grid": B, "weighted_C_P_fem": gap,
                        "exact_weighted_C_P": 4.0,
                        "directional_in_hardy_bracket": ok,
                        "density": "exact-normal-half-Cauchy-horseshoe",
                        "note": "Directional finite-grid diagnostic only. Exact scale covariance: "
                                "B_HS(tau)=B_HS(1), C_HS(tau)=C_HS(1); on this truncation "
                                "the FEM value lies below the exact infinite-line constant."})

    ys = np.linspace(0.0, 12.0, 2401)
    odd_residual = horseshoe_odd_barta_residual_lower(ys)
    records.append({"kind": "analytic-diagnostic", "instance": "stress-horseshoe-odd-barta",
                    "obstruction": OBSTRUCTION, "ledger_node": "prop:a3-horseshoe",
                    "theorem_status": "proved", "intrinsic_y_max": float(ys[-1]),
                    "minimum_sampled_residual_lower": float(np.min(odd_residual)),
                    "tail_spectral_threshold": 0.25,
                    "note": "Parity-separated regression for the closed positive Barta residual. "
                            "The positivity proof is algebraic; this sampled value is not evidence."})

    return records, {"calibration_passed": cal_ok, "grid_diagnostics_gated": True}


def selftest(rng):
    checks = []
    for beta in CAUCHY_BETAS:
        gap = cal_cauchy_gap(beta)
        exact = 1.0 / lambda_beta_d(beta, 1)
        checks.append((f"A3 cal-cauchy beta={beta}: weighted C_P ~= 1/lambda ({gap:.4f} vs {exact:.4f})",
                       abs(gap - exact) <= CAL_TOL * exact))
    # Student-t nu=1.5 (<2): classical gap must grow with grid width (diverging)
    cn, cw, wt, wexact = student_gaps(1.5)
    checks.append((f"A3 stress-student nu=1.5: finite-domain classical C_P grows ({cn:.2f}->{cw:.2f})",
                   cw > 1.3 * cn))
    # weighted match precise only for nu>2 (finite variance); use nu=4
    _, _, wt4, wex4 = student_gaps(4.0)
    checks.append((f"A3 stress-student nu=4: weighted C_P FEM matches ({wt4:.3f} vs {wex4:.3f})",
                   abs(wt4 - wex4) <= 0.06 * wex4))
    # The horseshoe is a scale family and the chosen weight scales quadratically.
    # A standardized grid must therefore return the same Hardy/FEM diagnostics.
    hs_half = horseshoe_bracket(0.5, x_max=100.0, n=2001)[:2]
    hs_one = horseshoe_bracket(1.0, x_max=100.0, n=2001)[:2]
    hs_two = horseshoe_bracket(2.0, x_max=100.0, n=2001)[:2]
    scale_err = max(abs(a - b) for pair in (hs_half, hs_two) for a, b in zip(pair, hs_one))
    checks.append((f"A3 stress-horseshoe: Hardy/FEM scale covariance (max err {scale_err:.2e})",
                   scale_err <= 1e-8))
    aa = np.geomspace(1e-8, 40.0, 2001)
    e1_slack = horseshoe_e1_rational_upper(aa) - _scaled_exp1(aa)
    checks.append((f"A3 horseshoe E1 rational bound: sampled minimum slack {e1_slack.min():.2e}",
                   bool(np.all(e1_slack > 0.0))))
    ys = np.linspace(0.0, 12.0, 2401)
    odd_residual = horseshoe_odd_barta_residual_lower(ys)
    checks.append((f"A3 horseshoe odd Barta residual: sampled minimum {odd_residual.min():.2e}",
                   bool(np.all(odd_residual > 0.0))))
    return checks
