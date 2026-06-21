"""Self-test: every target's calibration must reproduce its closed-form ground truth, and the
sound refuters must fire. `python -m finum selftest` exits 0 iff all checks pass — finum's own
"definition of done": if calibration cannot be reproduced, no run may emit a verdict.
"""
from __future__ import annotations

import sys

import numpy as np

from .targets import REGISTRY


def selftest(verbose: bool = True) -> int:
    rng = np.random.default_rng(7)
    fails: list[str] = []
    for name, mod in REGISTRY.items():
        if not hasattr(mod, "selftest"):
            continue
        if verbose:
            print(f"[{name}]")
        for label, ok in mod.selftest(rng):
            if verbose:
                print(f"  [{'ok' if ok else 'FAIL'}] {label}")
            if not ok:
                fails.append(label)
    if verbose:
        print(f"\n{'PASS' if not fails else 'FAIL'} — {len(fails)} failure(s)"
              + ("" if not fails else ":\n  - " + "\n  - ".join(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(selftest())
