# Prover: spectator obstruction to a superlinear excess remainder

Date: 2026-08-27  
Role: `prover` (`/root/prove_spectator_excess_rate_w2`)  
Run id: `w2w01`  
Concurrency key: `solution:prop-spectator-excess-rate-obstruction`  
Ledger node: `prop:spectator-excess-rate-obstruction`  
Dossier: `solutions/prop-spectator-excess-rate-obstruction.tex`  
Dossier SHA-256: `b4bf91df9433ce54deb1d025fca4d3e9f978d0e0d3ec818f0d4cdcd986b334be`  
Certification state: `checked_by: none`

## Result stated

For every $C,T_0,\gamma>0$, every $\eta\in(0,1/2)$, and every $\delta>0$, the dossier
constructs a dimension $d$, the isotropic product $\mu=\lambda^{\otimes d}$ of centered
rate-one one-sided exponentials, a balanced finite-perimeter cylinder $E$, and a time
$0<T\le T_0$ such that

$$
e_0(E)\le\delta,
\qquad
\frac{e_0(E)}{I_\mu(1/2)}\le\delta,
$$

but

$$
\mathbb E\int_0^{T\wedge\tau_\eta}e_t(E)\,dt
>C\bigl(Te_0(E)+T^{1+\gamma}\bigr).
$$

The construction also has $e_0(E)\le1$. The proof is unweighted from the outset; it does not
deduce this result from the global-operator-norm weighted obstruction. Thus, within the usual
normalized class $W_t\ge1$, a tensor-stable or cut-local replacement weight alone cannot
preserve the source-vanishing superlinear remainder. An $O(T)$ remainder, a remainder tied to a
nonlocalized source deficit, or an explicit near-worst-measure premise remains compatible with
this proposition.

## Analytic construction

Let $\lambda$ be the centered rate-one exponential and set
$a_m=I_{\lambda^{\otimes m}}(1/2)$. Cylinder extension shows $a_{m+1}\le a_m$.
`prop:products` and `lem:half` give a universal floor $a_m\ge a_*>0$, so
$a_m\downarrow a_\infty\ge a_*$.

Set

$$
h_{\mathrm{sp}}=1-e^{-1/2},
\qquad
\kappa_{\mathrm{sp}}=\frac{h_{\mathrm{sp}}}{128}.
$$

Given the proposed constants, choose

$$
0<\varepsilon<
\min\left\{\delta,\delta a_*,1,
\frac{\kappa_{\mathrm{sp}}a_*}{4C}\right\}.
$$

Choose $M$ with $a_M-a_\infty<\varepsilon/2$ and then a regular exact-half-mass base
$E_0\subset\mathbb R^M$ whose perimeter $P_0$ satisfies
$a_M\le P_0\le a_M+\varepsilon/2$. For every later $N$ the cylinder
$E_0\times\mathbb R^N$ has perimeter $P_0$ and

$$
0\le e_0(E_0\times\mathbb R^N)<\varepsilon,
\qquad
\frac{e_0(E_0\times\mathbb R^N)}
{I_{\lambda^{\otimes(M+N)}}(1/2)}<\frac\varepsilon{a_*}.
$$

This fixes both additive and relative near-minimality before time and spectator dimension are
chosen.

The base selection is made directly in the exact noncompact exponential product. The dossier
spells out weighted-BV strict approximation, an exact-mass correcting flow, equality of regular
relative BV and ambient lower Minkowski perimeter, and the posterior density-change formula

$$
(\nu_{u,t})^+(E_0)=\int F_{u,t}\,d\sigma_0
$$

whenever the tilt normalizer is finite. No compact surrogate of the covariance-spike measure is
introduced.

In the planted observation model $c_t=tX+B_t$, posterior factorization separates the base block
from all spectator coordinates. A base event $G_b$ of probability at least $1/4$, depending
only on the base latent variable and Brownian path, keeps

$$
|p_t-1/2|<\eta,
\qquad
P_t(E_0\times\mathbb R^N)\ge P_0/8
$$

simultaneously on a fixed interval $[0,T_b]$. The event and $T_b$ are independent of $N$.
This uses uniform $L^1$ continuity of finite-dimensional small tilts, a compact patch carrying
at least half of the base perimeter, and a reflected-Brownian union bound.

At each deterministic $t>0$, the published exponential covariance-spike event, with the exact
channel conversion $s=1/t$, gives

$$
H_t=\left\{\max_{1\le i\le N}v_{i,t}\ge c_{\mathrm{sp}}/t\right\},
\qquad
\mathbb P(H_t)\ge1-\left(1-\tfrac12e^{-1/t}\right)^N.
$$

If $\log N\ge2/T$, then $\mathbb P(H_t)\ge h_{\mathrm{sp}}$ separately for every
$t\in[T/2,T]$. On $H_t$, a $p_t$-quantile halfline in a high-variance spectator coordinate
has full-product mass exactly $p_t$. The one-dimensional density--variance estimate yields

$$
I_{\mu_t}(p_t)
\le f_{i,t}(q_{i,t})
\le v_{i,t}^{-1/2}
\le\sqrt{t/c_{\mathrm{sp}}}.
$$

Thus, after choosing $T\le T_b$ and
$T\le c_{\mathrm{sp}}P_0^2/256$, one has
$e_t(E)\ge P_0/16$ on $G_b\cap H_t$ for every deterministic $t\in[T/2,T]$.
Base/spectator independence gives
$\mathbb P(G_b\cap H_t)\ge h_{\mathrm{sp}}/4$. Nonnegative Tonelli, using only these
fixed-time events, then gives the unweighted lower bound

$$
\mathbb E\int_0^{T\wedge\tau_\eta}e_t(E)\,dt
\ge \frac{P_0}{16}\frac{h_{\mathrm{sp}}}{4}\frac T2
=\kappa_{\mathrm{sp}}P_0T.
$$

The initial choice of $\varepsilon$ makes
$Ce_0(E)<\kappa_{\mathrm{sp}}P_0/4$. Choose $T$ with
$T^\gamma<\kappa_{\mathrm{sp}}P_0/(4C)$, and only then choose finite $N$ with
$\log N\ge2/T$. The proposed upper bound is then strictly less than half the displayed lower
bound.

The load-bearing quantifier order is

$$
(C,T_0,\gamma,\eta,\delta)
\longrightarrow(\varepsilon,M,E_0,P_0,T_b)
\longrightarrow T
\longrightarrow(N,d,\mu,E).
$$

## Dead ends and failure modes excluded

- A persistent spectator-spike event is unavailable from the imported theorem and is not used.
  The event $H_t$ varies with deterministic time; Tonelli integrates its marginal probability.
- A spectator median cut would have mass $1/2$, not the random tracked mass $p_t$. The proof
  uses the exact $p_t$-quantile, so it is a legitimate competitor for $I_{\mu_t}(p_t)$.
- Selecting a new approximate minimizer after the final dimension would obscure the required
  independence and quantifier order. The monotone half-profile limit fixes the finite base first
  and makes its near-minimality uniform in all cylinder extensions.
- Compactifying the exponential prior would detach the argument from the published spike input.
  The weighted-BV lemma works directly for the exact exponential support.
- No lower bound on a moving localized isoperimetric profile is assumed. The only profile input
  after time zero is an upper bound from an explicit competitor.
- The unweighted conclusion is proved directly. The dossier never drops a weight from a proved
  weighted inequality or otherwise relies on `prop:weighted-spectator-obstruction`.

No analytic step is marked open under the stated hypotheses.

## Compatibility, dependencies, and fences

The four ledger dependencies are used exactly as declared:

- `prop:covariance-spike`: the fixed-time event only;
- `lem:one-dimensional-density-variance`: the quantile-halfline perimeter bound;
- `prop:products` and `lem:half`: a positive dimension-free lower floor for the half-profile.

All are proved nodes or published imports. The proposition has no `bounded_by` edge. It respects
the neighbouring circularity warning by inserting an explicit upper profile competitor, does not
make a two-tail or trace-upgrade-cluster implication, and uses no numerical evidence.

There is no conflict with `prop:trivial-excess`: that proposition gives an $O(T)$ upper bound,
while this obstruction gives an $O(T)$ lower bound and rules out only a coefficient that vanishes
uniformly with $e_0$ and $T^\gamma$. There is no conflict with `thm:bootstrap`: no near-worst
premise is supplied, and the bootstrap retains $h_\mu(T^{4/3}+\Xi_T)$ rather than the uniform
remainder refuted here. There is no conflict with product KLS because every witness already has a
dimension-free KLS constant; KLS does not assert this excess-propagation rate.

## Validation and deferred provenance

The forced standalone build

```text
cd solutions && latexmk -g -pdf -outdir=../build prop-spectator-excess-rate-obstruction.tex
```

completed successfully and produced a six-page PDF. Both bibliography citations resolve. The
remaining `??` entries are only expected standalone cross-module references. A
layout-preserving PDF extraction was inspected: the base-perimeter comparison, the
one-dimensional profile chain, the fixed-time probability, the Tonelli constant, and the final
strict inequality all render correctly. The log has no TeX error, undefined control sequence,
missing-math insertion, runaway argument, emergency stop, or fatal error.

There is no applicable ledger delta from an unreviewed dossier. If and only if a distinct cold
reviewer passes it, the deferred candidate is
`solution: solutions/prop-spectator-excess-rate-obstruction.tex`.

```yaml
outcome: complete
artifacts:
  - solutions/prop-spectator-excess-rate-obstruction.tex
  - research/explorations/2026-08-27-prover-spectator-excess-rate-obstruction-w2w01.md
proposed_deltas:
  - "No applicable ledger delta before independent review; deferred solution candidate: solutions/prop-spectator-excess-rate-obstruction.tex."
next_role: proof-checker
next_prompt: |
  Cold-review `solutions/prop-spectator-excess-rate-obstruction.tex` at SHA-256
  `b4bf91df9433ce54deb1d025fca4d3e9f978d0e0d3ec818f0d4cdcd986b334be` against the exact
  manuscript and ledger statement of `prop:spectator-excess-rate-obstruction`. Reconstruct the
  proof from repository artifacts. Verify all theorem quantifiers, both additive and relative
  near-minimality estimates, and the extra e0<=1. Audit the monotone positive half-profile limit;
  the regular exact-mass base selection in the exact noncompact exponential product; the
  lower-Minkowski/relative-BV and posterior density-change conventions; planted posterior
  factorization; the positive-probability base event uniformly controlling mass and perimeter;
  and base/spectator independence. Check the imported covariance spike only at each fixed time,
  the exact s=1/t conversion, log N>=2/T, and the exact-p_t quantile competitor. Verify the
  unweighted Tonelli lower bound kappa_sp P0 T with kappa_sp=(1-e^(-1/2))/128, the choices
  e0<<P0/C and T^gamma<<P0/C, the strict final comparison, and the full
  base-before-T-before-N quantifier order. Confirm compatibility with prop:trivial-excess,
  thm:bootstrap, and product KLS, and confirm that no weighted inequality, persistent event,
  moving-profile lower bound, numerical input, KLS refutation, or trace-cluster implication is
  used. Recompile standalone and inspect the rendered PDF. The reviewer must be distinct from
  `/root/prove_spectator_excess_rate_w2`, must write one NEW append-only review, and must not edit
  the dossier, manuscript, ledger, routes, gating, bibliography, prior explorations, or prior
  reviews. If and only if every step passes, return the exact atomic certification delta to the
  orchestrator; otherwise return a verbatim repair prompt.
```
