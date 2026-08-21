"""Artifact writes are immutable and dirty provenance is evidence-ineligible."""

from __future__ import annotations

import json

import pytest

from finum import provenance as provenance_module


def test_write_jsonl_uses_exclusive_creation(tmp_path):
    path = tmp_path / "run.jsonl"
    provenance_module.write_jsonl(path, {"target": "test"}, [{"kind": "diagnostic"}])
    with pytest.raises(FileExistsError):
        provenance_module.write_jsonl(path, {"target": "test"}, [])

    lines = path.read_text().splitlines()
    assert json.loads(lines[0])["_provenance"]["target"] == "test"
    assert json.loads(lines[1])["kind"] == "diagnostic"


def test_dirty_run_is_marked_evidence_ineligible(monkeypatch):
    answers = {
        ("rev-parse", "HEAD"): "abc123",
        ("status", "--porcelain"): " M tracked.py",
    }
    monkeypatch.setattr(provenance_module, "_git", lambda *args: answers.get(args))
    header = provenance_module.provenance(target="test", seed=0)
    assert header["git_dirty"] is True
    assert header["evidence_eligible"] is False
