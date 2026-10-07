---
title: "BK: explicit Poincaré and Cheeger bounds"
ledger-node:
  - thm:bk-explicit-poincare
  - cor:bk-cheeger
numbering:
  enumerator: "157.%s"
---

*Part of the Balasubramanian–Kasiviswanathan proof, Chapter [](#sec:bk-proof); the reading order is on the [full proofs](#sec:proofs-bk) page.*

**Overview.** Fix a regular measure and let the number of observed Appell
degrees tend to infinity. The integration-power bound loses its curvature
dependence. Approximation then preserves the resulting scalar Poincaré
constant. A contraction from isotropic coordinates handles every covariance
at most the identity, including proper affine supports. The existing
Cheeger comparison converts the spectral constant to the manuscript's
inverse Cheeger normalization.
This reconstructs Corollary 8.2, Section 9 and Appendix G of
[@BalasubramanianKasiviswanathan2026KLS], pinned at commit
`4837c33649ba2271f43c9684e9350ecbdd725f95`.

**Dependencies.** The substantive inputs are [](#thm:bk-appell-bound),
[](#cor:bk-integration-powers), and [](#lem:bk-regular-approximation), in
the conventions [](#def:bk-uniform-appell-coefficients) and
[](#def:bk-compatible-calculus). For the Cheeger corollary only, use the
classical comparison [](#eq:cheeger-two-sided)
[@Klartag2023Logarithmic; @Milman2009Isoperimetric]. The argument assumes
these BK inputs as stated; it neither reconstructs nor certifies them here.
It does not use the existing status of [](#conj:kls), a BKL result, or any
SZ v2 result.

:::{prf:theorem} Explicit universal bounds
:label: thm:sol-bk-explicit-poincare
Assume the BK inputs listed above. Put $R=10^8$ and
$K_P=1+2R^2=1+2\cdot10^{16}$.
Every log-concave probability law $\mu$ of covariance at most $I$, in every
dimension, satisfies
$$\operatorname{Var}_\mu f\le K_P\int|\nabla f|^2\,d\mu$$
for every real locally Lipschitz function on its affine support with finite
Dirichlet energy. Every such function belongs to $L^2(\mu)$. Gradients
are intrinsic to that support, and a point mass has Poincaré constant zero.
For every isotropic log-concave law of positive dimension,
$$h(\mu)^{-1}\le\sqrt{\pi(1+2\cdot10^{16})}.$$
These are [](#thm:bk-explicit-poincare) and [](#cor:bk-cheeger).
:::

:::{prf:proof}
Fix a centered regular law $\nu$ with covariance at most $I$ and fix one
positive lower curvature bound $a$ for it. The uniform coefficient theorem
gives $c_j(\nu)\le R^j/(j+1)^4$ for every $j\ge1$. For each integer
$D\ge2$, the integration-power corollary, with $\rho=R$, implies
$$C_P(\nu)\le1+2R^2\max\{1,a^{-1/(D+1)}\}.$$
Here the measure and $a$ remain fixed. Letting $D\to\infty$ yields
$C_P(\nu)\le1+2R^2=K_P$. Thus the scalar constant is independent of
both Hessian bounds and of dimension.

Now let $\mu$ be isotropic and log-concave on $\mathbb R^n$.
The regular approximation lemma supplies regular isotropic $\mu_j$
converging weakly to $\mu$. Each satisfies the just-proved Poincaré bound
$K_P$. For $u\in C_c^\infty$, weak convergence passes its variance and
Dirichlet energy to the limit, since $u,u^2,|\nabla u|^2$ are bounded and
continuous. The finite-energy extension in the same approximation lemma
then gives the inequality and square integrability for every locally
Lipschitz finite-energy test under $\mu$. No uniform curvature bound for
$\mu_j$ is required.

For an arbitrary covariance $\Sigma\preceq I$, translate to center the
law and work on its linear support $S$. If $\dim S=0$ there is nothing to
prove: every real function is constant almost surely. Otherwise $\Sigma$
is positive definite on $S$. Indeed a zero variance direction would force
the centered law onto a smaller linear subspace. Set
$Y=\Sigma^{-1/2}X$ on $S$, which is isotropic and log-concave. For a
locally Lipschitz function $f$ on $S$ of finite energy, the function
$g(y)=f(\Sigma^{1/2}y)$ is locally Lipschitz and
$$\int|\nabla g|^2d\mathcal L(Y)
=\mathbb E\langle\nabla f(X),\Sigma\nabla f(X)\rangle
\le\mathbb E|\nabla f(X)|^2<\infty.$$
The chain rule holds Lebesgue almost everywhere on $S$, hence almost surely
under this full-dimensional log-concave law on $S$.
The isotropic result implies $g(Y)\in L^2$ and
$$\operatorname{Var}f(X)=\operatorname{Var}g(Y)
\le K_P\mathbb E\langle\nabla f(X),\Sigma\nabla f(X)\rangle
\le K_P\mathbb E|\nabla f(X)|^2.$$
Translation back to the original affine support changes neither variance
nor energy.

Finally, in the normalization $\Psi_\mu=h(\mu)^{-1}$, the existing
comparison gives $h(\mu)^{-2}\le\pi C_P(\mu)\le\pi K_P$.
Taking the nonnegative square root proves the Cheeger assertion.
:::

**Fences respected.** The degree limit is taken at one fixed regular law,
then the scalar inequality is passed to nonsmooth laws. The covariance
contraction is intrinsic to the affine support. The Cheeger constant is
exactly the convention of [](#eq:hstar-def), not its reciprocal. No sharper
thin-shell, moment-map, conditional-fiber, or occupation premise is claimed.

:::{prf:remark} Dependencies and scope
This composition uses the separately proved BK coefficient, integration,
and approximation results. It supplies the scalar conclusion from those
inputs; it does not replace their proofs or independent reviews.
:::
