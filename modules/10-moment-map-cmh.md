---
numbering:
  enumerator: "10.%s"
---

(sec:moment-map-cmh)=
# The moment map: a deterministic inequality for the moment-map Hessian

## Overview of the approach

**The idea.** Bound one deterministic quantity, the canonical moment-Hessian constant $\CMH$, and pass it to an affine Poincaré inequality. No stochastic localization anywhere.

**The link to KLS.** It is the only approach here with a proved implication towards KLS rather than an assumed one: the target inequality bounds the affine Poincaré constant with no loss of constant, and the passage to every log-concave law needs one further assumption:

$$
\mathrm{CMH}(4)
\ \xRightarrow[\ \text{endpoint reduction}\ ]{}\
\CPaff\le\CMH
\ \xrightarrow[\ \text{approximation, under an assumption}\ ]{}\
\text{all log-concave }\mu .
$$

The first arrow is [](#thm:cmh-implies-affine-poincare). The second is [](#prop:cmh-approximation-closure), which assumes [](#ass:uniform-cmh-approximants). Throughout this approach the *endpoint* is the inequality $\mathrm{CMH}(4)$ itself — the last statement of the chain, which everything else here serves to prove — and the *endpoint reduction* is the first arrow, from it to the affine Poincaré inequality.

Two cautions belong here rather than in a footnote, because they change how the diagram should be read. $\mathrm{CMH}(4)$ is *not known* to be a reformulation of [](#conj:kls): by [](#prop:cmh-hodge) it additionally demands control of a solenoidal excess that vanishes identically in dimension one, so it may be strictly stronger, and this manuscript does not decide whether the two are equivalent at constant $4$ ([](#cor:cmh-hodge-comparison)). And the passage to arbitrary log-concave limits is only *conditional*: [](#prop:cmh-approximation-closure) rests on the separate premise [](#ass:uniform-cmh-approximants) about regular approximants.

**What it builds on.** From the literature: the fixed-matrix Hessian bound ([](#thm:letwin-moment-map)) and the moment-Hessian trace bound ([](#thm:chen-klartag-moment-hessian)); moment-potential regularity from [@BermanBerndtsson2013RealMA] and the Stein identity from [@Fathi2019SteinMomentMaps]. Set up in this manuscript: the endpoint's operator data ([](#def:cmh)) and the statements of Sections [](#sec:cmh-normalization)–[](#sec:cmh-exact-cases), each of which displays its status next to its title.

**What it gives.** The endpoint is made precise and then computed. It is given operator data rather than left as a slogan ([](#def:cmh)); it dominates the affine Poincaré constant ([](#thm:cmh-implies-affine-poincare)); its Hodge content separates an affine channel from a solenoidal excess ([](#prop:cmh-hodge)); and it is evaluated *exactly* on the line, on products, and on every log-concave Dirichlet law (Section [](#sec:cmh-exact-cases)). That last concerns a nontrivial family and is not a consistency check. The linear sector is resolved separately and exactly: it equals a directional third moment plus a named high-mode remainder ([](#lem:linear-sector-third-moment), [](#cor:gate-zero-third-moment)), and the exponential cones of §[](#subsec:cmh-cones) give it an explicit non-product equality set with an explicit moment map ([](#prop:cone-moment-map)–[](#prop:cone-linear-sector)). For product-simplex bases the full gate spectrum and its equality subspaces are determined by [](#prop:product-simplex-cone-gate).

**What blocks it.** The approach splits, and the split is the point. A *construction* layer (Section [](#sec:mm-construction)): [](#conj:mm-invariant-lift), deriving the target-flat Schur–Piola multiplier lift invariantly — the *lift* is the tensor through which a Haar multiplier, defined on one block of a Schur split of the Hessian, acts on the whole space, so far computed in coordinates and in low split dimensions only — and [](#conj:mm-square-root-commutator), controlling the full Haar sum of $[N^{1/2},K_M]$ errors without double-spending the positive reservoir. A *falsification* layer: gate zero, the inequality tested on linear functions only ([](#conj:gate-zero)), its sharp form ([](#conj:gate-zero-sharp)), and the solenoidal perturbation test [](#conj:cmh-second-variation). The first pair would complete the approach; a negative answer in the second would rule it out. The two gate statements are not interchangeable as falsifiers: a counterexample to the sharp form at constant $2$ would leave $\mathrm{CMH}(4)$ untouched, since only the constant $4$ statement is what CMH needs on linear tests.

**What fails, and why.** [](#prop:letwin-not-gate-zero) is the decisive negative result: no matrix-moment argument supplies gate zero, so the fixed-matrix estimate cannot be leveraged into the linear sector. Gate zero is itself an instance of the average-versus-uniform pattern of Section [](#sec:kls-remaining) — it asks $\lmax(\E H^2)\le4$ where only $\Tr(\E H^2)\le2n$ is known — so this approach relocates that difficulty rather than escaping it, and [](#prop:letwin-not-gate-zero) shows the relocation is not free. A separate saturation risk is discussed in Section [](#sec:cmh-exact-cases).

**What would settle it.** The approach succeeds if the construction layer is carried out *and* [](#ass:uniform-cmh-approximants) is established, or replaced by the weaker recovery-envelope assumption [](#ass:cmh-recovery-envelope), which suffices by [](#cor:cmh-recovery-sequence-suffices). It fails if gate zero is false, or if some admissible log-concave perturbation of the saturating one-sided-exponential product has strictly positive second variation of $\CMH$ ([](#conj:cmh-second-variation)), which would push $\CMH$ above $4$. The perturbative test first requires a two-sided admissible family in the precise source-potential ansatz; changing the target density potential is a different question (Section [](#subsec:cmh-saturation)).

**How to read it.** In the order of the chapters. This one presents the approach and its first necessary condition; Section [](#sec:cmh-normalization) makes the target precise; Section [](#sec:cmh-exact-cases) computes it exactly where that is possible; Section [](#sec:mm-construction), the construction layer, attempts to prove it. The two layers share the target $\mathrm{CMH}(4)$ and almost no machinery. The moment-map family survey is Section [](#sec:family-moment-map). None of the localization apparatus of the shared technical foundations is used by this approach; its longer calculations are in Appendix [](#sec:appendix-moment-map).

% Agent entry points for this approach: the approaches of research/program/portfolio.yaml.

:::{prf:remark} Program of the moment-map approach
:label: rem:cmh-program
First make the target inequality CMH and its reduction to KLS precise. Then derive the invariant multiplier lift, control the resulting square-root commutators with the full positive reservoir, and sum the complete Haar tree without nodewise positivity or duplicated slack.
:::

## The endpoint and a first necessary condition

The starting point is a covariance–moment–Hessian estimate of the schematic form

```{math}
:label: eq:cmh4-schema
\norm{\Sigma^{-1/2}H\nabla g}_2^2
\le4\norm{-Lg}_2^2.
```

A divergence-duality argument then gives $\CP(\mu)\le4$, the sharp plausible constant because a standard centered one-sided exponential has Poincaré constant $4$.

:::{prf:remark} CMH normalization and the reduction to KLS
:label: rem:cmh-normalization
Normalizing [](#eq:cmh4-schema) on the regular moment-map class means fixing $\Sigma$, $L$, the underlying $L^2$ space, the admissible class of $g$, and every inverse in it, so that the resulting estimate $\CMH(\mu)\le C$ implies $\CPaff(\mu)\le C$ on that class.
:::

This regular-class question is logically prior to the commutator calculation. [](#def:cmh) fixes $\Sigma$ as the covariance, $L$ as the Stein generator $\Div_\mu(H\nabla\,\cdot\,)$, the $L^2$ space as $L^2(\mu)$, the admissible class as $\Dom(\Aop)$, and every inverse as the pseudoinverse on $(\ker\Aop)^\perp$; [](#thm:cmh-implies-affine-poincare) is the reduction $\CPaff(\mu)\le\CMH(\mu)$, by a single Cauchy–Schwarz step, with a spectral truncation in place of an assumed gap.

:::{prf:assumption} Uniform CMH control on regular approximants
:label: ass:uniform-cmh-approximants
There is a universal $C<\infty$ such that, for every centered log-concave law $\mu$, the centered Gaussian-convolution, Gaussian-tilt, and growing-ball regular moment-map approximants $\mu_k$ satisfy $\sup_k\CMH(\mu_k)\le C$.
:::

:::{prf:proposition} Approximation closure for CMH
:label: prop:cmh-approximation-closure
Under [](#ass:uniform-cmh-approximants), with its constant $C$, every centered log-concave probability $\mu$ satisfies $\CPaff(\mu)\le C$, with the same constant and including when $\mu$ is carried by a proper affine subspace; in particular the bound is uniform over isotropic normalizations.
:::

The approximation closure [](#prop:cmh-approximation-closure) is conditional on [](#ass:uniform-cmh-approximants). Centered Gaussian-convolution, Gaussian-tilt, and growing-ball approximants converge in ambient $W_2$, and the affine Poincaré inequality passes with no loss on the intrinsic closed covariance-form domain, including proper affine-support degeneration. The closure argument supplies no bound on $\CMH$: the uniform premise $\sup_k\CMH(\mu_k)\le C$ is exactly what it assumes. Two consequences of the explicit normalization bear directly on the construction of Section [](#sec:mm-construction).

First, as the summary above says, the reduction is not known to be an equivalence: the solenoidal excess of [](#prop:cmh-hodge) is a channel KLS does not directly control, and no separating measure is known ([](#cor:cmh-hodge-comparison)). The construction pursues a sufficient condition of unknown truth value, not a reformulation of the conjecture.

Second, the endpoint now has a cheap necessary condition. Testing $\mathrm{CMH}(4)$ on linear functions gives gate zero, $\E[H\Sigma^{-1}H]\preceq4\Sigma$ ([](#conj:gate-zero)), and [](#prop:letwin-not-gate-zero) shows by an exact countermodel that [](#thm:letwin-moment-map) does not imply it through matrix algebra alone. The obstruction there is the *static* commutator [](#eq:static-commutator), $\Tr(B^2H^2)=\Tr(BHBH)+\tfrac12\norm{[B,H]}_{\HS}^2$ — the finite-dimensional shadow of the square-root commutator of [](#conj:mm-square-root-commutator). A program that controls $[N^{1/2},K_M]$ must in particular control $\E\norm{[B,H]}_{\HS}^2$; conversely, a counterexample to gate zero would rule out this approach without any Haar-tree analysis at all.
