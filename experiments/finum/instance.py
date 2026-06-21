"""The shared, sample-based Instance type used by the per-target batteries.

A target module under finum/targets/ exposes CALIBRATION / STRESS generators returning
Instance objects (for sample-based targets: A1, A2, A5, KLS) and/or its own analytic
representation (A3 weighted-gap/Hardy on a grid, A4 transport ratios). The common contract a
target module satisfies is `run_records(seed) -> (records, extra_header)` and
`selftest(rng) -> [(name, ok), ...]`; see finum/run.py and finum/selftest.py.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable

import numpy as np


def sigmoid(s):
    return 0.5 * (1.0 + np.tanh(0.5 * s))


@dataclass
class Instance:
    id: str
    tier: str                       # "calibration" | "stress"
    obstruction: str | None
    sampler: Callable[[int, np.random.Generator], np.ndarray]
    exact: float | None = None      # ground-truth C_P if known
    prior_bound: float | None = None    # A1: lambda_max(Sigma0)
    bulk_bound: float | None = None     # A1: tail-free candidate
    note: str = ""
    meta: dict = field(default_factory=dict)

    def sample(self, n: int, rng: np.random.Generator) -> np.ndarray:
        return self.sampler(n, rng)
