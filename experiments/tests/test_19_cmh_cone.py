"""Oracle tests for the exponential-cone CMH target (`cmh-cone`).

Every anchor here is a closed form from `modules/kls/42-cmh-exact-cases.tex`
(subsec:cmh-cones) or an identity the construction must satisfy for its own reasons
(Stein normalisation, affine invariance of the pencil, the Bochner identity).  A green
suite calibrates the implementation; it establishes no mathematical claim.
"""
from __future__ import annotations

from fractions import Fraction

import pytest

from numerics.targets.kls.cmh_cone import bases, gate, linalg as la


def cube_closed_form(n: int, beta: int):
    """cor:cube-cone-gate-zero: the exact normalized gate spectrum of a cube cone."""
    axis = Fraction(beta + n, beta)
    transverse = Fraction(6 * beta * beta + 11 * beta + 5 * n + 4, 5 * beta * (beta + 1))
    return axis, transverse


@pytest.mark.parametrize("m", [1, 2, 3, 4, 7])
def test_stein_normalisation_holds_exactly_for_every_base(m):
    for base in (bases.cube(m), bases.simplex(m),
                 bases.product_base(simplex_dims=(m,), intervals=0)):
        tau = base.tau()
        cov = base.cov()
        for i in range(base.m):
            for j in range(base.m):
                got = sum((c * base.moment(b) for (_, b), c in tau[i][j].items()),
                          Fraction(0))
                assert got == cov[i][j], (base.name, i, j, got, cov[i][j])


@pytest.mark.parametrize("n,beta", [(2, 2), (3, 3), (3, 4), (4, 4), (5, 10), (8, 40)])
def test_cube_cone_gate_matrix_matches_the_closed_form_exactly(n, beta):
    base = bases.cube(n - 1)
    M, Sigma = gate.gate_pencil(base, beta)
    axis, transverse = cube_closed_form(n, beta)
    assert M[0][0] == axis * Sigma[0][0]
    for i in range(1, n):
        assert M[0][i] == 0 and M[i][0] == 0
        for j in range(1, n):
            assert M[i][j] == transverse * Sigma[i][j]


@pytest.mark.parametrize("n", [2, 3, 4, 5])
def test_simplex_cone_at_beta_equals_n_is_an_exponential_product(n):
    """beta = n over Delta_{n-1}: S P_i are i.i.d. Exp(1), so M == 2 Sigma exactly."""
    M, Sigma = gate.gate_pencil(bases.simplex(n - 1), n)
    assert M == [[2 * x for x in row] for row in Sigma]


def test_delta_one_block_and_interval_block_give_the_same_pencil_spectrum():
    """Delta_1 is an affine copy of [-1,1]; the pencil is affine invariant."""
    for beta in (3, 4, 6):
        a = gate.gate_pencil(bases.product_base(simplex_dims=(1, 1), intervals=0), beta)
        b = gate.gate_pencil(bases.cube(2), beta)
        va, _ = gate.pencil_spectrum(*a)
        vb, _ = gate.pencil_spectrum(*b)
        assert max(abs(x - y) for x, y in zip(sorted(va), sorted(vb))) < 1e-12


# --------------------------------------------------------------------------------------
# the ball base (quadrature; directional)
# --------------------------------------------------------------------------------------

def test_ball_radial_ode_reproduces_the_one_dimensional_closed_form():
    from numerics.targets.kls.cmh_cone import ball
    profile = ball.radial_profile(1)
    assert abs(profile["R"] - 2.0) < 1e-10
    assert ball.one_dimensional_kernel_residual(profile) < 1e-9
    assert ball.stein_trace_residual(profile) < 1e-10


@pytest.mark.parametrize("m", [1, 2, 3, 5, 10])
def test_ball_radial_ode_satisfies_the_stein_normalisation(m):
    from numerics.targets.kls.cmh_cone import ball
    assert ball.stein_trace_residual(ball.radial_profile(m)) < 1e-9


@pytest.mark.parametrize("beta", [2, 3, 5])
def test_ball_cone_at_m_one_matches_the_cube_cone_closed_form(beta):
    """m = 1: the ball IS an interval, so channel 3 must reproduce channel 1 at n = 2."""
    from numerics.targets.kls.cmh_cone import ball
    ratios = ball.gate_ratios(ball.radial_profile(1), beta)
    _, transverse = cube_closed_form(2, beta)
    assert abs(ratios["transverse"] - float(transverse)) < 1e-9


# --------------------------------------------------------------------------------------
# channel 4 -- the CMH Galerkin quotient
# --------------------------------------------------------------------------------------

def _galerkin(base, beta, degree):
    from numerics.targets.kls.cmh_cone import galerkin, polys
    mom = polys.ConeMoments(base, beta)
    return galerkin, mom, galerkin.assemble(base, beta, degree, mom)


@pytest.mark.parametrize("n,beta", [(2, 2), (3, 3), (3, 5), (4, 4)])
def test_linear_axis_test_function_gives_one_plus_n_over_beta_exactly(n, beta):
    base = bases.cube(n - 1)
    _, _, built = _galerkin(base, beta, 1)
    axis = built["exponents"].index(tuple([1] + [0] * (n - 1)))
    v = [Fraction(0)] * built["basis_size"]
    v[axis] = Fraction(1)
    num = la.quadratic(built["N"], v)
    den = la.quadratic(built["D"], v)
    assert den == Fraction(beta)
    assert num / den == Fraction(beta + n, beta)


@pytest.mark.parametrize("n,beta", [(2, 2), (3, 3), (3, 4)])
def test_degree_one_galerkin_reproduces_the_gate_pencil(n, beta):
    base = bases.cube(n - 1)
    _, _, built = _galerkin(base, beta, 1)
    M, Sigma = gate.gate_pencil(base, beta)
    order = [built["exponents"].index(tuple(1 if k == i else 0 for k in range(n)))
             for i in range(n)]
    for a in range(n):
        for b in range(n):
            assert built["N"][order[a]][order[b]] == M[a][b]
            assert built["D"][order[a]][order[b]] == Sigma[a][b]


@pytest.mark.parametrize("n,beta,degree", [(2, 2, 3), (3, 3, 2), (2, 4, 3)])
def test_bochner_identity_holds_exactly_on_the_polynomial_test_space(n, beta, degree):
    base = bases.cube(n - 1)
    mod, mom, built = _galerkin(base, beta, degree)
    for i in range(built["basis_size"]):
        v = [Fraction(0)] * built["basis_size"]
        v[i] = Fraction(1)
        assert mod.bochner_residual(built, mom, v) == 0
    mixed = [Fraction(1 + (7 * i) % 5, 3 + i % 4) for i in range(built["basis_size"])]
    assert mod.bochner_residual(built, mom, mixed) == 0


def test_exponential_product_cone_galerkin_climbs_toward_four_from_below():
    """n = 2, beta = 2 is a product of two centered exponentials: C_CMH = 4 exactly."""
    base = bases.cube(1)
    previous = 0.0
    for degree in (2, 3, 4, 5):
        mod, _, built = _galerkin(base, 2, degree)
        vals, _, _ = mod.top_eigenpair(built["N"], built["D"])
        top = float(vals[-1])
        assert top <= 4.0 + 1e-9
        assert top > previous - 1e-12
        previous = top
    assert previous > 2.5     # the degree-5 space already sees well past the linear sector


# --------------------------------------------------------------------------------------
# the target as a whole
# --------------------------------------------------------------------------------------

def test_run_records_on_a_reduced_battery_is_well_formed_and_calibrated():
    from numerics.targets.kls import cmh_cone
    result = cmh_cone.run_records(
        cube_ns=(2, 3), cube_beta_rules=("n", "2n"), product_max_m=3,
        product_beta_rules=("n",), ball_ms=(1, 2),
        galerkin_specs=(("cube", 1, "n", (2, 3)), ("simplex", 2, "n", (2,))))
    result.validate()
    assert result.summary["calibration_passed"] is True
    assert result.summary["gate_sharp_exact_exceedance_instances"] == []
    assert result.summary["galerkin_exact_exceedance_instances"] == []
    kinds = {record["kind"] for record in result.records}
    assert {"calibration", "cone-gate-pencil", "cone-ball-gate",
            "cone-cmh-galerkin", "summary"} <= kinds
    for record in result.records:
        if record.get("kind") == "cone-gate-pencil":
            certificate = record["detail"]["certificate"]
            assert certificate["certificate_type"] == "exact-rational-loewner-pencil"
            assert certificate["arithmetic"] == "fractions.Fraction"


def test_exact_certificates_are_rejected_when_they_do_not_match():
    from numerics.targets.kls.cmh_cone import exact as cone_exact
    M, Sigma = gate.gate_pencil(bases.cube(2), 3)
    _, spectrum = gate.pencil_spectrum(M, Sigma)
    top = gate.rationalize(spectrum, 1000)
    lower, is_psd, certificate = cone_exact.pencil_certificate(M, Sigma, Fraction(2), top,
                                                              {"instance": "probe"})
    assert is_psd and lower <= 2
    with pytest.raises(ValueError):
        cone_exact.compare_exact_fraction("x <= 2", "probe", Fraction(2),
                                          lower + 1, certificate)
    with pytest.raises(ValueError):
        cone_exact.compare_exact_fraction("x <= 2", "probe", Fraction(2), lower,
                                          {**certificate, "certificate_type": "guess"})


@pytest.mark.parametrize("kind,parameter,beta,n", [("cube", 1, 2, 2), ("simplex", 1, 2, 2),
                                                  ("simplex", 2, 3, 3),
                                                  ("simplex", 3, 4, 4)])
def test_exponential_product_cones_hit_the_laguerre_closed_form(kind, parameter, beta, n):
    """2 + 2 cos(pi/(d+1)): the same anchor in every dimension, by affine invariance."""
    from numerics.targets.kls.cmh_cone import galerkin as galerkin_mod
    base = bases.cube(parameter) if kind == "cube" else bases.simplex(parameter)
    for degree in (2, 3, 4):
        _, _, built = _galerkin(base, beta, degree)
        vals, _, _ = galerkin_mod.top_eigenpair(built["N"], built["D"])
        want = galerkin_mod.exponential_product_galerkin_value(degree)
        assert abs(float(vals[-1]) - want) <= 1e-9 * want


def test_cube_cones_stay_strictly_below_the_exponential_product_anchor():
    """The non-product cube cone is not more extremal than the saturating product."""
    from numerics.targets.kls.cmh_cone import galerkin as galerkin_mod
    for n in (3, 4):
        for degree in (2, 3, 4):
            _, _, built = _galerkin(bases.cube(n - 1), n, degree)
            vals, _, _ = galerkin_mod.top_eigenpair(built["N"], built["D"])
            assert float(vals[-1]) < galerkin_mod.exponential_product_galerkin_value(degree)


@pytest.mark.slow
def test_full_standard_battery_runs_and_stays_calibrated():
    """The shipped `standard` profile end to end, including the ball quadrature channel."""
    from numerics.targets.kls import cmh_cone
    result = cmh_cone.run_records()
    result.validate()
    assert result.summary["calibration_passed"] is True
    assert result.summary["gate_sharp_exact_exceedance_instances"] == []
    assert result.summary["gate_zero_exact_exceedance_instances"] == []
    assert result.summary["galerkin_exact_exceedance_instances"] == []
    assert result.summary["ball_directional_exceedance_instances"] == []
