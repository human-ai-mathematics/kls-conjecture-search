---
---

# Repair of the August 25 Riccati and bootstrap dossiers

## Question examined

Starting lens: prove. Repair corrections 1–4 of
[the grouped revise report](../reviews/2026-10-04-aug25-grouped-revise.md)
while preserving the twelve canonical statements. This is maintenance of the
existing implications toward `conj:kls`, not a new portfolio route.

Repair author: researcher /root/aug25_grouped_repair, gpt-6-astra, 2026-10-04.
The dossiers were held frozen until the orchestrator's explicit GO after the
original reviewer finished validation. Only the two dossiers below and this
new checkpoint were edited by this author.

## What we learned

*Established (argument written, uncertified).* In
`solutions/kls-localization-riccati-core.md`, the proof of
[](#cor:tight-window-consumption) now sums [](#cor:per-direction) in a fixed
orthonormal basis before any use of the Carleson premise. This gives
$\mathbb E\int_0^T S_t\,dt\le\operatorname{Tr}R_0\le n$.
Stopped scalar Riccati expectations, monotone convergence for the source and
Fatou for the terminal and dissipation terms then give
$\mathbb E r_{T\wedge\tau_\eta}+\mathbb E\int_0^{T\wedge\tau_\eta}D_t\,dt\le1+n$.
Thus $u$ is locally integrable and every term is finite before absorption.
The premise is applied only on its original deterministic prefixes, after
auxiliary stops are removed. The dimension enters only the finiteness argument;
the subsequent dimension-free Gronwall and survival constants are unchanged.

*Established (argument written, uncertified).* The same dossier's header,
overview, scope paragraph, Section 2, tight-window conclusion reference and
endpoint audit now distinguish its six active claims from the separate
[](#lem:survival-implies-kls). The obsolete internal survival proof and its
general reduced-boundary assertion were removed. Section 2 points to
`solutions/lem-survival-implies-kls.md` and applies its deterministic-time
bridge with $b_0=1/3,c_0=1/2$. The new regularity paragraph uses original
posterior polynomial moments, an exponential majorant near zero, Gaussian
majorants away from zero and local moment/martingale stops. A measurable cut
is a bounded multiplier of polynomial tests; no cut smoothing is used.
The matrix/scalar algebra and away-from-zero formulas are unchanged.

*Established (argument written, uncertified).* In
`solutions/kls-bootstrap-interface.md`, the proof of [](#lem:half) now uses
Milman's interior concavity and symmetry (Corollaries 6.5 and 6.12). For
$0<\varepsilon<p<q\le1/2$, nonnegativity gives
$I(p)\ge (p-\varepsilon)I(q)/(q-\varepsilon)$; taking
$\varepsilon\downarrow0$ proves the ratio inequality. Assigned $I(0)=0$
is explicitly distinguished from the potentially positive one-sided limit.
The affine-hull reduction and vacuous Dirac case are stated. The canonical
identity $h_\nu=2I_\nu(1/2)$ is unchanged.

*Established (argument written, uncertified).* The statement and final proof
paragraph for [](#prop:ceiling) retain the exact quantified implication:
fix $\kappa\in(0,1]$ and a universal $T_0>0$ with
$9(1+\kappa)T_0\le1/2$; if $\Xi_{T_0}(\mu)\le\kappa T_0$ for every
isotropic log-concave $\mu$, KLS follows. The final paragraph now explicitly
separates that all-measure sufficient condition from the near-worst scope of
[](#thm:bootstrap), from the actual excess, and from the additional initial
term $Te_0$. No converse, equivalence, propagation impossibility, or automatic
circularity is inferred. Its quantitative martingale proof is unchanged.

## What resists

These are proposed repairs, not certifications. No new claim of mathematical
correctness or target progress follows from the edits. All four assigned
corrections have corresponding edits; the canonical manuscript proof and
explanatory prose corrections remain the writer's responsibility, and relation
changes remain the orchestrator's responsibility. No numerical experiment is
used and no canonical statement, program file, manuscript, review, or third
dossier was edited by this author.

Fence check: none of the twelve repaired-scope nodes has a `bounded_by` edge.
The existing methodological constraints remain: `rem:profile-circularity`
(no moving-family profile supermartingale), `rem:crude-insufficient` (the
crude upper estimate alone supplies no small certificate), and
`rem:relative-ceiling` (one-way sufficiency only). No open premise is discharged.
The tight-window result still assumes its original prefix Carleson estimate;
[](#cor:loglog) still consumes the existing proved covariance-window input.
No route state changes are proposed.

## Proposed next step

Obtain a fresh independent review of the stabilized two dossiers against the
full twelve-node scope in the revise report. In particular, check the new
original-posterior regularity paragraph, the finite-source removal of stops,
the interior-concavity proof at nonsmooth/affine supports, and the precise
quantifier scope of the ceiling. Retain the prior report as history.

Exact relation proposals for the orchestrator:

- [](#cor:tight-window-consumption):
  `depends_on: [thm:scalar-riccati, cor:per-direction, lem:survival-implies-kls]`.
- [](#prop:ceiling):
  `depends_on: [lem:survival-implies-kls, thm:bootstrap]`.

Neither is a status change. No applicable certification delta is supplied.

Build handoff: `UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py`
completed after the dossier edits via the approved execution path. It exited
with only twelve stale dossier-certification failures, one for each owned
node. It reported no MyST error or additional structural error. Those stale
fingerprints are expected until independent re-review; they are not replaced
by this author. The checkpoint was added after that build and contains no
candidate or other state mutation.
