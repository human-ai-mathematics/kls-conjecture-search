# Shared mathematical tools

This file is a compact index of reusable facts. The cited manuscript or ledger label owns the
formal statement; proof dossiers own full arguments and certification. Entries here record only
the fact, its common use, and the main guardrail.

## `lem:linear-test-lower` — linear-test lower bound

**Fact.** For every nonzero $v$,
$$
C_P(\pi)\ge \frac{v^T\operatorname{Cov}_\pi(X)v}{\|v\|^2},
\qquad
C_P(\pi)\ge\lambda_{\max}(\operatorname{Cov}_\pi(X)).
$$

**Use.** Refute a proposed upper bound with an exact covariance witness.

**Guardrail.** An empirical covariance is directional unless its sampling and numerical errors
are controlled.

## `thm:hardy-1d` — weighted Hardy criterion

**Fact.** For a density $p$, median $m$, and weight $a$, let
$B_+=\sup_{x>m}\mu([x,\infty))\int_m^xdt/(a(t)p(t))$ and define $B_-$ analogously. Then
$$
\max(B_+,B_-)\le C_{\mathrm{opt}}\le4\max(B_+,B_-).
$$

**Use.** Decide existence and scale of one-dimensional weighted Poincaré constants.

**Guardrail.** Use one-sided tails; a two-sided tail changes the normalization.

## Holley--Stroock perturbation

**Source.** Holley--Stroock bounded perturbation principle.

**Fact.** If $d\pi=e^{-W}d\nu/Z$ and $\operatorname{osc}(W)\le A$, then
$C_P(\pi)\le e^A C_P(\nu)$, with the analogous log-Sobolev bound.

**Use.** Transfer constants through a uniform density-ratio comparison.

**Guardrail.** Total variation convergence alone does not provide this comparison.

## Tensorization

**Fact.** For $\mu=\bigotimes_i\mu_i$,
$C_P(\mu)=\max_i C_P(\mu_i)$. If coordinate $i$ has weighted constant $C_i$ with weight $a_i$,
then the product has constant $\max_i C_i$ for the form
$\int\sum_i a_i|\partial_i f|^2d\mu$.

**Use.** Lift one-dimensional estimates to product measures.

**Guardrail.** A hierarchical or otherwise dependent law is not a product.

## $T_2$ covariance constraint

**Fact.** Under the convention
$W_2^2(\nu,\pi)\le2C\,\mathrm{KL}(\nu\|\pi)$,
$$
\operatorname{Cov}_\pi(X)\preceq CI,
\qquad
C_{\mathrm{TCI}}(\pi)\ge\lambda_{\max}(\operatorname{Cov}_\pi(X)).
$$

**Use.** Supply a necessary lower constraint for transportation-cost constants.

**Guardrail.** This is not an upper bound or an estimator of the optimal constant.

## `lem:a5-lipschitz` — Lipschitz transport

**Fact.** If $T_\#\nu=\mu$ and $T$ is globally $L$-Lipschitz, then
$C_P(\mu)\le L^2C_P(\nu)$; the same implication holds for $C_{\mathrm{LS}}$ and
$C_{\mathrm{TCI}}$.

**Use.** Compare functional inequalities under a controlled reparameterization.

**Guardrail.** No global comparison follows when the map is not globally Lipschitz.

## `lem:a5-pi-exp-tail` — Poincaré forces exponential tails

**Fact.** If a Euclidean law has Poincaré constant $C<\infty$, then every real
$1$-Lipschitz $f\in L^2$ satisfies
$$
\mathbb E e^{c|f-\operatorname{med}f|}<\infty
\quad\text{for }0<c<\frac{\log2}{2\sqrt C}.
$$

**Use.** Rule out a finite Poincaré constant from a Lipschitz heavy-tail witness.

**Guardrail.** The witness must be globally Lipschitz in the metric of the claimed inequality.

## `prop:a1-bulk-tail` — inverse-Hessian certificate

**Fact.** For smooth $U$ on $\mathbb R^d$ with
$mI\preceq\nabla^2U\preceq MI$ and $\pi\propto e^{-U}$,
$$
C_P(\pi)\le\mathbb E_\pi\lambda_{\max}((\nabla^2U)^{-1}).
$$

**Use.** Convert an average inverse-curvature estimate into a Poincaré bound.

**Guardrail.** The operative quantity is
$\mathbb E\lambda_{\max}(H^{-1})$, not $\lambda_{\max}((\mathbb EH)^{-1})$; check the source
statement before weakening its regularity assumptions.

## `prop:a1-mode-leverage` — mode-to-tail geometry

**Fact.** With mode Hessian $\widehat H$ and
$\eta=\max_iL_i\sqrt{x_i^T\widehat H^{-1}x_i}$, the source theorem gives radial curvature and
potential envelopes. When its hypotheses hold and $\eta<1$,
$$
C_P\le K_d(\eta)\lambda_{\max}(\widehat H^{-1}),
\qquad K_d(\eta)\to1\quad(\eta\to0).
$$

**Use.** Produce a data-computable certificate and recover the Fisher scale in low-leverage
sequences.

**Guardrail.** $\eta\ge1$ rejects this certificate, not the existence of a Poincaré inequality.

## Unrestricted posterior-mean transport dual

**Source.** `eq:a4-mean-dual` (manuscript label `thm:a4-mean-dual`).

**Fact.** For $X\sim\pi$,
$$
C_{\mathrm{mean},\mathrm{all}}(\pi)
=\sup_{\|u\|=1}\sup_{t\ne0}\frac{2}{t^2}
\log\mathbb E e^{tu^T(X-\mathbb EX)}.
$$

**Use.** Compute unrestricted posterior-mean transport through directional exponential moments.

**Guardrail.** For a restricted family $\mathcal Q$, only
$C_{\mathrm{mean},\mathcal Q}\le C_{\mathrm{mean},\mathrm{all}}$ is automatic.

## Symmetry averaging and block stability

**Source.** `lem:a4-symmetrization` and `prop:a5-block-stability`.

**Fact.** If a finite isometric group preserves $\pi$, then
$\bar q=|G|^{-1}\sum_g g_\#q$ preserves invariant observables and does not increase either
$\mathrm{KL}(q\|\pi)$ or $W_2^2(q,\pi)$. If invariant laws $\pi,\widetilde\pi$ satisfy
$\operatorname{osc}\log(d\widetilde\pi/d\pi)\le\varepsilon$, their invariant and non-invariant
restricted Poincaré gaps change by factors at most $e^{\pm\varepsilon}$.

**Use.** Separate quotient geometry from physical multimodality and test stability of a block
ordering.

**Guardrail.** The ratio $W_2^2/\mathrm{KL}$ need not decrease under averaging, and the
variational family must contain the average.
