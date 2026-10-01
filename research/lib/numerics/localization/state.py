"""Product posterior state under Eldan stochastic localization.

For a product base measure ``mu = ⊗_i mu^(i)`` the localized posterior ``mu_t``
stays a product (``prop:products`` in ``modules/30-model-geometries.md``): the
tilt ``exp(c_t·x − t|x|²/2)`` factorizes, ``A_t`` is diagonal with entries
``A_t^(i) = Var(mu_t^(i))``, and the barycenter is ``a_t^(i) = mean(mu_t^(i))``.

This module holds the per-coordinate tilt vector ``c`` and time ``t`` and reads
off the marginals by exact quadrature (`tilt1d`). It does **not** integrate the
matrix Riccati: ``A_t`` is a read-off, not an integration variable, so there is
no stiff covariance ODE.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from .tilt1d import Base1D, Tilted1D, tilted


@dataclass
class ProductState:
    """Localization state of a product measure: tilt ``c`` at time ``t``.

    Parameters
    ----------
    base : Base1D
        The (shared) 1D base measure for every coordinate.
    c : np.ndarray
        Per-coordinate tilt vector ``c_{t,i}`` (shape ``(n,)``, float64).
    t : float
        Localization time.
    quad : dict
        Keyword args forwarded to ``tilt1d.tilted`` (order, half_width, passes).
    """

    base: Base1D
    c: np.ndarray
    t: float
    quad: dict = field(default_factory=dict)
    _marginals: list[Tilted1D] | None = field(default=None, repr=False, compare=False)

    def __post_init__(self) -> None:
        self.c = np.ascontiguousarray(self.c, dtype=np.float64)
        if self.c.ndim != 1:
            raise ValueError("c must be a 1D array")
        self.t = float(self.t)

    @classmethod
    def isotropic(cls, base: Base1D, n: int, **quad) -> "ProductState":
        """Initial state ``t=0``, ``c=0`` (the untilted isotropic product)."""
        return cls(base=base, c=np.zeros(n, dtype=np.float64), t=0.0, quad=quad)

    @property
    def n(self) -> int:
        return self.c.shape[0]

    def marginals(self) -> list[Tilted1D]:
        """Per-coordinate tilted marginals (cached for the current ``c, t``)."""
        if self._marginals is None:
            self._marginals = [
                tilted(self.base, float(ci), self.t, **self.quad) for ci in self.c
            ]
        return self._marginals

    def mean(self) -> np.ndarray:
        """Barycenter ``a_t`` (shape ``(n,)``)."""
        return np.array([m.mean for m in self.marginals()], dtype=np.float64)

    def A_diag(self) -> np.ndarray:
        """Diagonal of the covariance ``A_t`` (the per-coordinate variances)."""
        return np.array([m.var for m in self.marginals()], dtype=np.float64)

    def lambda_max(self) -> float:
        return float(np.max(self.A_diag()))

    def excess_op_norm(self) -> float:
        """``X_t = (lambda_max(A_t) − 1)_+`` (the covariance-inflation excess)."""
        return max(self.lambda_max() - 1.0, 0.0)

    def check_bl_cap(self, tol: float = 1e-6) -> None:
        """Assert the pathwise Brascamp-Lieb cap ``A_t ⪯ (1/t) I`` (eq:BL-cap).

        Vacuous at ``t = 0``. A violation signals a quadrature/integrator bug
        (typically an under-resolved sharp posterior biasing the variance).
        """
        if self.t <= 0.0:
            return
        cap = 1.0 / self.t
        lam = self.lambda_max()
        if lam > cap * (1.0 + tol) + tol:
            raise AssertionError(
                f"BL cap violated at t={self.t:.6g}: lambda_max={lam:.6g} > 1/t={cap:.6g}"
            )

    def advanced(self, c_new: np.ndarray, t_new: float) -> "ProductState":
        """A fresh state at new tilt/time (invalidates the marginal cache)."""
        return ProductState(base=self.base, c=c_new, t=t_new, quad=self.quad)
