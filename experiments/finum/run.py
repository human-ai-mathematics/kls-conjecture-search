"""Dispatch a target run -> a provenance-stamped JSONL artifact in research/runs/.

The artifact is what a ledger node's `evidence_run:` points at. finum does NOT edit the
ledger; an agent reads the artifact and sets evidence/evidence_run (keeps numerics and
bookkeeping separate, soundness contract intact). Each target module owns its calibration-gate
and verdict logic in `run_records`.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

from .provenance import provenance, runs_dir, write_jsonl
from .targets import REGISTRY


def run(target: str, seed: int = 0, out: str | Path | None = None, **cfg) -> Path:
    """Run a target's battery; write the evidence_run artifact. Returns its path."""
    if target not in REGISTRY:
        raise ValueError(f"unknown target '{target}'; have {sorted(REGISTRY)}")
    records, extra = REGISTRY[target].run_records(seed, **cfg)
    header = provenance(target=target, seed=seed, **extra)
    if out is None:
        out = runs_dir() / f"{date.today().isoformat()}-{target}.jsonl"
    return write_jsonl(out, header, records)
