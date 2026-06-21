"""Rayleigh-quotient lower bounds for a *named* test function.

``finum.constants.poincare_lower`` optimizes the linear (and quadratic) test family in closed
form. These helpers instead evaluate ``R[f] = Var_mu(f) / E_mu||grad f||^2`` for ONE explicit
``geometries.test_functions.TestFunction`` ``f`` — the way to get the lower bound of a specific
witness (e.g. the smooth mode indicator on a double well, where the optimal linear test is weak).
Every value returned is a certified lower bound ``R[f] <= C_P``.

``rayleigh_from_samples`` uses MC draws; ``rayleigh_grid_1d`` uses exact 1D trapezoid quadrature
against ``exp(-U)`` (no sampling noise) and is the one to use for 1D targets.
"""
from __future__ import annotations

import numpy as np
from scipy.integrate import trapezoid

from .test_functions import TestFunction


def rayleigh_from_samples(samples: np.ndarray, f: TestFunction) -> float:
    """``Var(f)/E||grad f||^2`` from samples ``(N, d)`` — a certified lower bound on ``C_P``."""
    values = f.value(samples)
    variance = float(np.var(values))
    energy = float(np.mean(f.grad_norm_squared(samples)))
    if energy <= 0:
        return float("inf")
    return variance / energy


def rayleigh_grid_1d(
    distribution, f: TestFunction, *, radius: float = 8.0, grid_size: int = 4001
) -> float:
    """Exact 1D Rayleigh quotient of ``f`` under ``mu propto exp(-U)`` by trapezoid quadrature.

    ``distribution`` must expose ``potential(x)`` (= ``U`` up to a constant). Returns a certified
    lower bound ``R[f] <= C_P`` with no MC noise.
    """
    x = np.linspace(-radius, radius, grid_size)
    log_density = -np.asarray(distribution.potential(x), dtype=float)
    log_density -= float(np.max(log_density))
    density = np.exp(log_density)
    z = trapezoid(density, x)
    weights = density / z
    values = f.value(x[:, None])
    mean = trapezoid(values * weights, x)
    variance = trapezoid((values - mean) ** 2 * weights, x)
    energy = trapezoid(f.grad_norm_squared(x[:, None]) * weights, x)
    if energy <= 0:
        return float("inf")
    return float(variance / energy)
