"""finum — the numerical channel for the functional-inequalities open targets.

Role (see ../research/README.md, two-phase workflow):
  * Part II  — refine and refute *statements* (A1-A5): produce the `evidence_run` artifact
               a ledger node points to. Numerics validate/refute a refined statement; they
               NEVER promote it to proved.
  * Part III — the same core later refines KLS *sub-statements* and gates/refutes proof
               *routes* (research/kls/routes.md).

Soundness contract: the only sound move is *refutation* (an upper-bound claim falsified by a
certified lower bound) and *direction*. Corroboration is bounded evidence, never proof.

The headline primitive is the sound refuter `constants.poincare_lower` (the linear-test lower
bound C_P >= lambda_max(Cov); see research/knowledge/lemmas.md, lem:linear-test-lower).
"""
from __future__ import annotations

from .constants import poincare_lower, poincare_lower_basis
from .verdict import Verdict, falsify, calibration_ok

__all__ = [
    "poincare_lower",
    "poincare_lower_basis",
    "Verdict",
    "falsify",
    "calibration_ok",
]
