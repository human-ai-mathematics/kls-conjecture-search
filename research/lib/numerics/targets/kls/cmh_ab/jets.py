"""Truncated two-variable jet arithmetic to total order four.

A ``Jet`` carries the partial derivatives ``d^{i+j} f / dy_1^i dy_2^j`` for ``i + j <= 4`` as
numpy arrays over a quadrature grid.  Multiplication is the Leibniz rule and composition with a
scalar function uses the truncated Taylor series of that function around the value part, so
derivatives are *analytic*, not finite-differenced: no step size enters the battery anywhere.

The battery needs order four because the differentiated Monge-Ampere source
``A = H (D^2 V o grad psi) H`` requires the Hessian of ``psi + log det D^2 psi``.
"""
from __future__ import annotations

from math import comb, factorial

import numpy as np


ORDER = 4
KEYS = tuple((i, j) for i in range(ORDER + 1) for j in range(ORDER + 1 - i))


class Jet:
    __slots__ = ("c",)

    def __init__(self, coefficients: dict[tuple[int, int], np.ndarray]):
        self.c = {k: coefficients.get(k, None) for k in KEYS}
        shape = next(v.shape for v in self.c.values() if v is not None)
        zero = np.zeros(shape)
        for k in KEYS:
            if self.c[k] is None:
                self.c[k] = zero

    # -- construction -------------------------------------------------------------------
    @staticmethod
    def constant(value: np.ndarray) -> "Jet":
        return Jet({(0, 0): np.asarray(value, float)})

    @staticmethod
    def variable(values: np.ndarray, axis: int) -> "Jet":
        values = np.asarray(values, float)
        key = (1, 0) if axis == 0 else (0, 1)
        return Jet({(0, 0): values, key: np.ones_like(values)})

    @property
    def value(self) -> np.ndarray:
        return self.c[(0, 0)]

    # -- algebra ------------------------------------------------------------------------
    def __add__(self, other) -> "Jet":
        if isinstance(other, Jet):
            return Jet({k: self.c[k] + other.c[k] for k in KEYS})
        return Jet({k: (self.c[k] + other if k == (0, 0) else self.c[k]) for k in KEYS})

    __radd__ = __add__

    def __neg__(self) -> "Jet":
        return Jet({k: -self.c[k] for k in KEYS})

    def __sub__(self, other) -> "Jet":
        return self + (-other if isinstance(other, Jet) else -other)

    def __rsub__(self, other) -> "Jet":
        return (-self) + other

    def __mul__(self, other) -> "Jet":
        if not isinstance(other, Jet):
            return Jet({k: self.c[k] * other for k in KEYS})
        out: dict[tuple[int, int], np.ndarray] = {}
        for i, j in KEYS:
            acc = None
            for p in range(i + 1):
                for q in range(j + 1):
                    if p + q > ORDER or (i - p) + (j - q) > ORDER:
                        continue
                    term = comb(i, p) * comb(j, q) * self.c[(p, q)] * other.c[(i - p, j - q)]
                    acc = term if acc is None else acc + term
            out[(i, j)] = acc
        return Jet(out)

    __rmul__ = __mul__

    def compose(self, derivatives) -> "Jet":
        """``phi(self)`` given ``[phi(a), phi'(a), ..., phi''''(a)]`` at ``a = self.value``."""
        tail = Jet({k: (np.zeros_like(self.c[k]) if k == (0, 0) else self.c[k]) for k in KEYS})
        result = Jet.constant(derivatives[0])
        power = Jet({(0, 0): np.ones_like(self.value)})
        for k in range(1, ORDER + 1):
            power = power * tail
            result = result + power * (derivatives[k] / factorial(k))
        return result


# ---------------------------------------------------------------------------------------
# elementary functions
# ---------------------------------------------------------------------------------------

def jexp(jet: Jet) -> Jet:
    e = np.exp(jet.value)
    return jet.compose([e, e, e, e, e])


def jlog(jet: Jet) -> Jet:
    a = jet.value
    return jet.compose([np.log(a), 1.0 / a, -1.0 / a ** 2, 2.0 / a ** 3, -6.0 / a ** 4])


def jcosh(jet: Jet) -> Jet:
    c, s = np.cosh(jet.value), np.sinh(jet.value)
    return jet.compose([c, s, c, s, c])


def jgaussian_bump(jet: Jet, centre: float, width: float) -> Jet:
    """``exp(-(x - centre)^2 / (2 width^2))`` with exact derivatives (Hermite recursion)."""
    z = (jet.value - centre) / width
    base = np.exp(-z ** 2 / 2.0)
    he = [np.ones_like(z), z]
    for k in range(1, ORDER):
        he.append(z * he[k] - k * he[k - 1])
    derivatives = [((-1.0) ** k) * he[k] * base / width ** k for k in range(ORDER + 1)]
    return jet.compose(derivatives)


def jhermite(jet: Jet, degree: int) -> Jet:
    """Probabilists' Hermite ``He_degree`` of the jet, by the polynomial recursion."""
    one = Jet({(0, 0): np.ones_like(jet.value)})
    zero = Jet({(0, 0): np.zeros_like(jet.value)})
    previous, current = zero, one
    for k in range(degree):
        previous, current = current, jet * current - previous * float(k)
    return current
