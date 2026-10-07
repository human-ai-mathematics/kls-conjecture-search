---
title: 'Klartag–Lehec: stopped rank tails and integrated covariance'
ledger-node:
  - thm:kl-stopped-rank-tail
  - thm:kl-integrated-rank-covariance
numbering:
  enumerator: "105.%s"
---

*Part of the results of the literature written out here, Chapter [](#sec:covariance-tech); the reading order is on the [full proofs](#sec:proofs-literature) page.*

**Author:** researcher_kl_rank, gpt-6-astra, 2026-10-01.

**Overview.** This is an uncertified author dossier for
[](#thm:kl-stopped-rank-tail) and [](#thm:kl-integrated-rank-covariance).
It reconstructs the proof in Klartag–Lehec, *Thin-shell bounds via parallel
coupling*, [arXiv:2507.15495v2, HTML](https://arxiv.org/html/2507.15495v2)
and [pinned PDF](https://arxiv.org/pdf/2507.15495v2)
[@KlartagLehec2025ThinShell]. Both representations were read; the PDF identifies
v2 as submitted 23 February 2026 and has a title-page date of 24 February 2026.
The version, rather than the filename year or the title-page date, pins this import.
The source is distributed under CC BY 4.0; the reconstruction below is attributed
to its authors, with the additional justifications and replacement construction
identified explicitly. Availability and attribution do not certify the argument.

1. Construct the localization and its stopped covariance Itô formula, including
   repeated eigenvalues and the compact-support bounds needed for expectations.
2. Derive the tensor estimate from the established improved Lichnerowicz inequality,
   and use it to control a spectral potential at every stopped time.
3. Construct the potential explicitly, run the geometric-time iteration, and
   eliminate its terminal term without a dimension-uniform initial window.
4. Convert stopped counting into hitting-time inverse moments, then integrate each
   ordered rank and sum over ranks. No eigenvector tracking is involved.

## Exact target statements and conventions

The bodies of the following statements reproduce the two manuscript directives
in Chapter [](#sec:covariance-tech).

:::{prf:theorem} Stopped rank tails
:label: thm:sol-kl-rank-stopped
For the simplified stochastic localization of an isotropic compactly supported log-concave law, write $\lambda_1(t)\ge\cdots\ge\lambda_n(t)$ for the eigenvalues of $A_t$. There is a universal $C$ such that, for every stopping time $\sigma$ and $t>0$,

$$
\sum_{i=1}^n\Prob\bigl(\lambda_i(t\wedge\sigma)\ge3\bigr)
\le Cn\exp(-t^{-1/8}).
$$

Consequently, if $\sigma_k=\inf\{t:\lambda_k(t)\ge3\}$, then

$$
\Prob(\sigma_k\le t)\le C\frac nk\exp(-t^{-1/8}),
\qquad
\E\sigma_k^{-2}\le C\left(1+\log\frac nk\right)^{16}.
$$
:::

:::{prf:theorem} Integrated rank covariance
:label: thm:sol-kl-rank-integrated
Under the same hypotheses,

$$
\E\sum_{i=1}^n
\exp\left(2\int_0^1\lambda_i(t)\dd t\right)\le Cn .
$$
:::

Here $n\ge1$, $1\le k\le n$, and isotropic means mean zero and covariance
$I_n$. Stopping times take values in $[0,\infty]$ with respect to the Brownian
filtration (or its usual augmentation); $\inf\varnothing=\infty$ and
$\infty^{-2}=0$. The source specifies the natural Brownian filtration explicitly.
The manuscript's unqualified “stopping time” is read relative to this filtration,
not an anticipatively enlarged filtration. Constants are independent of
$n,\mu,\sigma,k,t$. A single final $C$ can be the maximum of the finitely many
constants obtained below. The second theorem has no stopping inside its integral.

## Source dependency map

Page numbers below are printed PDF pages, also the one-based PDF page numbers.

| Source location | Contribution | Treatment here |
|---|---|---|
| Section 2, (8)–(14), Lemma 2.1, pp. 6–7 | Tilt, barycenter, covariance, Brownian-driven ODE | Constructed below; only existence at initial point zero is needed |
| Section 4, (36), p. 16 | $A(t,\theta)\preceq t^{-1}I$ | Derived below from the established analytic input |
| Section 5, (57)–(59), pp. 23–24 | Initial exit probability vanishes faster than any power | Direct bounded-coefficient martingale proof below; no use of the quantitative (58) |
| Lemma 5.2, pp. 24–25, (60)–(62) | Restricted third tensor | Reproduced with the projection and nonsmooth-class justification |
| Lemma 5.3, pp. 25–26, (63)–(70) | Stopped spectral Itô formula | Reconstructed, including a.e. interpretation |
| Lemma 5.4, pp. 27–29, (71)–(74) | Spectral-potential growth | All index regions estimated below |
| Lemma 5.5, pp. 29–30, (75)–(78) | Positive increasing exponential/quadratic cutoff | Explicit replacement with universal coefficient $64$ instead of $12$ |
| Proposition 5.1, pp. 23, 30–32, (79)–(87) | Stopped rank tail | Iteration, terminal limit, and all-time extension below |
| Corollary 6.1, pp. 32–33, (88)–(91) | Rank hitting probability and inverse second moment | Layer-cake calculation below, including $k=n$ |
| Theorem 6.2, pp. 33–34 | Integrated rank bound | Pathwise split, then integrable rank sum below |

The one non-elementary geometric estimate taken as established is
[](#thm:improved-lichnerowicz), with reference [@Klartag2023Logarithmic]:
$C_P(\nu)\le\sqrt{\|\operatorname{Cov}\nu\|_{\mathrm{op}}/t}$ for a
$t$-strongly log-concave law. This node has no `depends_on`, `assumes`, or
`bounded_by` entries. Prékopa–Leindler (preservation of log-concavity by marginalization),
Itô's formula, and the elementary continuous-martingale exponential bound are
standard background used explicitly below. The source cites Guan for the growth
mechanism but supplies the needed argument in Lemmas 5.2–5.4; no unchecked theorem
of Guan is substituted for those steps here.

Corollary 4.10 is a **notation reference** in Theorem 6.2, not an input to its
proof. The parallel-coupling, Wasserstein, $H^{-1}$, and matrix-flow estimates of
Sections 2–4 beyond the tilt construction and covariance cap are not ancestors
of these two targets. Neither the thin-shell conclusion, the 2026 preprints, nor
an orientation estimate is used.

## Localization, regularity, and the analytic input

Put $\Lambda_t(\theta)=\log\int e^{\theta\cdot x-t|x|^2/2}\,d\mu(x)$,
$\mu_{t,\theta}(dx)=e^{\theta\cdot x-t|x|^2/2-\Lambda_t(\theta)}\mu(dx)$,
$a=\nabla\Lambda_t$, and $A=\nabla^2\Lambda_t$.
Compact support permits differentiation of every order under this integral.
If the support lies in a ball of radius $R$, all centered moments of order $m$
are at most $(2R)^m$ in absolute value, uniformly in $(t,\theta)$.
In particular $a$ is bounded and uniformly Lipschitz in $\theta$.
For every Brownian path the ODE for $\theta_t-B_t$ therefore has a unique global
solution to

$$
d\theta_t=dB_t+a(t,\theta_t)\,dt,\qquad \theta_0=0.
$$

Picard iteration shows that the solution is adapted. Set $\mu_t=\mu_{t,\theta_t}$,
$a_t=a(t,\theta_t)$, and $A_t=A(t,\theta_t)$. This is the simplified stochastic
localization used in the manuscript, with Brownian covariance $I_n\,dt$ and
quadratic tilt $t|x|^2/2$; there is no time rescaling. Equivalent positive tilts
preserve affine support, so isotropy implies $A_t\succ0$. Its ordered eigenvalues
are continuous and adapted, even at crossings, and $A_0=I_n$.

The identities
$\partial_t\Lambda_t=-\frac12(\operatorname{Tr}A+|a|^2)$ and Itô's formula give

$$
d\log(d\mu_t/d\mu)(x)=(x-a_t)\cdot dB_t-\tfrac12|x-a_t|^2dt,
\qquad d\mu_t(x)=(x-a_t)\cdot dB_t\,\mu_t(x).
$$

Consequently $da_t=A_t\,dB_t$, and applying the product rule to
$A_t=\int xx^T d\mu_t-a_ta_t^T$ gives

$$
dA_t=\sum_{\ell=1}^n H_{\ell,t}\,dB_t^\ell-A_t^2dt,
\qquad H_{\ell,t}=\int(x_\ell-a_{t,\ell})(x-a_t)(x-a_t)^T\,d\mu_t.
$$

These are source (65)–(66). All coefficients are bounded by constants depending
on the fixed compact law and dimension. This is enough for the martingales on
finite time intervals to be true martingales; it does not claim uniformity of
these intermediate support bounds.

The density of $\mu_t$ is $e^{-t|x|^2/2}$ times a log-concave function.
An orthogonal projection $Y$ onto a subspace $E$ has the same strong-convexity
parameter $t$: factor $e^{-t|y|^2/2}$ out of its marginal and apply
Prékopa–Leindler to the remaining log-concave integrand on $E\oplus E^\perp$.
Centering does not change this property.

To apply improved Lichnerowicz to a possibly nonsmooth compactly supported law
$\nu$ on $E$, convolve with $N(0,\varepsilon I_E)$. Completing the square in
$t|x|^2/2+|z-x|^2/(2\varepsilon)$ and applying Prékopa–Leindler shows that the
smooth positive convolution is $t/(1+t\varepsilon)$-strongly log-concave.
Its covariance is $\operatorname{Cov}(\nu)+\varepsilon I_E$. For every polynomial
of degree at most two, the Poincaré inequality for the convolution passes to
$\nu$ as $\varepsilon\downarrow0$, since moments through degree four converge
(use the coupling $Y+\sqrt\varepsilon G$). Polynomials in the smooth inequality
are justified by compact cutoffs and Gaussian tails; the compact support of
$Y$ gives all required moments. Thus, with
$u=\|\operatorname{Cov}\nu\|_{\mathrm{op}}$, the quadratic Poincaré constant
needed here is at most $\sqrt{u/t}$, without a boundary regularity assumption.
In particular a unit top-eigenvector linear test gives $u\le\sqrt{u/t}$,
hence $u\le t^{-1}$. Applied directly to $\mu_{t,\theta}$ this proves

$$
0\prec A(t,\theta)\preceq t^{-1}I_n\qquad(t>0),
$$

simultaneously in $\theta$. There is no exceptional-time issue in using this
bound along an entire path.

## The tensor estimate and stopped growth

:::{prf:lemma} Restricted tensor estimate (source Lemma 5.2)
:label: lem:sol-kl-rank-tensor
For a centered compactly supported $t$-strongly log-concave $X$, use an
orthonormal covariance eigenbasis, with eigenvalues $\lambda_i$ and coordinates
$X_i$. For $u>0$ and each $k$,

$$
\sum_{i,j:\,\lambda_i,\lambda_j\le u}(\mathbb E X_iX_jX_k)^2
\le4t^{-1/2}u^{3/2}\lambda_k.
$$
:::

:::{prf:proof}
Let $E$ be the span of the eigenvectors with eigenvalue at most $u$,
$Y=P_EX$, and $H=\mathbb E[X_kY\otimes Y]$ as a matrix on $E$.
If $E=\{0\}$ the assertion is zero. Otherwise the preceding projection and
approximation argument applies on $E$, with covariance norm at most $u$.
Write $S=\operatorname{Tr}H^2$. The quadratic Poincaré inequality yields

$$
\operatorname{Var}(Y^THY)
\le4\sqrt{u/t}\operatorname{Tr}(H^2\operatorname{Cov}Y)
\le4t^{-1/2}u^{3/2}S.
$$

Since $\mathbb EX_k=0$,
$S=\mathbb E[X_kY^THY]\le\sqrt{\lambda_k\operatorname{Var}(Y^THY)}$.
Squaring and dividing by $S$ when $S>0$ proves the result; $S=0$ is immediate.
No independence of $X_k$ and $Y$ is assumed.
:::

For an eigenbasis $(u_i)$ of $A_t$, let
$\xi_{ijk}=\mathbb E_{\mu_t}[(X-a_t)\cdot u_i\,(X-a_t)\cdot u_j\,(X-a_t)\cdot u_k]$
and $|\xi_{ij}|^2=\sum_k\xi_{ijk}^2$. The tensor is symmetric in all three
indices. These are instantaneous coordinates, not stochastic differentials of
an eigenbasis. The following formula is basis independent.
For $F(A)=\operatorname{Tr}f(A)$ with $f\in C^2([0,\infty))$,

$$
DF(A)[H]=\operatorname{Tr}f'(A)H,\qquad
D^2F(A)[H,H]=\sum_{i,j}q_{ij}H_{ij}^2,
\quad q_{ij}=\frac{f'(\lambda_i)-f'(\lambda_j)}{\lambda_i-\lambda_j},
$$

where the quotient at equal eigenvalues is $f''(\lambda_i)$. To justify the
formula, for a polynomial expand $\operatorname{Tr}(A+sH)^m$ to second order
and use cyclicity of trace; the coefficient is the displayed divided difference.
Approximate $f''$ uniformly by polynomials on a compact interval and integrate
twice, matching $f,f'$ at an endpoint. The divided differences converge uniformly
because they equal integrals of $f''$ along the intervening segment. This gives
the $C^2$ formula, including collisions, on the bounded spectral range in use.
One may extend $f$ across zero to apply ordinary finite-dimensional Itô.

Stopping the covariance SDE at any $\sigma$ and taking expectations therefore gives

$$
\frac d{dt}\mathbb E\operatorname{Tr}f(A_{t\wedge\sigma})
=\mathbb E\left[\mathbf1_{\{t<\sigma\}}
 \left(\tfrac12\sum_{i,j}q_{ij}|\xi_{ij}|^2
       -\sum_i\lambda_i^2f'(\lambda_i)\right)\right]
\quad\text{for a.e. }t.
$$

Bounded support bounds $f,f',f''$ on the relevant spectral interval and makes
the stochastic integral integrable. In particular the expectation is absolutely
continuous on finite intervals. The predictable stopped-integral indicator can
be written $\mathbf1_{\{t\le\sigma\}}$; its difference from $\mathbf1_{\{t<\sigma\}}$
is immaterial for both $dt$ and Brownian stochastic integration.

:::{prf:remark} Pointwise differentiation in source Lemmas 5.3–5.4
:label: rem:sol-kl-rank-time-derivative
The source writes a derivative at every fixed time, even for an arbitrary
stopping time. The universally justified statement is the absolutely continuous
integral identity and its a.e. derivative above. A deterministic stopping time
can create a corner in an expectation. Every later use is an integrated
Gronwall inequality, for which the a.e. statement suffices. This is a correction
of the formulation used in the proof, not an assumed differentiability claim.
:::

:::{prf:lemma} Stopped spectral-potential growth (source Lemma 5.4)
:label: lem:sol-kl-rank-growth
Let $f\ge0$ be increasing and $C^2$, with $f(x)=x^2$ for $x\ge r$,
$r\in[2,3]$, and $f''\le D^2f$, $D>1$. For every stopping time $\sigma$,

$$
\frac d{dt}\mathbb E\operatorname{Tr}f(A_{t\wedge\sigma})
\le C(t^{-1}+D^2t^{-1/2})\mathbb E\operatorname{Tr}f(A_{t\wedge\sigma})
$$

for almost every $t>0$, with universal $C$.
:::

:::{prf:proof}
The negative drift term in the preceding formula can be discarded since
$f'\ge0$. Fix an instantaneous covariance and suppress $t$ in its eigenvalues.
First set $S=\sum_{i,j,k}\xi_{ijk}^2\mathbf1_{\{\lambda_i\ge r\}}$.
By symmetry, assign a maximal eigenvalue in each triple to the first position.
Counting at most three positions, including ties, gives

$$
S\le3\sum_i\mathbf1_{\{\lambda_i\ge r\}}
 \sum_{j,k:\lambda_j,\lambda_k\le\lambda_i}\xi_{ijk}^2
\le12t^{-1/2}\sum_{\lambda_i\ge r}\lambda_i^{5/2}
\le12t^{-1}\sum_i f(\lambda_i).
$$

The middle inequality is the tensor lemma with fixed index $i$ and
$u=\lambda_i$; the last uses $\lambda_i\le t^{-1}$.
For a pair with both eigenvalues at least $r$, $q_{ij}=2$.
For $\lambda_i\ge r+1$ and $\lambda_j\le r$,
$q_{ij}\le2\lambda_i/(\lambda_i-\lambda_j)\le2(r+1)\le8$.
The reversed pairs have the same bound. Their total contribution is thus at
most a universal multiple of $S$, even if a divided difference is negative.

Every remaining pair has maximum eigenvalue at most $r+1$. By symmetry it
suffices, with a factor at most two, to take $\lambda_j\le\lambda_i\le r+1$.
The integral representation of the divided difference and monotonicity of $f$
give $q_{ij}\le D^2 f(\lambda_i)$. After expanding $|\xi_{ij}|^2$, enlarge the
index set and split according to $\lambda_k\le r+1$ or $\lambda_k>r+1$.
For the first part use the tensor lemma with fixed $i$, summing over $j,k$:

$$
\sum_{i,j,k:\max(\lambda_i,\lambda_j,\lambda_k)\le r+1}
 f(\lambda_i)\xi_{ijk}^2
\le4t^{-1/2}(r+1)^{3/2}
 \sum_{\lambda_i\le r+1}f(\lambda_i)\lambda_i
\le Ct^{-1/2}\sum_i f(\lambda_i).
$$

For the second part $f(\lambda_i)\le f(r+1)=(r+1)^2\le16$.
Use the tensor lemma with fixed $k$ and sum over the two low indices:

$$
\sum_{\lambda_i,\lambda_j\le r+1<\lambda_k}f(\lambda_i)\xi_{ijk}^2
\le Ct^{-1/2}\sum_{\lambda_k>r+1}\lambda_k
\le Ct^{-1/2}\sum_k f(\lambda_k).
$$

Combining the regions bounds $\sum q_{ij}|\xi_{ij}|^2$ by
$C(t^{-1}+D^2t^{-1/2})\operatorname{Tr}f(A_t)$.
Multiply by $\mathbf1_{\{t<\sigma\}}$ and use
$\mathbf1_{\{t<\sigma\}}\operatorname{Tr}f(A_t)
\le\operatorname{Tr}f(A_{t\wedge\sigma})$.
This step uses the nonnegativity of $f$, and is exactly why the growth estimate
survives arbitrary stopping with the same constant.
:::

## Explicit cutoff and the initial-time remainder

:::{prf:lemma} A polynomial completion of the cutoff
:label: lem:sol-kl-rank-cutoff
For $D>1$ and $2\le r\le3$ there is a positive increasing $C^2$ function
$f=f_{D,r}$ on $[0,\infty)$ satisfying

$$
f(x)=e^{D(x-r)}\ (x\le r-D^{-1}),\qquad
f(x)=x^2\ (x\ge r),\qquad f''(x)\le(64D)^2f(x).
$$
:::

:::{prf:proof}
This supplies explicitly the interpolation abbreviated in source Lemma 5.5.
Set $a=e^{-1}$, $b=2r/D$, $d=2/D^2$, and for $0\le s\le1$ define

$$
h_*(s)=a(2s^3-3s^2+1)+b(-2s^3+3s^2)
       +a(s^3-2s^2+s)+d(s^3-s^2).
$$

Then $h_*(0)=a$, $h_*(1)=b$, $h_*'(0)=a$, $h_*'(1)=d$ and
$J:=\int_0^1h_*=7a/12+b/2-d/12$.
Positivity follows by grouping the first and third terms as
$a(1-s)^2(1+3s)$ and the other two as
$s^2[b(3-2s)-d(1-s)]$: here $d\le b/2$.
Moreover $J\le7/(12e)+3<4-1/e\le r^2-a$, since $e>19/12$.
Define $M=30(r^2-a-J)>0$ and $h=h_*+Ms^2(1-s)^2$.
Since $\int_0^1s^2(1-s)^2ds=1/30$, the integral of $h$ is $r^2-a$;
its four endpoint data are unchanged. Also $M\le270$, because $J>0$.
The absolute derivatives of the two value basis polynomials are at most $3/2$,
and those of the two derivative basis polynomials at most $1$.
Using $b\le6$, $d\le2$ and
$|(s^2(1-s)^2)'|\le2$, we get $|h'|<600$.

For $x\in[r-D^{-1},r]$ put $s=D(x-r+D^{-1})$ and
$f(x)=a+\int_0^s h(v)dv$. Then $f'=Dh$, $f''=D^2h'$.
The four endpoint conditions match value, first derivative and second derivative
with the exponential at the left endpoint and $x^2$ at the right endpoint.
On this interval $f\ge a$, so $f''\le600D^2\le1800D^2f<(64D)^2f$.
The inequality outside the interval follows from $f''=D^2f$ on the left and
$f''=2$ on the right. Positivity and monotonicity hold everywhere.
:::

:::{prf:remark} What is and is not reproduced from Lemma 5.5
:label: rem:sol-kl-rank-cutoff-constant
The source obtains coefficient $12$ in place of $64$ by a Lipschitz interpolation
and leaves its last construction as an exercise. This dossier does not claim
that its polynomial has coefficient $12$, or certify that sharper auxiliary
constant. The source iteration only needs a fixed universal coefficient;
substituting $64$ alters the universal growth constant and leaves the exact
exponent $t^{-1/8}$, threshold $3$, and both target conclusions unchanged.
Thus no target step depends on the omitted interpolation exercise.
:::

For completeness, the qualitative source (59) can be justified without importing
its sharper dimension-dependent window (58). For a fixed compact law write
$M_t=\sum_\ell\int_0^tH_{\ell,s}dB_s^\ell$, so
$A_t=I+M_t-\int_0^tA_s^2ds$. If
$\tau_*:=\inf\{s:\|A_s\|_{\mathrm{op}}\ge2\}$ is at most $t$, then
$\lambda_{\max}(M_{\tau_*})\ge1$ because the integral is positive semidefinite.
Since $\|M\|_{\mathrm{op}}\le n\max_{i,j}|M_{ij}|$, one entry has reached
absolute value at least $1/n$. Bounded centered third moments imply
$\langle M_{ij}\rangle_t\le K_\mu t$ with finite $K_\mu>0$ for this fixed
law and dimension. The exponential supermartingale
$\exp(\eta M_{ij,s}-\eta^2\langle M_{ij}\rangle_s/2)$, stopped at first
passage and at $t$, gives

$$
\mathbb P\!\left(\sup_{s\le t}|M_{ij,s}|\ge1/n\right)
\le2\exp[-1/(2n^2K_\mu t)].
$$

Indeed the one-sided bound is
$\exp[-\eta/n+\eta^2K_\mu t/2]$, minimized at
$\eta=(nK_\mu t)^{-1}$; use also $-M_{ij}$.
Taking the union over $n^2$ entries proves
$\mathbb P(\tau_*\le t)=o(t^m)$ for every fixed $m>0$ as $t\downarrow0$.
Uniform constants in $\mu,n$ are neither asserted nor needed for this limit.

## The geometric-time iteration: Proposition 5.1

:::{prf:proof} Proof of the stopped-count assertion
Fix $\mu,n,\sigma$ first. For $0<t\le2^{-8}$ define

$$
t_j=2^{-8j}t,\quad D_j=t_j^{-1/4},\quad
r_0=3,\quad r_{j+1}=r_j-t_j^{1/8}.
$$

The total decrement is $2t^{1/8}\le1$, so $2\le r_j\le3$.
Put $f_j=f_{D_j,r_j}$ from the cutoff lemma and
$g_j(x)=x^2\mathbf1_{\{x\ge r_j\}}$.
In the growth lemma use parameter $64D_j$. For
$s\in[t_{j+1},t_j]$, $D_j^2/\sqrt s\le1/s$.
An a.e. differential inequality integrates to

$$
\mathbb E\operatorname{Tr}f_j(A_{t_j\wedge\sigma})
\le2^{8C_1}\mathbb E\operatorname{Tr}f_j(A_{t_{j+1}\wedge\sigma})
$$

with universal $C_1$, enlarged to absorb $64^2$.
Pointwise on $[0,\infty)$,

$$
g_j\le f_j,\qquad
f_j\le\tfrac94g_{j+1}+e^{-t_j^{-1/8}}.
$$

For the second inequality, if $x\le r_{j+1}$ then
$r_{j+1}\le r_j-D_j^{-1}$, so monotonicity and the exponential formula give
$f_j(x)\le e^{-D_jt_j^{1/8}}=e^{-t_j^{-1/8}}$.
If $x\ge r_j$, $f_j(x)=g_{j+1}(x)=x^2$.
On the intervening interval $f_j(x)\le r_j^2\le(9/4)x^2$ and
$g_{j+1}(x)=x^2$.

Writing $F_j=\mathbb E\operatorname{Tr}g_j(A_{t_j\wedge\sigma})$, choose
universal $b=8C_1+2>0$ to obtain

$$
F_0\le2^{b m}F_m+n\sum_{j=0}^{m-1}2^{b(j+1)}e^{-2^jt^{-1/8}}.
$$

Because $t^{-1/8}\ge2$, the sum is at most

$$
ne^{-t^{-1/8}}\sum_{j=0}^{\infty}2^{b(j+1)}e^{-2(2^j-1)}
=C_b n e^{-t^{-1/8}},\qquad C_b<\infty.
$$

It remains to justify discarding the first term. Compact support gives
$\sup_s\operatorname{Tr}A_s^2\le L_\mu<\infty$, also at stopped times.
As $r_m\ge2$ and eigenvalues are continuous from $A_0=I$,

$$
F_m\le L_\mu\mathbb P(\|A_{t_m\wedge\sigma}\|_{\mathrm{op}}\ge2)
\le L_\mu\mathbb P(\tau_*\le t_m).
$$

The previous qualitative estimate is faster than every power. Since
$2^{bm}\le t_m^{-b}$, the remainder tends to zero for this fixed law,
uniformly over the choice of $\sigma$ in this bound. The constants $L_\mu,K_\mu$
vanish with the terminal term and do not enter $C_b$.
Finally $\mathbf1_{\{x\ge3\}}\le g_0(x)$, proving the claimed rank count
for $t\le2^{-8}$. For $t\ge2^{-8}$ the count is at most $n$ and
$e^{-t^{-1/8}}\ge e^{-2}$; increasing $C$ to at least $e^2$ proves the
same statement for every $t>0$. This also covers $\sigma=0$ and $\sigma=\infty$.
:::

## Hitting times and time integration: Corollary 6.1 and Theorem 6.2

:::{prf:proof} Proof of the two hitting-time consequences
Continuity and adaptation make $\sigma_k$ a stopping time for the usual Brownian
filtration. Pathwise $\sigma_k>0$, because $\lambda_k(0)=1$.
On $\{\sigma_k\le t\}$ continuity gives $\lambda_k(\sigma_k)=3$ and
$\lambda_i(t\wedge\sigma_k)\ge3$ for all $i\le k$.
Thus

$$
k\mathbb P(\sigma_k\le t)
\le\sum_{i=1}^n\mathbb P(\lambda_i(t\wedge\sigma_k)\ge3)
\le Cn e^{-t^{-1/8}}.
$$

This uses the stopped estimate, not merely a bound at the deterministic time
$t$; an eigenvalue can fall below threshold after its first hit.

Set $q=n/k\ge1$, $\alpha=1/8$, and $x_0=(2\log q)^{1/\alpha}$.
Tonelli's layer-cake identity, with the convention $\infty^{-1}=0$, yields

$$
\mathbb E\sigma_k^{-2}
=\int_0^\infty2x\,\mathbb P(\sigma_k^{-1}>x)\,dx
\le x_0^2+Cq\int_{x_0}^\infty2x e^{-x^\alpha}\,dx.
$$

Use $qe^{-x_0^\alpha/2}=1$ and split the exponent into two halves:

$$
\mathbb E\sigma_k^{-2}
\le(2\log q)^{16}+C\int_0^\infty2x e^{-x^\alpha/2}\,dx
\le C'(1+\log q)^{16}.
$$

The integral is finite by the substitution $y=x^\alpha/2$, giving a constant
times $\int_0^\infty y^{15}e^{-y}dy$. When $k=n$, $x_0=0$ and the same
calculation applies. Strict versus non-strict hitting events does not affect
the upper bound. This completes all assertions of the first target.
:::

:::{prf:proof} Proof of the integrated rank covariance assertion
Each $\lambda_k$ is the $k$th largest eigenvalue **at that time**, with no choice
of a persistent eigenvector. Before $\sigma_k$ it is below $3$, and at every
positive time it is at most $1/t$. Hence, pathwise, with
$u_k=\sigma_k\wedge1\in(0,1]$,

$$
\int_0^1\lambda_k(t)dt
\le3u_k+\int_{u_k}^1\frac{dt}{t}
\le3-\log u_k,
\qquad
\exp\left(2\int_0^1\lambda_k(t)dt\right)
\le e^6(1+\sigma_k^{-2}).
$$

There is no integration of $1/t$ at zero: the initial interval uses the
threshold bound. If $\sigma_k=\infty$, $u_k=1$ and the right side is $e^6$.
Taking expectations and using the inverse moment bound reduces the claim to
$\sum_{k=1}^n(1+\log(n/k))^{16}\le Cn$.
For the decreasing nonnegative function
$h(x)=(1+\log(1/x))^{16}$ on $(0,1]$, every interval
$((k-1)/n,k/n]$ has $h(x)\ge h(k/n)$. Therefore

$$
\frac1n\sum_{k=1}^n h(k/n)
\le\int_0^1h(x)dx
=\int_0^\infty(1+y)^{16}e^{-y}dy<\infty.
$$

The finite sum and expectation can be interchanged by linearity (or Tonelli
before integrability has been shown). The pathwise integrals exist by covariance
continuity. This proves the second target with a universal constant, without
interchanging exponential and expectation or integrating a fixed-time tail.
:::

## Hypothesis usage, scope, and reviewer handoff

| Hypothesis or convention | Exact use | What is not inferred |
|---|---|---|
| Compact support | Uniform bounds on all tilt moments; global ODE; true martingales; polynomial approximation; vanishing terminal term | No extension of these two stochastic statements to noncompact laws is asserted |
| Isotropy | $A_0=I$, full-dimensional support, separation from thresholds $2,3$ | No arbitrary-covariance formulation or hidden rescaling |
| Log-concavity | Strong log-concavity after tilting; projected quadratic Poincaré bound and $1/t$ cap | No assertion for all compact isotropic distributions |
| Brownian-filtration stopping | Stopped Itô formula and first-hit argument | No anticipative random-time estimate |
| Decreasing eigenvalue order | At least $k$ eigenvalues at a rank-$k$ hit | No eigenvector or source alignment |
| Positive increasing cutoff | Discard negative drift; dominate the stopped integrand | No need for convexity of the interpolating cutoff |
| $t>0$, $n\ge1$, $1\le k\le n$ | Growth away from zero; rank sum and $k=n$ endpoint | No dimension restriction hidden in a logarithmic window |

**Mechanism and bottleneck.** For stopped rank tails: improved Lichnerowicz
controls a low-eigenvalue slice of the third tensor; tensor symmetry bounds the
spectral-potential drift; the shrinking thresholds and geometric times give a
summable exponential error. The growth estimate, not the initial window, governs
the exponents obtained by this iteration. For integrated covariance: a first hit
controls the number of large ranks; its inverse moment pays for the logarithmic
post-hit integral; summation of the logarithmic rank profile costs only $n$.
This last step sees eigenvalue ranks and loses all eigenspace orientation.

**Fences respected.** Neither target has a `bounded_by`, `depends_on`, or
`assumes` edge in the ledger read for this mission, so there are no explicit
node fences to discharge. The brief's thin-shell/KLS distinction and the
manuscript's orientation warning remain in force: no claim is made about
[](#conj:trace-upgrade), [](#conj:mm-spectral-occupation), or
[](#conj:stein-weighted). The proof uses the established
[](#thm:improved-lichnerowicz) as an input, not an open antecedent. The source
dependency map above records the internal dependence of the integrated bound
on the stopped one even though the present ledger does not encode it.

:::{prf:remark} Source-audit boundary and certification boundary
:label: rem:sol-kl-rank-audit-boundary
No source-access gap remained for the pinned HTML/PDF sections used here.
The pointwise derivative formulation is replaced by an a.e. identity; the
source cutoff's coefficient $12$ is not established by this dossier and is
replaced by the explicitly proved universal coefficient $64$. Neither difference
leaves a step of the two target arguments conditional on that unverified
formulation or constant. The established improved Lichnerowicz theorem and
standard Prékopa–Leindler inequality are external inputs, not newly proved here.
No independent certification is claimed. In particular the regularization,
cutoff algebra, tensor index accounting, and elimination of the nonuniform
terminal term still require a cold review of this reconstruction.
:::

**Next for the reviewer.** Independently check both exact manuscript directives
against the statements above and v2 Proposition 5.1, Corollary 6.1, and Theorem
6.2. Audit every row of the dependency map, in particular the nonsmooth projected
Poincaré passage, spectral Hessian at collisions, all regions of Lemma 5.4,
the explicit replacement cutoff, the a.e. Gronwall interpretation, the fixed-law
terminal limit and surviving universal constants, and the inverse-moment/rank
integration endpoints. Distinguish the published analytic input from the
preprint assertions being reviewed. Neither target has an explicit ledger
fence; retain the compact/isotropic/log-concave class and Brownian-filtration
scope, and exclude every orientation or KLS claim. Run the full checker and
fingerprint the stabilized dossier and relevant statements before any review
record. The author proposes no status or proof-record delta.
