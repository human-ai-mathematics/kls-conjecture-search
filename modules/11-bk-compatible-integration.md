---
numbering:
  enumerator: "11.%s"
---

(sec:bk-proof)=
# Balasubramanian–Kasiviswanathan: compatible integration

Balasubramanian and Kasiviswanathan (BK) prove a dimension-free Poincaré bound through **compatible integration**: undo differentiation on symmetric tensor fields, control arbitrarily many integrations from finitely many polynomial estimates, and use stochastic localization to recover the next polynomial estimate. Their source is the 53-page preprint [@BalasubramanianKasiviswanathan2026KLS], arXiv v1 of 6 October 2026, read in an identical PDF first distributed on GitHub. The argument and its composition into [](#conj:kls) have been reconstructed in this manuscript and checked by separate reviewer agents; this is distinct from journal peer review or a person's acceptance.

The quantitative conclusion is $\CP\le1+2\cdot10^{16}$ ([](#thm:bk-explicit-poincare)). The large constant comes from an explicit induction proving $c_d\le10^{8d}/(d+1)^4$ simultaneously in degree, dimension and measure ([](#thm:bk-appell-bound)). The qualitative exponential criterion already appears in [](#prop:sz-exponential-coefficients-equivalence). BK establish its coefficient premise without importing KLS or a coefficient bound from the other proofs, then use their integration estimate to obtain the Poincaré constant directly. They retain the earlier Appell normalization and Letwin's quadratic variance bound as shared inputs.

## A Gaussian calculation and the proof's design

For the standard Gaussian on the line, the first Appell polynomials are $A_1(x)=x$, $A_2(x)=x^2-1$ and $A_3(x)=x^3-3x$. Centered integration sends $x$ to $(x^2-1)/2$, then to $(x^3-3x)/6$. More generally it sends $A_d/d!$ to $A_{d+1}/(d+1)!$. Since $\mathbb E A_d^2=d!$, the coefficients are $c_d=1/\sqrt{d!}$. Thus powers of an integration operator really do measure the same normalized polynomials as the earlier chapters.

For a general measure there are three separate difficulties. Weighted divergence need not preserve the tensor fields that can be integrated; the Hodge estimate controls the projection needed to restore this property. A bound for one integration repeated naively pays its loss at every step; the operator estimate instead retains one common factor for every power. Finally, polynomial norms change with the measure; covariance-normalized localization transfers the curved integration estimate back to the original law. The induction closes only if all three estimates have compatible constants. These are the successive parts of this chapter.

## Appell normalization and regular approximation

The coefficient convention agrees exactly with that of Song–Zhang. The supremum over covariance at most identity is useful because localization and subsequent linear changes of variables need not produce an isotropic law at every intermediate step.

:::{prf:definition} Uniform Appell coefficient conventions
:label: def:bk-uniform-appell-coefficients
For a probability law $\mu$ on $\mathbb R^n$ with all moments, define the symmetric Appell tensors by the formal identity
$$\frac{e^{\langle z,x\rangle}}{\mathbb E_\mu e^{\langle z,X\rangle}}
=\sum_{d\ge0}\frac{\langle A_d^\mu(x),z^{\otimes d}\rangle}{d!}.$$
For $T\in\operatorname{Sym}^d\mathbb R^n$, put $P_d^\mu[T]=\langle T,A_d^\mu\rangle$ and
$$c_d(\mu)=\frac1{d!}\sup_{\|T\|_{\mathrm{HS}}=1}\|P_d^\mu[T]\|_{L^2(\mu)},\qquad d\ge1,$$
where the tensor norm sums squares over ordered indices. Let $c_d^*$ be the supremum of $c_d(\mu)$ over all dimensions and all centered log-concave laws with $\operatorname{Cov}(\mu)\preceq I$, allowing proper affine supports. Positive-degree Appell polynomials have mean zero, so these $c_d$ coincide with the coefficients in [](#thm:sz-polynomial-variance).
:::

The analytic construction starts with a smooth potential bounded above and below in Hessian. Approximation is needed both to enter this class and to return to nonsmooth log-concave laws. The following approximation result keeps covariance, curvature and fixed-degree polynomial norms together.

:::{prf:lemma} Regular approximation preserving covariance and curvature
:label: lem:bk-regular-approximation
Let $\mu$ be a centered full-dimensional log-concave law with $\operatorname{Cov}(\mu)\preceq I$ and curvature at least $aI$, where $0<a\le1$. If $X\sim\mu$ and $G$ is an independent standard Gaussian, then
$$\mu_\varepsilon=\mathcal L\big((X+\sqrt\varepsilon G)/\sqrt{1+\varepsilon}\big)$$
is regular in the sense of [](#def:bk-compatible-calculus), has covariance at most $I$ and curvature at least $aI$, and converges weakly and in every fixed moment to $\mu$. For fixed dimension and degree, its Appell coefficients and the squared $L^2$ norms of every fixed-order derivative of a fixed-degree Appell polynomial with fixed leading tensor converge to those of $\mu$.
Every isotropic log-concave law is also the weak and fixed-moment limit of regular isotropic laws. A common Poincaré bound for the approximating laws passes to locally Lipschitz finite-energy functions under the limit law, including square integrability.
:::

## Compatible tensors and the Hodge projection

A vector field can be integrated to a scalar only if it is curl-free. At higher rank, the corresponding condition says that differentiating in any new slot produces a fully symmetric tensor. Subtracting a constant preserves this condition, so a centered primitive can be chosen at each stage. The derivative itself is left uncentered: its constant part carries the polynomial information that must not be discarded.

:::{prf:definition} Compatible symmetric tensor calculus
:label: def:bk-compatible-calculus
For a centered law $\mu(dx)=Z^{-1}e^{-V(x)}dx$ on $\mathbb R^n$ with $V\in C^\infty$ and $0<aI\preceq D^2V\preceq a_+I$, let $E_r=\operatorname{Sym}^r\mathbb R^n$, with the norm summing squares over all ordered indices. Put $C_0=L^2(\mu)$; for $r\ge1$, let $C_r$ be the closed subspace of $L^2(\mu;E_r)$ satisfying $\partial_iF_{jI}=\partial_jF_{iI}$ in distributions for every $(r-1)$-tuple $I$. Let $G_r=\{F\in C_r:\mathbb EF=0\}$, so $C_r=E_r\oplus G_r$. The raw derivative is $D_r:G_r\supset G_r\cap W^{1,2}(\mu;E_r)\to C_{r+1}$, $D_rU=\nabla U$. Its Hilbert adjoint is $D_r^*$, and $H_r=D_r^*D_r$ is the operator associated with the gradient form on $G_r$. When the inverse exists, write $\widetilde J_r=D_r^{-1}$ and $J_r=\widetilde J_r|_{G_{r+1}}$. Define $L_r:E_{r+1}\to G_r$ by $L_rT(x)=T\mathbin{\lrcorner}x$. Set $\mathcal H=\bigoplus_{r\ge0}G_r$, $\mathcal E=\bigoplus_{r\ge0}E_{r+1}$, $(JF)_r=J_rF_{r+1}$ and $(LT)_r=L_rT_r$ whenever these formulas define bounded operators.
:::

### The smallest matrix example

Take $F=D^2\psi$ on $\mathbb R^2$, with $\psi$ smooth and compactly supported, and let $Y_i=\sum_j(-\partial_j+\partial_jV)F_{ij}$ be its weighted divergence. At a point where $D^2V$ is diagonal with eigenvalues $\kappa_1,\kappa_2$, direct differentiation gives
$$\partial_1Y_2-\partial_2Y_1=(\kappa_1-\kappa_2)F_{12}.$$
Thus even a Hessian can acquire curl under weighted divergence. The Hodge projection estimate in the source bounds the squared norm of the discarded part by
$$\mathbb E\frac{(\kappa_1-\kappa_2)^2}{\kappa_1+\kappa_2}F_{12}^2.$$
The mixed entry initially contributes $(\kappa_1+\kappa_2)F_{12}^2$ to the curvature energy. After subtracting this loss, its remaining contribution is
$$
\left(\kappa_1+\kappa_2-
\frac{(\kappa_1-\kappa_2)^2}{\kappa_1+\kappa_2}\right)F_{12}^2
=\frac{2\kappa_1\kappa_2}{\kappa_1+\kappa_2}\,(2F_{12}^2).
$$
The factor $2F_{12}^2$ is exactly the ordered-index norm of the mixed symmetric component. Its remaining weight is the harmonic mean, at least $a$ when both curvatures are at least $a$. Equal curvatures produce no projection loss. The higher-rank estimate below retains this same lower bound without deterioration as more tensor slots are added.

This Hodge comparison concerns the potential $V$ of the original measure and compatible derivative fields. The moment-Hessian comparison in [](#cor:cmh-hodge-comparison) concerns the canonical moment-map Hessian and a different energy. The shared word “Hodge” supplies no implication between their hypotheses.

:::{prf:lemma} Compatible-tensor Hodge estimate and operator domains
:label: lem:bk-compatible-hodge
For every law in [](#def:bk-compatible-calculus) and every integer $r\ge0$, $D_r$ is closed, densely defined and bijective, and $\|D_r^{-1}\|\le\sqrt{\CP(\mu)}$. The fields $\{\nabla^{r+1}\psi:\psi\in C_c^\infty(\mathbb R^n)\}$ form a graph core for $D_r^*$. Every $F\in\operatorname{Dom}(D_r^*)$ belongs to $W^{1,2}(\mu;E_{r+1})$ and satisfies
$$\|D_r^*F\|_2^2\ge\|\nabla F\|_2^2+a\|F\|_2^2.$$
The coefficient $a$ is independent of $r$ and $n$.
:::

The proof begins with weighted integration by parts, then subtracts the energy lost by projecting divergence onto compatible fields. The preceding harmonic-mean calculation illustrates the curvature left after subtraction. At general rank, symmetry must prevent a loss growing with the number of indices. Extending the estimate from compactly supported potentials to the adjoint domain is part of the assertion, not a formal consequence of the calculation on smooth fields. The inverse derivative then provides the integration operators used below.

## From polynomial tests to every integration power

The decomposition into constant and centered tensors separates the inverse derivative into $L$ and $J$. Constants produce linear functions through $L$; repeated application of $J$ produces normalized Appell polynomials. This is the abstract version of the Gaussian calculation above.

:::{prf:proposition} Compatible integration and Appell coefficients
:label: prop:bk-integration-calculus
For every law in [](#def:bk-compatible-calculus) with $\operatorname{Cov}(\mu)\preceq I$, the operators $J$ and $L$ are bounded, and
$$\|J\|^2\le \CP(\mu)\le1+\|J\|^2,\qquad \|L\|\le1.$$
For every $r\ge0$,
$$H_r^{-1}=J_rJ_r^*+L_rL_r^*,$$
and, with $g_a(t)=t/(1+at)$ defined on positive operators by spectral calculus,
$$J^*J\preceq g_a(JJ^*+LL^*).$$
For every $j\ge1$, with the Appell normalization of [](#def:bk-uniform-appell-coefficients),
$$\|J^{j-1}L\|\le c_j(\mu).$$
More precisely, for every $r,k\ge0$ and $T\in E_{r+k+1}$,
$$J_r\cdots J_{r+k-1}L_{r+k}T=\frac1{(k+1)!}T\mathbin{\lrcorner}A_{k+1}^\mu,$$
where the product is $L_r$ if $k=0$ and the contraction leaves $r$ free indices.
:::

The identity for $H_r^{-1}$ comes from this orthogonal decomposition. The Hodge lower bound, followed by inversion of positive operators, gives the inequality with $g_a$. The Appell identity follows by differentiating their generating series and selecting the mean-zero primitive at every step. The remaining issue is operator theoretic: estimates on the special inputs $J^{j-1}L$ must control $J^k$ on arbitrary compatible fields.

The following operator lemma isolates that issue on any Hilbert space. Its crucial feature is that $Q_D(B)$ does not depend on the power $k$.

:::{prf:lemma} Uniform bound for powers from finitely many observations
:label: lem:bk-uniform-power-bound
Let $R:X\to X$ and $L:Y\to X$ be bounded operators on real or complex Hilbert spaces, let $a>0$, and suppose
$$R^*R\preceq g(RR^*+LL^*),\qquad g(u)=\frac{u}{1+au}.$$
For an integer $D\ge2$, let $\gamma_2,\ldots,\gamma_D\ge0$ be finite and satisfy $\|R^{j-1}L\|\le\gamma_j$ for $2\le j\le D$.
Then for every $B>0$ with $aB^{D+1}>\gamma_D^2$, simultaneously for all integers $k\ge0$,
$$\|R^k\|^2\le B^kQ_D(B),\qquad Q_D(B)=1+\sum_{j=1}^{D-2}\frac{j\gamma_{j+1}^2}{B^{j+1}}.$$
The sum is empty for $D=2$.
:::

The source uses the concavity and monotonicity of $g(u)=u/(1+au)$ to compare successive operator powers. The observed terms $R^{j-1}L$ control the boundary contributions, while the strict inequality $aB^{D+1}>\gamma_D^2$ absorbs the last one. Retaining the finite sum $Q_D(B)$ avoids multiplying a separate prefactor for every integration. At $D=2$ the sum is empty and the prefactor is exactly one; this is also what makes a degree-two estimate sufficient to start the argument.

:::{prf:corollary} Uniform integration powers
:label: cor:bk-integration-powers
Let $\nu$ be a centered regular log-concave law with $\operatorname{Cov}(\nu)\preceq I$ and $D^2V\succeq aI$ for $a>0$, with coefficients and integration operators as in [](#def:bk-uniform-appell-coefficients) and [](#def:bk-compatible-calculus).
If $D\ge2$ is an integer, $\rho\ge1$, and $c_j(\nu)\le\rho^j/(j+1)^4$ for $2\le j\le D$, then with $B=\rho^2\max\{1,a^{-1/(D+1)}\}$ one has, simultaneously for all integers $q\ge1$,
$$\|J^q\|^2\le2B^q,\qquad\|J_0\cdots J_{q-1}\|^2\le2B^q.$$
In particular $\CP(\nu)\le1+2B$.
:::

Substituting the coefficient majorant in $Q_D$ gives a convergent sum bounded by two. This yields all powers with one factor two, rather than a factor $2^q$. The seed below uses only Letwin's quadratic variance estimate [](#thm:letwin-qcts): it gives $c_2\le\sqrt2$, hence $\|JL\|\le\sqrt2$. The $D=2$ operator estimate then gives the stated bound by taking $B$ down to $(2/a)^{1/3}$. No higher-degree coefficient estimate is needed to start.

:::{prf:corollary} Quadratic integration seed
:label: cor:bk-quadratic-seed
For every centered regular log-concave law $\nu$ with $\operatorname{Cov}(\nu)\preceq I$ and $D^2V\succeq aI$, $a>0$, the graded integration operator of [](#def:bk-compatible-calculus) satisfies
$$\|J\|^2\le(2/a)^{1/3}.$$
:::

## Returning from curved laws to polynomial norms

Localization introduces curvature, but the polynomial and its law both move. BK use noise normalized by the inverse covariance. Letwin's quadratic estimate controls the third moments in the covariance equation; tensor covariance bounds keep that control when several derivatives are contracted together. These estimates hold on the full ordered tensor spaces, so their use does not hide a dimension-dependent trace.

:::{prf:lemma} Global covariance-normalized localization
:label: lem:bk-localization-covariance
Let $\mu_0$ be any compactly supported isotropic log-concave law on
$\mathbb R^n$. Write
$$
 \mu_{\theta,\Lambda}(dx)=Z(\theta,\Lambda)^{-1}
 e^{\theta\cdot x-x^T\Lambda x/2}\mu_0(dx),
$$
and let $m(\theta,\Lambda)$ and $A(\theta,\Lambda)$ be its mean and covariance.
The SDE, started at $(0,0)$,
$$
 d\theta_t=A_t^{-1/2}dB_t+A_t^{-1}m_tdt,
 \qquad d\Lambda_t=A_t^{-1}dt,
 \qquad \mu_t=\mu_{\theta_t,\Lambda_t},
$$
has a global solution with $A_t\succ0$. Every bounded Borel test has
$\int f\,d\mu_t$ a true martingale. On the full ordered tensor spaces,
for every integer $k\ge1$, $0\le s\le t$, every integer $d\ge1$, and
$s_1,\ldots,s_d\in[0,t]$,
$$
 \mathbb E[A_t^{\otimes k}\mid\mathcal F_s]
 \preceq e^{4k^2(t-s)}A_s^{\otimes k},\qquad
 \mathbb E[A_{s_1}\otimes\cdots\otimes A_{s_d}]
 \preceq e^{4d^2t}I.
$$
For $t>0$, $0\le q\le d$ and $\delta\ge0$,
$$
 \mathbb E[(A_t+\delta\Lambda_t^{-1})^{\otimes q}
       \otimes A_t^{\otimes(d-q)}]
 \preceq (1+\delta/t)^q e^{4d^2t}I.
$$

:::

The covariance proof first stops the process where the covariance and its inverse are bounded, derives the tensor inequalities there, and then removes the stopping. The mixed-time bound is needed because the accumulated curvature integrates inverse covariances over earlier times. The estimate with $\Lambda_t^{-1}$ is what allows that curvature to enter the later change of coordinates. Global existence and true martingales are included explicitly to justify the expectation identities.

The next assertion follows the polynomial adapted to the current law. Its lower-degree errors involve a convolution of previously bounded Appell coefficients. This is the induction's error term.

:::{prf:lemma} Moving Appell variance
:label: lem:bk-moving-appell-variance
Fix $d\ge2$ and finite constants $C_k\ge0$ such that $c_k(\nu)\le C_k$
for every isotropic log-concave law in every dimension and $1\le k<d$.
Set $\Sigma_d=\sum_{k=2}^{d-1}(d-k+1)C_kC_{d-k+1}$, with an empty sum zero.
For the localization of [](#lem:bk-localization-covariance), fixed $T\in\operatorname{Sym}^d\mathbb R^n$,
$p_t=P_d^{\mu_t}[T]$ and $V(t)=\mathbb E E_tp_t^2$, one has, for all $t\ge0$,
$$
 \sqrt{V(0)}\le e^{(d+1)t}\sqrt{V(t)}
       +d!\Sigma_dt\,e^{(2d^2+d+1)t}\|T\|.
$$

:::

Differentiating the normalized Appell generating function along the localization produces the evolution of its variance. Taking a square root allows the error terms to be bounded by products of lower-degree norms. Integrating the resulting differential inequality compares the original polynomial norm with its later norm. The latter is estimated by integrating $q$ times from degree $d-q$ under the now curved law.

:::{prf:proposition} Reverse coefficient transfer
:label: prop:bk-reverse-transfer
Fix integers $d\ge2$ and $1\le q\le d-1$, a real $0<\eta\le1$, and put $\delta=\eta^2/d^2$.
Suppose $M_q<\infty$ is nonnegative and every centered regular log-concave law $\nu$ in every dimension with $\operatorname{Cov}(\nu)\preceq I$ and curvature at least $\delta I$ satisfies
$\|J_0^\nu J_1^\nu\cdots J_{q-1}^\nu\|_{\mathrm{op}}\le M_q$.
Suppose finite $C_1,\ldots,C_{d-1}\ge0$ satisfy $c_k(\nu)\le C_k$ for every isotropic log-concave law in every dimension and $1\le k<d$.
Set $\Sigma_d=\sum_{k=2}^{d-1}(d-k+1)C_kC_{d-k+1}$, with empty sum zero.
Then the supremum over all centered log-concave laws in every dimension with covariance at most identity satisfies
$$
c_d^*\le e^{3\eta}\left[(1+\eta)^{q/2}M_qC_{d-q}+\frac{\eta}{d^2}\Sigma_d\right].
$$
:::

The transfer uses time $t=\eta/d^2$. Its curvature parameter $\delta=\eta^2/d^2$ and the covariance tensor bound together account for the factor $(1+\eta)^{q/2}$. The principal term contains an actual chain of $q$ integration operators; replacing its norm by a product of separate one-step estimates would lose the common-factor advantage. The second term uses only degrees below $d$, so the estimate can close an induction.

## Closing the induction and extracting the constant

The source chooses the summable majorant $\beta_d=R_*^d/(d+1)^4$. Its convolution has enough decay to absorb the moving-polynomial error. A finite initial range is supplied by the quadratic seed; for larger degrees the integration length is $q=\lfloor d/2\rfloor$, of order $d$, and the observation degree is $D=\lfloor\sqrt d\rfloor$, of order $\sqrt d$. Both are below $d$. The strict margin in the operator bound leaves room for the transfer factors. The explicit choices in Appendix E of the source lead to the following value. The numerical induction has been checked separately from the qualitative exponential criterion.

:::{prf:theorem} Uniform Appell coefficient growth
:label: thm:bk-appell-bound
For the coefficients of [](#def:bk-uniform-appell-coefficients), the constant $R_*=10^8$ satisfies
$$c_d^*\le\frac{R_*^d}{(d+1)^4}\qquad\text{for every integer }d\ge1.$$
Thus the same bound holds in every dimension for every centered log-concave law of covariance at most the identity, including laws supported on a proper affine subspace.
:::

To extract a spectral gap, fix one regular law and its positive lower curvature $a$. Let the observation degree $D$ tend to infinity in [](#cor:bk-integration-powers), with $\rho=R_*$. Then $a^{-1/(D+1)}\to1$, and the one-step estimate gives $\CP\le1+2R_*^2$. Only after this degree limit is taken does approximation pass the common scalar inequality to arbitrary log-concave laws. This order avoids requiring a common positive curvature for all laws.

:::{prf:theorem} Explicit Poincaré bound from compatible integration
:label: thm:bk-explicit-poincare
Let $K_P=1+2\cdot10^{16}$. Every log-concave probability measure $\mu$ in every dimension with $\operatorname{Cov}(\mu)\preceq I$ satisfies
$$\operatorname{Var}_\mu f\le K_P\int|\nabla f|^2\,d\mu$$
for every real locally Lipschitz function on its affine support with finite Dirichlet energy. Such functions belong to $L^2(\mu)$. Gradients are intrinsic to the affine support; a point mass has Poincaré constant zero.
:::

The extension to a proper affine support is made within that support. For nonsmooth laws, the approximation statement must transfer the inequality to finite-energy locally Lipschitz functions as well as smooth tests; square integrability is part of the conclusion. The Cheeger consequence then uses the normalization already fixed in the introduction, with the factor $\pi$ coming from its reverse comparison.

:::{prf:corollary} Cheeger bound from the explicit Poincaré estimate
:label: cor:bk-cheeger
For every isotropic log-concave probability measure of positive dimension, with Euclidean distances and perimeter intrinsic to its affine support,
$$h(\mu)^{-1}\le\sqrt{\pi(1+2\cdot10^{16})}.$$
Here $h$ has the normalization of [](#eq:hstar-def) and the comparison of [](#eq:cheeger-two-sided).
:::

The BK proof therefore shares the Appell quantities and Letwin's quadratic input with the polynomial literature, while its new mechanism is the combination of a rank-independent Hodge estimate, a common bound for every integration power, and reverse transfer. It uses neither the BKL cumulant-and-suspension conclusion nor the SZ v2 summable-refinement conclusion as an input. This construction gives another proof of KLS; it does not establish the moment-Hessian, fixed-eigenfunction occupation or conditional-frame hypotheses. Their separate questions remain those of Chapter [](#sec:frontier-atlas).
