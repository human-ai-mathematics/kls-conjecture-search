"""Dispatch a target run -> a provenance-stamped JSONL research artifact.

The artifact may be cited by a dated exploration, but it does not enter a claim node.
``finum`` does not edit the ledger, validate claims, or certify proofs; the artifact records
research direction only. Each target module owns its calibration gate and diagnostic logic in
``run_records``.
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from .provenance import provenance, runs_dir, write_jsonl
from .targets import REGISTRY


def run(target: str, seed: int = 0, out: str | Path | None = None, **cfg) -> Path:
    """Run a target's battery; write a directional research artifact. Return its path."""
    if target not in REGISTRY:
        raise ValueError(f"unknown target '{target}'; have {sorted(REGISTRY)}")
    records, extra = REGISTRY[target].run_records(seed, **cfg)
    header = provenance(target=target, seed=seed, **extra)
    if out is None:
        stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%S.%fZ")
        out = runs_dir() / f"{stamp}-{target}.jsonl"
    return write_jsonl(out, header, records)
