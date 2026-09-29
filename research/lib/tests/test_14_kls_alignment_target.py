"""Soundness and schema checks for the product q:alignment CLI target."""

import json

import numpy as np

from numerics.targets import REGISTRY
from numerics.targets.kls import alignment


def test_paired_gate_rejects_a_coarse_only_spike():
    intervals = np.array([[0.0, 0.1]])
    fine = {
        "S_high": np.zeros((4, 1)),
        "r": np.zeros((4, 1)),
        "D": np.zeros((4, 1)),
    }
    coarse = {
        "S_high": np.ones((4, 1)),
        "r": np.zeros((4, 1)),
        "D": np.zeros((4, 1)),
    }
    gate = alignment._paired_refinement_gate(
        fine, coarse, intervals,
        np.full(4, 0.1), np.full(4, 0.1),
        np.zeros(4, dtype=bool), np.zeros(4, dtype=bool),
        dt=0.01, alphas=(0.5,), C1=1.0,
    )
    assert gate["passed"] is False
    assert gate["components"]["S_high"]["worst_normalized_drift"] > 1.0
    assert gate["components"]["S_high-C1*r-0.5*D"]["worst_normalized_drift"] > 1.0


def test_kls_align_is_registered_and_remains_model_diagnostic():
    assert REGISTRY["kls-align"].module is alignment
    result = alignment.run_records(
        seed=4, ns=(8,), T=0.12, dt=0.02, n_paths=4,
        widths=(0.04, 0.08), alphas=(0.5, 0.9),
    )
    records, extra = result.records, result.summary
    config = next(r for r in records if r["kind"] == "alignment-configuration")
    scan = next(r for r in records if r["kind"] == "alignment-window-scan")
    summary = records[-1]

    assert config["target"] == "q:alignment"
    assert {g["gate"] for g in config["gates"]} >= {
        "initial_balance",
        "dynamic_closed_form_vs_quadrature",
        "mass_martingale",
        "pathwise_identities",
        "paired_dt_refinement",
    }
    dt_gate = next(g for g in config["gates"] if g["gate"] == "paired_dt_refinement")
    assert set(dt_gate["components"]) >= {
        "S_high", "r", "D", "S_high-C1*r-0.5*D", "tau_and_stop",
    }
    assert "empirical" in dt_gate["stopping_control"]
    # Selection and estimation use independent halves of the path ensemble.
    assert "heldout_positive_source_minus_alpha_D_over_length_plus_r" in (
        scan["alpha_margins_C1_fixed"]["0.5"]
    )
    assert scan["discovery_paths"] == 2
    assert scan["heldout_paths"] == 2
    assert "heldout_high_count_time_integral" in scan
    assert summary["diagnostic_only"] is True
    assert summary["proof_status"] == "no-proof/no-universal-conclusion"
    assert extra["route_observable_available"] is True
    assert extra["dynamic_quadrature_available"] is True
    # The full payload must be provenance-writer/JSON compatible.
    json.dumps(records)
