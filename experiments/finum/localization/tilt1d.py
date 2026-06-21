"""One-dimensional tilted log-concave measures and their moments.

Under Eldan stochastic localization a product measure factorizes, and each
coordinate's posterior at tilt ``c`` and time ``t`` is the 1D measure

    mu_{c,t}(dx)  proportional to  exp(-V(x)) * exp(c x - t x^2 / 2) dx,

where ``exp(-V)`` is the (centered, isotropic) base log-concave density. This
module computes the moments of ``mu_{c,t}`` by *exact deterministic quadrature*
(rescaled Gauss-Legendre), never by Monte Carlo and never by a Gaussian
surrogate -- the surrogate is exactly what produced the retracted result in
``explorations/2026-06-14-energy-shell-occupation.md``.

Everything is float64; the partition function is handled in log space
(log-sum-exp) so the tilt ``exp(c x - t x^2 / 2)`` cannot over/underflow.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache

import numpy as np

# Isotropic two-sided exponential (Laplace) base, normalized to unit variance.
# Laplace density (1/2b) exp(-|x|/b) has variance 2 b^2; unit variance => b = 1/sqrt(2),
# i.e. V(x) = |x| / b = sqrt(2) |x|. Then E x^2 = 1, E x^4 = 6, Var(x^2) = 5.
_LAPLACE_B = 1.0 / np.sqrt(2.0)


@lru_cache(maxsize=None)
def _gauss_legendre(order: int) -> tuple[np.ndarray, np.ndarray]:
    """Gauss-Legendre nodes/weights on [-1, 1] (cached, float64)."""
    nodes, weights = np.polynomial.legendre.leggauss(order)
    return nodes.astype(np.float64), weights.astype(np.float64)


@dataclass(frozen=True)
class Base1D:
    """A centered isotropic 1D log-concave base measure ``exp(-V)``."""

    name: str

    def neg_potential(self, x: np.ndarray) -> np.ndarray:
        """Return ``-V(x)`` (log base density, up to an additive constant)."""
        x = np.asarray(x, dtype=np.float64)
        if self.name == "laplace":
            return -np.abs(x) / _LAPLACE_B
        if self.name == "gaussian":
            return -0.5 * x * x
        raise ValueError(f"unknown base measure {self.name!r}")

    def kinks(self) -> tuple[float, ...]:
        """Points where ``V`` is non-smooth; quadrature panels split here.

        The Laplace potential ``sqrt(2)|x|`` has a kink at 0; integrating across
        it with a single smooth Gauss-Legendre panel loses ~3 digits.
        """
        if self.name == "laplace":
            return (0.0,)
        return ()

    def approx_center_scale(self, c: float, t: float) -> tuple[float, float]:
        """Cheap Laplace-style guess for the tilted mode and width.

        Exact for the Gaussian base (mode ``c/(1+t)``, var ``1/(1+t)``); a
        robust over-estimate of the width for the Laplace base. Used only to
        seed the first quadrature pass, which is then refined.
        """
        if self.name == "gaussian":
            denom = 1.0 + t
            return c / denom, 1.0 / np.sqrt(denom)
        # laplace: curvature comes only from the -t x^2/2 factor; the base is
        # piecewise linear. A width that also covers the base scale at small t:
        scale = 1.0 / np.sqrt(t + 1.0)
        # mode of -|x|/b + c x - t x^2/2 on the dominant half-line:
        if abs(c) <= 1.0 / _LAPLACE_B or t == 0.0:
            center = 0.0
        else:
            sgn = np.sign(c)
            center = (c - sgn / _LAPLACE_B) / t if t > 0 else 0.0
        return float(center), float(scale)


LAPLACE = Base1D("laplace")
GAUSSIAN = Base1D("gaussian")


@dataclass(frozen=True)
class Tilted1D:
    """Quadrature representation of a single tilted 1D measure.

    Attributes
    ----------
    nodes, weights : np.ndarray
        Quadrature nodes ``x_a`` and *normalized* probability weights
        ``w_a`` (sum to 1) representing ``mu_{c,t}``.
    mean, var : float
        First and second central moments.
    """

    nodes: np.ndarray
    weights: np.ndarray
    mean: float
    var: float

    def moment(self, k: int) -> float:
        """Raw moment ``E[x^k]`` from the quadrature representation."""
        return float(np.sum(self.weights * self.nodes**k))

    def central_moment(self, k: int) -> float:
        return float(np.sum(self.weights * (self.nodes - self.mean) ** k))

    def expect(self, f) -> float:
        """``E[f(x)]`` for a vectorized callable ``f``."""
        return float(np.sum(self.weights * f(self.nodes)))


def tilted(
    base: Base1D,
    c: float,
    t: float,
    *,
    order: int = 500,
    half_width: float = 26.0,
    passes: int = 2,
    extra_breaks: tuple[float, ...] = (),
) -> Tilted1D:
    """Quadrature representation and moments of ``mu_{c,t}``.

    Two-pass rescaling: a pilot pass on a width from ``approx_center_scale``
    locates ``(mean, sd)``; subsequent passes recentre on ``u = (x-mean)/sd``
    so the integrand stays O(1)-wide even as ``var -> 1/t`` near the
    Brascamp-Lieb cap. This peak-tracking is what keeps the variance from being
    biased *low* (the failure direction that fakes "saturation").
    """
    c = float(c)
    t = float(t)
    if t < 0:
        raise ValueError("t must be >= 0")

    nodes_ref, w_ref = _gauss_legendre(order)
    kinks = tuple(base.kinks()) + tuple(extra_breaks)
    center, scale = base.approx_center_scale(c, t)

    mean = center
    sd = scale
    nodes = None
    weights = None
    for _ in range(max(1, passes)):
        lo = center - half_width * scale
        hi = center + half_width * scale
        x, logj = _composite_panels(nodes_ref, w_ref, lo, hi, kinks)
        logw = base.neg_potential(x) + c * x - 0.5 * t * x * x + logj
        logw -= logw.max()
        w = np.exp(logw)
        wsum = w.sum()
        if not np.isfinite(wsum) or wsum <= 0:
            raise FloatingPointError("degenerate tilted-measure quadrature weights")
        w /= wsum
        mean = float(np.sum(w * x))
        var = max(float(np.sum(w * (x - mean) ** 2)), 1e-300)
        sd = np.sqrt(var)
        nodes, weights = x, w
        center, scale = mean, sd  # recentre/rescale for the next pass

    assert nodes is not None and weights is not None
    assert nodes.dtype == np.float64 and weights.dtype == np.float64
    return Tilted1D(nodes=nodes, weights=weights, mean=mean, var=sd * sd)


def _composite_panels(
    nodes_ref: np.ndarray,
    w_ref: np.ndarray,
    lo: float,
    hi: float,
    kinks: tuple[float, ...],
) -> tuple[np.ndarray, np.ndarray]:
    """Map reference GL nodes onto ``[lo, hi]`` split at any interior ``kinks``.

    Returns the concatenated nodes and their *log* quadrature weights (including
    the affine Jacobian of each panel), so non-smooth points of the potential
    fall on panel boundaries rather than inside a smooth panel.
    """
    breaks = [lo, hi]
    for k in kinks:
        if lo < k < hi:
            breaks.append(k)
    breaks = sorted(breaks)
    xs = []
    logws = []
    for a, b in zip(breaks[:-1], breaks[1:]):
        if b <= a:
            continue
        half = 0.5 * (b - a)
        mid = 0.5 * (a + b)
        xs.append(mid + half * nodes_ref)
        logws.append(np.log(w_ref) + np.log(half))
    return np.concatenate(xs), np.concatenate(logws)


def tilted_variance(base: Base1D, c: float, t: float, **kw) -> float:
    """Convenience: just ``Var(mu_{c,t})`` (the per-coordinate ``A_t^{(i)}``)."""
    return tilted(base, c, t, **kw).var


def tilted_dense(
    base: Base1D,
    c: float,
    t: float,
    *,
    breaks: tuple[float, ...] = (),
    npts: int = 4000,
    half_width: float = 26.0,
) -> Tilted1D:
    """A *dense* uniform-grid representation of ``mu_{c,t}`` for sharp integrals.

    Gauss-Legendre atoms (from `tilted`) integrate smooth functions to ~1e-11
    but are useless against a step indicator ``1{x <= x0}`` -- the failure that
    made the ``k=1`` conditional moments wrong. This builds a fine composite-
    trapezoid grid with panel boundaries at ``base.kinks()`` and any extra
    ``breaks`` (e.g. a conditioning threshold), so a step at a break is integrated
    exactly up to the trapezoid error of the smooth density on each side.
    """
    c = float(c)
    t = float(t)
    m = tilted(base, c, t)  # accurate (mean, sd) to set the grid extent
    sd = np.sqrt(m.var)
    lo = m.mean - half_width * sd
    hi = m.mean + half_width * sd
    # One sorted grid with a node EXACTLY at every break (kink / threshold), so
    # each break is a single interior node with full trapezoid weight -- no
    # duplicated panel endpoints (which dropped the endpoint half-weight under a
    # threshold indicator and degraded O(h^2) to O(h)).
    extra = np.array([b for b in (*base.kinks(), *breaks) if lo < b < hi], dtype=np.float64)
    u = np.union1d(np.linspace(lo, hi, int(npts)), extra)
    tw = _trapezoid_weights(u)  # nonuniform trapezoid weights
    logd = base.neg_potential(u) + c * u - 0.5 * t * u * u + np.log(tw)
    logd -= logd.max()
    d = np.exp(logd)
    d /= d.sum()
    mean = float(np.sum(d * u))
    var = float(np.sum(d * (u - mean) ** 2))
    return Tilted1D(nodes=u, weights=d, mean=mean, var=var)


def _trapezoid_weights(u: np.ndarray) -> np.ndarray:
    """Trapezoid quadrature weights on a sorted (possibly nonuniform) grid."""
    w = np.empty_like(u)
    w[1:-1] = 0.5 * (u[2:] - u[:-2])
    w[0] = 0.5 * (u[1] - u[0])
    w[-1] = 0.5 * (u[-1] - u[-2])
    return w
