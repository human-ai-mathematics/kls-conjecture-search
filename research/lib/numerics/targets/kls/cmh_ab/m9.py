"""Channel 2 (task M9): a second-variation probe of ``CMH(4)`` at the saturating product.

`thm:cmh-product` and `thm:cmh-1d` give ``C_CMH = 4`` exactly for the centred one-sided
exponential times a standard Gaussian, with zero slack.  `q:cmh-solenoidal-perturbation` asks
whether an admissible perturbation raises the quotient.  The certified caveat, restated in
`2026-08-27-proof-miner-cmh-transverse-deficit-w3t01.md`, is that under a nonproduct perturbation
the law, covariance, canonical kernel, generator, numerator, denominator and the (non-attained)
near-extremizer all move together.  A numerical probe is therefore the natural directional tool,
and it is *only* directional.

Source-coordinate form of the quotient.  Write ``eta = e^{-psi} dy``, ``mu = (grad psi)_# eta``,
``H = D^2 psi``, and for a target test function ``g`` put ``G = g o grad psi``.  Then
``H grad_x g = grad_y G`` exactly, and

    L_mu g o grad psi = e^{psi} div_y( H^{-1} grad_y G e^{-psi} )
                      = sum_{i,a} H^{ia} G_{ia} + sum_a d_a G_a,
    d_a = - sum_{i,j,k} H^{ij} psi_{ijk} H^{ka} - sum_i H^{ia} psi_i,

so the CMH Rayleigh quotient is entirely a source-coordinate integral,

    Q(G) = int <grad G, Sigma^{-1} grad G> d eta  /  int (L G)^2 d eta,
    Sigma = int grad psi (grad psi)^T d eta.

Both the drift identity ``d_a = -(V_a o grad psi)`` (a consequence of the full symmetry of
``D^3 psi``) and the numerator identity are checked numerically in the oracle suite.

Calibration.  At ``eps = 0`` the degree-one Galerkin value must be exactly
``max(E H_exp^2, E H_gauss^2) = max(2, 1) = 2``, and increasing the polynomial degree must
increase the value monotonically toward ``4``.  Convergence to ``4`` is slow because the
exponential endpoint is the bottom of a purely continuous spectrum and is not attained by any
``L^2`` eigenfunction: a finite Galerkin space gives a *lower* bound that stays visibly below
``4``.  This limits the power of the probe and the limitation is reported with every value.
"""
from __future__ import annotations

import math

import numpy as np
from scipy.linalg import eigh

from .sourcemap import (
    DIM, ProductGeometry, coordinate_bump, damped_hermite, exponential_bump, fields,
    make_coupling, parse_factor as sourcemap_parse,
)


KEEP_REL_TOL = 1e-11
DEGREE_ONE_ANCHOR = 2.0
CMH_CEILING = 4.0
REFUTATION_CANDIDATE_Q = 4.05          # pre-registered before any run


# ---------------------------------------------------------------------------------------
# basis
# ---------------------------------------------------------------------------------------

def _laguerre_1d(s: np.ndarray, degree: int):
    """``L_k(u)`` and its first two ``s``-derivatives, ``u = e^s``."""
    u = np.exp(s)
    coefficients = np.zeros(degree + 1)
    coefficients[degree] = 1.0
    value = np.polynomial.laguerre.lagval(u, coefficients)
    first = np.polynomial.laguerre.lagval(u, np.polynomial.laguerre.lagder(coefficients, 1)) \
        if degree >= 1 else np.zeros_like(u)
    second = np.polynomial.laguerre.lagval(u, np.polynomial.laguerre.lagder(coefficients, 2)) \
        if degree >= 2 else np.zeros_like(u)
    return value, u * first, u * first + u * u * second


def _exponential_enrichment(s: np.ndarray, rate: float):
    """``exp(rate * u)`` and its first two ``s``-derivatives; admissible for ``rate < 1/2``."""
    u = np.exp(s)
    value = np.exp(rate * u)
    return value, rate * u * value, (rate * u + rate * rate * u * u) * value


def _hermite_1d(t: np.ndarray, degree: int):
    """Normalized probabilists' ``He_j`` and its first two derivatives."""
    coefficients = np.zeros(degree + 1)
    coefficients[degree] = 1.0
    norm = math.sqrt(math.factorial(degree))
    value = np.polynomial.hermite_e.hermeval(t, coefficients) / norm
    first = (np.polynomial.hermite_e.hermeval(
        t, np.polynomial.hermite_e.hermeder(coefficients, 1)) / norm
        if degree >= 1 else np.zeros_like(t))
    second = (np.polynomial.hermite_e.hermeval(
        t, np.polynomial.hermite_e.hermeder(coefficients, 2)) / norm
        if degree >= 2 else np.zeros_like(t))
    return value, first, second


def basis_labels(degree: int, enrichment_rates, enrichment_transverse: int):
    labels = [("laguerre", k, j) for k in range(degree + 1) for j in range(degree + 1 - k)
              if k + j >= 1]
    labels += [("enrich", rate, j) for rate in enrichment_rates
               for j in range(enrichment_transverse + 1)]
    return labels


def build_basis(s_nodes, t_nodes, labels, longitudinal_kind="laguerre"):
    """Values and first/second derivatives of every basis function on the tensor grid.

    ``longitudinal_kind`` is ``"laguerre"`` for a Gamma factor (polynomials in ``u = e^s``) and
    ``"hermite"`` for a Gaussian factor.  The second choice exists to calibrate the whole
    numerator/denominator/generator assembly against a CMH constant that is *attained*: for a
    Gaussian product, ``L He_k = -k He_k`` gives quotient ``1/k``, so the Galerkin value is
    exactly ``1`` at every degree.
    """
    n1, n2 = s_nodes.size, t_nodes.size
    cache_s: dict = {}
    cache_t: dict = {}
    values, grads, hessians = [], [], []
    for kind, index, transverse in labels:
        key = (kind, index)
        if key not in cache_s:
            if kind == "enrich":
                cache_s[key] = _exponential_enrichment(s_nodes, index)
            elif longitudinal_kind == "hermite":
                cache_s[key] = _hermite_1d(s_nodes, index)
            else:
                cache_s[key] = _laguerre_1d(s_nodes, index)
        if transverse not in cache_t:
            cache_t[transverse] = _hermite_1d(t_nodes, transverse)
        f0, f1, f2 = cache_s[key]
        b0, b1, b2 = cache_t[transverse]
        values.append(np.outer(f0, b0).ravel())
        grads.append(np.stack([np.outer(f1, b0).ravel(), np.outer(f0, b1).ravel()], axis=1))
        hess = np.empty((n1 * n2, DIM, DIM))
        hess[:, 0, 0] = np.outer(f2, b0).ravel()
        hess[:, 0, 1] = hess[:, 1, 0] = np.outer(f1, b1).ravel()
        hess[:, 1, 1] = np.outer(f0, b2).ravel()
        hessians.append(hess)
    return np.array(values), np.array(grads), np.array(hessians)


# ---------------------------------------------------------------------------------------
# the quotient
# ---------------------------------------------------------------------------------------

def galerkin_quotient(geometry, resolution, degree, enrichment_rates=(),
                      enrichment_transverse=2):
    """Largest Galerkin CMH quotient for one source potential; a lower bound for ``C_CMH``."""
    n1, n2 = resolution
    data = fields(geometry, resolution)
    w = data["weights"]
    h, t3, grad_psi = data["H"], data["T3"], data["grad"]
    eig_h = np.linalg.eigvalsh(h)
    convexity_margin = float(eig_h.min())
    if convexity_margin <= 0.0:
        return {"status": "skipped", "reason": "source potential not strictly convex",
                "convexity_margin": convexity_margin, "degree": degree,
                "resolution": list(resolution)}

    hinv = np.linalg.inv(h)
    barycentre = np.einsum("k,ka->a", w, grad_psi)
    sigma = np.einsum("k,ka,kb->ab", w, grad_psi, grad_psi) - np.outer(barycentre, barycentre)
    sigma_inv = np.linalg.inv(sigma)

    drift = (-np.einsum("kij,kijl,kla->ka", hinv, t3, hinv)
             - np.einsum("kia,ki->ka", hinv, grad_psi))

    s_nodes = np.unique(data["y1"])
    t_nodes = np.unique(data["y2"])
    if s_nodes.size != n1 or t_nodes.size != n2:
        raise ValueError("m9 requires a tensor-product quadrature grid")
    labels = basis_labels(degree, enrichment_rates, enrichment_transverse)
    longitudinal_kind = ("hermite"
                         if sourcemap_parse(geometry.factor_1)[0] == "gaussian" else "laguerre")
    _, grads, hessians = build_basis(s_nodes, t_nodes, labels, longitudinal_kind)

    generator = (np.einsum("kia,bkia->bk", hinv, hessians)
                 + np.einsum("ka,bka->bk", drift, grads))
    numerator = np.einsum("k,aki,ij,bkj->ab", w, grads, sigma_inv, grads)
    denominator = np.einsum("k,ak,bk->ab", w, generator, generator)
    numerator = 0.5 * (numerator + numerator.T)
    denominator = 0.5 * (denominator + denominator.T)

    eigenvalues, vectors = np.linalg.eigh(denominator)
    keep = eigenvalues > KEEP_REL_TOL * eigenvalues.max()
    reducer = vectors[:, keep] / np.sqrt(eigenvalues[keep])
    reduced_numerator = reducer.T @ numerator @ reducer
    reduced_numerator = 0.5 * (reduced_numerator + reduced_numerator.T)
    q = float(np.linalg.eigvalsh(reduced_numerator)[-1])
    return {
        "status": "ok", "q": q, "degree": degree, "resolution": list(resolution),
        "basis_size": len(labels), "kept_directions": int(keep.sum()),
        "denominator_condition": float(eigenvalues.max() / max(eigenvalues[keep].min(), 1e-300)),
        "convexity_margin": convexity_margin,
        "covariance": sigma.tolist(),
        "covariance_drift": float(np.linalg.norm(sigma - np.eye(DIM))),
        "enrichment_rates": list(enrichment_rates),
    }


def saturating_geometry(coupling=None, epsilon: float = 0.0,
                        shape: float = 1.0) -> ProductGeometry:
    """``Gamma(shape) x Gaussian`` moment potential, optionally perturbed.

    ``shape = 1`` is the certified saturator with ``C_CMH = 4`` exactly.  It sits on the boundary
    of the log-concave class: its target potential is affine on the support, so ``D^2 V`` has a
    zero eigenvalue and a two-sided perturbation generically leaves the class.  ``shape > 1``
    moves strictly inside (``V'' = (a-1)/w^2 > 0``) at the price of ``C_CMH < 4``, and is the
    only place in this channel where a *two-sided* second difference can be admissible.
    """
    label = "exp" if shape == 1.0 else f"gam{shape:g}"
    name = (f"{label}-gauss" if coupling is None
            else f"{label}-gauss+{coupling.label}@{epsilon:+g}")
    return ProductGeometry(
        name, f"gamma:{shape:g}", "gaussian", coupling=coupling, epsilon=epsilon,
        description=("centred Gamma(%g) times standard Gaussian; C_CMH = 4 exactly at a = 1"
                     % shape))


def degree_one_anchor(shape: float = 1.0) -> float:
    """Linear test functions give ``lambda_max(E H^2) = max(1 + 1/a, 1)``."""
    return max(1.0 + 1.0 / shape, 1.0)


DEFAULT_LONGITUDINAL = (("u-bump", 0.6, 0.5), ("u-bump", 1.2, 0.8), ("u-bump", 2.5, 1.2))
DEFAULT_TRANSVERSE = (0, 1, 2, 3)
DEFAULT_EPSILONS = (0.02, 0.05, 0.1)
DEFAULT_SHAPES = (1.0, 1.5, 3.0)


def make_dictionary(longitudinal=DEFAULT_LONGITUDINAL, transverse=DEFAULT_TRANSVERSE):
    couplings = []
    for kind, centre, width in longitudinal:
        first = (exponential_bump(centre, width) if kind == "u-bump"
                 else coordinate_bump(centre, width))
        for degree in transverse:
            couplings.append(make_coupling(first, damped_hermite(degree)))
    return couplings
