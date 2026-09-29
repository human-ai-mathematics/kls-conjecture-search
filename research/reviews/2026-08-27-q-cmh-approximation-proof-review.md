---
verdict: pass
authors:
  - /root/prove_cmh_approximation
reviewer: /root/review_cmh_approximation
fingerprints:
  solutions/q-cmh-approximation.md: bee592ea926fef6706f8474dca5cf22aeee226bd290732469b9d5faa81abe8de
  q:cmh-approximation: 26f10be5269f1b56dacc81d75c0fe3d9a8d856c97931c58c01c4e4554b9fbbe0
  def:cmh: 5093f7f871d8362c179b6ca901822ba370d6a14237ed9bb3fe076ab964ff9722
  thm:cmh-implies-affine-poincare: 96fd21faf9d64d72f98fb884b57bd648952eba813b3c71eba4c32088571bb433
  thm:regular-moment-map-compact-target: 6c5fc0b83ba7ee921113bb0cac813d6c92fd41e9b1a9dda5247df865f76eb813
  ass:uniform-cmh-approximants: d189a08645627f605d95d8f161bed294d6e48fccf1ed050b43e39ee5f1e6af45
---

# CMH approximation closure — independent proof review

This is a cold review of `solutions/q-cmh-approximation.tex`, whose reviewed SHA-256 is
`36410d7973150c6f7f430f6020e397908bc64b931a1a66c6580ffa21ad809262`.  The proof was
reconstructed from the dossier, manuscript, ledger, certified dependency dossier, and actual
published sources.  The prover's narrative was not used as evidence.  The author and reviewer
identities are distinct.

## Findings

### Statement agreement and status

The three statements agree mathematically.

- `modules/kls/40-moment-map-cmh.tex`, at `\label{q:cmh-approximation}`, asks for hypotheses and
  a constant-preserving passage from regular approximants satisfying
  $C_{\mathrm{CMH}}(\mu_k)\le C$ to the affine Poincar\'e inequality for an arbitrary centered
  log-concave limit, including isotropic normalization and affine-support degeneration.
- `research/kls/ledger.yaml` asks for the same regular approximation and closure argument,
  including affine-support degeneration.
- The dossier constructs one such sequence, proves the stronger inequality
  $$
  C_{\mathrm P}^{\mathrm{aff}}(\mu)
  \le \liminf_k C_{\mathrm P}^{\mathrm{aff}}(\mu_k)
  \le \liminf_k C_{\mathrm{CMH}}(\mu_k),
  $$
  and obtains the requested conclusion under the explicit premise
  $\sup_k C_{\mathrm{CMH}}(\mu_k)\le C$.

The case $\dim\operatorname{Ran}\Sigma=0$ is included: centeredness then gives
$\mu=\delta_0$, the intrinsic space contains only constants, and the affine Poincar\'e constant
is $0$.  The unresolved uniform-CMH premise is not discharged.  Under repository constraint 7,
the node may therefore become `conditional` but not `proved`.

### Hypothesis accounting

The proof uses exactly the following hypotheses.

1. $\mu$ is a centered log-concave probability on $\mathbb R^n$.  Log-concavity supplies finite
   second moments, preservation under Gaussian convolution and convex truncation, and the
   intrinsic log-concave density on the affine hull.  Centering makes the affine hull the linear
   space $S=\operatorname{Ran}\Sigma$, centers the Gaussian convolution, and supplies the
   barycenter condition for the moment-map theorem.
2. The smoothing variance, Gaussian tilt, and truncation radius satisfy
   $\delta_k>0$, $\varepsilon_k>0$, and $R_k<\infty$.  These are constructed parameters, not
   additional assumptions on $\mu$.
3. For the compact-target import, the target is a convex body containing the origin in its
   interior, its density is the restriction of a positive smooth ambient function, and its
   barycenter is zero.  All are verified for each $\mu_k$.
4. For the certified CMH endpoint, each $\mu_k$ is centered, full-dimensional and log-concave;
   its canonical kernel is smooth, symmetric and positive on the target interior; its global
   Stein identity has weak zero flux; and the exact ambient-restriction form is closable with
   constant kernel.  The dossier verifies each item before invoking the endpoint.
5. The only unresolved route hypothesis is
   $\sup_k C_{\mathrm{CMH}}(\mu_k)\le C$.

No used hypothesis is unstated.  The displayed strict lower Hessian bound from the Gaussian tilt
and the optional upper Hessian observation are stronger than the published compact-target input
requires; this is harmless slack, not a hidden premise.

### Construction and ambient $W_2$ convergence

For $X\sim\mu$ and an independent standard Gaussian $G$, the coupling
$X\leftrightarrow X+\sqrt\delta G$ gives
$W_2^2(\mu,\lambda_\delta)\le n\delta$, while preserving the mean and changing the covariance to
$\Sigma+\delta I$.

For fixed $\delta$, the tilted and ball-truncated density relative to $\lambda_\delta$ tends
pointwise to $1$.  Its normalizer tends to $1$, and dominated convergence applies both to bounded
tests and to $|x|^2$.  Equivalently, one may couple the common part of the two densities
identically and couple their residual parts; the weighted $L^1$ convergence with weight
$1+|x|^2$ makes the residual quadratic cost vanish.  Thus the asserted fixed-$\delta$ $W_2$
convergence is valid without relying merely on numerical or weak agreement.

The two-parameter limit permits simultaneous choices
$\delta_k=k^{-4}$, $0<\varepsilon_k<k^{-1}$, $R_k>k$, and truncation error below $k^{-1}$.
Comparison of means under a coupling gives $|m_k|<k^{-1}$.  Translation and the triangle
inequality then give the exact ambient estimate
$$
W_2(\mu_k,\mu)<\frac{2}{k}+\frac{\sqrt n}{k^2}.
$$
This argument remains in the original coordinates and is valid when the limiting covariance is
singular.  The word “explicit” describes the displayed family and quantitative diagonal bound;
$\varepsilon_k,R_k$ are selected from the proved limit rather than given by a closed formula.

### Published compact-target input, Stein identity, and mean kernel

The two non-elementary external inputs were checked against their actual sources and are both
published.

- Berman--Berndtsson, Theorem 1.1, *Annales de la Facult\'e des Sciences de Toulouse* 22
  (2013), DOI `10.5802/afst.1386`, gives a smooth convex solution and a global gradient
  diffeomorphism $\mathbb R^n\to\operatorname{int}P$ for a positive smooth target density on a
  convex body precisely under the zero-barycenter condition.  A convex smooth potential whose
  gradient is a diffeomorphism has positive-definite Hessian and is strictly convex.
- Fathi, Theorem 2.3, *Annals of Probability* 47 (2019), DOI `10.1214/18-AOP1305`, identifies
  $D^2\varphi((\nabla\varphi)^{-1})$ as a positive symmetric Stein kernel when the moment
  potential is $C^2$ on all of $\mathbb R^n$.  The source explicitly covers compact convex
  targets with density bounded above and below; the dossier's ambient-positive smooth density
  has those bounds on the compact target.

After centering, the target is the closed ball with center $-m_k$ and radius $R_k$ (writing the
closure is immaterial to the indicator and measure).  Its density extends positively and
smoothly to all of $\mathbb R^n$, it is full-dimensional and centered, and $0$ lies in its
interior.  Thus every imported hypothesis is met.

Fathi's global test identity has no boundary distribution.  In target coordinates it is exactly
$\operatorname{Div}_{\mu_k}H_k=-x$ on ambient $\mathbb R^n$, hence the required weak zero-normal-
flux convention.  A compactly supported cutoff equal to $x_j$ on a neighborhood of the bounded
target gives
$$
\mathbb E_{\mu_k}(H_k)_{ij}=\mathbb E_{\mu_k}X_iX_j=(\Sigma_k)_{ij}.
$$
There is no omitted cutoff or boundary term.

The routine supporting facts have no unresolved citation debt: preservation under marginalization
is the published Pr\'ekopa--Brascamp--Lieb theorem (`BrascampLieb1976` in the repository), the
$W_2$/moment fact is standard published optimal-transport theory (`Villani2008`), and the
relative-density statement is the classical published Borell characterization of log-concave
measures.  The uses of the Friedrichs representation theorem and Weyl's inequality are standard
functional-analysis and finite-dimensional spectral facts and were also checked directly in the
places used.  No preprint-unreviewed result enters this proof.

### Exact closed Stein form and the certified endpoint

The core
$$
\mathscr D_k=\{F|_{P_k}:F\in\mathbb R+C_c^\infty(\mathbb R^n)\}
$$
is dense in $L^2(\mu_k)$.  Its energy is well defined independently of the ambient extension,
because equal smooth restrictions have equal gradients on the target interior.  Positivity of
$H_k$ and $\mathbb E H_k=\Sigma_k$ give finite energy for every core function.

For closability, if $f_j\to0$ in $L^2(\mu_k)$ and
$H_k^{1/2}\nabla f_j\to u$, then on each compact subset of the target interior the density is
equivalent to Lebesgue measure and $H_k^{\pm1/2}$ are bounded.  Hence
$f_j\to0$ and $\nabla f_j\to H_k^{-1/2}u$ locally in ordinary $L^2$.  Closedness of
distributional differentiation forces $u=0$.  Exhaustion of the interior is legitimate because
the convex boundary is null.  The same argument applied to a zero-energy element of the closed
form gives zero distributional gradient on the connected target interior, so the closed-form
kernel is exactly the constants.

The nonnegative self-adjoint operator represented by this closed form is therefore the exact
closed Stein generator used in `def:cmh`, not an asserted maximal Neumann or distributional
realization.  The dependency `thm:cmh-implies-affine-poincare` is `proved`, is agent-certified by
`solutions/thm-cmh-normalization.tex` and
`research/reviews/2026-08-25-kls-cmh-normalization-repair-audit.md`, and depends only on the
defined node `def:cmh`.  Its hypotheses now match, so its application gives
$C_{\mathrm P}^{\mathrm{aff}}(\mu_k)\le C_{\mathrm{CMH}}(\mu_k)$.  There is no circular use of
the present approximation node.

### Intrinsic singular-support form and common-core limit

For $d>0$, the covariance restriction $\Sigma_S$ is positive definite.  On the relative
interior of its convex support, $\mu$ has a positive log-concave density locally bounded above
and below.  The same local distributional-gradient argument proves closability of the constant-
coefficient covariance pre-form and identifies its kernel with the constants.

The three approximation steps in the dossier are valid in the form norm: truncate values,
multiply a bounded function by growing compact cutoffs, and mollify intrinsically on $S$.
Consequently
$\mathbb R+C_c^\infty(S)$ is dense in the declared closed relaxation.  The cutoff cross term is
controlled by Cauchy--Schwarz (or the quadratic inequality) together with the two displayed
vanishing terms.

This intrinsic core is exactly the restriction of
$\mathbb R+C_c^\infty(\mathbb R^n)$.  Conversely, a compactly supported intrinsic test extends
as $F(s+t)=\phi(s)\eta(t)$ with $\eta=1$ near $0$ in $S^\perp$.  If two ambient extensions agree
on $S$, their gradient difference is normal, and
$$
\Sigma=P_S\Sigma_SP_S,
\qquad
\Sigma^+=P_S\Sigma_S^{-1}P_S
$$
annihilate that difference.  Thus the covariance energy and the Moore--Penrose affine-tangent
convention are independent of extension, including at rank zero.

Ambient $W_2$ convergence gives $\Sigma_k\to\Sigma$.  For every fixed function in the common
ambient core, variance converges by weak convergence and covariance energy converges by the
matrix convergence plus weak convergence of a bounded continuous integrand.  A single
subsequence realizing the finite liminf of the approximant constants is then fixed; the
approximant inequality passes along it for every common-core test.  Intrinsic core density extends
the limit inequality to the entire declared closed domain.  This proves
$$
C_{\mathrm P}^{\mathrm{aff}}(\mu)
\le\liminf_k C_{\mathrm P}^{\mathrm{aff}}(\mu_k)
$$
with no loss of constant.

Finally, covariance convergence and Weyl's inequality give convergence of the $d$ positive
eigenvalues and collapse of the remaining $n-d$ eigenvalues.  Each full-rank approximant may be
whitened separately.  Invertible affine covariance of CMH and of the covariance-form Poincar\'e
constant permits its inequality to be unwhitened before taking the original-coordinate $W_2$
limit.  No canonical kernel is transported through a noninvertible map.

### Fences

The ledger gives `q:cmh-approximation` no `bounded_by` edge.  No fixed-cut obstruction, localization
occupation estimate, projection ceiling, relative trace upgrade, or trace-upgrade-cluster
implication is invoked.  The spatial cutoff used only to prove density of a Dirichlet-form core
is not a fixed-cut route argument.

### Mechanical validation

From `solutions/`,

```text
latexmk -g -pdf -outdir=../build q-cmh-approximation.tex
```

completed successfully and produced a 6-page PDF.  There is no TeX error.  The unresolved
cross-manuscript references are the expected standalone behavior allowed by `solutions/README.md`.
Before this report was added, `python3 research/check_ledger.py` reported 0 errors.

## Corrections

None.  The closed-ball convention and the existential choice of two diagonal parameters are
minor wording precisions and do not change any statement or proof step.

## Exclusions

This review does not discharge or support the premise
$\sup_kC_{\mathrm{CMH}}(\mu_k)\le C$.  It does not certify lower semicontinuity or continuity of
$C_{\mathrm{CMH}}$, equality of the declared closed relaxation with an unnamed maximal Sobolev
or Neumann domain, regularity of an untruncated full-support moment map, transport of a canonical
kernel through a noninvertible map, universal $\mathrm{CMH}(4)$, or KLS.  It uses and certifies no
numerical artifact.  Updating the dossier header, ledger, and nearby manuscript status prose is
control-plane work outside this reviewer's write surface.
