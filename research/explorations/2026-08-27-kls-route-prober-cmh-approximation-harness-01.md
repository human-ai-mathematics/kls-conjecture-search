---
type: exploration
date: "2026-08-27"
outcome: dead-end
nodes:
  - q:cmh-approximation
---
# KLS route probe: CMH approximation closure

Date: 2026-08-27

Role: `kls-route-prober`

Concurrency key: `kls-gate:q:cmh-approximation`

Target: `q:cmh-approximation`

This probe treats the uniform premise
$\sup_k C_{\mathrm{CMH}}(\mu_k)\le C$ as a hypothesis. It does not try to prove universal
$\mathrm{CMH}(4)$, pass the canonical moment-map kernel through a noninvertible map, or identify
$C_{\mathrm{CMH}}$ with the KLS constant.

## Gate, verbatim

> Specify the approximation topology and common core, prove lower semicontinuity with constant
> preservation, and handle degeneration to a proper affine support.

The ledger statement is more explicit: pass
$C_P^{\mathrm{aff}}\le C$ from regular moment-map approximants satisfying
$C_{\mathrm{CMH}}\le C$ to an arbitrary centered log-concave limit, including affine-support
degeneration.

## Dependency and certification audit

The complete dependency closure of `q:cmh-approximation` is:

- `def:cmh`, which defines $C_{\mathrm{CMH}}$ using the closed Stein generator and the
  Moore--Penrose covariance inverse on the affine tangent space;
- `thm:cmh-implies-affine-poincare`, which depends only on `def:cmh` and proves, on the regular
  moment-map class,
  $C_P^{\mathrm{aff}}(\mu_k)\le C_{\mathrm{CMH}}(\mu_k)$.

The theorem is certified by `solutions/thm-cmh-normalization.tex` and the distinct-agent review
`research/reviews/2026-08-25-kls-cmh-normalization-repair-audit.md`. The review explicitly
excludes `q:cmh-approximation`. There are no further dependencies and the target has no
`bounded_by` edge.

## What “lower semicontinuity” can mean here

There are two possible readings, only one of which is supported by the node and its dependency.

1. The mathematically relevant reading is closure of the affine covariance Dirichlet-form
   inequality, equivalently
   $$
   C_P^{\mathrm{aff}}(\mu)
   \le \liminf_{k\to\infty} C_P^{\mathrm{aff}}(\mu_k)
   \le \liminf_{k\to\infty} C_{\mathrm{CMH}}(\mu_k)
   $$
   in the topology specified below.
2. It cannot mean lower semicontinuity or continuity of $C_{\mathrm{CMH}}$. No convergence of the
   canonical kernels $H_k$, Stein generators, or their operator domains is assumed, and both the
   manuscript and the certified dossier expressly disclaim such a conclusion.

There is a genuine residual control-plane ambiguity about the notation $H^1(\mu)$ at a nonsmooth,
affine-degenerate limit. In the regular full-dimensional theorem it is the closure of a smooth
core. At the limiting node, the manuscript instead says “subject to smooth-core density” without
declaring whether the intended target is the same closed relaxation or a separately defined
maximal distributional weighted Sobolev space. The proof below closes the gate for the intrinsic
closed-form convention and proves smooth-core density for that convention. If the target is the
maximal distributional space, an additional theorem identifying it with the closed relaxation
must be stated; the repository currently contains no such theorem.

## Term-by-term decomposition

### 1. Approximation class and topology

The topology should be ambient quadratic Wasserstein convergence:
$$
W_2(\mu_k,\mu)\longrightarrow0.
$$
Equivalently, $\mu_k\Rightarrow\mu$ weakly and the second moments converge. This topology is
load-bearing: weak convergence alone does not control the varying covariance in the affine
Dirichlet energy.

The approximants required by the regular endpoint are centered, full-dimensional log-concave
probability laws whose canonical moment potentials satisfy the regular-class hypotheses used in
`thm:cmh-implies-affine-poincare`. The repository does not contain a theorem constructing such a
sequence for an arbitrary $\mu$. Section `subsec:mm-audit` only says that a preprint appendix
addresses approximation; that sentence is not an imported theorem with hypotheses.

An explicit analytic candidate sequence is constructed below. Proving that it belongs to the
certified regular moment-map class is the first external-source gap.

### 2. One common core and convergence of both sides

Use one ambient core for every $k$ and for the limit:
$$
\mathscr C=\mathbb R+C_c^\infty(\mathbb R^n).
$$
Every $F\in\mathscr C$ and its gradient are bounded and continuous. On each regular approximant,
`thm:cmh-implies-affine-poincare` gives
$$
\operatorname{Var}_{\mu_k}(F)
\le C_k\int\langle\Sigma_k\nabla F,\nabla F\rangle\,d\mu_k,
\qquad C_k=C_{\mathrm{CMH}}(\mu_k).
$$
Quadratic Wasserstein convergence gives $\Sigma_k\to\Sigma$; weak convergence then passes both
sides to the limit with no change in $C_k$.

### 3. Isotropic normalization

Each $\Sigma_k$ is positive definite and may be whitened by the invertible map
$A_k=\Sigma_k^{-1/2}$. The certified affine covariance of $C_{\mathrm{CMH}}$ and
$C_P^{\mathrm{aff}}$ therefore allows the regular theorem to be applied in isotropic coordinates
and pulled back to the original coordinates before taking $k\to\infty$.

Uniform invertibility of $A_k$ is neither needed nor true when the limit has proper affine
support. The eigenvalues that collapse must be tracked rather than divided by at the limiting
step.

### 4. Proper affine support and the limiting domain

For centered $\mu$, its affine hull is a linear subspace $S$. One has
$$
S=\operatorname{Ran}\Sigma,\qquad S^\perp=\ker\Sigma,
$$
and $\Sigma_S=\Sigma|_S$ is positive definite. The limiting Sobolev form must be defined
intrinsically on $S$, not by pretending that $\Sigma$ is invertible in $\mathbb R^n$.

The intrinsic smooth core is $\mathbb R+C_c^\infty(S)$. It is exactly the restriction of
$\mathscr C$ to $S$, and it is dense in the closed covariance-form domain defined below.
Ambient normal derivatives make no contribution because both $\Sigma$ and its Moore--Penrose
inverse $\Sigma^+$ vanish on $S^\perp$.

### 5. Moment-map input beyond ordinary smoothing

Ordinary Gaussian convolution supplies smooth, positive, full-dimensional log-concave targets
and $W_2$ convergence. It does not, by itself or by any theorem recorded in this repository,
supply all of the following certified endpoint inputs:

- a smooth strictly convex moment potential $\varphi_k$;
- a global diffeomorphism $\nabla\varphi_k$ onto the target coordinates;
- a positive canonical Hessian field $H_k$ with
  $\operatorname{Div}_{\mu_k}H_k=-x$ and $\mathbb E H_k=\Sigma_k$;
- the no-flux/noncompact integration-by-parts and closability facts needed for the closed Stein
  form and its kernel convention.

No convergence of $H_k$ is required for this gate. Only the Poincaré inequalities produced on
the regular approximants are passed to the limit.

## The closure theorem

### Statement

Let $\mu_k$ be centered, full-dimensional regular moment-map log-concave laws on $\mathbb R^n$,
let $\mu$ be any centered log-concave law, and suppose
$W_2(\mu_k,\mu)\to0$. Write $\Sigma_k=\operatorname{Cov}(\mu_k)$ and
$\Sigma=\operatorname{Cov}(\mu)$. With the intrinsic closed-form convention for
$H^1_\Sigma(\mu)$ specified below,
$$
C_P^{\mathrm{aff}}(\mu)
\le \liminf_{k\to\infty}C_P^{\mathrm{aff}}(\mu_k)
\le \liminf_{k\to\infty}C_{\mathrm{CMH}}(\mu_k).
\tag{1}
$$
Consequently, the hypothesis $\sup_k C_{\mathrm{CMH}}(\mu_k)\le C$ passes the affine Poincaré
inequality to $\mu$ with the same constant $C$.

### Moment and covariance convergence

Quadratic Wasserstein convergence implies convergence of first moments and uniform integrability
of $|x|^2$. Applying this to the entries $x_ix_j$ (or using polarization) gives
$$
\int x\,d\mu_k\to\int x\,d\mu=0,
\qquad
\int xx^\top\,d\mu_k\to\int xx^\top\,d\mu.
$$
Hence $\Sigma_k\to\Sigma$ in every matrix norm.

### Common-core passage

Fix $F\in\mathscr C$. Since $F$ and $F^2$ are bounded and continuous,
$$
\operatorname{Var}_{\mu_k}(F)\longrightarrow\operatorname{Var}_{\mu}(F).
$$
For the energy, put $h(x)=\langle\Sigma\nabla F(x),\nabla F(x)\rangle$. Then $h$ is bounded and
continuous, and
\begin{align*}
&\left|\int\langle\Sigma_k\nabla F,\nabla F\rangle\,d\mu_k
-\int\langle\Sigma\nabla F,\nabla F\rangle\,d\mu\right|\\
&\quad\le
\|\Sigma_k-\Sigma\|_{\mathrm{op}}\|\nabla F\|_\infty^2
+\left|\int h\,d\mu_k-\int h\,d\mu\right|\longrightarrow0.
\tag{2}
\end{align*}
Let $L=\liminf_k C_{\mathrm{CMH}}(\mu_k)$ and take a subsequence on which the constants converge
to $L$. If $L<\infty$, the regular endpoint inequality and (2) yield
$$
\operatorname{Var}_{\mu}(F)
\le L\int\langle\Sigma\nabla F,\nabla F\rangle\,d\mu.
\tag{3}
$$
The case $L=\infty$ is vacuous. Thus the constant is unchanged on the common core. This is the
precise lower-semicontinuity statement; no $H_k$ or Stein-generator limit has entered.

### Intrinsic $H^1_\Sigma(\mu)$ and smooth-core density

Assume first that $d=\dim S>0$. A log-concave law with affine hull $S$ has a density with respect
to $d$-dimensional Lebesgue measure on $S$. For a globally Lipschitz $f:S\to\mathbb R$, define
$$
\|f\|_{H^1_\Sigma(\mu)}^2
=\int_S f^2\,d\mu
+\int_S\langle\Sigma_S\nabla_S f,\nabla_S f\rangle\,d\mu.
\tag{4}
$$
Define $H^1_\Sigma(\mu)$ as the completion of the globally Lipschitz functions for (4). This is
the closed relaxation of the covariance Dirichlet form.

The core $\mathbb R+C_c^\infty(S)$ is dense in this domain. It suffices to approximate a globally
Lipschitz $f$:

1. Value truncation $T_Mf=(-M)\vee f\wedge M$ converges in (4), by the Lipschitz chain rule and
   dominated convergence.
2. For bounded $f$, multiply by a smooth cutoff $\chi_R$ equal to one on $B_R\cap S$, supported
   in $B_{2R}\cap S$, and satisfying $|\nabla_S\chi_R|\le c/R$. The $L^2$ error and the term
   $(1-\chi_R)\nabla_Sf$ vanish by dominated convergence, while
   $$
   \int f^2\langle\Sigma_S\nabla\chi_R,\nabla\chi_R\rangle\,d\mu
   \le \|f\|_\infty^2\|\Sigma_S\|_{\mathrm{op}}c^2/R^2\to0.
   $$
3. A compactly supported Lipschitz function on $S$ may be convolved inside the Euclidean space
   $S$. Standard mollification converges in $L^2(\mu)$; its gradients converge Lebesgue-a.e. and
   are uniformly bounded by the original Lipschitz constant. Relative absolute continuity of
   $\mu$ and dominated convergence give convergence of the energy in (4).

This proves the required density rather than merely assuming it. If $d=0$, then $\mu=\delta_0$,
$\Sigma=0$, the domain is one-dimensional, and every variance is zero.

Every $\phi\in C_c^\infty(S)$ has an ambient extension: in the orthogonal splitting
$x=s+t\in S\oplus S^\perp$, take $F(s+t)=\phi(s)\eta(t)$ with
$\eta\in C_c^\infty(S^\perp)$ equal to one near zero. Conversely, an ambient smooth function
restricts smoothly to $S$. Hence the intrinsic core is exactly the restriction of the common
ambient core.

If two ambient extensions agree on $S$, the difference of their gradients on $S$ lies in
$S^\perp$. Since
$$
\Sigma P_{S^\perp}=0,
\qquad
\Sigma^+P_{S^\perp}=0,
$$
both the affine covariance form and the Moore--Penrose covariance metric ignore ambient normal
derivatives. Extending (3) by the just-proved density establishes (1).

### Eigenvalue tracking and why one must unwhiten before the limit

Let the positive eigenvalues of $\Sigma$ be
$\lambda_1\ge\cdots\ge\lambda_d>0$, followed by $n-d$ zeros. Matrix convergence and Weyl's
inequality give
$$
\lambda_i(\Sigma_k)\to\lambda_i(\Sigma)>0\quad(i\le d),
\qquad
\lambda_i(\Sigma_k)\to0\quad(i>d).
$$
Thus the whitening maps are uniformly controlled on the limiting tangent space but diverge in
the collapsing normal directions. When $d=n$, $\Sigma_k^{-1/2}\to\Sigma^{-1/2}$ and whitening
commutes with the $W_2$ limit. When $d<n$, it cannot do so: every whitened law has covariance
$I_n$, whereas a $W_2$ limit supported on $S$ has singular covariance.

The valid order of operations is therefore:

1. whiten each full-dimensional $\mu_k$ by its invertible covariance if the regular theorem or
   the uniform CMH premise is stated isotropically;
2. use invertible affine covariance to pull the resulting Poincaré inequality back to $\mu_k$;
3. take the $W_2$ limit in the original coordinates by (2).

No noninvertible transport of a canonical moment-map Hessian is asserted. Only the
Poincaré-level inequality survives the limit.

## A precise analytic approximating family

The ordinary measure-theoretic part of the approximation can be constructed without an external
theorem. Let $X\sim\mu$, let $G\sim N(0,I_n)$ be independent, and let
$\bar\mu_\varepsilon$ be the law of $Y_\varepsilon=X+\sqrt\varepsilon G$. Its density
$q_\varepsilon$ is positive, smooth, full-dimensional, and log-concave, and
$$
W_2(\bar\mu_\varepsilon,\mu)^2\le n\varepsilon,
\qquad
\operatorname{Cov}(\bar\mu_\varepsilon)=\Sigma+\varepsilon I_n.
$$

If the regularity theorem requires a uniformly strictly convex target potential, define
$$
d\nu_\varepsilon(x)
=Z_\varepsilon^{-1}q_\varepsilon(x)e^{-\varepsilon|x|^2/2}\,dx,
\qquad
m_\varepsilon=\int x\,d\nu_\varepsilon(x),
\qquad
\mu_\varepsilon=(x\mapsto x-m_\varepsilon)_\#\nu_\varepsilon.
\tag{5}
$$
The potential of $\nu_\varepsilon$ is smooth and satisfies
$$
\varepsilon I_n
\preceq D^2\bigl(-\log q_\varepsilon+\varepsilon|x|^2/2\bigr)
\preceq(\varepsilon^{-1}+\varepsilon)I_n.
$$
The upper bound follows from the Gaussian-convolution Hessian formula; the lower bound uses
log-concavity of $q_\varepsilon$. Translation preserves these properties.

The family (5) still converges to $\mu$ in $W_2$. Indeed log-concavity gives finite fourth
moments, $\sup_{0<\varepsilon\le1}\mathbb E|Y_\varepsilon|^4<\infty$, and
$$
0\le1-e^{-\varepsilon|Y_\varepsilon|^2/2}
\le\frac\varepsilon2|Y_\varepsilon|^2.
$$
Therefore the Gaussian tilt changes neither weak nor second-moment limits; in particular
$Z_\varepsilon\to1$ and $m_\varepsilon\to0$. The standard weak-plus-second-moment criterion then
gives $W_2(\mu_\varepsilon,\mu)\to0$.

What is not proved in the repository is the exact implication
$$
\text{smooth target with the Hessian bounds above}
\quad\Longrightarrow\quad
\text{all regular moment-map hypotheses of the certified endpoint}.
\tag{6}
$$
The vague statement that the Letwin or Chen--Klartag appendix “handles approximation” does not
identify (6), its theorem number, its boundary assumptions, or the integration-by-parts scope.
This is the first unjustified step, and the attack stops there.

## Exact residue

- **Technical gap — exact regular moment-map approximation theorem.** Verify a primary theorem
  which implies (6) for the explicit family (5), including smooth strict convexity of the moment
  potential, the global target-coordinate map, the canonical Stein identity, and the closed-form
  conventions used by `thm:cmh-implies-affine-poincare`. If an available theorem needs stronger
  target hypotheses, the approximating family must be adjusted and its $W_2$ convergence
  rechecked. The repository's current preprint-summary sentence does not discharge this.
- **Technical gap / control-plane choice — maximal versus relaxed Sobolev domain.** For the
  intrinsic closed relaxation defined in (4), density and constant-preserving closure are proved
  above. If `q:cmh-approximation` intends a separately defined maximal distributional
  $W^{1,2}(\mu)$, the orchestrator must name that domain and import or prove its equality with the
  relaxed domain. This is not a failure of (3); it is missing target semantics.
- **Fenced:** none.
- **Needs new idea:** none identified. No new estimate is needed after the regularity import; the
  remaining passage is the closed-form argument above.

The hypothesis $\sup_k C_{\mathrm{CMH}}(\mu_k)\le C$ is not residue: it is the premise assigned
to this gate. Nothing here proves that premise or asserts lower semicontinuity of
$C_{\mathrm{CMH}}$.

## Fence-by-fence evasion check

The ledger gives `q:cmh-approximation` no `bounded_by` edge. The full obstruction file was
nevertheless checked:

- `obs:two-tail`: no slice-wise excess, Stein source, or covariance weight is estimated.
- `obs:proj-ceiling`: no radial/projection test or quadratic-chaos estimate is used.
- `obs:crude-insufficient`: no stochastic covariance occupation integral or crude bootstrap is
  used.
- `obs:relative-ceiling`: no universal relative $\Xi_T$ bound is inserted.
- `obs:circularity`: no localized isoperimetric profile or evolving competitor family appears.
- `obs:rank-one-refuted`: no product-cut incident estimate or counterexample is proposed.

The noninvertible-image guardrail is respected: the proof never transports the canonical
moment-map kernel through the limiting projection. The trace-upgrade cluster is not touched.

## Route viability and proposed gate text

The route remains viable. The constant-preserving $W_2$ closure, covariance degeneration,
intrinsic core, and whitening/unwhitening order admit a complete analytic argument. The only
mathematical input not present in the repository is an exact theorem placing a concrete smooth,
strongly log-concave approximating family in the certified regular moment-map class.

Proposed one-line gate update for the orchestrator:

> Use centered $W_2$-convergent regular moment-map approximants and the intrinsic closed
> covariance-form domain to prove
> $C_P^{\mathrm{aff}}(\mu)\le\liminf_k C_{\mathrm{CMH}}(\mu_k)$, and cite an exact theorem that
> places the Gaussian-convolution/Gaussian-tilt family in the regular class, including proper
> affine-support collapse.

## Proposed ledger delta

None. The closure lemma is a candidate for a future dossier, but the existing gate should not be
promoted until the regular-moment-map approximation input is source-verified and the Sobolev-domain
convention is fixed.

```yaml
outcome: blocked
artifacts:
  - research/explorations/2026-08-27-kls-route-prober-cmh-approximation-harness-01.md
proposed_deltas:
  - none
next_role: literature-scout
next_prompt: |
  Source-verify the one missing external input for `q:cmh-approximation`. Read
  `research/explorations/2026-08-27-kls-route-prober-cmh-approximation-harness-01.md`,
  `modules/kls/04-family-moment-map.tex`, `modules/kls/40-moment-map-cmh.tex`,
  `modules/kls/41-cmh-normalization.tex`, and `solutions/thm-cmh-normalization.tex`.
  Find a primary-source theorem, with exact theorem/lemma number, version, hypotheses, and
  conclusion, showing that centered targets with smooth potentials satisfying
  `a I <= D^2 V <= b I` (or a precisely stated stronger class met by an adjusted approximating
  family) have canonical moment potentials that are smooth and strictly convex, whose gradient
  is a global diffeomorphism and whose target-coordinate Hessian gives the Stein identity,
  integration-by-parts/no-flux, and closed-form data required by
  `thm:cmh-implies-affine-poincare`. Check Cordero-Erausquin--Klartag, Klartag, Fathi, and the
  exact approximation appendices of Letwin 2026 and Chen--Klartag 2026; do not report that an
  appendix “handles approximation” without quoting the exact result and matching every
  hypothesis. Verify separately whether the explicit centered Gaussian-convolution plus
  Gaussian-tilt family in the exploration meets that theorem and converges in W2 through
  affine-support degeneration. If no source gives the full implication, identify the first
  missing regularity or boundary statement exactly. Propose publication-class metadata and a
  BibTeX entry or correction, but do not edit `fi_references.bib`, either ledger, the manuscript,
  or route-control files.
```
