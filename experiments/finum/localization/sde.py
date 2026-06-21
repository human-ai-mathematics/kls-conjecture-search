"""Seeded Euler-Maruyama integrator for the localization tilt process.

The Eldan tilt obeys ``dc_t = dW_t + a_t dt`` with ``a_t = mean(mu_t)`` (this is
the SDE that makes ``da_t = A_t dW_t``; for the Gaussian base it reproduces
``A_t = (1+t)^{-1} I`` exactly -- see the oracle test). For a product measure
each coordinate evolves independently, driven by its own Brownian motion.

Reproducibility: streams come from ``numpy.random.default_rng`` seeded via a
``SeedSequence`` so that independent paths use ``SeedSequence(seed).spawn(k)``
-- never ``seed + i`` and never the legacy global RNG.
"""

from __future__ import annotations

from collections.abc import Iterator

import numpy as np

from .state import ProductState
from .tilt1d import Base1D


def make_rng(seed: int) -> np.random.Generator:
    """A float64 PCG64 generator from an integer seed."""
    return np.random.default_rng(np.random.SeedSequence(int(seed)))


def spawn_rngs(seed: int, k: int) -> list[np.random.Generator]:
    """``k`` independent generators with provenance-stable child seeds."""
    children = np.random.SeedSequence(int(seed)).spawn(int(k))
    return [np.random.default_rng(s) for s in children]


def localization_path(
    base: Base1D,
    n: int,
    T: float,
    dt: float,
    rng: np.random.Generator,
    *,
    t0: float = 0.0,
    check_bl: bool = True,
    bl_tol: float = 1e-6,
    quad: dict | None = None,
) -> Iterator[ProductState]:
    """Yield ``ProductState`` along one localization path on ``[t0, T]``.

    Starts at the isotropic state ``c=0`` (if ``t0=0``). Yields the state at
    each grid time ``t0, t0+dt, ...`` up to and including the last node ``<= T``.
    The first yielded state is the initial one (before any step). The BL cap is
    asserted at every step when ``check_bl`` (vacuous at ``t=0``).
    """
    quad = quad or {}
    if dt <= 0:
        raise ValueError("dt must be > 0")
    c = np.zeros(n, dtype=np.float64)
    state = ProductState(base=base, c=c, t=t0, quad=quad)
    yield state

    t = t0
    sqrt_dt = np.sqrt(dt)
    n_steps = int(np.floor((T - t0) / dt + 1e-12))
    for _ in range(n_steps):
        a = state.mean()
        dW = rng.standard_normal(n) * sqrt_dt
        c = state.c + a * dt + dW
        t = t + dt
        state = ProductState(base=base, c=c, t=t, quad=quad)
        if check_bl:
            state.check_bl_cap(tol=bl_tol)
        yield state
