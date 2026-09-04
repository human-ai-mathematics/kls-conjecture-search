"""Channel 1(b): exact rational ``N``, ``D``, ``R`` for the log-concave Dirichlet moment maps.

`solutions/thm-cmh-dirichlet.tex` certifies that ``varphi(y) = A log sum_i e^{y_i/A} - q.y`` is a
genuine moment potential: ``grad varphi = p - q``, ``D^2 varphi = C(p)/A`` with
``C(p) = diag(p) - p p^T``, and ``(grad varphi)_# e^{-varphi}`` is the centred law of ``P - q``
for ``P ~ Dir(alpha)``.  So ``H = C(p)/A`` here is the *canonical moment-map Hessian*, not merely
some Stein kernel: the anisotropic-bootstrap matrices of the probe are defined on it.

``varphi`` is invariant along ``1``, so the moment map is nondegenerate only after quotienting.
The chart used throughout is the linear one ``u = (p_1, ..., p_{m-1})``, i.e. the section
``y_m = 0`` of the quotient.  In that chart

    H(u)      = ( diag(pbar) - pbar pbar^T ) / A,      pbar = (p_1, ..., p_{n}),  n = m-1,
    A d_e H   = e_e u_e^T + u_e e_e^T,                 u_e = e_e/2 - pbar,
    Sigma     = ( diag(alpha)_[n] - alpha_[n] alpha_[n]^T / A ) / (A(A+1)),
    Sigma^-1  = A(A+1) ( diag(1/alpha_i)_[n] + 1_n 1_n^T / alpha_m ).

The whitened bootstrap matrices are ``N_w = Sigma^{-1/2} N Sigma^{-1/2}`` and likewise for ``D``,
where the *chart* matrices

    N = E[ H Sigma^{-1} H ],
    D = E[ sum_{e,f} H_{ef} (d_e H) Sigma^{-1} (d_f H) ]

are exact rationals of Dirichlet moments of degree at most four.  Because both whitenings are the
same congruence, every Loewner question about ``N_w``, ``D_w`` and ``R_w = N_w - D_w`` is an exact
rational question about the chart matrices:

    R_w >= N_w / 2            <=>   N/2 - D >= 0,
    N_w - I <= D_w            <=>   D - N + Sigma >= 0,
    lambda_min(R_w + b I, N_w) = lambda_min(N - D + b Sigma, N),
    lambda_max(N_w)           = lambda_max(N, Sigma)   ( = the certified gate-zero ratio ).

No floating eigensolver is needed for the two Loewner verdicts, and none is trusted for them.
"""
from __future__ import annotations

from fractions import Fraction

from . import exact_forms as ex


# ---------------------------------------------------------------------------------------
# exact polynomials in (p_1, ..., p_n)
# ---------------------------------------------------------------------------------------

def _pmul(f, g):
    out: dict[tuple[int, ...], Fraction] = {}
    for ef, cf in f.items():
        for eg, cg in g.items():
            key = tuple(a + b for a, b in zip(ef, eg))
            out[key] = out.get(key, Fraction(0)) + cf * cg
    return {k: v for k, v in out.items() if v}


def _padd(f, g, scale: Fraction = Fraction(1)):
    out = dict(f)
    for e, c in g.items():
        out[e] = out.get(e, Fraction(0)) + scale * c
    return {k: v for k, v in out.items() if v}


def _pconst(n: int, value: Fraction):
    return {tuple([0] * n): value} if value else {}


def _pvar(n: int, i: int):
    e = [0] * n
    e[i] = 1
    return {tuple(e): Fraction(1)}


class DirichletMoments:
    """``E[prod_i P_i^{k_i}] = prod_i (alpha_i)_{k_i} / (A)_{sum k_i}``, exact and memoized."""

    def __init__(self, alpha):
        self.alpha = tuple(Fraction(a) for a in alpha)
        self.total = sum(self.alpha)
        self._cache: dict[tuple[int, ...], Fraction] = {}

    @staticmethod
    def _rising(a: Fraction, k: int) -> Fraction:
        out = Fraction(1)
        for j in range(k):
            out *= a + j
        return out

    def __call__(self, key) -> Fraction:
        key = tuple(int(x) for x in key)
        value = self._cache.get(key)
        if value is None:
            numerator = Fraction(1)
            for a, k in zip(self.alpha, key):
                if k:
                    numerator *= self._rising(a, k)
            value = numerator / self._rising(self.total, sum(key))
            self._cache[key] = value
        return value

    def expect(self, poly) -> Fraction:
        return sum((c * self(e) for e, c in poly.items()), Fraction(0))


# ---------------------------------------------------------------------------------------
# the chart data
# ---------------------------------------------------------------------------------------

def chart_covariance(alpha):
    """``Sigma`` and ``Sigma^{-1}`` in the chart ``u = (p_1, ..., p_{m-1})``, exact."""
    al = [Fraction(a) for a in alpha]
    total = sum(al)
    n = len(al) - 1
    sigma = [[(al[i] if i == j else Fraction(0)) - al[i] * al[j] / total for j in range(n)]
             for i in range(n)]
    sigma = [[x / (total * (total + 1)) for x in row] for row in sigma]
    inverse = [[(Fraction(1) / al[i] if i == j else Fraction(0)) + Fraction(1) / al[n]
                for j in range(n)] for i in range(n)]
    inverse = [[x * total * (total + 1) for x in row] for row in inverse]
    return sigma, inverse


def bootstrap_matrices(alpha):
    """Exact chart matrices ``(Sigma, N, D)`` for ``Dir(alpha)``."""
    al = [Fraction(a) for a in alpha]
    if len(al) < 2 or any(a <= 0 for a in al):
        raise ValueError("Dirichlet alpha needs at least two positive entries")
    total = sum(al)
    n = len(al) - 1
    sigma, sinv = chart_covariance(alpha)
    moments = DirichletMoments(alpha)

    pbar = [_pvar(n, i) for i in range(n)]
    # H = (diag(pbar) - pbar pbar^T)/A
    hmat = [[_padd(_pconst(n, Fraction(0)) if i != j else _pvar(n, i),
                   _pmul(pbar[i], pbar[j]), Fraction(-1)) for j in range(n)] for i in range(n)]
    hmat = [[{e: c / total for e, c in poly.items()} for poly in row] for row in hmat]

    # N = E[H Sigma^{-1} H]
    hs = [[{} for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            acc: dict = {}
            for k in range(n):
                if sinv[k][j]:
                    acc = _padd(acc, hmat[i][k], sinv[k][j])
            hs[i][j] = acc
    n_poly = [[{} for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            acc: dict = {}
            for k in range(n):
                acc = _padd(acc, _pmul(hs[i][k], hmat[k][j]))
            n_poly[i][j] = acc
            n_poly[j][i] = acc
    n_mat = [[moments.expect(n_poly[i][j]) for j in range(n)] for i in range(n)]
    n_mat = [[(n_mat[i][j] + n_mat[j][i]) / 2 for j in range(n)] for i in range(n)]

    # D = E[ sum_{e,f} H_{ef} (d_e H) Sigma^{-1} (d_f H) ]  using A d_e H = e_e u_e^T + u_e e_e^T
    uvec = [[_padd(_pconst(n, Fraction(1, 2)) if i == e else {}, pbar[i], Fraction(-1))
             for i in range(n)] for e in range(n)]        # uvec[e][i] = delta_{ie}/2 - p_i
    sp = []                                              # sp[i] = (Sigma^{-1} pbar)_i
    for i in range(n):
        acc: dict = {}
        for k in range(n):
            acc = _padd(acc, pbar[k], sinv[i][k])
        sp.append(acc)
    psp: dict = {}                                       # pbar^T Sigma^{-1} pbar
    for i in range(n):
        psp = _padd(psp, _pmul(pbar[i], sp[i]))

    d_mat = [[Fraction(0)] * n for _ in range(n)]
    scale = Fraction(1) / (total * total)
    for e in range(n):
        for f in range(n):
            c1 = _padd(_pconst(n, sinv[e][f] / 2), sp[f], Fraction(-1))      # u_e^T S e_f
            c4 = _padd(_pconst(n, sinv[e][f] / 2), sp[e], Fraction(-1))      # e_e^T S u_f
            c2 = _padd(_padd(_padd(_pconst(n, sinv[e][f] / 4), sp[f], Fraction(-1, 2)),
                             sp[e], Fraction(-1, 2)), psp)                   # u_e^T S u_f
            c3 = sinv[e][f]                                                  # e_e^T S e_f
            weight = hmat[e][f]
            for i in range(n):
                for j in range(n):
                    # K^{ef}_{ij} = (e_e)_i c1 (u_f)_j + (e_e)_i c2 (e_f)_j
                    #             + c3 (u_e)_i (u_f)_j + (u_e)_i c4 (e_f)_j
                    acc: dict = {}
                    if i == e:
                        acc = _padd(acc, _pmul(c1, uvec[f][j]))
                        if j == f:
                            acc = _padd(acc, c2)
                    if c3:
                        acc = _padd(acc, _pmul(uvec[e][i], uvec[f][j]), c3)
                    if j == f:
                        acc = _padd(acc, _pmul(c4, uvec[e][i]))
                    if not acc:
                        continue
                    d_mat[i][j] += scale * moments.expect(_pmul(weight, acc))
    d_mat = [[(d_mat[i][j] + d_mat[j][i]) / 2 for j in range(n)] for i in range(n)]
    return sigma, n_mat, d_mat


# ---------------------------------------------------------------------------------------
# diagnostics
# ---------------------------------------------------------------------------------------

RHO_BETAS = (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(1))
SHARP_RHO = Fraction(1, 2)
GATE_ZERO_IMPLIED_CEILING = Fraction(2)


def instance_id(alpha) -> str:
    return "dir(" + ",".join(str(int(a)) for a in alpha) + ")"


def analyse(alpha, betas=RHO_BETAS) -> dict:
    """Every exact Loewner verdict the anisotropic bootstrap asks of one Dirichlet instance."""
    alpha = tuple(int(a) for a in alpha)
    sigma, n_mat, d_mat = bootstrap_matrices(alpha)
    n_dim = len(sigma)
    r_mat = ex.add(n_mat, d_mat, Fraction(-1))

    sharp = ex.add(ex.scale_matrix(n_mat, SHARP_RHO), d_mat, Fraction(-1))     # N/2 - D
    sharp_verdict, sharp_cert = ex.loewner_verdict(sharp, "N/2 - D  (sharp candidate R >= N/2)")
    sharp_witness = (ex.negativity_witness(sharp, "N/2 - D") if sharp_verdict == "indefinite"
                     else None)
    sharp_rayleigh = ex.rational_lower_bound_for_max_ratio(d_mat, n_mat)

    brascamp = ex.add(ex.add(d_mat, n_mat, Fraction(-1)), sigma)               # D - N + Sigma
    bl_verdict, bl_cert = ex.loewner_verdict(brascamp, "D - N + Sigma  (Brascamp-Lieb N-I <= D)")

    gate_zero = ex.generalized_max_ratio_float(n_mat, sigma)
    gate_zero_excess = ex.add(n_mat, sigma, -GATE_ZERO_IMPLIED_CEILING)        # N - 2 Sigma
    gz_verdict, gz_cert = ex.loewner_verdict(gate_zero_excess, "N - 2 Sigma")
    gate_zero_above_two = ex.negativity_witness(
        ex.scale_matrix(gate_zero_excess, Fraction(-1)), "2 Sigma - N")

    rho: dict[str, dict] = {}
    for beta in betas:
        pencil = ex.add(r_mat, sigma, beta)                                    # R + beta I
        rho[str(beta)] = ex.certified_min_ratio_bracket(pencil, n_mat)

    return {
        "instance": instance_id(alpha), "alpha": list(alpha), "m": len(alpha), "n": n_dim,
        "A": float(sum(alpha)),
        "sigma": ex.matrix_payload(sigma),
        "N": ex.matrix_payload(n_mat), "D": ex.matrix_payload(d_mat),
        "R": ex.matrix_payload(r_mat),
        "sharp_candidate_verdict": sharp_verdict,
        "sharp_candidate_holds": sharp_verdict in {"pd", "psd_singular"},
        "sharp_candidate_certificate": sharp_cert,
        "sharp_candidate_negativity_witness": sharp_witness,
        "lambda_max_D_over_N_exact_lower": sharp_rayleigh["lower_bound_float"],
        "lambda_max_D_over_N_certificate": sharp_rayleigh,
        "lambda_max_D_over_N_directional": ex.generalized_max_ratio_float(d_mat, n_mat),
        "brascamp_lieb_verdict": bl_verdict,
        "brascamp_lieb_holds": bl_verdict in {"pd", "psd_singular"},
        "brascamp_lieb_certificate": bl_cert,
        "gate_zero_ratio_directional": gate_zero,
        "gate_zero_minus_two_verdict": gz_verdict,
        "gate_zero_exceeds_two_witness": gate_zero_above_two,
        "gate_zero_exceeds_two": gate_zero_above_two is not None,
        "rho_star": {k: {"floating": v["floating_estimate"],
                         "exact_upper_bound": v["exact_upper_bound"]["upper_bound_float"],
                         "exact_lower_bound": (v["exact_lower_bound"]["candidate_float"]
                                               if v["exact_lower_bound"]["proves_lower_bound"]
                                               else None)}
                     for k, v in rho.items()},
        "rho_star_certificates": rho,
    }


def gate_zero_crosscheck(alpha) -> tuple[float, float]:
    """``lambda_max(N, Sigma)`` here must equal the certified ``cmh-gate-zero`` ratio."""
    from ..cmh_gate_zero import dirichlet_gate_zero

    sigma, n_mat, _ = bootstrap_matrices(alpha)
    return ex.generalized_max_ratio_float(n_mat, sigma), dirichlet_gate_zero(alpha)["g0ratio"]


def one_dimensional_crosscheck(a_par: int, b_par: int) -> tuple[float, float, float, float]:
    """``Dir(a,b)`` on ``Delta_1`` is ``Beta(a,b)``: both channels must give the same N and D."""
    from .onedim import beta_instance

    sigma, n_mat, d_mat = bootstrap_matrices((a_par, b_par))
    whiten = Fraction(1) / sigma[0][0]
    row = beta_instance(a_par, b_par)
    return (float(n_mat[0][0] * whiten), float(row["N"]),
            float(d_mat[0][0] * whiten), float(row["D"]))
