"""Convex bases ``K`` of an exponential cone, with exact moments and Stein kernels.

A base is a Cartesian product of blocks, so ``Unif(K)`` is the product of the blocks'
uniform laws and the canonical Stein kernel ``tau_K`` is block diagonal.  Two block
types are implemented, both with rational moments of every order:

``interval``
    the centered segment ``[-1, 1]``, ``tau = (1 - u^2)/2`` (subsec:cmh-cones).
``simplex(k)``
    the uniform law on the ``k``-dimensional simplex, i.e. ``Dir(1, ..., 1)`` with
    ``A = k + 1``, in the centered free coordinates ``u_a = p_a - 1/A`` (``a = 1..k``).
    Its Stein kernel is the Wright-Fisher matrix ``C(p)/A`` of eq:cmh-dirichlet-data
    restricted to those coordinates, ``H_{ab} = (delta_{ab} p_a - p_a p_b)/A``.

Dropping the last barycentric coordinate is an invertible linear map on the simplex's
tangent space, and both the covariance and the Stein kernel are linearly equivariant
(``tau_{AK}(Au) = A tau_K(u) A^T``), so the free-coordinate representation carries the
same gate pencil as any other frame.  That is what lets this module stay rational: no
isotropic normalization, hence no square roots, is ever taken.

``E[tau_K] == Cov(U)`` is the Stein normalization, and it is checked exactly for every
base in :func:`..cmh_cone.selftest`.
"""
from __future__ import annotations

from fractions import Fraction
from math import comb

from . import polys as P


def _rising(a: Fraction, k: int) -> Fraction:
    out = Fraction(1)
    for j in range(k):
        out *= a + j
    return out


class _Interval:
    """``[-1, 1]`` with the uniform law."""

    dim = 1
    tag = "I"

    def __init__(self):
        self.arity = 1

    def moment(self, e) -> Fraction:
        (k,) = e
        return Fraction(0) if k % 2 else Fraction(1, k + 1)

    def cov(self):
        return [[Fraction(1, 3)]]

    def tau_local(self, offset: int, m: int):
        """``{(i, j): Poly}`` for this block's entries in the ambient index range."""
        b = [0] * m
        b[offset] = 2
        return {(offset, offset): {(0, tuple([0] * m)): Fraction(1, 2),
                                   (0, tuple(b)): Fraction(-1, 2)}}


class _Simplex:
    """``Delta_k`` (uniform = ``Dir(1, ..., 1)``, ``A = k + 1``) in centered free coordinates."""

    def __init__(self, k: int):
        if k < 1:
            raise ValueError("a simplex block needs k >= 1")
        self.dim = k
        self.arity = k + 1
        self.tag = f"S{k}"
        self._A = Fraction(k + 1)
        self._cache: dict = {}

    def _dirichlet(self, j) -> Fraction:
        """``E[prod_a p_a^{j_a}]`` under ``Dir(1, ..., 1)`` with ``A = k+1``."""
        num = Fraction(1)
        for ja in j:
            num *= _rising(Fraction(1), ja)
        return num / _rising(self._A, sum(j))

    def moment(self, e) -> Fraction:
        e = tuple(int(x) for x in e)
        got = self._cache.get(e)
        if got is not None:
            return got
        k = self.dim
        inv = -1 / self._A
        total = Fraction(0)
        idx = [0] * k
        while True:
            weight = Fraction(1)
            for a in range(k):
                weight *= comb(e[a], idx[a]) * inv ** (e[a] - idx[a])
            total += weight * self._dirichlet(tuple(idx))
            a = 0
            while a < k:
                idx[a] += 1
                if idx[a] <= e[a]:
                    break
                idx[a] = 0
                a += 1
            else:
                break
        self._cache[e] = total
        return total

    def cov(self):
        k, A = self.dim, self._A
        return [[(Fraction(int(a == b), 1) / A - 1 / (A * A)) / (A + 1)
                 for b in range(k)] for a in range(k)]

    def tau_local(self, offset: int, m: int):
        k, A = self.dim, self._A
        out = {}
        for a in range(k):
            for b in range(k):
                ua = P.term(0, _unit(m, offset + a))
                ub = P.term(0, _unit(m, offset + b))
                pa = P.padd(ua, P.const(1 / A, m))
                pb = P.padd(ub, P.const(1 / A, m))
                entry = P.pscale(P.padd(pa if a == b else {}, P.pmul(pa, pb), -1), 1 / A)
                out[(offset + a, offset + b)] = entry
        return out


def _unit(m: int, i: int):
    b = [0] * m
    b[i] = 1
    return tuple(b)


class ConeBase:
    """A product base ``K = Delta_{k_1} x ... x Delta_{k_r} x [-1,1]^s``."""

    def __init__(self, blocks):
        self.blocks = list(blocks)
        self.m = sum(block.dim for block in self.blocks)
        if self.m < 1:
            raise ValueError("a cone base needs at least one dimension")
        self.offsets, off = [], 0
        for block in self.blocks:
            self.offsets.append(off)
            off += block.dim
        self.name = "".join(block.tag for block in self.blocks) or "empty"
        self._mom: dict = {}

    # -- moments ---------------------------------------------------------------------
    def moment(self, b) -> Fraction:
        b = tuple(int(x) for x in b)
        got = self._mom.get(b)
        if got is not None:
            return got
        out = Fraction(1)
        for block, off in zip(self.blocks, self.offsets):
            out *= block.moment(b[off:off + block.dim])
            if out == 0:
                break
        self._mom[b] = out
        return out

    # -- second-order data -----------------------------------------------------------
    def cov(self):
        m = self.m
        out = [[Fraction(0)] * m for _ in range(m)]
        for block, off in zip(self.blocks, self.offsets):
            sub = block.cov()
            for a in range(block.dim):
                for b in range(block.dim):
                    out[off + a][off + b] = sub[a][b]
        return out

    def tau(self):
        """``tau_K(u)`` as an ``m x m`` matrix of polynomials in ``u``."""
        m = self.m
        out = [[dict() for _ in range(m)] for _ in range(m)]
        for block, off in zip(self.blocks, self.offsets):
            for (i, j), poly in block.tau_local(off, m).items():
                out[i][j] = poly
        return out

    def describe(self) -> dict:
        return {"name": self.name, "m": self.m,
                "blocks": [{"kind": "interval" if isinstance(block, _Interval) else "simplex",
                            "dim": block.dim} for block in self.blocks]}


def cube(m: int) -> ConeBase:
    """``K = [-1,1]^m``, the cube base of cor:cube-cone-gate-zero."""
    return ConeBase([_Interval() for _ in range(m)])


def simplex(k: int) -> ConeBase:
    """``K = Delta_k``; with ``beta = n = k + 1`` the cone is a product of exponentials."""
    return ConeBase([_Simplex(k)])


def product_base(simplex_dims=(), intervals: int = 0) -> ConeBase:
    return ConeBase([_Simplex(k) for k in simplex_dims]
                    + [_Interval() for _ in range(intervals)])
