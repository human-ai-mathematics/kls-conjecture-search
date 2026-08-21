"""Exact product-tail-union observables for the KLS ``q:alignment`` stress test.

The base measure is the isotropic product Laplace law and the fixed cut is

    E_a = {max_i |x_i| >= a},        F_a = E_a^c = product_i {|x_i| < a}.

The complement is a product event.  Consequently all two-colour quantities are
reconstructed from one-dimensional *truncated* tilted-Laplace moments; no FFT,
Gaussian surrogate, or dense ``n x n`` matrix is involved.  A state therefore
costs O(n).

For marginal mean/variance ``m_i,A_i``, inside mean/variance ``u_i,w_i``,
``z_i=P_i(|X_i|<a)``, and ``q=product z_i``, put ``p=1-q``.  Then

    delta_i = (m_i-u_i)/p,
    G = diag((A_i-w_i)/p) - q delta delta^T.

The formulas below evaluate ``S=s||G||_HS^2`` and the incident-high source
``S_high`` without materialising ``G``.  They also return the Riccati information
rate ``r`` and damping ``D``.

The half-line tilted-Laplace integrals are evaluated in closed form.  At positive
time they are truncated-normal tails, with ``log_ndtr``/``erfcx`` used to avoid
underflow.  At time zero they reduce to incomplete-gamma formulas.  The small-time
far-tail cancellation in the normal representation is handled with the inverse
Mills expansion when necessary.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.special import erfcx, gammainc, gammaln, log_ndtr, logsumexp


_SQRT2 = float(np.sqrt(2.0))
_LOG_2PI = float(np.log(2.0 * np.pi))
_LOG_SQRT_2_OVER_PI = float(0.5 * np.log(2.0 / np.pi))


@dataclass(frozen=True)
class SymmetricTruncationMoments:
    """Moments of a tilted isotropic Laplace law and its restriction ``|X|<a``."""

    probability: float
    mean: float
    variance: float
    second_moment: float
    full_mean: float
    full_variance: float
    full_second_moment: float


@dataclass(frozen=True)
class _HalfLineMoments:
    """Unnormalised mass and conditional moments on ``y>=0`` and ``0<=y<a``."""

    log_mass: float
    mean: float
    variance: float
    second_moment: float
    inside_probability: float
    inside_log_mass: float
    inside_mean: float
    inside_variance: float
    inside_second_moment: float


def balanced_tail_radius(n: int) -> float:
    """Radius making ``P(max_i |X_i| >= a)=1/2`` for isotropic Laplace products."""

    if int(n) != n or n < 1:
        raise ValueError("n must be a positive integer")
    # P(|X|<a)=1-exp(-sqrt(2)a)=2^(-1/n).  expm1 retains accuracy for large n.
    tail_probability = -np.expm1(-np.log(2.0) / float(n))
    return float(-np.log(tail_probability) / _SQRT2)


def _inverse_mills_residual(a: float) -> tuple[float, float]:
    """Return ``h(a)-a`` and ``Var(Z | Z>=a)`` stably.

    Here ``h=phi(a)/Phi(-a)``.  Direct subtraction loses accuracy when ``a`` is
    large and positive, exactly the small-localization-time Laplace regime.
    """

    if a > 35.0:
        inv = 1.0 / a
        inv2 = inv * inv
        # h-a = a^-1 - 2a^-3 + 10a^-5 - 74a^-7 + 706a^-9 + O(a^-11)
        residual = inv * (
            1.0 + inv2 * (-2.0 + inv2 * (10.0 + inv2 * (-74.0 + 706.0 * inv2)))
        )
        # Var(Z|Z>=a) = a^-2 - 6a^-4 + 50a^-6 - 518a^-8 + O(a^-10)
        variance = inv2 * (
            1.0 + inv2 * (-6.0 + inv2 * (50.0 - 518.0 * inv2))
        )
        return float(residual), float(max(variance, 0.0))

    if a >= 0.0:
        h = float(np.exp(_LOG_SQRT_2_OVER_PI) / erfcx(a / _SQRT2))
    else:
        log_phi = -0.5 * a * a - 0.5 * _LOG_2PI
        h = float(np.exp(log_phi - log_ndtr(-a)))
    residual = h - a
    variance = 1.0 - h * residual
    return float(residual), float(max(variance, 0.0))


def _positive_halfline_moments(rate: float, t: float, radius: float) -> _HalfLineMoments:
    """Moments of density proportional to ``exp(-rate*y-t*y^2/2)``, ``y>=0``."""

    if radius <= 0.0 or not np.isfinite(radius):
        if radius != np.inf:
            raise ValueError("radius must be positive")
    if t < 0.0:
        raise ValueError("t must be non-negative")

    if t == 0.0:
        if rate <= 0.0:
            raise ValueError("the t=0 tilted Laplace law requires |c| < sqrt(2)")
        log_mass = -float(np.log(rate))
        mean = 1.0 / rate
        variance = 1.0 / (rate * rate)
        second = 2.0 / (rate * rate)
        if radius == np.inf:
            return _HalfLineMoments(
                log_mass, mean, variance, second,
                1.0, log_mass, mean, variance, second,
            )
        u = rate * radius
        z = float(-np.expm1(-u))
        # Integral y^k exp(-rate*y)dy = k! P(k+1,u)/rate^(k+1).
        inside_mean = float(gammainc(2, u) / (rate * z))
        inside_second = float(2.0 * gammainc(3, u) / (rate * rate * z))
        inside_var = max(inside_second - inside_mean * inside_mean, 0.0)
        return _HalfLineMoments(
            log_mass, mean, variance, second,
            z, log_mass + float(np.log(z)), inside_mean, inside_var, inside_second,
        )

    # Completing the square turns this law into a normal conditioned far beyond its
    # mean.  When t/rate^2 is tiny that representation subtracts O(rate/sqrt(t))
    # numbers to recover an O(1) mean.  The convergent-at-this-scale perturbation
    # expansion around the exponential law is substantially more accurate.
    if rate > 0.0 and t / (rate * rate) < 1.0e-3:
        return _small_t_halfline_moments(rate, t, radius)

    sqrt_t = float(np.sqrt(t))
    a = rate / sqrt_t
    log_sf_a = float(log_ndtr(-a))
    if a >= 0.0:
        log_mass = float(0.5 * np.log(np.pi / (2.0 * t)) + np.log(erfcx(a / _SQRT2)))
    else:
        log_mass = float(0.5 * (_LOG_2PI - np.log(t)) + 0.5 * a * a + log_sf_a)

    residual, variance_z = _inverse_mills_residual(a)
    mean = residual / sqrt_t
    variance = variance_z / t
    second = variance + mean * mean

    if radius == np.inf:
        return _HalfLineMoments(
            log_mass, mean, variance, second,
            1.0, log_mass, mean, variance, second,
        )

    delta = radius * sqrt_t
    b = a + delta
    log_sf_b = float(log_ndtr(-b))
    log_tail_ratio = min(log_sf_b - log_sf_a, 0.0)
    # P(a<=Z<=b)/P(Z>=a), evaluated accurately even when it is close to 0 or 1.
    z = float(-np.expm1(log_tail_ratio))
    z = min(max(z, np.finfo(float).tiny), 1.0)

    # If the removed tail is below roundoff, reuse the more stable full moments.
    if log_tail_ratio < np.log(np.finfo(float).eps):
        inside_mean = mean
        inside_variance = variance
        inside_second = second
    else:
        log_interval = log_sf_a + float(np.log(z))
        log_phi_a = -0.5 * a * a - 0.5 * _LOG_2PI
        log_phi_b = -0.5 * b * b - 0.5 * _LOG_2PI
        boundary_a = float(np.exp(log_phi_a - log_interval))
        boundary_b = float(np.exp(log_phi_b - log_interval))
        mean_u = boundary_a - boundary_b - a
        second_u = 1.0 - a * mean_u - delta * boundary_b
        variance_u = max(second_u - mean_u * mean_u, 0.0)
        inside_mean = mean_u / sqrt_t
        inside_variance = variance_u / t
        inside_second = inside_variance + inside_mean * inside_mean

    return _HalfLineMoments(
        log_mass, mean, variance, second,
        z, log_mass + float(np.log(z)),
        float(inside_mean), float(inside_variance), float(inside_second),
    )


def _small_t_integral(rate: float, t: float, radius: float, power: int) -> float:
    """Asymptotic integral of ``y^power exp(-rate*y-t*y^2/2)`` in long double."""

    total = np.longdouble(0.0)
    previous = np.longdouble(np.inf)
    log_rate = np.log(rate)
    for j in range(24):
        degree = power + 2 * j
        log_abs = (
            j * np.log(t / 2.0)
            - gammaln(j + 1.0)
            + gammaln(degree + 1.0)
            - (degree + 1.0) * log_rate
        )
        if radius != np.inf:
            regularized = float(gammainc(degree + 1, rate * radius))
            if regularized == 0.0:
                continue
            log_abs += np.log(regularized)
        term = np.longdouble(np.exp(log_abs))
        if j % 2:
            term = -term
        magnitude = abs(term)
        # This is an asymptotic series.  Stop before its terms turn around.
        if j > 0 and magnitude > previous:
            break
        total += term
        if j >= 2 and magnitude <= np.finfo(float).eps * max(abs(total), np.longdouble(1.0)):
            break
        previous = magnitude
    return float(total)


def _small_t_halfline_moments(rate: float, t: float, radius: float) -> _HalfLineMoments:
    full = [_small_t_integral(rate, t, np.inf, k) for k in range(3)]
    mass, first, second_raw = full
    mean = first / mass
    second = second_raw / mass
    variance = max(second - mean * mean, 0.0)
    log_mass = float(np.log(mass))
    if radius == np.inf:
        return _HalfLineMoments(
            log_mass, mean, variance, second,
            1.0, log_mass, mean, variance, second,
        )

    inside = [_small_t_integral(rate, t, radius, k) for k in range(3)]
    inside_mass, inside_first, inside_second_raw = inside
    z = min(max(inside_mass / mass, np.finfo(float).tiny), 1.0)
    inside_mean = inside_first / inside_mass
    inside_second = inside_second_raw / inside_mass
    inside_variance = max(inside_second - inside_mean * inside_mean, 0.0)
    return _HalfLineMoments(
        log_mass, mean, variance, second,
        z, float(np.log(inside_mass)), inside_mean, inside_variance, inside_second,
    )


def _mix_two(
    log_mass_a: float,
    mean_a: float,
    second_a: float,
    log_mass_b: float,
    mean_b: float,
    second_b: float,
) -> tuple[float, float, float, float]:
    """Return ``(log total mass, mean, variance, second moment)`` of two pieces."""

    log_total = float(logsumexp([log_mass_a, log_mass_b]))
    wa = float(np.exp(log_mass_a - log_total))
    wb = 1.0 - wa
    mean = wa * mean_a + wb * mean_b
    second = wa * second_a + wb * second_b
    variance = max(second - mean * mean, 0.0)
    return log_total, float(mean), float(variance), float(second)


def tilted_laplace_symmetric_truncation(
    c: float,
    t: float,
    radius: float,
) -> SymmetricTruncationMoments:
    """Exact moments of ``mu_{c,t}`` and ``mu_{c,t}(. | |X|<radius)``.

    ``mu_{c,t}(dx)`` is proportional to
    ``exp(-sqrt(2)|x| + c*x - t*x^2/2) dx``.
    """

    c = float(c)
    t = float(t)
    radius = float(radius)
    if radius <= 0.0 or not np.isfinite(radius):
        raise ValueError("radius must be finite and positive")

    # On x>=0 use y=x and rate sqrt(2)-c.  On x<=0 use y=-x and rate sqrt(2)+c.
    pos = _positive_halfline_moments(_SQRT2 - c, t, radius)
    neg = _positive_halfline_moments(_SQRT2 + c, t, radius)

    log_full, full_mean, full_var, full_second = _mix_two(
        pos.log_mass, pos.mean, pos.second_moment,
        neg.log_mass, -neg.mean, neg.second_moment,
    )
    log_inside, inside_mean, inside_var, inside_second = _mix_two(
        pos.inside_log_mass, pos.inside_mean, pos.inside_second_moment,
        neg.inside_log_mass, -neg.inside_mean, neg.inside_second_moment,
    )
    probability = float(np.exp(min(log_inside - log_full, 0.0)))
    probability = min(max(probability, 0.0), 1.0)
    return SymmetricTruncationMoments(
        probability=probability,
        mean=inside_mean,
        variance=inside_var,
        second_moment=inside_second,
        full_mean=full_mean,
        full_variance=full_var,
        full_second_moment=full_second,
    )


@dataclass(frozen=True)
class TailUnionObservables:
    """Exact O(n) two-colour observables for ``E={max_i |x_i|>=radius}``."""

    t: float
    radius: float
    p: float
    q: float
    s: float
    r: float
    D: float
    S: float
    S_high: float
    S_low: float
    high_count: int
    lambda_max: float
    delta: np.ndarray
    A: np.ndarray
    G_diagonal: np.ndarray


def observe_tail_union(
    c: np.ndarray,
    t: float,
    radius: float,
    *,
    high_threshold: float = 2.0,
) -> TailUnionObservables:
    """Evaluate the tail-union source, incident-high source, information and damping."""

    c = np.ascontiguousarray(c, dtype=np.float64)
    if c.ndim != 1 or c.size == 0:
        raise ValueError("c must be a non-empty one-dimensional array")
    if high_threshold <= 0.0:
        raise ValueError("high_threshold must be positive")

    n = c.size
    z = np.empty(n)
    u = np.empty(n)
    w = np.empty(n)
    m = np.empty(n)
    A = np.empty(n)
    for i, ci in enumerate(c):
        stats = tilted_laplace_symmetric_truncation(float(ci), float(t), float(radius))
        z[i] = stats.probability
        u[i] = stats.mean
        w[i] = stats.variance
        m[i] = stats.full_mean
        A[i] = stats.full_variance

    if np.any(z <= 0.0):
        log_q = -np.inf
        q = 0.0
    else:
        log_q = float(np.sum(np.log(z)))
        q = float(np.exp(log_q))
    p = float(-np.expm1(log_q)) if np.isfinite(log_q) else 1.0
    p = min(max(p, np.finfo(float).tiny), 1.0)
    q = min(max(q, 0.0), 1.0)
    s = p * q

    epsilon = m - u
    delta = epsilon / p
    diag_scale = (A - w) / p
    delta2 = delta * delta
    G_diagonal = diag_scale - q * delta2

    delta2_sum = float(np.sum(delta2))
    delta4_sum = float(np.dot(delta2, delta2))
    offdiag_sq = max(q * q * (delta2_sum * delta2_sum - delta4_sum), 0.0)
    G_norm_sq = float(np.dot(G_diagonal, G_diagonal)) + offdiag_sq

    high = A >= high_threshold
    low = ~high
    h2 = float(np.sum(delta2[high]))
    l2 = float(np.sum(delta2[low]))
    h4 = float(np.dot(delta2[high], delta2[high])) if np.any(high) else 0.0
    hh_offdiag_sq = max(q * q * (h2 * h2 - h4), 0.0)
    hh_sq = float(np.dot(G_diagonal[high], G_diagonal[high])) + hh_offdiag_sq
    hl_sq = q * q * h2 * l2
    high_norm_sq = hh_sq + 2.0 * hl_sq

    l4 = float(np.dot(delta2[low], delta2[low])) if np.any(low) else 0.0
    ll_offdiag_sq = max(q * q * (l2 * l2 - l4), 0.0)
    low_norm_sq = float(np.dot(G_diagonal[low], G_diagonal[low])) + ll_offdiag_sq

    r = s * delta2_sum
    D = 2.0 * s * float(np.dot(A, delta2)) - r * r
    S = s * G_norm_sq
    S_high = s * high_norm_sq
    S_low = s * low_norm_sq

    return TailUnionObservables(
        t=float(t), radius=float(radius), p=p, q=q, s=s,
        r=float(r), D=float(D), S=float(S), S_high=float(S_high),
        S_low=float(S_low), high_count=int(np.count_nonzero(high)),
        lambda_max=float(np.max(A)), delta=delta, A=A,
        G_diagonal=G_diagonal,
    )
