---
numbering:
  enumerator: "40.%s"
---

(sec:moment-map-cmh)=
# The moment map: a deterministic inequality for the moment-map Hessian

## Overview of the approach

**The idea.** Bound one deterministic quantity, the canonical moment-Hessian constant $\CMH$, and pass it to an affine Poincaré inequality. No stochastic localization anywhere.

**The link to KLS.** The strongest link of any approach here, and the one place this document gives an implication *into* the neighbourhood of KLS rather than assuming one:

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

**What it gives.** The endpoint is made precise and then computed. It is given operator data rather than left as a slogan ([](#def:cmh)); it dominates the affine Poincaré constant ([](#thm:cmh-implies-affine-poincare)); its Hodge content separates an affine channel from a solenoidal excess ([](#prop:cmh-hodge)); and it is evaluated *exactly* on the line, on products, and on every log-concave Dirichlet law (Section [](#sec:cmh-exact-cases)). That last concerns a nontrivial family and is not a consistency check. The linear sector is resolved separately and exactly: it equals a directional third moment plus a named high-mode remainder ([](#lem:linear-sector-third-moment), [](#cor:gate-zero-third-moment)), and the exponential cones of §[](#subsec:cmh-cones) give it an explicit non-product equality set with an explicit moment map ([](#prop:cone-moment-map)–[](#prop:cone-linear-sector)).

**What blocks it.** The approach splits, and the split is the point. A *construction* layer: [](#conj:mm-invariant-lift), deriving the target-flat Schur–Piola multiplier lift invariantly — the *lift* is the tensor through which a Haar multiplier, defined on one block of a Schur split of the Hessian, acts on the whole space, so far computed in coordinates and in low split dimensions only — and [](#conj:mm-square-root-commutator), controlling the full Haar sum of $[N^{1/2},K_M]$ errors without double-spending the positive reservoir. A *falsification* layer: gate zero, the inequality tested on linear functions only ([](#conj:gate-zero)), its sharp form ([](#conj:gate-zero-sharp)), and the solenoidal perturbation test [](#conj:cmh-second-variation). The first pair would complete the approach; a negative answer in the second would rule it out. The two gate statements are not interchangeable as falsifiers: a counterexample to the sharp form at constant $2$ would leave $\mathrm{CMH}(4)$ untouched, since only the constant $4$ statement is what CMH needs on linear tests.

**What fails, and why.** [](#prop:letwin-not-gate-zero) is the decisive negative result: no matrix-moment argument supplies gate zero, so the fixed-matrix estimate cannot be leveraged into the linear sector. Gate zero is itself an instance of the average-versus-uniform pattern of Section [](#sec:kls-remaining) — it asks $\lmax(\E H^2)\le4$ where only $\Tr(\E H^2)\le2n$ is known — so this approach relocates that difficulty rather than escaping it, and [](#prop:letwin-not-gate-zero) shows the relocation is not free. A separate saturation risk is discussed in Section [](#sec:cmh-exact-cases).

**What would settle it.** The approach succeeds if the construction layer is carried out *and* [](#ass:uniform-cmh-approximants) is established, or replaced by the weaker recovery-envelope assumption [](#ass:cmh-recovery-envelope), which suffices by [](#cor:cmh-recovery-sequence-suffices). It fails if gate zero is false, or if some admissible log-concave perturbation of the saturating one-sided-exponential product has strictly positive second variation of $\CMH$ ([](#conj:cmh-second-variation)), which would push $\CMH$ above $4$. Both falsifiers are cheaper than the construction, which is why they are stated as gates.

**How to read it.** Read *out of order*: the normalization layer, Section [](#sec:cmh-normalization), is logically prior and should be read first, then the exact cases in Section [](#sec:cmh-exact-cases), then this construction layer. The moment-map family survey is Section [](#sec:family-moment-map). None of the localization apparatus of the shared technical foundations is used by this approach; its longer calculations are in Appendix [](#sec:appendix-moment-map).

This section records a second, deterministic use of the moment map. Its aim is to extend [](#thm:letwin-moment-map) from constant matrices to multiplier fields selected by an arbitrary test function. Its conclusion is not established here: the identities displayed in this section outside labelled statements are formal calculations, not proofs, and the labelled problems below say what closing each gap would deliver.

% Agent entry points for this approach: the approaches of research/program/portfolio.yaml.

The moment-map approach is organized in two layers. This section is the *construction* layer: Haar compression, Schur–Piola transport, and the square-root commutator that the program must control. Sections [](#sec:cmh-normalization) and [](#sec:cmh-exact-cases) are the *normalization* layer, logically prior: they fix the endpoint's operator data, show that it implies the affine Poincaré inequality, compute it exactly on the line, on products, and on every log-concave Dirichlet law, and isolate the two falsification tests the approach admits. The two layers share the target $\mathrm{CMH}(4)$ and almost no machinery; a reader starting here should read §[](#sec:cmh-normalization) first.

To avoid a collision with the stochastic quantities $H_t,S_t,K_t$ and $A_t$ used earlier, all objects in this section are stationary moment-map objects: $H=D^2\phi$ is the Hessian metric, $N$ is a weighted elliptic operator, and $K_M$ is a compressed multiplier.

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

The approximation closure [](#prop:cmh-approximation-closure) is conditional on [](#ass:uniform-cmh-approximants). Centered Gaussian-convolution, Gaussian-tilt, and growing-ball approximants converge in ambient $W_2$, and the affine Poincaré inequality passes with no loss on the intrinsic closed covariance-form domain, including proper affine-support degeneration. The closure argument supplies no bound on $\CMH$: the uniform premise $\sup_k\CMH(\mu_k)\le C$ is exactly what it assumes. Two consequences of the explicit normalization bear directly on the rest of this section.

First, as the summary above says, the reduction is not known to be an equivalence: the solenoidal excess of [](#prop:cmh-hodge) is a channel KLS does not directly control, and no separating measure is known ([](#cor:cmh-hodge-comparison)). The program below pursues a sufficient condition of unknown truth value, not a reformulation of the conjecture.

Second, the endpoint now has a cheap necessary condition. Testing $\mathrm{CMH}(4)$ on linear functions gives gate zero, $\E[H\Sigma^{-1}H]\preceq4\Sigma$ ([](#conj:gate-zero)), and [](#prop:letwin-not-gate-zero) shows by an exact countermodel that [](#thm:letwin-moment-map) does not imply it through matrix algebra alone. The obstruction there is the *static* commutator [](#eq:static-commutator), $\Tr(B^2H^2)=\Tr(BHBH)+\tfrac12\norm{[B,H]}_{\HS}^2$ — the finite-dimensional shadow of the square-root commutator of [](#conj:mm-square-root-commutator). A program that controls $[N^{1/2},K_M]$ must in particular control $\E\norm{[B,H]}_{\HS}^2$; conversely, a counterexample to gate zero would rule out this approach without any Haar-tree analysis at all.

## Haar compression and the commutator error

On the mean-zero subspace, formally set

$$
N=D_\nu^*H^{-1}D,
\qquad
Q_M=D_\nu^*H^{-1/2}MH^{-1/2}D,
$$

and

$$
R=H^{-1/2}DN^{-1/2},
\qquad K_M=R^*MR.
$$

On a common core, $R^*R=I$ and

$$
Q_M=N^{1/2}K_MN^{1/2}.
$$

For normalized Haar contrast multipliers $M_S$, the formal error is therefore

```{math}
:label: eq:mm-commutator-error
e_S(u)=Q_{M_S}u-K_{M_S}Nu
=[N^{1/2},K_{M_S}]N^{1/2}u.
```

The reported complete-tree Bessel deficit is

```{math}
:label: eq:mm-bessel-deficit
\mathfrak B(h)
=\left(1-\frac1n\right)\norm{h}^2-\sum_S\norm{K_{M_S}h}^2
=\sum_S\norm{(I-RR^*)M_SRh}^2.
```

Numerical experiments produce rotated examples with negative individual sibling deficits, and Laguerre near-extremizers that consume nearly all descendant slack. These are evidence, not proofs, and no such example is recorded here as an exact counterexample; what they suggest is that neither nodewise positivity nor a fixed fractional allocation of slack along the tree can work.

% Agent note: the witnesses behind this paragraph are not persisted; see the originating exploration.

## Schur–Piola transport and local algebra

For a $1+d$ split write

$$
H=\begin{pmatrix}h&b^\top\\ b&C\end{pmatrix},\qquad
v=C^{-1}b,\qquad s=h-b^\top C^{-1}b,\qquad \Delta=\det C,
$$

and $X=\partial_r-v\cdot\nabla_q$. Block algebra, Piola's identity, and Hessian compatibility formally give

$$
\operatorname{cof}H
=\Delta\begin{pmatrix}1&-v^\top\\-v&vv^\top+sC^{-1}\end{pmatrix},
\qquad
\operatorname{div}(\Delta X)=0,
$$

$$
Xv=C^{-1}\nabla_qs,
\qquad XC=J^\top C=CJ,
\qquad \Tr(C^{-1}XC)=\operatorname{div}_qv.
$$

If $z=\nabla_q\phi$ is the child target coordinate, then $Xz=0$; for $x=\nabla\phi$, $Xx_\perp=0$ and $Xx_0=s$. Hence $s^{-1}X$ is the pullback of $\partial_{x_0}$. In particular, the trace/conformal derivative is constrained by the Schur connection and is not a free scalar mode.

At a Schur-normal $1+2$ point, let $T\in\operatorname{Sym}_2$, $a,g\in\R^2$, let $R_\perp e_1=e_2$ and $R_\perp e_2=-e_1$, and use $\operatorname{sym}(u\otimes v)=\tfrac12(u\otimes v+v\otimes u)$. Put

$$
B_i=\operatorname{sym}(g\otimes R_\perp^\top e_i).
$$

The fixed-target coordinate form expands exactly as

$$
\begin{aligned}
Q(a,T,g)
&=8|a|^2+\frac12\sum_i\norm{\{B_i,T\}}_{\HS}^2-4a\cdot R_\perp Tg\\
&=8\left|a-\frac14R_\perp Tg\right|^2
+\frac32|Tg|^2+\frac14(\Tr T)^2|g|^2\ge0.
\end{aligned}
$$

An independent coordinate expansion checked this identity. What is missing is the invariant identification of the tensorial lift actually generated by the global operator, and a reduction covering all higher-dimensional splits. Positivity in $1+2$, $1+3$, and $2+2$ alone would not be a dimension-free theorem; the missing step is [](#conj:mm-invariant-lift).

:::{prf:conjecture} Invariant lift and all-split reduction
:label: conj:mm-invariant-lift
The multiplier transport can be derived in a target-flat Schur–Piola frame without choosing a moving-frame coefficient by hand, and the resulting Codazzi shape terms decompose, for arbitrary split dimensions, into controlled irreducible pieces, each negative component of which is matched by a retained Letwin/Monge–Ampère square.
:::

## Two solenoidal channels

Let $S(z)=\E[C\mid z]$ be the inherited child block of the parent Stein kernel and let $K(z)$ be the canonical child moment-map Stein kernel. Both solve the same Stein equation, so

$$
\mathsf D=S-K,
\qquad \partial_\beta(\rho\mathsf D_{\alpha\beta})=0.
$$

In a two-dimensional child, subject to topology and boundary conditions,

$$
\rho\mathsf D=R_\perp^\top D^2\lambda R_\perp
$$

is the Airy representation. For a parent datum $h$, the reported canonical flux residual has the form

```{math}
:label: eq:mm-hodge-residual
r_h=r_{\mathrm{cond}}+(I-\Pi_K)\mathsf D\nabla v.
```

Thus a conditional-flux channel and a canonical-versus-inherited Stein-kernel channel must be controlled separately: a single local conserved vector would identify the two projections in [](#eq:mm-hodge-residual), which differ in general.

## The main global obstacle

The cubic symbol does not cancel in general. With $A_M=H^{-1/2}MH^{-1/2}$, a direct calculation gives

$$
C_3(\xi)=2\left[(H^{-1}\xi)^r(\partial_rA_M)(\xi,\xi)
-(A_M\xi)^r(\partial_rH^{-1})(\xi,\xi)\right].
$$

It is expected, but not shown here, to equal

$$
2(H^{-1}\xi)^k\xi^\top H^{-1/2}[\Omega_k,M]H^{-1/2}\xi,
\qquad
\Omega_k=\frac12\left(H^{-1/2}\partial_kH^{1/2}
-(\partial_kH^{1/2})H^{-1/2}\right),
$$

exhibiting eigenframe rotation rather than conformal variation. The square-root bridge is the standard resolvent formula

$$
[N^{1/2},K_M]
=\frac1\pi\int_0^\infty t^{1/2}(N+t)^{-1}
[N,K_M](N+t)^{-1}\dd t,
$$

provided all forms and domains are justified.

:::{prf:conjecture} Global square-root commutator
:label: conj:mm-square-root-commutator
Let $\mathfrak R_{\mathrm{Letwin}}(u)$ be the retained nonnegative remainder made up of the available variable-multiplier, Codazzi, Monge–Ampère, corrector, and descendant squares, and of nothing else. Over the complete Haar tree

$$
2\sum_S\operatorname{Re}\langle K_{M_S}Nu,e_S(u)\rangle
+\sum_S\norm{e_S(u)}^2
\le \mathfrak B(Nu)+\mathfrak R_{\mathrm{Letwin}}(u)
$$

with a dimension-free constant and stable operator domains; and the complete-tree estimate supplies the global analytic input required by the fully defined CMH target of [](#rem:cmh-normalization).
:::

This is the main obstacle, but not the only gap. The invariant lift, all-split reduction, Hodge boundary conditions, and one-edge flux identity must be settled alongside it; the endpoint duality is not among them, since it is [](#thm:cmh-implies-affine-poincare). Note also that [](#prop:letwin-not-gate-zero) places a floor under the difficulty: even the constant-multiplier, static specialization of the estimate above is not available from [](#eq:letwin-matrix) by algebra, so no argument here may treat the commutator as a lower-order correction. Numerical experiments on model cases suggest that no scalar, conformal-only, or nodewise shortcut works. This is evidence rather than proof, and it points to an argument that is global and couples the matrix structure.
