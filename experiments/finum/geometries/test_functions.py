"""Explicit test functions for variational (Rayleigh) lower bounds.

Every test function ``f`` gives the rigorous relation
``Var(f)/E||grad f||^2 <= C_P`` when its expectations are exact. These are the named witnesses a
sample- or grid-Rayleigh quotient estimates; a numerical value is directional without error
bounds. The linear one reproduces ``finum.constants
.poincare_lower``, the polynomial/mode-indicator ones extend the witness family for metastable
targets (the smooth ``tanh`` mode indicator is the natural near-eigenfunction of a two-well
density, where it gives a much larger — i.e. tighter — lower bound than any linear test).
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np


class TestFunction:
    name: str

    def value(self, x: np.ndarray) -> np.ndarray:
        raise NotImplementedError

    def grad_norm_squared(self, x: np.ndarray) -> np.ndarray:
        raise NotImplementedError


@dataclass(frozen=True)
class LinearFunction(TestFunction):
    """``f(x) = <v, x>`` (v normalized): the linear test, ``R[f] = v^T Cov v``."""

    direction: np.ndarray
    name: str = "linear"

    def __post_init__(self) -> None:
        v = np.asarray(self.direction, dtype=float)
        norm = np.linalg.norm(v)
        if norm == 0:
            raise ValueError("direction must be nonzero")
        object.__setattr__(self, "direction", v / norm)

    def value(self, x: np.ndarray) -> np.ndarray:
        x = np.asarray(x, dtype=float)
        return x @ self.direction

    def grad_norm_squared(self, x: np.ndarray) -> np.ndarray:
        return np.ones(x.shape[0])


@dataclass(frozen=True)
class Polynomial1D(TestFunction):
    """A univariate polynomial test function from its coefficient tuple."""

    coefficients: tuple[float, ...]
    name: str = "polynomial_1d"

    def value(self, x: np.ndarray) -> np.ndarray:
        t = np.asarray(x).reshape(-1)
        out = np.zeros_like(t, dtype=float)
        for power, coeff in enumerate(self.coefficients):
            out += coeff * t**power
        return out

    def grad_norm_squared(self, x: np.ndarray) -> np.ndarray:
        t = np.asarray(x).reshape(-1)
        deriv = np.zeros_like(t, dtype=float)
        for power, coeff in enumerate(self.coefficients[1:], start=1):
            deriv += power * coeff * t ** (power - 1)
        return deriv**2


@dataclass(frozen=True)
class SmoothModeIndicator1D(TestFunction):
    """Smooth proxy ``tanh(sharpness x)`` for ``1_{x>0}`` — the two-well near-eigenfunction."""

    sharpness: float = 4.0
    name: str = "smooth_mode_indicator_1d"

    def value(self, x: np.ndarray) -> np.ndarray:
        t = np.asarray(x).reshape(-1)
        return np.tanh(self.sharpness * t)

    def grad_norm_squared(self, x: np.ndarray) -> np.ndarray:
        t = np.asarray(x).reshape(-1)
        sech2 = 1.0 / np.cosh(self.sharpness * t) ** 2
        return (self.sharpness * sech2) ** 2
