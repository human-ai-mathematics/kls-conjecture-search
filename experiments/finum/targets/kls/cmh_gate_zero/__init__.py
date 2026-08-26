"""Part III (KLS, moment-map/CMH route) — **gate zero**, the cheapest falsifiable consequence.

For a centered log-concave `mu` on `R^n` with covariance `Sigma`, let `phi` be the moment-map
potential (`(grad phi)_# e^{-phi} = mu`) and `H(p) = D^2 phi` at the preimage of `p`.  `H` is
Fathi's positive symmetric Stein kernel: `E_mu[p f(p)] = E_mu[H grad f]` and `E_mu H = Sigma`.
With the Stein generator `L_mu g = Tr(H D^2 g) - p . grad g`, the route's headline conjecture is

    C_CMH(mu) = sup_g  E <H grad g, Sigma^{-1} H grad g> / E (L_mu g)^2  <=  4 .

Testing linear `g(p) = a.p` (so `D^2 g = 0`, `L_mu g = -a.p`) gives the necessary condition

    (G0)   E[H Sigma^{-1} H] <= 4 Sigma      i.e.   G0ratio(mu) <= 4,
    G0ratio(mu) = lambda_max( Sigma^{-1/2} E[H Sigma^{-1} H] Sigma^{-1/2} ).

**What this channel gates.** Gate zero is *necessary* for `C_CMH <= 4`: a single instance with
`G0ratio > 4` and a rigorous lower-bound certificate identifies a candidate analytic refutation.
The certificate must be persisted and reviewed independently before logical status changes. Four
sub-channels are deterministic — there is **no Monte Carlo anywhere** in this module, but
determinism by itself is not a rigor certificate:

1. one-dimensional closed forms — `tau` derived from `(tau rho)' = -x rho` in closed form and
   verified against the defining ODE by high-accuracy quadrature; `R1 = E[tau^2]/sigma^4` is an
   exact rational/closed-form number.  The Gaussian anchor `R1 = 1` calibrates the channel.
   The companion `C_CMH = C_P/Var` (a proved 1D identity) uses `constants.poincare_1d_fem`,
   which is a finite-domain FEM estimate and therefore **directional only**.
2. the Dirichlet family — exactly solvable, genuinely non-product: `H(p) = C(p)/A` with
   `C(p) = diag(p) - p p^T`.  `E[H Sigma^dagger H]` is a degree-4 Dirichlet moment, computed in
   exact rational arithmetic.  The floating generalized eigenvalue is directional; a rationalized
   test vector is evaluated again in exact arithmetic to give a certified Rayleigh lower bound.
   Anchor: `G0ratio(Dir(1,...,1)) = 2(m+1)/(m+3)` on `Delta_{m-1}`.
3. the algebraic countermodel regression — an exact `O(m)`-sector computation showing Letwin's
   constant-matrix estimate `E Tr(B H B H) <= 2 Tr(B^2)` does **not** imply gate zero by matrix
   algebra alone.  The `H` used there is a random PSD matrix with `E H = I`; it is *not* claimed
   to be a moment-map Hessian.
4. the Dirichlet CMH Galerkin regression — polynomial test functions on the simplex, with
   Dirichlet moments supplied by the exact helper but floating polynomial coefficients, matrix
   assembly, whitening, and generalized eigensolve.  It is therefore directional only.

**What this channel cannot decide.**  Gate zero is necessary, not sufficient: passing it on any
finite family is *not* evidence for `C_CMH <= 4`, still less for KLS.  The exact instances here
are two structured families (1D log-concave, Dirichlet) plus one algebraic countermodel; they do
not sample the log-concave cone, and non-refutation is not support for a universal theorem.  The
FEM `C_P/Var`, floating Dirichlet eigenvalues, and Galerkin values are uncertified numerical
approximations and go through `comparison.compare_directional`. Only closed-form rational `R1`
values and exact rational Rayleigh witnesses are eligible for `comparison.compare_exact`.
"""
from __future__ import annotations

import itertools
import math
from fractions import Fraction

import numpy as np
from scipy.integrate import quad
from scipy.linalg import eigh

from ....contract import RunResult
from ....constants import poincare_1d_fem
from ....comparison import compare_directional, matches
from .countermodel import (
    countermodel_params,
    countermodel_sectors,
    countermodel_tensor_crosscheck,
    etr_bhbh_closed,
    etr_bhbh_tensor,
)
from .exact import (
    compare_exact_fraction as _compare_exact_fraction,
    exact_rayleigh_certificate as _exact_rayleigh_certificate,
    fraction_from_payload as _fraction_from_payload,
    fraction_payload as _fraction_payload,
)

GATE_ZERO_CEILING_EXACT = Fraction(4)
GATE_ZERO_CEILING = float(GATE_ZERO_CEILING_EXACT)

QUAD_LIMIT = 500
QUAD_EPSABS = 1e-13
QUAD_EPSREL = 1e-13
QUAD_KINKS = (0.0,)
ODE_PROBES = 7
UNIFORM_SIMPLEX_M_RANGE = (2, 12)
RATIONAL_WITNESS_MAX_DENOMINATOR = 1_000_000
DIRICHLET_ANCHOR_REL_TOL = 1e-9
CROSS_CHANNEL_ABS_TOL = 1e-9
GALERKIN_KEEP_REL_TOL = 1e-11
GALERKIN_HEALTH_ABS_TOL = 1e-6
GALERKIN_DIRECTIONAL_REL_TOL = 1e-8

# Dirichlet instances swept exactly in channel 2 (log-concave: every alpha_i >= 1).
DIRICHLET_ALPHAS: tuple[tuple[int, ...], ...] = (
    (1, 1), (1, 1, 1), (1, 1, 1, 1), (1, 1, 1, 1, 1),
    (1, 1, 10), (1, 1, 100), (1, 1, 1000),
    (1, 5, 25), (1, 2, 3, 4, 5), (1, 1, 1, 1, 50),
    (1,) * 9 + (100,), (1,) * 11 + (500,),
)
# Galerkin degree per ambient simplex size m (cost grows fast in m; see channel 4 notes).
GALERKIN_DEGREE = {2: 6, 3: 6, 4: 4, 5: 4}


# =====================================================================================
# exact Dirichlet moments
# =====================================================================================

def rising(a: Fraction, k: int) -> Fraction:
    """Rising factorial ``(a)_k = a (a+1) ... (a+k-1)``, exact."""
    out = Fraction(1)
    for j in range(k):
        out *= a + j
    return out


class DirichletMoments:
    """``E[prod_i P_i^{k_i}] = (prod_i (alpha_i)_{k_i}) / (A)_{sum k_i}`` — exact, memoized."""

    def __init__(self, alpha):
        self.alpha = tuple(Fraction(a) for a in alpha)
        self.A = sum(self.alpha)
        self._cache: dict[tuple[int, ...], Fraction] = {}

    def exact(self, k) -> Fraction:
        k = tuple(int(x) for x in k)
        v = self._cache.get(k)
        if v is None:
            num = Fraction(1)
            for ai, ki in zip(self.alpha, k):
                if ki:
                    num *= rising(ai, ki)
            v = num / rising(self.A, sum(k))
            self._cache[k] = v
        return v

    def __call__(self, k) -> float:
        return float(self.exact(k))


# =====================================================================================
# channel 1 — one-dimensional closed forms  (tau exact; R1 = E[tau^2]/sigma^4 exact)
# =====================================================================================

def _beta1b_r1(b: int) -> Fraction:
    """Exact ``R1`` for Beta(1,b) centered and standardized.

    ``tau_V(v) = W(1-W)/A`` with ``A = 1+b`` (from ``(tau rho)' = -(w-mean) rho``); scaling by
    ``s = sd(W)`` gives ``R1 = E[(W(1-W))^2] / (A^2 s^4)``.
    """
    A = Fraction(1 + b)
    var = Fraction(b) / (A * A * Fraction(b + 2))

    def mom(k: int) -> Fraction:
        num = Fraction(math.factorial(k))
        den = Fraction(1)
        for j in range(1, k + 1):
            den *= Fraction(b + j)
        return num / den

    return (mom(2) - 2 * mom(3) + mom(4)) / (A * A * var * var)


def one_d_laws():
    """The standardized (variance 1) one-dimensional battery.

    Each entry carries a CLOSED-FORM ``tau`` derived from ``(tau rho)' = -x rho``, the exact
    ``R1 = E[tau^2]``, an (unnormalized) density for the ODE cross-check, and the FEM potential
    and grid used for the directional ``C_CMH = C_P/Var`` companion.
    """
    laws = []

    # --- Gaussian N(0,1): tau = 1, R1 = 1  (CALIBRATION ANCHOR) ----------------------
    laws.append(dict(
        name="gaussian", tau=lambda x: np.ones_like(np.asarray(x, float)), r1_exact=1.0,
        r1_exact_fraction=Fraction(1),
        distribution_parameters={"mean": 0, "variance": 1},
        rho=lambda x: np.exp(-np.asarray(x, float) ** 2 / 2.0),
        support=(-np.inf, np.inf), U=lambda x: x ** 2 / 2.0,
        grid=np.linspace(-12.0, 12.0, 4001),
        tau_note="tau = 1 (Gaussian Stein kernel)"))

    # --- centered exponential: rho = e^{-(x+1)} on x >= -1, tau = x+1, R1 = E[Y^2] = 2 -
    laws.append(dict(
        name="exponential-centered", tau=lambda x: np.asarray(x, float) + 1.0, r1_exact=2.0,
        r1_exact_fraction=Fraction(2),
        distribution_parameters={"rate": 1, "centering_shift": -1},
        rho=lambda x: np.exp(-(np.asarray(x, float) + 1.0)),
        support=(-1.0, np.inf), U=lambda x: x + 1.0,
        grid=np.linspace(-1.0, 39.0, 8001),
        tau_note="tau(x) = x+1 (Y = x+1 ~ Exp(1))"))

    # --- uniform[-h,h], h = sqrt3: tau = (h^2-x^2)/2 = (3-x^2)/2, R1 = 6/5 ------------
    h = math.sqrt(3.0)
    laws.append(dict(
        name="uniform", tau=lambda x: (3.0 - np.asarray(x, float) ** 2) / 2.0, r1_exact=1.2,
        r1_exact_fraction=Fraction(6, 5),
        distribution_parameters={"interval": "[-sqrt(3),sqrt(3)]"},
        rho=lambda x: np.ones_like(np.asarray(x, float)),
        support=(-h, h), U=lambda x: np.zeros_like(np.asarray(x, float)),
        grid=np.linspace(-h, h, 4001),
        tau_note="tau(x) = (3 - x^2)/2"))

    # --- two-sided Laplace, var 1: b = 1/sqrt2, tau = b(|x|+b), R1 = 5 b^4 = 5/4 ------
    b = 1.0 / math.sqrt(2.0)
    laws.append(dict(
        name="laplace", tau=lambda x, b=b: b * (np.abs(np.asarray(x, float)) + b),
        r1_exact=1.25, r1_exact_fraction=Fraction(5, 4),
        distribution_parameters={"location": 0, "scale": "1/sqrt(2)"},
        rho=lambda x, b=b: np.exp(-np.abs(np.asarray(x, float)) / b),
        support=(-np.inf, np.inf), U=lambda x, b=b: np.abs(x) / b,
        grid=np.linspace(-30 * b, 30 * b, 8001),
        tau_note="tau(x) = b(|x|+b), b = 1/sqrt2"))

    # --- Gamma(a,1) centered + standardized: tau(x) = 1 + x/sqrt(a), R1 = 1 + 1/a -----
    for a in (1, 2, 5, 20):
        sa = math.sqrt(a)
        w_lo = 0.0 if a == 1 else 1e-10
        w_hi = a + 12.0 * sa + 10.0

        def _rho(x, a=a, sa=sa):
            w = a + sa * np.asarray(x, float)
            w = np.maximum(w, 1e-300)
            return np.exp((a - 1) * np.log(w) - w)

        def _U(x, a=a, sa=sa):
            w = np.maximum(a + sa * np.asarray(x, float), 1e-300)
            return w - (a - 1) * np.log(w)

        laws.append(dict(
            name=f"gamma-a{a}", tau=lambda x, sa=sa: 1.0 + np.asarray(x, float) / sa,
            r1_exact=1.0 + 1.0 / a, r1_exact_fraction=Fraction(a + 1, a), rho=_rho,
            distribution_parameters={"shape": a, "scale": 1, "centered_and_standardized": True},
            support=((w_lo - a) / sa, np.inf), U=_U,
            grid=np.linspace((w_lo - a) / sa, (w_hi - a) / sa, 8001),
            tau_note=f"tau(x) = 1 + x/sqrt(a), a={a}"))

    # --- Beta(1,b) centered + standardized: tau(x) = w(1-w)/(A s^2), w = mu + s x -----
    for bb in (1, 2, 5, 20):
        A = 1 + bb
        mu = 1.0 / A
        s = math.sqrt(bb / (A * A * (bb + 2)))
        w_hi = 1.0 if bb == 1 else 1.0 - 1e-10

        def _tau(x, A=A, mu=mu, s=s):
            w = mu + s * np.asarray(x, float)
            return w * (1.0 - w) / (A * s * s)

        def _rho(x, bb=bb, mu=mu, s=s):
            w = np.clip(mu + s * np.asarray(x, float), 0.0, 1.0)
            return np.power(1.0 - w, bb - 1)

        def _U(x, bb=bb, mu=mu, s=s):
            x = np.asarray(x, float)
            if bb == 1:
                return np.zeros_like(x)          # Beta(1,1) = uniform: flat potential
            w = np.clip(mu + s * x, 0.0, 1.0 - 1e-12)
            return -(bb - 1) * np.log(1.0 - w)

        laws.append(dict(
            name=f"beta-1-{bb}", tau=_tau, r1_exact=float(_beta1b_r1(bb)),
            r1_exact_fraction=_beta1b_r1(bb), rho=_rho,
            distribution_parameters={"alpha": 1, "beta": bb,
                                     "centered_and_standardized": True},
            support=(-mu / s, (w_hi - mu) / s), U=_U,
            grid=np.linspace(-mu / s, (w_hi - mu) / s, 8001),
            tau_note=f"tau(x) = w(1-w)/(A s^2), w = mu + s x, Beta(1,{bb})"))

    return laws


def stein_ode_residual(law, probes=ODE_PROBES):
    """Max relative residual of ``tau(x) rho(x) = int_x^r t rho(t) dt`` by adaptive quadrature.

    This VERIFIES the closed-form ``tau`` against its defining ODE; it is not itself used as a
    numerical value downstream.
    """
    lo, hi = law["support"]
    rho = law["rho"]
    norm = _quad(lambda t: rho(t), lo, hi)
    lo_f = max(lo, -8.0) if not np.isfinite(lo) else lo
    hi_f = min(hi, 8.0) if not np.isfinite(hi) else hi
    xs = np.linspace(lo_f, hi_f, probes + 2)[1:-1]
    worst = 0.0
    for x in xs:
        lhs = float(law["tau"](x)) * float(rho(x)) / norm
        rhs = _quad(lambda t: t * rho(t), x, hi) / norm
        worst = max(worst, abs(lhs - rhs) / max(abs(rhs), 1e-12))
    return float(worst)


def _quad(f, lo, hi) -> float:
    """Adaptive quadrature at tight tolerance, split at 0 when the integrand kinks there."""
    kinks = [p for p in QUAD_KINKS if lo < p < hi]
    parts = [lo, *kinks, hi]
    total = 0.0
    for a, b in zip(parts[:-1], parts[1:]):
        total += quad(f, a, b, limit=QUAD_LIMIT, epsabs=QUAD_EPSABS, epsrel=QUAD_EPSREL)[0]
    return float(total)


def stein_moments_quadrature(law):
    """``(E[tau], E[tau^2])`` by adaptive quadrature — the independent check on ``R1``."""
    lo, hi = law["support"]
    rho = law["rho"]
    norm = _quad(lambda t: rho(t), lo, hi)
    m1 = _quad(lambda t: law["tau"](t) * rho(t), lo, hi) / norm
    m2 = _quad(lambda t: law["tau"](t) ** 2 * rho(t), lo, hi) / norm
    return float(m1), float(m2)


# =====================================================================================
# channel 2 — the Dirichlet family (exact, non-product)
# =====================================================================================

def dirichlet_gate_zero(alpha):
    """Directional ``G0ratio`` plus an exact Rayleigh lower bound for ``P ~ Dir(alpha)``.

    ``H(p) = C(p)/A``, ``C(p) = diag(p) - p p^T``;
    ``Sigma = (diag(alpha) - alpha alpha^T/A) / (A(A+1))`` has kernel ``span{1}``, and on the
    tangent space ``1^perp``: ``v^T Sigma^dagger v = A(A+1) sum_i v_i^2/alpha_i``.  Hence

        v^T E[H Sigma^dagger H] v = ((A+1)/A) E[ sum_i P_i^2 (v_i - P.v)^2 / alpha_i ],

    a degree-4 Dirichlet moment, assembled exactly in ``Fraction``.  ``G0ratio`` is estimated by a
    floating generalized eigensolve on ``1^perp``.  Its top vector is rationalized and the
    resulting Rayleigh quotient is then re-evaluated from the exact matrices.  Only that latter
    quotient is a rigorous lower bound.
    """
    m = len(alpha)
    if m < 2 or any(int(a) != a or a <= 0 for a in alpha):
        raise ValueError("Dirichlet alpha must contain at least two positive integers")
    al = [Fraction(a) for a in alpha]
    A = sum(al)
    mom = DirichletMoments(alpha)

    def E(*terms):
        k = [0] * m
        for i, p in terms:
            k[i] += p
        return mom.exact(tuple(k))

    Sigma = [[(Fraction(1) / (A * (A + 1))) * ((al[i] if i == j else Fraction(0))
                                               - al[i] * al[j] / A)
              for j in range(m)] for i in range(m)]
    # Q_{jk} = E[ sum_i P_i^2 (v_i - P.v)^2 / alpha_i ] as a quadratic form in v
    Q = [[Fraction(0)] * m for _ in range(m)]
    for j in range(m):
        for k in range(m):
            v = Fraction(0)
            if j == k:
                v += E((j, 2)) / al[j]
            v -= E((j, 2), (k, 1)) / al[j]
            v -= E((k, 2), (j, 1)) / al[k]
            for i in range(m):
                v += E((i, 2), (j, 1), (k, 1)) / al[i]
            Q[j][k] = v
    scale = (A + 1) / A
    M_exact = [[scale * Q[j][k] for k in range(m)] for j in range(m)]

    # Pull both forms back through the integer tangent basis B=(e_1-e_m,...,e_{m-1}-e_m).
    # Keeping these matrices as Fractions is what makes the later Rayleigh witness certifiable.
    last = m - 1
    Mt_exact = [[M_exact[i][j] - M_exact[i][last] - M_exact[last][j]
                 + M_exact[last][last] for j in range(last)] for i in range(last)]
    St_exact = [[Sigma[i][j] - Sigma[i][last] - Sigma[last][j]
                 + Sigma[last][last] for j in range(last)] for i in range(last)]
    Mt0 = np.array([[float(x) for x in row] for row in Mt_exact])
    St0 = np.array([[float(x) for x in row] for row in St_exact])

    Mt, St = Mt0.copy(), St0.copy()
    dsc = 1.0 / np.sqrt(np.diag(St))              # diagonal rescale: conditioning only
    Mt = Mt * dsc[:, None] * dsc[None, :]
    St = St * dsc[:, None] * dsc[None, :]
    Mt, St = 0.5 * (Mt + Mt.T), 0.5 * (St + St.T)
    vals, vecs = eigh(Mt, St)

    # If y is an eigenvector of (D Mt0 D, D St0 D), x=D y is a vector for (Mt0,St0).
    # Normalize its largest coordinate to one before rationalization to avoid unstable scale.
    x_float = dsc * vecs[:, -1]
    pivot = int(np.argmax(np.abs(x_float)))
    if x_float[pivot] == 0:
        raise ArithmeticError("floating eigensolver returned the zero vector")
    x_rational = [Fraction.from_float(float(x / x_float[pivot])).limit_denominator(
        RATIONAL_WITNESS_MAX_DENOMINATOR) for x in x_float]
    exact_lower, certificate = _exact_rayleigh_certificate(Mt_exact, St_exact, x_rational)
    certificate.update({
        "source": "Dirichlet degree-4 moment formula",
        "alpha": [int(a) for a in alpha],
        "rationalization_max_denominator": RATIONAL_WITNESS_MAX_DENOMINATOR,
        "selection_method": "floating top eigenvector; largest coordinate normalized to one",
    })
    return dict(alpha=list(int(a) for a in alpha), m=m, n_ambient=m - 1, A=float(A),
                g0ratio=float(vals[-1]), g0ratio_directional=float(vals[-1]),
                g0ratio_min_directional=float(vals[0]),
                exact_rayleigh_lower=float(exact_lower),
                exact_rayleigh_lower_fraction=str(exact_lower),
                exact_rayleigh_certificate=certificate,
                tangent_cond=float(np.linalg.cond(St)))


def uniform_simplex_anchor(m: int) -> float:
    """``G0ratio(Dir(1,...,1)) = 2(m+1)/(m+3)`` on ``Delta_{m-1}`` (the ground truth)."""
    return float(uniform_simplex_anchor_exact(m))


def uniform_simplex_anchor_exact(m: int) -> Fraction:
    return Fraction(2 * (m + 1), m + 3)


# =====================================================================================
# channel 3 — the algebraic countermodel regression (exact, O(m)-sector decomposition)
# =====================================================================================

# =====================================================================================
# channel 4 — Dirichlet CMH Galerkin regression (floating, directional)
# =====================================================================================
# Polynomials on the simplex are dicts {exponent tuple over m ambient coords: float coeff}.
# The Wright-Fisher data (C grad g, L_alpha g) are extension-independent because C 1 = 0 and
# <alpha - A p, 1> = 0, so any polynomial extension of g may be used.

def _pmul(f, g):
    out: dict = {}
    for ef, cf in f.items():
        for eg, cg in g.items():
            e = tuple(x + y for x, y in zip(ef, eg))
            out[e] = out.get(e, 0.0) + cf * cg
    return out


def _padd(f, g, s=1.0):
    out = dict(f)
    for e, c in g.items():
        out[e] = out.get(e, 0.0) + s * c
    return out


def _pdiff(f, i):
    out: dict = {}
    for e, c in f.items():
        k = e[i]
        if k:
            e2 = list(e)
            e2[i] = k - 1
            e2 = tuple(e2)
            out[e2] = out.get(e2, 0.0) + c * k
    return out


def _pvar(m, i):
    e = [0] * m
    e[i] = 1
    return {tuple(e): 1.0}


def _basis_exponents(nfree, deg):
    out = []
    for tot in range(1, deg + 1):
        for comb in itertools.combinations_with_replacement(range(nfree), tot):
            e = [0] * nfree
            for i in comb:
                e[i] += 1
            out.append(tuple(e))
    return out


def _moment_gram(polys, mom):
    """Coefficient matrix + exact moment Gram over the union of monomials of ``polys``."""
    idx: dict = {}
    for p in polys:
        for e in p:
            idx.setdefault(e, len(idx))
    keys = list(idx)
    n = len(keys)
    C = np.zeros((len(polys), n))
    for a, p in enumerate(polys):
        for e, c in p.items():
            C[a, idx[e]] = c
    G = np.empty((n, n))
    for i in range(n):
        ki = keys[i]
        for j in range(i, n):
            v = mom(tuple(x + y for x, y in zip(ki, keys[j])))
            G[i, j] = v
            G[j, i] = v
    return C, G


def dirichlet_ceiling(A: float) -> float:
    """The route theorem's predicted ceiling ``4/(1 + 4 s_A/(A(A+1)))``.

    ``z_A = (A-1)(A-2)``; ``s_A = (z_A-2)/4`` if ``z_A <= 4`` else ``sqrt(z_A) - 3/2``.
    """
    z = (A - 1.0) * (A - 2.0)
    s = (z - 2.0) / 4.0 if z <= 4.0 else math.sqrt(z) - 1.5
    return 4.0 / (1.0 + 4.0 * s / (A * (A + 1.0)))


def dirichlet_galerkin(alpha, deg: int):
    """Largest Galerkin ``Q(g) = A(A+1) d_alpha(g)/n_alpha(g)`` over polynomials of degree <= deg.

    ``d_alpha(g) = E sum_i (C(P) grad g)_i^2/alpha_i``,
    ``n_alpha(g) = E (L_alpha g)^2``, ``L_alpha g = Tr(C D^2 g) + <alpha - A p, grad g>``.
    Algebraically, ``Q`` is the CMH Rayleigh quotient (``L_mu = L_alpha/A`` and
    ``E<H grad g, Sigma^dagger H grad g> = ((A+1)/A) d_alpha``), so a finite-degree value is a
    lower bound for ``C_CMH``.  This implementation uses floating polynomial coefficients,
    matrix products, whitening, and generalized eigenvalues; without an exact rational test
    function evaluated from exact forms, its reported value is directional rather than rigorous.

    Numerical health: because ``L_alpha`` acts on degree-``k`` polynomials with eigenvalue
    ``-k(k+A-1)``, after whitening by the covariance form one must have exactly
    ``lambda_min(N') = A^2``.  That identity is the run's conditioning gate.
    """
    m = len(alpha)
    A = float(sum(alpha))
    mom = DirichletMoments(alpha)
    zero = tuple([0] * m)
    mu = [a / A for a in alpha]
    sd = [math.sqrt(a * (A - a) / (A * A * (A + 1.0))) for a in alpha]
    ypoly = []
    for i in range(m - 1):                       # standardized free coordinates (conditioning)
        e = [0] * m
        e[i] = 1
        ypoly.append({tuple(e): 1.0 / sd[i], zero: -mu[i] / sd[i]})

    psis = []
    for ex in _basis_exponents(m - 1, deg):
        p = {zero: 1.0}
        for i, k in enumerate(ex):
            for _ in range(k):
                p = _pmul(p, ypoly[i])
        psis.append(p)
    nb = len(psis)

    Us, Ls = [], []
    for p in psis:
        g = [_pdiff(p, i) for i in range(m)]
        pdotg: dict = {}
        for j in range(m):
            pdotg = _padd(pdotg, _pmul(_pvar(m, j), g[j]))
        Us.append([_padd(_pmul(_pvar(m, i), g[i]), _pmul(_pvar(m, i), pdotg), -1.0)
                   for i in range(m)])
        L: dict = {}
        for i in range(m):
            L = _padd(L, _pmul(_pvar(m, i), _pdiff(g[i], i)))            # sum_i p_i d_i^2 g
            for j in range(m):
                L = _padd(L, _pmul(_pmul(_pvar(m, i), _pvar(m, j)), _pdiff(g[j], i)), -1.0)
            L = _padd(L, g[i], float(alpha[i]))
            L = _padd(L, _pmul(_pvar(m, i), g[i]), -A)
        Ls.append(L)

    CU, GU = _moment_gram([Us[a][i] for a in range(nb) for i in range(m)], mom)
    CU = CU.reshape(nb, m, -1)
    D = np.zeros((nb, nb))
    for i in range(m):
        X = CU[:, i, :]
        D += (X @ GU @ X.T) / float(alpha[i])
    CL, GL = _moment_gram(Ls, mom)
    N = CL @ GL @ CL.T
    CP, GP = _moment_gram(psis, mom)
    means = np.array([sum(c * mom(e) for e, c in p.items()) for p in psis])
    V = CP @ GP @ CP.T - np.outer(means, means)
    D, N, V = 0.5 * (D + D.T), 0.5 * (N + N.T), 0.5 * (V + V.T)

    w, vec = np.linalg.eigh(V)
    keep = w > GALERKIN_KEEP_REL_TOL * w.max()
    W = vec[:, keep] / np.sqrt(w[keep])
    Dp, Np = W.T @ D @ W, W.T @ N @ W
    Dp, Np = 0.5 * (Dp + Dp.T), 0.5 * (Np + Np.T)
    health = float(np.linalg.eigvalsh(Np)[0] / (A * A))
    reliable = bool(int(keep.sum()) == nb and abs(health - 1.0) <= GALERKIN_HEALTH_ABS_TOL)
    q = float(eigh(A * (A + 1.0) * Dp, Np, eigvals_only=True)[-1])
    return dict(alpha=[int(a) for a in alpha], m=m, A=A, degree=deg, basis_size=nb,
                kept_directions=int(keep.sum()), q_max=q, ceiling=dirichlet_ceiling(A),
                conditioning_health=health, numerically_reliable=reliable)


# =====================================================================================
# run + selftest
# =====================================================================================

def run_records(seed: int = 0, dirichlet_alphas=DIRICHLET_ALPHAS,
                countermodel_ms=tuple(range(18, 61)),
                countermodel_tensor_ms=(18, 20, 24), galerkin_max_m: int = 5):
    """Deterministic gate-zero battery. ``seed`` is recorded for provenance only.

    Deterministic numerical values still use directional verdicts.  Analytic falsification is
    restricted to the closed-form Fractions and exact rational Rayleigh certificates assembled
    below.
    """
    dirichlet_alphas = tuple(tuple(int(a) for a in alpha) for alpha in dirichlet_alphas)
    countermodel_ms = tuple(int(m) for m in countermodel_ms)
    countermodel_tensor_ms = tuple(int(m) for m in countermodel_tensor_ms)
    records: list[dict] = []
    cal_ok = True

    # ---- channel 1: 1D closed forms -------------------------------------------------
    laws = one_d_laws()
    gauss = next(l for l in laws if l["name"] == "gaussian")
    v_cal = matches("cal-cmh-gauss-R1", "R1(N(0,1)) == 1 exactly", gauss["r1_exact"], 1.0,
                    rel_tol=0.0)
    cal_ok = cal_ok and v_cal.outcome == "match"
    records.append({"kind": "calibration", "channel": "1d-closed-form",
                    "instance": "cal-cmh-gauss-R1", "R1": gauss["r1_exact"], "exact": 1.0,
                    "comparison": v_cal.dict(),
                    "note": "tau == 1 for the standard Gaussian; exact, not a numerical value."})

    r1_max, r1_ode_worst, ccmh_max = 0.0, 0.0, 0.0
    for law in laws:
        ode = stein_ode_residual(law)
        m1, m2 = stein_moments_quadrature(law)
        r1_fraction = law["r1_exact_fraction"]
        r1 = float(r1_fraction)
        r1_max = max(r1_max, r1)
        r1_ode_worst = max(r1_ode_worst, ode)
        cp = poincare_1d_fem(law["U"], law["grid"])
        ccmh = float(cp)                      # variance is 1 by construction => C_CMH = C_P/Var
        ccmh_max = max(ccmh_max, ccmh)
        r1_certificate = {
            "certificate_type": "closed-form-rational",
            "arithmetic": "fractions.Fraction",
            "quantity": "R1 = E[tau^2]/sigma^4",
            "law": law["name"],
            "formula": law["tau_note"],
            "lower_bound": _fraction_payload(r1_fraction),
        }
        v_g0 = _compare_exact_fraction(
            f"1D gate zero R1 <= {GATE_ZERO_CEILING}", f"1d-{law['name']}",
            GATE_ZERO_CEILING_EXACT, r1_fraction, r1_certificate,
            note="R1 is a closed-form rational; quadrature only cross-checks the formula.")
        v_cmh = compare_directional(f"1D C_CMH = C_P/Var <= {GATE_ZERO_CEILING}",
                                    f"1d-{law['name']}", GATE_ZERO_CEILING, ccmh,
                                    note="C_P from finite-domain P1-FEM (constants.poincare_1d_fem); "
                                         "uncertified truncation/discretization error => directional only.")
        records.append({"kind": "stein-1d", "channel": "1d-closed-form",
                        "instance": law["name"], "tau": law["tau_note"],
                        "sigma_sq": 1.0, "R1_exact": r1,
                        "R1_exact_fraction": str(r1_fraction),
                        "R1_quadrature": m2, "E_tau_quadrature": m1,
                        "R1_quadrature_rel_err": abs(m2 - r1) / max(r1, 1e-300),
                        "stein_ode_max_rel_residual": ode,
                        "C_P_fem": float(cp), "C_CMH_fem": ccmh,
                        "gate_zero_exact_certificate": r1_certificate,
                        "gate_zero_exact_comparison": v_g0.dict(),
                        "C_CMH_directional_comparison": v_cmh.dict()})

    # ---- channel 2: Dirichlet gate zero (exact) --------------------------------------
    anchor_worst = 0.0
    for m in range(UNIFORM_SIMPLEX_M_RANGE[0], UNIFORM_SIMPLEX_M_RANGE[1] + 1):
        got = dirichlet_gate_zero((1,) * m)["g0ratio"]
        anchor_worst = max(anchor_worst, abs(got - uniform_simplex_anchor(m)))
    v_anchor = matches("cal-cmh-uniform-simplex",
                       "G0ratio(Dir(1,..,1)) == 2(m+1)/(m+3) for m = 2..12",
                       1.0 + anchor_worst, 1.0, rel_tol=DIRICHLET_ANCHOR_REL_TOL)
    cal_ok = cal_ok and v_anchor.outcome == "match"
    records.append({"kind": "calibration", "channel": "dirichlet",
                    "instance": "cal-cmh-uniform-simplex",
                    "m_range": list(UNIFORM_SIMPLEX_M_RANGE),
                    "max_abs_error_vs_anchor": anchor_worst, "comparison": v_anchor.dict(),
                    "note": "ground truth E H^2 = (2(m+1)/(m+3)) I in isotropic coordinates; "
                            "m = 2 must also equal the uniform-interval R1 = 1.2."})

    m2_dir = dirichlet_gate_zero((1, 1))["g0ratio"]
    v_m2 = matches("cal-cmh-m2-vs-uniform-interval",
                   "G0ratio(Dir(1,1)) == R1(uniform) == 1.2", m2_dir, 1.2,
                   rel_tol=DIRICHLET_ANCHOR_REL_TOL)
    cal_ok = cal_ok and v_m2.outcome == "match"
    records.append({"kind": "calibration", "channel": "dirichlet",
                    "instance": "cal-cmh-m2-vs-uniform-interval", "g0ratio": m2_dir,
                    "exact": 1.2, "comparison": v_m2.dict(),
                    "note": "cross-channel: Delta_1 with alpha=(1,1) IS the uniform interval."})

    g0_max_directional, g0_max_exact_lower, g0_rows = 0.0, 0.0, []
    covered = set()
    for m in range(UNIFORM_SIMPLEX_M_RANGE[0], UNIFORM_SIMPLEX_M_RANGE[1] + 1):
        row = dirichlet_gate_zero((1,) * m)
        row["family"] = "uniform-simplex"
        row["anchor_exact"] = uniform_simplex_anchor(m)
        row["anchor_abs_error"] = abs(row["g0ratio"] - row["anchor_exact"])
        g0_rows.append(row)
        covered.add((1,) * m)
    for alpha in dirichlet_alphas:
        if tuple(alpha) in covered:
            continue                                   # already swept as a uniform simplex
        covered.add(tuple(alpha))
        row = dirichlet_gate_zero(alpha)
        row["family"] = "swept"
        g0_rows.append(row)
    for row in g0_rows:
        g0_max_directional = max(g0_max_directional, row["g0ratio_directional"])
        g0_max_exact_lower = max(g0_max_exact_lower, row["exact_rayleigh_lower"])
        inst = "dir(" + ",".join(map(str, row["alpha"])) + ")"
        v_directional = compare_directional(
            f"gate zero G0ratio <= {GATE_ZERO_CEILING}", inst,
            GATE_ZERO_CEILING, row["g0ratio_directional"], rel_tol=0.0,
            note="Largest generalized eigenvalue from scipy.linalg.eigh; deterministic but "
                 "uncertified, hence directional only.")
        exact_lower = _fraction_from_payload(
            row["exact_rayleigh_certificate"]["lower_bound"])
        v_exact = _compare_exact_fraction(
            f"gate zero G0ratio <= {GATE_ZERO_CEILING}", inst,
            GATE_ZERO_CEILING_EXACT, exact_lower, row["exact_rayleigh_certificate"],
            note="Exact rational Rayleigh quotient is a rigorous lower bound for G0ratio.")
        records.append({"kind": "dirichlet-gate-zero", "channel": "dirichlet",
                        **row, "directional_comparison": v_directional.dict(),
                        "exact_rayleigh_comparison": v_exact.dict()})

    # ---- channel 3: algebraic countermodel (exact) -----------------------------------
    sector_rows = [countermodel_sectors(m) for m in countermodel_ms]
    sectors_ok = all(r["all_sectors_at_most_2"] for r in sector_rows)
    identities_ok = all(r["traceless_formula_residual"] <= 1e-12
                        and r["scalar_perfect_square_residual"] <= 1e-12 * max(1.0, r["m"])
                        and abs(r["scalar_discriminant"]) <= 1e-12 * max(1.0, r["m"])
                        for r in sector_rows)
    exceed_ok = all(r["EH2_11_exceeds_4"] for r in sector_rows)
    tensor_worst = max(countermodel_tensor_crosscheck(m) for m in countermodel_tensor_ms)
    records.append({"kind": "countermodel-regression", "channel": "algebraic-countermodel",
                    "m_range": [int(min(countermodel_ms)), int(max(countermodel_ms))],
                    "all_sectors_at_most_2": bool(sectors_ok),
                    "sector_identities_exact": bool(identities_ok),
                    "EH2_11_exceeds_4_for_every_m": bool(exceed_ok),
                    "one_plus_d_at_m18": sector_rows[0]["one_plus_d"],
                    "closed_form_vs_sphere_moment_tensor_max_abs_err": tensor_worst,
                    "tensor_crosscheck_ms": [int(m) for m in countermodel_tensor_ms],
                    "rows": sector_rows,
                    "note": "H here is a random PSD matrix with E H = I, NOT claimed to be a "
                            "moment-map Hessian. It shows E Tr(B H B H) <= 2 Tr(B^2) (Letwin's "
                            "constant-matrix estimate) cannot imply gate zero by matrix algebra "
                            "alone: e_1^T E[H^2] e_1 = 1 + d > 4 for m >= 18. All quantities are "
                            "exact O(m)-sector closed forms; z is never sampled."})

    # ---- channel 4: Dirichlet CMH Galerkin regression (floating/directional) ----------
    q_rows = []
    seen = set()
    for alpha in (tuple((1,) * m for m in range(2, galerkin_max_m + 1)) + tuple(dirichlet_alphas)):
        if alpha in seen:
            continue
        seen.add(alpha)
        if len(alpha) > galerkin_max_m:
            records.append({"kind": "dirichlet-galerkin-skipped", "channel": "galerkin",
                            "alpha": [int(a) for a in alpha], "m": len(alpha),
                            "reason": f"m > galerkin_max_m={galerkin_max_m}; the floating "
                                      "moment Gram over degree-<=2*deg monomials is too large. "
                                      "Not a numerical failure."})
            continue
        q_rows.append(dirichlet_galerkin(alpha, GALERKIN_DEGREE[len(alpha)]))

    q_ratio_max, galerkin_directional_exceeded = 0.0, []
    for row in q_rows:
        ratio = row["q_max"] / row["ceiling"]
        q_ratio_max = max(q_ratio_max, ratio)
        inst = "dir(" + ",".join(map(str, row["alpha"])) + ")"
        health_note = ("conditioning checks passed" if row["numerically_reliable"] else
                       "conditioning checks FAILED")
        v = compare_directional(
            "Dirichlet CMH Galerkin Q <= predicted ceiling", inst,
            row["ceiling"], row["q_max"], rel_tol=GALERKIN_DIRECTIONAL_REL_TOL,
            note=f"Floating polynomial assembly/whitening/generalized eigensolve; {health_note}. "
                 "Determinism and exact scalar moment inputs do not certify the eigenvalue.")
        v4 = compare_directional(
            f"Dirichlet CMH Galerkin Q <= {GATE_ZERO_CEILING}", inst,
            GATE_ZERO_CEILING, row["q_max"], rel_tol=GALERKIN_DIRECTIONAL_REL_TOL,
            note="Floating Galerkin estimate; no exact rational test-function certificate, so "
                 "an exceedance is directional only.")
        if v.outcome == "exceeds" or v4.outcome == "exceeds":
            galerkin_directional_exceeded.append(inst)
        records.append({"kind": "dirichlet-galerkin", "channel": "galerkin", **row,
                        "q_over_ceiling": ratio, "ceiling_comparison": v.dict(),
                        "gate_zero_comparison": v4.dict()})

    # degree-1 Galerkin must reproduce channel 2 exactly (linear g <-> gate zero)
    deg1_worst = 0.0
    for alpha in ((1, 1), (1, 1, 1), (1, 1, 10), (1, 2, 3, 4, 5)):
        deg1_worst = max(deg1_worst,
                         abs(dirichlet_galerkin(alpha, 1)["q_max"]
                             - dirichlet_gate_zero(alpha)["g0ratio"]))
    records.append({"kind": "cross-channel-consistency", "channel": "galerkin",
                    "check": "degree-1 Galerkin Q == channel-2 G0ratio",
                    "max_abs_error": deg1_worst,
                    "passed": bool(deg1_worst <= CROSS_CHANNEL_ABS_TOL),
                    "note": "linear g gives Q(g) = G0ratio; channels 2 and 4 must agree."})

    # ---- summary --------------------------------------------------------------------
    g0_exceeded: list[str] = []
    for r in records:
        if r.get("kind") == "stein-1d" and r["gate_zero_exact_comparison"]["outcome"] == "exceeds":
            g0_exceeded.append(r["gate_zero_exact_comparison"]["instance"])
        if (r.get("kind") == "dirichlet-gate-zero"
                and r["exact_rayleigh_comparison"]["outcome"] == "exceeds"):
            g0_exceeded.append(r["exact_rayleigh_comparison"]["instance"])

    records.append({
        "kind": "summary", "target": "cmh-gate-zero",
        "calibration_passed": bool(cal_ok),
        "gate_zero_ceiling": GATE_ZERO_CEILING,
        "max_R1_1d_exact": r1_max,
        "max_C_CMH_1d_fem_directional": ccmh_max,
        "max_stein_ode_rel_residual": r1_ode_worst,
        "max_G0ratio_dirichlet_directional": g0_max_directional,
        "max_G0ratio_dirichlet_exact_rayleigh_lower": g0_max_exact_lower,
        "exact_exceedance_instances": g0_exceeded,
        "exact_exceedance_detected": bool(g0_exceeded),
        "max_galerkin_Q_over_ceiling": q_ratio_max,
        "galerkin_directional_exceeded_instances": galerkin_directional_exceeded,
        "dirichlet_exact_exceedance_detected": False,
        "countermodel_identities_exact": bool(identities_ok and sectors_ok and exceed_ok),
        "deterministic": True, "monte_carlo_used": False,
        "proof_status": "no-proof; gate zero is NECESSARY for C_CMH <= 4, never sufficient",
        "note": "Determinism/no Monte Carlo is not a rigor certificate. Only closed-form "
                "Fractions and exact rational Rayleigh witnesses can refute; non-refutation on "
                "these families is not evidence for CMH or KLS.",
    })

    def json_endpoint(x):
        if np.isneginf(x):
            return "-inf"
        if np.isposinf(x):
            return "+inf"
        return float(x)

    one_d_config = []
    for law in laws:
        grid = law["grid"]
        one_d_config.append({
            "name": law["name"],
            "distribution_parameters": law["distribution_parameters"],
            "R1_exact_fraction": str(law["r1_exact_fraction"]),
            "tau_formula": law["tau_note"],
            "support": [json_endpoint(law["support"][0]), json_endpoint(law["support"][1])],
            "fem_grid": {"start": float(grid[0]), "stop": float(grid[-1]),
                         "num_points": int(len(grid))},
        })
    battery = {
        "schema_version": 2,
        "one_dimensional": {
            "instances": one_d_config,
            "ode_probes": ODE_PROBES,
            "quadrature": {"limit": QUAD_LIMIT, "epsabs": QUAD_EPSABS,
                           "epsrel": QUAD_EPSREL, "split_points": list(QUAD_KINKS)},
            "fem_backend": "constants.poincare_1d_fem",
        },
        "dirichlet_gate_zero": {
            "uniform_simplex_m_range_inclusive": list(UNIFORM_SIMPLEX_M_RANGE),
            "swept_alphas": [list(alpha) for alpha in dirichlet_alphas],
            "effective_alphas": [row["alpha"] for row in g0_rows],
            "anchor_rel_tol": DIRICHLET_ANCHOR_REL_TOL,
            "floating_eigensolver": "scipy.linalg.eigh",
            "tangent_basis": "columns e_i-e_m, i=1,...,m-1",
            "rational_witness_max_denominator": RATIONAL_WITNESS_MAX_DENOMINATOR,
        },
        "algebraic_countermodel": {
            "m_values": list(countermodel_ms),
            "tensor_crosscheck_m_values": list(countermodel_tensor_ms),
            "identity_abs_tol": 1e-12,
            "tensor_crosscheck_abs_tol": 1e-9,
            "deterministic_test_matrix_seed": 0,
            "deterministic_test_matrices_per_m": 4,
        },
        "dirichlet_galerkin": {
            "galerkin_max_m": int(galerkin_max_m),
            "degree_by_m": {str(m): int(deg) for m, deg in GALERKIN_DEGREE.items()},
            "effective_instances": [{"alpha": row["alpha"], "degree": row["degree"]}
                                    for row in q_rows],
            "polynomial_basis": "total-degree monomials in standardized first m-1 coordinates",
            "moment_backend": "DirichletMoments (exact scalar moments converted to float)",
            "floating_eigensolver": "scipy.linalg.eigh",
            "covariance_keep_rel_tol": GALERKIN_KEEP_REL_TOL,
            "conditioning_health_abs_tol": GALERKIN_HEALTH_ABS_TOL,
            "directional_comparison_rel_tol": GALERKIN_DIRECTIONAL_REL_TOL,
        },
        "cross_channel_degree_one": {
            "alphas": [[1, 1], [1, 1, 1], [1, 1, 10], [1, 2, 3, 4, 5]],
            "abs_tol": CROSS_CHANNEL_ABS_TOL,
        },
    }

    config = {
        "dirichlet_alphas": [list(alpha) for alpha in dirichlet_alphas],
        "countermodel_ms": list(countermodel_ms),
        "countermodel_tensor_ms": list(countermodel_tensor_ms),
        "galerkin_max_m": int(galerkin_max_m),
        "battery": battery,
    }
    summary = {
        "calibration_passed": bool(cal_ok), "deterministic": True,
        "monte_carlo_used": False,
        "gate_zero_ceiling": GATE_ZERO_CEILING,
        "max_R1_1d_exact": r1_max,
        "max_G0ratio_dirichlet_directional": g0_max_directional,
        "max_G0ratio_dirichlet_exact_rayleigh_lower": g0_max_exact_lower,
        "max_C_CMH_1d_fem_directional": ccmh_max,
        "max_galerkin_Q_over_ceiling": q_ratio_max,
        "exact_exceedance_detected": bool(g0_exceeded),
        "dirichlet_exact_exceedance_detected": False,
        "galerkin_directional_exceeded_instances": galerkin_directional_exceeded,
        "countermodel_identities_exact": bool(identities_ok and sectors_ok and exceed_ok),
        "countermodel_first_m": sector_rows[0]["m"],
        "countermodel_first_one_plus_d": sector_rows[0]["one_plus_d"],
        "n_dirichlet_instances": len(g0_rows),
        "n_galerkin_instances": len(q_rows),
        "proof_status": "no-proof/necessary-condition-only",
    }
    return RunResult(records, config=config, summary=summary)


def selftest(rng):
    checks = []

    # 1D anchor: the Gaussian Stein kernel is tau == 1, so R1 == 1 exactly.
    gauss = next(l for l in one_d_laws() if l["name"] == "gaussian")
    checks.append(("CMH cal: R1(N(0,1)) == 1 exactly", gauss["r1_exact"] == 1.0))

    # every closed-form tau satisfies (tau rho)' = -x rho, and E[tau^2] matches R1.
    worst_ode, worst_r1 = 0.0, 0.0
    for law in one_d_laws():
        worst_ode = max(worst_ode, stein_ode_residual(law, probes=5))
        _, m2 = stein_moments_quadrature(law)
        worst_r1 = max(worst_r1, abs(m2 - law["r1_exact"]) / law["r1_exact"])
    checks.append((f"CMH 1D: closed-form tau solves (tau rho)'=-x rho "
                   f"(max rel residual {worst_ode:.2e})", worst_ode <= 1e-6))
    checks.append((f"CMH 1D: E[tau^2] quadrature == exact R1 (max rel err {worst_r1:.2e})",
                   worst_r1 <= 1e-6))

    # Dirichlet anchor: G0ratio(Dir(1,...,1)) == 2(m+1)/(m+3), m = 2..12.
    worst = max(abs(dirichlet_gate_zero((1,) * m)["g0ratio"] - uniform_simplex_anchor(m))
                for m in range(2, 13))
    checks.append((f"CMH cal: G0ratio(Dir(1,..,1)) == 2(m+1)/(m+3), m=2..12 "
                   f"(max abs err {worst:.2e})", worst <= 1e-10))

    # m = 2 Dirichlet IS the uniform interval: both give 1.2.
    d2 = dirichlet_gate_zero((1, 1))["g0ratio"]
    u1 = next(l for l in one_d_laws() if l["name"] == "uniform")["r1_exact"]
    checks.append((f"CMH cal: Dir(1,1) G0ratio == uniform-interval R1 == 1.2 ({d2:.10f})",
                   abs(d2 - 1.2) <= 1e-10 and abs(u1 - 1.2) <= 1e-12))

    # countermodel: exact sector identities, and 1 + d > 4 for m >= 18.
    rows = [countermodel_sectors(m) for m in (18, 25, 40, 60)]
    ok = all(r["traceless_formula_residual"] <= 1e-12
             and r["scalar_perfect_square_residual"] <= 1e-12 * r["m"]
             and abs(r["scalar_discriminant"]) <= 1e-12 * r["m"]
             and r["all_sectors_at_most_2"] and r["EH2_11_exceeds_4"] for r in rows)
    checks.append((f"CMH countermodel: sectors <= 2, deficit a perfect square, "
                   f"1+d = {rows[0]['one_plus_d']:.6f} > 4 at m=18", ok))
    tw = countermodel_tensor_crosscheck(18)
    checks.append((f"CMH countermodel: closed form == sphere-moment tensor contraction "
                   f"(max abs err {tw:.2e})", tw <= 1e-9))

    # Galerkin: degree-1 reproduces gate zero; every instance respects its ceiling and 4.
    d1 = max(abs(dirichlet_galerkin(a, 1)["q_max"] - dirichlet_gate_zero(a)["g0ratio"])
             for a in ((1, 1), (1, 1, 10), (1, 2, 3, 4, 5)))
    checks.append((f"CMH Galerkin: degree-1 Q == G0ratio (max abs err {d1:.2e})", d1 <= 1e-9))
    rows = [dirichlet_galerkin(a, GALERKIN_DEGREE[len(a)])
            for a in ((1, 1), (1, 1, 1), (1, 1, 100), (1, 1, 1000), (1, 1, 1, 1, 50))]
    worst_ratio = max(r["q_max"] / r["ceiling"] for r in rows)
    checks.append((f"CMH Galerkin: Q <= predicted ceiling and <= 4 "
                   f"(worst Q/ceiling {worst_ratio:.4f})",
                   worst_ratio <= 1.0 and all(r["q_max"] <= GATE_ZERO_CEILING for r in rows)
                   and all(r["numerically_reliable"] for r in rows)))
    return checks
