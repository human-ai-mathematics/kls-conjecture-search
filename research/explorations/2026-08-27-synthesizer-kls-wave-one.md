---
type: exploration
date: "2026-08-27"
outcome: proposed
nodes:
  - q:upgrade
  - q:stein-weighted
  - q:mm-spectral-occupation
  - cor:tight-window-consumption
---
# Synthesis: KLS Wave One

Date: 2026-08-27

Role: `synthesizer`

Concurrency key: singleton `knowledge`, granted by the orchestrator

Scope: convergence of the Wave-1 KLS route probes, proof mining, and literature imports. This
record changes no ledger, manuscript, route-control file, bibliography, dossier, or review. No
numerical result is used.

## Sources converged

Persisted sources:

- `research/explorations/2026-08-27-kls-route-prober-spectral-rank-tail-w1s03.md`;
- `research/explorations/2026-08-27-kls-route-prober-rank-tail-orientation-w1r01.md`;
- `research/explorations/2026-08-27-kls-route-prober-conditional-fiber-frame-w1f01.md`;
- `research/explorations/2026-08-27-kls-route-prober-cmh-recovery-envelope-w1c02.md`;
- `research/explorations/2026-08-27-kls-route-prober-weighted-spectator-w0w01.md`;
- `research/explorations/2026-08-27-prover-weighted-spectator-obstruction-w0w02.md`;
- `research/reviews/2026-08-27-prop-weighted-spectator-obstruction-proof-review.md`;
- `research/explorations/2026-08-27-literature-scout-weighted-spectator-w0l01.md`;
- `research/explorations/2026-08-27-literature-scout-conditional-fiber-w1l02.md`;
- `research/explorations/2026-08-27-synthesizer-kls-first-wave-par-04.md`;
- `research/explorations/2026-08-27-orchestrator-kls-wave-two-targets.md`;
- `research/explorations/2026-08-27-prover-lyapunov-stein-duality-w2s01.md`; and
- the live KLS ledger, gating file, route briefs, manuscript anchors, knowledge files, and the
  certified dossiers cited by those records.

Read-only handoffs with no source artifact at the time of synthesis were also compared:

- boundary/Stein and Eldan proof mining;
- CMH recovery and exact-case proof mining;
- the second-route scout's `laplace-brenier` proposal.

Claims from an unpersisted handoff are not treated as certification. They are either derived
again below from a persisted proof or classified as needing statement extraction or a bounded
probe.

The current control-plane snapshot passes the structural ledger validator. The orchestrator has staged
`lem:lyapunov-stein-duality`, `prop:spectator-excess-rate-obstruction`,
`prop:cmh-recovery-calculus`, and `cor:full-matrix-dissipation` as `open`, with no premature
solution or review metadata. The Lyapunov--Stein author has now produced an unreviewed standalone
dossier, while the other three proof cycles are active under distinct solution keys. The
Klartag--Lehec rank
nodes are imported from an unreviewed version-2 preprint. The exponential covariance-spike and
one-dimensional density--variance nodes are published imports. The weighted-spectator dossier
has a noncertifying first audit and its repaired bytes are in a fresh cold-review cycle;
there is therefore no weighted-route status delta available from this synthesis alone.

## Executive convergence

Wave One does not prove KLS, but it materially changes the search tree.

1. The new rank-tail literature controls covariance eigenvalue counts and entrance times, not
   source orientation. It yields a polylogarithmic worst-orientation bound and a
   dimension-free near-full-stable-rank branch, but neither live stochastic gate.
2. The minimal Eldan consumer needs only prefix estimates from time zero. Combining this
   certified fact with the soft-projector identity removes the positive interval-boundary term
   from the next `q:upgrade` gate. The remaining obstruction is exactly the two
   cut-dependent projector-motion contractions.
3. Independent exponential spectators kill more than the global operator-norm weight. The same
   construction defeats every universal bound with a superlinear source-vanishing remainder,
   even when the weight is identically one. A viable replacement must change the rate as well
   as the weight, unless it adds an explicit near-worst-measure hypothesis.
4. The cut tensor has an exact Lyapunov-dual covariance scale that ignores independent direct
   sums and equals the dangerous variance on the anisotropic two-tail model. This is a
   calibrated replacement candidate, not an occupation theorem.
5. The natural conditional-fiber root frame is analytically dead on the simplex, with gap
   $O(m^{-2})$. The existential all-frame route survives, and its exact remaining object is a
   finite-dimensional min--max/continuum dual certificate.
6. The existential CMH recovery gate is now cleanly separated into a reusable recovery calculus
   and a genuine-Hessian density problem. The first unsupported estimate already occurs on
   linear tests; full CMH then still needs variable-field and solenoidal coercivity.
7. The proposed Laplace--Brenier transport route is distinct enough to merit one bounded probe,
   but not route registration. Its first falsification test is the optimized simplex Hessian.

## Common normalization I: covariance rank versus oriented energy

Let $A\succeq0$ be the current covariance, let

$$
X=A^{1/2}ZA^{1/2},
\qquad
P_L=\mathbf1_{(L,\infty)}(A),
\qquad
Q_L=I-P_L,
$$

and define the complete high-incidence energy

$$
\mathcal I_L(X)
=\|P_LXP_L\|_{\mathrm{HS}}^2
+2\|P_LXQ_L\|_{\mathrm{HS}}^2.
\tag{N1}
$$

Then

$$
\|X\|_{\mathrm{HS}}^2
=\|Q_LXQ_L\|_{\mathrm{HS}}^2+\mathcal I_L(X),
\qquad
\|Q_LXQ_L\|_{\mathrm{HS}}^2\le L^2\|Z\|_{\mathrm{HS}}^2.
\tag{N2}
$$

The two stochastic streams instantiate (N1) with different carriers:

| stream | $X$ | exact residue | damping budget |
|---|---|---|---|
| `q:upgrade` | $\sqrt{s_t}K_t$ | $\mathcal H^K_{t,L}=\mathcal I_L(\sqrt{s_t}K_t)$ | a strict fraction of $D_t$ after converting $K_t$ to the Riccati tensor $G_t$ |
| `q:mm-spectral-occupation` | $H_t$ for one fixed eigenfunction | $\mathcal R_{t,L}=\mathcal I_L(H_t)$ | at most the complete exact damping $2g_t^TA_tg_t$ |

The Klartag--Lehec inputs bound the unweighted random rank
$\operatorname{rank}P_{t,3}$ and integrals of ordered covariance eigenvalues. The gates require
the energy-weighted rank

$$
\sum_{i,j}a_i(t)a_j(t)Z_{ij}(t)^2
\mathbf1_{\{a_i(t)>3\ \mathrm{or}\ a_j(t)>3\}}.
\tag{N3}
$$

No imported theorem controls the coupling between the covariance eigenspaces and the random
weights in (N3). The cut tensor and eigenfunction tensor are not identified, and no implication
between their occupation estimates is asserted.

## Common normalization II: the cut-oriented Lyapunov scale

For $A\succ0$ let

$$
\mathscr L_A(M)=\frac{AM+MA}{2}.
$$

The proof of the certified `lem:pathwise-BL` establishes before operator-norm scalarization

$$
s\langle K,M\rangle^2
\le\frac4t\operatorname{Tr}(MAM)
=\frac4t\langle M,\mathscr L_A M\rangle
\qquad(M=M^T).
\tag{L1}
$$

Duality in the symmetric-matrix Hilbert space gives

$$
s\langle K,\mathscr L_A^{-1}K\rangle\le\frac4t.
\tag{L2}
$$

For $K\ne0$ define

$$
\lambda_{\mathrm{cut}}(A,K)
=\frac{\|K\|_{\mathrm{HS}}^2}
{\langle K,\mathscr L_A^{-1}K\rangle},
\qquad
\lambda_{\mathrm{cut}}(A,0)=0.
\tag{L3}
$$

Then

$$
s\|K\|_{\mathrm{HS}}^2
\le\frac{4\lambda_{\mathrm{cut}}(A,K)}t.
\tag{L4}
$$

In an eigenbasis of $A$, (L3) is the $K_{ij}^2$-weighted harmonic mean of
$(a_i+a_j)/2$. It has the two calibrations a replacement covariance weight must pass:

$$
\lambda_{\mathrm{cut}}(A\oplus B,K\oplus0)
=\lambda_{\mathrm{cut}}(A,K),
\tag{L5}
$$

so independent spectators are ignored, while on the certified anisotropic two-tail model
$\lambda_{\mathrm{cut}}=\Lambda$. This exact algebra has been promoted, with guardrails, to
`research/knowledge/lemmas.md`.

Equations (L2)--(L5) do not control the initial layer: the $t^{-1}$ factor remains, and no
weighted excess or occupation estimate follows. They identify a plausible tensor-stable scale,
not a replacement theorem.

## Common normalization III: what the weighted route actually consumes

For a nonnegative adapted weight $W_t$, put

$$
\mathfrak E_W(T;\mu,E)
=\mathbb E\int_0^{T\wedge\tau_\eta}e_t(E)W_t\,dt.
\tag{E1}
$$

The current open question takes
$W_t=(1+\|A_t\|_{\mathrm{op}})^{5/2}$ and asks for

$$
\mathfrak E_W(T;\mu,E)
\le C\bigl(Te_0(E)+T^{1+\gamma}\bigr).
\tag{E2}
$$

The certified tight-window consumption uses only

$$
\mathfrak E_W(T;\mu,E)\le C_*T
\tag{E3}
$$

for cuts with $e_0\le1$. The exponent $1+\gamma$ is not consumed.

The spectator proof supplies, on a base event independent of the fixed-time spike event,

$$
e_t(E)\ge cP_0
\qquad(t\in[T/2,T]),
\tag{E4}
$$

after the base is fixed and the spectator dimension is chosen as a function of $T$. Dropping
the covariance weight from the same Tonelli calculation yields

$$
\mathbb E\int_0^{T\wedge\tau_\eta}e_t(E)\,dt
\ge c'P_0T.
\tag{E5}
$$

The initial cylinder can have arbitrarily small additive and relative excess, uniformly in all
later spectator dimensions, while $P_0$ stays bounded below. Consequently, for every
$\gamma>0$ and proposed $C,T_0$, one first chooses the base with
$e_0\ll P_0/C$, then $T$ with $T^\gamma\ll P_0/C$, and finally the spectator dimension. This
contradicts

$$
\mathfrak E_W(T)\le C(Te_0+T^{1+\gamma})
\tag{E6}
$$

for every weight $W_t\ge1$, including $W_t\equiv1$.

This strengthens the design diagnosis but is not yet a ledger refutation: the current dossier
states the global-weight obstruction, its first review is noncertifying, and the stronger
unweighted corollary has no standalone dossier or cold review. The orchestrator has correctly
staged the distinct open node `prop:spectator-excess-rate-obstruction`; it must not be silently
folded into the existing proposition.

## The minimal prefix gate for `q:upgrade`

The live `ass:all-cut-carleson` asks for every time interval. The certified
`cor:tight-window-consumption` needs only prefixes from zero: for one fixed universal
$\eta\in(0,1/6]$, every $0<T\le T_0$, and every fixed initially balanced cut,

$$
\mathbb E\int_0^{T\wedge\tau_\eta}S_t\,dt
\le C_0T+C_1\mathbb E\int_0^{T\wedge\tau_\eta}r_t\,dt
+\alpha\mathbb E\int_0^{T\wedge\tau_\eta}D_t\,dt,
\qquad\alpha<1.
\tag{P1}
$$

This weaker quantifier materially improves the soft-projector reduction. In the notation of the
rank-orientation probe, choose one fixed $C^2$ cutoff with $\chi=0$ on
$(-\infty,3]$ and $\chi=1$ on $[4,\infty)$, put

$$
F_t=\chi(A_t),
\qquad
R_t=A_t-B_t,
\qquad
Y_t=\operatorname{Tr}(F_tR_t)\ge0.
$$

The exact It\^o identity contains the endpoint decrement $Y_0-Y_T$. Since $A_0=I$, one has
$F_0=0$ and $Y_0=0$, so on a prefix

$$
Y_0-Y_T=-Y_T\le0.
$$

It can be discarded. The next gate therefore need not control positive interval decrements.
After the favorable Riccati and deterministic covariance-drift terms are also discarded, the
only surviving injection is

$$
\begin{aligned}
\mathfrak J_\chi^0(T)
&=\frac12\mathbb E\int_0^{T\wedge\tau_\eta}
\sum_k\operatorname{Tr}\!left(
D^2\chi(A_t)[\Theta_{t,k},\Theta_{t,k}]R_t
\right)dt\\
&\quad+\mathbb E\int_0^{T\wedge\tau_\eta}
\sum_k\operatorname{Tr}\!\left(
D\chi(A_t)[\Theta_{t,k}]\Gamma_{t,k}
\right)dt.
\end{aligned}
\tag{P2}
$$

Here $\Theta$ is the covariance third-moment martingale coefficient and $\Gamma$ is the
cut-dependent martingale coefficient of $R$. Conditional on the intrinsic low-block input, an
estimate

$$
\mathfrak J_\chi^0(T)
\le C_\chi T+C_r\mathbb E\int_0^{T\wedge\tau_\eta}r_tdt
+\gamma\mathbb E\int_0^{T\wedge\tau_\eta}D_tdt,
\qquad\gamma<\frac18,
\tag{P3}
$$

implies (P1), with final damping coefficient $3/4+2\gamma<1$. This is strictly narrower than
the every-interval gate proposed in the rank-orientation report. Rank tails still control
neither contraction in (P2); the gain is removal of a third, unnecessary boundary term.

## Directional implication tables

The status words below concern the displayed directions. `Open` includes reductions proved only
inside an exploration but not backed by a standalone certified dossier; such a row warrants no
ledger edge.

### Rank/orientation and the trace-upgrade cluster

| direction | status | reason |
|---|---|---|
| Klartag--Lehec rank imports $\Rightarrow$ `q:upgrade` | open | the imports count covariance ranks but do not weight them by $K_t$ or control the two contractions in (P2) |
| `q:upgrade` $\Rightarrow$ Klartag--Lehec rank imports | not even conjectured | the imported statements are cut-free covariance theorems with different quantifiers |
| Klartag--Lehec rank imports $\Rightarrow$ `q:mm-spectral-occupation` | open | they do not control the fixed eigenfunction's energy weights, rotation, or mixed block |
| `q:mm-spectral-occupation` $\Rightarrow$ the rank imports | not even conjectured | one eigenfunction source cannot recover a cut-free rank theorem |
| `q:upgrade` $\Rightarrow$ the product incident-high conclusion of `q:alignment` | open | restriction to products and $S_t^H\le S_t$ is recorded only in a probe, not a dossier |
| `q:alignment` $\Rightarrow$ `q:upgrade` | not even conjectured | the product statement is narrower in measures and fixes the covariance eigenbasis |
| incident-$K$ occupation $\Rightarrow$ the numerical Stein-tensor part of `q:stein-weighted` | open | the tensors agree algebraically, but no dossier promotes the reduction |
| incident-$K$ occupation $\Rightarrow$ the geometric Jacobi/Reilly statement in `q:stein-weighted` | not even conjectured | covariance projectors do not identify Jacobi modes or boundary terms |
| `q:stein-weighted` $\Rightarrow$ `q:upgrade` | not even conjectured | its scope is near-Cheeger cuts and no boundary-to-all-cut transform exists |
| `q:upgrade` $\Rightarrow$ `q:stein-weighted` | not even conjectured | all-cut Riccati control gives no almost-stability or Reilly theorem |
| `q:mm-spectral-occupation` $\Rightarrow$ any trace-upgrade-cluster node | not even conjectured | $H_t$ belongs to one eigenfunction; $K_t,G_t$ belong to a fixed cut |
| any trace-upgrade-cluster node $\Rightarrow$ `q:mm-spectral-occupation` | not even conjectured | no cut/eigenfunction reconstruction is stated |
| tight-prefix estimate (P1) $\Rightarrow$ universal boundary lower bound for the cut | proved (dossier) | this is exactly agent-certified `cor:tight-window-consumption` |

No equivalence among `q:upgrade`, high-rank `q:stein-weighted`, and `q:alignment` is asserted.
The CMH square-root commutator remains a related orientation problem, not a fourth equivalent
member.

### Weighted excess

| direction | status | reason |
|---|---|---|
| certified `prop:weighted-spectator-obstruction` $\Rightarrow$ negation of literal `q:weighted` | open | the first audit is noncertifying; a repaired dossier needs a fresh cold review |
| every universal $W\ge1$ superlinear-remainder rate of the form (E6) holds | known false | the spectator construction and (E5)--(E6) negate it by a direct analytic reuse of the same base event and Tonelli argument; a new dossier is still required for ledger provenance |
| an $O(T)$ bound (E3) $\Rightarrow$ the weighted consumption step | proved (dossier) | `cor:tight-window-consumption` and the existing weighted-package consumption use no $T^{1+\gamma}$ gain |
| replacing the global weight by any $W\ge1$ cut-local weight while keeping the same rate $\Rightarrow$ a viable gate | known false | (E5) remains after every such replacement |
| Lyapunov scale (L3) $\Rightarrow$ a replacement weighted-excess theorem | open | it passes direct-sum and two-tail calibrations but supplies no time-integrated excess estimate |

### Conditional-fiber frame

| direction | status | reason |
|---|---|---|
| universal test-independent frame gap $\Rightarrow$ KLS | open | the factor-$4$ bridge is proved and independently audited only in the exploration; it still needs a dossier |
| KLS $\Rightarrow$ universal frame gap | not even conjectured | the one-dimensional comparison has the wrong direction for a converse |
| $A_{m-1}$ root frame $\Rightarrow$ a universal simplex gap | known false | the repository cap is $O(m^{-2})$, and Sasada's published normalization gives the explicit upper bound $48/[m(m+1)]$ |
| root-frame failure $\Rightarrow$ failure of every admissible frame | not even conjectured | permutation-invariant frames may mix arbitrary direction orbits |
| fixed-degree all-frame dual certificates with objective $\varepsilon_m\to0$ $\Rightarrow$ route refutation | open | the finite exact certificate is derived, but no such sequence is known |

### CMH recovery

| direction | status | reason |
|---|---|---|
| `ass:cmh-recovery-envelope` $\Rightarrow$ KLS | proved (dossier) | this is the existing conditional `cor:cmh-recovery-sequence-suffices`; the premise remains open |
| KLS $\Rightarrow$ bounded CMH recovery envelope | not even conjectured | the CMH solenoidal channel may make the envelope strictly larger than affine Poincar\'e |
| `prop:cmh-recovery-calculus` $\Rightarrow$ the general recovery envelope | not even conjectured | the calculus closes exact tensor-generated classes only |
| a universal linear quotient along one recovery $\Rightarrow$ full CMH recovery | open | variable gradients and the nonnegative solenoidal channel remain |
| exact product/simplex CMH $\Rightarrow$ arbitrary projected targets | not even conjectured | rectangular projections do not preserve the canonical moment Hessian |

## Killed variants — do not rerun

These conclusions kill proof shapes, not KLS and not necessarily their containing routes.

1. **Marginal rank rarity as source occupation.** Multiplying a covariance-rank probability by
   a mean source bound is an invalid correlation step. Even a fictitious pathwise variance cap
   leaves $O((1+\log n)^8)$ in Route S.
2. **Universal pointwise effective rank.** Near-full stable rank would close the cut high-rank
   branch, but the certified two-tail slice has stable rank one, aligns with the inflated
   direction, and has zero instantaneous damping.
3. **One-sided projected eigenfunction energy.** A frozen projector counts the high--low block
   once while the residue counts it twice; the generic repair forces damping coefficient
   $\alpha\ge2$ before projector-motion errors.
4. **Hard-projector limiting without a motion estimate.** $D\chi$, $D^2\chi$, inverse-gap,
   rotation, and threshold-local-time terms are real. Rank entrance times control none of them.
5. **Global-operator-norm weighted excess.** Independent spectators create covariance spikes
   unrelated to the tracked cylinder. The current global weight is tensor-unstable.
6. **Changing only the weight while retaining $T^{1+\gamma}$.** Equation (E5) kills the
   source-vanishing remainder even at weight one. A valid repair must change the rate, add a
   near-worst-measure premise, or both.
7. **The simplex root frame.** The $A_{m-1}$ pair-exchange form has gap $O(m^{-2})$. Symmetry does
   not make this orbit optimal, so the existential frame route is not killed.
8. **CMH descent through inherited kernels.** Convolution, rectangular projection, nonlinear
   transport, mixture, or triangulation does not preserve the canonical moment Hessian without
   a new comparison theorem.
9. **Scalar Riccati/BL deweighting.** The certified time-weighted source budget cannot be
   deweighted at zero by another scalar multiplier; the initial high-rank orientation remains.

## Surviving exact gates

### Eldan all-cut route

Prove the prefix soft-projector injection estimate (P3) for a single fixed cutoff. The
unnecessary interval-decrement term has disappeared; the unresolved terms are precisely the
cut-dependent $D^2\chi$ curvature contraction and $D\chi$ cross variation. The damping
threshold is $\gamma<1/8$.

### Moment-map spectral route

At threshold $L=3$, the high-residue estimate with coefficient-one full damping is equivalent,
up to the controlled low block, to

$$
q(T)-|g_0|^2
\le C_0T+C_1\int_0^Tq(t)dt,
\qquad q(t)=\mathbb E|g_t|^2.
$$

The missing theorem is a joint energy-weighted rank entrance/rotation estimate for the fixed
eigenfunction tensor, counting the mixed block twice. Unweighted rank tails do not weaken this
gate.

### Weighted geometric route

The consumer-compatible target is an $O(T)$ estimate, not a superlinear remainder. A surviving
package must make one of two choices explicit:

- restrict to near-worst measures and prove that the restriction excludes the spectator
  mechanism; or
- replace the global norm by a cut-local tensor-stable scale, such as the calibrated candidate
  $\lambda_{\mathrm{cut}}$, and ask only for an $O(T)$ supply.

Either choice still needs the separate Jacobi/Reilly almost-stability theorem. A cut-local
weight does not identify covariance-high modes with Jacobi modes.

### Conditional-fiber frame route

The exact surviving quantity on the isotropic uniform simplex is

$$
\Lambda_{m,k}
=\sup_{\rho:\,(m-1)\int\theta\theta^T\,d\rho=I}
\lambda_{\min}\left((m-1)\int B_{m,k}(\theta)d\rho(\theta),G_{m,k}\right).
$$

The next decision is either a uniform lower bound for this min--max or an exact fixed-degree
dual certificate with objective tending to zero. The uniform spherical frame is the clean first
stress test. No root-only computation decides it.

### CMH recovery route

For a general target, the first missing estimate is already linear: construct a regular
compact-target $\nu$ with $W_2(\nu,\mu)<\varepsilon$ and

$$
Q_{\mathrm{lin}}(\nu)
=\lambda_{\max}\!\left(
\Sigma_\nu^{-1/2}
\mathbb E[H_\nu\Sigma_\nu^{-1}H_\nu]
\Sigma_\nu^{-1/2}
\right)
\le C_{\mathrm{lin}}+\varepsilon,
$$

where $C_{\mathrm{lin}}$ is independent of dimension, target, and accuracy. On the same
sequence one must then prove the variable-field inequality with the Bochner Hessian square and
retain the Hodge solenoidal channel.

### Laplace--Brenier proposal

The scout proposes transporting a suitably normalized isotropic product Laplace source to the
target through a rotated Brenier map whose Hessian has a universal operator bound. This is a
transport mechanism, not a relabeling of localization, Route S, CMH, or conditional fibers.
One-dimensional and product calibrations do not decide it. Before route registration, optimize
over the allowed rotations on the uniform simplex and determine whether the Brenier Hessian
must diverge with dimension. This is the bounded kill test; no implication is currently
claimed.

## Prover-ready and near-ready work

| priority | candidate | disposition |
|---|---|---|
| 0 | repaired `prop:weighted-spectator-obstruction` | already in flight; obtain a new cold report before any status change |
| 1 | `prop:spectator-excess-rate-obstruction` | staged `open`; reuse the base selection/stability and fixed-time spectator competitor, drop the weight, prove the $cP_0T$ lower bound, and negate every $W\ge1$ superlinear-remainder rate |
| 1 | `prop:cmh-recovery-calculus` | staged `open` with an active prover: lower floor, invertible invariance, singular-square monotonicity, product max, normal collapse, Gaussian envelope $1$, and product/uniform-simplex envelope at most $4$ |
| 1 | `lem:conditional-fiber-form` and `prop:conditional-fiber-root-obstruction` | the structural closed-form/factor-$4$ bridge and the exact $O(m^{-2})$ root refuter are independently audited; neither decides the universal frame question |
| 1 | `lem:lyapunov-stein-duality` | staged `open`; an author has produced a compiling standalone dossier, but independent review is still required before certification or a formal dependency |
| 2 | exact prefix soft-projector identity | certify the It\^o identity and implication (P3)$\Rightarrow$(P1), with the imported intrinsic low block explicitly conditional |
| 3 | Route-S residue/local-growth equivalence | useful diagnostic lemma, but it does not itself advance the occupation gate |

Further proof-surplus candidates are exact enough to stage as `open`, but rank below the table
above because they do not attack the live gates directly:

- `cor:full-matrix-dissipation`, now staged `open` with an active prover:
  $\mathbb E\int_0^\infty(R_t^2+s_tG_t^2)dt\preceq R_0$; taking a trace can still cost $n$;
- `thm:bootstrap-stopped-interface`: retain the stopping indicators in the certified bootstrap
  proof and replace $\Xi_T$ by its cut-stopped version;
- `thm:fixed-subspace-source-budget`: if the source remains in one deterministic rank-$k$
  block, then $\mathbb E\int S_tdt\le\operatorname{Tr}(P_HR_0P_H)\le k$;
- `prop:stein-rep-second-moment`: the static Stein identity needs finite second, not fourth,
  moments;
- `lem:boundary-flux-general-domain`: convexity is unused once the support-boundary Neumann flux
  is stated explicitly;
- `obs:two-tail-general-weight`: a general scalar slice weight must satisfy
  $w(\Lambda)=\Omega(\Lambda^{5/2})$, not only a pure-power weight; and
- `lem:time-weighted-source-general`: the already-certified time-weighted source lemma does not
  use initial isotropy.

These are proof generalizations, not new gate closures. The stopped bootstrap and noncompact
perimeter variants should wait for the active excess-repair review so that their domain and
supermartingale conventions are inherited from final certified bytes rather than an obsolete
dossier version.

The CMH proof miner also isolated a promising exponential--Gaussian transverse-deficit identity,
schematically $4D-N\ge3\mathbb E(L_{\mathrm{Gauss}}g)^2$ plus eight times a mixed-Hessian
square, and a Dirichlet aggregation surplus. These are not dispatched from this synthesis: the
handoff did not persist the exact definitions, domains, and dependency statement. A bounded
statement-extraction pass must precede a prover.

## Candidates requiring one bounded probe

1. **Laplace--Brenier simplex kill.** Optimize the allowed rotation and compute an analytic
   lower bound on the necessary Brenier-Hessian Lipschitz scale for the isotropic simplex. Admit
   the route only if this test survives.
2. **Uniform-spherical conditional frame.** Analyze $\Lambda_{m,k}$ for the spherical frame at
   the smallest nontrivial degree, or construct the exact all-frame dual certificate. Do not
   rerun the root orbit.
3. **Cut-local weighted replacement.** Test
   $W_t=(1+\lambda_{\mathrm{cut}}(A_t,K_t))^{5/2}$ analytically on Gaussian, two-tail, fixed-block
   products, and exponential spectators, then attack only the consumer-compatible $O(T)$ rate.
   Passing these calibrations changes no status.
4. **CMH transverse-deficit extraction.** Recover the exact exponential--Gaussian identity from
   the certified product/Bochner dossier with all symbols and cores fixed. Decide whether it is
   a genuinely reusable coercive lemma or only a model-specific surplus.
5. **General CMH linear recovery.** Any proposed regularization should first be tested against
   $Q_{\mathrm{lin}}$; do not spend a full variable-field proof before this necessary quotient is
   dimension-free.

No `finum` run is requested. Each remaining decision is an analytic universal statement or an
exact semialgebraic certificate; a floating finite sweep would change no status.

## Literature synthesis

1. The Klartag--Lehec version-2 stopped rank tail and integrated rank-covariance theorem are real
   and underused. Their correct role is covariance-rank control. They contain no cut,
   eigenfunction, source tensor, or eigenspace transport, and remain unreviewed preprint imports.
2. The exponential spectator uses published inputs in exactly the needed strength:
   Klartag--Lehec's event is fixed-time, not persistent, and Bobkov--Chistyakov gives the upper
   density--variance direction needed for an exact-$p_t$ quantile competitor. Tonelli and product
   filtration independence supply the time integral.
3. Sasada's published 2015 negative-rate exchange obstruction is exact prior art for the dead
   root orbit. At symmetric-Dirichlet shape one and exponent $-2$, the source normalization gives
   $\operatorname{gap}(\mathcal D_{\mathrm{root}})\le48/[m(m+1)]$. The repository's
   fixed-$\varepsilon$ cap remains an independent derivation. Caputo proves the constant-rate
   flat-simplex gap, and Carlen--Posta--Toth cover nonnegative exponents; none optimizes over
   arbitrary tight frames.
4. Existing decomposition-of-identity methods support the form's plausibility but do not select
   an all-test frame or reverse the conditional-energy inequality.
5. The Laplace--Brenier literature motivates a transport comparison but supplies no verified
   universal Hessian bound for all isotropic log-concave targets. The simplex test must precede
   promotion.

If the conditional-fiber route is admitted with a manuscript anchor, the orchestrator should
consider the literature scout's published import
`imp:sasada-negative-exchange-obstruction` and its exact bibliography entries for Sasada,
Caputo, and Carlen--Posta--Toth. That import would certify only the coordinate-pair/root orbit;
it creates no edge to the existential all-frame question.

## Promotion and shared battery

Promoted to `research/knowledge/lemmas.md`:

- the cut-oriented Lyapunov duality (L1)--(L5), sourced from agent-certified
  `lem:pathwise-BL`, with direct-sum/two-tail calibration and explicit no-occupation guardrails.

Not promoted:

- the unweighted spectator-rate refuter, pending its own dossier and review;
- the conditional-fiber form and root obstruction, pending standalone dossiers;
- CMH recovery calculus and model surpluses, pending the same;
- either rank-tail reduction, because neither is a certified consumer implication; or
- Laplace--Brenier, which is still a proposal awaiting its first kill test.

No shared-battery edit is made. The exponential spectator cylinder is broadly useful, but its
exact witness family and stronger rate obstruction should enter `research/knowledge/instances.md`
only after the proof cycle. The root simplex and CMH models already have sufficient analytic
registries or are too route-specific to justify another battery row now.

## Duplicate-attempt and harness audit

- The spectral and all-cut rank probes legitimately study different tensors, but both confirm
  the same information mismatch. Future prompts should cite (N1)--(N3) and must not spend a new
  wave multiplying marginal rank probabilities by mean source energies.
- Repeated scalar Riccati plus Brascamp--Lieb deweighting is exhausted. The certified quadratic
  time weight and positive-time cap already identify its endpoint.
- The root-frame cap calculation was shared between a route prober and its literature companion;
  this was complementary source verification, not a conflicting rerun. Future conditional-fiber
  work must optimize over all frames.
- The stronger unweighted spectator observation is a genuine generalization of the weighted
  proof, not a duplicate. It changes the required replacement rate and deserves a separate node.
- Proof miners again found historical perimeter/bootstrapping semantic defects already recorded
  in earlier audits. Those are synchronization tasks, not new mathematical probes; future mining
  prompts should cite the active repair record.

## What is now known jointly

1. The trace-upgrade bottleneck can be stated without an interval-boundary term: certified
   prefix consumption plus the soft-projector identity leaves exactly two motion contractions.
2. Rank information is useful only after an orientation hypothesis. It closes the
   near-full-stable-rank branch, while the two-tail model proves that low-rank temporal alignment
   is unavoidable.
3. A tensor-stable covariance scale exists algebraically. It ignores independent spectators and
   detects the two-tail direction, but its positive-time BL bound remains too singular to solve
   occupation.
4. The weighted route has two independent design failures: global operator-norm weighting and a
   superlinear source-vanishing remainder. Repairing only one leaves the other obstruction.
5. Conditional fibers and Laplace--Brenier are genuinely distinct mechanisms. The first now has
   one killed canonical frame and an exact surviving min--max; the second has not yet passed its
   first simplex test.
6. CMH approximation topology is no longer the vague obstacle. Exact recovery operations are
   understood; the hard content is a dimension-free genuine-Hessian quotient, followed by
   variable-field/solenoidal coercivity.

## Barrier ledger, one line each

- **A1 $\leftrightarrow$ A2:** untouched by this KLS-only wave; no asymptotic consistency delta.
- **A1-bis $\leftrightarrow$ KLS:** untouched; the existing comparison remains a bridge, not a
  proof dependency.
- **Trace-upgrade cluster:** lacks control of the cut-dependent projector-motion contractions;
  no equivalence among the three nodes is proved.
- **Moment-map spectral:** lacks a joint eigenfunction-energy/rank-rotation estimate with the
  mixed block counted twice and coefficient-one damping.
- **Weighted geometric:** requires an $O(T)$, tensor-stable or near-worst-specific replacement
  plus the independent Jacobi/Reilly theorem.
- **Conditional-fiber frame:** root orbit is dead; the all-frame simplex min--max is undecided.
- **Moment-map CMH:** first blocked by bounded linear genuine-Hessian recovery, then by the
  variable-field and solenoidal channels.
- **Laplace--Brenier:** not admitted; optimized simplex Hessian is the first gate.

## Proposed central semantic actions

Ordered by value and dependency:

1. Finish the fresh proof cycle for `prop:weighted-spectator-obstruction`. Only a passing new
   review can support the atomic proposition certification and literal `q:weighted` refutation.
2. Continue the already staged `prop:spectator-excess-rate-obstruction` through a distinct
   prover/reviewer cycle. Do not silently strengthen the existing proposition. Once certified,
   rewrite the weighted gate so every replacement changes both the global weight and the
   superlinear rate, unless it explicitly assumes near-worstness.
3. Replace or supplement the all-interval `q:upgrade` target by the exact tight-prefix assumption
   (P1), whose sufficiency is already certified. Then target (P3), not another eigenvalue tail.
4. Keep `q:mm-spectral-occupation` open and do not wire either rank import to it. Its gate should
   state the local-growth/energy-weighted-rotation target and the factor-two mixed-block rule.
5. Send the completed Lyapunov--Stein candidate dossier to a cold reviewer; continue the active
   CMH recovery-calculus and full-matrix-dissipation provers; and dispatch the conditional-fiber
   structural dossier under a distinct solution key. None changes a general gate status by
   itself.
6. Complete the bounded Laplace--Brenier simplex probe before editing route control. If it fails,
   archive the proposal; if it survives, return to the orchestrator for route admission.
7. Send `q:stein-weighted` to semantic sync: the ledger currently describes a Jacobi/Reilly
   mechanism while the manuscript's operative object is a weighted integral inequality. State
   both the exact demanded inequality and the proposed mechanism without treating them as
   equivalent to `q:upgrade`.
8. Include the proof-miner's CMH semantic debt in that sync wave: make the inverse domain in
   `prop:cmh-hodge` explicit, add the direct Bochner dependency where the Gamma proof uses it,
   repair linear-image provenance, and remove stale `checked_by: none` prose from dossiers whose
   headers now carry certification. These are statement/provenance repairs, not status changes.

The exact new assumption shell supported by the certified consumer is:

```yaml
- id: ass:tight-prefix-carleson
  kind: assumption
  status: open
  route: eldan-localization
  statement: "There exist universal eta in (0,1/6], T0,C0,C1 and alpha<1 such that every isotropic log-concave mu, every fixed cut with |mu(E)-1/2|<=eta/2, and every 0<T<=T0 satisfy E int_0^(T wedge tau_eta) S_t dt <= C0 T + C1 E int_0^(T wedge tau_eta) r_t dt + alpha E int_0^(T wedge tau_eta) D_t dt."
  bounded_by: [obs:two-tail, obs:relative-ceiling, obs:proj-ceiling]
```

Its implication to a universal cut boundary lower bound is already the certified
`cor:tight-window-consumption`; no claim that (P3) proves the new assumption is certified yet.

## Proposed ledger delta

No immediate status, `depends_on`, `refuted_by`, solution, review, or cross-route edge is
warranted from this synthesis. In particular:

- the weighted-spectator proposition still awaits a fresh passing report;
- the staged unweighted rate obstruction, staged CMH calculus, conditional-fiber facts,
  soft-projector reduction, full-matrix dissipation, and staged Lyapunov scale have no passing
  standalone reviews; the Lyapunov author dossier is a candidate only; and
- the rank imports do not imply either stochastic occupation gate.

The orchestrator may add the open `ass:tight-prefix-carleson` shell above because its consumer
implication is already certified, but it must not mark the assumption proved or wire (P3) to it
before a separate dossier and review. No other graph edge leaves the implication tables.

```yaml
outcome: complete
artifacts:
  - research/explorations/2026-08-27-synthesizer-kls-wave-one.md
  - research/knowledge/lemmas.md
proposed_deltas:
  - "No immediate mathematical status, dependency, bridge, refutation, solution, or review delta."
  - "Optionally stage open ass:tight-prefix-carleson exactly as displayed; its sufficiency is already certified by cor:tight-window-consumption, but the soft-projector injection premise is not."
  - "After fresh certification of prop:weighted-spectator-obstruction, apply its literal q:weighted refutation atomically; separately prove the stronger unweighted rate obstruction before changing that status or provenance."
next_role: orchestrator
next_prompt: |
  First finish the repaired prop:weighted-spectator-obstruction cold-review cycle. If and only if
  the new report passes, certify that proposition and refute the literal q:weighted node in one
  synchronized manuscript/ledger/gating update, while leaving thm:intro-weighted conditional as
  an implication. Continue the staged open prop:spectator-excess-rate-obstruction through a
  prover and cold reviewer to formalize the c P0 T unweighted lower bound; do not fold it into
  the already reviewed statement. Supplement q:upgrade with ass:tight-prefix-carleson exactly as displayed
  and direct its next owner to prove the prefix soft-projector injection estimate (P3), with
  gamma<1/8 and only the Dchi/D2chi cut-dependent contractions retained. Keep both
  Klartag--Lehec rank imports unwired to q:upgrade and q:mm-spectral-occupation, and assert no
  equivalence across q:upgrade, high-rank q:stein-weighted, and q:alignment. Continue the active
  lem:lyapunov-stein-duality review cycle and the prop:cmh-recovery-calculus and
  cor:full-matrix-dissipation proof cycles; under a distinct key,
  send the conditional-fiber structural lemma/root obstruction to a prover and then a cold
  reviewer. If that route receives a manuscript anchor, import only Sasada's published root-orbit
  obstruction, never an all-frame refutation. Complete the bounded Laplace--Brenier
  optimized-simplex probe before admitting that route. Finally ask latex-sync to reconcile the
  q:stein-weighted ledger/manuscript object and the listed CMH provenance/domain debts without
  changing status.
```
