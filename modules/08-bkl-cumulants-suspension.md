---
numbering:
  enumerator: "8.%s"
---

(sec:bkl-proof)=
# Cumulants, suspension and the BKL proof

**What to retain.** The cumulants of an isotropic log-concave law — the
Taylor coefficients of the logarithm of its Laplace transform — satisfy
$\abs{\kappa_m^\mu(u,\cdot,\dots,\cdot)}^2\le K^{m-1}((m-1)!)^2\abs u^2$ with
$K$ independent of the dimension: up to a geometric factor, the factorial
growth already forced by the exponential law on the line. Suspension then encodes an arbitrary test
function as an extra coordinate of a larger log-concave law, so the bound
on linear observables becomes the exponential Appell coefficient bound for
every function, which by the spectral criterion of the first version of
Song–Zhang is KLS.

Bizeul, Klartag and Lehec (BKL) give a proof of KLS in their preprint of
4 October 2026 [@BizeulKlartagLehec2026KLS, version 1]. This chapter explains
its mechanism: the analytic criterion, the cumulant induction and suspension.
Each statement displays its status; how it was checked is explained on the
[welcome page](#sec:overview-checking).

The decisive change is to estimate cumulants of every order and then encode
an arbitrary test function in an additional coordinate of a log-concave
measure. Uniformity in dimension allows this enlarged measure to use the
same cumulant bound. The resulting estimate is exactly the exponential
Appell coefficient bound of [](#prop:sz-exponential-coefficients-equivalence).

The second version of Song–Zhang, deposited the same day and presented in
the next chapter, [](#sec:sz-v2-proof), closes the argument differently,
through repeated refinement from the same spectral foundation. The two proofs
are compared, and what each reconstruction uses is listed, in Chapter
[](#sec:kls-synthesis).

## A one-dimensional calibration

For a standard Gaussian, the logarithm of the Laplace transform is $z^2/2$:
the second cumulant is one and every higher cumulant vanishes. For the centered
mean-one exponential $X=E-1$, it is
$-z-\log(1-z)=\sum_{m\ge2}z^m/m$, so the $m$th cumulant is $(m-1)!$.
Factorial growth is therefore already necessary on the line. In higher
dimension the issue is to bound the full tensor with one argument fixed,
summing the squares of all remaining entries without a dimension factor.

A tilted average is the expectation of a test function after reweighting the
law by $e^{\langle z,x\rangle}$. Its first derivative at zero is
$\operatorname{Cov}(X,f)$; its higher derivatives retain the response to all
small exponential tilts. We use the following conventions.


:::{prf:definition} Tilt averages, cumulants and regular measures
:label: def:bkl-tilt-cumulants
For a log-concave probability measure $\mu$ on $\mathbb R^n$, set, in a
neighbourhood of the origin,
$$
\Lambda_\mu(z)=\log\int e^{\langle z,x\rangle}\,d\mu(x),\qquad
\kappa_m^\mu=\nabla^m\Lambda_\mu(0),\qquad
F_f^\mu(z)=\frac{\int f(x)e^{\langle z,x\rangle}\,d\mu(x)}
{\int e^{\langle z,x\rangle}\,d\mu(x)},\qquad
\mathcal T_d^\mu f=\frac{\nabla^dF_f^\mu(0)}{d!}
$$
for $f\in L^2(\mu)$. Tensor norms and inner products are the Hilbert--Schmidt
ones with all ordered indices summed. The positive semidefinite matrix $R_m^\mu$
is determined by
$$
\langle R_m^\mu u,u\rangle=|\kappa_m^\mu(u,\cdot,\ldots,\cdot)|^2.
$$
In this chapter, a BKL-regular measure has density $e^{-V}$ on $\mathbb R^n$,
where $V\in C^\infty$, every derivative of $V$ has at most polynomial growth,
and $aI\preceq\nabla^2V\preceq bI$ for some $0<a\le b<\infty$ depending on
the measure. Write $\mathcal A$ for the smooth functions all of whose derivatives
have at most polynomial growth, $\mathcal A_0=\{g\in\mathcal A:\int g\,d\mu=0\}$,
$L=\Delta-\langle\nabla V,\nabla\rangle$, and
$\nabla_0g=\nabla g-\int\nabla g\,d\mu$.
:::

## From tilt averages to a spectral gap

The analytic part works first with smooth measures whose curvature is bounded
above and below. The lower bound supplies a spectral gap at each fixed measure;
it is not assumed uniform across measures. Approximation is used only after
a bound independent of that curvature has been obtained.

:::{prf:lemma} Analytic foundations for the tilt criterion
:label: lem:bkl-analytic-foundations
For every BKL-regular measure, $L$ maps $\mathcal A$ into $\mathcal A$ and
$$
\int (Lu)v\,d\mu=-\int\langle\nabla u,\nabla v\rangle\,d\mu,
\qquad
\int(Lu)^2\,d\mu=\int|\nabla^2u|^2\,d\mu+
\int\langle\nabla^2V\nabla u,\nabla u\rangle\,d\mu
$$
for $u,v\in\mathcal A$. Its spectral gap $\lambda=C_P(\mu)^{-1}>0$ is
attained by a function $f\in\mathcal A_0$ with $\|f\|_2=1$ and $Lf=-\lambda f$.
For every $g\in\mathcal A_0$ there is a unique $u\in\mathcal A_0$ solving
$-Lu=g$, and
$$
\|u\|_2\le\lambda^{-1}\|g\|_2,\qquad
\|\nabla u\|_2^2=\langle g,u\rangle_{L^2}\le\lambda^{-1}\|g\|_2^2,
\qquad \|\nabla_0u\|_2\le\lambda^{-1/2}\|g\|_2.
$$
These assertions hold componentwise for finite-dimensional tensor-valued functions.
Every isotropic log-concave probability measure is the weak limit of isotropic
BKL-regular measures, with convergence of every polynomial moment. A common
Poincaré bound for these approximants passes to the limit.
:::

The integration identities permit repeated inversion of the diffusion operator
and centered differentiation of a first eigenfunction. The next estimate
recovers a tensor from partial symmetrization. Its exponential cost is
absorbed in the finite dyadic estimates used by the spectral argument.

:::{prf:lemma} Two-block tensor symmetrization
:label: lem:bkl-tensor-symmetrization
For integers $n,d\ge1$, let $T$ be a tensor on $\mathbb R^n$ of order at least
$3d$, symmetric in its first $d$ slots and separately in its next $2d$ slots.
If $\mathcal S_{2d}$ symmetrizes the first $2d$ slots, then
$$
|T|\le\binom{2d}{d}|\mathcal S_{2d}T|\le4^d|\mathcal S_{2d}T|.
$$
:::

This is the Song–Zhang component of the BKL argument. One coefficient bound
at all orders replaces successive curvature profiles with increasing constants.

:::{prf:theorem} The tilt-average criterion
:label: thm:bkl-tilt-criterion
There exists a universal $C>0$ such that the following holds. Let $\mu$ be a
centered BKL-regular measure with $\operatorname{Cov}(\mu)\preceq I$, and let
$R\ge1$. If
$$
|\mathcal T_d^\mu f|\le R^d\|f\|_{L^2(\mu)}
\qquad\text{for every }d\ge1\text{ and }f\in L^2(\mu),
$$
then $C_P(\mu)\le CR^2$.
:::

The mechanism follows a first eigenfunction through centered gradients and
inverse operators. A small spectral gap makes the resulting tensors large;
the means removed by centering are expressed through tilted averages.
Partial symmetrization compares these tensors with symmetric Taylor tensors.
A single exponential bound controls the centering terms at every order.
Summing the resulting estimates over finitely many dyadic orders up to an
exit index forces a lower spectral gap. The analytic and
tensor estimates above are separate inputs to this comparison.

The relation to the preceding chapter is exact, including the factorial:
both constructions differentiate the same normalized exponential.

:::{prf:proposition} Duality between tilt derivatives and Appell coefficients
:label: prop:bkl-tilt-appell-duality
For every full-dimensional log-concave probability measure $\mu$, integer
$d\ge1$, symmetric order-$d$ tensor $T$ and $f\in L^2(\mu)$, the Appell
conventions of [](#thm:sz-polynomial-variance) give
$$
\langle T,\nabla^dF_f^\mu(0)\rangle=\int f P_d^\mu[T]\,d\mu.
$$
Consequently, with $K_d(\mu)=\sup_{T\text{ symmetric},\,|T|=1}
\operatorname{Var}_\mu(P_d^\mu[T])$ and $c_d(\mu)=\sqrt{K_d(\mu)}/d!$,
$$
\|\mathcal T_d^\mu\|_{L^2(\mu)\to\mathrm{HS}}=c_d(\mu).
$$
:::

The Appell generating function is
$e^{\langle z,x\rangle-\Lambda_\mu(z)}$. Differentiating its integral
against $f$ gives the pairing. Positive-degree Appell polynomials have mean
zero, so their $L^2$ norms equal the square roots of their variances.
Taking the two Hilbert-space operator norms gives the coefficient identity.
It identifies the common end point; it does not improve the older bound.

## The cumulant induction

The stochastic part rescales its noise by the inverse square root of the
current covariance. The deterministic covariance decay is then exponential.
Higher cumulants are measured in the inverse covariance metric, keeping each
index at its current variance scale.

:::{prf:lemma} Inverse-covariance localization and cumulant dynamics
:label: lem:bkl-cumulant-dynamics
Let $\mu$ be compactly supported, isotropic and log-concave on $\mathbb R^n$.
There exists a global stochastic localization
$$
d\mu_t(x)=\frac{e^{\langle c_t,x\rangle-\langle Q_tx,x\rangle/2}\,d\mu(x)}
{\int e^{\langle c_t,y\rangle-\langle Q_ty,y\rangle/2}\,d\mu(y)},\qquad
dc_t=A_t^{-1}a_t\,dt+A_t^{-1/2}\,dB_t,\qquad dQ_t=A_t^{-1}\,dt,
$$
with $c_0=0$, $Q_0=0$, $a_t=\int x\,d\mu_t$, and
$A_t=\operatorname{Cov}(\mu_t)$ positive definite at every finite time.
Put $\kappa_m(t)=\kappa_m^{\mu_t}$ and
$H_i(t)=\kappa_3(t)(\cdot,\cdot,A_t^{-1/2}e_i)$. Then
$$
dA_t=\sum_iH_i(t)\,dB_t^i-A_t\,dt,\qquad
\mathbb EA_t=e^{-t}I,\qquad
\sum_iH_i(t)A_t^{-1}H_i(t)\preceq8A_t.
$$
For $m\ge3$,
$$
d\kappa_m(t)=\kappa_{m+1}(t)(\cdot,\ldots,\cdot,A_t^{-1/2}dB_t)
-\bigl(m\kappa_m(t)+L_m(t)\bigr)dt,
$$
where, for $h_J=(h_j)_{j\in J}$,
$$
L_m(t)(h_1,\ldots,h_m)=
\sum_{\substack{J\subset\{1,\ldots,m\},\,1\in J\\2\le |J|\le m-2}}
\left\langle\kappa_{|J|+1}(t)(h_J,\cdot),
A_t^{-1}\kappa_{m-|J|+1}(t)(h_{J^c},\cdot)\right\rangle.
$$
For tensors of order $q$ define $\langle S,T\rangle_t=
\langle S,(A_t^{-1})^{\otimes q}T\rangle$ and $|T|_t^2=\langle T,T\rangle_t$.
For fixed $u$, write $\mathcal E_m(t)=|\kappa_m(t)(u,\cdot,\ldots,\cdot)|_t^2$.
Then $\mathcal E_2(t)=\langle A_tu,u\rangle$ and
$\int_0^\infty\mathbb E\mathcal E_2(t)\,dt=|u|^2$.
Moreover $\mathcal E_3(t)\le8\langle A_tu,u\rangle$. For fixed $n,m$,
the processes $\mathcal E_m(t)$ and $|L_m(t)(u)|_t^2$ have deterministic
bounds depending on $n,m,u$ and the initial support radius. The Itô local
martingale part of each $\mathcal E_m$ is a square-integrable martingale on
every bounded time interval.
:::

Differentiating the logarithmic Laplace transform along this localization
produces a next-order cumulant in the noise and products of lower-order
cumulants in the drift. The third-moment estimate controls covariance noise
in its own metric. Positive definiteness at finite times and integrability
after stopping justify use of that metric. These are mathematical inputs,
not a convention for interpreting a singular inverse.

:::{prf:lemma} Differential and integrated cumulant energy estimates
:label: lem:bkl-cumulant-energy
For the process and quantities of [](#lem:bkl-cumulant-dynamics), a universal
$C>0$ satisfies, for every $m\ge3$ and fixed $u$,
$$
\operatorname{drift}\mathcal E_m(t)\ge\tfrac12\mathcal E_{m+1}(t)
-Cm^2\mathcal E_m(t)-2\langle\kappa_m(t)(u),L_m(t)(u)\rangle_t.
$$
If $I_m=\int_0^\infty\mathbb E\mathcal E_m(t)\,dt<\infty$ and
$J_m=\int_0^\infty\mathbb E|L_m(t)(u)|_t^2\,dt<\infty$, then
$$
\mathcal E_m(0)+\tfrac12\int_0^\infty\mathbb E\mathcal E_{m+1}(t)\,dt
\le Cm^2I_m+2\sqrt{I_mJ_m}.
$$
:::

The energy computation retains the variation of the inverse covariance and
its cross variation with the cumulant. Noise supplies a positive next-order
energy. The moving metric costs a quadratic factor in the order, and the
remaining term is a product of lower-order cumulants. To integrate, finite
total energy supplies terminal times at which the expected boundary term
tends to zero. The induction must supply the stated integrability hypotheses.

:::{prf:theorem} Dimension-free cumulant bounds at every order
:label: thm:bkl-cumulant-bound
There exists a universal $K\ge1$ such that for every dimension $n\ge1$,
every isotropic log-concave probability measure $\mu$ on $\mathbb R^n$,
every integer $m\ge2$ and every $u\in\mathbb R^n$,
$$
|\kappa_m^\mu(u,\cdot,\ldots,\cdot)|^2
\le K^{m-1}((m-1)!)^2|u|^2.
$$
:::

The induction proves a static bound and an integrated next-order bound
together. In each product of cumulants, the factor containing the fixed
vector uses the integrated estimate; the other uses the static estimate
for the whitened law. The number of index splittings is a binomial
coefficient, canceled exactly by the two factorials. A polynomial cost
in the order remains and is absorbed by one large exponential base $K$.
Conditioning on expanding balls and convergence of moments remove compact
support. No KLS estimate enters this induction.

## Suspension: putting a function into a coordinate

For an isotropic BKL-regular law, take a smooth test $f$ with bounded Hessian,
unit $L^2$ norm and orthogonal to affine functions. Let $X_1,\ldots,X_N$ be
independent copies from this law and put
$F_N=N^{-1/2}\sum_i f(X_i)$. Adjoin
$S=(F_N+\eta_\beta)/\sqrt{1+2/\beta^2}$, with an independent centered
Laplace variable $\eta_\beta$ of rate $\beta$. The joint law is isotropic.
For large $N$ it is log-concave: the Hessian cost of each copy of $f$ is
reduced by $N^{-1/2}$ and absorbed by the original positive curvature.
The dimension has increased, which is precisely why the cumulant estimate
must hold in every dimension with the same constant.

:::{prf:proposition} Suspension converts cumulants into tilt bounds
:label: prop:bkl-suspension
Fix an integer $d\ge2$ and $b>0$. Assume that $R_{d+1}^\nu\preceq bI$
for every isotropic log-concave probability measure $\nu$, in every dimension.
Then every isotropic BKL-regular measure $\mu$ satisfies
$$
|\mathcal T_d^\mu f|^2\le\frac{2b}{(d!)^2}\|f\|_{L^2(\mu)}^2
\qquad\text{for every }f\in L^2(\mu).
$$
:::

A cumulant with one slot in the new coordinate and the others in one copy
of $X$ equals the tilt derivative divided by $\sqrt{N(1+2/\beta^2)}$.
The $N$ disjoint tensor blocks cancel the factor $N^{-1}$ in their squared
norms. Increasing $\beta$ removes the added variance. Decomposing a test
into constant, linear and affine-orthogonal parts, then using density,
extends the estimate to $L^2$. The suspension needs only its cumulant premise.

Substitution of the all-order bound gives one exponential base. Approximation
passes the Appell polynomial moment inequalities to arbitrary laws; linear
contraction includes singular covariances.

:::{prf:theorem} Uniform exponential tilt coefficients
:label: thm:bkl-tilt-bound
Let $K\ge1$ be any universal constant satisfying [](#thm:bkl-cumulant-bound).
For every dimension, every centered log-concave probability measure $\mu$ with
$\operatorname{Cov}(\mu)\preceq I$, every integer $d\ge1$ and every
$f\in L^2(\mu)$,
$$
|\mathcal T_d^\mu f|\le(2K)^{d/2}\|f\|_{L^2(\mu)}.
$$
Measures supported on a proper affine subspace are included, with derivatives
defined by their ambient Laplace transform.
:::

Combining [](#thm:bkl-tilt-bound) with [](#thm:bkl-tilt-criterion) gives the
KLS conclusion [](#conj:kls), first for regular measures and then
by scalar Poincaré stability. This is the BKL argument.

## Consequences for the earlier questions

The exponential estimate also supplies the initialization bound used in the
first-version iteration of Chapter [](#sec:polynomial-curvature), without a
curvature-profile premise. Since that bound is already of KLS strength, feeding
it back into the iteration gives no second proof.

:::{prf:corollary} Uniform conditional initialization from BKL
:label: cor:bkl-uniform-conditional-initialization
There exists a universal $G\ge1$ such that for every integer $r\ge2$, every
$\Gamma\ge G$, every dimension, every centered log-concave probability measure
$\mu$ with $\operatorname{Cov}(\mu)\preceq I$, and every integer $d\ge1$,
$$
c_d(\mu)\le\frac{((1+r^{-2})\Gamma)^d\ell_r(d)^d}{(d+1)^2},
\qquad \ell_0(x)=x,\quad\ell_{r+1}(x)=\log(e+\ell_r(x)).
$$
Here the Appell coefficients use ambient tensors also for measures on a proper
affine subspace. One may take $G=\max\{1,4\sqrt{2K}\}$ for $K$ as in
[](#thm:bkl-tilt-bound). No curvature-profile assumption is needed.
:::

Indeed $(d+1)^2\le4^d$ and $\ell_r(d)\ge1$, so enlarging the exponential
base absorbs the denominator uniformly in degree and depth. This does not
estimate the accumulated centering losses of a different spectral comparison.
What KLS does not give for the alternative mechanisms is in Section
[](#subsec:atlas-assessment).
