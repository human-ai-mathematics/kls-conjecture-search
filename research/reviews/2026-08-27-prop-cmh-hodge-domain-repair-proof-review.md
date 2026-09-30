---
verdict: pass
authors:
  - /root/kls_proof_audit
  - /root/repair_cmh_hodge_domain_w3
reviewer: /root/review_cmh_hodge_domain_w3
fingerprints:
  solutions/thm-cmh-normalization.md: e46056f3b5044d2d4c8690907be9d6188b19d9093670e47c96c2691aa6fc28c5
  prop:cmh-bochner: 237164772a03afb3fb5bfb7a896dbd45f8487332637efa548b827454d8f8ea6c
  def:cmh: 5093f7f871d8362c179b6ca901822ba370d6a14237ed9bb3fe076ab964ff9722
  thm:cmh-implies-affine-poincare: 434bde8b4ccac59502b5c71180a4f20df98e1abc02f85826578bba9321480559
  prop:cmh-hodge: e53f8f0d21ff4afad0be69fb034e09db1f7daaa882338a1d927af40c3117410e
  rem:cmh-stronger-than-kls: 42676f87e102fd9313af73973dcf29ff5a7f17ccec197c3284254e7cf2c0e0cc
  thm:cmh-1d: 20ca97481f8d3f33bab114618adc59596740cec2d34e37ad9c5c8ec1b9fa9904
  prop:letwin-not-gate-zero: d01d5a5df0ca378b977846fd59185615903c42ec4bf019d71ebb41b5bf8e7c3a
---

*Follows up* `research/reviews/2026-08-25-kls-cmh-normalization-repair-audit.md`.

# CMH Hodge operator-domain repair — independent supplementary review

## Scope and immutable bytes

This is a cold supplementary review of
`solutions/thm-cmh-normalization.tex` at SHA-256
`1a241c1b1e1dfa2b417626661d9cc555f5cefeeb480b21b37695a56726826a38`.
It reviews the repaired operator-domain proof of `prop:cmh-hodge` and the directly affected
Hodge consequence `rem:cmh-stronger-than-kls`. The earlier five unaffected nodes in this
dossier remain outside this report's front-matter scope.

The review was reconstructed from the dossier, the statements at
`modules/kls/41-cmh-normalization.tex`, the KLS ledger, and the published source named below.
It did not use the repair author's narrative as proof evidence.

## Statement agreement

The manuscript and dossier make the same standing assumptions: $\mu$ is centered,
full-dimensional, log-concave, and in the regular moment-map class; its covariance
$\Sigma$ is positive definite; $\mathcal A=-\operatorname{Div}_\mu(H\nabla\,\cdot\,)$ is the
closed Stein operator; and the closed covariance operator is

$$
\mathcal A_1=-\operatorname{Div}_\mu(\Sigma\nabla\,\cdot\,),
\qquad L^2_0(\mu)=(\ker\mathcal A_1)^\perp.
$$

For $g\in\operatorname{Dom}(\mathcal A)$ with
$u=H\nabla g\in L^2(\mu;\Sigma^{-1})$, all three planes set

$$
h=\mathcal A g=-\operatorname{Div}_\mu u\in L^2_0(\mu),\qquad
\psi=\mathcal A_1^{-1}h,\qquad w=u-\Sigma\nabla\psi,
$$

and declare the centered inverse with the exact domain and codomain

$$
\mathcal A_1^{-1}:L^2_0(\mu)
\longrightarrow \operatorname{Dom}(\mathcal A_1)\cap L^2_0(\mu).
$$

The manuscript and dossier explicitly conclude weak divergence-freeness, orthogonality, the
Pythagorean energy identity, and the exact affine-Poincare Rayleigh supremum. The ledger writes
the last numerator as $\langle h,\mathcal A_1^{-1}h\rangle$ rather than as the covariance
gradient energy. These are identical by the checked form--operator identity below. Although the
ledger does not repeat $\operatorname{Div}_\mu w=0$ as a separate clause, it follows
algebraically from the ledger's definitions of $\mathcal A_1,h,\psi,w$; no mathematical
conclusion is lost.

The downstream corollary agrees across all three planes: the affine channel has optimal constant
$\mathsf C_{P,\mathrm{aff}}$, the remaining channel is nonnegative and solenoidal, and it
vanishes in dimension one under the declared no-flux convention. None of the statements asserts
a strict separation between CMH and KLS.

## Line-by-line mathematical check

### 1. Closed covariance gradient and its adjoint

Let

$$
\mathscr H_\Sigma=L^2(\mu;\Sigma^{-1}),\qquad
G_\Sigma f=\Sigma\nabla f,
\qquad \operatorname{Dom}(G_\Sigma)=H^1_\Sigma(\mu).
$$

The target norm satisfies

$$
\|G_\Sigma f\|_{\mathscr H_\Sigma}^2
=\int\langle\Sigma\nabla f,\nabla f\rangle\,d\mu.
$$

Thus the graph norm of $G_\Sigma$ is exactly the norm used to define the closed covariance-form
domain. This proves closedness, and the smooth core is dense in $L^2(\mu)$, so $G_\Sigma$ is
dense as required for an adjoint.

For a vector field $v$, the adjoint condition is

$$
\langle G_\Sigma f,v\rangle_{\mathscr H_\Sigma}
=\int\nabla f\cdot v\,d\mu
=\langle f,-\operatorname{Div}_\mu v\rangle_{L^2(\mu)}
$$

for every $f\in H^1_\Sigma(\mu)$. Hence
$G_\Sigma^*=-\operatorname{Div}_\mu$ with divergence interpreted weakly and with the closed
form's no-flux boundary convention. The standard closed-operator construction then gives
$G_\Sigma^*G_\Sigma=\mathcal A_1$ with exactly the dossier's operator domain.

### 2. Kernel, gap, and centered inverse

Because $\Sigma\succ0$ and the support of a full-dimensional log-concave law is connected,
$\mathcal E_\Sigma(f,f)=0$ forces $\nabla f=0$ and therefore
$\ker\mathcal A_1$ to be precisely the constants. A fixed full-dimensional log-concave law has
a finite, dimension-dependent Euclidean Poincare constant. Combining that fact with
$\Sigma\succeq\lambda_{\min}(\Sigma)I$ gives a finite affine Poincare constant and a positive
bottom spectral value for $\mathcal A_1$ on $L^2_0(\mu)$. Therefore zero is outside the spectrum
of that restriction, and spectral calculus gives the bounded everywhere-defined inverse

$$
\mathcal A_1^{-1}:L^2_0(\mu)
\longrightarrow\operatorname{Dom}(\mathcal A_1)\cap L^2_0(\mu).
$$

The external input here was checked in the published primary source S. G. Bobkov,
*Isoperimetric and Analytic Inequalities for Log-Concave Probability Measures*, Annals of
Probability 27 (1999), 1903--1921, DOI
[10.1214/aop/1022874820](https://doi.org/10.1214/aop/1022874820): Theorem 1.2 gives a positive
Cheeger constant for every log-concave probability measure with finite second moment, and
equation (1.3) together with Cheeger's implication gives the required finite Poincare constant.
This source is published and already appears as `Bobkov1999LogConcave` in the repository
bibliography.

### 3. The CMH source lies in the adjoint domain

For $g\in\operatorname{Dom}(\mathcal A)$, the defining form--operator relation is

$$
\int\langle H\nabla g,\nabla f\rangle\,d\mu
=\langle\mathcal A g,f\rangle_{L^2(\mu)}.
$$

The additional hypothesis $u=H\nabla g\in\mathscr H_\Sigma$ makes the left side precisely
$\langle G_\Sigma f,u\rangle_{\mathscr H_\Sigma}$. Consequently
$u\in\operatorname{Dom}(G_\Sigma^*)$ and
$G_\Sigma^*u=\mathcal A g=h$. Self-adjointness gives
$h\perp\ker\mathcal A$, and both $\ker\mathcal A$ and $\ker\mathcal A_1$ are the constants;
hence $h\in L^2_0(\mu)$ as stated.

### 4. Domain closure, divergence, orthogonality, and exact energy

The inverse mapping proved in Step 2 gives
$\psi\in\operatorname{Dom}(\mathcal A_1)$. By the definition of
$G_\Sigma^*G_\Sigma$, this says

$$
G_\Sigma\psi\in\operatorname{Dom}(G_\Sigma^*),\qquad
G_\Sigma^*G_\Sigma\psi=h.
$$

Both summands defining $w=u-G_\Sigma\psi$ are therefore in the adjoint domain, and

$$
G_\Sigma^*w=h-h=0.
$$

This is exactly $\operatorname{Div}_\mu w=0$ in the weak convention. The adjoint pairing is
legitimate at these domains and gives

$$
\langle G_\Sigma\psi,w\rangle_{\mathscr H_\Sigma}
=\langle\psi,G_\Sigma^*w\rangle_{L^2(\mu)}=0.
$$

Expanding $u=G_\Sigma\psi+w$ proves the displayed energy identity with no missing boundary
term. Replacing $u$ by any $v\in\operatorname{Dom}(G_\Sigma^*)$ satisfying
$G_\Sigma^*v=h$ gives the same orthogonal decomposition and proves the stated least-energy
property.

### 5. Spectral Rayleigh identification

For every $h\in L^2_0(\mu)$, the domains in Step 4 justify

$$
\|G_\Sigma\psi\|_{\mathscr H_\Sigma}^2
=\langle\mathcal A_1\psi,\psi\rangle
=\langle h,\mathcal A_1^{-1}h\rangle.
$$

The inverse is bounded, positive, and self-adjoint on $L^2_0$. Its quadratic-form supremum is
therefore $\|\mathcal A_1^{-1}\|$. Spectral calculus identifies this norm with the reciprocal
of the bottom covariance-form Rayleigh quotient. On functions perpendicular to the constants,
$\operatorname{Var}_\mu f=\|f\|_2^2$, so the reciprocal is exactly
$\mathsf C_{P,\mathrm{aff}}(\mu)$, with no loss of constants.

### 6. Direct Hodge consequence

The passage from the splitting to
$\mathsf C_{\rm CMH}(\mu)\ge\mathsf C_{P,\mathrm{aff}}(\mu)$ requires a density point not
written out in the short corollary. It is valid. If any $g\in\operatorname{Dom}(\mathcal A)$
has infinite CMH numerator, then $\mathsf C_{\rm CMH}=\infty$ and the comparison is immediate.
Otherwise the Hodge splitting applies to every source $h=\mathcal A g$ and yields

$$
\frac{\|H\nabla g\|_{L^2(\Sigma^{-1})}^2}{\|\mathcal A g\|_2^2}
\ge
\frac{\langle h,\mathcal A_1^{-1}h\rangle}{\|h\|_2^2}.
$$

For a self-adjoint operator,
$\overline{\operatorname{Ran}\mathcal A}=(\ker\mathcal A)^\perp=L^2_0(\mu)$.
Because $\mathcal A_1^{-1}$ is bounded, its quadratic-form supremum is unchanged when restricted
to this dense range. Taking suprema proves the claimed comparison.

In dimension one, $\operatorname{Div}_\mu w=0$ means that $\rho w$ is distributionally
constant. The no-flux convention encoded by the adjoint domain forces that constant to vanish,
so the solenoidal energy is zero. In dimensions at least two the manuscript's claim that the
ambient divergence-free subspace is nontrivial is correct (compactly supported weighted curls
inside the support provide examples), but neither the proof nor the statement claims that a CMH
extremizer has a nonzero such component.

## Hypothesis and dependency accounting

The proof uses positive definiteness of $\Sigma$, connectedness of the support, closedness and
density of the covariance form, finiteness of the fixed-law Poincare constant, the declared
form/operator meaning of $\mathcal A$, the extra integrability
$H\nabla g\in L^2(\mu;\Sigma^{-1})$, and the no-flux convention for the one-dimensional
conclusion. Centering and the full moment-map structure are needed by the surrounding CMH setup
but not by the abstract Hodge argument once $u,h,\Sigma$ are supplied; this is a possible
generalization, not a defect or an unstated premise.

`prop:cmh-hodge` depends only on the defined CMH operator setup `def:cmh`. The downstream
`rem:cmh-stronger-than-kls` additionally names `thm:cmh-1d`, which is already proved and
independently reviewed; this repair changes none of its proof bytes or hypotheses. There is no
open or `preprint-unreviewed` premise in the reviewed implication.

Neither reviewed node has a `bounded_by` edge. The fixed-cut Eldan obstructions therefore impose
no fence here, and the proof uses neither projection-only estimates nor any claimed equivalence
with the trace-upgrade cluster.

## Mechanical validation

The required standalone command

```text
cd solutions && latexmk -g -pdf -outdir=../build thm-cmh-normalization.tex
```

completed successfully and produced a six-page PDF. The warnings are only unresolved
cross-manuscript references allowed by `solutions/README.md`; there is no undefined control
sequence, emergency stop, or fatal TeX error. The dossier hash after the forced build remained
`1a241c1b1e1dfa2b417626661d9cc555f5cefeeb480b21b37695a56726826a38`.

## Corrections

None.

## Proposed ledger delta

Both nodes may remain unconditional `status: proved`. For each of `prop:cmh-hodge` and
`rem:cmh-stronger-than-kls`, retain
`solution: solutions/thm-cmh-normalization.tex`, retain/set `checked_by: agent`, and replace the
active `review:` pointer by
`research/reviews/2026-08-27-prop-cmh-hodge-domain-repair-proof-review.md`.

## Exclusions

This report does not re-review `q:cmh-normalization`, `def:cmh`, `prop:cmh-bochner`,
`thm:cmh-implies-affine-poincare`, or `prop:letwin-not-gate-zero`; their proof sections were not
altered by the Hodge repair. It also does not certify the separate exact-case dossier,
`rem:cmh-saturation-risk`, any CMH recovery or perturbation node, universal $\mathrm{CMH}(4)$,
gate zero, KLS itself, or any numerical artifact.
