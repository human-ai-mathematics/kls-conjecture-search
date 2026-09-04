---
type: exploration
date: "2026-08-27"
outcome: proposed
nodes:
  - ass:cmh-recovery-envelope
  - cor:cmh-recovery-sequence-suffices
  - def:cmh
  - lem:affine-poincare-w2-liminf
---
# CMH recovery sequence and affine-Poincaré $W_2$ lower semicontinuity

**Date:** 2026-08-27  
**Role:** `prover` (`/root/prove_cmh_recovery`)  
**Run:** `w0c01`  
**Targets:** `lem:affine-poincare-w2-liminf`, `cor:cmh-recovery-sequence-suffices`  
**Outcome:** one standalone candidate dossier proves the unconditional lower-semicontinuity
lemma and the conditional one-recovery-sequence implication. It remains unreviewed
(`checked_by: none`) and has no ledger value.

## What was attempted

The certified approximation mechanism in `solutions/q-cmh-approximation.tex` was separated into
two logically distinct claims:

1. a CMH-free lower-semicontinuity theorem for the affine Poincaré constant under ambient
   $W_2$ convergence, including degeneration to a proper affine support; and
2. the short conditional implication from one recovery sequence with bounded
   $\liminf C_{\mathrm{CMH}}$ to KLS.

The proof audit explicitly checked the common ambient core, covariance convergence, the fixed
liminf subsequence, intrinsic affine-support forms, the published compact-target hypotheses,
and the exact closed Stein-form endpoint. No numerical work was run or used.

## Statements proved

For a centered log-concave probability $\mu$ on $\mathbb R^n$, there is a sequence of centered,
full-dimensional, compactly supported regular moment-map laws $\mu_k$ with
$W_2(\mu_k,\mu)\to0$. More strongly, for every centered log-concave sequence $\nu_k$ with
$W_2(\nu_k,\mu)\to0$,

$$
C_P^{\mathrm{aff}}(\mu)
\le \liminf_{k\to\infty} C_P^{\mathrm{aff}}(\nu_k).
$$

Under the explicit unresolved premise `ass:cmh-recovery-envelope`, which supplies one regular
sequence satisfying

$$
\liminf_{k\to\infty} C_{\mathrm{CMH}}(\mu_k)\le C,
$$

the certified regular endpoint gives

$$
C_P^{\mathrm{aff}}(\mu)
\le\liminf_k C_P^{\mathrm{aff}}(\mu_k)
\le\liminf_k C_{\mathrm{CMH}}(\mu_k)
\le C.
$$

Thus the corollary preserves the constant and implies KLS conditionally on precisely the
recovery-envelope premise. It does not assert continuity or lower semicontinuity of
$C_{\mathrm{CMH}}$.

## Construction of regular recovery

For $X\sim\mu$ and an independent $G\sim N(0,I_n)$, first set

$$
\lambda_\delta=\mathcal L(X+\sqrt\delta G).
$$

This is centered, smooth, positive, full-dimensional, and log-concave, with

$$
W_2^2(\lambda_\delta,\mu)\le n\delta,
\qquad
\operatorname{Cov}(\lambda_\delta)=\Sigma+\delta I_n.
$$

If $q_\delta$ is its density, tilt and truncate it by

$$
d\widetilde\mu_{\delta,\varepsilon,R}(x)
=Z_{\delta,\varepsilon,R}^{-1}
\mathbf 1_{B(0,R)}(x)q_\delta(x)e^{-\varepsilon|x|^2/2}\,dx,
$$

then recenter. For fixed $\delta$, dominated convergence of the relative densities with the
weight $1+|x|^2$ gives $W_2$ convergence back to $\lambda_\delta$. Choosing
$\delta_k=k^{-4}$ and the remaining parameters diagonally gives the ambient estimate

$$
W_2(\mu_k,\mu)<\frac2k+\frac{\sqrt n}{k^2}.
$$

After recentering, the support is a translated ball and its interior density is the restriction
of a positive smooth ambient function. The law is centered and full-dimensional. Therefore the
published theorem `thm:regular-moment-map-compact-target` applies and supplies the canonical
positive Stein kernel with weak zero flux and mean equal to the covariance.

## Common core and affine-support degeneration

Let $S=\operatorname{Ran}\Sigma$. On globally Lipschitz functions on $S$, the limiting form is

$$
\mathcal E_{\Sigma,\mu}(f)
=\int_S\langle\Sigma_S\nabla_Sf,\nabla_Sf\rangle\,d\mu.
$$

Local equivalence of the intrinsic log-concave density with Lebesgue measure and positivity of
$\Sigma_S$ prove closability and identify the zero-energy kernel with constants. The following
three form-norm approximations prove that $\mathbb R+C_c^\infty(S)$ is a core:

1. truncate the values of a Lipschitz function;
2. multiply a bounded function by expanding smooth spatial cutoffs;
3. mollify a compactly supported Lipschitz function intrinsically on $S$.

This intrinsic core equals the restriction of the single ambient core
$\mathbb R+C_c^\infty(\mathbb R^n)$. If two ambient extensions agree on $S$, their gradient
difference is normal, while

$$
\Sigma=P_S\Sigma_SP_S,
\qquad
\Sigma^+=P_S\Sigma_S^{-1}P_S
$$

annihilate normal directions. This is the entire affine-support convention used by the proof.
When $\dim S=0$, centeredness gives $\mu=\delta_0$ and
$C_P^{\mathrm{aff}}(\mu)=0$.

No whitening is performed before the limit. In particular, no canonical moment-map kernel is
pushed through a noninvertible limiting map.

## Covariance convergence and the liminf subsequence

Ambient $W_2$ convergence admits couplings with $X_k\to X$ in $L^2$. Cauchy--Schwarz then gives
entrywise, hence operator-norm, covariance convergence $\Sigma_k\to\Sigma$.

For one fixed ambient test $F\in\mathbb R+C_c^\infty(\mathbb R^n)$, weak convergence gives
convergence of the variance. Covariance convergence and weak convergence of the bounded
continuous integrand give

$$
\int\langle\Sigma_k\nabla F,\nabla F\rangle\,d\nu_k
\longrightarrow
\int\langle\Sigma\nabla F,\nabla F\rangle\,d\mu.
$$

If $L=\liminf_kC_P^{\mathrm{aff}}(\nu_k)<\infty$, one subsequence on which the constants
converge to $L$ is selected before any test function is considered. Every common-core
inequality passes along that same subsequence. Intrinsic core density then extends the limit
inequality to the entire closed covariance-form domain. If $L=\infty$, the claim is immediate.

## Exact regular CMH endpoint

For a compact-target regular law with canonical kernel $H$, the ambient restriction form

$$
\mathcal E_H(f)=\int\langle H\nabla f,\nabla f\rangle\,d\mu
$$

is finite on the smooth core because $\mathbb EH=\Sigma$. Local positivity and smoothness of
$H$ and of the density prove closability by closedness of distributional differentiation; the
same argument makes its kernel exactly the constants. The global weak Stein identity identifies
the Friedrichs operator with the closed Stein generator in `def:cmh`, without an unrecorded
boundary condition or maximal-domain convention. The certified theorem
`thm:cmh-implies-affine-poincare` therefore applies pointwise along every regular recovery
sequence:

$$
C_P^{\mathrm{aff}}(\mu_k)\le C_{\mathrm{CMH}}(\mu_k).
$$

## Dependencies, hypotheses, and fences

- `lem:affine-poincare-w2-liminf` depends only on the imported published node
  `thm:regular-moment-map-compact-target`. The lower-semicontinuity part is elementary; the
  import is used only to certify that the constructed compact approximants belong to the
  regular moment-map class.
- `cor:cmh-recovery-sequence-suffices` depends on the open
  `ass:cmh-recovery-envelope`, the lemma, the definition `def:cmh`, and the proved endpoint
  `thm:cmh-implies-affine-poincare`.
- Centeredness is used to identify the affine hull with $\operatorname{Ran}\Sigma$, preserve
  the barycenter in the construction, and obtain covariance convergence directly from second
  moments.
- Log-concavity is used for the intrinsic density and is preserved by smoothing, Gaussian tilt,
  convex truncation, and translation.
- Finite-dimensionality is used in covariance convergence and the moment-map theorem.
- No isotropy, smoothness or full-dimensionality of the limiting law, pre-existing spectral
  gap, or numerical input is used.

Neither node has a `bounded_by` edge. The proof does not use any fixed-cut, projection,
localization occupation, trace-upgrade, or moving-competitor claim, so none of the catalogued KLS
fences is crossed.

## Dead ends and corrections retained

1. Merely proving existence of one lower-semicontinuous approximation sequence would not
   justify applying the lemma to a potentially different sequence supplied by the recovery
   assumption. The dossier avoids this quantifier mismatch by proving lower semicontinuity
   along every centered log-concave $W_2$-convergent sequence.
2. Whitening the full-dimensional approximants is harmless individually but divergent in
   collapsing normal directions. The proof stays in original ambient coordinates and uses the
   covariance form, so no singular unwhitening limit is needed.
3. A bound on $\liminf C_{\mathrm{CMH}}$ does not require and does not imply any continuity of
   $C_{\mathrm{CMH}}$. Only the pointwise regular inequality
   $C_P^{\mathrm{aff}}\le C_{\mathrm{CMH}}$ is passed through the liminf.
4. Invoking the formal differential expression for the Stein generator without checking its
   closed form would leave a boundary/domain gap. The dossier verifies closability, constant
   kernel, and the weak zero-flux realization before using the certified endpoint.
5. The first standalone TeX run exposed the undefined shorthand `\\Ran`; it was replaced by
   `\\operatorname{Ran}`. The resulting failure was purely mechanical and no mathematical step
   depended on it.

## Artifact, validation, and certification boundary

Candidate dossier: `solutions/lem-affine-poincare-w2-liminf.tex`.

The required command

`cd solutions && latexmk -pdf -outdir=../build lem-affine-poincare-w2-liminf.tex`

succeeds and produces `build/lem-affine-poincare-w2-liminf.pdf` (five pages). The final log has
no TeX error, undefined control sequence, overfull box, or underfull box. Its unresolved
cross-manuscript references are expected for a standalone subfile under `solutions/README.md`.
The source SHA-256 at this stage is
`929482e5360db8782d1defd95a27547cc54fcaca957e529dadde8a34e56f4e22`.

The dossier intentionally records `checked_by: none`. There is no applicable ledger delta now.
Only after a distinct proof-checker passes the dossier may the orchestrator atomically point both
nodes to the deferred candidate
`solution: solutions/lem-affine-poincare-w2-liminf.tex` with real review provenance. The lemma
may then be marked proved; the corollary must remain conditional until
`ass:cmh-recovery-envelope` is discharged.
