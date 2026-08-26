"""Exact regressions for A4's three local Gaussian regimes."""

import numpy as np

from finum.targets.a_series.a4 import gaussian_fixed_cov_local


def test_fixed_covariance_gaussian_local_formula_matches_endpoint_optimization():
    sigma = np.array([[2.0, 0.4], [0.4, 1.0]])
    fixed_covariance = np.array([[1.4, 0.2], [0.2, 0.7]])
    rho = 0.35
    result = gaussian_fixed_cov_local(sigma, fixed_covariance, rho)

    eigenvalues, eigenvectors = np.linalg.eigh(sigma)
    top_vector = eigenvectors[:, -1]
    inverse_sigma = np.linalg.inv(sigma)
    scale = np.sqrt(2.0 * rho / (top_vector @ inverse_sigma @ top_vector))
    endpoint_shift = scale * top_vector
    entropy_quadratic = endpoint_shift @ inverse_sigma @ endpoint_shift
    endpoint_transport = (
        result["covariance_w2"] + endpoint_shift @ endpoint_shift
    ) / (2.0 * result["delta"] + entropy_quadratic)
    endpoint_mean = (endpoint_shift @ endpoint_shift) / (
        2.0 * result["delta"] + entropy_quadratic
    )

    assert np.isclose(entropy_quadratic, 2.0 * rho)
    assert np.isclose(endpoint_transport, result["endpoint_transport"])
    assert np.isclose(
        result["raw_transport"],
        max(result["baseline_transport"], endpoint_transport),
    )
    assert np.isclose(endpoint_mean, result["raw_mean"])
    assert np.isclose(result["excess_transport"], eigenvalues[-1])
    assert np.isclose(result["excess_mean"], eigenvalues[-1])


def test_well_specified_gaussian_is_exact_at_every_positive_radius():
    sigma = np.array([[1.7, -0.3], [-0.3, 0.9]])
    result = gaussian_fixed_cov_local(sigma, sigma, rho=0.2)
    exact = np.max(np.linalg.eigvalsh(sigma))

    assert result["well_specified"]
    assert np.isclose(result["delta"], 0.0, atol=1e-12)
    assert np.isclose(result["covariance_w2"], 0.0, atol=1e-12)
    assert np.isclose(result["raw_transport"], exact)
    assert np.isclose(result["raw_mean"], exact)
    assert np.isclose(result["excess_transport"], exact)
