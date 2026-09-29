"""Oracle tests for the `fiber-frame-dual` target (conditional-fiber-frame route).

Every exact identity here is a calibration anchor, not a mathematical claim about the
all-frame gate.  The Monte Carlo cross-checks validate the *implementation* of the exact
chamber machinery against an independent sampled estimator; they certify nothing.
"""
from fractions import Fraction

import numpy as np
import pytest

from numerics.targets.kls import fiber_frame_dual as ffd
from numerics.targets.kls.fiber_frame_dual import certify, frames, spherical


# ---------------------------------------------------------------------------------------
# exact machinery cross-checks
# ---------------------------------------------------------------------------------------

@pytest.mark.parametrize("m,k", [(3, 2), (4, 2), (5, 2), (3, 3), (4, 3)])
def test_root_closed_form_equals_chord_machinery(m, k):
    mons = frames.monomial_basis(m, k)
    closed = frames.root_single_direction_closed(m, mons)
    chord = frames.root_single_direction_matrix(m, k, mons)
    assert closed == chord


@pytest.mark.parametrize("m", [3, 4, 5, 6])
def test_linear_sector_quotient_one_exact(m):
    basis = frames.monomial_basis(m, 2)
    G = frames.gram_matrix(m, basis)
    assert frames.linear_block_equals_gram(frames.root_K(m, basis), G, m)
    assert frames.linear_block_equals_gram(frames.vertex_K(m, 2, basis), G, m)


@pytest.mark.parametrize("m", [3, 4, 5])
def test_root_radial_quadratic_anchor(m):
    basis = frames.monomial_basis(m, 2)
    G = frames.gram_matrix(m, basis)
    K = frames.root_K(m, basis)
    c = frames.radial_quadratic_vector(m, basis)
    got = certify.quadratic_form(K, c) / certify.quadratic_form(G, c)
    assert got == Fraction((m + 2) * (m + 3), 5 * m * m)


@pytest.mark.parametrize("m", [3, 4])
def test_single_root_direction_radial_energy_eq35(m):
    basis = frames.monomial_basis(m, 2)
    B12 = frames.root_single_direction_closed(m, basis)
    c = frames.radial_quadratic_vector(m, basis)
    assert certify.quadratic_form(B12, c) == Fraction(4, 5 * m * m * (m + 1) * (m + 1))


@pytest.mark.parametrize("k", [2, 3])
def test_vertex_equals_root_at_m2(k):
    basis = frames.monomial_basis(2, k)
    assert frames.root_K(2, basis) == frames.vertex_K(2, k, basis)


def test_vertex_linear_anchor_k3():
    basis = frames.monomial_basis(4, 3)
    G = frames.gram_matrix(4, basis)
    assert frames.linear_block_equals_gram(frames.vertex_K(4, 3, basis), G, 4)


def test_frame_tight_identity_directions():
    # d * int theta theta^T d rho == I on H_0 for both direction orbits (numeric check).
    for m in (3, 5, 8):
        d = m - 1
        eye = np.eye(m) - np.ones((m, m)) / m       # projector onto H_0
        roots = []
        for i in range(m):
            for j in range(i + 1, m):
                v = np.zeros(m)
                v[i], v[j] = 1.0, -1.0
                roots.append(v / np.sqrt(2.0))
        A = d * sum(np.outer(v, v) for v in roots) / len(roots)
        assert np.allclose(A, eye, atol=1e-12)
        verts = []
        for i in range(m):
            v = -np.ones(m) / m
            v[i] += 1.0
            verts.append(v / np.linalg.norm(v))
        B = d * sum(np.outer(v, v) for v in verts) / len(verts)
        assert np.allclose(B, eye, atol=1e-12)


# ---------------------------------------------------------------------------------------
# certification
# ---------------------------------------------------------------------------------------

def test_bareiss_pd_oracle():
    assert certify.bareiss_positive_definite(
        [[Fraction(2), Fraction(1)], [Fraction(1), Fraction(2)]])
    assert not certify.bareiss_positive_definite(
        [[Fraction(1), Fraction(2)], [Fraction(2), Fraction(1)]])
    assert not certify.bareiss_positive_definite(
        [[Fraction(0), Fraction(0)], [Fraction(0), Fraction(1)]])
    # PD with fractions and a nontrivial elimination
    M = [[Fraction(5, 3), Fraction(1, 2), Fraction(0)],
         [Fraction(1, 2), Fraction(7, 4), Fraction(-1, 3)],
         [Fraction(0), Fraction(-1, 3), Fraction(9, 5)]]
    assert certify.bareiss_positive_definite(M)


@pytest.mark.parametrize("m,k", [(4, 2), (5, 2), (3, 3)])
def test_certified_enclosure_brackets_float(m, k):
    basis = frames.monomial_basis(m, k)
    G = frames.gram_matrix(m, basis)
    K = frames.root_K(m, basis)
    cert = certify.certify_lambda_min(K, G)
    lo, hi = cert["lambda_lower_exact"], cert["lambda_upper_exact"]
    lam = cert["lambda_float"]
    assert lo is not None and Fraction(0) < lo < hi
    assert float(lo) <= lam * (1 + 1e-9)
    assert float(hi) >= lam * (1 - 1e-9)
    assert float(hi) - float(lo) <= 0.02 * float(hi)


def test_mixture_exact_linearity():
    basis = frames.monomial_basis(4, 2)
    Kr = frames.root_K(4, basis)
    Kv = frames.vertex_K(4, 2, basis)
    a = Fraction(3, 8)
    Km = frames.mixture_K(Kr, Kv, a)
    n = len(basis)
    for i in range(n):
        for j in range(n):
            assert Km[i][j] == a * Kr[i][j] + (1 - a) * Kv[i][j]


# ---------------------------------------------------------------------------------------
# Monte Carlo cross-checks of the exact chamber machinery (implementation validation only)
# ---------------------------------------------------------------------------------------

def test_vertex_exact_matches_mc_direction_estimate():
    m, k = 3, 2
    basis = frames.monomial_basis(m, k)
    Kv = frames.vertex_K(m, k, basis)
    Kv_f = np.array([[float(v) for v in row] for row in Kv])
    rng = np.random.default_rng(20260830)
    est = np.zeros_like(Kv_f)
    for i in range(m):
        u = -np.ones(m) / m
        u[i] += 1.0
        est += spherical.estimate_direction_form(m, k, basis, u, 30000, rng)
    est *= (m - 1) / m
    scale = np.max(np.abs(Kv_f))
    assert np.max(np.abs(est - Kv_f)) <= 0.05 * scale


def test_root_exact_matches_mc_direction_estimate():
    m, k = 3, 2
    basis = frames.monomial_basis(m, k)
    B12 = frames.root_single_direction_closed(m, basis)
    B12_f = np.array([[float(v) for v in row] for row in B12])
    u = np.array([1.0, -1.0, 0.0])
    rng = np.random.default_rng(7)
    est = spherical.estimate_direction_form(m, k, basis, u, 30000, rng)
    scale = np.max(np.abs(B12_f))
    assert np.max(np.abs(est - B12_f)) <= 0.05 * scale


def test_spherical_linear_anchor():
    m, k = 4, 2
    basis = frames.monomial_basis(m, k)
    G = frames.gram_matrix(m, basis)
    Gf = np.array([[float(v) for v in row] for row in G])
    A = spherical.spherical_frame_estimate(m, k, basis, 15000, 11)
    nlin = m - 1
    dev = np.max(np.abs(A[:nlin, :nlin] - Gf[:nlin, :nlin])) / np.max(np.abs(Gf[:nlin, :nlin]))
    assert dev <= 0.1


# ---------------------------------------------------------------------------------------
# run-level contract
# ---------------------------------------------------------------------------------------

def test_run_records_small_contract():
    res = ffd.run_records(
        seed=1, k2_ms=(3, 4), k2_root_extra_ms=(), k3_ms=(3,), k3_root_extra_ms=(),
        mixture_grid_denominator=4, spherical_k2_ms=(3,), spherical_k3_ms=(),
        spherical_samples=2000, do_certify=True)
    res.validate()
    kinds = {r["kind"] for r in res.records}
    assert {"calibration", "exact-frame-gap", "mixture-scan", "spherical-directional",
            "gap-table", "threshold-evaluation"} <= kinds
    assert res.summary["no_status_change"] is True
    # certified lower bounds exist and bracket the float values
    for r in res.records:
        if r["kind"] == "exact-frame-gap" and r["lambda_lower_exact"] is not None:
            assert float(Fraction(r["lambda_lower_exact"])) <= r["lambda_float"] * (1 + 1e-9)
            assert float(Fraction(r["lambda_upper_exact"])) >= r["lambda_float"] * (1 - 1e-9)
    # pre-registered thresholds are recorded verbatim in the config
    assert res.config["preregistered_thresholds"] == ffd.PREREGISTERED_THRESHOLDS
