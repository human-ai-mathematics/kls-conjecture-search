"""The measure zoo — concrete test geometries for the A1-A5 batteries.

A geometry exposes a log-density (``potential`` = ``-log`` density up to a constant) and a
``sample(n, rng)`` draw, so the sound refuters (``finum.constants.poincare_lower`` /
``poincare_lower_basis``) can be pointed at it directly, and the 1D ones expose the analytic
hooks (Hessian floor, perturbation oscillation) the ``geometries.references`` oracle bounds need.

The metastable ``DoubleWell1D`` and the bounded-perturbation ``PerturbedGaussian1D`` are the
canonical non-trivial Poincare test cases (a two-mode target where a tail-blind bound fails, and
a Holley-Stroock reference-transfer target). These geometries carry no certification machinery:
finum's refuter + verdict layer is the only sound path — numerics never prove.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

import numpy as np
from numpy.typing import ArrayLike


class Distribution(Protocol):
    """Minimal interface the refuters and Rayleigh tests consume."""

    name: str
    dim: int

    def potential(self, x: np.ndarray) -> np.ndarray | float: ...

    def sample(self, n: int, rng: np.random.Generator) -> np.ndarray: ...


@dataclass(frozen=True)
class GaussianDistribution:
    """Multivariate Gaussian ``N(0, Sigma)`` — the calibration anchor (C_P = ||Sigma||_op)."""

    covariance: np.ndarray
    name: str = "gaussian"

    def __post_init__(self) -> None:
        cov = np.asarray(self.covariance, dtype=float)
        if cov.ndim != 2 or cov.shape[0] != cov.shape[1]:
            raise ValueError("covariance must be a square matrix")
        if np.min(np.linalg.eigvalsh(cov)) <= 0:
            raise ValueError("covariance must be positive definite")
        object.__setattr__(self, "covariance", cov)

    @property
    def dim(self) -> int:
        return int(self.covariance.shape[0])

    @property
    def precision(self) -> np.ndarray:
        return np.linalg.inv(self.covariance)

    @property
    def covariance_operator_norm(self) -> float:
        """``lambda_max(Sigma) = C_P`` (the exact Poincare constant of a Gaussian)."""
        return float(np.max(np.linalg.eigvalsh(self.covariance)))

    @property
    def hessian_lower_bound(self) -> float:
        """``lambda_min(Hess U) = lambda_min(Sigma^{-1}) = 1/lambda_max(Sigma)`` (Bakry-Emery m)."""
        return float(np.min(np.linalg.eigvalsh(self.precision)))

    def potential(self, x: np.ndarray) -> np.ndarray | float:
        x = np.asarray(x, dtype=float)
        p = self.precision
        if x.ndim == 1:
            return float(0.5 * x @ p @ x)
        return 0.5 * np.einsum("ni,ij,nj->n", x, p, x)

    def sample(self, n: int, rng: np.random.Generator) -> np.ndarray:
        return rng.multivariate_normal(mean=np.zeros(self.dim), cov=self.covariance, size=n)

    def top_eigenvector(self) -> np.ndarray:
        values, vectors = np.linalg.eigh(self.covariance)
        return vectors[:, int(np.argmax(values))]


@dataclass(frozen=True)
class DoubleWell1D:
    """Two-mode density ``exp(-(x^2-a^2)^2 / 4)`` — metastable; a tail-blind bound fails here."""

    a: float = 2.0
    name: str = "double_well_1d"

    @property
    def dim(self) -> int:
        return 1

    def potential(self, x: ArrayLike) -> np.ndarray | float:
        x_arr = np.asarray(x, dtype=float)
        u = 0.25 * (x_arr**2 - self.a**2) ** 2
        return float(u) if np.ndim(x_arr) == 0 else u

    def grad_potential(self, x: ArrayLike) -> np.ndarray | float:
        x_arr = np.asarray(x, dtype=float)
        g = x_arr * (x_arr**2 - self.a**2)
        return float(g) if np.ndim(x_arr) == 0 else g

    def sample(self, n: int, rng: np.random.Generator) -> np.ndarray:
        # Importance-resampling from a wide Gaussian; adequate for tests and examples.
        proposal_scale = max(2.0, self.a + 1.5)
        m = max(20 * n, 5000)
        y = rng.normal(0.0, proposal_scale, size=m)
        logw = -self.potential(y) + 0.5 * (y / proposal_scale) ** 2
        logw -= float(np.max(logw))
        w = np.exp(logw)
        w /= np.sum(w)
        idx = rng.choice(np.arange(m), size=n, replace=True, p=w)
        return y[idx, None]


@dataclass(frozen=True)
class PerturbedGaussian1D:
    """``exp(-x^2/(2 sigma^2) - eps cos(freq x))`` — a bounded perturbation of a Gaussian."""

    sigma: float = 1.0
    eps: float = 0.2
    freq: float = 1.0
    name: str = "perturbed_gaussian_1d"

    @property
    def dim(self) -> int:
        return 1

    def potential(self, x: ArrayLike) -> np.ndarray | float:
        x_arr = np.asarray(x, dtype=float)
        u = 0.5 * (x_arr / self.sigma) ** 2 + self.eps * np.cos(self.freq * x_arr)
        return float(u) if np.ndim(x_arr) == 0 else u

    @property
    def reference_hessian_lower_bound(self) -> float:
        """``1/sigma^2`` — the Bakry-Emery floor of the Gaussian reference ``N(0, sigma^2)``."""
        return 1.0 / (self.sigma**2)

    @property
    def perturbation_oscillation_bound(self) -> float:
        """``osc(W) <= 2|eps|`` — the Holley-Stroock bounded-perturbation budget."""
        return 2.0 * abs(self.eps)

    def sample(self, n: int, rng: np.random.Generator) -> np.ndarray:
        # Importance resampling from N(0, sigma^2).
        m = max(20 * n, 5000)
        y = rng.normal(0.0, self.sigma, size=m)
        logw = -self.eps * np.cos(self.freq * y)
        logw -= float(np.max(logw))
        w = np.exp(logw)
        w /= np.sum(w)
        idx = rng.choice(np.arange(m), size=n, replace=True, p=w)
        return y[idx, None]
