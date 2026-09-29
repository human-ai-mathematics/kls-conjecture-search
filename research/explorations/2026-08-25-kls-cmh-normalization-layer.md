---
---
# KLS Route C: the CMH normalization layer, its exact classes, and its two new failure modes

Date: 2026-08-25

Status: repository integration plus independent audit. This record does **not** prove KLS and
does **not** certify universal $\mathrm{CMH}(4)$. It discharges task **M0** of the CMH route and
opens a falsification layer (**M9**, **M10**) that did not exist before.

## Scope

Source: an intermediate working manuscript supplied on 25 August 2026
("Moment-Map Hessians and the KLS Conjecture: Exact Model Cases, Spectral Windows, and a
Transverse-Commutator Obstruction", dated 22 August 2026), together with the 24 August
consolidated summary already triaged in
[`2026-08-25-kls-directional-quotient-triage.md`](2026-08-25-kls-directional-quotient-triage.md).

The manuscript is **not** a later draft of
[`2026-08-24-kls-moment-map-cmh-consolidation.md`](2026-08-24-kls-moment-map-cmh-consolidation.md).
The two share the headline $\mathrm{CMH}(4)$ and essentially no machinery: the 24 August record
is Haar/Bessel compression, Schur--Piola transport, Airy residuals and $[N^{1/2},K_M]$; this one
is the Stein generator, a Hodge splitting, gate zero, and three exact model classes. Route C
therefore now has **two layers**, recorded as such in the route README. Conflating them would
misattribute proofs.

## What was verified and imported

Every claim below was re-derived from scratch before import, then audited independently
(`research/reviews/2026-08-25-kls-cmh-normalization-audit.md`). The manuscript's own status
vocabulary (*Provisional Theorem*, *Computer-assisted Claim*) was **not** carried over; the
repository's R2 contract was applied instead, and only what cleared it was promoted.

### 1. M0 discharged — the endpoint reduction

The originating schema $\lVert\Sigma^{-1/2}H\nabla g\rVert_2^2\le4\lVert{-Lg}\rVert_2^2$ named no
operator. `def:cmh` now fixes all of it: $\Sigma$ is the covariance, $L_\mu$ the Stein generator
$\operatorname{div}_\mu(H\nabla\cdot)$, the space $L^2(\mu)$, the class
$\operatorname{Dom}(\mathsf A)$, inverses pseudoinverses on $(\ker\mathsf A)^\perp$, and
$\Sigma^{-1}$ the Moore--Penrose inverse on the affine tangent space for simplex laws.

`thm:cmh-implies-affine-poincare`: $C_P^{\mathrm{aff}}\le C_{\mathrm{CMH}}$. The proof is one
Cauchy--Schwarz step after $\mathbb Ef^2=\mathbb E\langle\nabla f,H\nabla g\rangle$, plus a
spectral truncation so that no spectral gap is assumed. It uses **only** symmetry, positivity, and
$\operatorname{div}_\mu H=-p$ — not log-concavity, not Monge--Ampère positivity, not the Bochner
identity. That economy is why the constant transfers with no loss, and it means the reduction
holds for any positive symmetric Stein kernel, not only the moment-map one.

### 2. The Hodge splitting — the route's headline may be false

`prop:cmh-hodge`: with $u=H\nabla g$, $h=-\operatorname{div}_\mu u$ and $\psi$ solving
$-\operatorname{div}_\mu(\Sigma\nabla\psi)=h$,
$$
\mathbb E\langle u,\Sigma^{-1}u\rangle
=\mathbb E\langle\Sigma\nabla\psi,\nabla\psi\rangle+\mathbb E\langle w,\Sigma^{-1}w\rangle,
\qquad \operatorname{div}_\mu w=0,
$$
and the first term's operator norm in $h$ is **exactly** $C_P^{\mathrm{aff}}$.

So CMH $=$ KLS $+$ solenoidal excess, and the excess vanishes only in dimension one. **This is the
most consequential thing the normalization layer adds, and it is bad news for the route:**
$\mathrm{CMH}(4)$ can be false while KLS is true. Nothing in the earlier route documents recorded
this; `prog:cmh-route` was being pursued as though its headline were a reformulation of the
conjecture. It is not.

### 3. Gate zero and the exact countermodel

Linear test functions give the necessary condition
$\mathbb E[H\Sigma^{-1}H]\preceq4\Sigma$ (`conj:gate-zero`), i.e. $\mathbb EH^2\preceq4I$ in
isotropic position. The gap to Letwin's theorem is exactly one commutator,
$\operatorname{tr}(B^2H^2)=\operatorname{tr}(BHBH)+\tfrac12\lVert[B,H]\rVert_{\mathrm{HS}}^2$,
and `prop:letwin-not-gate-zero` shows that gap is unconstrained by matrix moments: an exact
$O(m)$-invariant random PSD law with $\mathbb EH=I$ satisfying
$\mathbb E\operatorname{tr}(BHBH)\le2\operatorname{tr}(B^2)$ for **every** symmetric $B$, yet with
$(\mathbb EH^2)_{11}=1+d>4$ for $m\ge18$.

Two disciplines attach to this and were written into the route documents:

- **It is a fence, not a counterexample to gate zero.** No Monge--Ampère or Codazzi condition is
  imposed on those matrices. Reporting it as evidence against `conj:gate-zero` is a category
  error.
- **Gate zero is a trace-upgrade problem.** Chen--Klartag give
  $\operatorname{tr}(\mathbb EH^2)\le2n$, so the average eigenvalue is already $\le2$ and gate zero
  asks the maximum to be $\le4$: an operator-to-trace upgrade with a factor-2 budget, inside the
  ownership cluster of `rem:trace-upgrade-unification`. **Hard constraint 6 applies** — the
  falsification half is dispatchable, the proof half is not, and must be routed to that cluster's
  owner rather than opened as a parallel effort.

### 4. Exact classes, including the route's first nonproduct theorem

- `thm:cmh-1d`: $C_{\mathrm{CMH}}=C_P/\operatorname{Var}$ — an **identity**, because the
  solenoidal channel is empty on the line. Hence $\le4$ for log-concave, sharp at the one-sided
  exponential.
- `thm:cmh-product`: $C_{\mathrm{CMH}}=\max_iC_P(\mu_i)/\operatorname{Var}(\mu_i)$.
- `thm:cmh-dirichlet`: $A(A+1)d_\alpha(g)\le4n_\alpha(g)$ for every $\alpha_i\ge1$ — the first
  genuinely nonproduct family for which Route C has any theorem. Homogeneous Gamma lift, exact row
  completion, constrained Hessian-row minimization under the differentiated Euler identity, and a
  two-branch scalar minimization giving the surplus $s_A$.

Worth recording because it is unusually clean: **log-concavity is spent at exactly one sign** in
the Dirichlet proof, $\delta_i=\alpha_i^2/(\alpha_i+1)^2-1/4\ge0\iff\alpha_i\ge1$. Everything else
is algebra valid for all positive $\alpha$.

## The trap this creates, and the test it opens

`cor:cmh-dirichlet-surplus` gives $s_A>0$ for $A>3$: the Dirichlet family is **strictly inside**
the bound. It is tempting to read that as evidence for universal $\mathrm{CMH}(4)$. It is not, and
`models.md` now says so explicitly, because the product formula locates the saturating direction
elsewhere: **products of one-sided exponentials hit $C_{\mathrm{CMH}}=4$ exactly, with zero
slack.**

Combining that with the Hodge splitting gives the sharpest probe the route has ever had
(**M9**, `q:cmh-solenoidal-perturbation`): perturb a saturating product and compute the second
variation of the solenoidal excess. A strictly positive second variation refutes
$\mathrm{CMH}(4)$. Both ingredients are exact theorems, so this needs no Haar tree, no invariant
lift, and no new operator domains. It should be attempted before M1--M8.

The perturbation family to use is the one already triaged from the 24 August summary — a product
moment potential $\phi(s)+t^2/2$ perturbed by $\varepsilon a(s)b(t)$ — whose delicate ingredient
(vanishing first covariance variation, so whitening is $I+O(\varepsilon^2)$) is what makes it an
admissible isotropic witness.

## What was NOT imported, and why

- **The spectral-window lemma** (band criterion, constant $\tfrac{13}4(2\zeta(2)-1)$) and the
  **high-frequency product tail** $O(\Lambda^{-3/2})$. The abstract almost-orthogonality lemma is
  sound but its entire content is deferred to constructing $\mathsf A_{\mathrm{vec}}$ and proving
  the second band hypothesis, both open. The tail estimate additionally leans on a *polarized*
  rank-one form of Letwin's estimate — for $B=\operatorname{sym}(a\otimes b)$ one has
  $\operatorname{tr}(B^2)=(|a|^2|b|^2+(a\cdot b)^2)/2$, not $|a|^2|b|^2$ — which the source does not
  derive. Given that the same manuscript's countermodel is itself a warning about polarization,
  this step needs writing out before import. Not promoted; recorded here so it is not lost.
- **The row-angle conjecture** $J_b\ge\tfrac14F_b$. Its supporting relations
  $F_b=G_b+J_b$ and $F_b-b^\top\Sigma b\le G_b$ are asserted without derivation, and the evidence
  offered is "survived the low-dimensional tests performed in this exploration" — uncertified
  numerics, barred by hard constraint 2. Not imported in any form.
- **The universal conification construction.** The log-concavity criterion
  $A-n-1\ge\sup_p\nabla V^\top(D^2V)^{-1}\nabla V$ is correct and its Gaussian divergence is a
  genuine no-go for that route, but the accompanying claim that the optimal row calculation
  reproduces the base deficit is stated without the calculation. Left as a route-level note.
- **The chaos/SOS certificate** for symmetric Dirichlet. Correctly quarantined by the source
  itself as unused; under repo rules it needs exact rational certificates, software versions, and
  verifier hashes before it counts as a second proof. Not imported.
- **The variable-$B$ residual term $X_B$.** Only the residual is recorded in the source, not the
  full integrated identity. Left in the construction layer as an open item.

## Corrections made during import

- The manuscript's frontier table and the repository's differ in convention
  ($\psi_n$ vs $\Psi_{\mathrm{KLS}}=h^{-1}$). The repository convention and `rem:psi-convention`
  were kept; no frontier numbers were changed.
- The manuscript states the hypothesis $\alpha_i\le A-2$ in the Dirichlet proof. It is never used:
  the angular minimization is over all $a\ge1$ with no upper constraint. Dropped from the
  dossier; flagged for the auditor to confirm independently.
- The manuscript's endpoint reduction proof handles general $f$ by a bare spectral-resolution
  remark. That is not quite enough, because the $\Sigma$-form and the $H$-form do not commute, so
  a cutoff applied to $f$ does not obviously leave the $\Sigma$-gradient energy controlled. The
  dossier re-runs the estimate on the CMH side with the orthogonal projection instead. This was
  the one place the source's argument needed repair rather than transcription.

## Numerical channel

New `finum` target **`cmh-gate-zero`** covering the normalization layer only: closed-form
one-dimensional Stein kernels, exact Dirichlet moments (calibrated on the uniform-simplex anchor
$2(m+1)/(m+3)$, which must reproduce $1.2$ at $m=2$), exact three-sector verification of the
countermodel, and a Galerkin regression of the Dirichlet surplus. Everything in it is closed-form
or deterministic quadrature — no Monte Carlo — so an exceedance would be a genuine refutation
rather than a directional signal. The target can refute `conj:gate-zero` and
`thm:cmh-dirichlet`; it supports neither.

Extending it to moment maps outside the proved classes (M10) will require numerically solved
Monge--Ampère equations, and those are directional only.

## Ledger effect

Promoted with dossiers and an independent review: `def:cmh`, `prop:cmh-bochner`,
`thm:cmh-implies-affine-poincare`, `prop:cmh-hodge`, `prop:letwin-not-gate-zero`, `thm:cmh-1d`,
`thm:cmh-product`, `cor:cmh-linear-images`, `lem:cmh-gamma-completion`, `lem:cmh-row-min`,
`lem:cmh-angular-coefficient`, `thm:cmh-dirichlet`, `cor:cmh-dirichlet-surplus`,
`cor:cmh-dirichlet-poincare`.

Opened: `conj:gate-zero`, `q:gate-zero`, `q:cmh-solenoidal-perturbation`,
`rem:cmh-stronger-than-kls`, `rem:gate-zero-trace-upgrade`.

`q:cmh-normalization` is marked discharged, with its two residues (uniformity through
approximation; the one-way direction of the reduction) explicitly carried forward rather than
closed. `prog:cmh-route` remains **open**: nothing here proves the headline, and §12 of
`claims.md` now records that the headline may be false.
