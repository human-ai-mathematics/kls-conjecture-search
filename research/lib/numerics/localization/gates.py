"""Convergence and cross-check gates for the deferred large-n alignment runs.

The foundation oracle suite (``tests/``) trusts the engine at small ``k``. Before
reading any DIRECTIONAL number off a multi-coordinate thin-shell run (the
``q:alignment`` family), two gates must pass first:

  ``n_bins_convergence``  the gridded ``k>=2`` background converges -- report the
                          relative drift of the mass ``p`` and the source ``S`` as
                          ``n_bins`` doubles. A run whose number moves under
                          refinement is a binning artifact, not evidence.
  ``fft_vs_mc``           the FFT leave-k-out background agrees with an INDEPENDENT
                          inverse-CDF Monte-Carlo estimate of the same ``(p, S)``.
                          This is the direct guard against the retracted Gaussian
                          surrogate (see
                          ``explorations/2026-06-14-energy-shell-occupation.md``):
                          the MC reuses the sampler discipline of
                          ``tests/test_06_offdiagonal_vs_mc.py`` for a general
                          ``Base1D``.

Neither gate certifies anything; they bound numerical error so a directional observation is not
just a discretization artifact. Per the epistemic contract they never promote a ledger
node. Large ``n`` still needs the deferred saddlepoint / prefix-suffix background
(see README) -- these gates are how you would *detect* that the FFT background has
run out of accuracy.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .cuts import CutSpec
from .state import ProductState
from .observables import observe
from .tilt1d import Base1D


@dataclass
class GateResult:
    name: str
    passed: bool
    measured: float
    tol: float
    detail: str

    def __str__(self) -> str:
        flag = "PASS" if self.passed else "FAIL"
        return f"[{flag}] {self.name}: {self.detail}"

    def as_record(self) -> dict:
        return {
            "gate": self.name,
            "passed": self.passed,
            "measured": self.measured,
            "tol": self.tol,
            "detail": self.detail,
        }


def _rel(a: float, b: float) -> float:
    return abs(b - a) / max(abs(b), 1e-12)


def n_bins_convergence(
    state: ProductState,
    cut: CutSpec,
    *,
    n_bins_list: tuple[int, ...] = (1 << 15, 1 << 16, 1 << 17),
    tol: float = 5e-3,
    cm_kw: dict | None = None,
) -> GateResult:
    """Mass/source drift under ``n_bins`` doubling.

    Pass iff the relative change of both ``p`` and ``S`` over the LAST doubling is
    below ``tol``. (We watch ``S`` because it is the quantity the thin-shell run
    integrates; ``p`` guards the balance.)
    """
    cm_kw = dict(cm_kw or {})
    cm_kw.pop("n_bins", None)
    ps: list[float] = []
    Ss: list[float] = []
    for nb in n_bins_list:
        obs = observe(state, cut, n_bins=nb, **cm_kw)
        ps.append(obs.p)
        Ss.append(obs.S)
    dS = _rel(Ss[-2], Ss[-1])
    dp = _rel(ps[-2], ps[-1])
    measured = max(dS, dp)
    detail = (
        f"last-step rel drift S {dS:.2e}, p {dp:.2e} over "
        f"n_bins {n_bins_list[-2]}->{n_bins_list[-1]} (tol {tol:.0e}); "
        f"S={Ss[-1]:.5f} p={ps[-1]:.5f}"
    )
    return GateResult("n_bins_convergence", measured < tol, measured, tol, detail)


def _inverse_cdf_sample(
    base: Base1D, c_i: float, t: float, rng: np.random.Generator, N: int,
    *, half: float = 32.0, npts: int = 300_000,
) -> np.ndarray:
    """One coordinate's tilted marginal mu_{c_i, t} by inverse-CDF sampling."""
    u = np.linspace(-half, half, npts)
    logd = base.neg_potential(u) + c_i * u - 0.5 * t * u * u
    logd -= logd.max()
    d = np.exp(logd)
    cdf = np.cumsum(d)
    cdf /= cdf[-1]
    return np.interp(rng.random(N), cdf, u)


def _mc_observables(
    state: ProductState, cut: CutSpec, rng: np.random.Generator, N: int,
) -> tuple[float, float]:
    """``(p, S)`` of ``cut`` from an INDEPENDENT inverse-CDF Monte-Carlo sampler.

    Mirrors ``observe`` from raw samples: only the cut's ``J`` block matters for
    ``G`` (``lem:block``), so we sample exactly those coordinates.
    """
    J = cut.J
    cols = [
        _inverse_cdf_sample(state.base, float(state.c[i]), state.t, rng, N)
        for i in J
    ]
    XJ = np.stack(cols, axis=1)                      # (N, k)
    Y = cut.psi.apply(XJ)                            # psi applied coordinatewise
    ssum = Y.sum(axis=1)
    inE = ssum >= cut.theta if cut.side == "ge" else ssum <= cut.theta
    p = float(inE.mean())
    XE, XF = XJ[inE], XJ[~inE]
    mE, mF = XE.mean(0), XF.mean(0)
    k = len(J)
    SigmaE = np.cov(XE, rowvar=False).reshape(k, k)
    SigmaF = np.cov(XF, rowvar=False).reshape(k, k)
    G = SigmaE - SigmaF
    s = p * (1.0 - p)
    S = s * float(np.sum(G * G))
    return p, S


def fft_vs_mc(
    state: ProductState,
    cut: CutSpec,
    rng: np.random.Generator,
    *,
    N: int = 2_000_000,
    n_bins: int = 1 << 17,
    tol_p: float = 5e-3,
    tol_S: float = 6e-2,
    cm_kw: dict | None = None,
) -> GateResult:
    """Cross-check the FFT-background ``(p, S)`` against independent MC.

    Pass iff ``|p_fft - p_mc| < tol_p`` and the relative source gap is ``< tol_S``.
    (``S`` is a quadratic functional of the full conditional covariance contrast,
    so its MC estimate is noisier than ``p`` -- hence the looser relative tol.)
    """
    cm_kw = dict(cm_kw or {})
    cm_kw["n_bins"] = n_bins
    obs = observe(state, cut, **cm_kw)
    p_mc, S_mc = _mc_observables(state, cut, rng, N)
    dp = abs(obs.p - p_mc)
    dS = _rel(S_mc, obs.S)
    passed = (dp < tol_p) and (dS < tol_S)
    measured = max(dp / tol_p, dS / tol_S)  # normalized worst margin (pass iff < 1)
    detail = (
        f"|dp|={dp:.2e} (tol {tol_p:.0e}), rel dS={dS:.2e} (tol {tol_S:.0e}); "
        f"FFT p={obs.p:.4f} S={obs.S:.4f} | MC p={p_mc:.4f} S={S_mc:.4f} (N={N})"
    )
    return GateResult("fft_vs_mc", passed, measured, 1.0, detail)
