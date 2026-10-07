---
title: 'BKL: the tilt criterion and Appell duality'
ledger-node:
  - thm:bkl-tilt-criterion
  - prop:bkl-tilt-appell-duality
numbering:
  enumerator: '131.%s'
---

*Part of the Bizeul–Klartag–Lehec proof, Chapter [](#sec:bkl-proof); the reading order is on the [full proofs](#sec:proofs-bkl) page.*

**Overview.** This reconstructs the criterion in Section 3 of
[@BizeulKlartagLehec2026KLS], version
[arXiv:2610.05474v1](https://arxiv.org/html/2610.05474v1).
A sequence of normalized inverse-gradient tensors spends the
Dirichlet energy of a first eigenfunction. Its failure of symmetry
is paid by the Bochner defects. Taylor coefficients transfer along
the sequence; a finite dyadic sum then bounds the total energy loss.
The final section proves the exact duality with the existing Appell
coefficients, including its factorial and tensor-norm conventions.

**Dependencies.** The criterion uses [](#def:bkl-tilt-cumulants),
[](#lem:bkl-analytic-foundations), and
[](#lem:bkl-tensor-symmetrization).
The Appell comparison uses the polynomial convention in
[](#thm:sz-polynomial-variance), but does not use its quantitative
bound. We do not invoke [](#prop:sz-exponential-coefficients-equivalence)
to prove the criterion, nor assume KLS or the cumulant estimate.
The exponential Taylor bound is the stated premise of the criterion,
not a conclusion of this dossier.

% Author identity: plan_import (researcher), unknown, 2026-10-06.
% This dossier is an uncertified reconstruction, not its own review.

## Criterion and analytic conventions

:::{prf:theorem} Poincaré inequality from the full Taylor hierarchy
:label: thm:sol-bkl-tilt-criterion
There is a universal $C<\infty$ with the following property.
Let $\mu=e^{-V}dx$ be centered and regular in the sense of
[](#def:bkl-tilt-cumulants), with $\operatorname{Cov}(\mu)\preceq I$.
For $f\in L^2(\mu)$ put

$$
F_f(z)=\frac{\int f(x)e^{z\cdot x}\,d\mu(x)}
{\int e^{z\cdot x}\,d\mu(x)},\qquad
\mathcal T_df=\frac{\nabla^dF_f(0)}{d!}.
$$

Suppose $R\ge1$ and
$|\mathcal T_df|\le R^d\|f\|_2$ for every integer $d\ge1$
and every $f\in L^2(\mu)$. Then $C_P(\mu)\le CR^2$.
This proves [](#thm:bkl-tilt-criterion).
:::

We prove this statement below, after deriving the estimates used in
the finite summation. All quantities in that proof belong to this one
fixed measure. Write $L=\Delta-\nabla V\cdot\nabla$,
$\lambda=C_P(\mu)^{-1}>0$,
and $\nabla_0u=\nabla u-\int\nabla u\,d\mu$.
The space $\mathcal A$ and its centered subspace are those of
[](#lem:bkl-analytic-foundations).
Derivatives add a new first tensor index; Taylor indices precede
the indices of the input. Full tensor norms sum all ordered indices.
The scalar Taylor premise extends to every tensor-valued $u$
componentwise:

$$
|\mathcal T_du|^2
=\sum_J|\mathcal T_du_J|^2
\le R^{2d}\sum_J\|u_J\|_2^2
=R^{2d}\|u\|_2^2.
\tag{T1}
$$

Strong convexity gives Gaussian tails. Cauchy--Schwarz therefore
permits every derivative under the integral defining $F_f$, locally
uniformly in $z\in\mathbb R^n$, even for arbitrary $f\in L^2(\mu)$.
For instance its differentiated integrands are bounded by
$|f(x)|\,|x|^k e^{M|x|}$ on $|z|\le M$, which is integrable by
Cauchy--Schwarz and Gaussian decay.

## The inverse-gradient sequence and its energy

Choose a real $f\in\mathcal A_0$ with
$\|f\|_2=1$ and $-Lf=\lambda f$, as furnished by
[](#lem:bkl-analytic-foundations).
Put $h_1=f$ and $w_i=\nabla_0h_i$.
If $w_i=0$, set $h_{i+1}=0$ and $\alpha_{i+1}=0$.
Otherwise set

$$
u_{i+1}=(-L)^{-1}w_i,\qquad
\alpha_{i+1}=\frac{\|w_i\|_2}{\|\nabla u_{i+1}\|_2},
\qquad h_{i+1}=\alpha_{i+1}u_{i+1}.
\tag{T2}
$$

All components are centered and in $\mathcal A$.
The denominator is positive when $w_i\ne0$: a zero gradient would
make centered $u_{i+1}$ zero, contradicting $-Lu_{i+1}=w_i$.
The inverse bound gives $\alpha_{i+1}^2\ge\lambda$ whenever it
is positive.
The identity $-Lh_{i+1}=\alpha_{i+1}w_i$ holds also in the zero case.
In particular

$$
v_i:=\|\nabla h_i\|_2^2,\qquad
v_{i+1}=\|w_i\|_2^2,\qquad
p_i:=v_i-v_{i+1}=\left|\int\nabla h_i\,d\mu\right|^2\ge0,
\tag{T3}
$$

and $v_1=\lambda$.
Define the nonnegative defect

$$
\chi_i=\|\nabla^2h_i-\alpha_{i+1}\nabla h_{i+1}\|_2^2.
\tag{T4}
$$

Integration by parts gives

$$
\langle\nabla^2h_i,\nabla h_{i+1}\rangle_{L^2}
=\langle w_i,-Lh_{i+1}\rangle_{L^2}
=\alpha_{i+1}v_{i+1}.
$$

Expanding (T4) now shows

$$
\|D^2h_i\|_2^2=\alpha_{i+1}^2v_{i+1}+\chi_i
=\|Lh_{i+1}\|_2^2+\chi_i.
$$

If $aI\preceq D^2V$, Bochner's identity therefore implies

$$
\|Lh_i\|_2^2\ge
\|Lh_{i+1}\|_2^2+\chi_i+a v_i.
\tag{T5}
$$

Sum through any finite index. Because $\|Lh_1\|_2^2=\lambda^2$,
this proves

$$
\sum_{i\ge1}\chi_i\le\lambda^2,\qquad
a\sum_{i\ge1}v_i\le\lambda^2,\qquad v_i\longrightarrow0.
\tag{T6}
$$

Let $N\ge1$ be the first index such that $v_{N+1}<\lambda/2$.
It exists by (T6). For $2\le j\le N$ we have $v_j\ge\lambda/2$,
so $\alpha_j>0$ and

$$
\lambda\le\alpha_j^2
=\frac{\|Lh_j\|_2^2}{v_j}\le2\lambda.
\tag{T7}
$$

The upper bound follows by telescoping (T5).
The two budgets required below are

$$
\sum_{i=1}^N p_i=\lambda-v_{N+1}>\frac{\lambda}{2},
\qquad
\sum_{i=1}^N\chi_i\le\lambda^2.
\tag{T8}
$$

## Symmetry defects

Let $\tau_\ell$ exchange slots $\ell$ and $\ell+1$, and let
$\mathcal S_q$ average permutations of the first $q$ slots.
These are isometries and orthogonal projections, respectively,
on the full tensor space.

If $\alpha_{i+1}>0$, the tensor
$\nabla_0(\nabla h_i)/\alpha_{i+1}$ is symmetric in its first two
slots. Centering (T4) and using $\alpha_{i+1}^2\ge\lambda$ gives

$$
\left\|w_{i+1}-
\frac{\nabla_0(\nabla h_i)}{\alpha_{i+1}}\right\|_2^2
\le\frac{\chi_i}{\lambda}.
$$

If $\alpha_{i+1}=0$ then $w_{i+1}=0$, so the same distance
assertion holds with the zero tensor. It follows in every case that

$$
\|w_j-\tau_1w_j\|_2^2\le\frac{4\chi_{j-1}}{\lambda}
\quad(j\ge2).
\tag{T9}
$$

For $\ell\ge2$, a permutation of slots $\ell,\ell+1$ in
$w_j=\alpha_j\nabla_0(-L)^{-1}w_{j-1}$ acts on slots
$\ell-1,\ell$ of its input. Therefore

$$
w_j-\tau_\ell w_j
=\alpha_j\nabla_0(-L)^{-1}
(w_{j-1}-\tau_{\ell-1}w_{j-1}).
$$

The input is centered componentwise. By the analytic inverse bound
and (T7), this operator has norm at most $\sqrt2$ whenever
$2\le j\le N$. Consequently, for $2\le q\le i\le N$
and $1\le\ell<q$, iteration down to (T9) gives

$$
\|w_i-\tau_\ell w_i\|_2^2
\le\frac{2^{\ell+1}}{\lambda}\chi_{i-\ell}.
\tag{T10}
$$

A permutation of $q$ objects is a product of at most $q^2$
adjacent exchanges. Telescoping along such a product and applying
Cauchy--Schwarz bounds its squared displacement of $w_i$ by
$q^4\sum_{\ell=1}^{q-1}\|w_i-\tau_\ell w_i\|_2^2$.
Average this inequality over permutations and use convexity of the
squared norm. Since $\ell+1\le q$ and $q^4\le16^q$,
we obtain the explicit bound

$$
\|w_i-\mathcal S_qw_i\|_2^2
\le\frac{32^q}{\lambda}
\sum_{j=i-q+1}^{i-1}\chi_j
\qquad(2\le q\le i\le N).
\tag{T11}
$$

Thus the defects in (T5) pay for all the permutations needed below.

## Moving Taylor coefficients along the sequence

For a scalar or tensor-valued $u\in\mathcal A$, integrate by parts
against the tilted density. Its potential is $V-z\cdot x$ and its
generator is $L_z=L+z\cdot\nabla$. Polynomial growth and Gaussian
tails justify the integration, giving

$$
F_{-Lu}(z)=z\cdot F_{\nabla u}(z).
$$

Differentiate at zero. Exactly one derivative hits the explicit
factor $z$; the other $d$ derivatives hit $F_{\nabla u}$.
The factorial normalization therefore gives

$$
\mathcal T_1(-Lu)=\int\nabla u\,d\mu,\qquad
\mathcal T_{d+1}(-Lu)
=\mathcal S_{d+1}\mathcal T_d(\nabla u)\quad(d\ge1).
\tag{T12}
$$

In the second identity the symmetrization acts on the $d$ Taylor
slots and the newly added gradient slot, leaving pre-existing
tensor slots unchanged. Constants have zero Taylor tensors of
positive order. Apply (T12) to $h_{i+1}$ and use (T2):

$$
\mathcal S_{d+1}\mathcal T_dw_{i+1}
=\alpha_{i+1}\mathcal T_{d+1}w_i.
\tag{T13}
$$

We now derive a uniform doubling estimate. If $2d\le i\le N$ and
$T=\mathcal T_dw_i$, repeated use of (T13) yields

$$
\mathcal S_{d+k}T
=\left(\prod_{j=i-k+1}^{i}\alpha_j\right)
\mathcal T_{d+k}w_{i-k}\quad(1\le k\le d).
\tag{T14}
$$

This follows inductively because
$\mathcal S_{r+1}\mathcal S_r=\mathcal S_{r+1}$: averaging over
the larger permutation group absorbs averaging over its subgroup.
All indices of the product satisfy $2\le j\le N$.
Taking $k=d$ and using (T7) gives

$$
|\mathcal S_{2d}T|^2
\le(2\lambda)^d|\mathcal T_{2d}w_{i-d}|^2.
\tag{T15}
$$

Set $\widetilde T=\mathcal T_d(\mathcal S_{2d}w_i)$.
This tensor has at least $3d$ slots; its first $d$ are symmetric
Taylor slots and its next $2d$ are symmetric input slots.
By (T1) and (T11),

$$
\delta^2:=|T-\widetilde T|^2
\le\frac{32^{2d}R^{2d}}{\lambda}
\sum_{j=i-2d+1}^{i-1}\chi_j.
\tag{T16}
$$

Apply [](#lem:bkl-tensor-symmetrization) to $\widetilde T$.
Since $\mathcal S_{2d}$ is a contraction, the triangle inequality gives

$$
|T|\le\delta+4^d|\mathcal S_{2d}\widetilde T|
\le4^d|\mathcal S_{2d}T|+(1+4^d)\delta.
$$

After squaring and using (T15)--(T16), this implies

$$
|\mathcal T_dw_i|^2
\le(C_0\lambda)^d|\mathcal T_{2d}w_{i-d}|^2
+\frac{C_0^dR^{2d}}{\lambda}
\sum_{j=i-2d+1}^{i-1}\chi_j,
\qquad C_0=2^{17}.
\tag{T17}
$$

Indeed the first coefficient is at most $2\cdot32^d\le64^d$,
and the second coefficient is at most
$2(1+4^d)^2\,32^{2d}\le8\cdot16384^d\le(2^{17})^d$.
This gives one universal constant valid for every degree; it is
not optimized.

## The finite dyadic argument

:::{prf:proof} Proof of the tilt criterion
First express the lost gradient means using Taylor tensors.
Testing $-Lf=\lambda f$ against the coordinate functions gives
$\int\nabla f\,d\mu=\lambda\int xf\,d\mu$.
Since $\mu$ is centered and $\operatorname{Cov}(\mu)\preceq I$,
duality and Cauchy--Schwarz give $|\int xf\,d\mu|\le1$.
Thus $p_1\le\lambda^2$.
For $2\le i\le N$, (T12), (T2), and (T7) give

$$
p_i=|\mathcal T_1(-Lh_i)|^2
=\alpha_i^2|\mathcal T_1w_{i-1}|^2
\le2\lambda|\mathcal T_1w_{i-1}|^2.
$$

Define, for every positive integer $d$,

$$
S_d=\sum_{i=1}^{N-d}|\mathcal T_dw_i|^2,
$$

with an empty sum equal to zero. In particular $S_d=0$ for $d\ge N$.
The preceding bounds imply

$$
\sum_{i=1}^Np_i\le\lambda^2+2\lambda S_1.
\tag{T18}
$$

For each term of $S_d$, (T1) and (T3) give
$|\mathcal T_dw_i|^2\le R^{2d}v_{i+1}\le\lambda R^{2d}$.
There are at most $2d-1$ terms with $i<2d$.
For the others, sum (T17) over $2d\le i\le N-d$.
Its higher-order terms are a sub-sum of $S_{2d}$, since
$d\le i-d\le N-2d$. Every $\chi_j$ occurs in at most $2d$
of the intervals $[i-2d+1,i-1]$. Thus (T8) gives

$$
\begin{aligned}
S_d
&\le(2d-1)\lambda R^{2d}
 +(C_0\lambda)^dS_{2d}
 +\frac{2dC_0^dR^{2d}}{\lambda}\sum_{j=1}^N\chi_j\\
&\le(C_0\lambda)^dS_{2d}
 +4dC_0^d\lambda R^{2d}.
\end{aligned}
\tag{T19}
$$

This remains true when any of the sums is empty.
Suppose, for a contradiction, that
$\lambda R^2\le(100C_0^2)^{-1}$.
Multiplication of (T19) by $(C_0\lambda)^{d-1}$ gives

$$
(C_0\lambda)^{d-1}S_d
\le(C_0\lambda)^{2d-1}S_{2d}
+4dC_0^{2d-1}(\lambda R^2)^d
\le(C_0\lambda)^{2d-1}S_{2d}+\frac{4d}{100^d}.
$$

Choose $m\ge1$ with $2^m\ge N$ and sum over
$d=1,2,\ldots,2^{m-1}$ restricted to powers of two.
The left and right weighted sums telescope, and $S_{2^m}=0$.
Consequently

$$
S_1\le4\sum_{k=0}^{m-1}\frac{2^k}{100^{2^k}}
\le4\sum_{d=1}^{\infty}\frac d{100^d}
=\frac{400}{9801}<\frac1{20}.
$$

The equality is the derivative of the geometric series at $1/100$.
Our supposition also implies $\lambda\le1/100$, because $R,C_0\ge1$.
By (T18),

$$
\sum_{i=1}^Np_i
<\lambda\left(\frac1{100}+\frac1{10}\right)
<\frac{\lambda}{2},
$$

contradicting (T8). We conclude
$C_P(\mu)=\lambda^{-1}\le100C_0^2R^2$, proving the theorem
with a universal constant. The summation is finite at each fixed
measure; there is no exchange of a spectral limit with an
approximation limit.
:::

## Exact comparison with Appell coefficients

:::{prf:theorem} Tilt--Appell duality with ordered-index norms
:label: thm:sol-bkl-tilt-appell-duality
Let $\mu$ be a full-dimensional log-concave probability on
$\mathbb R^n$, let $d\ge1$, and use the Appell convention of
[](#thm:sz-polynomial-variance). For every symmetric $d$-tensor $T$
and $f\in L^2(\mu)$,

$$
\langle T,\nabla^dF_f(0)\rangle
=\int fP_d^\mu[T]\,d\mu.
\tag{T20}
$$

If
$K_d(\mu)=\sup_{T=T^{\rm sym},\,|T|=1}
\operatorname{Var}_\mu P_d^\mu[T]$, then

$$
\|\mathcal T_d:L^2(\mu)\longrightarrow
\operatorname{Sym}^d(\mathbb R^n)\|
=\frac{\sqrt{K_d(\mu)}}{d!}=c_d(\mu).
\tag{T21}
$$

This proves [](#prop:bkl-tilt-appell-duality).
:::

:::{prf:proof}
A finite-dimensional full-dimensional log-concave probability has
an exponential moment $\int e^{\eta|x|}\,d\mu<\infty$ for some
$\eta>0$. Recall the elementary reason: an integrable log-concave
density has a bounded convex superlevel set with nonempty interior;
concavity of its logarithm along rays from an interior point bounds
that logarithm above by a negative linear function outside a
sufficiently large ball. Radial integration then gives an exponential
moment after decreasing its exponent.
In particular all polynomial moments are finite.
For $|z|<\eta/4$, differentiation under the integral defining
$F_f$ is valid to every fixed order:
Cauchy--Schwarz reduces it to finiteness of integrals of
$|x|^{2k}e^{2|z||x|}$, and these are dominated locally by
a constant times $e^{\eta|x|}$.
The denominator is positive for real $z$ near zero.

The normalized exponential has formal expansion

$$
\frac{e^{z\cdot x}}{\int e^{z\cdot y}\,d\mu(y)}
=\sum_{k\ge0}\frac{\langle\mathcal A_k^\mu(x),
z^{\otimes k}\rangle}{k!},\qquad
P_k^\mu[T]=\langle T,\mathcal A_k^\mu\rangle.
$$

Its derivative tensor of order $d$ at zero is exactly
$\mathcal A_d^\mu(x)$, with no additional symmetrization factor.
The preceding integrable domination permits differentiating its
integral against $f$, proving (T20).
The integral of the normalized exponential against $\mu$ is the
constant one; taking derivatives shows
$\int P_d^\mu[T]\,d\mu=0$ for $d\ge1$.
Thus its squared $L^2$ norm is its variance.

Consider the linear operator
$B_d:\operatorname{Sym}^d(\mathbb R^n)\to L^2(\mu)$,
$B_dT=P_d^\mu[T]/d!$.
Its finite-dimensional domain makes it bounded, and its norm is
$\sqrt{K_d(\mu)}/d!$ by the definition of $K_d$.
Equation (T20) says that its Hilbert-space adjoint is
$B_d^*f=\mathcal T_df$. An operator and its adjoint have equal
norms, proving (T21). In particular this is the norm on the full
symmetric tensor space, not a supremum restricted to tensors
$u^{\otimes d}$.
:::

**Source concordance.** Equations (T2)--(T8) reconstruct the normalized
sequence, Bochner decay and exit index in BKL Section 3.
(T9)--(T11) give its Lemmas 3.2--3.3; (T12)--(T17) give
Lemmas 3.6--3.8; (T18)--(T19) and the finite summation give
Lemma 3.9 and Theorem 3.1. The duality identifies the result with
the Appell convention already used in this repository.

**Scope and fences.** The premise must hold simultaneously for all
degrees and all $L^2$ tests for the fixed measure. Different
constants at different degrees do not meet it.
The coefficient condition in
[](#prop:sz-exponential-coefficients-equivalence) is not assumed
as an unconditional theorem.
The tensor operations respect [](#rem:projection-ceiling).
No covariance occupation, sharp CMH bound or posterior-profile
estimate is inferred, so [](#rem:relative-ceiling),
[](#rem:crude-insufficient), and [](#rem:profile-circularity)
are unaffected. No additional bounded-by edge is proposed.
