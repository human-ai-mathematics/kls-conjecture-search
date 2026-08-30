"""Oracle tests for the cut-scale / perimeter / screened-supply machinery (``kls-screen``).

Every check here compares the new O(n) code against either a dense brute-force evaluation,
the pre-existing scalar closed-form engine, or a closed form derived by hand.  Passing them
establishes implementation correctness only; it proves nothing about ``q:weighted``.
"""

import json

import numpy as np
import pytest

from finum.localization import screening as scr
from finum.localization.tail_union import (
    balanced_tail_radius,
    observe_tail_union,
    tilted_laplace_symmetric_truncation,
)
from finum.targets import REGISTRY
from finum.targets.kls import screening as target


_SQRT2 = float(np.sqrt(2.0))


def _random_state(n, t, rng, scale=0.8):
    c = np.zeros(n) if t == 0.0 else rng.normal(scale=scale, size=n)
    return c


# ---------------------------------------------------------------------------------------
# 1D tilted-marginal primitives against the pre-existing scalar engine
# ---------------------------------------------------------------------------------------


@pytest.mark.parametrize("t", [0.0, 1e-3, 0.05, 0.4, 2.0])
def test_vectorized_inside_mass_matches_scalar_truncation_engine(t):
    c = np.array([-2.4, -1.0, -0.2, 0.0, 0.3, 1.1, 2.9]) if t > 0 else np.zeros(7)
    radius = 1.7
    mar = scr.marginals(c, t)
    mine = scr.log_inside_mass(mar, np.full(c.size, radius))
    reference = np.array([
        tilted_laplace_symmetric_truncation(float(ci), t, radius).probability for ci in c
    ])
    # Compare in log space, away from the reference engine's underflow clamp: a strongly
    # tilted coordinate can put e^-1000 of its mass inside the cut radius.
    resolved = reference > 1e-250
    assert resolved.sum() >= 5
    gap = np.abs(mine[resolved] - np.log(reference[resolved]))
    assert np.all(gap <= 1e-11 * np.maximum(1.0, np.abs(np.log(reference[resolved]))))
    assert np.allclose(
        np.exp(mine[reference > 1e-8]), reference[reference > 1e-8], rtol=2e-12, atol=0.0
    )


@pytest.mark.parametrize("t", [0.0, 0.02, 0.4])
def test_survival_quantile_inverts_the_survival_function(t):
    c = np.array([-1.3, 0.0, 0.9]) if t > 0 else np.zeros(3)
    mar = scr.marginals(c, t)
    for p in (0.5, 0.2, 1e-3, 1e-6):
        b = scr.survival_quantile(mar, np.log(p))
        assert np.allclose(np.exp(scr.log_survival(mar, b)), p, rtol=1e-10, atol=0.0)


def test_untilted_marginal_reproduces_the_laplace_closed_forms():
    mar = scr.marginals(np.zeros(3), 0.0)
    # density at zero is 1/sqrt(2); median is zero; P(|X|<a) = 1-exp(-sqrt(2) a)
    assert np.allclose(np.exp(scr.log_density(mar, np.zeros(3))), 1.0 / _SQRT2, rtol=1e-14)
    assert np.allclose(scr.survival_quantile(mar, np.log(0.5)), 0.0, atol=1e-13)
    a = 0.9
    assert np.allclose(
        np.exp(scr.log_inside_mass(mar, np.full(3, a))), 1.0 - np.exp(-_SQRT2 * a), rtol=1e-14
    )


# ---------------------------------------------------------------------------------------
# lambda_cut: the O(n) diagonal + cross + rank-one split versus the dense double sum
# ---------------------------------------------------------------------------------------


def test_cauchy_quadratic_form_matches_the_dense_double_sum():
    rng = np.random.default_rng(7)
    g = np.abs(rng.normal(size=37))
    g[5:9] = 0.0
    a = 0.2 + np.abs(rng.normal(size=37))
    dense = float(np.sum(np.outer(g, g) / (a[:, None] + a[None, :])))
    for block_size in (1, 4, 37, 1000):
        assert scr.cauchy_quadratic_form(g, a, block_size=block_size) == pytest.approx(
            dense, rel=1e-13
        )


@pytest.mark.parametrize("t", [0.0, 0.05, 0.3, 1.0])
def test_lambda_cut_decomposition_matches_the_dense_n8_double_sum(t):
    n = 8
    radius = balanced_tail_radius(n)
    rng = np.random.default_rng(20260830)
    for _ in range(6):
        c = _random_state(n, t, rng)
        state = scr.screened_state(c, t, radius)
        K = scr.dense_cut_tensor(state.k_diagonal, state.delta, state.p)
        dense = scr.dense_cut_scale(state.A, K)
        assert state.lambda_cut == pytest.approx(dense, rel=1e-12, abs=1e-14)
        # the emitted weight is the probe's (1+lambda_cut)^{5/2}
        assert state.W_cut == pytest.approx((1.0 + dense) ** 2.5, rel=1e-12)


def test_hilbert_schmidt_norm_matches_the_dense_tensor():
    n = 11
    t = 0.2
    radius = balanced_tail_radius(n)
    rng = np.random.default_rng(3)
    state = scr.screened_state(rng.normal(scale=0.8, size=n), t, radius)
    K = scr.dense_cut_tensor(state.k_diagonal, state.delta, state.p)
    assert state.hs_norm_sq == pytest.approx(float(np.sum(K * K)), rel=1e-13)


def test_lambda_cut_is_bracketed_by_the_covariance_spectrum():
    n = 24
    t = 0.15
    radius = balanced_tail_radius(n)
    rng = np.random.default_rng(11)
    for _ in range(5):
        state = scr.screened_state(rng.normal(scale=1.1, size=n), t, radius)
        assert state.lambda_min - 1e-13 <= state.lambda_cut <= state.lambda_max + 1e-13


def test_scalar_covariance_gives_lambda_cut_equal_to_the_common_variance():
    """Probe eq. (9): ``lambda_cut(sigma^2 I, K) = sigma^2`` for every nonzero ``K``."""

    rng = np.random.default_rng(5)
    sigma2 = 0.37
    a = np.full(9, sigma2)
    scale = scr.cut_scale(a, rng.normal(size=9), np.abs(rng.normal(size=9)), 0.4)
    assert scale.lambda_cut == pytest.approx(sigma2, rel=1e-13)


def test_aligned_two_tail_calibration_returns_the_spike():
    """Probe eq. (11): ``A=diag(Lambda,1,..,1)``, ``K = const * e1 e1^T`` gives ``Lambda``."""

    for Lambda in (1.0, 5.0, 250.0):
        a = np.concatenate([[Lambda], np.ones(6)])
        k_diagonal = np.zeros(7)
        k_diagonal[0] = 3.5
        scale = scr.cut_scale(a, k_diagonal, np.zeros(7), 0.5)
        assert scale.lambda_cut == pytest.approx(Lambda, rel=1e-13)


def test_cross_block_leakage_identity_is_reproduced():
    """Probe eq. (8): ``lambda_cut(diag(1,L), eps*(e12+e21)) = (1+L)/2`` for every eps != 0."""

    for L in (1.0, 10.0, 1e4):
        for eps in (1e-9, 1.0):
            K = np.array([[0.0, eps], [eps, 0.0]])
            assert scr.dense_cut_scale(np.array([1.0, L]), K) == pytest.approx(
                0.5 * (1.0 + L), rel=1e-13
            )


# ---------------------------------------------------------------------------------------
# weighted perimeter and profile competitors
# ---------------------------------------------------------------------------------------


@pytest.mark.parametrize("n", [1, 2, 8, 64])
def test_untilted_perimeter_matches_its_closed_form(n):
    radius = balanced_tail_radius(n)
    mar = scr.marginals(np.zeros(n), 0.0)
    expected = 0.5 * n * _SQRT2 * (2.0 ** (1.0 / n) - 1.0)
    assert scr.tail_union_perimeter(mar, radius) == pytest.approx(expected, rel=1e-12)


@pytest.mark.parametrize("t", [0.0, 0.1, 0.5])
def test_perimeter_matches_the_finite_difference_minkowski_content(t):
    n = 12
    radius = balanced_tail_radius(n)
    rng = np.random.default_rng(99)
    c = _random_state(n, t, rng)
    exact = scr.tail_union_perimeter(scr.marginals(c, t), radius)
    estimate = scr.minkowski_perimeter_estimate(c, t, radius, 1e-5)
    assert exact == pytest.approx(estimate, rel=1e-8)


def test_block_perimeter_ignores_spectator_coordinates():
    n0, n = 5, 23
    radius = balanced_tail_radius(n0)
    rng = np.random.default_rng(4)
    base = rng.normal(scale=0.9, size=n0)
    full = np.concatenate([base, rng.normal(scale=0.9, size=n - n0)])
    t = 0.2
    assert scr.tail_union_perimeter(scr.marginals(full, t), radius, block=n0) == pytest.approx(
        scr.tail_union_perimeter(scr.marginals(base, t), radius), rel=1e-13
    )


@pytest.mark.parametrize("n", [2, 8, 64, 256])
def test_equal_tail_competitor_reproduces_the_cut_at_time_zero(n):
    radius = balanced_tail_radius(n)
    mar = scr.marginals(np.zeros(n), 0.0)
    perimeter = scr.tail_union_perimeter(mar, radius)
    assert scr.equal_tail_product_bound(mar, 0.5) == pytest.approx(perimeter, rel=1e-11)
    surrogate = scr.profile_surrogate(mar, 0.5, radius)
    assert surrogate.excess_rich == pytest.approx(0.0, abs=1e-11)


@pytest.mark.parametrize("n", [2, 8, 256])
def test_halfline_competitor_alone_is_worse_than_the_balanced_tail_union_cut(n):
    """Documents why the clamp in ``ehat=(P-Ihat)_+`` is active for the half-line family."""

    radius = balanced_tail_radius(n)
    mar = scr.marginals(np.zeros(n), 0.0)
    perimeter = scr.tail_union_perimeter(mar, radius)
    assert scr.halfline_profile_bound(mar, 0.5) == pytest.approx(1.0 / _SQRT2, rel=1e-10)
    assert perimeter < 1.0 / _SQRT2
    assert scr.profile_surrogate(mar, 0.5, radius).excess_halfline == 0.0


def test_surrogate_excess_never_exceeds_the_perimeter_and_stays_nonnegative():
    n = 16
    radius = balanced_tail_radius(n)
    rng = np.random.default_rng(21)
    for t in (0.05, 0.25, 0.6):
        state = scr.screened_state(rng.normal(scale=1.0, size=n), t, radius)
        s = state.surrogate
        assert 0.0 <= s.excess_rich <= s.perimeter + 1e-12
        assert s.excess_halfline <= s.excess_rich + 1e-12  # richer family, larger surrogate
        assert s.rich_bound <= s.halfline_bound + 1e-12


# ---------------------------------------------------------------------------------------
# consistency with the pre-existing tail-union engine, and the spectator direct sum
# ---------------------------------------------------------------------------------------


@pytest.mark.parametrize("t", [0.0, 0.07, 0.5])
def test_two_colour_observables_reproduce_the_reference_engine(t):
    n = 20
    radius = balanced_tail_radius(n)
    rng = np.random.default_rng(1234)
    c = _random_state(n, t, rng)
    mine = scr.screened_state(c, t, radius)
    reference = observe_tail_union(c, t, radius)
    assert mine.p == pytest.approx(reference.p, rel=1e-14)
    assert mine.S == pytest.approx(reference.S, rel=1e-13)
    assert mine.S_high == pytest.approx(reference.S_high, rel=1e-13)
    assert mine.r == pytest.approx(reference.r, rel=1e-13)
    assert mine.D == pytest.approx(reference.D, rel=1e-13)
    assert np.allclose(mine.delta, reference.delta, rtol=1e-13)


@pytest.mark.parametrize("n", [40, 200])
def test_cylinder_cut_lambda_cut_is_exactly_the_base_block_value(n):
    n0 = 8
    radius = balanced_tail_radius(n0)
    rng = np.random.default_rng(66)
    base = rng.normal(scale=0.9, size=n0)
    for t in (0.0, 0.12, 0.45):
        spectators = np.zeros(n - n0) if t == 0.0 else rng.normal(scale=0.9, size=n - n0)
        full = scr.screened_state(np.concatenate([base, spectators]), t, radius, block=n0)
        base_only = scr.screened_state(base, t, radius)
        assert abs(full.lambda_cut - base_only.lambda_cut) <= 1e-10
        assert full.p == pytest.approx(base_only.p, rel=1e-14)
        assert full.Q == pytest.approx(base_only.Q, rel=1e-13)
        # the spectator rows/columns of K vanish exactly
        assert np.all(full.delta[n0:] == 0.0)
        assert np.all(full.k_diagonal[n0:] == 0.0)
        assert full.surrogate.excess_rich_block == pytest.approx(
            base_only.surrogate.excess_rich, rel=1e-11, abs=1e-14
        )


def test_cylinder_lambda_cut_matches_a_dense_full_dimensional_evaluation():
    n0, n = 5, 30
    radius = balanced_tail_radius(n0)
    rng = np.random.default_rng(2)
    c = rng.normal(scale=0.8, size=n)
    state = scr.screened_state(c, 0.25, radius, block=n0)
    dense = scr.dense_cut_scale(
        state.A, scr.dense_cut_tensor(state.k_diagonal, state.delta, state.p)
    )
    assert state.lambda_cut == pytest.approx(dense, rel=1e-12)


# ---------------------------------------------------------------------------------------
# target-level schema and epistemic labelling
# ---------------------------------------------------------------------------------------


def test_kls_screen_is_registered_and_stays_diagnostic_only():
    assert REGISTRY["kls-screen"].module is target
    assert set(REGISTRY["kls-screen"].profiles) >= {"smoke", "standard", "high-n"}
    result = target.run_records(
        seed=5, ns=(8,), T=0.1, dt=0.01, snapshot_stride=2, n_paths=4,
        kappas=(0.05, 1.0), widths=(0.02,),
        spectator_ns=(12, 20), spectator_n0=4, spectator_paths=2, spectator_stride=5,
    )
    kinds = {r["kind"] for r in result.records}
    assert kinds >= {
        "screen-preregistration", "screen-configuration", "screen-trajectory",
        "screen-window", "screen-joint-occurrence", "screen-spectator", "screen-summary",
    }
    prereg = result.records[0]
    assert prereg["decision_rule"]["fixed_before_run"] is True
    assert prereg["decision_rule"]["screening_kappa_of_record"] == 0.05

    config = next(r for r in result.records if r["kind"] == "screen-configuration")
    assert {g["gate"] for g in config["gates"]} >= {
        "initial_balance",
        "mass_vectorized_vs_scalar_engine",
        "lambda_cut_bracket",
        "two_colour_vs_reference_engine",
        "lambda_cut_decomposition_vs_dense",
        "perimeter_vs_minkowski_finite_difference",
        "mass_martingale",
        "snapshot_stride_refinement",
    }
    summary = result.records[-1]
    assert summary["diagnostic_only"] is True
    assert summary["proof_status"] == "no-proof/no-universal-conclusion"
    assert summary["verdict"]["outcome"] in {
        "directional-support", "directional-against", "inconclusive",
    }
    assert result.summary["excess_is_surrogate"] is True
    assert result.summary["surrogate_direction"] == "understates the true excess"
    assert {g["gate"] for g in summary["spectator_gates"]} == {
        "spectator_lambda_cut_block_invariance",
        "spectator_pathwise_block_supply_invariance",
        "spectator_all_coordinate_family_paired_drift",
    }
    reported = next(
        g for g in summary["spectator_gates"]
        if g["gate"] == "spectator_all_coordinate_family_paired_drift"
    )
    assert reported["passed"] is None and reported["paired_statistics"]
    json.dumps(result.records)


def test_screen_window_records_carry_theta_hat_for_every_kappa():
    result = target.run_records(
        seed=6, ns=(6,), T=0.08, dt=0.01, snapshot_stride=2, n_paths=4,
        kappas=(0.05, 0.25), widths=(0.02,),
        spectator_ns=(8, 10), spectator_n0=3, spectator_paths=2, spectator_stride=4,
    )
    window = next(r for r in result.records if r["kind"] == "screen-window")
    for label in ("S_H_pulse", "supply_peak"):
        assert "selected_interval" in window[label]
        for kappa in ("0.05", "0.25"):
            assert "heldout_theta_hat" in window[label][f"kappa@{kappa}"]
            assert "heldout_aligned_supply_integral" in window[label][f"kappa@{kappa}"]


def test_kls_align_target_records_are_untouched_by_the_sibling():
    """The screening target must not perturb the pre-existing alignment schema."""

    from finum.targets.kls import alignment

    records = alignment.run_records(
        seed=4, ns=(8,), T=0.12, dt=0.02, n_paths=4, widths=(0.04,), alphas=(0.5,),
    ).records
    config = next(r for r in records if r["kind"] == "alignment-configuration")
    assert config["target"] == "q:alignment"
    assert {g["gate"] for g in config["gates"]} == {
        "initial_balance", "dynamic_closed_form_vs_quadrature", "mass_martingale",
        "pathwise_identities", "paired_dt_refinement",
    }
