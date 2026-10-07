---
numbering:
  enumerator: "7.%s"
---

(sec:polynomial-curvature)=
# Song–Zhang, first version: polynomial estimates and curvature

**What to retain.** Bounds on the Appell polynomials of a measure control its spectral gap, through a first eigenfunction followed by repeated centered gradients; stochastic localization turns a spectral gap back into better polynomial bounds. Composing the two conversions gives $\CP\lesssim16^{\log^*(n+2)}$, and its end point, one exponential base for the coefficients of every degree, is equivalent to KLS ([](#prop:sz-exponential-coefficients-equivalence)).

This chapter works through the first version of Song and Zhang's preprint [@SongZhang2026IteratedLogKLS] (SZ v1), whose polynomial–curvature iteration gives the dimension-dependent bound [](#thm:song-zhang-kls), and locates its losses. Its spectral criterion is the starting point of two of the three proofs: Bizeul–Klartag–Lehec (BKL) prove its exponential end point directly (Chapter [](#sec:bkl-proof)), and the second version of Song–Zhang (SZ v2) makes the losses of the iteration summable (Chapter [](#sec:sz-v2-proof)) [@SongZhang2026ConstantKLS]. Balasubramanian–Kasiviswanathan (BK) share its Appell normalization but reach the spectral gap through their own integration calculus (Chapter [](#sec:bk-proof)). The estimates and limitations below are those of SZ v1.

**Why the iteration stalls.** Each round of the loop multiplies the profile constant by about $4$, and is admissible only above thresholds that grow with its depth; so the constants of the curvature profiles grow like $4^r$ at depth $r$ (Section [](#sec:sz-profile-iteration)). The depth needed grows, very slowly, with the dimension, and so does the bound.

**Where this argument meets the alternative mechanisms.** It shares the first eigenfunction with the fixed eigenfunction and Letwin's quadratic estimate with the moment map; Section [](#subsec:atlas-assessment) says, mechanism by mechanism, what the proofs built on it give and what still needs an estimate of its own.

(sec:sz-notation)=
## Notation and the smallest cases

A probability measure $\nu(dx)=e^{-W(x)}dx$ on $\R^n$ is called *regular* here if $W$ is smooth and $aI\preceq D^2W\preceq bI$ for some $0<a\le b<\infty$; the lower bound $a$ is its *curvature*. The Bakry–Émery bound gives $\CP(\nu)\le1/a$, and every isotropic log-concave measure is a weak limit of regular isotropic ones ([](#lem:sz-analytic-foundations)). The question of this chapter is how much better than $1/a$ one can do when $a$ is small. A *curvature profile* is an answer valid in every dimension: a function $F$ with $\CP(\nu)\le F(a)$ for every regular isotropic $\nu$ of curvature $a$.

For a centered real random variable of variance $\sigma^2$, the first three Appell polynomials are $1$, $x$, and $x^2-\sigma^2$. Their means vanish in positive degree, and differentiation lowers degree: $(x^2-\sigma^2)'=2x$. In several dimensions the quadratic one is $x^TTx-\operatorname{Tr}(T\Sigma)$, where $T$ is symmetric and $\Sigma$ is the covariance. In every degree $d$, the Appell tensor $\mathcal A_d^\nu$ is the coefficient of $z^{\otimes d}/d!$ in the expansion of $e^{\langle z,x\rangle}/\int e^{\langle z,y\rangle}d\nu(y)$ (see [](#thm:sz-polynomial-variance)), and $P_d^\nu[T]=\langle T,\mathcal A_d^\nu\rangle$ for a symmetric $d$-tensor $T$. These polynomials keep the centering and differentiation identities in every degree; they need not be orthogonal in $L^2(\nu)$. The size of degree $k$ is measured by

$$
K_k(\nu)=\sup_{\substack{T\text{ symmetric}\\\|T\|_{\mathrm{HS}}=1}}\Var_\nu(P_k^\nu[T]),
\qquad
c_k(\nu)=\frac{\sqrt{K_k(\nu)}}{k!}.
$$

In isotropic position $P_1^\nu[T]=\langle T,x\rangle$, so $K_1=1$ and $c_1=1$. For the standard Gaussian the Appell polynomials are the Hermite polynomials, $K_k=k!$, and $c_k=1/\sqrt{k!}$.

Degree two already separates measures. For a standard Gaussian $G$, $\Var(G^2-1)=3-1=2$, so $c_2=\sqrt2/2$. For $X=E-1$ with $E$ a mean-one exponential, $\E X^4=9$, hence $\Var(X^2-1)=8$ and $c_2=\sqrt2$, twice the Gaussian value. Here $\E[X(X^2-1)]=\E X^3=2$: even the first two positive degrees are not orthogonal, so the orthogonality of Hermite polynomials is not available in general, and nothing below uses it.

(sec:sz-loop)=
## The argument in one loop

The chapter follows the loop of Figure [](#fig:sz-loop). The first estimate, [](#thm:sz-polynomial-variance), bounds every coefficient, with factorial growth in the degree. The comparison [](#thm:sz-curvature-comparison) turns coefficient bounds into a spectral gap for a regular measure of curvature $a$; fed the factorial bound, it gives a first curvature profile of order $\log(e+1/a)^2$, already far below the Bakry–Émery $1/a$. Applied to the measures produced by stochastic localization, that profile improves the coefficients, and the comparison then gives the next profile, one logarithm deeper: this is [](#thm:sz-iterated-curvature). Finally [](#thm:sz-curvature-transfer) evaluates a profile at curvature of order $1/\log(en)$ to reach every isotropic log-concave measure, which gives [](#thm:song-zhang-kls).

::::{figure}
:label: fig:sz-loop

```{mermaid}
flowchart TB
  coef["Appell coefficient bounds: c_k ≤ 32^k k!"] --> comp["Curvature comparison: coefficients give C_P at curvature a"]
  comp --> prof["Curvature profile at depth r: C_P ≤ Γ_r² ℓ_r(1/a)²"]
  prof --> loc["Localization: the profile improves the coefficients"]
  loc -->|"next depth r+1"| comp
  prof --> tr["Gaussian transfer at curvature c / log(en)"]
  tr --> res["C_P ≲ 16^r ℓ_r(log en)², depth r ≈ log*(n+2)"]:::res
  classDef res fill:#f2f2f2
```

The loop of Song–Zhang's argument. Coefficient bounds ([](#thm:sz-polynomial-variance)) feed the curvature comparison ([](#thm:sz-curvature-comparison)), which gives a curvature profile; localization improves the coefficients and the comparison is applied again, one logarithm deeper ([](#thm:sz-iterated-curvature)). The transfer ([](#thm:sz-curvature-transfer)) then gives the general bound [](#thm:song-zhang-kls).
::::

(sec:sz-polynomial-estimates)=
## Controlling polynomial coefficients

:::{prf:theorem} Dimension-free Appell coefficient bounds
:label: thm:sz-polynomial-variance
Let $\mu$ be a centered log-concave probability measure on $\mathbb R^n$
with $\operatorname{Cov}(\mu)\preceq I$. Define its symmetric Appell tensors
$\mathcal A_d^\mu$ by the formal generating identity

$$
\frac{e^{\langle z,x\rangle}}{\int e^{\langle z,y\rangle}d\mu(y)}
=\sum_{d\ge0}\frac{\langle\mathcal A_d^\mu(x),z^{\otimes d}\rangle}{d!}.
$$

For every integer $d\ge1$ and symmetric $d$-tensor $T$, put
$P_d^\mu[T]=\langle T,\mathcal A_d^\mu\rangle$, with Hilbert–Schmidt norms
summing over all ordered indices. Then

$$
\operatorname{Var}_\mu(P_d^\mu[T])
\le1024^d(d!)^4\|T\|_{\mathrm{HS}}^2.
$$

Consequently every polynomial $q$ of degree at most $s$ satisfies

$$
\sqrt{\operatorname{Var}_\mu(q)}
\le\sum_{k=1}^s32^k k!\left\|\int D^kq\,d\mu\right\|_{\mathrm{HS}}.
$$
The constants do not depend on the dimension or the measure.
:::

The proof starts with Letwin's quadratic estimate [](#thm:letwin-qcts), which controls the whitened third moments driving covariance noise. Localization with covariance-dependent noise then follows all derivative means of a degree-$d$ polynomial, weighted by the matching tensor powers of the covariance. The lower derivative means of an Appell polynomial start at zero. The drift inequalities couple degree $j$ only to higher derivatives, allowing induction on $d$; retaining the covariance–mean cross variation is essential. After a time of order $d^{-2}$, the accumulated Gaussian curvature bounds the remaining variance. Conditioning on growing balls and convergence of finitely many moments remove compact support. The Appell expansion then gives the estimate for a general polynomial by the triangle inequality.

In the notation above, this first estimate gives $c_k\le32^k k!$. The dimension has disappeared, but the factorial remains: fed into the comparison below, it gives only a bound depending on the curvature, of order $\log(e+1/a)^2$.

(sec:sz-analytic-setting)=
## The analytic setting

The passage to the spectral gap uses inverse powers of the diffusion operator. The next lemma supplies their domains, a first eigenfunction, and the approximation needed to return to general measures: the analytic prerequisites for applying the polynomial estimate to a function selected by the measure.

:::{prf:lemma} Analytic foundations for polynomial–curvature comparison
:label: lem:sz-analytic-foundations
Let $\mu(dx)=e^{-W(x)}dx$ be a probability measure on $\mathbb R^n$ with
$W\in C^\infty$ and $aI\preceq D^2W\preceq bI$ for some
$0<a\le b<\infty$. Let $H$ be the nonnegative self-adjoint operator associated
with the closure of $\int|\nabla g|^2d\mu$ on $C_c^\infty$.
Its form domain is the weighted Sobolev space $H^1(\mu)$, its kernel consists
of constants, and $C_c^\infty$ is a graph core. Every $g\in\operatorname{Dom}H$
has second weak derivatives in $L^2(\mu)$ and satisfies

$$
\|Hg\|_2^2=\int\|D^2g\|_{\mathrm{HS}}^2d\mu
+\int\langle\nabla g,D^2W\nabla g\rangle d\mu.
$$

The operator has compact resolvent; its first positive eigenvalue is
$\lambda=\CP(\mu)^{-1}$. It has a real centered unit eigenfunction for
$\lambda$. On centered functions, if $h\in\operatorname{Dom}H^{1/2}$, then
$g=H^{-1/2}h\in\operatorname{Dom}H$ and
$\|Hg\|_2^2=\|H^{1/2}h\|_2^2$, $\|\nabla g\|_2^2=\|h\|_2^2$.

Every isotropic log-concave probability measure is a weak limit of isotropic
measures of this regular class. If probability measures $\mu_j$ converge
weakly to an absolutely continuous probability measure $\mu$ and satisfy
$\operatorname{Var}_{\mu_j}(q)\le K\int|\nabla q|^2d\mu_j$ for every
$q\in C_c^\infty$ with a common finite $K$, then every real locally Lipschitz
$q$ of finite $\mu$-Dirichlet energy belongs to $L^2(\mu)$ and satisfies
the same inequality for $\mu$.
:::

The proof uses cutoffs and local elliptic regularity to extend the Bochner identity from compact smooth functions to the operator domain. Conjugation by $e^{-W/2}$ gives a Schrödinger operator with a confining quadratic lower bound, so its resolvent is compact. Spectral calculus then defines the inverse square root on centered functions. For approximation, Gaussian convolution gives a smooth convex potential with bounded Hessian; a small quadratic tilt supplies positive curvature, and whitening restores isotropy. Only scalar Poincaré inequalities pass through the final weak limit. The eigenfunction and its inverse-operator iterates are used at a fixed regular measure.

(sec:sz-curvature-comparison)=
## From coefficients to every test function

:::{prf:theorem} Polynomial coefficients control curvature dependence
:label: thm:sz-curvature-comparison
Let $0<\epsilon\le1$, let $\ell:\mathbb N\to[1,\infty)$ be nondecreasing,
and let $R\ge2^{40}\epsilon^{-2}$. Let $\nu(dx)=e^{-W(x)}dx$ be a centered
probability measure on $\mathbb R^n$ with $W\in C^\infty$,
$aI\preceq D^2W\preceq bI$ for some $0<a\le b<\infty$, and
$\operatorname{Cov}(\nu)\preceq I$. Using the Appell tensors of
[](#thm:sz-polynomial-variance), define

$$
K_k(\nu)=\sup_{\substack{T\text{ symmetric}\\\|T\|_{\mathrm{HS}}=1}}
\operatorname{Var}_\nu(P_k^\nu[T]),\qquad
c_k(\nu)=\frac{\sqrt{K_k(\nu)}}{k!}.
$$

If $c_k(\nu)\le R^k\ell(k)^k/(k+1)^2$ for every integer $k\ge1$, then
every dyadic integer $d\ge2$ satisfies

$$
\CP(\nu)\le16(1+\epsilon)R^2\ell(d)^2
\max\{1,a^{-1/(d+1)}\}.
$$
:::

The proof follows a first eigenfunction of eigenvalue $\lambda=\CP(\nu)^{-1}$ through repeated application of a centered gradient and an inverse square root of the diffusion operator. Normalization preserves the size of each family, while centering removes a nonnegative amount of mass. Bochner's identity charges positive curvature against the energy of every surviving family. Polynomial tests estimate the mass lost to centering; the difficulty is that iterated derivative tensors are only approximately symmetric. A two-block tensor recovery inequality and a dyadic decomposition bound the defects, and a convolution estimate sums their overlapping contributions without a factor depending on the number of iterations. If $\lambda$ were too small, most mass would survive while curvature used up more energy than was initially available. The resulting contradiction gives the displayed comparison.

This is a direct argument with an extremal function. Its all-degree polynomial hypothesis controls the centering losses; no density argument with a degree-dependent Poincaré constant is involved. The threshold $R\ge2^{40}\epsilon^{-2}$ pays for the initial small degrees and the absorption of normalization errors.

(sec:sz-profile-iteration)=
## Feeding the curvature estimate back into the polynomials

:::{prf:theorem} Iterated curvature profiles
:label: thm:sz-iterated-curvature
Put $\ell_0(x)=x$ and $\ell_{r+1}(x)=\log(e+\ell_r(x))$ for $x\ge0$.
There are a universal constant $C_0>0$ and universal constants
$(\Gamma_r)_{r\ge1}$, with $\Gamma_r\le C_0 4^r$, such that the following
holds simultaneously in every dimension. If $\nu(dx)=e^{-W(x)}dx$ is a
centered probability measure, $W\in C^\infty$,
$aI\preceq D^2W\preceq bI$ for some $0<a\le b<\infty$, and
$\operatorname{Cov}(\nu)\preceq I$, then for every integer $r\ge1$,

$$
\CP(\nu)\le\Gamma_r^2\ell_r(a^{-1})^2.
$$
:::

Start with the factorial coefficient estimate and choose a dyadic degree comparable to $\log(e+a^{-1})$ in [](#thm:sz-curvature-comparison). This gives the first logarithmic curvature profile. To return from a profile to coefficients, apply it to localized measures after an affine change of variables. Their covariance and accumulated curvature enter together as a matrix weight; treating them as unrelated scalar bounds would lose the required control. The derivative hierarchy used in the first polynomial estimate then improves the coefficient growth. Keeping its zero initial values below the top degree makes the extra coefficient loss approach one at large depth. A further use of the comparison advances the logarithmic depth, and the constants can be chosen with

$$
\Gamma_{r+1}=4e^{3/r^2}\Gamma_r
$$

above one fixed initial depth. The summability of $r^{-2}$ gives one envelope $C_0 4^r$ valid for all finite depths.

**Why optimizing the multiplier alone does not give a bounded profile.** With $\epsilon=r^{-2}$ and $R=(1+r^{-2})\Gamma_r$, the comparison requires $R\ge2^{40}r^4$. Initializing the improved coefficient induction also requires $\Gamma_r\ge Kr^2$ for a universal $K$. Exponentially growing constants can meet both thresholds simultaneously; a bounded sequence cannot. Replacing the factor $4$ by a fixed number greater than one still gives an unbounded product, and replacing it by one does not remove these growing admissibility costs. Within this iteration, a bounded profile needs both a smaller multiplier and a replacement for these growing thresholds. These are obstructions to retaining the existing estimates, not lower bounds on every possible comparison argument.

The two thresholds pay different bills. The coefficient induction uses the factorial bound below degree $\lceil32r^2\rceil$; the nearly lossless hierarchy starts above that degree. The comparison must also absorb centering losses along the whole inverse-gradient sequence, including its initial terms. Improving only the final tensor estimate or only the high-degree tail leaves these earlier costs in place. A useful replacement would supply low-degree coefficient control conditional on the current curvature profile, together with a comparison whose multipliers have bounded cumulative product and whose admissibility is uniform in depth. The initialization bound now follows from BKL ([](#cor:bkl-uniform-conditional-initialization)), though not independently of KLS (Section [](#subsec:proofs-provenance)). SZ v2 avoids the question altogether: it iterates a common coefficient radius instead and pays the fixed spectral conversion only once (Section [](#subsec:proofs-compared-differences)).

(sec:sz-exponential-criterion)=
## The exact coefficient growth demanded by KLS

The coefficient hierarchy gives an exact reformulation of the dimension-free bound, now obtained by BKL. The two assertions below have the same strength; the second identifies the coefficient growth established by [](#thm:bkl-tilt-bound).

:::{prf:proposition} KLS and exponential Appell coefficient growth
:label: prop:sz-exponential-coefficients-equivalence
For the Appell polynomials of [](#thm:sz-polynomial-variance), set
$K_k(\nu)=\sup_{T\text{ symmetric},\,\|T\|_{\mathrm{HS}}=1}
\operatorname{Var}_\nu(P_k^\nu[T])$ and $c_k(\nu)=\sqrt{K_k(\nu)}/k!$.
The following are equivalent:

1. There is a universal $C<\infty$ such that $\CP(\mu)\le C$ for every
   isotropic log-concave probability measure in every dimension.
2. There is a universal $A<\infty$ such that $c_k(\nu)\le A^k$ for every
   integer $k\ge1$ and every isotropic probability measure
   $\nu(dx)=e^{-W(x)}dx$ in every dimension, where $W\in C^\infty$ and
   $0<a_\nu I\preceq D^2W\preceq b_\nu I<\infty$ for constants that may
   depend on $\nu$.

Quantitatively, condition 1 with $C\ge1$ implies
$c_k(\nu)\le C^{(k-1)/2}$. Condition 2 implies condition 1 with
$C=32\max\{4A,2^{40}\}^2$.
:::

For the forward direction, differentiation lowers an Appell polynomial by one degree. A Poincaré constant $C$ therefore gives $K_k\le Ck^2K_{k-1}$, starting from $K_1=1$ in isotropic position, and the factorials cancel in $c_k$. For the converse, exponential growth fits [](#thm:sz-curvature-comparison) with $\ell=1$, $\epsilon=1$, and $R=\max\{4A,2^{40}\}$. At one fixed regular measure, let the dyadic degree tend to infinity: its positive curvature $a$ stays fixed, so $a^{-1/(d+1)}$ tends to one. This gives a scalar bound uniform over all regular measures, which then passes to arbitrary isotropic log-concave measures by approximation.

The order of quantifiers is the substantive demand: one $A$ must work for every degree, dimension and regular measure, regardless of its curvature bounds. Neither the factorial estimate of [](#thm:sz-polynomial-variance) nor constants chosen afresh at each logarithmic depth meet it.

(sec:sz-profile-transfer)=
## The iterated-logarithm bound

A curvature profile valid in every dimension bounds the Poincaré constant of every isotropic log-concave measure: it suffices to evaluate it at curvature of order $1/\log(en)$.

:::{prf:theorem} Transfer of a curvature profile by Gaussian localization
:label: thm:sz-curvature-transfer
There are universal constants $c,C>0$ with the following property.
Let $F:(0,\infty)\to(0,\infty)$ be any function such that, in every
dimension, every isotropic probability measure $\nu(dx)=e^{-W(x)}dx$ with
$W\in C^\infty$ and $aI\preceq D^2W\preceq bI$ for some
$0<a\le b<\infty$ satisfies $\CP(\nu)\le F(a)$ for every such lower
curvature bound $a$. Then every isotropic log-concave probability measure
$\mu$ on $\mathbb R^n$ satisfies

$$
\CP(\mu)\le C F\!\left(\frac{c}{\log(en)}\right).
$$

No continuity or monotonicity of $F$ is required.
:::

This statement is where ordinary Gaussian stochastic localization enters. A bounded Lipschitz test detects the original Poincaré constant: after variance normalization, its supremum is universally bounded and its Lipschitz constant is of order $\CP(\mu)^{-1/2}$ [@KLnotes, Theorem 20]. Stop the posterior covariance at its first exit from $(I/2,2I)$. Letwin's quadratic estimate controls the exit probability on a time interval of order $1/\log(en)$, while the stopped variance decays by at most a fixed factor. The boundedness of the test pays for the exceptional paths, leaving one posterior with controlled covariance and substantial variance. Whitening that posterior gives curvature at least half the elapsed time, so evaluating $F$ at this deterministic bound controls the original Poincaré constant. No comparison of nearby values of $F$ is used. Regular approximation passes the same scalar bound to arbitrary measures with its argument unchanged. Any improved curvature profile can be substituted here.

Feeding the profiles of [](#thm:sz-iterated-curvature) into this transfer gives Song–Zhang's main theorem, stated in their first-version preprint (arXiv:2610.01447v1, 1 October 2026) as Theorem 7.1.

:::{prf:theorem} Song–Zhang iterated-logarithm bound
:label: thm:song-zhang-kls
Let $\ell_0(x)=x$ and $\ell_{r+1}(x)=\log(e+\ell_r(x))$ for $x\ge0$.
There are universal constants $C,C'>0$ such that every isotropic log-concave
probability measure $\mu$ on $\mathbb R^n$ satisfies, for every integer $r\ge1$,

$$
\CP(\mu)\le C16^r\ell_r(\log(en))^2,
\qquad
\PsiKLS_n\le C'4^r\ell_r(\log(en)).
$$

The constants are independent of both $r$ and $n$. In particular, after enlarging
them if necessary,

$$
\CP(\mu)\le C16^{\log^*(n+2)},
\qquad
\PsiKLS_n\le C'4^{\log^*(n+2)},
$$

where $\log^*x$ is the least number of successive natural logarithms needed to
bring $x$ to at most one. This is [@SongZhang2026IteratedLogKLS, Theorem 7.1].
:::

Insert the profile of [](#thm:sz-iterated-curvature) into [](#thm:sz-curvature-transfer), absorbing the universal rescaling of its argument into the outer constant, and pass to the Cheeger scale by [](#eq:cheeger-two-sided). Uniformity in the depth $r$ is essential, because the depth is chosen depending on $n$: near $\log^*(n+2)$, the iterated logarithm $\ell_r(\log(en))$ is universally bounded and only the factor $16^r$ remains. That factor is all the dimension dependence left in this particular iteration. SZ v2 removes it by refinements with summable costs (Chapter [](#sec:sz-v2-proof)).

:::{prf:corollary} Affine iterated-logarithm Poincaré bound
:label: cor:sz-affine-poincare
There is a universal constant $C>0$ such that every log-concave probability
measure $\mu$ on $\mathbb R^n$ with positive definite covariance $\Sigma$
satisfies, for every integer $r\ge1$,

$$
\CP(\mu)\le C16^r\ell_r(\log(en))^2\|\Sigma\|_{\mathrm{op}},
$$

where $\ell_r$ is defined in [](#thm:sz-iterated-curvature). Consequently

$$
\CP(\mu)\le C16^{\log^*(n+2)}\|\Sigma\|_{\mathrm{op}}
$$

after enlarging the universal constant.
:::

Whitening an arbitrary positive definite covariance contributes $\|\Sigma\|_{\mathrm{op}}$ to the gradient energy, which turns the isotropic bound into the affine form.
