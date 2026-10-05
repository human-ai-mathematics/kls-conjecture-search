---
title: 'Solution: the Letwin matrix and quadratic imports'
ledger-node:
  - thm:letwin-moment-map
  - thm:letwin-qcts
numbering:
  enumerator: '103.%s'
---

**Overview.** This dossier gives a proof of the precise matrix and quadratic estimates
imported as [](#thm:letwin-moment-map) and [](#thm:letwin-qcts). It follows the mechanism
of [@Letwin2026QuadraticKLS], pinned to
[arXiv:2607.24164v1](https://arxiv.org/abs/2607.24164v1), and expands the coordinate
change and the analytic domains needed in that mechanism. This is an author's dossier,
not its independent certification.

1. On a bounded regular target, construct cutoffs in the source coordinates and justify
   integrating the differentiated Monge–Ampère identity before using its positive terms.
2. Transform the third-order tensor and the fixed matrix together. The pointwise
   comparison then combines with Brascamp–Lieb to give the matrix estimate.
3. Transfer the Stein kernel by congruence, apply the published $H^{-1}$ inequality on a
   generally non-isotropic law, and remove singular matrices and target regularity.

The source locations are Theorem 2.5 (PDF pp. 8–13), Theorem 1.2 (p. 3, proof on
pp. 14–16), and Appendix A (pp. 16–18). Page numbers refer to the PDF, with its first
page numbered one. The [versioned HTML](https://arxiv.org/html/2607.24164v1) also carries
the theorem and lemma numbers. The proof of the general KLS bound, Theorem 1.1 of the
source, is outside this dossier.

## Statements and published inputs

:::{prf:definition} Regular target used in this dossier
:label: def:sol-letwin-regular
Fix an integer $n\ge1$. A regular target is an isotropic probability measure
$\mu(dx)=e^{-V(x)}\mathbf1_K(x)\,dx$, where $K\subset\mathbb R^n$ is nonempty,
bounded, open and convex, and $V$ is smooth and convex on an open neighborhood of
$\overline K$. Isotropic means $\mathbb E X=0$ and $\mathbb E XX^T=I$.
Let $\varphi$ be its canonical moment potential, normalized so that
$\nu(dy)=e^{-\varphi(y)}dy$ is a probability and $(\nabla\varphi)_\#\nu=\mu$.
Write $H=D^2\varphi$.
:::

:::{prf:theorem} Matrix estimate and quadratic Poincaré estimate
:label: thm:sol-letwin-imports
For every regular target in [](#def:sol-letwin-regular) and every constant real
symmetric $n\times n$ matrix $B$,

$$
\mathbb E_\nu\operatorname{Tr}(BHBH)\le2\operatorname{Tr}(B^2).
$$

For every isotropic log-concave random vector $X$ in $\mathbb R^n$, $n\ge1$, and
every real symmetric $n\times n$ matrix $M$,

$$
\operatorname{Var}(X^TMX)\le8\|M\|_{\mathrm{HS}}^2
 =2\mathbb E|\nabla(x^TMx)|_{x=X}^2.
$$

Consequently the quantity in [](#def:qcts) satisfies $\mathcal Q(\mu)\le8$.
:::

The established inputs used below are the compact-target regularity theorem
[](#thm:regular-moment-map-compact-target), the pointwise estimate of
[@Klartag2013MomentMeasures, Theorem 1.1], the convex-boundary Brascamp–Lieb
inequality [@KolesnikovMilman2017BoundaryBL, Theorem 1.2(1)], and
[@BartheKlartag2019SpectralGaps, Propositions 10 and 27].
We use these as published results, not the conclusions of either recent preprint.
The application of each is specified below. Gaussian convolution preserves log-concavity,
and finite-dimensional log-concave probabilities have finite polynomial moments; these
standard facts are used only in the last approximation step.

## Regularity, symmetry and integration

The regularity node applies with $P=\overline K$. Indeed, multiplying $V$ by a smooth
cutoff equal to one near $P$ gives a globally smooth extension of $V|_P$; its exponential
is positive and globally smooth, as required by that node. The extension need not be
convex outside $P$. Thus $\varphi$ is smooth, $H\succ0$, and $\nabla\varphi$ maps
$\mathbb R^n$ diffeomorphically onto $K$. The change-of-variables equation is

$$
\log\det H=-\varphi+V(\nabla\varphi).
$$

The hypotheses of Klartag's Theorem 1.1 are satisfied: $V$ and each of its derivatives
are bounded on $K$, by smoothness near the compact set $\overline K$. It gives
$\operatorname{Tr}H\le2R_K^2$, where $R_K=\sup_{x\in K}|x|$.
In particular $H$ and $\nabla\varphi$ are bounded; no positive uniform lower bound
on $H$ is asserted or used.

Use $H^{ab}$ for the entries of $H^{-1}$ and define

$$
Lf=H^{ab}\partial_{ab}f-V_a(\nabla\varphi)\partial_af,
\qquad \Gamma(f,g)=H^{ab}\partial_af\partial_bg.
$$

Repeated indices are summed. Differentiating the inverse Hessian and using symmetry
of third derivatives gives
$\partial_a H^{ab}=-H^{bi}\partial_i\log\det H$.
The logarithmic equation therefore implies the divergence formula

$$
Lf=e^{\varphi}\partial_a(e^{-\varphi}H^{ab}\partial_bf).
$$

Consequently $\int (Lf)g\,d\nu=-\int\Gamma(f,g)\,d\nu$ when either smooth
function has compact support. This assertion is local and requires no tail estimate
on $H^{-1}$.

Ordinary Euclidean integration by parts with a cutoff $\zeta(y/R)$ gives
$\mathbb E\partial_i f=\mathbb E f\partial_i\varphi$ whenever all displayed
terms and $f$ are integrable: the extra term is bounded by
$C R^{-1}\mathbb E|f|$. Applying it to $f=\partial_j\varphi$, whose derivative
and all other terms are bounded, gives

$$
\mathbb E_\nu H_{ij}=\mathbb E_\nu(\partial_i\varphi\partial_j\varphi)
=\mathbb E_\mu X_iX_j=\delta_{ij}.
$$

:::{prf:lemma} Cutoffs and vanishing integrated generator
:label: lem:sol-letwin-cutoffs
There are $\chi_R\in C_c^\infty(\mathbb R^n)$ with $0\le\chi_R\le1$,
$\chi_R\to1$ pointwise and $\|L\chi_R\|_{L^1(\nu)}\to0$.
If $f$ is bounded and smooth and $Lf+cf\ge0$ for some $c>0$, then
$Lf\in L^1(\nu)$ and $\mathbb E Lf=0$.
:::

:::{prf:proof}
An integrable exponential of a finite convex potential has bounded sublevel sets:
otherwise a sublevel set with nonempty interior would be an unbounded convex set
containing a ball, hence have infinite volume, contradicting integrability. Thus
$\varphi$ is coercive and attains its minimum. Put $W=\varphi-\min\varphi+1$.
The formula for $L$ gives $LW=n-\nabla V(\nabla\varphi)\cdot\nabla\varphi$,
so $D=\|LW\|_\infty<\infty$.

Choose a smooth nonincreasing $\eta$ with values in $[0,1]$, equal to one on
$(-\infty,1]$ and zero on $[2,\infty)$, and set $\chi_R=\eta(W/R)$.
These cutoffs are compactly supported. Choose smooth compactly supported
$w\ge|\eta''|$, $w\ge0$, and put
$q_R(t)=R^{-1}\int_{t/R}^{\infty}w(s)\,ds$.
Then $q_R(W)$ has compact support, $\|q_R\|_\infty\le R^{-1}\|w\|_1$,
and $-q_R'(t)=R^{-2}w(t/R)$. Compactly supported integration by parts yields

$$
R^{-2}\int w(W/R)\Gamma(W)\,d\nu
=\int q_R(W)LW\,d\nu\le D\|w\|_1/R.
$$

The chain rule
$L\chi_R=R^{-1}\eta'(W/R)LW+R^{-2}\eta''(W/R)\Gamma(W)$ now gives
$\|L\chi_R\|_1\le D(\|\eta'\|_\infty+\|w\|_1)/R$.

For the last assertion, compact support and symmetry give

$$
\int\chi_R(Lf+cf)\,d\nu=c\int\chi_R f\,d\nu+\int fL\chi_R\,d\nu.
$$

The left integrand is nonnegative and the right side is uniformly bounded.
Fatou's lemma gives $Lf+cf\in L^1$, hence $Lf\in L^1$. Dominated convergence
and $\|L\chi_R\|_1\to0$ then give $\int Lf\,d\nu=0$.
:::

For later use, every bounded smooth $u$ satisfies
$\operatorname{Var}_\nu u\le\int\Gamma(u)\,d\nu$, allowing infinity on the right.
Here the precise boundary input is
[Kolesnikov–Milman, Theorem 1.2(1)](https://publications.hse.ru/pubs/share/direct/216903475.pdf)
([DOI](https://doi.org/10.1007/s12220-016-9736-5)). Set
$M_R=\{\varphi\le R\}$ for $R>\min\varphi$, with its Euclidean metric and
conditional probability $\nu_R=\nu|_{M_R}/\nu(M_R)$.
These closed sublevels are compact, connected and convex. Since $H\succ0$, their
boundaries are smooth and $\nabla\varphi$ does not vanish there. With outward normal
$\nabla\varphi/|\nabla\varphi|$, their second fundamental form on tangent vectors is
$H/|\nabla\varphi|\succeq0$ (vacuously on the zero-dimensional boundary when $n=1$).
The conditional potential is $\varphi+\log\nu(M_R)$, so the Euclidean
$N=\infty$ curvature tensor in the cited theorem is exactly $D^2\varphi=H\succ0$;
its prefactor $N/(N-1)$ equals one. The theorem applies to arbitrary $C^1(M_R)$
tests, with no Neumann condition on $u$, and yields

$$
\operatorname{Var}_{\nu_R}u
\le\frac{1}{\nu(M_R)}\int_{M_R}\nabla u^TH^{-1}\nabla u\,d\nu.
$$

The domains exhaust $\mathbb R^n$ and $\nu(M_R)\to1$. Boundedness of $u$ passes
its conditional first and second moments; monotone convergence passes the
unnormalized nonnegative energy integrals. This proves the claimed inequality,
including the case of infinite energy.

## The full tensor comparison

Differentiating the logarithmic Monge–Ampère identity twice gives

$$
LH+H=A+Q,\qquad
A=H(D^2V\circ\nabla\varphi)H,\qquad
Q_{ij}=H^{ac}H^{bd}\varphi_{abi}\varphi_{cdj}.
$$

For clarity, its first derivative is
$H^{ab}\varphi_{abi}=-\varphi_i+V_a\varphi_{ai}$, and differentiating it uses
$\partial_jH^{ab}=-H^{ac}\varphi_{cdj}H^{db}$.
The drift term $V_a\varphi_{aij}$ moves to the left and gives $LH_{ij}$.
Both $A$ and $Q$ are positive semidefinite: convexity gives the first, and the second
is the Gram matrix of $H^{-1/2}(\partial_iH)H^{-1/2}$.

Fix $B\succeq0$ and introduce

$$
S=\operatorname{Tr}(BHBH),\quad
D_B=H^{ab}\operatorname{Tr}(B\partial_aH B\partial_bH),\quad
C_B=\operatorname{Tr}(BHBQ),\quad
A_B=\operatorname{Tr}(BHBA).
$$

All four are nonnegative. For $D_B$ this follows by contracting the Gram matrix of
$B^{1/2}(\partial_aH)B^{1/2}$ with $H^{-1}$; for $C_B,A_B$ it follows from
the trace of a product of positive semidefinite matrices. Product differentiation gives

$$
LS=-2S+2(D_B+A_B+C_B).
$$

$S$ is bounded. The cutoff lemma with $c=2$ first gives $LS\in L^1$ and
$\mathbb E LS=0$. The nonnegative sum is therefore integrable, and each summand
is integrable separately. Only at this point do we obtain

$$
\mathbb E S=\mathbb E D_B+\mathbb E A_B+\mathbb E C_B.
$$

The pointwise comparison is $C_B\ge D_B$. Here is the coordinate calculation
including the invariance that permits normalization. At the point in question take
an invertible constant matrix $P$, put $y=Pz$, and transform

$$
\widetilde H=P^THP,\quad
\widetilde B=P^{-1}BP^{-T},\quad
\widetilde T_{abc}=P_{ia}P_{jb}P_{kc}T_{ijk},\qquad T_{ijk}=\varphi_{ijk}.
$$

The inverse Hessian transforms as $P^{-1}H^{-1}P^{-T}$. Contracting two copies of
$\widetilde T$ with two inverse Hessians gives $\widetilde Q=P^TQP$; hence
$\operatorname{Tr}(\widetilde B\widetilde H\widetilde B\widetilde Q)=C_B$.
Moreover

$$
\partial_{z_a}\widetilde H
=\sum_i P_{ia}P^T(\partial_{y_i}H)P,
$$

so cyclicity of the trace and
$\sum_{ab}(\widetilde H^{-1})_{ab}P_{ia}P_{jb}=(H^{-1})_{ij}$ show
$\widetilde D_{\widetilde B}=D_B$. Thus each scalar in the comparison is invariant.
Choose $P$ so that $P^THP=I$, followed by an orthogonal change that diagonalizes
$\widetilde B=\operatorname{diag}(b_1,\ldots,b_n)$. It remains symmetric and
positive semidefinite by congruence. In these coordinates

$$
D_B=\sum_{ijk}b_i b_j T_{ijk}^2,\qquad
C_B=\sum_{ijk}b_i^2T_{ijk}^2,
$$

and full symmetry of $T$ implies

$$
C_B-D_B=\frac12\sum_{ijk}(b_i-b_j)^2T_{ijk}^2\ge0.
$$

This is a change at a single point with a constant $P$; no derivative of a moving
normalizing frame is taken. The global mean identity and Brascamp–Lieb step remain
in the original coordinates. We conclude that $\mathbb E D_B\le\tfrac12\mathbb E S$.

## Proof of the matrix assertion

:::{prf:proof}
For $B\succeq0$, put $F=B^{1/2}HB^{1/2}$. Its entries are bounded smooth functions,
its mean is $B$, and summing their Brascamp–Lieb inequalities gives

$$
\mathbb E S-\operatorname{Tr}(B^2)
=\sum_{ij}\operatorname{Var}(F_{ij})
\le\mathbb E D_B\le\tfrac12\mathbb E S.
$$

This proves the matrix estimate for positive semidefinite $B$, including singular $B$.
For any symmetric $B$, in its orthonormal eigenbasis
$\operatorname{Tr}(BHBH)=\sum_{ij}b_i b_j H_{ij}^2
\le\sum_{ij}|b_i||b_j|H_{ij}^2=\operatorname{Tr}(|B|H|B|H)$.
Apply the established positive case to $|B|$, whose squared trace norm is unchanged.
This proves the first assertion of [](#thm:sol-letwin-imports).
:::

## Quadratic functions, congruence, and singular matrices

For a centered log-concave probability $\lambda$, use the homogeneous dual norm

$$
\|h\|_{H^{-1}(\lambda)}
=\sup\left\{\int hg\,d\lambda:\ g\text{ locally Lipschitz},\quad
g\in L^2(\lambda),\quad\int|\nabla g|^2\,d\lambda\le1\right\},
\qquad \int h\,d\lambda=0.
$$

The published Barthe–Klartag Proposition 10 states that
$\operatorname{Var}_\lambda f\le\sum_i\|\partial_i f\|_{H^{-1}(\lambda)}^2$
provided $f,\partial_i f\in L^2$ and $\int\partial_i f\,d\lambda=0$ for every $i$.
It requires log-concavity, not isotropy. Their Proposition 27 supplies density of
$C_c^\infty(\mathbb R^n)$ in the weighted $H^1$ norm.

In target coordinates let $\tau(x)=H((\nabla\varphi)^{-1}(x))$.
For $g\in C_c^\infty(\mathbb R^n)$ the bounded functions
$g(\nabla\varphi)$ and their derivatives permit ordinary source integration by parts:

$$
\mathbb E_\mu X_i g(X)
=\mathbb E_\nu\varphi_i g(\nabla\varphi)
=\mathbb E_\nu\sum_jH_{ij}(\partial_jg)(\nabla\varphi)
=\mathbb E_\mu\sum_j\tau_{ij}(X)\partial_jg(X).
$$

If a centered full-dimensional log-concave $\lambda$ has a symmetric Stein kernel
$\tau_\lambda\in L^2(\lambda)$, Cauchy–Schwarz gives for such $g$

$$
\left|\mathbb E (v\cdot Z)g(Z)\right|
\le\left(\mathbb E|\tau_\lambda(Z)v|^2\right)^{1/2}
\left(\mathbb E|\nabla g(Z)|^2\right)^{1/2}.
$$

Proposition 27 extends this to every test in the dual norm: both sides of the Stein
identity converge in an $H^1$ approximation by Cauchy–Schwarz, since $v\cdot Z$
and $\tau_\lambda v$ are square integrable. Therefore
$\|v\cdot z\|_{H^{-1}(\lambda)}^2\le\mathbb E|\tau_\lambda(Z)v|^2$.

:::{prf:proof} Proof of the quadratic assertion on regular targets
First suppose $M$ is symmetric and invertible. Write $P=|M|^{1/2}$,
$J=M|M|^{-1}$, $Z=PX$, and $\lambda=P_\#\mu$.
Then $J^TJ=I$, $\mathbb EZ=0$, and $\operatorname{Cov}Z=|M|$.
Changing variables in the Stein identity gives the symmetric Stein kernel
$\tau_\lambda(Z)=P\tau(X)P$. In particular,

$$
\mathbb E\|\tau_\lambda(Z)\|_{\mathrm{HS}}^2
=\mathbb E_\nu\operatorname{Tr}(|M|H|M|H)
\le2\operatorname{Tr}(M^2).
$$

The function $f(z)=z^TJz-\operatorname{Tr}M$ has zero mean and derivatives
$\partial_i f(z)=2(Je_i)\cdot z$ with zero means. Since $\lambda$ has bounded
support, $f$ and its derivatives are in $L^2$. The published inequality and the dual
Stein bound therefore give

$$
\begin{aligned}
\operatorname{Var}(X^TMX)
&\le4\sum_i\|(Je_i)\cdot z\|_{H^{-1}(\lambda)}^2\\
&\le4\mathbb E\sum_i|\tau_\lambda(Z)Je_i|^2
=4\mathbb E\|\tau_\lambda(Z)\|_{\mathrm{HS}}^2
\le8\operatorname{Tr}(M^2).
\end{aligned}
$$

For a singular symmetric $M$, let $P_0$ be the orthogonal projection onto its kernel
and set $M_\delta=M+\delta P_0$, $\delta>0$. This matrix is invertible,
$\operatorname{Tr}(M_\delta^2)=\operatorname{Tr}(M^2)+\delta^2\dim\ker M$,
and $\|X^T(M_\delta-M)X\|_2\le\delta(\mathbb E|X|^4)^{1/2}$.
Hence the estimate passes to $M$ in $L^2$. This order avoids using an orthogonal
sign matrix or an invertible congruence for a singular $M$.
:::

## Removing target regularity and matching the normalization

:::{prf:proof} Proof of the quadratic assertion for every isotropic log-concave law
Fix the dimension and an isotropic log-concave $X$. Let $G$ be an independent standard
Gaussian and $Y_\varepsilon=X+\sqrt\varepsilon G$, for $0<\varepsilon\le1$.
Condition its law on $|Y_\varepsilon|<\varepsilon^{-1/2}$ and denote the conditional
mean and covariance by $m_\varepsilon,A_\varepsilon$.
The convolved density is smooth, positive and log-concave. Conditioning on the ball
preserves log-concavity and gives positive definite covariance. After the affine map
$y\mapsto A_\varepsilon^{-1/2}(y-m_\varepsilon)$ its law $\mu_\varepsilon$ is
an isotropic regular target: the support is a bounded open ellipsoid and its potential
is smooth convex on a neighborhood of the closed ellipsoid, with the normalization
constant absorbed into the potential.

All moments of $X$ are finite, so $\sup_{0<\varepsilon\le1}\mathbb E|Y_\varepsilon|^8$
is finite. Moreover

$$
\mathbb E\left[|Y_\varepsilon|^4
\mathbf1_{\{|Y_\varepsilon|\ge\varepsilon^{-1/2}\}}\right]
\le\varepsilon^2\mathbb E|Y_\varepsilon|^8\longrightarrow0.
$$

The probability of the conditioning event tends to one, and
$Y_\varepsilon\to X$ in $L^4$. Thus conditional moments through degree four converge
to those of $X$; in particular $m_\varepsilon\to0$ and $A_\varepsilon\to I$.
Continuity of the inverse square root near $I$ shows that affine normalization preserves
all these moment limits. For each fixed symmetric $M$, apply the regular-target
quadratic bound to $\mu_\varepsilon$. Variance involves only moments through degree
four, so its limit gives $\operatorname{Var}(X^TMX)\le8\operatorname{Tr}(M^2)$.

Finally $\nabla(x^TMx)=2Mx$ and isotropy gives
$\mathbb E|2MX|^2=4\operatorname{Tr}(M^2)$, yielding the gradient formulation.
The supremum in [](#def:qcts) is also harmless if read over all real matrices:
$x^TMx=x^T(M+M^T)x/2$ and symmetrization does not increase the Hilbert–Schmidt norm.
Taking the supremum proves $\mathcal Q(\mu)\le8$.
:::

## Transfer, hypotheses, and exclusions

The matrix statement matches source Theorem 2.5 on exactly the class of its Lemma A.1;
the quadratic statement matches source Theorem 1.2 on the whole isotropic log-concave
class. The preceding argument uses no regular moment potential for the limiting law.
It does not assert convergence of Hessians under the approximation, only convergence
of the polynomial moments needed for the quadratic variance.

| Hypothesis | Where it is used |
|---|---|
| Centering and covariance $I$ | $\mathbb EH=I$, centered derivatives, and the final gradient normalization |
| Convex target and smooth convex $V$ near its closure | Regular moment map, bounded coefficients, and positivity of $A$ |
| Bounded target | Bounded $\nabla\varphi,H,LW$ and bounded regular quadratic tests |
| Constant symmetric $B$ | Product differentiation and the tensor comparison; no derivatives of $B$ occur |
| Invertible $M$ at the intermediate step | Full-dimensional congruence and orthogonality of $J$; removed by an explicit limit |
| Log-concavity of the transported law | Published $H^{-1}$ inequality and Sobolev density; isotropy is not needed there |
| Finite polynomial moments of the original law | Gaussian conditioning and the fourth-moment passage |

:::{prf:remark} Scope of the source examination
:label: rem:sol-letwin-scope
The argument above reconstructs the proof ingredients needed for the two imported
statements, including the noncompact cutoffs and singular-matrix limit. It does not
verify source Theorem 1.1 or the bridge $C_P\lesssim\kappa_n\sqrt{\log n}$.
That bridge remains a separate review task; its omission here is not an antecedent
of either theorem proved above. The published regularity, Hessian bound,
Brascamp–Lieb and Barthe–Klartag results are external inputs, whose applications are
specified rather than whose published proofs are reproduced. No claim of independent
certification is made by this dossier.
:::

**Fences respected.** Neither imported node has a `bounded_by` edge. The program's
relevant boundaries are nevertheless explicit. [](#prop:letwin-not-gate-zero) is
respected because the conclusion is a fixed-matrix trace inequality, not
$\mathbb E H^2\preceq cI$. [](#rem:projection-ceiling) is respected because the proof
uses a full tensor comparison, not projection-only data. The two-tail scaling boundary
[](#rem:two-tail-slice-bounds) is untouched: no unwhitened cut source is bounded here.
The occupation, bootstrap and moving-competitor boundaries
[](#rem:relative-ceiling), [](#rem:crude-insufficient), [](#rem:profile-circularity)
and [](#rem:single-coordinate-cuts) are untouched because no stochastic-time or
cut-dependent assertion is proved. No comparison between the trace-upgrade cluster
members is asserted, and no open antecedent is discharged by assumption.
