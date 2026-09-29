"""Exact term algebra for exponential cone measures (def:exponential-cone).

A *term* is the pair ``(c, b)`` standing for the monomial ``s^c * prod_j u_j^{b_j}``,
where ``s = x_1`` is the radial coordinate and ``u = x'/x_1`` the base coordinate of
``X = S (1, U)``, ``S ~ Gamma(beta, 1)`` and ``U ~ Unif(K)`` independent.  A *polynomial*
is a ``dict`` from terms to :class:`fractions.Fraction` coefficients.

Independence factorizes every moment exactly,
``E[s^c u^b] = E[s^c] * E_K[u^b]``, with ``E[s^c] = beta (beta+1) ... (beta+c-1)`` for
``c >= 0`` and ``E[s^{-k}] = 1/((beta-1) ... (beta-k))`` for ``0 < k < beta``.  Nothing
here samples anything: every coefficient and every moment is a ``Fraction``.

The two Cartesian derivations are expressed in the same basis.  On ``s^c u^b``,

    d/dx_1 = d/ds - sum_j (u_j/s) d/du_j   gives   (c - |b|) s^{c-1} u^b,
    d/dx_j = (1/s) d/du_j                  gives   b_j s^{c-1} u^{b - e_j},

which is why a polynomial in ``x`` never leaves this algebra and why the negative powers
of ``s`` carried by the Stein kernel cancel against the derivatives (see the module
docstring of :mod:`..cmh_cone`).
"""
from __future__ import annotations

from fractions import Fraction

Term = tuple  # (c: int, b: tuple[int, ...])
Poly = dict   # {Term: Fraction}


def zero() -> Poly:
    return {}


def const(value, m: int) -> Poly:
    value = Fraction(value)
    return {} if value == 0 else {(0, (0,) * m): value}


def term(c: int, b, coeff=1) -> Poly:
    coeff = Fraction(coeff)
    return {} if coeff == 0 else {(int(c), tuple(int(x) for x in b)): coeff}


def padd(f: Poly, g: Poly, scale=1) -> Poly:
    scale = Fraction(scale)
    out = dict(f)
    for k, v in g.items():
        w = out.get(k, Fraction(0)) + scale * v
        if w:
            out[k] = w
        else:
            out.pop(k, None)
    return out


def pscale(f: Poly, scale) -> Poly:
    scale = Fraction(scale)
    if scale == 0:
        return {}
    return {k: scale * v for k, v in f.items()}


def pmul(f: Poly, g: Poly) -> Poly:
    out: Poly = {}
    for (c1, b1), v1 in f.items():
        for (c2, b2), v2 in g.items():
            k = (c1 + c2, tuple(x + y for x, y in zip(b1, b2)))
            w = out.get(k, Fraction(0)) + v1 * v2
            if w:
                out[k] = w
            else:
                out.pop(k, None)
    return out


def dx1(f: Poly) -> Poly:
    """``d/dx_1`` in the ``(s, u)`` chart."""
    out: Poly = {}
    for (c, b), v in f.items():
        coeff = v * (c - sum(b))
        if coeff:
            k = (c - 1, b)
            w = out.get(k, Fraction(0)) + coeff
            if w:
                out[k] = w
            else:
                out.pop(k, None)
    return out


def dxj(f: Poly, j: int) -> Poly:
    """``d/dx_{j+1}`` (``j`` is the zero-based index into the base coordinates)."""
    out: Poly = {}
    for (c, b), v in f.items():
        if not b[j]:
            continue
        coeff = v * b[j]
        nb = list(b)
        nb[j] -= 1
        k = (c - 1, tuple(nb))
        w = out.get(k, Fraction(0)) + coeff
        if w:
            out[k] = w
        else:
            out.pop(k, None)
    return out


def grad(f: Poly, m: int) -> list[Poly]:
    """``[d/dx_1, d/dx_2, ..., d/dx_n]`` as polynomials, ``n = m + 1``."""
    return [dx1(f)] + [dxj(f, j) for j in range(m)]


def hessian(f: Poly, m: int) -> list[list[Poly]]:
    g = grad(f, m)
    return [grad(gi, m) for gi in g]


def gamma_moment(beta: int, c: int) -> Fraction:
    """``E[S^c]`` for ``S ~ Gamma(beta, 1)``, exact; raises when the moment diverges."""
    beta = Fraction(beta)
    out = Fraction(1)
    if c >= 0:
        for i in range(c):
            out *= beta + i
        return out
    for i in range(1, -c + 1):
        d = beta - i
        if d <= 0:
            raise ValueError(f"E[S^{c}] diverges for beta={beta}")
        out /= d
    return out


class ConeMoments:
    """``E[s^c u^b]`` for one ``(base, beta)`` pair, memoized and exact."""

    def __init__(self, base, beta: int):
        self.base = base
        self.beta = int(beta)
        self._cache: dict = {}

    def term(self, key) -> Fraction:
        v = self._cache.get(key)
        if v is None:
            c, b = key
            ub = self.base.moment(b)
            v = Fraction(0) if ub == 0 else ub * gamma_moment(self.beta, c)
            self._cache[key] = v
        return v

    def expect(self, f: Poly) -> Fraction:
        return sum((coeff * self.term(k) for k, coeff in f.items()), Fraction(0))
