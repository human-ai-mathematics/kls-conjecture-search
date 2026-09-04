---
type: exploration
date: "2026-08-20"
outcome: directional
nodes:
  - q:alignment
---
# KLS research program — cycle 1 synthesis

Date: 2026-08-20

Status: completed exploratory cycle. This note records route triage, proved reductions,
counterexamples, and a finite-dimensional numerical stress test. It does **not** prove KLS or
promote any open ledger node. Every use of Letwin's 27 July 2026 version-1 preprint is conditional
on that recent, unreviewed source being correct.

## Outcome

The cycle changes the route ranking without closing the conjecture.

1. The most amenable next proof target is now the **fixed-eigenfunction stochastic-localization
   source/damping estimate**. It has an exact SDE, a short conditional proof of KLS, and retains
   the orientation information discarded by a global covariance-norm potential.
2. The proposed full first-eigenfunction \(H^{-1}\) residual estimate is not an easier lemma: on
   the regular class it is quantitatively equivalent to KLS. Its heat representation is still a
   useful diagnostic, because it isolates the entire difficulty in a long-time, low-spectrum
   tail.
3. A natural attempt to unweight the positive moment-map Stein form is false, even in dimension
   one for genuine first eigenfunctions. A truncated-exponential family gives an explicit
   counterexample.
4. The designated product tail-union stress test for `q:alignment` is now implemented. It finds a
   genuine high-dimensional alignment pulse, but does not find divergent required constants
   through \(n=1024\). A separate boundary-Poisson analysis predicts a bounded limiting pulse.
   Thus this family does not currently refute Route A; that route remains a useful secondary
   model problem.

The best allocation is therefore: put the main analytical effort into the eigenfunction-aware
dynamic estimate; retain product alignment as a secondary falsification channel; do not make the
full \(H^{-1}\) residual or another global maximum-eigenvalue potential the first subgoal.

## What is rigorous

### Fixed-function localization

For a deterministic function \(f\), let

\[
g_t=\operatorname{Cov}_{\mu_t}(f,X),\qquad
H_t=\mathbb E_t[(f-\mathbb E_tf)(X-a_t)^{\otimes2}],\qquad
A_t=\operatorname{Cov}_{\mu_t}(X).
\]

The exact localization system includes

\[
d g_t=H_t\,dW_t-A_tg_t\,dt,
\]

and hence

\[
d|g_t|^2=\text{martingale}
  +\bigl(\|H_t\|_{\mathrm{HS}}^2-2g_t^TA_tg_t\bigr)dt.
\]

For a normalized first eigenfunction with gap \(\lambda\), posterior Brascamp--Lieb and the
fixed-gradient density martingale give

\[
\mathbb E\operatorname{Var}_{\mu_T}(f)\le \lambda/T.
\]

These identities prove the following conditional implication. If universal
\(T_0,C_0,C_1>0\) and \(\alpha<1\) satisfy, for all \(t\le T_0\),

\[
\mathbb E\int_0^t\|H_s\|_{\mathrm{HS}}^2ds
\le C_0t+C_1\mathbb E\int_0^t|g_s|^2ds
+\alpha\mathbb E\int_0^t2g_s^TA_sg_s\,ds,
\]

then Gronwall preserves a fixed amount of posterior variance for a universal time, while the
terminal estimate bounds it by \(\lambda/T\); consequently \(\lambda\ge c>0\). The one-horizon
net-occupation and random-horizon variants in the detailed note are weaker sufficient forms.

Conditional on Letwin's quadratic-form Poincare theorem, Hilbert--Schmidt duality also gives the
sharp intrinsic estimate

\[
\|A_t^{-1/2}H_tA_t^{-1/2}\|_{\mathrm{HS}}^2
\le 8\operatorname{Var}_{\mu_t}(f).
\]

The remaining operation is unwhitening over time without discarding the alignment of this tensor
with the inflated eigenspaces of \(A_t\). That is the exact dynamic bottleneck.

### The \(H^{-1}\) endpoint

For a normalized first eigenfunction put

\[
b=\int\nabla f\,d\mu,\qquad
R(f)=\sum_i\|\partial_i f-b_i\|_{H^{-1}(\mu)}^2.
\]

The exact sandwich

\[
1+|b|^2-2|b|^2/\lambda
\le R(f)\le 1-|b|^2/\lambda
\]

shows both directions of the route audit: a universal estimate \(R(f)\le C\lambda\) implies a
universal gap, while a universal gap implies that estimate. Thus the full target is
KLS-equivalent on the regular class.

Writing \(P_t=e^{-t(-L)}\) and \(h_i=\partial_i f-b_i\) gives the exact heat split

\[
R(f)=\int_0^\infty\sum_i\langle h_i,P_th_i\rangle\,dt,
\qquad
\int_0^T\sum_i\langle h_i,P_th_i\rangle\,dt\le T\lambda.
\]

The short-time and high-frequency portions are therefore controlled; the long-time,
low-spectrum projection is the whole remaining problem. Products tensorize this residual
exactly, and the truncated exponential shows that the obstruction can be rank one. Effective
rank alone will not close it.

### A rejected shortcut

There is no universal estimate of the form

\[
\mathbb E\langle\tau\nabla f,\nabla f\rangle
\le C\bigl(\mathbb E|\nabla f|^2+
            \mathbb E\|\nabla^2f\|_{\mathrm{HS}}^2\bigr)
\]

for the positive moment-map Stein kernel \(\tau\), even when \(f\) is the first nonconstant
Neumann eigenfunction of an isotropized one-dimensional truncated exponential. The left side
grows linearly with the truncation length while the two energies on the right stay bounded.
This also explains why a constant-matrix quadratic estimate cannot simply be used with the
variable matrix \(\nabla^2f(X)\).

## Numerical product stress test

The new `kls-align` target uses the balanced tail union

\[
E_n=\{\max_i|X_i|\ge a_n\}
\]

in an isotropic Laplace product. Exact tilted one-dimensional moments and the filtering
representation \(c_t=tX+B_t\) produce the incident-high source \(S_t^H\), centroid term \(r_t\),
and damping \(D_t\) in \(O(n)\) work per state. Intervals are selected on 16 discovery paths and
evaluated on 16 independent held-out paths.

The final sweep used \(n=128,256,512,1024\), \(T=0.5\), reported grid \(dt=0.005\), and fixed
plus \(1/\log n\) and \(1/\log^2n\) windows. All recorded gates passed. In particular, the worst
normalized coarse/fine drift was between \(0.448\) and \(0.569\) against a tolerance of one, and
the analytic moments agreed with independent quadrature to below \(1.1\times10^{-13}\).
An independent rerun with the recorded seed reproduced the retained 45-line artifact byte for
byte (SHA-256
`4219b4690e5951c659199fa6bf0370b49ebb2201e8c234913c032fc3891e5170`).

For the shortest globally selected interval and \(C_1=1\), the held-out required \(C_0\) at
\(\alpha=0.9\) was

| \(n\) | 128 | 256 | 512 | 1024 |
|---:|---:|---:|---:|---:|
| required \(C_0\) | 0 | 0 | \(0.285\pm0.096\) | \(0.249\pm0.135\) |

At \(\alpha=0\) it rose from \(0.411\pm0.158\) to \(1.236\pm0.183\), diagnostically indicating
that alignment is not negligible. At \(n=1024\) the selected source pulse lies near
\([0.14,0.15]\).

Exact finite-dimensional hazard identities and a proved bounded-window, fixed-time boundary
point-process limit explain this crossover. Formal extension to the full observable predicts a
finite source-density peak near \(t=0.148\), not divergence. The extension to an unbounded cloud,
uniform small times, and first-exit stopping remains open, so the asymptotic conclusion is a
well-calibrated conjecture rather than a theorem.

The artifact is intentionally `diagnostic_only`, `no-proof/no-route-verdict`, and
`evidence_eligible: false`: the worktree was dirty; there are only 16 held-out paths; stopping is
node-detected without a Brownian-bridge exit/re-entry correction; and one cut family cannot decide
the universal all-cut statement. No ledger status is promoted.

## Route decision and next lemma

The next analytical calculation should use the eigenfunction equation inside the Gaussian
posterior channel to relate either

\[
g_t^TA_tg_t
\quad\text{or the high-space incidence of}\quad
A_t^{-1/2}H_tA_t^{-1/2}
\]

to the fixed initial energies

\[
\mathbb E|\nabla f|^2=\lambda,
\qquad
\mathbb E\|\nabla^2f\|_{\mathrm{HS}}^2\le\lambda^2.
\]

A successful estimate should feed the absorptive criterion above and permit covariance inflation
when it is not aligned with the eigenfunction tensor. Another bound on
\(\|A_t\|_{\mathrm{op}}\) alone loses that information and is lower priority.

For the product strand, the clean proof target is a uniform stopped envelope
\(\mathbb E[1_{\{t<\tau\}}S_t^H]\le C\) for the tail union. If more computation is warranted,
fixed-time slices at much larger \(n\) are more informative than another modest increase in the
number of full paths.

## Detailed records

- [Frontier and source audit](2026-08-20-kls-frontier-audit.md)
- [Fixed-eigenfunction localization derivation](2026-08-20-kls-eigenfunction-localization.md)
- [First-eigenfunction \(H^{-1}\) model analysis](2026-08-20-kls-hminus1-models.md)
- [Tail-union high-dimensional asymptotics](2026-08-20-kls-tail-union-asymptotics.md)
- [Final held-out diagnostic artifact](../runs/2026-08-20-kls-align-high-n-final.jsonl)
- [`kls-align` target](../../experiments/finum/targets/kls_alignment.py)
- [Exact tail-union formulas](../../experiments/finum/localization/tail_union.py)
- [Filtering-path implementation](../../experiments/finum/localization/alignment.py)
