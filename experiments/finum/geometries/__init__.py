"""finum.geometries — the measure zoo + named test functions for the A1-A5 batteries.

ONE place to add a test measure. A target battery (``finum/targets/``) builds an ``Instance``
around a distribution here and evaluates directional numerical diagnostics; ``references``
contains analytic upper-bound oracles for calibration or assumption checks.

  distributions   GaussianDistribution, DoubleWell1D, PerturbedGaussian1D
  test_functions  LinearFunction, Polynomial1D, SmoothModeIndicator1D
  rayleigh        rayleigh_from_samples / rayleigh_grid_1d  (lower bound of a named witness)
  references      bakry_emery_cp, holley_stroock_cp         (refutable upper-bound oracles)
"""
from __future__ import annotations

from . import references
from .distributions import (
    Distribution,
    DoubleWell1D,
    GaussianDistribution,
    PerturbedGaussian1D,
)
from .rayleigh import rayleigh_from_samples, rayleigh_grid_1d
from .references import bakry_emery_cp, holley_stroock_cp
from .test_functions import (
    LinearFunction,
    Polynomial1D,
    SmoothModeIndicator1D,
    TestFunction,
)

__all__ = [
    "Distribution", "GaussianDistribution", "DoubleWell1D", "PerturbedGaussian1D",
    "TestFunction", "LinearFunction", "Polynomial1D", "SmoothModeIndicator1D",
    "rayleigh_from_samples", "rayleigh_grid_1d",
    "bakry_emery_cp", "holley_stroock_cp", "references",
]
