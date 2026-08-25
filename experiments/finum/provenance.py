"""Run provenance + repo paths: turn "committed + seeded" into reproducible.

Every artifact carries a header from ``provenance()`` (seed, run params, interpreter/library
versions, plus the current commit as a best-effort trace). A run that cannot be reproduced from
its recorded seed and params is not a result.
"""
from __future__ import annotations

import json
import platform
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Any

import numpy as np
import scipy


def repo_root() -> Path:
    """The repository root: the nearest ancestor holding both research/ and modules/,
    else `git rev-parse --show-toplevel`, else two levels up from this file."""
    here = Path(__file__).resolve()
    for p in here.parents:
        if (p / "research").is_dir() and (p / "modules").is_dir():
            return p
    top = _git("rev-parse", "--show-toplevel")
    if top:
        return Path(top)
    return here.parents[2]


def runs_dir() -> Path:
    """``research/runs/`` (created on demand), for directional research artifacts."""
    d = repo_root() / "research" / "runs"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _git(*args: str) -> str | None:
    try:
        out = subprocess.run(
            ["git", *args],
            cwd=Path(__file__).resolve().parent,
            capture_output=True, text=True, check=True,
        )
        return out.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def provenance(**params: Any) -> dict[str, Any]:
    """A JSON-serializable provenance header; pass run params (seed, n, d, ...) as keywords.

    ``git_commit`` is a best-effort trace of which checkout produced the artifact. It is
    informational: reproducibility rests on the recorded seed, params, and library versions,
    and nothing gates on the state of the worktree.
    """
    return {
        "date": date.today().isoformat(),
        "git_commit": _git("rev-parse", "HEAD"),
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "params": params,
    }


def write_jsonl(path: str | Path, header: dict, records: list[dict]) -> Path:
    """Write a ``.jsonl`` artifact: provenance header line, then one record per line.

    ``.jsonl`` (not ``.log``) so the repo's LaTeX .gitignore does not swallow it.
    """
    path = Path(path)
    if path.suffix == ".log":
        raise ValueError("use .jsonl for artifacts; the repo .gitignore eats *.log")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x") as fh:
        fh.write(json.dumps({"_provenance": header}) + "\n")
        for rec in records:
            fh.write(json.dumps(rec) + "\n")
    return path
