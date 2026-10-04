---
title: 'Solution: balanced posterior survival and exterior boundary'
ledger-node: lem:survival-implies-kls
numbering:
  enumerator: '126.%s'
---

**Overview.** This standalone proof of [](#lem:survival-implies-kls) uses the
actual lower outer Minkowski content of a fixed measurable set. Neighborhood
increments and conditional expectation transfer that content back from a
finite-time posterior. A curvature-preserving approximation proves the
required Gaussian comparison on arbitrary convex supports. Finally, concavity
of the original law's isoperimetric profile converts balanced cuts to Cheeger
isoperimetry. No Riccati or occupation estimate enters.

**Conventions.** For an actual set $E\subset\mathbb R^n$, put
$E^r=\{x:\operatorname{dist}(x,E)<r\}$ for $r>0$, with
$\operatorname{dist}(x,\varnothing)=+\infty$, and set

$$
\nu^+(E)=\liminf_{r\downarrow0}\frac{\nu(E^r)-\nu(E)}r.
$$

Sets may be measurable in the completion of $\nu$. Their neighborhoods are
open, regardless of the measurability of the set itself. We retain the actual
set when taking neighborhoods: changing a null subset can change this content.
All posterior measures below are equivalent to the original measure, so their
completions coincide. Integrals of a completed-measurable indicator are defined
using a Borel representative; neighborhoods still belong to the actual set.

:::{prf:theorem} Balanced posterior survival
:label: thm:sol-survival-standalone
Let $\mu$ be isotropic log-concave and $E$ measurable. If, for some $T_0,c_0,b_0>0$,

$$
\mathbb P\bigl(\min(p_{T_0},q_{T_0})\ge b_0\bigr)\ge c_0,
$$

then $\mu^+(E)\ge c\,c_0b_0\sqrt{T_0}$. Consequently, if $T_0,c_0,b_0$ are universal and the event holds for every balanced cut of every isotropic log-concave measure, KLS follows.

Here $T_0$ is finite, $p_t=\mu_t(E)$, $q_t=1-p_t$, and $\mu_t$ is the usual
stochastic-localization posterior. One can take $c=\sqrt{2/\pi}$.
:::

We first provide the two analytic ingredients, including their generality.

:::{prf:lemma} Neighborhood expectation inequality
:label: lem:sol-survival-neighborhood
For every deterministic completed-measurable $E$ and every finite deterministic
$t>0$, the usual localization posterior satisfies
$\mathbb E\mu_t^+(E)\le\mu^+(E)$, with extended nonnegative values allowed.
:::

:::{prf:proof}
The posterior has the conditional-law realization obtained by sampling
$X\sim\mu$, taking independent standard Brownian motion $B$, and observing
$Y_s=sX+B_s$. With $\mathcal F_t=\sigma(Y_s:0\le s\le t)$, Bayes' formula gives

$$
\mu_t(dx)=\mathbb P(X\in dx\mid\mathcal F_t)
=\frac{e^{Y_t\cdot x-t|x|^2/2}}{\int e^{Y_t\cdot z-t|z|^2/2}\mu(dz)}\mu(dx).
$$

Indeed, the conditional density of $Y_t$ given $X=x$ is Gaussian with mean
$tx$ and covariance $tI$. Moreover the observation bridge
$Y_s-(s/t)Y_t=B_s-(s/t)B_t$, $s\le t$, is independent of $(X,Y_t)$, so the
whole observation history has the same posterior as $Y_t$. The denominator
is positive and finite for every finite $Y_t$ and $t>0$, by completing the
square. This is the usual localization law: if $a_s=\mathbb E(X\mid\mathcal
F_s)$, then $W_t=Y_t-\int_0^t a_s\,ds$ is a continuous $\mathcal F_t$
martingale with quadratic covariation $tI$, hence Brownian motion, and
$dY_t=dW_t+a_t\,dt$. The martingale assertion follows by conditioning
$X-a_s$ against the past and using the independent Brownian increments;
integrability holds since $\mathbb E|X|<\infty$. These are precisely the
coefficient and posterior formula of stochastic localization.

In particular, for each fixed completed-measurable $A$, $\mu_t(A)$ is a
bounded conditional-expectation martingale and
$\mathbb E\mu_t(A)=\mu(A)$. A Borel representative gives this assertion
also for completed-measurable $A$, since all finite-time likelihoods are
strictly positive and finite.

For each $r>0$ apply this identity to $A=E^r\setminus E$. The random variable

$$
G_t(r)=\frac{\mu_t(E^r\setminus E)}r\ge0
\quad\hbox{satisfies}\quad
\mathbb E G_t(r)=\frac{\mu(E^r\setminus E)}r=G_0(r).
$$

The full lower limit defining $\mu_t^+(E)$ is measurable: it equals the lower
limit over positive rational radii. To see this, the numerator $H(r)$ is
nondecreasing and is left continuous, because
$E^r=\bigcup_{s<r}E^s$. Thus $H(q)/q\to H(r)/r$ as rational $q\uparrow r$.
Taking infima over radii in each interval $(0,\delta)$ therefore gives the
same infimum over its rational radii. A countable sequence of such infima
computes the lower limit.

If $\mu^+(E)=+\infty$, the proposed inequality is automatic. Otherwise choose
a deterministic sequence $r_j\downarrow0$ realizing the initial lower limit.
Nonnegativity, the pointwise lower-limit inequality, and Fatou give

$$
\mathbb E\mu_t^+(E)
\le\mathbb E\liminf_jG_t(r_j)
\le\liminf_j\mathbb E G_t(r_j)=\mu^+(E).
$$

No boundary integral, finite-perimeter hypothesis, or exchange of an
uncountable infimum with expectation is used.
:::

:::{prf:lemma} Gaussian comparison on convex supports
:label: lem:sol-survival-convex-support
Suppose $\kappa>0$ and
$\nu(dx)=Z^{-1}e^{-\kappa|x|^2/2-W(x)}dx$ is a full-dimensional probability,
where $W$ is a proper lower semicontinuous convex function with values in
$\mathbb R\cup\{+\infty\}$. For every completed-measurable set $E$,

$$
\nu^+(E)\ge\sqrt\kappa\,J(\nu(E))
\ge\sqrt{2/\pi}\sqrt\kappa\min(\nu(E),1-\nu(E)),
$$

where $J=\varphi\circ\Phi^{-1}$ is the standard Gaussian profile, extended
by zero at both endpoints. No smoothness of $W$ or its convex domain is required.
:::

:::{prf:proof}
The smooth input is the functional inequality

$$
\sqrt\kappa\left[J\!\left(\int f\,d\rho\right)
-\int J(f)\,d\rho\right]\le\int|\nabla f|\,d\rho,
\qquad 0\le f\le1.
\tag{*}
$$

For a smooth potential $U$ with $\nabla^2U\succeq\kappa I$ and probability
$d\rho\propto e^{-U}dx$, this is
[Bakry–Ledoux, *Inventiones Mathematicae* 123 (1996), Corollary 2.2,
equation (2.10), p. 267](https://www.math.univ-toulouse.fr/~ledoux/LevyGromov.pdf).
Their (2.11), p. 268, uses lower outer Minkowski content. We use (*) and
give the extension ourselves.

Choose an affine minorant $\ell(x)=a\cdot x+b\le W(x)$; such a minorant
exists for a proper lower semicontinuous convex function. Define

$$
W_j(x)=\inf_y\{W(y)+\tfrac j2|x-y|^2\},\qquad j\ge1.
$$

These functions are finite and convex, are continuously differentiable with
$j$-Lipschitz gradient, and increase pointwise to $W$. For completeness, the
minimizer exists uniquely by the affine lower bound and the strictly convex
quadratic term. Its optimality condition, together with monotonicity of the
convex subgradient, shows that $x\mapsto x-y_j(x)$ is 1-Lipschitz; differentiating
the minimum gives $\nabla W_j=j(x-y_j(x))$. For convergence, monotonicity in
$j$ is immediate. If $W_j(x)$ stays bounded along $j\to\infty$, the affine
lower bound forces $y_j(x)\to x$, and lower semicontinuity yields
$W(x)\le\liminf_j W(y_j(x))\le\liminf_j W_j(x)$. If $W(x)$ is finite the
reverse bound follows by testing $y=x$; if it is infinite the same argument
excludes a finite limit.

Convolve $W_j$ with a nonnegative smooth even compactly supported probability
mollifier of sufficiently small radius to obtain $\widetilde W_j$ with

$$
\sup_{|x|\le j}|\widetilde W_j(x)-W_j(x)|\le j^{-1}.
$$

Such a radius exists by uniform continuity on compact sets.
Convexity and the $j$-Lipschitz gradient persist under convolution, so
$0\preceq\nabla^2\widetilde W_j\preceq jI$. Also

$$
W_j(x)\ge a\cdot x+b-\frac{|a|^2}{2j},\qquad
\widetilde W_j(x)\ge a\cdot x+b-\frac{|a|^2}{2j}.
$$

The second bound uses the zero mean of the mollifier. Consequently the
unnormalized densities $e^{-\kappa|x|^2/2-\widetilde W_j(x)}$ converge
pointwise to $e^{-\kappa|x|^2/2-W(x)}$ and are dominated by the integrable
function $e^{-\kappa|x|^2/2-a\cdot x-b+|a|^2/2}$. Their normalizations
converge to $Z>0$ and the probability densities converge in $L^1$.

For each approximating law $\nu_j$, the potential
$U_j=\kappa|x|^2/2+\widetilde W_j$ has Hessian between $\kappa I$ and
$(\kappa+j)I$. The generator $\Delta-\nabla U_j\cdot\nabla$ has globally
Lipschitz drift, a nonexplosive diffusion, invariant probability $\nu_j$,
and curvature at least $\kappa$. Thus the stated smooth theorem applies.
It extends from smooth tests to every bounded Lipschitz $f:\mathbb R^n\to[0,1]$:
first multiply $f$ by smooth cutoffs equal to one on the radius-$R$ ball and
zero off the radius-$2R$ ball, with gradient bounded by $C/R$, then mollify.
Mollification preserves the range and has gradients converging almost
everywhere to the gradient of the Lipschitz cutoff function, with a common
bound. Absolute continuity and dominated convergence pass the mollification
limit in (*); then $R\to\infty$ passes the cutoff limit, since the extra
gradient term has integral at most $C/R$. This also explains explicitly the
test-function domain used from the smooth theorem.

Now fix a bounded Lipschitz $f$. The quantities $f,J(f),|\nabla f|$ are bounded
measurable functions (with any representative of the almost everywhere
gradient). The $L^1$ density convergence passes (*) from $\nu_j$ to $\nu$.
This is a functional limit, and does not claim continuity of set perimeters
under total variation.

For an actual measurable $E$, if $\nu(\overline E)>\nu(E)$, then
$\nu^+(E)=+\infty$, by continuity from above of $\nu(E^r)$ as $r\downarrow0$.
Otherwise set
$f_r(x)=(1-\operatorname{dist}(x,E)/r)_+$. Empty sets are immediate.
These are bounded Lipschitz functions, converge to $1_{\overline E}$, and
satisfy

$$
\int|\nabla f_r|\,d\nu
\le\frac{\nu(E^r\setminus E)}r.
$$

Indeed a Lipschitz function has zero gradient almost everywhere on each of
its level sets, so the gradient vanishes on $\{f_r=0\}$ and $\{f_r=1\}$;
elsewhere it is bounded by $1/r$. Absolute continuity transfers this
Lebesgue-almost-everywhere assertion to $\nu$. Dominated convergence gives
$\nu f_r\to\nu(E)$ and $\nu J(f_r)\to0$. Apply (*) and take the lower limit
over $r\downarrow0$ to obtain $\nu^+(E)\ge\sqrt\kappa J(\nu(E))$.
Finally symmetry and concavity of $J$, with $J(0)=0$ and
$J(1/2)=1/\sqrt{2\pi}$, give the claimed linear lower bound.
:::

:::{prf:proof} Proof of the survival theorem
Isotropy makes the log-concave measure full dimensional. Its density can be
written $e^{-V}$ with $V$ proper lower semicontinuous convex, after modification
on a Lebesgue null set if needed. This convention allows $V=+\infty$ off its
convex domain. At the original time $T_0$, each posterior has potential

$$
V(x)-Y_{T_0}\cdot x+\tfrac{T_0}2|x|^2
$$

up to an additive constant. Apply the convex-support lemma directly to this
posterior with $W=V-Y_{T_0}\cdot x$ and $\kappa=T_0$. No stochastic experiment
or event is approximated. Together with the neighborhood lemma this gives

$$
\mu^+(E)\ge\mathbb E\mu_{T_0}^+(E)
\ge\sqrt{2/\pi}\sqrt{T_0}\,
\mathbb E\min(p_{T_0},q_{T_0})
\ge\sqrt{2/\pi}\,c_0b_0\sqrt{T_0}.
$$

For the uniform consequence put $L=\sqrt{2/\pi}\,c_0b_0\sqrt{T_0}$ and
define $I_\mu(p)=\inf_{\mu(E)=p}\mu^+(E)$. The infimum may be over Borel or
completed-measurable sets: every completed-measurable $E$ contains a Borel
subset of equal mass, whose neighborhoods are smaller, so these two infima
agree. The balanced hypothesis implies $I_\mu(1/2)\ge L$ directly, without
attainment of the infimum.

For any absolutely continuous log-concave law, $I_\mu$ is concave on $(0,1)$
by [Milman (2009), Corollary 6.12, with Theorem 1.8 and its Section 6
extension](https://arxiv.org/pdf/0712.4092). It is therefore continuous there,
and Corollary 6.5 of the same source gives symmetry. That paper's definition
is the lower outer Minkowski convention used here. These results include
nonsmooth densities and convex supports in every dimension, including one.
For $0<\varepsilon<p<1/2$, concavity and nonnegativity give

$$
I_\mu(p)\ge
\frac{p-\varepsilon}{1/2-\varepsilon}I_\mu(1/2)
+\frac{1/2-p}{1/2-\varepsilon}I_\mu(\varepsilon)
\ge\frac{p-\varepsilon}{1/2-\varepsilon}L.
$$

Letting $\varepsilon\downarrow0$ and using symmetry proves
$I_\mu(p)\ge2L\min(p,1-p)$. Thus $h_\mu\ge2L$ for every isotropic
log-concave law, the universal Cheeger formulation of KLS. Endpoint values
may be assigned zero by the empty and full sets; no continuity at either
endpoint is asserted or used.
:::

**Hypotheses and scope.** The individual perimeter implication needs only a
full-dimensional log-concave probability with finite first moment, a fixed
deterministic measurable set, a positive finite deterministic time, and the
displayed survival premise. Isotropy selects the KLS class. An impossible
premise (for instance $b_0>1/2$ or $c_0>1$) makes the implication vacuous.
The proof establishes no uniform survival premise. The only imported analytic
results are the smooth Bakry–Ledoux functional comparison and Milman's
general-density profile theorem, identified above; no inaccessible book
passage is required.

**Fences respected.** The node has no `bounded_by`, `depends_on`, or `assumes`
edges. The survival condition is an explicit antecedent of the theorem, not
an additional proved node. The argument claims neither a moving-family
profile supermartingale nor a solution of any occupation or covariance gate.
