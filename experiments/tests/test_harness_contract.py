"""Small end-to-end checks for the public target and artifact boundary."""
from __future__ import annotations

import json

import pytest

from numerics.__main__ import main
from numerics.contract import ARTIFACT_SCHEMA_VERSION, RunResult
from numerics.artifact import run
from numerics.targets import REGISTRY


def test_registry_has_explicit_metadata_and_standard_profiles():
    assert set(REGISTRY) == {
        "kls", "loc-engine", "kls-align", "cmh-gate-zero",
        "kls-screen", "fiber-frame-dual", "cmh-ab",
    }
    assert "kls-loc" not in REGISTRY
    for target, spec in REGISTRY.items():
        assert spec.id == target
        assert spec.summary
        assert "standard" in spec.profiles
        assert hasattr(spec.module, "run_records")
        assert hasattr(spec.module, "selftest")


def test_run_result_rejects_untyped_records():
    with pytest.raises(ValueError, match="string 'kind'"):
        RunResult([{"instance": "missing-kind"}]).validate()
    with pytest.raises(ValueError, match="runner-owned 'seed'"):
        RunResult([], config={"seed": 1}).validate()
    with pytest.raises(ValueError, match="runner-owned field"):
        RunResult([], summary={"kind": "wrong"}).validate()


def test_kls_run_writes_versioned_envelope_and_separate_summary(tmp_path):
    path = run("kls", seed=3, profile="standard", out=tmp_path / "kls.jsonl")
    lines = [json.loads(line) for line in path.read_text().splitlines()]
    header = lines[0]["_provenance"]
    assert header["schema_version"] == ARTIFACT_SCHEMA_VERSION
    assert header["target"] == "kls"
    assert header["config"] == {"seed": 3, "d": 4}
    assert lines[-1]["kind"] == "run-summary"
    assert lines[-1]["target"] == "kls"


def test_target_rejects_unknown_profile():
    with pytest.raises(ValueError, match="no profile"):
        REGISTRY["kls"].config_for("heavy")


def test_cli_requires_a_target_and_maps_the_legacy_localization_spelling(monkeypatch, tmp_path):
    with pytest.raises(SystemExit):
        main(["run"])

    called = {}

    def fake_run(target, seed, profile, out):
        called.update(target=target, seed=seed, profile=profile, out=out)
        return tmp_path / "artifact.jsonl"

    monkeypatch.setattr("numerics.artifact.run", fake_run)
    assert main(["run", "--target", "kls-loc", "--heavy", "--seed", "9"]) == 0
    assert called == {"target": "loc-engine", "seed": 9, "profile": "full", "out": None}
