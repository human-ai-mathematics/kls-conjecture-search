"""Cut-scale, perimeter, and source-screening observables for the KLS ``conj:weighted-excess-rate`` probe.

This module implements, exactly and without sampling inside a state, the objects that the
``w3`` route probe
(``research/explorations/2026-08-27-kls-route-prober-cut-local-weighted-replacement-w3.md``)
parks as Candidates A and B:

    lambda_cut(A,K) = ||K||_HS^2 / <K, L_A^{-1} K>,    L_A(M) = (AM+MA)/2,
    W_cut           = (1 + lambda_cut)^{5/2},
    Q               = s ||K||_HS^2,
    A_{kappa,t}     = {Q_t >= kappa * e_t * W_cut}.

Model.  Isotropic product of two-sided exponentials, base density proportional to
``exp(-sqrt(2)|x|)``, tilted to ``exp(-sqrt(2)|x| + c_i x - t x^2 / 2)``.  The cut is the
tail union ``E = {max_{i in J} |x_i| >= a}`` for an index block ``J``; ``J`` equal to all
coordinates is the balanced tail-union cut used by the ``kls-align`` target, and a proper
prefix ``J`` is the spectator cylinder ``E_0 x R^{n-n0}`` of
``prop:weighted-spectator-obstruction``.

Exact structure used throughout
-------------------------------
With ``z_i = P(|X_i| < a)`` for ``i in J`` (and ``z_i = 1`` otherwise), ``q = prod z_i``,
``p = 1-q``, ``s = pq``, marginal mean/variance ``m_i, A_i``, inside mean/variance ``u_i, w_i``:

    delta_i = (m_i - u_i)/p,      d_i = (A_i - w_i)/p,
    G       = diag(d) - q delta delta^T                      (= Cov(mu_E) - Cov(mu_F)),
    K       = G + (q-p) delta delta^T = diag(d) - p delta delta^T.

So ``K`` is *diagonal plus rank one*, with diagonal ``kappa_i = d_i - p delta_i^2`` and
off-diagonal ``K_ij = -p delta_i delta_j``.  Writing ``g_i = delta_i^2`` and ``a_i = A_i``
(the tilted product covariance is diagonal), the two scalars defining ``lambda_cut`` split as

    ||K||_HS^2 = sum_i kappa_i^2 + p^2 [ (sum_i g_i)^2 - sum_i g_i^2 ],                  (D1)
    <K,L_A^{-1}K> = sum_i kappa_i^2 / a_i
                    + 2 p^2 [ C(g,a) - (1/2) sum_i g_i^2 / a_i ],                        (D2)
    C(g,a) := sum_{i,j} g_i g_j / (a_i + a_j).                                           (D3)

(D1) is O(n).  (D2) is O(n) apart from the Cauchy-kernel form (D3), which genuinely couples
all pairs and is evaluated exactly in blocks over the support ``{g_i > 0}``; for a cylinder
cut that support is the base block, so the cost is O(|J|^2) and not O(n^2).
:func:`dense_cut_scale` is the brute-force dense reference used by the oracle test.

Weighted perimeter and profile competitors
------------------------------------------
The complement ``F = prod_{i in J} (-a,a)`` is a product box, so the tilted weighted perimeter
of the cut is exactly

    P_t = q * sum_{i in J} ( f_i(a) + f_i(-a) ) / z_i = d/da [ mu_t(F_a) ],               (P1)

the second form being the finite-difference Minkowski oracle used by the target's gate.

``e_t = P_t - I_{mu_t}(p_t)`` is not computable: the localized isoperimetric profile is
unknown.  Every competitor set of mass ``p_t`` gives an **upper** bound ``Ihat >= I``, hence

    ehat_t := (P_t - Ihat_t)_+  <=  e_t.                                                 (P2)

**The surrogate therefore UNDERSTATES the excess.**  A screened-supply integral built from
``ehat`` is a lower bound for the same integral built from ``e``.  Growth seen in the
surrogate is therefore directional evidence against a bounded supply; boundedness of the
surrogate is weak evidence for it.  Two competitor families are implemented:

* ``halfline``    -- coordinate half-lines ``{x_i >= b}`` and ``{x_i <= b}`` at mass ``p_t``;
* ``equal-tail``  -- product boxes ``prod_i (b_i^-, b_i^+)`` with a common per-coordinate
  tail mass, which at ``t = 0`` reproduces the cut itself and hence gives ``ehat_0 = 0``.

The half-line family alone is a *bad* competitor here: for ``n >= 2`` the balanced tail-union
cut has strictly smaller weighted perimeter than any coordinate half-space, so
``P_0 - Ihat^{hl}_0 < 0`` and the clamp in (P2) is active.  Both are reported.

Nothing in this module is proof evidence.  Everything it emits is a directional product-model
diagnostic under ``CLAUDE.md`` constraint 2.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.special import erf, erfcx, log_ndtr, logsumexp

from .tail_union import tilted_laplace_symmetric_truncation


_SQRT2 = float(np.sqrt(2.0))
_LOG_2PI = float(np.log(2.0 * np.pi))
_LOG2 = float(np.log(2.0))

#: Radius standing in for "this coordinate is not constrained by the cut".  At every time
#: used here the tilted marginal has no mass beyond it, so the truncated moments returned by
#: :func:`tilted_laplace_symmetric_truncation` coincide with the full moments bit for bit.
SPECTATOR_RADIUS = 1.0e3


def _log1mexp(u: np.ndarray) -> np.ndarray:
    """``log(1-exp(u))`` for ``u <= 0``, accurate at both ends."""

    u = np.minimum(np.asarray(u, dtype=float), 0.0)
    with np.errstate(divide="ignore", invalid="ignore"):
        near = np.log(-np.expm1(u))
        far = np.log1p(-np.exp(u))
    return np.where(u > -_LOG2, near, far)


def _log_upper_halfline(rate: np.ndarray, t: float, x: np.ndarray) -> np.ndarray:
    """``log int_x^inf exp(-rate*y - t y^2/2) dy`` for finite ``x >= 0``.

    Cancellation-free: the ``beta >= 0`` branch factors the whole Gaussian decay into the
    exactly computable exponent ``rate*x + t x^2/2`` and an ``erfcx`` ratio.
    """

    rate = np.asarray(rate, dtype=float)
    x = np.asarray(x, dtype=float)
    if not np.all(np.isfinite(x)) or np.any(x < 0.0):
        raise ValueError("x must be finite and non-negative")
    if t < 0.0:
        raise ValueError("t must be non-negative")
    if t == 0.0:
        if np.any(rate <= 0.0):
            raise ValueError("the t=0 tilted Laplace law requires |c| < sqrt(2)")
        return -rate * x - np.log(rate)

    sqrt_t = float(np.sqrt(t))
    alpha = rate / sqrt_t
    beta = alpha + sqrt_t * x
    base = 0.5 * (_LOG_2PI - float(np.log(t)))
    positive = beta >= 0.0
    with np.errstate(divide="ignore", invalid="ignore", over="ignore"):
        value_pos = (
            base
            - (rate * x + 0.5 * t * x * x)
            + np.log(0.5 * erfcx(np.where(positive, beta, 0.0) / _SQRT2))
        )
        value_neg = (
            base + 0.5 * alpha * alpha + log_ndtr(-np.where(positive, -1.0, beta))
        )
    return np.where(positive, value_pos, value_neg)


def _log_interval_halfline(rate: np.ndarray, t: float, x: np.ndarray) -> np.ndarray:
    """``log int_0^x exp(-rate*y - t y^2/2) dy`` for finite ``x >= 0``.

    Three cancellation-free branches, selected by the sign of the completed-square limits
    ``alpha = rate/sqrt(t)`` and ``beta = alpha + sqrt(t) x``.  Unlike the ``1 - tails``
    route this stays accurate when the interval carries a vanishing fraction of the mass,
    which happens when a strong tilt pushes a coordinate far outside the cut radius.
    """

    rate = np.asarray(rate, dtype=float)
    x = np.asarray(x, dtype=float)
    if not np.all(np.isfinite(x)) or np.any(x < 0.0):
        raise ValueError("x must be finite and non-negative")
    if t == 0.0:
        if np.any(rate <= 0.0):
            raise ValueError("the t=0 tilted Laplace law requires |c| < sqrt(2)")
        with np.errstate(divide="ignore"):
            return np.log(-np.expm1(-rate * x)) - np.log(rate)

    sqrt_t = float(np.sqrt(t))
    alpha = rate / sqrt_t
    beta = alpha + sqrt_t * x
    base = 0.5 * (_LOG_2PI - float(np.log(t)))
    drop = rate * x + 0.5 * t * x * x
    left = alpha >= 0.0
    right = beta <= 0.0
    middle = ~(left | right)
    with np.errstate(divide="ignore", invalid="ignore", over="ignore"):
        la = np.log(erfcx(np.where(left, alpha, 0.0) / _SQRT2))
        lb = np.log(erfcx(np.where(left, beta, 0.0) / _SQRT2))
        value_left = base - _LOG2 + la + _log1mexp(lb - la - drop)

        ra = np.log(erfcx(np.where(right, -alpha, 0.0) / _SQRT2))
        rb = np.log(erfcx(np.where(right, -beta, 0.0) / _SQRT2))
        value_right = base - _LOG2 - drop + rb + _log1mexp(ra - rb + drop)

        am = np.where(middle, alpha, -1.0)
        bm = np.where(middle, beta, 1.0)
        value_middle = (
            base + 0.5 * am * am
            + np.log(0.5 * (erf(bm / _SQRT2) - erf(am / _SQRT2)))
        )
    return np.where(left, value_left, np.where(right, value_right, value_middle))


@dataclass(frozen=True)
class TiltedLaplaceMarginals:
    """Vectorized normalizers for the tilted product marginals at one time."""

    c: np.ndarray
    t: float
    rate_pos: np.ndarray
    rate_neg: np.ndarray
    log_Z: np.ndarray

    @property
    def n(self) -> int:
        return int(self.c.size)


def marginals(c: np.ndarray, t: float) -> TiltedLaplaceMarginals:
    """Normalizing constants of ``exp(-sqrt(2)|x| + c_i x - t x^2/2)``."""

    c = np.ascontiguousarray(np.asarray(c, dtype=float).ravel())
    if c.size == 0:
        raise ValueError("c must be non-empty")
    t = float(t)
    rate_pos = _SQRT2 - c
    rate_neg = _SQRT2 + c
    zero = np.zeros_like(c)
    log_Z = np.logaddexp(
        _log_upper_halfline(rate_pos, t, zero),
        _log_upper_halfline(rate_neg, t, zero),
    )
    return TiltedLaplaceMarginals(c=c, t=t, rate_pos=rate_pos, rate_neg=rate_neg, log_Z=log_Z)


def log_survival(mar: TiltedLaplaceMarginals, b: np.ndarray) -> np.ndarray:
    """``log P(X_i >= b_i)`` under the tilted marginals.

    For ``b < 0`` the survival is assembled additively as ``[b,0] + [0,inf)`` rather than as
    ``1 - P(X<b)``, so no cancellation occurs when the survival itself is small.
    """

    b = np.asarray(b, dtype=float)
    upper = _log_upper_halfline(mar.rate_pos, mar.t, np.maximum(b, 0.0)) - mar.log_Z
    zero = np.zeros_like(mar.c)
    lower = np.logaddexp(
        _log_interval_halfline(mar.rate_neg, mar.t, np.maximum(-b, 0.0)),
        _log_upper_halfline(mar.rate_pos, mar.t, zero),
    ) - mar.log_Z
    return np.where(b >= 0.0, upper, lower)


def log_density(mar: TiltedLaplaceMarginals, x: np.ndarray) -> np.ndarray:
    """``log f_i(x_i)`` for the normalized tilted marginals."""

    x = np.asarray(x, dtype=float)
    return -_SQRT2 * np.abs(x) + mar.c * x - 0.5 * mar.t * x * x - mar.log_Z


def log_inside_mass(mar: TiltedLaplaceMarginals, radius: np.ndarray) -> np.ndarray:
    """``log P(|X_i| < radius_i)``.

    Two representations, each accurate in its own regime and switched on the size of the
    discarded tail: ``log(1-tail)`` when the cut keeps almost all of the mass (the balanced
    regime, where the additive form would lose the leading digits of ``log z``), and the
    additive interval form when it does not.
    """

    radius = np.asarray(radius, dtype=float)
    tails = np.logaddexp(
        _log_upper_halfline(mar.rate_pos, mar.t, radius) - mar.log_Z,
        _log_upper_halfline(mar.rate_neg, mar.t, radius) - mar.log_Z,
    )
    interval = np.logaddexp(
        _log_interval_halfline(mar.rate_pos, mar.t, radius),
        _log_interval_halfline(mar.rate_neg, mar.t, radius),
    ) - mar.log_Z
    return np.where(tails < -0.5, _log1mexp(np.minimum(tails, 0.0)), interval)


def survival_quantile(
    mar: TiltedLaplaceMarginals,
    log_level: np.ndarray,
    *,
    bracket: float = 80.0,
    iterations: int = 80,
) -> np.ndarray:
    """Solve ``log P(X_i >= b_i) = log_level_i`` by vectorized bisection."""

    log_level = np.broadcast_to(np.asarray(log_level, dtype=float), mar.c.shape)
    lo = np.full(mar.c.shape, -abs(bracket))
    hi = np.full(mar.c.shape, abs(bracket))
    for _ in range(int(iterations)):
        mid = 0.5 * (lo + hi)
        too_much = log_survival(mar, mid) > log_level
        lo = np.where(too_much, mid, lo)
        hi = np.where(too_much, hi, mid)
    return 0.5 * (lo + hi)


# --------------------------------------------------------------------------------------
# cut masses, perimeter, and profile competitors
# --------------------------------------------------------------------------------------


def cut_radii(n: int, radius: float, block: int | None) -> np.ndarray:
    """Per-coordinate truncation radius: ``radius`` on the cut block, spectator elsewhere."""

    radii = np.full(int(n), float(SPECTATOR_RADIUS))
    stop = int(n) if block is None else int(block)
    if stop < 1 or stop > int(n):
        raise ValueError("block must satisfy 1 <= block <= n")
    radii[:stop] = float(radius)
    return radii


def tail_union_perimeter(
    mar: TiltedLaplaceMarginals,
    radius: float,
    block: int | None = None,
) -> float:
    """Exact tilted weighted perimeter (P1) of ``{max_{i<block} |x_i| >= radius}``."""

    stop = mar.n if block is None else int(block)
    idx = slice(0, stop)
    radius = float(radius)
    log_z = log_inside_mass(mar, cut_radii(mar.n, radius, block))
    log_q = float(np.sum(log_z[idx]))
    y = np.abs(mar.c[idx] * radius)
    log_face = (
        -_SQRT2 * radius
        - 0.5 * mar.t * radius * radius
        - mar.log_Z[idx]
        + y
        + np.log1p(np.exp(-2.0 * y))
    )
    return float(np.exp(log_q + logsumexp(log_face - log_z[idx])))


def halfline_profile_bound(
    mar: TiltedLaplaceMarginals,
    p: float,
    block: int | None = None,
) -> float:
    """Smallest coordinate half-line perimeter at mass ``p``; an upper bound on the profile."""

    stop = mar.n if block is None else int(block)
    if not (0.0 < p < 1.0):
        return float("inf")
    level = float(np.log(p))
    reflected = marginals(-mar.c, mar.t)
    right = np.exp(log_density(mar, survival_quantile(mar, level)))
    left = np.exp(log_density(reflected, survival_quantile(reflected, level)))
    return float(np.minimum(right, left)[:stop].min())


def equal_tail_product_bound(
    mar: TiltedLaplaceMarginals,
    p: float,
    block: int | None = None,
) -> float:
    """Perimeter of the equal-per-coordinate-tail product box of mass ``1-p``.

    At ``t=0`` with zero tilt this competitor is exactly the balanced tail-union cut, so the
    surrogate excess vanishes there instead of going negative.
    """

    stop = mar.n if block is None else int(block)
    if not (0.0 < p < 1.0):
        return float("inf")
    log_z = float(np.log1p(-p)) / float(stop)
    z = float(np.exp(log_z))
    tau = 0.5 * (1.0 - z)
    if not (0.0 < tau < 0.5):
        return float("inf")
    level = float(np.log(tau))
    sub = TiltedLaplaceMarginals(
        c=np.ascontiguousarray(mar.c[:stop]), t=mar.t,
        rate_pos=np.ascontiguousarray(mar.rate_pos[:stop]),
        rate_neg=np.ascontiguousarray(mar.rate_neg[:stop]),
        log_Z=np.ascontiguousarray(mar.log_Z[:stop]),
    )
    reflected = marginals(-sub.c, sub.t)
    right = log_density(sub, survival_quantile(sub, level))
    left = log_density(reflected, survival_quantile(reflected, level))
    total = float(logsumexp(np.concatenate([right, left])))
    return float(np.exp(np.log1p(-p) - log_z + total))


@dataclass(frozen=True)
class ProfileSurrogate:
    """Perimeter, competitor bounds, and the resulting clamped surrogate excess."""

    perimeter: float
    halfline_bound: float
    equal_tail_bound: float
    rich_bound: float
    excess_halfline: float
    excess_rich: float
    halfline_bound_block: float
    equal_tail_bound_block: float
    excess_rich_block: float


def profile_surrogate(
    mar: TiltedLaplaceMarginals,
    p: float,
    radius: float,
    block: int | None = None,
) -> ProfileSurrogate:
    """Evaluate (P1)-(P2) with the all-coordinate and block-restricted competitor families."""

    perimeter = tail_union_perimeter(mar, radius, block)
    hl_all = halfline_profile_bound(mar, p, None)
    et_all = equal_tail_product_bound(mar, p, None)
    rich_all = min(hl_all, et_all)
    if block is None:
        hl_block, et_block, rich_block = hl_all, et_all, rich_all
    else:
        hl_block = halfline_profile_bound(mar, p, block)
        et_block = equal_tail_product_bound(mar, p, block)
        rich_block = min(hl_block, et_block)
    return ProfileSurrogate(
        perimeter=float(perimeter),
        halfline_bound=float(hl_all),
        equal_tail_bound=float(et_all),
        rich_bound=float(rich_all),
        excess_halfline=float(max(perimeter - hl_all, 0.0)),
        excess_rich=float(max(perimeter - rich_all, 0.0)),
        halfline_bound_block=float(hl_block),
        equal_tail_bound_block=float(et_block),
        excess_rich_block=float(max(perimeter - rich_block, 0.0)),
    )


def minkowski_perimeter_estimate(
    c: np.ndarray,
    t: float,
    radius: float,
    h: float,
    block: int | None = None,
) -> float:
    """Central finite difference of ``a -> mu_t(F_a)`` through the scalar reference engine.

    This deliberately routes through :func:`tilted_laplace_symmetric_truncation`, i.e. through
    the pre-existing closed-form path, so the gate compares two independent implementations.
    """

    c = np.asarray(c, dtype=float).ravel()
    stop = c.size if block is None else int(block)

    def mass(a: float) -> float:
        log_q = 0.0
        for i in range(stop):
            stats = tilted_laplace_symmetric_truncation(float(c[i]), float(t), float(a))
            log_q += float(np.log(stats.probability))
        return float(np.exp(log_q))

    return (mass(radius + h) - mass(radius - h)) / (2.0 * h)


# --------------------------------------------------------------------------------------
# the cut scale
# --------------------------------------------------------------------------------------


def cauchy_quadratic_form(g: np.ndarray, a: np.ndarray, *, block_size: int = 512) -> float:
    """Exact ``sum_{i,j} g_i g_j / (a_i + a_j)`` (D3), blocked over the support of ``g``."""

    g = np.asarray(g, dtype=float).ravel()
    a = np.asarray(a, dtype=float).ravel()
    if g.shape != a.shape:
        raise ValueError("g and a must have the same shape")
    support = np.flatnonzero(g > 0.0)
    if support.size == 0:
        return 0.0
    gs = np.ascontiguousarray(g[support])
    as_ = np.ascontiguousarray(a[support])
    if np.any(as_ <= 0.0):
        raise ValueError("a must be strictly positive on the support of g")
    total = 0.0
    for start in range(0, gs.size, int(block_size)):
        gi = gs[start:start + int(block_size)][:, None]
        ai = as_[start:start + int(block_size)][:, None]
        total += float(np.sum(gi * gs[None, :] / (ai + as_[None, :])))
    return total


@dataclass(frozen=True)
class CutScale:
    """``||K||_HS^2``, the Lyapunov energy, and ``lambda_cut`` with its bracket."""

    hs_norm_sq: float
    lyapunov_energy: float
    lambda_cut: float
    lambda_max: float
    lambda_min: float


def cut_scale(
    a: np.ndarray,
    k_diagonal: np.ndarray,
    g: np.ndarray,
    p: float,
    *,
    block_size: int = 512,
) -> CutScale:
    """Evaluate (D1)-(D3) for ``K = diag(k_diagonal) - p delta delta^T``, ``g = delta^2``."""

    a = np.asarray(a, dtype=float).ravel()
    k_diagonal = np.asarray(k_diagonal, dtype=float).ravel()
    g = np.asarray(g, dtype=float).ravel()
    p = float(p)
    if not (a.shape == k_diagonal.shape == g.shape):
        raise ValueError("a, k_diagonal and g must have the same shape")
    if np.any(a <= 0.0):
        raise ValueError("the tilted product covariance must be positive")

    g_sum = float(g.sum())
    g_sq_sum = float(np.dot(g, g))
    offdiag = max(g_sum * g_sum - g_sq_sum, 0.0)
    hs = float(np.dot(k_diagonal, k_diagonal)) + p * p * offdiag

    cauchy = cauchy_quadratic_form(g, a, block_size=block_size)
    diag_correction = 0.5 * float(np.sum(g * g / a))
    energy = float(np.sum(k_diagonal * k_diagonal / a)) + 2.0 * p * p * max(
        cauchy - diag_correction, 0.0
    )
    lam = float(hs / energy) if (hs > 0.0 and energy > 0.0) else 0.0
    return CutScale(
        hs_norm_sq=float(hs),
        lyapunov_energy=float(energy),
        lambda_cut=lam,
        lambda_max=float(a.max()),
        lambda_min=float(a.min()),
    )


def dense_cut_tensor(k_diagonal: np.ndarray, delta: np.ndarray, p: float) -> np.ndarray:
    """Materialize ``K`` from its diagonal and its ``-p delta delta^T`` off-diagonal part.

    ``k_diagonal`` is *the diagonal of* ``K`` (namely ``d_i - p delta_i^2``), so it replaces
    rather than adds to the rank-one diagonal.  Reference path only.
    """

    k_diagonal = np.asarray(k_diagonal, dtype=float).ravel()
    delta = np.asarray(delta, dtype=float).ravel()
    K = -float(p) * np.outer(delta, delta)
    np.fill_diagonal(K, k_diagonal)
    return K


def dense_cut_scale(a: np.ndarray, K: np.ndarray) -> float:
    """Brute-force ``lambda_cut`` from the full matrix, for oracle comparison only."""

    a = np.asarray(a, dtype=float).ravel()
    K = np.asarray(K, dtype=float)
    if K.shape != (a.size, a.size):
        raise ValueError("K must be square of the size of a")
    pair = 0.5 * (a[:, None] + a[None, :])
    hs = float(np.sum(K * K))
    energy = float(np.sum(K * K / pair))
    return float(hs / energy) if (hs > 0.0 and energy > 0.0) else 0.0


# --------------------------------------------------------------------------------------
# one screened state
# --------------------------------------------------------------------------------------


@dataclass(frozen=True)
class ScreenedState:
    """Every exact observable of one localization state for one cut."""

    t: float
    p: float
    q: float
    s: float
    r: float
    D: float
    S: float
    S_high: float
    high_count: int
    lambda_max: float
    lambda_min: float
    lambda_cut: float
    W_cut: float
    hs_norm_sq: float
    Q: float
    surrogate: ProfileSurrogate
    delta: np.ndarray
    A: np.ndarray
    k_diagonal: np.ndarray


def moment_table(c: np.ndarray, t: float, radii: np.ndarray):
    """Per-coordinate ``(z,u,w,m,A)`` from the scalar closed-form reference engine."""

    c = np.asarray(c, dtype=float).ravel()
    radii = np.asarray(radii, dtype=float).ravel()
    if c.shape != radii.shape:
        raise ValueError("c and radii must have the same shape")
    n = c.size
    z = np.empty(n)
    u = np.empty(n)
    w = np.empty(n)
    m = np.empty(n)
    A = np.empty(n)
    for i in range(n):
        stats = tilted_laplace_symmetric_truncation(float(c[i]), float(t), float(radii[i]))
        z[i] = stats.probability
        u[i] = stats.mean
        w[i] = stats.variance
        m[i] = stats.full_mean
        A[i] = stats.full_variance
    return z, u, w, m, A


def screened_state(
    c: np.ndarray,
    t: float,
    radius: float,
    *,
    block: int | None = None,
    high_threshold: float = 2.0,
    block_size: int = 512,
) -> ScreenedState:
    """Assemble the two-colour, cut-scale, perimeter and surrogate-excess observables."""

    c = np.asarray(c, dtype=float).ravel()
    n = c.size
    stop = n if block is None else int(block)
    radii = cut_radii(n, radius, block)
    z, u, w, m, A = moment_table(c, t, radii)

    log_q = float(np.sum(np.log(z[:stop])))
    q = float(np.exp(log_q))
    p = float(-np.expm1(log_q))
    p = min(max(p, np.finfo(float).tiny), 1.0)
    q = min(max(q, 0.0), 1.0)
    s = p * q

    delta = (m - u) / p
    d = (A - w) / p
    g = delta * delta
    G_diagonal = d - q * g
    k_diagonal = d - p * g

    delta2_sum = float(g.sum())
    delta4_sum = float(np.dot(g, g))
    offdiag_sq = max(q * q * (delta2_sum * delta2_sum - delta4_sum), 0.0)
    G_norm_sq = float(np.dot(G_diagonal, G_diagonal)) + offdiag_sq

    high = A >= float(high_threshold)
    low = ~high
    h2 = float(np.sum(g[high]))
    l2 = float(np.sum(g[low]))
    h4 = float(np.dot(g[high], g[high])) if np.any(high) else 0.0
    hh_sq = float(np.dot(G_diagonal[high], G_diagonal[high])) + max(
        q * q * (h2 * h2 - h4), 0.0
    )
    high_norm_sq = hh_sq + 2.0 * q * q * h2 * l2

    r = s * delta2_sum
    D = 2.0 * s * float(np.dot(A, g)) - r * r

    scale = cut_scale(A, k_diagonal, g, p, block_size=block_size)
    mar = marginals(c, t)
    surrogate = profile_surrogate(mar, p, radius, block)

    return ScreenedState(
        t=float(t), p=p, q=q, s=s, r=float(r), D=float(D),
        S=float(s * G_norm_sq), S_high=float(s * high_norm_sq),
        high_count=int(np.count_nonzero(high)),
        lambda_max=scale.lambda_max, lambda_min=scale.lambda_min,
        lambda_cut=scale.lambda_cut,
        W_cut=float((1.0 + scale.lambda_cut) ** 2.5),
        hs_norm_sq=scale.hs_norm_sq, Q=float(s * scale.hs_norm_sq),
        surrogate=surrogate, delta=delta, A=A, k_diagonal=k_diagonal,
    )


def cut_mass(mar: TiltedLaplaceMarginals, radius: float, block: int | None = None) -> float:
    """``p_t`` from the vectorized log-tail path (used on the fine stopping grid)."""

    stop = mar.n if block is None else int(block)
    log_z = log_inside_mass(mar, cut_radii(mar.n, radius, block))
    return float(-np.expm1(float(np.sum(log_z[:stop]))))
