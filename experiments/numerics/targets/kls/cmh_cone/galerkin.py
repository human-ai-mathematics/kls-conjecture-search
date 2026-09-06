"""CMH Galerkin quotients on exponential cones, from exactly assembled moment matrices.

The CMH Rayleigh quotient of def:cmh at a test function ``g`` is

    Q(g) = E<tau grad g, Sigma^{-1} tau grad g> / E (L_mu g)^2,
    L_mu g = Tr(tau D^2 g) - <x - beta e_1, grad g>,

and ``sup_g Q(g)`` is ``C_CMH``.  Restricting ``g`` to the span of the monomials of
``x = (x_1, x')`` of total degree ``1..d`` turns this into a generalized eigenvalue problem
``N v = lambda D v`` whose largest eigenvalue is a *lower* bound for ``C_CMH`` -- provided
the polynomial span lies in the operator core, which this module tests rather than
assumes (see ``bochner_residual``).

Both matrices are assembled in exact ``Fraction`` arithmetic.  The Stein kernel carries a
factor ``x_1^{-1}`` in its transverse block, but every such factor cancels: ``tau`` has
``s``-degree exactly ``1``, ``grad g`` has ``s``-degree at least ``0`` and ``D^2 g`` at
least ``0`` for ``g`` of ``x``-degree at least one, so ``tau grad g`` and ``L_mu g`` have
``s``-degree at least ``1`` and ``0``.  Only nonnegative Gamma moments
``E[S^k] = beta (beta+1) ... (beta+k-1)`` are ever needed, and the assembly is exact for
every integer ``beta >= n``, ``beta = n = 2`` included.

The largest generalized eigenvalue is obtained from a *floating* solver and is therefore
directional.  Its top eigenvector is rationalized and the quotient re-evaluated from the
exact matrices; only that number is an exact lower bound, and it certifies one explicit
test function, so it needs no positive-definiteness claim about ``D`` -- just
``den(g) > 0``, which the certificate carries.

Anchors: ``g = x_1`` gives exactly ``1 + n/beta`` (prop:cone-linear-sector (ii)), the
degree-1 block reproduces the gate pencil of :mod:`.gate`, and the ``beta = n`` cone over
``Delta_{n-1}`` is a product of ``n`` centered exponentials with ``C_CMH = 4`` exactly
(thm:cmh-product), which the Galerkin values must approach from below.
"""
from __future__ import annotations

import itertools
import math
from fractions import Fraction

import numpy as np
from scipy.linalg import eigh

from . import gate
from . import linalg as la
from . import polys as P


def exponential_product_galerkin_value(degree: int) -> float:
    """``2 + 2 cos(pi/(d+1))``: the exact degree-``d`` CMH Galerkin value of an exponential.

    For the centered one-sided exponential, ``tau(s) = s`` and ``L g = s g'' - (s-1) g'``
    is the Laguerre operator, ``L L_k = -k L_k`` on the orthonormal Laguerre basis, with
    ``s L_k' = k (L_k - L_{k-1})``.  Hence on ``span{L_1, ..., L_d}``

        E[(tau g')^2] = 2 sum_k k^2 v_k^2 - 2 sum_k k(k-1) v_k v_{k-1},
        E[(L g)^2]    = sum_k k^2 v_k^2,

    and the substitution ``w_k = k v_k`` turns the quotient into
    ``2 - 2 (sum w_k w_{k-1}) / (sum w_k^2)``, whose maximum is ``2 + 2 cos(pi/(d+1))``
    -- the extreme eigenvalue of the ``d x d`` tridiagonal matrix with zero diagonal and
    ``-1`` off-diagonal.  It increases to the exact value ``C_CMH = 4`` of
    thm:cmh-1d without attaining it.

    ``C_CMH`` and the total-degree polynomial spaces are both invariant under invertible
    linear maps, and thm:cmh-product makes the value of a product equal to the value of
    its factors, so the same number is the degree-``d`` anchor for every exponential
    product -- in particular for the cone over ``Delta_{n-1}`` at ``beta = n``, in every
    dimension.
    """
    return 2.0 + 2.0 * math.cos(math.pi / (degree + 1))


def monomial_basis(n: int, degree: int):
    """Monomials of ``x`` of total degree ``1..degree``, as exponent tuples of length ``n``."""
    out = []
    for total in range(1, degree + 1):
        for combo in itertools.combinations_with_replacement(range(n), total):
            exps = [0] * n
            for i in combo:
                exps[i] += 1
            out.append(tuple(exps))
    return out


def _monomial_poly(exps):
    """``x_1^{a_0} prod_j x_{j+1}^{a_j}`` in the ``(s, u)`` chart."""
    c = sum(exps)
    b = tuple(exps[1:])
    return {(c, b): Fraction(1)}


def _sym_moment_matrix(rows, mom):
    """``A_{ij} = E[rows_i * rows_j]`` for a list of polynomials, exact and symmetric."""
    index: dict = {}
    sparse = []
    for poly in rows:
        entry = []
        for key, coeff in poly.items():
            idx = index.get(key)
            if idx is None:
                idx = index[key] = len(index)
            entry.append((idx, coeff))
        sparse.append(entry)
    keys = list(index)
    nk = len(keys)
    gram = [[Fraction(0)] * nk for _ in range(nk)]
    for a in range(nk):
        ca, ba = keys[a]
        for b in range(a, nk):
            cb, bb = keys[b]
            value = mom.term((ca + cb, tuple(x + y for x, y in zip(ba, bb))))
            gram[a][b] = gram[b][a] = value
    nb = len(rows)
    out = [[Fraction(0)] * nb for _ in range(nb)]
    for i in range(nb):
        y = [Fraction(0)] * nk
        for idx, coeff in sparse[i]:
            row = gram[idx]
            for t in range(nk):
                if row[t]:
                    y[t] += coeff * row[t]
        for j in range(i, nb):
            value = sum((coeff * y[idx] for idx, coeff in sparse[j]), Fraction(0))
            out[i][j] = out[j][i] = value
    return out


def _tau_x(base, beta: int):
    """``tau`` in ``x`` coordinates: ``s * T(u)`` with ``T`` from eq:cone-stein-kernel."""
    T = gate.stein_matrix(base, beta)
    shift = P.term(1, (0,) * base.m)
    return [[P.pmul(shift, entry) for entry in row] for row in T]


def assemble(base, beta: int, degree: int, mom):
    """Exact ``(N, D)`` and the per-basis Bochner residuals for one Galerkin space."""
    m = base.m
    n = m + 1
    tau = _tau_x(base, beta)
    Sigma_inv = la.inverse(gate.gate_pencil(base, beta)[1])
    L, pivots = la.ldl(Sigma_inv)

    exps = monomial_basis(n, degree)
    grads, hessians, fluxes, generators = [], [], [], []
    for e in exps:
        g = _monomial_poly(e)
        grad = P.grad(g, m)
        hess = [P.grad(gi, m) for gi in grad]
        # tau grad g
        flux = []
        for a in range(n):
            acc: dict = {}
            for b in range(n):
                if tau[a][b] and grad[b]:
                    acc = P.padd(acc, P.pmul(tau[a][b], grad[b]))
            flux.append(acc)
        # L_mu g = Tr(tau D^2 g) - <x - beta e_1, grad g>
        gen: dict = {}
        for a in range(n):
            for b in range(n):
                if tau[a][b] and hess[a][b]:
                    gen = P.padd(gen, P.pmul(tau[a][b], hess[a][b]))
        drift = P.pmul(P.padd(P.term(1, (0,) * m), P.const(-beta, m)), grad[0])
        for j in range(m):
            unit = [0] * m
            unit[j] = 1
            drift = P.padd(drift, P.pmul(P.term(1, tuple(unit)), grad[j + 1]))
        generators.append(P.padd(gen, drift, -1))
        grads.append(grad)
        hessians.append(hess)
        fluxes.append(flux)

    nb = len(exps)
    N = [[Fraction(0)] * nb for _ in range(nb)]
    for a in range(n):
        rows = []
        for i in range(nb):
            acc: dict = {}
            for b in range(n):
                if L[b][a] and fluxes[i][b]:
                    acc = P.padd(acc, fluxes[i][b], L[b][a])
            rows.append(acc)
        block = _sym_moment_matrix(rows, mom)
        weight = pivots[a]
        for i in range(nb):
            for j in range(i, nb):
                N[i][j] = N[j][i] = N[i][j] + weight * block[i][j]
    D = _sym_moment_matrix(generators, mom)
    return {"exponents": exps, "N": N, "D": D, "tau": tau,
            "grads": grads, "hessians": hessians, "basis_size": nb}


def bochner_residual(assembled, mom, vector=None):
    """``E(L_mu g)^2 - E[<tau grad g, grad g> + Tr(tau D^2 g tau D^2 g)]`` at one ``g``.

    Zero is prop:cmh-bochner holding exactly at ``g``: the integration by parts that
    defines the Stein Dirichlet form has no boundary defect there, which is the
    admissibility question a polynomial test space raises on an unbounded cone.  A nonzero
    residual would invalidate the Galerkin value as a lower bound, so it is reported.
    """
    tau = assembled["tau"]
    n = len(tau)
    nb = assembled["basis_size"]
    if vector is None:
        vector = [Fraction(0)] * nb
    grad = [dict() for _ in range(n)]
    hess = [[dict() for _ in range(n)] for _ in range(n)]
    for i, coeff in enumerate(vector):
        if not coeff:
            continue
        for a in range(n):
            grad[a] = P.padd(grad[a], assembled["grads"][i][a], coeff)
            for b in range(n):
                hess[a][b] = P.padd(hess[a][b], assembled["hessians"][i][a][b], coeff)
    energy: dict = {}
    for a in range(n):
        for b in range(n):
            if tau[a][b] and grad[a] and grad[b]:
                energy = P.padd(energy, P.pmul(tau[a][b], P.pmul(grad[a], grad[b])))
    prod = [[dict() for _ in range(n)] for _ in range(n)]          # tau D^2 g
    for a in range(n):
        for b in range(n):
            acc: dict = {}
            for t in range(n):
                if tau[a][t] and hess[t][b]:
                    acc = P.padd(acc, P.pmul(tau[a][t], hess[t][b]))
            prod[a][b] = acc
    hs: dict = {}
    for a in range(n):
        for b in range(n):
            if prod[a][b] and prod[b][a]:
                hs = P.padd(hs, P.pmul(prod[a][b], prod[b][a]))
    rhs = mom.expect(energy) + mom.expect(hs)
    lhs = la.quadratic(assembled["D"], vector)
    return lhs - rhs


def top_eigenpair(N, D):
    """Floating ``lambda_max`` of the pencil ``(N, D)`` and its top vector (directional)."""
    Nf = np.array(la.to_float(N))
    Df = np.array(la.to_float(D))
    scale = 1.0 / np.sqrt(np.diag(Df))
    Nf = Nf * scale[:, None] * scale[None, :]
    Df = Df * scale[:, None] * scale[None, :]
    vals, vecs = eigh(0.5 * (Nf + Nf.T), 0.5 * (Df + Df.T))
    return vals, scale * vecs[:, -1], float(np.linalg.cond(Df))
