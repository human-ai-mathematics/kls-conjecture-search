"""Exact sparse-polynomial chord/moment machinery for the conditional-fiber-frame pencil.

Everything in this module is exact `fractions.Fraction` arithmetic.  The object computed is,
for the isotropic uniform simplex (`P ~ Dir(1,...,1)` on `Delta_{m-1}`), the matrix of the
normalized single-direction conditional-fiber form

    q_theta[f] = E_p[ Var(f | chord through p in direction theta) / Var(T | same chord) ]

on monomial test polynomials.  The chord conditional law of the uniform simplex is UNIFORM on
the chord segment, so with any affine chord parameter `w in [0, h]` (the ratio is
parametrization invariant),

    q_theta contribution = E_p[ 12 * Cov_w(f, g) / h^2 ],

and for chord polynomials `f = sum_n c_{a,n}(p) w^n` this is the exact finite sum

    sum_{n1>=1, n2>=1} 12 * kappa(n1,n2) * E_p[ c_{a,n1} c_{b,n2} h^{n1+n2-2} ],
    kappa(n1,n2) = 1/(n1+n2+1) - 1/((n1+1)(n2+1)),

with NO polynomial division (n1+n2-2 >= 0).  The outer expectation `E_p` reduces to exact
Dirichlet/simplex monomial moments on a chamber-adapted coordinate system:

* root direction (e_1 - e_2)/sqrt(2): the chord is `p_1' = w in [0, s]`, `p_2' = s - w`,
  `s = p_1 + p_2` conserved; `(s, p_3, ..., p_m) ~ Dir(2, 1, ..., 1)` by aggregation, no
  chamber split is needed;
* vertex direction `e_1 - (1/m) 1`: along the chord all `p_l`, `l >= 2`, shift together, so
  the argmin over `l >= 2` is chord-constant and the simplex splits into m-1 polyhedral
  chambers.  On the chamber `argmin = 2` the unimodular coordinates
  `q_1 = p_1, q_2 = p_2, q_l = p_l - p_2 (l >= 3)` map it onto the weighted simplex
  `q_1 + (m-1) q_2 + sum_{l>=3} q_l = 1`, where monomial integrals are exact factorials.

Chambers/directions related by a permutation of coordinates are recovered by relabeling
exponents (the uniform Dirichlet is exchangeable); `frames.py` owns that bookkeeping.
"""
from __future__ import annotations

import math
from fractions import Fraction

Poly = dict  # exponent tuple (length m) -> Fraction coefficient


def pzero() -> Poly:
    return {}


def padd(f: Poly, g: Poly, scale: Fraction = Fraction(1)) -> Poly:
    """Return f + scale * g (does not mutate inputs)."""
    out = dict(f)
    for e, c in g.items():
        v = out.get(e, Fraction(0)) + scale * c
        if v:
            out[e] = v
        elif e in out:
            del out[e]
    return out


def pmul(f: Poly, g: Poly) -> Poly:
    out: Poly = {}
    for ef, cf in f.items():
        for eg, cg in g.items():
            e = tuple(x + y for x, y in zip(ef, eg))
            v = out.get(e, Fraction(0)) + cf * cg
            if v:
                out[e] = v
            elif e in out:
                del out[e]
    return out


def pscale(f: Poly, c: Fraction) -> Poly:
    if c == 0:
        return {}
    return {e: c * v for e, v in f.items()}


def punit(m: int, i: int) -> Poly:
    e = [0] * m
    e[i] = 1
    return {tuple(e): Fraction(1)}


def pconst(m: int, c: Fraction) -> Poly:
    return {(0,) * m: Fraction(c)} if c else {}


def ppowers(f: Poly, m: int, nmax: int) -> list[Poly]:
    """[f^0, f^1, ..., f^nmax]."""
    out = [pconst(m, Fraction(1))]
    for _ in range(nmax):
        out.append(pmul(out[-1], f))
    return out


# -------------------------------------------------------------------------------------
# moment functionals
# -------------------------------------------------------------------------------------

def uniform_dirichlet_moment(c: tuple[int, ...]) -> Fraction:
    """E[prod p_l^{c_l}] for P ~ Dir(1,...,1) on Delta_{m-1}: (m-1)! prod c! / (m-1+|c|)!."""
    m = len(c)
    num = math.factorial(m - 1)
    for x in c:
        num *= math.factorial(x)
    return Fraction(num, math.factorial(m - 1 + sum(c)))


def make_L_root(m: int):
    """Moment functional for root-chord variables (s, unused, p_3, ..., p_m).

    (s, p_3, ..., p_m) ~ Dir(2, 1, ..., 1) with A = m, so
    L(c) = (2)_{c0} prod (1)_{c_l} / (m)_{|c|} = (c0+1)! (m-1)! prod c_l! / (m-1+|c|)!.
    Index 1 of the exponent tuple is unused and must stay 0.
    """
    cache: dict[tuple[int, ...], Fraction] = {}

    def L(c: tuple[int, ...]) -> Fraction:
        v = cache.get(c)
        if v is None:
            if c[1] != 0:
                raise ValueError("root moment functional: exponent slot 1 must be unused")
            num = math.factorial(c[0] + 1) * math.factorial(m - 1)
            for x in c[2:]:
                num *= math.factorial(x)
            v = Fraction(num, math.factorial(m - 1 + sum(c)))
            cache[c] = v
        return v

    return L


def make_L_vertex(m: int):
    """Chamber moment functional for direction e_1 - 1/m, chamber `argmin_{l>=2} p_l = 2`.

    Coordinates q_1 = p_1, q_2 = p_2, q_l = p_l - p_2 (l>=3) map the chamber unimodularly to
    {q >= 0 : q_1 + (m-1) q_2 + sum_{l>=3} q_l = 1}; with r_2 = (m-1) q_2,

    L(c) = E[ 1_chamber * q^c ] = (m-1)! prod c_l! / ( (m-1)^{c_2+1} (m-1+|c|)! ).

    Sanity: L(0) = 1/(m-1) = P(chamber).
    """
    cache: dict[tuple[int, ...], Fraction] = {}

    def L(c: tuple[int, ...]) -> Fraction:
        v = cache.get(c)
        if v is None:
            num = math.factorial(m - 1)
            for x in c:
                num *= math.factorial(x)
            v = Fraction(num, (m - 1) ** (c[1] + 1) * math.factorial(m - 1 + sum(c)))
            cache[c] = v
        return v

    return L


def apply_L(poly: Poly, L) -> Fraction:
    return sum((c * L(e) for e, c in poly.items()), Fraction(0))


# -------------------------------------------------------------------------------------
# chord coefficient expansions
# -------------------------------------------------------------------------------------

def root_chord_coeffs(m: int, a: tuple[int, ...]) -> dict[int, Poly]:
    """w-coefficients of p'^a on the (1,2) root chord: p_1' = w, p_2' = s - w, rest fixed.

    Output polynomials live in the root moment variables (s, unused, p_3, ..., p_m).
    """
    base = [0] * m
    for l in range(2, m):
        base[l] = a[l]
    out: dict[int, Poly] = {}
    for t in range(a[1] + 1):
        e = list(base)
        e[0] = a[1] - t
        coeff = Fraction(math.comb(a[1], t) * ((-1) ** t))
        n = a[0] + t
        out[n] = padd(out.get(n, {}), {tuple(e): coeff})
    return {n: p for n, p in out.items() if p}


def vertex_hpoly(m: int) -> Poly:
    """Chord length h = p_1 + (m-1) p_2 = q_1 + (m-1) q_2 on the chamber."""
    return padd(punit(m, 0), punit(m, 1), Fraction(m - 1))


def vertex_chord_coeffs(m: int, a: tuple[int, ...]) -> dict[int, Poly]:
    """w-coefficients of p'^a on the vertex chord (direction 1, chamber argmin = 2).

    Chord: p_1' = w in [0, h]; p_l' = g_l + (h - w)/(m-1) for l >= 2, with g_2 = 0 and
    g_l = q_l (l >= 3).  Expand prod_{l>=2}(g_l + y)^{a_l} in y = (h-w)/(m-1), then expand
    each y^s in (h, w) binomially.
    """
    zero = (0,) * m
    # sy[s] = coefficient polynomial of y^s (in the q variables)
    sy: dict[int, Poly] = {0: {zero: Fraction(1)}}
    for l in range(1, m):                      # python index l <-> coordinate l+1
        g = None if l == 1 else punit(m, l)    # coordinate 2 has g = 0
        for _ in range(a[l]):
            new: dict[int, Poly] = {}
            for s, pol in sy.items():
                new[s + 1] = padd(new.get(s + 1, {}), pol)
                if g is not None:
                    new[s] = padd(new.get(s, {}), pmul(pol, g))
            sy = {s: p for s, p in new.items() if p}
    smax = max(sy) if sy else 0
    hp = ppowers(vertex_hpoly(m), m, smax)
    out: dict[int, Poly] = {}
    for s, pol in sy.items():
        for t in range(s + 1):
            coeff = Fraction(math.comb(s, t) * ((-1) ** t), (m - 1) ** s)
            n = a[0] + t
            out[n] = padd(out.get(n, {}), pmul(pol, hp[s - t]), coeff)
    return {n: p for n, p in out.items() if p}


# -------------------------------------------------------------------------------------
# single-direction form matrix
# -------------------------------------------------------------------------------------

def _kappa(n1: int, n2: int) -> Fraction:
    """12 * Cov(w^{n1}, w^{n2}) / h^{n1+n2} on w ~ Unif[0, h]."""
    return 12 * (Fraction(1, n1 + n2 + 1) - Fraction(1, (n1 + 1) * (n2 + 1)))


def direction_form_matrix(mons, coeffs_fn, hpoly: Poly, L, m: int, k: int,
                          speed_sq: Fraction = Fraction(1)):
    """Matrix of the normalized single-direction fiber form on the monomial list `mons`.

    Entry (a,b) = E[ Cov_chord(p^a, p^b) / Var(T | chord) ] with T the ISOTROPIC line
    coordinate <X, theta>.  With the affine chord parameter `w in [0, h]` one has
    Var(T | chord) = speed_sq * h^2 / 12 where `speed_sq = (dT/dw)^2` is an exact rational
    supplied by the caller:

    * root chord (p_1' = w, p_2' = s - w): T = R_m (2w - s)/sqrt(2), speed_sq = 2 m (m+1);
    * vertex chord (p_1' = w): T = R_m (w - 1/m) sqrt(m/(m-1)), speed_sq = m^2 (m+1)/(m-1).

    The expectation is taken through the exact moment functional L (which may carry a
    chamber indicator).
    """
    hp = ppowers(hpoly, m, max(2 * k - 2, 0))
    inv_speed = Fraction(1) / Fraction(speed_sq)
    coeffs = [coeffs_fn(m, a) for a in mons]
    n = len(mons)
    B = [[Fraction(0)] * n for _ in range(n)]
    for x in range(n):
        ca = coeffs[x]
        for y in range(x, n):
            cb = coeffs[y]
            tot = Fraction(0)
            for n1, p1 in ca.items():
                if n1 == 0:
                    continue
                for n2, p2 in cb.items():
                    if n2 == 0:
                        continue
                    kap = _kappa(n1, n2)
                    if kap == 0:
                        continue
                    tot += kap * apply_L(pmul(pmul(p1, p2), hp[n1 + n2 - 2]), L)
            tot *= inv_speed
            B[x][y] = tot
            B[y][x] = tot
    return B
