---
---
# Prover: exponential-spectator obstruction

Date: 2026-08-27

Role: `prover`

Run id: `w0w02`

Concurrency key: `solution:prop-weighted-spectator-obstruction`

Ledger node: `prop:weighted-spectator-obstruction`

Artifact: `solutions/prop-weighted-spectator-obstruction.tex`

Certification: `checked_by: none`

## Outcome

A standalone analytic dossier now proves the current candidate statement: for every
$C,T_0,\gamma>0$, $\eta\in(0,1/2)$, and $\delta>0$, a sufficiently high product of centered
one-sided exponentials has a balanced finite-perimeter cylinder with both
$e_0\le\delta$ and $e_0/I_\mu(1/2)\le\delta$ that violates the literal
global-operator-norm weighted rate at some $T\le T_0$. The construction additionally has
$e_0\le1$, so it lies in the explicit quantifier class of `conj:weighted-excess-rate`.

The result attacks only the global weight used by the current gate. It does not attack KLS:
the same product theorem used in the proof gives a dimension-free KLS bound for every witness.

## Proof architecture

1. For $\lambda$ the centered rate-one one-sided exponential, set
   $a_m=I_{\lambda^{\otimes m}}(1/2)$. Cylinder extension gives
   $a_{m+1}\le a_m$, while `prop:products` and `lem:half` give a universal positive lower
   bound. Thus $a_m\downarrow a_\infty>0$.
2. Choose $M$ near the limit and a regular weighted-BV half-volume competitor $E_0$ in
   $\lambda^{\otimes M}$. This base is fixed before either $T$ or $N$. For every later
   spectator count $N$, the cylinder $E_0\times\mathbb R^N$ has uniformly small additive and
   relative excess.
3. In the planted Gaussian observation realization, posterior factorization makes mass,
   cylinder perimeter, and $\tau_\eta$ base-measurable and independent of the spectator
   process.
4. A base event of probability at least $1/4$ keeps
   $|p_t-1/2|<\eta$ and the cylinder perimeter at least $P_0/8$ for all $t\le T_b$. The proof
   uses direct $L^1$ small-tilt continuity and the exact weighted-perimeter density-change
   formula.
5. At each deterministic $t\in[T/2,T]$, Klartag--Lehec Proposition 65 is used only in its
   fixed-time event form, with the exact conversion $s=1/t$. On the spike event, the
   Bobkov--Chistyakov density bound supplies a spectator-coordinate halfline of the actual
   random mass $p_t$ and perimeter at most $\sqrt{t/c_{\rm sp}}$.
6. Base/spectator independence and Tonelli give a lower bound
   $\kappa_{\rm sp}P_0T^{-3/2}$. Choosing $T$ small and only then choosing
   $N\ge e^{2/T}$ makes this exceed $C(Te_0+T^{1+\gamma})$.

The final quantifier order is
$$
(C,T_0,\gamma,\eta,\delta)
\longrightarrow(\varepsilon,M,E_0,P_0,T_b)
\longrightarrow T
\longrightarrow N.
$$

## Regularization and perimeter convention

The witness law remains the exact noncompact exponential product. The dossier does not pass the
covariance-spike statement through a compact approximation. Instead it proves the needed
selection and density-change layer directly:

- finite outer Minkowski content dominates relative weighted-BV perimeter;
- compact truncation, smooth approximation in support charts, coarea, and a local smooth flow
  produce an exact-mass regular relative competitor with arbitrarily small perimeter loss;
- for this regular set, ambient outer Minkowski content equals relative weighted surface area
  inside the convex support;
- multiplying the volume density by the posterior factor $F_{u,t}$ multiplies the relative
  perimeter measure by the same factor; support-boundary pieces contribute no artificial term.

This is precisely the regularity needed for the uniform lower bound on localized cylinder
perimeter.

## Dead ends avoided or resolved

- **Persistent spike:** the primary source gives no common path event on $[T/2,T]`. The dossier
  uses a different event $H_t$ at each deterministic time and integrates its marginal lower
  bound by nonnegative Tonelli.
- **Half-mass spectator cut:** after localization the tracked mass is $p_t$, not $1/2$. A fixed
  median halfline would not bound $I_{\mu_t}(p_t)$. The proof uses the exact $p_t$-quantile.
- **Base chosen after dimension:** choosing a new near-minimizer after $N$ would not give the
  independence/quantifier structure required by the obstruction. Monotonicity of $a_m$ fixes a
  finite base first and makes its near-minimality uniform in all extensions.
- **Compact-law approximation:** compactifying the exponential law would detach the proof from
  the imported covariance-spike theorem. The direct weighted-BV formula above removes that
  detour.
- **Profile lower bound:** no posterior isoperimetric lower bound is inserted. The only profile
  comparison is an upper bound from an explicit spectator quantile cylinder.

No analytic step remains marked open in the dossier. This statement still has no proof value
until a distinct cold reviewer checks the complete argument.

## Dependencies, fences, and hypotheses used

Dependencies are exactly
`[prop:covariance-spike, lem:one-dimensional-density-variance, prop:products, lem:half]`.
All are published imports or proved nodes, so the candidate is unconditional relative to the
repository's accepted inputs. The node has no `bounded_by` entry. The nearby `rem:two-tail-slice-bounds`
calibration is respected because the proof retains exponent $5/2$; `rem:profile-circularity` is evaded
by the explicit profile competitor. No trace-upgrade claim is made.

Additional standard analytic facts actually used are weighted-BV strict approximation and
density change, local exponential integrability of a finite exponential product, the planted
Gaussian posterior representation, Brownian reflection, and Tonelli. No numerical evidence is
used.

## Validation

- Standalone command:
  `cd solutions && latexmk -pdf -outdir=../build prop-weighted-spectator-obstruction.tex`
- Result: success; PDF emitted at `build/prop-weighted-spectator-obstruction.pdf`.
- The remaining `??` warnings are only cross-module references, which are expected for a
  standalone subfile. Both bibliography citations resolve.
- `python3 research/check_ledger.py`: 0 errors (185 nodes at validation time).
- `git diff --check -- solutions/prop-weighted-spectator-obstruction.tex
  research/explorations/2026-08-27-prover-weighted-spectator-obstruction-w0w02.md`: clean.

## Deferred control-plane delta

There is no applicable ledger delta from an unreviewed dossier. If and only if a distinct
proof-checker passes the proof, the deferred candidate solution is
`solutions/prop-weighted-spectator-obstruction.tex`. Any resulting `conj:weighted-excess-rate` refutation
transition belongs to the orchestrator and must name the certified proposition as its refuter;
this prover changes neither node.

```yaml
outcome: complete
artifacts:
  - solutions/prop-weighted-spectator-obstruction.tex
  - research/explorations/2026-08-27-prover-weighted-spectator-obstruction-w0w02.md
proposed_deltas:
  - "No applicable ledger delta before independent review; deferred solution candidate: solutions/prop-weighted-spectator-obstruction.tex."
next_role: proof-checker
next_prompt: |
  Cold-review `solutions/prop-weighted-spectator-obstruction.tex` against the exact manuscript
  statement and ledger node `prop:weighted-spectator-obstruction`. Verify the theorem for every
  C,T0,gamma>0, eta in (0,1/2), and delta>0, including both e0<=delta and
  e0/I_mu(1/2)<=delta and the additional e0<=1 needed to refute literal conj:weighted-excess-rate. Check the
  monotonicity and positive limit of a_m=I_{lambda^m}(1/2) from prop:products plus lem:half;
  verify that the regular exact-mass base competitor is selected before T and N and that the
  weighted-BV, support-boundary, outer-Minkowski, and density-change conventions are valid for
  the exact one-sided-exponential product. Check planted posterior factorization, base/spectator
  independence, the simultaneous base event keeping tau_eta>T_b and perimeter >=P0/8, and every
  constant in its probability estimate. Audit the imported Klartag--Lehec event only at each
  fixed time, the exact s=1/t conversion, the condition log N>=2/T, and the
  Bobkov--Chistyakov p_t-quantile competitor. Verify the Tonelli calculation, the
  kappa_sp constant, and the strict final comparison while preserving base -> T -> N. Confirm
  that no persistent spike, posterior-profile lower bound, numerical input, KLS refutation, or
  trace-cluster implication is claimed. Recompile standalone. If every step passes, persist a
  proof review for the single node with author `/root/prove_weighted_spectator_obstruction` and
  return the exact atomic certification/refutation delta to the orchestrator; otherwise return
  a verbatim repair prompt. Do not edit the dossier, manuscript, ledger, routes, gating, or
  bibliography.
```
