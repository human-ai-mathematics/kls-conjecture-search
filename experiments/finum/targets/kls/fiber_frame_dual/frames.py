"""Exact pencil assembly (G, K_root, K_vertex, mixtures) on the degree-<=k quotient V_{m,k}.

Basis: monomials p^a in the FIRST m-1 coordinates, 1 <= |a| <= k (exponent tuples of length m
with last slot 0).  These are a rational basis of
V_{m,k} = R[p]_{<=k} / ((sum p - 1) R[p]_{<=k-1} + R 1), and the variance Gram G on that basis
is positive definite.

* G: exact Dir(1,...,1) covariance of monomials (probe w1f01 eq. 30).
* K_root: the A_{m-1} root frame, closed Dirichlet-neutrality form (probe eqs. 28-29, 31),
  K_root = (2/m) sum_{i<j} B^{ij}.
* K_vertex: the vertex frame theta_i ~ e_i - (1/m) 1 (X-images of simplex vertices; an
  admissible tight frame since sum_i theta_i theta_i^T ~ I on 1^perp).  The direction-1 /
  chamber-2 single-chamber matrix is computed once by exact chamber integration on the FULL
  m-variable monomial list, and all other (direction, chamber) pairs are recovered by
  exchangeability: B^{(i),C_j}_{a,b} = B^{(1),C_2}_{tau a, tau b} for any coordinate
  relabeling tau with tau(i)=1, tau(j)=2 (the (1,2) computation is invariant under
  permutations of coordinates 3..m).  Then K_vertex = ((m-1)/m) sum_{i != j} B^{(i),C_j}.
* Mixtures: the frame constraint is linear, so alpha*rho_root + (1-alpha)*rho_vertex is
  admissible for every alpha in [0,1] and K_alpha = alpha K_root + (1-alpha) K_vertex.
"""
from __future__ import annotations

import itertools
import math
from fractions import Fraction

from .exactpoly import (
    direction_form_matrix,
    make_L_root,
    make_L_vertex,
    punit,
    root_chord_coeffs,
    uniform_dirichlet_moment,
    vertex_chord_coeffs,
    vertex_hpoly,
)


def monomial_basis(m: int, k: int, nvars: int | None = None) -> list[tuple[int, ...]]:
    """Exponent tuples of length m over the first `nvars` coordinates, degree 1..k.

    Default nvars = m-1 (the quotient basis); nvars = m gives the full spanning monomial list
    used by the vertex chamber computation.
    """
    if nvars is None:
        nvars = m - 1
    out = []
    for deg in range(1, k + 1):
        for comb in itertools.combinations_with_replacement(range(nvars), deg):
            e = [0] * m
            for v in comb:
                e[v] += 1
            out.append(tuple(e))
    return out


def gram_matrix(m: int, basis) -> list[list[Fraction]]:
    """Exact covariance Gram G_{a,b} = E[p^{a+b}] - E[p^a] E[p^b] under Dir(1,...,1)."""
    means = [uniform_dirichlet_moment(a) for a in basis]
    n = len(basis)
    G = [[Fraction(0)] * n for _ in range(n)]
    for x in range(n):
        a = basis[x]
        for y in range(x, n):
            b = basis[y]
            v = uniform_dirichlet_moment(tuple(u + w for u, w in zip(a, b)))
            v -= means[x] * means[y]
            G[x][y] = v
            G[y][x] = v
    return G


# -------------------------------------------------------------------------------------
# root frame, closed form
# -------------------------------------------------------------------------------------

def beta_moment(r: int, s: int) -> Fraction:
    """beta(r,s) = int_0^1 u^r (1-u)^s du = r! s! / (r+s+1)!."""
    return Fraction(math.factorial(r) * math.factorial(s), math.factorial(r + s + 1))


def root_pair_entry(m: int, a, b, i: int, j: int) -> Fraction:
    """B^{ij}_{a,b}: normalized fiber covariance of p^a, p^b for direction (e_i-e_j)/sqrt2."""
    ra = a[i] + a[j]
    rb = b[i] + b[j]
    if ra == 0 or rb == 0:
        return Fraction(0)
    c = beta_moment(a[i] + b[i], a[j] + b[j]) - beta_moment(a[i], a[j]) * beta_moment(b[i], b[j])
    if c == 0:
        return Fraction(0)
    prod = math.factorial(m - 1) * math.factorial(ra + rb - 1)
    for l in range(m):
        if l != i and l != j:
            prod *= math.factorial(a[l] + b[l])
    return Fraction(6, m * (m + 1)) * c * Fraction(prod, math.factorial(m + sum(a) + sum(b) - 3))


def root_K(m: int, basis) -> list[list[Fraction]]:
    """K_root = (2/m) sum_{i<j} B^{ij} in exact rational arithmetic."""
    n = len(basis)
    supports = [tuple(l for l in range(m) if a[l]) for a in basis]
    K = [[Fraction(0)] * n for _ in range(n)]
    pref = Fraction(2, m)
    for x in range(n):
        a = basis[x]
        for y in range(x, n):
            b = basis[y]
            union = set(supports[x]) | set(supports[y])
            pairs = set()
            for i in union:
                for j in range(m):
                    if j != i:
                        pairs.add((min(i, j), max(i, j)))
            tot = Fraction(0)
            for (i, j) in pairs:
                tot += root_pair_entry(m, a, b, i, j)
            v = pref * tot
            K[x][y] = v
            K[y][x] = v
    return K


def root_single_direction_matrix(m: int, k: int, mons) -> list[list[Fraction]]:
    """B^{(1,2)} via the generic chord machinery (independent cross-check of eq. 29).

    Chord parameter w = p_1' in [0, s]; isotropic coordinate T = R_m (2w - s)/sqrt(2), so
    (dT/dw)^2 = 2 R_m^2 = 2 m (m+1).
    """
    return direction_form_matrix(mons, root_chord_coeffs, punit(m, 0), make_L_root(m), m, k,
                                 speed_sq=Fraction(2 * m * (m + 1)))


def root_single_direction_closed(m: int, mons) -> list[list[Fraction]]:
    """B^{(1,2)} via the closed Dirichlet-neutrality formula."""
    n = len(mons)
    B = [[Fraction(0)] * n for _ in range(n)]
    for x in range(n):
        for y in range(x, n):
            v = root_pair_entry(m, mons[x], mons[y], 0, 1)
            B[x][y] = v
            B[y][x] = v
    return B


# -------------------------------------------------------------------------------------
# vertex frame, chamber machinery + exchangeability
# -------------------------------------------------------------------------------------

def vertex_chamber_matrix(m: int, k: int, full_mons) -> list[list[Fraction]]:
    """B^{(1),C_2} on the full m-variable monomial list.

    Chord parameter w = p_1'; isotropic coordinate T = R_m (w - 1/m) sqrt(m/(m-1)), so
    (dT/dw)^2 = R_m^2 m/(m-1) = m^2 (m+1)/(m-1).
    """
    return direction_form_matrix(full_mons, vertex_chord_coeffs, vertex_hpoly(m),
                                 make_L_vertex(m), m, k,
                                 speed_sq=Fraction(m * m * (m + 1), m - 1))


def _relabel_positions(m: int):
    """For every ordered pair (i, j), the position map old -> new with i->0, j->1."""
    maps = []
    for i in range(m):
        for j in range(m):
            if j == i:
                continue
            rest = [l for l in range(m) if l != i and l != j]
            pos = [0] * m
            pos[i] = 0
            pos[j] = 1
            for newpos, old in enumerate(rest, start=2):
                pos[old] = newpos
            maps.append(pos)
    return maps


def vertex_K(m: int, k: int, basis) -> list[list[Fraction]]:
    """K_vertex = ((m-1)/m) sum_{i != j} B^{(i),C_j}, exact."""
    full = monomial_basis(m, k, nvars=m)
    Q = vertex_chamber_matrix(m, k, full)
    index = {mon: t for t, mon in enumerate(full)}
    maps = _relabel_positions(m)

    def permuted_indices(a):
        out = []
        for pos in maps:
            e = [0] * m
            for old in range(m):
                if a[old]:
                    e[pos[old]] = a[old]
            out.append(index[tuple(e)])
        return out

    perm_idx = [permuted_indices(a) for a in basis]
    n = len(basis)
    pref = Fraction(m - 1, m)
    K = [[Fraction(0)] * n for _ in range(n)]
    for x in range(n):
        px = perm_idx[x]
        for y in range(x, n):
            py = perm_idx[y]
            tot = Fraction(0)
            for t in range(len(maps)):
                tot += Q[px[t]][py[t]]
            v = pref * tot
            K[x][y] = v
            K[y][x] = v
    return K


def mixture_K(K_root_ex, K_vertex_ex, alpha: Fraction) -> list[list[Fraction]]:
    n = len(K_root_ex)
    return [[alpha * K_root_ex[i][j] + (1 - alpha) * K_vertex_ex[i][j] for j in range(n)]
            for i in range(n)]


# -------------------------------------------------------------------------------------
# reference vectors and exact anchors
# -------------------------------------------------------------------------------------

def radial_quadratic_vector(m: int, basis) -> list[Fraction]:
    """Coordinates of sum_{i=1}^m p_i^2 (mod constants) in the quotient basis.

    Eliminating p_m: sum p_i^2 = 2 sum_{i<m} p_i^2 + 2 sum_{i<j<m} p_i p_j - 2 sum_{i<m} p_i
    + const.  Proportional (after centering/scaling) to F = |X|^2 - d, so its exact
    root-frame quotient is (m+2)(m+3)/(5 m^2) (probe eq. 36).
    """
    coeff = {}
    for i in range(m - 1):
        e = [0] * m
        e[i] = 1
        coeff[tuple(e)] = Fraction(-2)
        e2 = [0] * m
        e2[i] = 2
        coeff[tuple(e2)] = Fraction(2)
        for j in range(i + 1, m - 1):
            e3 = [0] * m
            e3[i] = 1
            e3[j] = 1
            coeff[tuple(e3)] = Fraction(2)
    return [coeff.get(a, Fraction(0)) for a in basis]


def radial_root_anchor_exact(m: int) -> Fraction:
    return Fraction((m + 2) * (m + 3), 5 * m * m)


def linear_block_equals_gram(K_ex, G_ex, m: int) -> bool:
    """Exact anchor: every admissible frame has quotient one on linear tests, i.e. the
    linear-linear block of K equals that of G exactly (basis is ordered degree-1 first)."""
    nlin = m - 1
    for x in range(nlin):
        for y in range(nlin):
            if K_ex[x][y] != G_ex[x][y]:
                return False
    return True
