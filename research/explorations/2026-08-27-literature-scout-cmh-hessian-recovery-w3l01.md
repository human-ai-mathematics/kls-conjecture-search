---
---
# CMH Hessian recovery: literature audit for the linear quotient

Date: 2026-08-27
Role: literature-scout
Scope: stability and compactness of canonical moment-map Hessians, uniform linear-quotient bounds, compact-target approximation, and obstructions

## Exact target and normalization

Let $\nu$ be a centered full-dimensional log-concave probability measure with covariance
$\Sigma_\nu\succ0$.  Write its source-centered moment potential as $\phi$:

$$
(\nabla\phi)_\#(e^{-\phi(y)}\,dy)=\nu,
\qquad
H_\nu(x)=D^2\phi((\nabla\phi)^{-1}x).
$$

The linear quotient used by the CMH route is

$$
Q_{\rm lin}(\nu)=
\lambda_{\max}\!\left(
\Sigma_\nu^{-1/2}
\mathbb E_\nu[H_\nu\Sigma_\nu^{-1}H_\nu]
\Sigma_\nu^{-1/2}
\right).
$$

Equivalently,

$$
\mathbb E_\nu[H_\nu\Sigma_\nu^{-1}H_\nu]
=\int D^2\phi(y)\Sigma_\nu^{-1}D^2\phi(y)e^{-\phi(y)}\,dy.
$$

The searched-for recovery statement was: for every centered full-dimensional log-concave
$\mu$ and every $\varepsilon>0$, find a regular compact-target $\nu$ with
$W_2(\nu,\mu)<\varepsilon$ and $Q_{\rm lin}(\nu)\le C_{\rm lin}+\varepsilon$, where
$C_{\rm lin}$ is universal.  Stronger neighbours were continuity or lower semicontinuity of
$Q_{\rm lin}$ under $W_2$ convergence.  Weaker neighbours were convergence of the canonical
source measures, potentials, or gradients, and dimension- or support-dependent bounds.

No source located proves convergence of canonical moment-map Hessians, convergence of
$\nabla\phi_k$ in the Hessian-weighted norm appearing above, lower semicontinuity of
$Q_{\rm lin}$, or the stated universal recovery result.

## Found: published results

### Klartag: compact-target moment potentials and directional Hessian moments

**Source.** Bo'az Klartag, *Logarithmically-Concave Moment Measures I*, in *Geometric
Aspects of Functional Analysis*, Lecture Notes in Mathematics 2116 (2014), arXiv:1309.2767v1.
`import_class: published`.  Source read: Proposition 2.1 and its proof; Theorem 1.1 and its
proof; Proposition 6.1 and its proof.

Proposition 2.1 says, after fixing the source-translation normalization, that if the moment
measures $\mu_k,\mu$ are all supported in one compact set $\Omega$, then

$$
\mu_k\Rightarrow\mu
\quad\Longleftrightarrow\quad
\phi_k(y)\to\phi(y)\quad\text{for every }y.
$$

The proof supplies common local compactness for the convex potentials.  Consequently the
convergence is locally uniform, and standard convex convergence gives
$\nabla\phi_k(y)\to\nabla\phi(y)$ at every point where the relevant convex functions are
differentiable.  The proof does **not** give convergence of $D^2\phi_k$, uniform integrability
of quadratic Hessian expressions, or convergence of gradients in a Hessian metric.

The proof of Theorem 1.1 also provides a genuine regular compact-target approximation: smooth
the target on approximating smooth convex bodies, add a small Gaussian tilt, truncate, and
recenter.  The resulting moment potentials converge pointwise and their gradients converge
almost everywhere.  The argument passes a Laplacian bound distributionally; it does not pass
$D^2\phi_k\Sigma_k^{-1}D^2\phi_k$ or $Q_{\rm lin}$.

For a target supported in a compact convex $K$, Theorem 1.1 gives

$$
0\preceq H_\mu(x)\preceq 2R(K)^2 I.
$$

In isotropic normalization, $\mathbb E H_\mu=I$, hence

$$
H_\mu^2\preceq2R(K)^2H_\mu,
\qquad Q_{\rm lin}(\mu)\le2R(K)^2.
$$

More invariantly, whitening first gives
$Q_{\rm lin}(\mu)\le2R(\Sigma^{-1/2}K)^2$.  This is not a recovery bound: the whitening
radius is not universal and truncation radii diverge.

Proposition 6.1 yields, in the notation above, for every $p\ge1$ and $\theta\in\mathbb R^n$,

$$
\left(\mathbb E_\mu|\theta^T H_\mu\theta|^p\right)^{1/p}
\le 4p^2\,\theta^T\Sigma\theta.
$$

For $p=2$ this bounds the second moment of a scalar Rayleigh quotient.  It does not bound
$\mathbb E|H_\mu\theta|^2=\theta^T\mathbb E[H_\mu^2]\theta$; the latter contains all columns
and is exactly where rotating eigendirections/static commutator effects remain.

Primary source: <https://arxiv.org/html/1309.2767v1>

### Fathi: a special-class pointwise contraction

**Source.** Max Fathi, *Stein Kernels and Moment Maps*, Annals of Probability 47 (2019),
arXiv:1804.04699v3.  `import_class: published`.  Source read: Theorem 2.3 and Corollary 2.4,
including their proofs.

Fathi identifies the canonical target-coordinate moment Hessian with a Stein kernel.  If a
regular target has density $e^{-V}$ and $D^2V\succeq\varepsilon I$, Corollary 2.4 gives

$$
0\preceq H_\mu\preceq\varepsilon^{-1}I.
$$

In the repository's affine normalization, assume
$D^2V(x)\succeq\varepsilon\Sigma^{-1}$.  Whitening and congruence give
$0\preceq\bar H\preceq\varepsilon^{-1}I$, while
$\mathbb E\bar H=I$.  Thus

$$
Q_{\rm lin}(\mu)=\lambda_{\max}\mathbb E[\bar H^2]le\varepsilon^{-1}.
$$

This proves the desired form only on a relatively strongly log-concave subclass.  Adding an
absolute Gaussian tilt $\varepsilon_k I$ to approximate a general target gives relative
curvature parameter at best $\varepsilon_k\lambda_{\min}(\Sigma_k)$, so this estimate becomes
$Q_{\rm lin}\le(\varepsilon_k\lambda_{\min}\Sigma_k)^{-1}$ and degenerates as the tilt is
removed.

Primary source: <https://arxiv.org/html/1804.04699v3>

### Delalande--Farinelli: regularized moment measures are not canonical ones

**Source.** Alex Delalande and Sara Farinelli, *Regularized Moment Measures*, Potential
Analysis 64(2) (2026), arXiv:2506.13218v2.  `import_class: published`.  Source read: Theorem
3.1 and its proof.

For fixed $\alpha>0$, the minimizer/source measure is $W_2$-stable (locally $1/2$-Hölder) in
the target.  Its representation is

$$
(\nabla u)_\#e^{-(u+\alpha|y|^2/2)}dy=\mu.
$$

This is not the canonical moment representation: the source log-density is
$U=u+\alpha|y|^2/2$, whereas the pushforward map is $\nabla u$, not $\nabla U$.
Consequently this theorem supplies neither stability of the canonical $H_\mu$ nor a bound on
$Q_{\rm lin}$.  Its constants also degenerate as $\alpha\downarrow0$ (Remark 3.2).

Primary source: <https://arxiv.org/html/2506.13218>

## Found: unreviewed preprints

### Bonnet--Rubinstein: inverse stability at source-density level

**Source.** Guillaume Bonnet and Yanir A. Rubinstein, *Quantitative Stability and Numerical
Resolution of the Moment Measure Problem*, arXiv:2604.09914v1, 10 April 2026.
`import_class: preprint-unreviewed`.  Theorem 1.3 and its proof in Sections 3.1--3.5 were read.

For centered equal-mass full-dimensional moment measures $\mu\ne\nu$, choose

$$
R\ge m^{-1}\int|y|d\mu,
\qquad
0<r\le m^{-1}\inf_{w\in S^{d-1}}\int|w\cdot y|d\mu.
$$

After translating one source potential, Theorem 1.3 gives

$$
\|e^{-\phi_\mu}-e^{-\phi_\nu(\cdot-v)}\|_{L^1}
\lesssim_{d,R/r}m
\left[
\frac{W_1(\mu,\nu)}{mR}
\log\!\left(1+\frac{mR}{W_1(\mu,\nu)}\right)
\right]^{1/2}.
$$

Unlike ordinary fixed-source optimal-transport stability, this is genuinely stability of the
inverse moment-measure problem.  It remains a zeroth-order statement about source Gibbs
densities: the paper gives no convergence of gradients or Hessians and no $Q_{\rm lin}$
semicontinuity.

Primary source: <https://arxiv.org/html/2604.09914>

### Machado--Ramos: source stability and an affine-collapse obstruction

**Source.** João Miguel Machado and João P. G. Ramos, *Quantitative Stability for the
Brascamp--Lieb Inequality and Moment Measures*, arXiv:2511.22636v3, 29 July 2026.
`import_class: preprint-unreviewed`.  Theorems 1.3, 5.3, 5.6 and Proposition 5.7 and their
proofs were read.  The proof of Theorem 5.12 is omitted in the source, so that theorem is only
a lead here, not an import.

On targets in a fixed compact set, with a uniform lower bound on
$\Theta(\mu)=\inf_{\theta\in S^{d-1}}\int|\theta\cdot y|d\mu$, Theorem 5.6 gives a Hölder
$W_2$ stability estimate for the **source Gibbs minimizer sets**.  Theorem 5.3 gives $L^1$
convergence of regularized source Gibbs densities as regularization is removed.  Neither
statement gives canonical potential-gradient convergence, Hessian convergence, or control of
$Q_{\rm lin}$.

Proposition 5.7 shows that the source-$W_2$ constant cannot be uniform as
$\Theta\downarrow0$: mollifications of a lower-dimensional target would otherwise yield a
forbidden full-ambient moment representation in the limit.  This is an obstruction to uniform
source-measure stability through affine-support collapse, not an obstruction to a universal
$Q_{\rm lin}$ bound on full-dimensional targets.

Primary source: <https://arxiv.org/html/2511.22636>

## Why ordinary optimal-transport stability does not close the route

Stability theorems for a Brenier map with a fixed source do not apply directly.  In the
canonical moment problem both the source $e^{-\phi_k}dy$ and the map $\nabla\phi_k$ vary with
the target, and $Q_{\rm lin}$ is quadratic in $D^2\phi_k$.  The moment-measure-specific results
above improve source/potential compactness, but stop before this derivative level.  In
particular, this audit makes no inference from ordinary optimal-transport stability to
canonical-Hessian continuity.

## Proposed ledger deltas

These are candidate imported nodes for the orchestrator; no ledger or manuscript was edited.
The manuscript anchors would first need to be added to
`modules/kls/04-family-moment-map.tex`.

```yaml
- id: thm:klartag-moment-potential-continuity
  kind: theorem
  status: imported
  route: moment-map-cmh
  file: modules/kls/04-family-moment-map.tex
  statement: >-
    For source-centered finite convex moment potentials phi_k and phi whose moment
    measures mu_k and mu are supported in one compact set Omega, mu_k converges weakly
    to mu if and only if phi_k converges pointwise to phi. The convergence is locally
    uniform, and gradients converge at common differentiability points. No Hessian
    convergence is asserted.
  import_class: published
  references: [Klartag2013MomentMeasures]

- id: thm:klartag-directional-moment-hessian
  kind: theorem
  status: imported
  route: moment-map-cmh
  file: modules/kls/04-family-moment-map.tex
  statement: >-
    For a regular centered compact-target log-concave law with covariance Sigma and
    canonical target-coordinate moment Hessian H, every theta and p>=1 satisfy
    (E |theta^T H theta|^p)^(1/p) <= 4 p^2 theta^T Sigma theta.
  import_class: published
  references: [Klartag2013MomentMeasures]

- id: thm:fathi-canonical-hessian-contraction
  kind: theorem
  status: imported
  route: moment-map-cmh
  file: modules/kls/04-family-moment-map.tex
  statement: >-
    If a regular centered target exp(-V) has covariance Sigma and
    D^2 V >= epsilon Sigma^{-1}, then its whitened canonical moment Hessian satisfies
    0 <= Hbar <= epsilon^{-1} I; consequently Q_lin <= epsilon^{-1}.
  import_class: published
  references: [Fathi2019SteinMomentMaps]

- id: thm:bonnet-rubinstein-moment-source-stability
  kind: theorem
  status: imported
  route: moment-map-cmh
  file: modules/kls/04-family-moment-map.tex
  statement: >-
    Under the full-dimensionality parameters R and r of Theorem 1.3, W1-close centered
    moment measures have source Gibbs densities that are L1-close after source
    translation, with modulus C(d,R/r)[(W1/R) log(1+R/W1)]^{1/2} in probability
    normalization. This asserts no gradient or Hessian stability.
  import_class: preprint-unreviewed
  references: [BonnetRubinstein2026MomentMeasureStability]
```

The last node would impose preprint citation debt on any downstream result using it.  It is not
needed for, and does not prove, CMH recovery.

The first three reference keys already occur in `fi_references.bib`.  The only exact append-only
BibTeX entry proposed is:

```bibtex
@misc{BonnetRubinstein2026MomentMeasureStability,
  author        = {Bonnet, Guillaume and Rubinstein, Yanir A.},
  title         = {Quantitative Stability and Numerical Resolution of the Moment Measure Problem},
  year          = {2026},
  eprint        = {2604.09914},
  archivePrefix = {arXiv},
  primaryClass  = {math.FA},
  note          = {Version 1, 10 April 2026; preprint}
}
```

No imported node is proposed for Delalande--Farinelli because its regularized representation is
not canonical, or for Machado--Ramos because the verified results stop at source-measure
stability.  Their citations can be added later only if the manuscript discusses those negative
comparisons.

## Precise remaining gap

Even on a common compact target set, the verified compactness is only

$$
\phi_k\to\phi\ \text{locally uniformly},
\qquad \nabla\phi_k\to\nabla\phi\ \text{a.e.}
$$

What is missing is a dimension-free uniform-integrability/semicontinuity principle of the form

$$
\liminf_k
\lambda_{\max}\!\left(
\Sigma_k^{-1/2}\int D^2\phi_k\Sigma_k^{-1}D^2\phi_k e^{-\phi_k}
\Sigma_k^{-1/2}
\right)
\le C,
$$

or a direct construction of approximants satisfying such a bound.  Scalar estimates for
$\theta^TH\theta$ do not supply the column-energy estimate for $|H\theta|^2$, and strong
log-concavity supplies it only with a constant that diverges under removal of the Gaussian
tilt.  Even a successful linear recovery theorem would still leave the CMH route's
variable-field/solenoidal upgrade unresolved.

## Citation debt and collisions with repository fences

- Theorem 5.12 of Machado--Ramos is not importable from the inspected version because its proof
  is explicitly omitted.  Treat it as a lead only.
- Bonnet--Rubinstein and Machado--Ramos are 2026 unreviewed preprints; neither can support an
  unconditional proved downstream node.
- No collision was found with the repository's static commutator/orientation fence.  Klartag's
  directional scalar moment bound lands exactly on the weaker side of that fence.
- Regularized moment-measure stability cannot be transferred to canonical CMH without changing
  the pushforward map; doing so would contradict the repository's canonicality requirement.
- Existing compact-target regularity imports provide smoothness/existence, not uniform
  $Q_{\rm lin}$ control.  No citation reviewed here upgrades them.

## Searched and not found

Queries included: `moment measure Hessian stability`, `moment map Hessian W2 convergence
log-concave`, `stability moment measure problem second derivatives`, `regularized moment
measures Hessian`, `Monge Ampere moment measure W2 stability Hessian`, `canonical Stein kernel
continuity`, and searches within the full texts for `Hessian`, `second derivatives`, `gradient
convergence`, and `semicontinuity`.

No theorem was found giving any of the following:

1. $D^2\phi_k$ convergence for canonical moment potentials from $W_2(\mu_k,\mu)\to0$;
2. convergence of $\nabla\phi_k$ in a norm weighted by $D^2\phi_k$;
3. lower semicontinuity of $\mathbb E[H\Sigma^{-1}H]$ or $Q_{\rm lin}$;
4. a dimension-free uniform bound on $\mathbb E[H\Sigma^{-1}H]$ for arbitrary log-concave
   targets;
5. a compact-target approximation retaining such a bound uniformly as the support expands.

## Handoff

```yaml
next_role: orchestrator
next_prompt: >-
  Review the four candidate imported nodes in this note. The clean published imports are
  Klartag's compact-support potential continuity/directional Hessian estimates and Fathi's
  strongly-log-concave canonical contraction. If the new inverse-stability context is wanted,
  atomically add thm:bonnet-rubinstein-moment-source-stability with import_class
  preprint-unreviewed and the exact BonnetRubinstein2026MomentMeasureStability BibTeX entry
  above. Add manuscript anchors and ledger records together. Do not infer canonical-Hessian
  continuity: every verified stability result stops at source densities, potentials, or
  pointwise gradients, while Q_lin is quadratic in the canonical Hessian.
```
