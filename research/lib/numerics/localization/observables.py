"""Two-color observables and occupation integrals along a localization path.

Assembles, from a ``ProductState`` and a fixed cut ``E``, the Riccati-level
quantities (``modules/26-notation.md``, ``modules/27-riccati.md``):

    p = mu_t(E), q = 1-p, s = p q,
    delta_i = m^E_i - m^F_i        (centroid gap; supported on J),
    G = Sigma^E - Sigma^F          (covariance contrast; supported on J x J),
    S = s ||G||_HS^2               (source: only positive Riccati term),
    r = s |delta|^2,               (information rate; d[p]_t = s r dt)
    D = 2 s delta^T A delta - r^2, (coercive damping, D >= r^2)
    R0 = A0 - s0 delta0 delta0^T   (within-class covariance at t=0),
    X = (lambda_max(A) - 1)_+.

and the occupation integral ``Xi_S(T) = E int_0^{T wedge tau} S dt`` with the
coarse balanced stop ``tau = inf{t : p_t notin [1/3, 2/3]}`` (in-step linear
interpolation at the crossing).
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .cuts import CutSpec, conditional_moments
from .state import ProductState
from .sde import localization_path
from .tilt1d import Base1D


@dataclass
class Observables:
    """Two-color Riccati quantities at one time on one path."""

    t: float
    p: float
    s: float
    r: float
    D: float
    S: float
    lambda_max: float
    X: float
    J: tuple[int, ...]
    delta_J: np.ndarray   # centroid gap on the J block
    A_J: np.ndarray       # diagonal covariance on J
    G: np.ndarray         # k x k covariance contrast block

    def source_in_direction(self, coord: int) -> float:
        """``s |G e_coord|^2`` for a coordinate ``coord in J`` (per-direction)."""
        idx = self.J.index(coord)
        col = self.G[:, idx]
        return float(self.s * np.dot(col, col))


def observe(state: ProductState, cut: CutSpec, **cm_kw) -> Observables:
    """Compute the two-color observables for ``cut`` at the current state."""
    cm = conditional_moments(state, cut, **cm_kw)
    p = cm.p
    s = p * (1.0 - p)
    delta_J = cm.mE - cm.mF
    A_J = cm.A_J
    G = cm.SigmaE - cm.SigmaF

    r = s * float(np.dot(delta_J, delta_J))
    D = 2.0 * s * float(np.sum(A_J * delta_J * delta_J)) - r * r
    S = s * float(np.sum(G * G))
    lam = state.lambda_max()
    return Observables(
        t=state.t, p=p, s=s, r=r, D=D, S=S,
        lambda_max=lam, X=max(lam - 1.0, 0.0),
        J=cut.J, delta_J=delta_J, A_J=A_J, G=G,
    )


def R0_diag(state0: ProductState, cut: CutSpec, coord: int, **cm_kw) -> float:
    """``(R0)_{coord,coord} = A0_{cc} - s0 delta0_c^2`` at the initial state."""
    cm = conditional_moments(state0, cut, **cm_kw)
    s0 = cm.p * (1.0 - cm.p)
    idx = cut.J.index(coord)
    delta_c = cm.mE[idx] - cm.mF[idx]
    return float(cm.A_J[idx] - s0 * delta_c * delta_c)


# ---------------------------------------------------------------------------
# Occupation integrals along a path
# ---------------------------------------------------------------------------

_BALANCED = (1.0 / 3.0, 2.0 / 3.0)


@dataclass
class PathIntegrals:
    """Accumulated integrals along one localization path."""

    xi_S: float            # int S dt
    xi_r: float            # int r dt
    xi_dir: float          # int s |G e_dir|^2 dt  (if a direction was given)
    t_stop: float          # tau wedge T actually reached
    tau_hit: bool


def integrate_path(
    base: Base1D,
    n: int,
    cut: CutSpec,
    T: float,
    dt: float,
    rng: np.random.Generator,
    *,
    direction: int | None = None,
    stop_at_tau: bool = False,
    quad: dict | None = None,
    cm_kw: dict | None = None,
) -> PathIntegrals:
    """Integrate the source (and friends) along one path on ``[0, T]``.

    Trapezoid in time. If ``stop_at_tau`` and ``p_t`` leaves ``[1/3, 2/3]``
    between two steps, the crossing time is found by linear interpolation in
    ``p`` and the final sub-interval is added with the boundary integrand
    linearly interpolated -- so the stop does not bias the integral.
    """
    cm_kw = cm_kw or {}
    xi_S = xi_r = xi_dir = 0.0
    prev_t = None
    prev = None  # (S, r, dir, p)
    t_stop = 0.0
    tau_hit = False

    for state in localization_path(base, n, T, dt, rng, quad=quad or {}):
        obs = observe(state, cut, **cm_kw)
        d = obs.source_in_direction(direction) if direction is not None else 0.0
        cur = (obs.S, obs.r, d, obs.p)
        t = state.t

        if prev is not None:
            outside = not (_BALANCED[0] <= obs.p <= _BALANCED[1])
            if stop_at_tau and outside:
                # linear-interpolate the crossing fraction in p
                p0 = prev[3]
                bound = _BALANCED[0] if obs.p < _BALANCED[0] else _BALANCED[1]
                denom = obs.p - p0
                frac = 1.0 if denom == 0 else (bound - p0) / denom
                frac = min(max(frac, 0.0), 1.0)
                h = (t - prev_t) * frac
                # integrand at crossing by linear interpolation
                Sx = prev[0] + frac * (cur[0] - prev[0])
                rx = prev[1] + frac * (cur[1] - prev[1])
                dx = prev[2] + frac * (cur[2] - prev[2])
                xi_S += 0.5 * (prev[0] + Sx) * h
                xi_r += 0.5 * (prev[1] + rx) * h
                xi_dir += 0.5 * (prev[2] + dx) * h
                t_stop = prev_t + h
                tau_hit = True
                return PathIntegrals(xi_S, xi_r, xi_dir, t_stop, tau_hit)

            h = t - prev_t
            xi_S += 0.5 * (prev[0] + cur[0]) * h
            xi_r += 0.5 * (prev[1] + cur[1]) * h
            xi_dir += 0.5 * (prev[2] + cur[2]) * h

        prev_t = t
        prev = cur
        t_stop = t

    return PathIntegrals(xi_S, xi_r, xi_dir, t_stop, tau_hit)


@dataclass
class EnsembleResult:
    mean: float
    stderr: float
    n_paths: int
    label: str


def ensemble_mean(values: np.ndarray, label: str) -> EnsembleResult:
    values = np.asarray(values, dtype=np.float64)
    n = values.size
    return EnsembleResult(
        mean=float(values.mean()),
        stderr=float(values.std(ddof=1) / np.sqrt(n)) if n > 1 else float("nan"),
        n_paths=n,
        label=label,
    )
