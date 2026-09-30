"""Cuts and their two-color conditional moments -- without a Gaussian surrogate.

A cut here is ``E = {x : sum_{i in J} psi(x_i) (side) theta}`` for an index set
``J``, a per-coordinate map ``psi``, threshold ``theta`` and ``side in {ge, le}``.
We need the two-color conditional first and second moments of the coordinates
under ``E`` and ``F = E^c`` -- in particular the **off-diagonal** conditional
covariance ``Cov(x_i, x_j | E)``, the quantity the retracted energy-shell
computation got wrong by regressing against a Gaussian surrogate
(``explorations/2026-06-14-energy-shell-occupation.md``).

Method (exact up to background binning). Condition the product on the one-sided
sum event by integrating against the law of the *other* coordinates' partial sum:

    E[g(x_i) 1_E] = integral g(x_i) P(W_{-i} (side) theta - psi(x_i)) dmu_t^(i),
    E[x_i x_j 1_E] = integral x_i x_j P(W_{-ij} (side) theta - psi(x_i) - psi(x_j)),

with ``W_{-i}, W_{-ij}`` the leave-one/two-out partial sums. The *target*
coordinate is integrated on a dense grid (`tilt1d.tilted_dense`) with panel
breaks at ``psi``'s kinks and (when ``k=1``) the threshold level set, so a sharp
membership is integrated exactly; only the smooth *background* sum law is gridded
(linear binning + FFT convolution).

For ``i, j not in J`` the coordinate is independent of ``E``, so ``G = Sigma^E -
Sigma^F`` is supported on the ``J x J`` block (``lem:block``); only that block is
computed.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Literal

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.signal import fftconvolve

from .state import ProductState
from .tilt1d import tilted, tilted_dense

Side = Literal["ge", "le"]


@dataclass(frozen=True)
class Psi:
    """A per-coordinate cut map with knowledge of its non-smooth structure."""

    name: str
    apply: Callable[[np.ndarray], np.ndarray]
    kinks: tuple[float, ...]
    level_points: Callable[[float], tuple[float, ...]]


PSI_ID = Psi(
    name="identity",
    apply=lambda x: x,
    kinks=(),
    level_points=lambda th: (float(th),),
)
PSI_SQ = Psi(
    name="square",
    apply=lambda x: x * x,
    kinks=(0.0,),
    level_points=lambda th: (-np.sqrt(th), np.sqrt(th)) if th > 0 else (),
)


@dataclass(frozen=True)
class CutSpec:
    """``E = { sum_{i in J} psi(x_i) (side) theta }``."""

    J: tuple[int, ...]
    psi: Psi
    theta: float
    side: Side = "ge"

    @property
    def k(self) -> int:
        return len(self.J)


def halfspace(coord: int, x0: float) -> CutSpec:
    """``E = {x_coord <= x0}``."""
    return CutSpec(J=(coord,), psi=PSI_ID, theta=float(x0), side="le")


def single_coord(coord: int, theta: float, *, psi: Psi = PSI_ID, side: Side = "ge") -> CutSpec:
    return CutSpec(J=(coord,), psi=psi, theta=float(theta), side=side)


def block_sum(J, theta: float, *, psi: Psi = PSI_ID, side: Side = "ge") -> CutSpec:
    return CutSpec(J=tuple(int(i) for i in J), psi=psi, theta=float(theta), side=side)


def energy_shell(n: int, theta: float) -> CutSpec:
    """``E = {sum_i x_i^2 >= theta}`` -- the W-measurable energy shell."""
    return CutSpec(J=tuple(range(n)), psi=PSI_SQ, theta=float(theta), side="ge")


# ---------------------------------------------------------------------------
# Background partial-sum law (gridded)
# ---------------------------------------------------------------------------


class _SumDist:
    """Law of ``sum psi(x_i)`` over background coords, on a uniform grid.

    Empty set -> degenerate at 0. ``sf(z)=P(W>=z)`` by linear interpolation of
    the grid survival; the convolved law is smooth so interpolation is accurate.
    """

    def __init__(self, origin: float, h: float, pmf: np.ndarray, degenerate: bool):
        self.origin = float(origin)
        self.h = float(h)
        self.pmf = pmf
        self.degenerate = degenerate
        if not degenerate:
            self._sf_grid = np.cumsum(pmf[::-1])[::-1]
            self._size = pmf.size

    @classmethod
    def from_coords(cls, values, weights, vmin, vmax, n_bins) -> "_SumDist":
        if len(values) == 0:
            return cls(0.0, 1.0, np.array([1.0]), degenerate=True)
        h = (vmax - vmin) / n_bins
        if h <= 0:
            h = 1.0
        size = n_bins + 2
        acc = None
        for v, w in zip(values, weights):
            pmf = _linear_bin(v, w, vmin, h, size)
            acc = pmf if acc is None else fftconvolve(acc, pmf)
        acc = np.maximum(acc, 0.0)
        s = acc.sum()
        if s > 0:
            acc /= s
        return cls(vmin * len(values), h, acc, degenerate=False)

    def membership(self, thresh: np.ndarray, side: Side) -> np.ndarray:
        """Vectorized ``P(W >= thresh)`` (side='ge') or ``P(W <= thresh)``."""
        thr = np.asarray(thresh, dtype=np.float64)
        if self.degenerate:
            # P(0 >= thr): 1 for thr<0, 0 for thr>0, 1/2 at the boundary thr=0.
            # The 1/2 gives the target node sitting exactly on the threshold its
            # correct trapezoid half-weight, restoring O(h^2) convergence.
            sf = np.where(thr < 0.0, 1.0, np.where(thr > 0.0, 0.0, 0.5))
        else:
            f = (thr - self.origin) / self.h
            lo = np.clip(np.floor(f).astype(np.int64), 0, self._size - 2)
            frac = f - lo
            sf_in = (1 - frac) * self._sf_grid[lo] + frac * self._sf_grid[lo + 1]
            sf = np.where(f <= 0, 1.0, np.where(f >= self._size - 1, 0.0, sf_in))
        return sf if side == "ge" else 1.0 - sf


def _linear_bin(v, w, origin, h, size) -> np.ndarray:
    pmf = np.zeros(size, dtype=np.float64)
    f = (v - origin) / h
    lo = np.clip(np.floor(f).astype(np.int64), 0, size - 2)
    frac = f - lo
    np.add.at(pmf, lo, w * (1.0 - frac))
    np.add.at(pmf, lo + 1, w * frac)
    return pmf


# ---------------------------------------------------------------------------
# Conditional moments
# ---------------------------------------------------------------------------


@dataclass
class ConditionalMoments:
    """Two-color conditional moments on the ``J x J`` block."""

    J: tuple[int, ...]
    p: float
    mE: np.ndarray
    mF: np.ndarray
    SigmaE: np.ndarray
    SigmaF: np.ndarray
    a_J: np.ndarray
    A_J: np.ndarray


def conditional_moments(
    state: ProductState,
    cut: CutSpec,
    *,
    n_bins: int = 65536,
    npts: int = 4000,
    atom_order: int = 300,
) -> ConditionalMoments:
    """Two-color conditional moments on the cut's ``J`` block (surrogate-free).

    Accuracy. ``k=1`` is exact partial integration (O(h^2), ~1e-6). For ``k>=2``
    the background sum law is gridded; the error is dominated by ``n_bins`` and
    converges ~linearly (vs an independent MC: ``n_bins=2^17`` gives ``p`` to
    ~5e-4, conditional covariances to MC noise). The default suffices for the
    foundation oracles (small ``k``). The deferred large-``n`` ``conj:product-alignment``
    runs need a higher ``n_bins`` or a better background method -- see README.
    """
    if cut.k == 1:
        return _moments_k1(state, cut, npts=npts)

    J = cut.J
    k = cut.k
    psi = cut.psi
    side = cut.side
    theta = cut.theta

    # For k>=2 the background smooths the threshold, so the target integrand is
    # smooth (kink only at psi's own breaks). Use high-order Gauss-Legendre atoms
    # (split at psi.kinks) rather than the 4000-point dense grid: the off-diagonal
    # is an O(atoms^2) double sum, so a few hundred GL nodes is both faster and
    # more accurate than thousands of trapezoid nodes.
    gl = [
        tilted(state.base, float(state.c[i]), state.t, order=atom_order,
               extra_breaks=tuple(psi.kinks))
        for i in J
    ]
    xs = [g.nodes for g in gl]
    ws = [g.weights for g in gl]
    ys = [psi.apply(x) for x in xs]

    vmin = min(float(y.min()) for y in ys)
    vmax = max(float(y.max()) for y in ys)
    if vmax <= vmin:
        vmax = vmin + 1.0

    # Single-coordinate conditional sums via leave-one-out background.
    p_each = np.empty(k)
    Ex1 = np.empty(k); Ex2 = np.empty(k)
    Ew1 = np.empty(k); Ew2 = np.empty(k)
    for i in range(k):
        bg = _SumDist.from_coords(
            [ys[m] for m in range(k) if m != i],
            [ws[m] for m in range(k) if m != i],
            vmin, vmax, n_bins,
        )
        memb = bg.membership(theta - ys[i], side)
        wi, xi = ws[i], xs[i]
        p_each[i] = float(np.sum(wi * memb))
        Ex1[i] = float(np.sum(wi * xi * memb))
        Ex2[i] = float(np.sum(wi * xi * xi * memb))
        membF = 1.0 - memb
        Ew1[i] = float(np.sum(wi * xi * membF))
        Ew2[i] = float(np.sum(wi * xi * xi * membF))

    p = float(np.mean(p_each))
    q = 1.0 - p
    mE = Ex1 / p
    mF = Ew1 / q
    SigmaE = np.zeros((k, k))
    SigmaF = np.zeros((k, k))
    for i in range(k):
        SigmaE[i, i] = Ex2[i] / p - mE[i] ** 2
        SigmaF[i, i] = Ew2[i] / q - mF[i] ** 2

    # Off-diagonal via leave-two-out background.
    for i in range(k):
        for j in range(i + 1, k):
            bg = _SumDist.from_coords(
                [ys[m] for m in range(k) if m not in (i, j)],
                [ws[m] for m in range(k) if m not in (i, j)],
                vmin, vmax, n_bins,
            )
            thr = theta - ys[i][:, None] - ys[j][None, :]
            memb = bg.membership(thr, side)
            wij = ws[i][:, None] * ws[j][None, :]
            xij = xs[i][:, None] * xs[j][None, :]
            ExixjE = float(np.sum(wij * xij * memb))
            ExixjF = float(np.sum(wij * xij * (1.0 - memb)))
            SigmaE[i, j] = SigmaE[j, i] = ExixjE / p - mE[i] * mE[j]
            SigmaF[i, j] = SigmaF[j, i] = ExixjF / q - mF[i] * mF[j]

    marg = state.marginals()
    a_J = np.array([marg[i].mean for i in J])
    A_J = np.array([marg[i].var for i in J])
    return ConditionalMoments(J=J, p=p, mE=mE, mF=mF, SigmaE=SigmaE, SigmaF=SigmaF, a_J=a_J, A_J=A_J)


def _moments_k1(state: ProductState, cut: CutSpec, *, npts: int = 4000) -> ConditionalMoments:
    """Exact single-coordinate conditional moments by partial integration.

    A ``k=1`` cut has a genuine discontinuity at ``psi(x)=theta``; integrating it
    by a smooth quadrature is what introduced the original ~1e-3 error. Here we
    build the cumulative trapezoid integrals of ``[1, x, x^2] dmu_i`` on a fine
    uniform grid and evaluate them at the exact threshold by linear
    interpolation -- O(h^2), node-placement-independent.
    """
    i = cut.J[0]
    psi = cut.psi
    theta = float(cut.theta)
    side = cut.side
    ci = float(state.c[i])
    base = state.base

    m = tilted(base, ci, state.t)
    sd = np.sqrt(m.var)
    H = 16.0
    u = np.linspace(m.mean - H * sd, m.mean + H * sd, int(npts))
    logd = base.neg_potential(u) + ci * u - 0.5 * state.t * u * u
    logd -= logd.max()
    dens = np.exp(logd)

    C0 = cumulative_trapezoid(dens, u, initial=0.0)
    C1 = cumulative_trapezoid(dens * u, u, initial=0.0)
    C2 = cumulative_trapezoid(dens * u * u, u, initial=0.0)
    Z, M1, M2 = C0[-1], C1[-1], C2[-1]

    def cdf(level: float) -> tuple[float, float, float]:
        """``(∫_{-inf}^{level} dmu, ∫ x dmu, ∫ x^2 dmu)`` (unnormalized)."""
        return (
            float(np.interp(level, u, C0)),
            float(np.interp(level, u, C1)),
            float(np.interp(level, u, C2)),
        )

    # E-region integrals I0,I1,I2 (unnormalized) from the level set + side.
    if psi.name == "identity":
        a0, a1, a2 = cdf(theta)
        if side == "le":  # {x <= theta}
            I = (a0, a1, a2)
        else:             # {x >= theta}
            I = (Z - a0, M1 - a1, M2 - a2)
    elif psi.name == "square":
        if theta <= 0:
            inside = (0.0, 0.0, 0.0)
        else:
            r = np.sqrt(theta)
            lo0, lo1, lo2 = cdf(-r)
            hi0, hi1, hi2 = cdf(r)
            inside = (hi0 - lo0, hi1 - lo1, hi2 - lo2)  # {x^2 <= theta}
        if side == "le":  # {x^2 <= theta}
            I = inside
        else:             # {x^2 >= theta} = complement
            I = (Z - inside[0], M1 - inside[1], M2 - inside[2])
    else:
        raise ValueError(f"k=1 partial integration not implemented for psi={psi.name!r}")

    I0, I1, I2 = I
    Jc0, Jc1, Jc2 = Z - I0, M1 - I1, M2 - I2  # complement (F) integrals
    p = I0 / Z
    mE = I1 / I0
    SigmaE = I2 / I0 - mE * mE
    mF = Jc1 / Jc0
    SigmaF = Jc2 / Jc0 - mF * mF

    return ConditionalMoments(
        J=cut.J,
        p=p,
        mE=np.array([mE]),
        mF=np.array([mF]),
        SigmaE=np.array([[SigmaE]]),
        SigmaF=np.array([[SigmaF]]),
        a_J=np.array([m.mean]),
        A_J=np.array([m.var]),
    )


def balanced_threshold(
    state: ProductState,
    J,
    *,
    psi: Psi = PSI_SQ,
    side: Side = "ge",
    p_target: float = 0.5,
    n_bins: int = 65536,
    npts: int = 4000,
) -> float:
    """Solve ``theta`` so ``mu_t(E)=p_target`` (keeps cuts balanced across n)."""
    J = tuple(int(i) for i in J)
    dense = [tilted_dense(state.base, float(state.c[i]), state.t, breaks=tuple(psi.kinks), npts=npts) for i in J]
    ys = [psi.apply(d.nodes) for d in dense]
    ws = [d.weights for d in dense]
    vmin = min(float(y.min()) for y in ys)
    vmax = max(float(y.max()) for y in ys)
    full = _SumDist.from_coords(ys, ws, vmin, vmax, n_bins)
    grid = full.origin + full.h * np.arange(full.pmf.size)
    sf = full._sf_grid  # P(W >= grid), decreasing
    prob = sf if side == "ge" else 1.0 - sf
    # find theta with prob(theta) ~ p_target
    if side == "ge":
        idx = int(np.clip(np.searchsorted(-prob, -p_target), 1, grid.size - 1))
    else:
        idx = int(np.clip(np.searchsorted(prob, p_target), 1, grid.size - 1))
    return float(grid[idx])
