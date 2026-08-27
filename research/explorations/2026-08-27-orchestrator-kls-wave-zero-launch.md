# Orchestrator launch: KLS certification and refutation wave zero

Date: 2026-08-27

Role: orchestrator

Branch: `codex/kls-wave-zero-20260827`

## Scope

This record accepts precise open statements for the first staged parallel KLS wave.  It records
no numerical evidence, no proof certification, and no KLS status change.  Ledger, manuscript,
gate, and route-control changes are applied together because the mathematical targets changed.

## Route-S endpoint correction

For $Q(t)=\mathbb E|g_t|^2$, $S_t=\|H_t\|_{\mathrm{HS}}^2$, and
$D_t=g_t^TA_tg_t$, the fixed-function SDE gives
$$
Q(t)=|g_0|^2+\mathbb E\int_0^t(S_s-2D_s)\,ds.
$$
If the occupation input charges the source against the full damping,
$$
\mathbb E\int_0^tS_s\,ds
\le C_0t+C_1\int_0^tQ(s)\,ds+\mathbb E\int_0^t2D_s\,ds,
$$
then $Q(t)\le1+C_0t+C_1\int_0^tQ(s)\,ds$.  Gronwall, the filtering identity
$\mathbb E\operatorname{Var}_t(f)=1-\int_0^tQ(s)\,ds$, and posterior Brascamp--Lieb therefore
give a universal spectral gap on a sufficiently short universal interval.  The former strict
condition $\alpha<1$ was stronger than this sufficiency mechanism needs.  The open occupation
gate is weakened to the full-damping endpoint, while `prop:spectral-sufficiency` stays open until
a standalone dossier and cold review certify the constants and regularization limit.

## Fixed-function source candidate

The same SDE and $A_t\preceq(\kappa+t)^{-1}I$ yield the proof-ready candidate
`lem:mm-time-weighted-fixed-source`.  It retains a linear time weight and consequently does not
claim the unweighted initial-layer estimate required by `q:mm-spectral-occupation`.

## CMH recovery-envelope correction

The existing approximation dossier contains the unconditional inequality
$$
C_P^{\mathrm{aff}}(\mu)\le\liminf_k C_P^{\mathrm{aff}}(\mu_k).
$$
Combining this with the regular CMH endpoint requires only one recovery sequence with bounded
$\liminf C_{\mathrm{CMH}}$, not uniform control over every canonical regularization parameter.
The new open premise `ass:cmh-recovery-envelope` records this weaker gate.  The stronger
`ass:uniform-cmh-approximants` and its certified conditional consumer are retained unchanged.

## Weighted gate and integrity work

The exponential-spectator cylinder obstruction to the literal `q:weighted` statement is sent
first to a gate prober and source verifier, then to a prover only if the analytic sketch survives.
No refutation node or status change is accepted at launch.  Existing dossier/manuscript defects
identified by proof mining are sent through author and cold-review repair cycles rather than
silently patched into certified artifacts.

## Dispatch order

1. Distinct provers author the spectral sufficiency, fixed-function source, and CMH recovery
   dossiers.
2. A `q:weighted` prober and literature scout independently settle the spectator construction
   and its source normalization.
3. Separate provers repair the excess, product, and persistent-splitting dossiers; manuscript-only
   synchronization patches remain with the orchestrator.
4. Every dossier receives a cold reviewer with a distinct identity.  Only passing persisted
   reviews permit certification metadata or status changes.
5. A singleton synthesizer merges the wave before any trace-upgrade work is launched.

No cross-route implication is asserted.  The single-owner rule for the trace-upgrade cluster is
unchanged.
