# Weighted-spectator obstruction: mechanical repair round W0W03

- Date: 2026-08-27
- Role: `prover`
- Original proof author: `/root/prove_weighted_spectator_obstruction`
- Repair author: `/root/repair_weighted_spectator_w0r2`
- Ledger node: `prop:weighted-spectator-obstruction`
- Dossier: `solutions/prop-weighted-spectator-obstruction.tex`
- Repair contract: `research/reviews/2026-08-27-prop-weighted-spectator-obstruction-proof-review.md`
- Repaired dossier SHA-256: `8c837c6e8ab677049071a4d5727d82cd7328bafd3d2ef88887e52c30ec672700`
- Certification state: `checked_by: none`

## Theorem retained

The repair does not change the proposition. For every $C,T_0,\gamma>0$, every
$\eta\in(0,1/2)$, and every $\delta>0$, the dossier constructs a finite-dimensional centered
one-sided-exponential product $\mu$, a balanced finite-perimeter cylinder $E$ with both additive
and relative profile excess at most $\delta$ (and with $e_0(E)\le 1$), and a time
$0<T\le T_0$ such that

$$
\mathbb E\int_0^{T\wedge\tau_\eta}
e_t(E)(1+\lVert A_t\rVert_{\mathrm{op}})^{5/2}\,dt
> C\bigl(Te_0(E)+T^{1+\gamma}\bigr).
$$

The result negates only the literal all-measure, global-operator-norm weighted-excess rate in
`q:weighted`. It does not refute KLS, and it does not address a replacement gate restricted to
near-worst measures or using a cut-local tensor-stable weight.

## Corrections applied

Every item in the cold review's `next_prompt` was applied without changing the analytic argument:

1. The initial mass-$p$ BV competitor is now named $S^{(0)}$, the approximation is correctly
   typeset as
   $\operatorname{Per}_\nu(S_k)\longrightarrow\operatorname{Per}_\nu(S^{(0)})$, and one
   exact-mass corrected regular approximant is explicitly renamed as the lemma's final $S$.
2. The tilted probability $\nu_{u,t}$ and its density-change identity are defined only for
   parameters satisfying $t\ge0$ and $0<Z(u,t)<\infty$.
3. The malformed uniform supremum was repaired to
   $\sup_{|u|\le a,\,0\le t\le\bar T}$.
4. The critical exact-mass competitor comparison is now
   $I_{\mu_t}(p_t)\le f_{i,t}(q_{i,t})$.
5. The author header records both the original author and this repair author and remains
   `checked_by: none`.

A source scan found no remaining instance of the reported malformed tokens. Inspection of the
rendered PDF confirmed that the BV perimeter convergence has two arrows, the supremum has the
correct two constraints, and equation (18) displays the full chain
$I_{\mu_t}(p_t)\le f_{i,t}(q_{i,t})\le\lVert f_{i,t}\rVert_\infty\le
v_{i,t}^{-1/2}\le\sqrt{t/c_{\mathrm{sp}}}$.

## Dependency, hypothesis, and fence audit

The proof retains exactly the four declared dependencies:

- `prop:covariance-spike` supplies only a separate fixed-time covariance-spike event;
- `lem:one-dimensional-density-variance` supplies the quantile-halfline perimeter upper bound;
- `prop:products` and `lem:half` give the positive dimension-free floor for the half-profile of
  the exponential products.

All four are proved or published imports in the current ledger. The node has no `bounded_by`
edge. The neighbouring fences are respected: the argument retains the $5/2$ two-tail-calibrated
weight, evades `obs:circularity` by using an explicit upper profile competitor, and asserts no
implication inside the trace-upgrade cluster. The proof also uses deterministic weighted-BV
approximation and density change, local exponential integrability, the planted Gaussian posterior
representation, the Brownian reflection principle, and nonnegative Tonelli. There is no numerical
input and no unstated probabilistic persistence claim.

No analytic step is left open by this repair. The theorem is unconditional relative to the
repository's accepted analytic dependencies, but the dossier is not certified until a distinct
cold proof-checker passes it.

## Validation and deferred provenance

The forced standalone build

```text
cd solutions && latexmk -g -pdf -outdir=../build prop-weighted-spectator-obstruction.tex
```

completed successfully and produced a six-page PDF. The standalone-only unresolved cross-module
references are expected; both bibliography entries resolve, and the log contains no TeX error,
undefined control sequence, missing-math insertion, runaway argument, emergency stop, or fatal
error. The PDF was inspected through a layout-preserving text extraction.

No applicable ledger delta exists at this stage. If a distinct reviewer certifies the dossier,
the deferred artifact candidate is
`solution: solutions/prop-weighted-spectator-obstruction.tex`; the orchestrator alone may then
apply the certification and status deltas.

```yaml
outcome: complete
artifacts:
  - solutions/prop-weighted-spectator-obstruction.tex
  - research/explorations/2026-08-27-prover-weighted-spectator-obstruction-w0w03.md
proposed_deltas:
  - none; certification and any refutation/status transition are deferred to the orchestrator after a fresh cold pass
next_role: proof-checker
next_prompt: |
  Cold-review the current solutions/prop-weighted-spectator-obstruction.tex at SHA-256
  8c837c6e8ab677049071a4d5727d82cd7328bafd3d2ef88887e52c30ec672700 for ledger node
  prop:weighted-spectator-obstruction. Reconstruct the proof from repository artifacts; do not
  rely on the prover's narrative. Verify the unchanged theorem quantifiers, additive and relative
  near-minimality, the four dependency edges, absence of bounded_by fences, neighbouring
  two-tail/circularity fences, base-before-T-before-N quantifier order, fixed-time-only
  Klartag--Lehec event with s=1/t, exact-p_t quantile competitor, base/spectator independence,
  nonnegative Tonelli integration, and final constants. In particular verify the repaired
  S^(0)-to-S weighted-BV approximation, the restriction 0<Z(u,t)<infinity, the corrected uniform
  supremum, and equation (18)'s profile comparison in both source and rendered PDF. Confirm that
  checked_by remains none while auditing. The reviewer must be distinct from
  /root/prove_weighted_spectator_obstruction and /root/repair_weighted_spectator_w0r2, must write a
  NEW append-only review rather than altering the prior non-certifying audit, and must compile the
  dossier standalone. If and only if every step passes, propose the exact dossier-header and
  ledger certification delta for prop:weighted-spectator-obstruction and the logically consequent
  q:weighted refutation; do not edit the dossier, ledger, manuscript, routes, gating, bibliography,
  or any existing review.
```
