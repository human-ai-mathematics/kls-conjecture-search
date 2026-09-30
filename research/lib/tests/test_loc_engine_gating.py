"""Focused soundness tests for the diagnostic-only ``loc-engine`` target.

The target does not yet compute the observables in conj:product-alignment or conj:taming.  These tests pin the
contract that missing/red numerical gates cannot accidentally turn its engine diagnostics into a
route conclusion, and that even an all-green diagnostic remains unavailable.
"""

from __future__ import annotations

import json

import numerics.localization as localization
from numerics.localization.gates import GateResult
from numerics.localization.observables import EnsembleResult
from numerics.targets.kls import loc_engine as target


def _gate(name: str, passed: bool) -> GateResult:
    return GateResult(name, passed, 0.0 if passed else 1.0, 0.5, "test gate")


def _result(n: int = 2) -> EnsembleResult:
    return EnsembleResult(mean=0.4, stderr=0.01, n_paths=4, label=f"xi_S(n={n})")


def _patch_common(monkeypatch, *, calibration: bool = True, bins: bool = True):
    monkeypatch.setattr(
        target, "_gaussian_covariance_max_err",
        lambda *args, **kwargs: 0.0 if calibration else 1.0,
    )
    monkeypatch.setattr(target, "_balanced_thinshell", lambda n: (object(), object()))
    monkeypatch.setattr(target, "n_bins_convergence",
                        lambda *args, **kwargs: _gate("n_bins_convergence", bins))
    monkeypatch.setattr(target, "_occupation_xi_S",
                        lambda n, *args, **kwargs: _result(n))


def _assert_diagnostic_only(records):
    payload = json.dumps(records)
    assert "supports_taming" not in payload
    assert all(rec.get("kind") != "verdict" for rec in records)
    for rec in records:
        if "assessment" in rec:
            assert rec["assessment"]["evidence"] == "directional"
            assert rec["assessment"]["outcome"] == "inconclusive"


def _thinshell(records):
    # These records test no claim — the route observables are not implemented — so the
    # contract keeps them as auxiliary data under `case` rather than `instance`.
    return next(rec for rec in records if rec.get("case") == "thinshell-n2")


def test_failed_calibration_short_circuits_all_downstream_gates(monkeypatch):
    _patch_common(monkeypatch, calibration=False)
    monkeypatch.setattr(target, "_balanced_thinshell",
                        lambda n: (_ for _ in ()).throw(AssertionError("must not build cut")))

    result = target.run_records(ns=(2,), heavy=True)
    records, extra = result.records, result.summary

    rec = _thinshell(records)
    assert rec["gate_calibration"]["passed"] is False
    assert rec["gate_n_bins"]["status"] == "not-run"
    assert rec["gate_n_bins"]["gate"] == "initial_n_bins_convergence"
    assert rec["gate_fft_vs_mc"]["status"] == "not-run"
    assert rec["gate_fft_vs_mc"]["gate"] == "initial_fft_vs_mc"
    assert rec["gate_dt_refinement"]["status"] == "not-run"
    assert extra["route_comparison_available"] is False
    _assert_diagnostic_only(records)


def test_red_n_bins_gate_skips_fft_and_dt(monkeypatch):
    _patch_common(monkeypatch, bins=False)
    monkeypatch.setattr(
        localization, "fft_vs_mc",
        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("must not run FFT/MC")),
    )
    monkeypatch.setattr(
        target, "_dt_refinement_gate",
        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("must not refine dt")),
    )

    records = target.run_records(ns=(2,), heavy=True).records

    rec = _thinshell(records)
    assert rec["gate_n_bins"]["passed"] is False
    assert rec["gate_fft_vs_mc"]["status"] == "not-run"
    assert rec["gate_dt_refinement"]["status"] == "not-run"
    _assert_diagnostic_only(records)


def test_missing_or_red_fft_gate_cannot_reach_dt(monkeypatch):
    _patch_common(monkeypatch)
    monkeypatch.setattr(
        target, "_dt_refinement_gate",
        lambda *args, **kwargs: (_ for _ in ()).throw(AssertionError("must not refine dt")),
    )

    missing_records = target.run_records(ns=(2,), heavy=False).records
    missing = _thinshell(missing_records)
    assert missing["gate_fft_vs_mc"]["status"] == "not-run"
    assert missing["gate_dt_refinement"]["status"] == "not-run"
    _assert_diagnostic_only(missing_records)

    monkeypatch.setattr(localization, "fft_vs_mc",
                        lambda *args, **kwargs: _gate("fft_vs_mc", False))
    red_records = target.run_records(ns=(2,), heavy=True).records
    red = _thinshell(red_records)
    assert red["gate_fft_vs_mc"]["status"] == "run"
    assert red["gate_fft_vs_mc"]["passed"] is False
    assert red["gate_dt_refinement"]["status"] == "not-run"
    _assert_diagnostic_only(red_records)


def test_red_dt_and_all_green_runs_both_remain_no_verdict(monkeypatch):
    _patch_common(monkeypatch)
    monkeypatch.setattr(localization, "fft_vs_mc",
                        lambda *args, **kwargs: _gate("fft_vs_mc", True))

    red_dt = target._gate_record("dt_refinement", False, 1.0, 0.5, "test red")
    monkeypatch.setattr(target, "_dt_refinement_gate",
                        lambda *args, **kwargs: (red_dt, _result()))
    red_records = target.run_records(ns=(2,), heavy=True).records
    red = _thinshell(red_records)
    red_summary = next(rec for rec in red_records if rec["kind"] == "diagnostic-summary")
    assert red["gate_dt_refinement"]["passed"] is False
    assert red["assessment"]["gates_passed"] is False
    assert "2" not in red_summary["gated_normalized_budget_by_n"]
    _assert_diagnostic_only(red_records)

    green_dt = target._gate_record("dt_refinement", True, 0.0, 0.5, "test green")
    monkeypatch.setattr(target, "_dt_refinement_gate",
                        lambda *args, **kwargs: (green_dt, _result()))
    result = target.run_records(ns=(2,), heavy=True)
    green_records, extra = result.records, result.summary
    green = _thinshell(green_records)
    summary = next(rec for rec in green_records if rec["kind"] == "diagnostic-summary")
    assert green["assessment"]["gates_passed"] is True
    assert green["assessment"]["outcome"] == "inconclusive"
    assert summary["assessment"]["outcome"] == "inconclusive"
    assert "not built" in summary["assessment"]["reason"]
    assert extra["diagnostic_only"] is True
    assert extra["route_observable_available"] is False
    assert extra["dynamic_quadrature_available"] is False
    _assert_diagnostic_only(green_records)
