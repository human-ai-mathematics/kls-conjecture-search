# KLS weighted-package refutation sync

Date: 2026-08-27

Role: orchestrator

## Trigger

The repaired standalone proof of `prop:weighted-spectator-obstruction` passed an independent
cold review:

- dossier: `solutions/prop-weighted-spectator-obstruction.tex`;
- reviewed mathematical bytes:
  `8c837c6e8ab677049071a4d5727d82cd7328bafd3d2ef88887e52c30ec672700`;
- certification report:
  `research/reviews/2026-08-27-prop-weighted-spectator-obstruction-repair-proof-review.md`;
- post-certification dossier bytes, after the exact permitted header delta:
  `9725715db0136dfdcf7742fe100fd3f270ae70a6b3397d242f4afbccfc66e6f4`.

The proof gives, for every proposed $C,T_0,\gamma>0$, every
$\eta\in(0,1/2)$, and every $\delta>0$, a balanced cylinder in an isotropic product of centered
one-sided exponentials whose additive and relative initial excess are at most $\delta$ but which
violates

$$
\mathbb E\int_0^{T\wedge\tau_\eta}
e_t(E)(1+\|A_t\|_{\mathrm{op}})^{5/2}\,dt
\le C\bigl(Te_0(E)+T^{1+\gamma}\bigr)
$$

at some $T\le T_0$.

## Status delta

The certification supports the following atomic interpretation.

- `prop:weighted-spectator-obstruction` is `proved` and agent-checked.
- `q:weighted` is `refuted` by that proposition.
- `ass:weighted-package` is `refuted`, because its first conjunct is exactly the false uniform
  global-operator-norm estimate.
- `thm:intro-weighted` remains `conditional`: its proof is a valid implication from the explicit
  package, but the premise is now known to be false. The theorem is not promoted to `proved`.

The witnesses are product measures, so this is not a counterexample to KLS. It is a refutation
of one proof package and of the claim that the global covariance operator norm is a tensor-stable
weight for propagation of a fixed cut.

## Consequence for the search tree

A replacement must ignore covariance inflation in independent spectator directions while still
detecting the aligned anisotropic two-tail mode. Plausible shapes include a cut-oriented or
tensor-stable covariance scale, or an explicit near-worst-measure premise. The certified
consumption proof only needs an $O(T)$ supply; it does not require the displayed superlinear
remainder.

The stronger unweighted statement tested by `prop:spectator-excess-rate-obstruction` is a
separate node. At the time of this sync it remains open pending its own independent review, so no
claim about that node is used here.

## Synchronized surfaces

The orchestrator synchronized the status and interpretation in:

- `research/kls/ledger.yaml`;
- `research/kls/gating.md`;
- `modules/kls/00-orientation.tex`;
- `modules/kls/20-eldan-statements.tex`;
- `modules/kls/23-stein-route.tex`;
- `modules/kls/24-excess-propagation.tex`; and
- `modules/kls/27-eldan-open-targets.tex`.

The literal package and its implication remain visible as an audit trail; the prose no longer
advertises the refuted premise as the corrected live route. After synchronization,
`python3 research/check_ledger.py` reports zero errors.
