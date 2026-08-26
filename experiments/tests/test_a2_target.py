import numpy as np

from finum.targets.a_series.a2 import _endpoint_error_summary, gaussian_prior_tail_tradeoff


def test_bvm_endpoint_diagnostic_uses_distance_to_target():
    # The historical sweep decreases toward the target overall, but is non-monotone at the end.
    summary = _endpoint_error_summary(
        [(60, 12.596), (120, 10.718), (240, 7.004), (480, 7.649)],
        target=6.603,
    )

    assert summary["endpoint_closer_to_target"]
    assert summary["final_abs_error"] < summary["initial_abs_error"]


def test_bvm_endpoint_diagnostic_can_approach_from_below():
    summary = _endpoint_error_summary([(60, 2.0), (480, 5.5)], target=6.0)

    assert summary["endpoint_closer_to_target"]


def test_gaussian_prior_tail_tradeoff_separates_negligible_and_fisher_scale_priors():
    n = 10_000
    negligible = gaussian_prior_tail_tradeoff(n, n ** -0.5 * np.eye(2))
    fisher_scale = gaussian_prior_tail_tradeoff(n, n ** -1.0 * np.eye(2))

    # Sigma_n^{-1}/n -> 0 leaves the prior locally negligible, but n*C_global diverges.
    assert negligible["relative_precision_max"] == n ** -0.5
    assert negligible["n_global_lsi_t2_constant"] == n ** 0.5

    # A global O(1/n) constant requires order-n prior precision, changing local information.
    assert fisher_scale["n_global_lsi_t2_constant"] == 1.0
    assert fisher_scale["relative_precision_min"] == 1.0
