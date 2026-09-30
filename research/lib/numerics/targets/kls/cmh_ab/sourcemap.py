"""Channel 1(c): two-dimensional moment maps built from an analytic *source* potential.

The requested channel prescribed a target ``mu = g dx`` on a compact convex body and asked for a
damped-Newton solve of ``g(grad phi) det D^2 phi = e^{-phi}``.  That inverse problem is fragile
and its residual is the dominant uncertainty.  It is also unnecessary here: by the
Cordero-Erausquin--Klartag characterization a moment map is exactly a pair
``(psi, (grad psi)_# e^{-psi})`` with ``psi`` convex and ``e^{-psi}`` a probability density, so
*prescribing ``psi`` and reading off the target* enumerates the same class of objects with no
PDE solve at all.  The cost is that the target is known only through ``psi``; the benefit is that
``H = D^2 psi`` and all its derivatives are analytic and every integral is a source-coordinate
quadrature against ``e^{-psi}``.

What is *not* free is admissibility.  The candidate ``(AB)`` concerns centred **log-concave**
targets, so each instance verifies:

* ``D^2 psi > 0`` at every node (else the instance is not a moment map at all);
* ``int e^{-psi} = 1``, ``int grad psi d eta = 0`` (barycentre; automatic in exact arithmetic,
  a genuine quadrature residual here);
* the Stein identities ``int H d eta = Sigma`` and ``E_mu[H grad f] = E_mu[x f]`` on quadratic
  ``f`` -- the requested ``E_mu H = Cov`` and ``Div_mu H = -x`` residual checks;
* ``D^2 V >= 0`` at every node, where ``V(grad psi(y)) = psi(y) + log det D^2 psi(y)``; this is
  target log-concavity and it is *not* automatic;
* the differentiated Monge-Ampere identity ``N = D + R`` with ``R = (1/2) int {H, A + Q}``
  computed independently of ``N - D``.

The last item is the strongest available validation of the whole transport: ``N`` and ``D`` come
from the probe's definitions and ``R`` from the differentiated Monge-Ampere reservoirs, and the
two routes share no code path.  An instance whose residuals exceed the recorded tolerance is
reported as ABORTED and contributes to no verdict.

Everything in this module is quadrature on a finite grid.  It is **directional** evidence only.
"""
from __future__ import annotations

import math

import numpy as np

from .jets import Jet, jexp, jlog, jcosh, jgaussian_bump, jhermite


DIM = 2
MOMENT_MAP_RESIDUAL_ABORT = 1e-6          # pre-registered; weighted L2 residual gate
CONVEXITY_MARGIN_ABORT = 1e-10
LOG_CONCAVITY_NODE_TOL = 1e-6             # relative pointwise tolerance on lambda_min(A)
LOG_CONCAVITY_MEAN_TOL = 1e-9             # relative tolerance on lambda_min(int A d eta)
WELL_CONDITIONED_KAPPA = 1e6              # cond(H) below which the pointwise sign of A is safe


# ---------------------------------------------------------------------------------------
# one-dimensional reference rules (each integrates its own factor exactly to machine precision)
# ---------------------------------------------------------------------------------------

def gamma_rule(n: int, shape: float):
    """Nodes/weights for the ``Gamma(shape)`` moment potential via generalized Gauss-Laguerre.

    ``phi_a(y) = e^y - a y + log Gamma(a)`` is the moment potential of the centred
    ``Gamma(a, 1)`` law: ``phi_a'' = phi_a' + a``, ``e^y ~ Gamma(a)``, and
    ``int f(y) e^{-phi_a} dy = int_0^infty f(log u) u^{a-1} e^{-u} du / Gamma(a)``.
    ``a = 1`` is the centred one-sided exponential, the CMH and (AB) saturator; ``a > 1`` moves
    strictly into the interior of the log-concave class because ``V'' = (a-1)/w^2 > 0``.
    """
    from scipy.special import roots_genlaguerre

    u, w = roots_genlaguerre(n, shape - 1.0)
    return np.log(u), w / w.sum()


def exponential_rule(n: int):
    """Nodes/weights for ``int f(s) e^{-(e^s - s)} ds`` via ``u = e^s`` and Gauss-Laguerre."""
    u, w = np.polynomial.laguerre.laggauss(n)
    return np.log(u), w / w.sum()


def gaussian_rule(n: int):
    """Nodes/weights for ``int f(t) e^{-t^2/2 - log sqrt(2 pi)} dt`` via Gauss-Hermite."""
    x, w = np.polynomial.hermite_e.hermegauss(n)
    return x, w / w.sum()


UNIFORM_C = math.sqrt(3.0) / 2.0


def uniform_rule(n: int):
    """Nodes/weights for the moment potential ``2 log cosh(c y) + log(4/sqrt 3)`` of U[-r,r]."""
    v, w = np.polynomial.legendre.leggauss(n)
    return np.arctanh(v) / UNIFORM_C, w / 2.0


def exponential_potential(j: Jet) -> Jet:
    return jexp(j) - j


def gaussian_potential(j: Jet) -> Jet:
    return j * j * 0.5 + 0.5 * math.log(2.0 * math.pi)


def uniform_potential(j: Jet) -> Jet:
    return 2.0 * jlog(jcosh(j * UNIFORM_C)) + math.log(4.0 / math.sqrt(3.0))


FACTORS = {
    "exponential": (exponential_rule, exponential_potential),
    "gaussian": (gaussian_rule, gaussian_potential),
    "uniform": (uniform_rule, uniform_potential),
}
# How many nodes a factor needs, relative to a base budget: the Gauss-Hermite rule resolves a
# Gaussian factor with very few nodes, while the Gauss-Laguerre rule has to reach far into the
# exponential tail before the H^2 moments converge.
FACTOR_NODE_SCALE = {"exponential": 1.0, "uniform": 0.6, "gaussian": 0.3}


def parse_factor(name: str):
    """``"gamma:1.5"`` -> ``("gamma", 1.5)``; every other name is a fixed factor."""
    if name.startswith("gamma:"):
        return "gamma", float(name.split(":", 1)[1])
    return name, None


def factor_rule(name: str, n: int):
    kind, shape = parse_factor(name)
    if kind == "gamma":
        return gamma_rule(n, shape)
    return FACTORS[kind][0](n)


def factor_potential(name: str):
    kind, shape = parse_factor(name)
    if kind == "gamma":
        offset = math.lgamma(shape)
        return lambda j: jexp(j) - j * shape + offset
    return FACTORS[kind][1]


def factor_node_scale(name: str) -> float:
    kind, _ = parse_factor(name)
    return FACTOR_NODE_SCALE.get(kind, 1.0)


def factor_exact_bootstrap(name: str):
    """Exact one-dimensional ``(N, D)`` of a factor, standardized to variance one."""
    kind, shape = parse_factor(name)
    if kind == "gamma":
        return 1.0 + 1.0 / shape, 1.0 / shape          # tau = w: N = (a+1)/a, D = 1/a
    if kind == "exponential":
        return 2.0, 1.0
    if kind == "gaussian":
        return 1.0, 0.0
    if kind == "uniform":
        return 1.2, 0.6
    raise KeyError(name)


# ---------------------------------------------------------------------------------------
# geometries
# ---------------------------------------------------------------------------------------

class ProductGeometry:
    """``psi = f_1(y_1) + f_2(y_2) + eps a(y_1) b(y_2)``, quadrature by the factor rules."""

    def __init__(self, name, factor_1, factor_2, coupling=None, epsilon=0.0,
                 description=""):
        self.name = name
        self.factor_1, self.factor_2 = factor_1, factor_2
        self.coupling = coupling
        self.epsilon = float(epsilon)
        self.description = description

    def parameters(self) -> dict:
        return {"kind": "perturbed-product-source-potential",
                "factor_1": self.factor_1, "factor_2": self.factor_2,
                "coupling": None if self.coupling is None else self.coupling.label,
                "epsilon": self.epsilon}

    def resolution(self, base_nodes: int):
        return tuple(max(24, int(round(base_nodes * factor_node_scale(factor))))
                     for factor in (self.factor_1, self.factor_2))

    def nodes(self, resolution):
        n1, n2 = resolution
        y1, w1 = factor_rule(self.factor_1, n1)
        y2, w2 = factor_rule(self.factor_2, n2)
        grid_1, grid_2 = np.meshgrid(y1, y2, indexing="ij")
        weights = np.outer(w1, w2)
        return grid_1.ravel(), grid_2.ravel(), weights.ravel(), self._reference

    def _reference(self, j1: Jet, j2: Jet) -> Jet:
        return factor_potential(self.factor_1)(j1) + factor_potential(self.factor_2)(j2)

    def psi(self, j1: Jet, j2: Jet) -> Jet:
        base = self._reference(j1, j2)
        if self.coupling is None or self.epsilon == 0.0:
            return base
        return base + self.coupling(j1, j2) * self.epsilon


class DirichletGeometry:
    """The certified Dirichlet moment potential on ``m = 3``, in the chart ``y_3 = 0``.

    ``varphi(y) = A log(e^{y_1/A} + e^{y_2/A} + 1) - q_1 y_1 - q_2 y_2``.  This is the one
    geometry in the channel whose exact answer is known independently (channel 1(b)), so it
    calibrates the quadrature engine on a genuinely nonproduct moment map.
    """

    def __init__(self, alpha):
        if len(alpha) != 3:
            raise ValueError("the two-dimensional chart needs exactly three Dirichlet weights")
        self.alpha = tuple(float(a) for a in alpha)
        self.total = sum(self.alpha)
        self.name = "dirichlet(" + ",".join(str(int(a)) for a in alpha) + ")"
        self.description = "certified Dirichlet moment potential, chart y_3 = 0"

    def parameters(self) -> dict:
        return {"kind": "dirichlet-moment-potential", "alpha": list(self.alpha),
                "quadrature": "stick-breaking Gauss-Jacobi (exact for polynomials in p)"}

    def resolution(self, base_nodes: int):
        return (max(24, base_nodes // 4), max(24, base_nodes // 4))

    @staticmethod
    def _beta_rule(n: int, first: float, second: float):
        """Gauss-Jacobi nodes/weights for ``Beta(first, second)`` on ``(0,1)``."""
        from scipy.special import roots_jacobi

        x, w = roots_jacobi(n, second - 1.0, first - 1.0)
        return (1.0 + x) / 2.0, w / w.sum()

    def nodes(self, resolution):
        n1, n2 = resolution
        a1, a2, a3 = self.alpha
        b1, w1 = self._beta_rule(n1, a1, a2 + a3)
        b2, w2 = self._beta_rule(n2, a2, a3)
        grid_1, grid_2 = np.meshgrid(b1, b2, indexing="ij")
        weights = np.outer(w1, w2).ravel()
        p1 = grid_1.ravel()
        p2 = ((1.0 - grid_1) * grid_2).ravel()
        p3 = ((1.0 - grid_1) * (1.0 - grid_2)).ravel()
        total = self.total
        return (total * np.log(p1 / p3), total * np.log(p2 / p3), weights, self._reference)

    def _reference(self, j1: Jet, j2: Jet) -> Jet:
        return self.psi(j1, j2)

    def psi(self, j1: Jet, j2: Jet) -> Jet:
        a = self.total
        inner = jexp(j1 * (1.0 / a)) + jexp(j2 * (1.0 / a)) + 1.0
        return a * jlog(inner) - j1 * (self.alpha[0] / a) - j2 * (self.alpha[1] / a)


class Coupling:
    """``a(y_1) b(y_2)`` with analytic derivatives, carrying its own label."""

    def __init__(self, label, first, second):
        self.label = label
        self.first, self.second = first, second

    def __call__(self, j1: Jet, j2: Jet) -> Jet:
        return self.first(j1) * self.second(j2)


def exponential_bump(centre: float, width: float):
    """A Gaussian bump in ``u = e^s``.

    Parametrizing in ``u`` rather than ``s`` matters: the unperturbed ``psi_ss = e^s`` vanishes
    as ``s -> -infinity``, and an ``s``-bump has ``a''(s) = O(1)`` there, which destroys strict
    convexity for every nonzero epsilon.  A ``u``-bump has ``a''(s) = O(u)``, the same order as
    the unperturbed Hessian, so convexity survives for small epsilon.
    """
    def factor(j: Jet) -> Jet:
        return jgaussian_bump(jexp(j), centre, width)

    factor.label = f"u-bump(c={centre},w={width})"
    return factor


def coordinate_bump(centre: float, width: float):
    def factor(j: Jet) -> Jet:
        return jgaussian_bump(j, centre, width)

    factor.label = f"y-bump(c={centre},w={width})"
    return factor


def damped_hermite(degree: int):
    """``He_degree(t) exp(-t^2/4)`` -- the transverse dictionary of the M9 task."""
    def factor(j: Jet) -> Jet:
        return jhermite(j, degree) * jgaussian_bump(j, 0.0, math.sqrt(2.0))

    factor.label = f"He{degree}*exp(-t^2/4)"
    return factor


def make_coupling(first, second) -> Coupling:
    return Coupling(f"{first.label} x {second.label}", first, second)


# ---------------------------------------------------------------------------------------
# field assembly
# ---------------------------------------------------------------------------------------

def _tensor_from_jet(jet: Jet, rank: int, size: int) -> np.ndarray:
    out = np.zeros((size,) + (DIM,) * rank)
    for index in np.ndindex(*(DIM,) * rank):
        ones = sum(index)
        out[(slice(None),) + index] = jet.c[(rank - ones, ones)]
    return out


def fields(geometry, resolution):
    """Analytic ``psi`` jets on the quadrature grid plus the normalized weights."""
    y1, y2, raw_weights, reference = geometry.nodes(resolution)
    j1, j2 = Jet.variable(y1, 0), Jet.variable(y2, 1)
    psi = geometry.psi(j1, j2)
    ref = reference(j1, j2)
    weights = raw_weights * np.exp(-(psi.value - ref.value))
    mass = float(weights.sum())
    weights = weights / mass
    size = y1.size
    return {
        "y1": y1, "y2": y2, "weights": weights, "quadrature_mass": mass,
        "psi": psi.value,
        "grad": np.stack([psi.c[(1, 0)], psi.c[(0, 1)]], axis=1),
        "H": _tensor_from_jet(psi, 2, size),
        "T3": _tensor_from_jet(psi, 3, size),
        "T4": _tensor_from_jet(psi, 4, size),
    }


def _sym_inv_sqrt(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(0.5 * (matrix + matrix.T))
    if values.min() <= 0:
        raise ValueError("covariance is not positive definite")
    return (vectors / np.sqrt(values)) @ vectors.T


def analyse(geometry, resolution=(160, 60), residual_abort=MOMENT_MAP_RESIDUAL_ABORT,
            keep_fields: bool = False) -> dict:
    """Whitened ``N``, ``D``, ``R`` plus every admissibility residual, for one geometry.

    ``keep_fields`` attaches the per-node numpy tensors under ``_fields``; that key is for oracle
    tests only and is never written to an artifact.
    """
    data = fields(geometry, resolution)
    w = data["weights"]
    hraw = data["H"]

    eig_h = np.linalg.eigvalsh(hraw)
    convexity_margin = float(eig_h.min())

    grad = data["grad"]
    barycentre = np.einsum("k,ka->a", w, grad)
    sigma = np.einsum("k,ka,kb->ab", w, grad, grad) - np.outer(barycentre, barycentre)

    # A perturbed potential is renormalized by the additive constant log Z; that constant changes
    # no derivative of psi, hence no bootstrap quantity, but it must be recorded to make the
    # instance a genuine moment map with a probability source density.
    mass = data["quadrature_mass"]
    aborted = []
    if convexity_margin <= CONVEXITY_MARGIN_ABORT:
        aborted.append("source potential is not strictly convex on the quadrature grid")
    if not np.isfinite(mass) or mass <= 0.0:
        aborted.append("source density does not have a finite positive mass")
    if aborted:
        return {"instance": geometry.name, "status": "aborted", "reasons": aborted,
                "parameters": geometry.parameters(), "resolution": list(resolution),
                "convexity_margin": convexity_margin,
                "log_normalizer": float(np.log(mass)) if mass > 0 else None}

    whiten = _sym_inv_sqrt(sigma)
    h = np.einsum("ai,kij,jb->kab", whiten, hraw, whiten)
    t3 = np.einsum("ai,bj,cl,kijl->kabc", whiten, whiten, whiten, data["T3"])
    t4 = np.einsum("ai,bj,cl,dm,kijlm->kabcd", whiten, whiten, whiten, whiten, data["T4"])
    hinv = np.linalg.inv(h)

    stein_residual = float(np.linalg.norm(np.einsum("k,kab->ab", w, h) - np.eye(DIM)))
    x = (grad - barycentre) @ whiten
    div_residual = 0.0
    for i in range(DIM):
        for j in range(DIM):
            lhs = (np.einsum("k,ka,k->a", w, h[:, :, i], x[:, j])
                   + np.einsum("k,ka,k->a", w, h[:, :, j], x[:, i]))
            rhs = np.einsum("k,ka,k,k->a", w, x, x[:, i], x[:, j])
            div_residual = max(div_residual, float(np.abs(lhs - rhs).max()))

    n_mat = np.einsum("k,kab,kbc->ac", w, h, h)
    d_mat = np.einsum("k,kab,kaij,kbjl->il", w, hinv, t3, t3)

    # A = H (D^2 V o grad psi) H is assembled *directly* as D^2 F - Gamma with
    # F = psi + log det H.  Forming D^2 V = H^{-1} A H^{-1} first would multiply the roundoff by
    # ||H^{-1}||^2, which is enormous wherever the Hessian degenerates (simplex boundary), and
    # the sign question ``mu log-concave <=> D^2 V >= 0`` is unchanged by the congruence.
    q_mat = np.einsum("kij,kajl,klm,kbmi->kab", hinv, t3, hinv, t3)
    trace_t4 = np.einsum("kij,kabij->kab", hinv, t4)
    f_hess = h + trace_t4 - q_mat
    grad_f = x + np.einsum("kij,kaij->ka", hinv, t3)
    vx = np.einsum("kbd,kd->kb", hinv, grad_f)
    gamma = np.einsum("kcab,kb->kca", t3, vx)
    a_mat = f_hess - gamma
    a_mat = 0.5 * (a_mat + np.swapaxes(a_mat, 1, 2))
    a_scale = np.maximum(np.abs(f_hess).max(axis=(1, 2)), np.abs(gamma).max(axis=(1, 2)))
    a_eigenvalues = np.linalg.eigvalsh(a_mat)
    relative_margin = a_eigenvalues[:, 0] / np.maximum(a_scale, 1e-300)
    log_concavity_margin = float(relative_margin.min())
    # ``A`` is a difference of two ``H^{-1}``-amplified terms, so wherever ``H`` degenerates the
    # pointwise sign is dominated by roundoff.  The mass carried by the violating nodes, and the
    # well-conditioned average int A d eta, are the two robust readouts.
    violating = relative_margin < -LOG_CONCAVITY_NODE_TOL
    violating_mass = float(w[violating].sum())
    # ``A`` loses relative accuracy like the condition number of ``H``; on nodes where that
    # number stays below WELL_CONDITIONED_KAPPA the pointwise sign of ``A`` is trustworthy.
    kappa = eig_h[:, -1] / np.maximum(eig_h[:, 0], 1e-300)
    well_conditioned = kappa < WELL_CONDITIONED_KAPPA
    if well_conditioned.any():
        masked = np.where(well_conditioned, relative_margin, np.inf)
        worst_node = int(np.argmin(masked))
        bulk_margin = float(masked[worst_node])
        bulk_mass = float(w[well_conditioned].sum())
        bulk_violating_mass = float(w[well_conditioned & violating].sum())
        bulk_argmin = {"y1": float(data["y1"][worst_node]), "y2": float(data["y2"][worst_node]),
                       "condition_number": float(kappa[worst_node]),
                       "source_weight": float(w[worst_node])}
    else:
        bulk_margin, bulk_mass, bulk_violating_mass = float("nan"), 0.0, 0.0
        bulk_argmin = None
    a_mean = np.einsum("k,kab->ab", w, a_mat)
    a_mean = 0.5 * (a_mean + a_mean.T)
    a_mean_scale = max(float(np.abs(a_mean).max()), 1.0)
    a_mean_margin = float(np.linalg.eigvalsh(a_mean).min()) / a_mean_scale
    # ``mu`` log-concave  =>  A = H (D^2 V) H >= 0 pointwise  =>  int A d eta >= 0.  The averaged
    # test is one-sided but well conditioned, so a negative eigenvalue of the average is robust
    # evidence that the target has LEFT the log-concave class; the pointwise readout is not,
    # because A is a difference of two H^{-1}-amplified terms wherever H degenerates.
    if a_mean_margin < -LOG_CONCAVITY_MEAN_TOL or bulk_margin < -LOG_CONCAVITY_NODE_TOL:
        log_concavity = "violated"
    else:
        log_concavity = "consistent"

    # The two reservoirs are kept apart: R = R_A + R_Q with R_X = (1/2) int {H, X}.  Only R_A
    # sees log-concavity of the target; R_Q is the anisotropic version of the Chen-Klartag
    # cyclic square, whose trace obeys Tr R_Q >= Tr D.  Whether the *matrix* inequality
    # R_Q >= D holds is exactly the step the probe fenced off as having no pointwise Loewner
    # promotion, so ``lambda_min(R_Q - D)`` is reported separately.
    r_a = np.einsum("k,kai,kib->ab", w, h, a_mat)
    r_a = 0.5 * (r_a + r_a.T)
    r_q = np.einsum("k,kai,kib->ab", w, h, q_mat)
    r_q = 0.5 * (r_q + r_q.T)
    r_aq = r_a + r_q

    n_mat = 0.5 * (n_mat + n_mat.T)
    d_mat = 0.5 * (d_mat + d_mat.T)
    r_def = n_mat - d_mat
    identity_residual = float(np.linalg.norm(r_def - r_aq) / max(np.linalg.norm(n_mat), 1e-300))

    residuals = {
        "barycentre_norm": float(np.linalg.norm(barycentre)),
        "stein_EH_minus_Sigma": stein_residual,
        "stein_div_quadratic": div_residual,
        "monge_ampere_identity_relative": identity_residual,
    }
    worst = max(residuals["barycentre_norm"], residuals["stein_EH_minus_Sigma"],
                residuals["stein_div_quadratic"], residuals["monge_ampere_identity_relative"])
    status = "ok" if worst <= residual_abort else "aborted"

    sharp = 0.5 * n_mat - d_mat
    sharp_min = float(np.linalg.eigvalsh(sharp).min())
    brascamp = d_mat - (n_mat - np.eye(DIM))
    from scipy.linalg import eigh

    rho_star = {}
    for beta in (0.0, 0.25, 0.5, 1.0):
        rho_star[str(beta)] = float(
            eigh(r_def + beta * np.eye(DIM), n_mat, eigvals_only=True)[0])

    result = {
        "instance": geometry.name, "status": status,
        "reasons": [] if status == "ok" else ["residual gate exceeded"],
        "description": geometry.description,
        "parameters": geometry.parameters(), "resolution": list(resolution),
        "convexity_margin": convexity_margin,
        "log_normalizer": float(np.log(mass)),
        "target_log_concavity_margin": log_concavity_margin,
        "target_log_concavity_margin_definition":
            "min over nodes of lambda_min(A) / max(|D^2 F|, |Gamma|), A = H (D^2 V) H",
        "target_log_concavity_violating_mass": violating_mass,
        "target_log_concavity_node_tolerance": LOG_CONCAVITY_NODE_TOL,
        "target_log_concavity_bulk_margin": bulk_margin,
        "target_log_concavity_bulk_argmin": bulk_argmin,
        "target_log_concavity_bulk_mass": bulk_mass,
        "target_log_concavity_bulk_violating_mass": bulk_violating_mass,
        "well_conditioned_kappa": WELL_CONDITIONED_KAPPA,
        "target_mean_A_min_eigenvalue_relative": a_mean_margin,
        "target_log_concavity": log_concavity,
        "target_log_concavity_test":
            "'violated' iff lambda_min(int A d eta) < 0 or lambda_min(A) < 0 on a "
            "well-conditioned node; both are one-sided, so 'consistent' does NOT prove that mu "
            "is log-concave",
        "target_log_concave": bool(log_concavity == "consistent"),
        "covariance": sigma.tolist(),
        "N": n_mat.tolist(), "D": d_mat.tolist(), "R": r_def.tolist(),
        "R_from_monge_ampere_sources": r_aq.tolist(),
        "R_A": r_a.tolist(), "R_Q": r_q.tolist(),
        "lambda_min_R_A": float(np.linalg.eigvalsh(r_a).min()),
        # the certified Chen-Klartag scalar fact: cyclic symmetry of D^3 psi gives Tr R_Q >= Tr D
        "trace_R_Q_minus_D": float(np.trace(r_q) - np.trace(d_mat)),
        "trace_R_Q_minus_D_relative": float((np.trace(r_q) - np.trace(d_mat))
                                            / max(np.trace(d_mat), 1e-300)),
        "lambda_min_R_Q_minus_D": float(np.linalg.eigvalsh(r_q - d_mat).min()),
        "lambda_min_R_Q_minus_D_relative": float(
            np.linalg.eigvalsh(r_q - d_mat).min() / max(np.linalg.norm(d_mat), 1e-300)),
        "residuals": residuals, "worst_residual": worst,
        "residual_abort_threshold": residual_abort,
        "lambda_max_N": float(np.linalg.eigvalsh(n_mat).max()),
        "lambda_max_D_over_N": float(eigh(d_mat, n_mat, eigvals_only=True)[-1]),
        "lambda_min_sharp_R_minus_half_N": sharp_min,
        "lambda_min_brascamp_lieb": float(np.linalg.eigvalsh(brascamp).min()),
        "rho_star": rho_star,
    }
    if keep_fields:
        result["_fields"] = {"weights": w, "H": h, "H_raw": hraw, "T3": t3, "A": a_mat,
                             "Q": q_mat, "whiten": whiten, "x": x,
                             "relative_margin": relative_margin,
                             "y1": data["y1"], "y2": data["y2"]}
    return result


def dirichlet_target_hessian_error(alpha, resolution=(48, 48)):
    """Oracle: the engine's ``A = H (D^2 V) H`` against the closed-form Dirichlet ``D^2 V``.

    For ``P ~ Dir(alpha)`` the chart target density is proportional to
    ``prod_{i<m} p_i^{alpha_i - 1} * p_m^{alpha_m - 1}`` with ``p_m = 1 - sum_{i<m} p_i``, so

        D^2 V = diag((alpha_i - 1)/p_i^2)_{i<m} + (alpha_m - 1)/p_m^2 * 1 1^T .

    Returned is the largest relative error over the nodes carrying all but ``1e-10`` of the
    source mass; the excluded nodes sit where ``H`` degenerates and ``A`` is a difference of two
    ``H^{-1}``-amplified terms.
    """
    geometry = DirichletGeometry(alpha)
    row = analyse(geometry, resolution, keep_fields=True)
    if row["status"] != "ok":
        raise RuntimeError(f"engine aborted on {geometry.name}: {row['reasons']}")
    fld = row["_fields"]
    total = geometry.total
    z1, z2 = np.exp(fld["y1"] / total), np.exp(fld["y2"] / total)
    denominator = z1 + z2 + 1.0
    p = np.stack([z1 / denominator, z2 / denominator], axis=1)
    p_last = 1.0 / denominator
    exact_v = np.zeros((p.shape[0], DIM, DIM))
    for i in range(DIM):
        exact_v[:, i, i] += (alpha[i] - 1.0) / p[:, i] ** 2
    exact_v += ((alpha[2] - 1.0) / p_last ** 2)[:, None, None]
    whiten = fld["whiten"]
    unwhiten = np.linalg.inv(whiten)
    exact_v_whitened = np.einsum("ai,kij,jb->kab", unwhiten, exact_v, unwhiten)
    exact_a = np.einsum("kai,kij,kjb->kab", fld["H"], exact_v_whitened, fld["H"])
    scale = np.maximum(np.abs(exact_a).max(axis=(1, 2)), 1e-12)
    error = np.abs(fld["A"] - exact_a).max(axis=(1, 2)) / scale
    weights = fld["weights"]
    order = np.argsort(error)
    kept = np.cumsum(weights[order]) <= 1.0 - 1e-10
    return float(error[order][kept].max()), float(weights[order][~kept].sum())
