---
title: "Chen–Klartag imports: moment Hessian, thin shell, and third tensor"
ledger-node:
  - thm:chen-klartag-moment-hessian
  - thm:chen-klartag-thin-shell
  - thm:chen-klartag-third-moment
numbering:
  enumerator: "104.%s"
---

*Part of the results of the literature written out here, Chapter [](#sec:family-moment-map); the reading order is on the [full proofs](#sec:proofs-literature) page.*

**Author:** researcher_chen_klartag, gpt-6-astra, 2026-10-01.

**Overview.** This is an author dossier, without certification. The source is
Chen–Klartag, *Digesting the Proof of the Sharp Thin-Shell Inequality*,
[arXiv:2607.23307v1](https://arxiv.org/html/2607.23307v1)
[@ChenKlartag2026SharpThinShell]. The pinned HTML, including Sections 2–4 and
Appendix A, was accessible and read. No replacement version is used.
Theorem 1.5 is the Hessian import; Theorems 1.1 and 1.2 are the two consequences.
Corollary 1.3 is also addressed because its convex-body and simplex assertion
occurs inside the manuscript's third-tensor directive.

The proof below differentiates Monge–Ampère, establishes the required integrability
before integrating the resulting identity, and combines its energy balance with
Brascamp–Lieb. It then derives the third tensor by orthogonal projection and thin
shell by the published negative-Sobolev inequality. A moment-convergent regularization
removes the target regularity only for the distributional conclusions. Finally,
exact exponential and simplex calculations check the constants.

## Statements and normalization

The three manuscript directives in Chapter [](#sec:family-moment-map) read as follows
(the mathematical content is transcribed; bibliography and cross-reference rendering
are immaterial):

> Under the regularity assumptions of [@ChenKlartag2026SharpThinShell],
> $\mathbb E_\nu\|H\|_{\mathrm{HS}}^2\le2n$.
> The general log-concave conclusions below follow by the approximation argument in that preprint.

> For every isotropic log-concave $X\in\mathbb R^n$,
> $\operatorname{Var}(|X|^2)\le8n$.
> The constant is attained by products of standard centered one-sided exponential variables.

> If $X\in\mathbb R^n$ is isotropic and log-concave and
> $T_3(X)=(\mathbb E X_iX_jX_k)_{i,j,k}$, then
> $\|T_3(X)\|_{\mathrm{HS}}^2\le4n$.
> The preprint also proves sharper convex-body estimates with equality for the regular simplex.

Here isotropic means $\mathbb EX=0$ and $\mathbb EXX^T=I_n$, with $n\ge1$.
We use the source's $\psi$ for the moment potential; this is the manuscript's
$\varphi$, not the source's Legendre-dual $\varphi=\psi^*$.
Thus $\nu=e^{-\psi(x)}dx$, $(\nabla\psi)_\#\nu=\mu$, and $H=D^2\psi$.
All matrix and tensor norms below use the fixed Euclidean structure. In particular,
$\|H\|_{\mathrm{HS}}^2=\operatorname{Tr}(H^2)$ and
$\|T\|_{\mathrm{HS}}^2=\sum_{i,j,k}T_{ijk}^2$, summing **ordered** triples.
This is not a sum restricted to $i\le j\le k$, nor an operator norm.

:::{prf:theorem} The three imported conclusions with the regular class expanded
:label: thm:sol-ck-imports
Let $\mu$ be an isotropic log-concave probability law on $\mathbb R^n$.
For the Hessian conclusion assume additionally that $\mu$ has density
$e^{-V}\mathbf1_K$, where $K$ is bounded, open and convex, $V\in C^\infty(K)$
is convex, and $V$ and every partial derivative of every order are bounded on $K$.
Then its moment potential satisfies
$\int\|D^2\psi\|_{\mathrm{HS}}^2e^{-\psi}\,dx\le2n$.
For every isotropic log-concave law, without this additional assumption,
$\operatorname{Var}(|X|^2)\le8n$ and $\|T_3(X)\|_{\mathrm{HS}}^2\le4n$.
Both latter constants are attained by independent centered exponential coordinates.
If $X$ is uniform on an isotropic convex body, then furthermore

$$
\operatorname{Var}(|X|^2)\le\frac{4n(n+1)^2}{(n+3)(n+4)},\qquad
\|T_3(X)\|_{\mathrm{HS}}^2\le\frac{4n(n-1)(n+2)}{(n+3)^2},
$$

with equality for an isotropic regular simplex.
These imply [](#thm:chen-klartag-moment-hessian),
[](#thm:chen-klartag-thin-shell), and [](#thm:chen-klartag-third-moment).
:::

The source regular class does not require a smooth boundary of $K$, strict convexity
of $V$, or a globally smooth density across $\partial K$. A uniform convex-body law
belongs to it, with $V$ constant. Conversely, smooth positive density on all of
$\mathbb R^n$ alone does not satisfy this bounded-target assumption.

## Published inputs and their precise uses

The moment-measure existence theorem [@CorderoErausquinKlartag2015MomentMeasures]
and the regularity theory summarized in Section 1, condition (2), of
[@Klartag2013MomentMeasures] give a smooth strictly convex $\psi$ and a
diffeomorphism $\nabla\psi:\mathbb R^n\to K$ in the stated class.
The latter reference's main Hessian theorem gives
$\operatorname{Tr}H\le2R(K)^2$, where $R(K)=\sup_{y\in K}|y|$.
These assumptions and the bound were checked against the
[author's PDF](https://www.math.tau.ac.il/~klartagb/papers/lc_moment.pdf),
pp. 2–3 (Theorem 1 there; cited as Theorem 1.1 in Chen–Klartag).
This is a published input, not a theorem newly proved here.

The other inputs are Brascamp–Lieb [@BrascampLieb1976] for $\nu$,
$\operatorname{Var}_\nu u\le\int\langle H^{-1}\nabla u,\nabla u\rangle d\nu$,
and Proposition 10 of Barthe–Klartag [@BartheKlartag2019SpectralGaps], checked in the
[author's PDF](https://www.weizmann.ac.il/math/klartag/sites/math.klartag/files/uploads/1907.01823.pdf),
pp. 5–6. That proposition applies to a finite log-concave measure and a locally
Lipschitz $f\in L^2$ with $\partial_i f\in L^2$ and $\int\partial_i f=0$;
it gives $\operatorname{Var}f\le\sum_i\|\partial_i f\|_{H^{-1}}^2$.
We use it only for $f(x)=|x|^2$. Its proof uses the convex Bochner inequality
and density of the range of the weighted Laplacian in centered $L^2$; these
published functional-analytic inputs are not being certified anew here.
Brascamp–Lieb supplies the source's equation (8) directly, so no claim about
stochastic completeness or exact eigenspaces is needed.

## The Hessian estimate, including the integration audit

:::{prf:proof}
Work first in the regular class. Put $\psi^{ab}=(H^{-1})_{ab}$ and

$$
Lu=\psi^{ab}u_{ab}-V_a(\nabla\psi)u_a,\qquad
\Gamma(u,v)=\psi^{ab}u_av_b.
$$

Repeated indices are summed. The cofactor identity for a Hessian,
$\partial_a((\det H)\psi^{ab})=0$, and
$\log\det H=-\psi+V(\nabla\psi)$ imply
$e^\psi\partial_a(e^{-\psi}\psi^{ab})=-V_b(\nabla\psi)$.
Consequently $\int vLu\,d\nu=-\int\Gamma(u,v)d\nu$ if $v$ is compactly supported.
This is a local identity, not yet permission to put $v=1$.

Differentiating the same logarithmic equation twice gives

$$
LH+H=A+Q,\quad A=H(D^2V\circ\nabla\psi)H,\quad
Q_{ij}=\operatorname{Tr}(H^{-1}\partial_iH H^{-1}\partial_jH).
$$

Convexity gives $A\succeq0$; $Q$ is the Gram matrix of the symmetric matrices
$H^{-1/2}\partial_iH H^{-1/2}$, so $Q\succeq0$.
Define

$$
G=\operatorname{Tr}(H^2),\quad d=\sum_{i,j}\Gamma(H_{ij}),\quad
 a=\operatorname{Tr}(HA),\quad q=\operatorname{Tr}(HQ),\quad S=d+a+q.
$$

The product rule yields $LG=2(S-G)$. All three summands of $S$ are nonnegative.
The bounded-Hessian input gives $0\le G\le B<\infty$.
Matrix Cauchy–Schwarz applied to $\partial_aG=2\operatorname{Tr}(H\partial_aH)$
gives $\Gamma(G)\le4Gd\le4BS$.

Here is the noncompact integration justification, before any global energy is
assumed finite. Integrability and convexity of $e^{-\psi}$ imply that $\psi$ has
compact sublevel sets. Indeed an unbounded full-dimensional convex sublevel set
has infinite volume; a bounded sublevel set containing a neighborhood of a
minimizer then gives a linear lower bound outside it by convexity.
Moreover $L\psi=n-\langle\nabla V(\nabla\psi),\nabla\psi\rangle\le C_0$
for some finite nonnegative $C_0$, since $K$ and $\nabla V$ are bounded.
Take a smooth nonincreasing $\eta$ equal to one on $(-\infty,1]$ and zero
on $[2,\infty)$, with values in $[0,1]$, and set $\chi_R=\eta(\psi/R)$.
Set also

$$
b_R(t)=R^{-1}\int_{t/R}^\infty\eta'(s)^2ds.
$$

Both $\chi_R$ and $b_R(\psi)$ have compact support for large $R$.
Compactly supported integration gives

$$
e_R:=\int\Gamma(\chi_R)d\nu
=-\int b_R'(\psi)\Gamma(\psi)d\nu
=\int b_R(\psi)L\psi\,d\nu\le C_0\|\eta'\|_2^2/R.
$$

Also $\chi_R\to1$ pointwise and in $L^2$. Testing $LG=2(S-G)$ against
$\chi_R^2$ and using $\Gamma(G)\le4BS$ yields, with
$U_R=\int\chi_R^2S\,d\nu$,

$$
2U_R\le2B+4\sqrt{B U_R e_R}\le2B+U_R+4Be_R.
$$

Fatou therefore gives $\int S\le2B$. Now the boundary term is at most
$4(B\int S)^{1/2}e_R^{1/2}\to0$. Dominated convergence proves
$\int S=\int G$, not merely an inequality. Write

$$
N=\int G,\qquad D=\int d,\qquad A_0=\int a,\qquad Q_0=\int q;
\qquad N=D+A_0+Q_0. \tag{1}
$$

For any bounded smooth $F$ with finite $\int\Gamma(F)$,

$$
\int\Gamma((1-\chi_R)F)\le
2\int(1-\chi_R)^2\Gamma(F)+2\|F\|_\infty^2e_R\longrightarrow0.
$$

The analogous difference estimate makes $\chi_RF$ Cauchy in the closed-form
norm. Thus Brascamp–Lieb, first applied to $\chi_RF$, passes to $F$.
This applies to every $H_{ij}$ because $D<\infty$ has just been proved.
Ordinary Euclidean cutoffs $\zeta(x/R)$ in
$\int\partial_i(\psi_j e^{-\psi})=0$ justify
$\int H_{ij}=\int\psi_i\psi_j=\delta_{ij}$: the cutoff error is $O(R^{-1})$
since $\nabla\psi$ is bounded, and $H$ is bounded for dominated convergence.
It follows that

$$
N-n=\sum_{i,j}\operatorname{Var}_\nu H_{ij}\le D. \tag{2}
$$

At a fixed point choose a **constant orthogonal coordinate change** diagonalizing
$H$ there, with positive eigenvalues $\lambda_a$. No derivative of an eigenframe
is taken. The above definitions are orthogonal contractions, and become

$$
d=\sum_{a,i,j}\frac{\psi_{aij}^2}{\lambda_a},\qquad
q=\sum_{a,i,j}\frac{\lambda_a\psi_{aij}^2}{\lambda_i\lambda_j}.
$$

The complete symmetry of $D^3\psi$ permits cyclic averaging, including repeated
indices, in the sum over ordered triples:

$$
q-d=\frac16\sum_{a,i,j}\frac{\psi_{aij}^2}{\lambda_a\lambda_i\lambda_j}
\left[(\lambda_a-\lambda_i)^2+(\lambda_i-\lambda_j)^2+
(\lambda_j-\lambda_a)^2\right]\ge0. \tag{3}
$$

Indeed the unaveraged numerator is $\lambda_a^2-\lambda_i\lambda_j$;
its cyclic mean is one sixth of the displayed sum of squares.
Thus (1)–(3) give $N\ge2D\ge2(N-n)$ and hence $N\le2n$.
This verifies the mechanism of source Lemmas 3.1–3.5 and Appendix A.1–A.2,
including the order of the integrability arguments.
:::

## Third tensor and thin shell in the regular class

:::{prf:proof}
Let $M=2R(K)^2$. Since $H\preceq MI$, the now finite $D$ controls
$\int\sum_{a,i,j}\psi_{aij}^2\le MD$. Thus every third derivative is integrable.
Euclidean cutoffs in derivatives of $H_{ij}e^{-\psi}$ give
$\int\psi_{ijk}=\int H_{ij}\psi_k$. The error is bounded by
$\|H\|_\infty\|\nabla\zeta_R\|_\infty$.
Doing the same with $\psi_j\psi_ke^{-\psi}$ gives

$$
T_{ijk}=\int\psi_i\psi_j\psi_k
=\int(H_{ij}\psi_k+H_{ik}\psi_j)
=2\int\psi_{ijk}=2\int(H_{ij}-\delta_{ij})\psi_k.
$$

All integrals here are with respect to $\nu$. Centering justifies the subtraction;
isotropy makes $\psi_1,\ldots,\psi_n$ orthonormal in $L^2(\nu)$.
Bessel's inequality for each $H_{ij}-\delta_{ij}$, followed by summation, gives

$$
\sum_{i,j,k}T_{ijk}^2\le4\sum_{i,j}\int(H_{ij}-\delta_{ij})^2
=4(N-n)\le4n. \tag{4}
$$

This also checks source Lemma 3.7 and Theorem 1.2 without confusing a full
third tensor with a fixed-direction contraction.

For thin shell define $\tau(y)=H((\nabla\psi)^{-1}(y))$ on $K$.
For any smooth compactly supported $g$ on $\mathbb R^n$, Euclidean integration
by parts in the moment coordinates gives

$$
\int y_i g(y)d\mu(y)=\int\psi_i g(\nabla\psi)d\nu
=\int\sum_jH_{ij}\partial_jg(\nabla\psi)d\nu
=\int\sum_j\tau_{ij}\partial_jg\,d\mu. \tag{5}
$$

Although $g\circ\nabla\psi$ need not have compact support, its value is bounded,
its differentiated terms are bounded by the Hessian bound, and the Euclidean
cutoff error is $O(R^{-1})$. Thus (5) is justified.
For centered $h$ use the homogeneous norm

$$
\|h\|_{H^{-1}(\mu)}=
\sup\{\int hg\,d\mu:g\in C_c^\infty(\mathbb R^n),\ \int|\nabla g|^2d\mu\le1\}.
$$

Rowwise Cauchy–Schwarz in (5) gives
$\|y_i\|_{H^{-1}}^2\le\int\sum_j\tau_{ij}^2d\mu$, hence
$\sum_i\|y_i\|_{H^{-1}}^2\le N\le2n$.
The norm convention agrees with the published negative-Sobolev inequality:
smooth Sobolev tests can be approximated by ambient compactly supported smooth
tests on this bounded convex target; its density is bounded above and below.
Apply Proposition 10 of Barthe–Klartag to $f(y)=|y|^2$.
Here $f$ and its derivatives are square-integrable, and
$\int\partial_i f\,d\mu=2\int y_i d\mu=0$.
It follows that

$$
\operatorname{Var}_\mu(|y|^2)\le4\sum_i\|y_i\|_{H^{-1}(\mu)}^2\le8n. \tag{6}
$$

These are source equation (23), Theorem 1.4 and the deduction of Theorem 1.1.
:::

## Approximation and exact boundary examples

:::{prf:proof}
Let $X$ now have an arbitrary isotropic log-concave law $\mu$. Its finite fourth
moment follows from the standard exponential-tail property of a full-dimensional
integrable log-concave density. For $\delta,\varepsilon>0$ and finite $R$ consider

$$
f_{\delta,\varepsilon,R}(x)=c_{\delta,\varepsilon,R}
\mathbf1_{B(0,R)}(x)e^{-\varepsilon|x|^2/2}(\mu*\gamma_\delta)(x),
\qquad \gamma_\delta=N(0,\delta I).
$$

The convolution has a positive smooth log-concave density. On the closed ball,
its logarithm and each derivative are bounded, since the density has a positive
minimum and its derivatives are continuous. Thus the potential inside the ball
is smooth convex (indeed uniformly convex after the Gaussian factor), with all
required bounds. No claim is made that these bounds are uniform in the parameters.

To justify a diagonal sequence, first choose $\delta\downarrow0$. On a common
space $X+\sqrt\delta Z\to X$ in $L^4$, so all mixed moments of degree at most four
converge. For each chosen $\delta$, dominated convergence for the integrable weight
$1+|x|^4$ allows $\varepsilon\downarrow0$ and $R\uparrow\infty$ so that normalized
truncation and multiplication change these finitely many moments by an arbitrarily
small amount. Normalizing constants tend to one. This constructs a sequence with
means $m_r\to0$ and covariances $C_r\to I$.
The densities are positive on balls, so $C_r$ is positive definite. The affine
images $C_r^{-1/2}(X_r-m_r)$ are isotropic and remain in the regular class on
ellipsoids; each derivative remains bounded for each fixed $r$.
Since $C_r^{-1/2}\to I$, expansion of each polynomial shows convergence of every
mixed moment of degree at most four after this normalization.

Both sides of (4) and (6) are polynomials in these finitely many moments.
Their limits therefore give the general assertions. This is the approximation
at the end of source Section 3. In particular, it does not require convergence of
moment-map Hessians or their squares. The source also passes the summed $H^{-1}$
bound to the limit; one can check that passage directly from

$$
\sum_i\|x_i\|_{H^{-1}(\mu)}^2
=\sup_{g_1,\ldots,g_n\in C_c^\infty}
\sum_i\left(2\int x_i g_i\,d\mu-\int|\nabla g_i|^2d\mu\right).
$$

Each fixed tuple defines a continuous functional of weak convergence, because
its integrands are bounded continuous. Their supremum is lower semicontinuous.
This verifies that step without using the recent Klartag–Lehec preprint cited
there. It is optional for the moment-based limit proof above.

For constants let $E$ have density $e^{-s}\mathbf1_{s>0}$ and $Z=E-1$.
Integration by parts gives $\mathbb EE^r=r!$. Hence
$\mathbb EZ=0$, $\mathbb EZ^2=1$, $\mathbb EZ^3=2$, $\mathbb EZ^4=9$.
For independent copies, mixed third moments vanish unless all indices agree,
and the squares are independent. Thus the third-tensor squared norm is $4n$
and the radial variance is $n(9-1)=8n$.
Their moment potential can also be computed directly:
$\psi(t)=\sum_i(e^{t_i}-t_i)$, $H=\operatorname{diag}(e^{t_i})$.
The substitution $s_i=e^{t_i}$ makes $\nu$ a product of exponential measures
in $s_i$, giving $\int\operatorname{Tr}H^2=2n$.
This explicit Hessian example has unbounded target and unbounded Hessian.
It is a boundary calibration, not an admissible invocation of the regular-class
Hessian theorem. No uniqueness classification of equality is asserted.
:::

## Convex bodies and the simplex clause

:::{prf:proof}
Let $X$ be uniform isotropic in a convex body in dimension $n$, and put $k=n+1$.
Independently take $G$ with Gamma$(k,1)$ density and set

$$
Y=\left(\frac{GX}{\sqrt{k(k+1)}},\frac{G-k}{\sqrt k}\right).
$$

The change $(x,s)\mapsto(sx,s)$ has Jacobian $s^n$. Consequently $(GX,G)$ has
density proportional to $e^{-s}$ on a convex cone, and $Y$ is log-concave.
The Gamma moments $\mathbb EG^r=k(k+1)\cdots(k+r-1)$ and isotropy of $X$
give $\mathbb EY=0$ and $\mathbb EYY^T=I_k$.
Write $v=\operatorname{Var}(|X|^2)$. Squaring
$|Y|^2=G^2|X|^2/[k(k+1)]+(G-k)^2/k$ gives

$$
\mathbb E|Y|^4=
\frac{(k+2)(k+3)}{k(k+1)}[v+(k-1)^2]
+\frac{2(k-1)(k+6)}k+\frac{3(k+2)}k.
$$

Here the cross moment is $\mathbb E[G^2(G-k)^2]=k(k+1)(k+6)$ and
$\mathbb E(G-k)^4=3k(k+2)$, both obtained by expanding the Gamma moments.
Subtracting $k^2$ yields

$$
\operatorname{Var}(|Y|^2)=\frac{k+3}{k(k+1)}[(k+2)v+4k^2].
$$

For $i,j,\ell<k$ the third moments are

$$
T(Y)_{ij\ell}=\frac{k+2}{\sqrt{k(k+1)}}T(X)_{ij\ell},\quad
T(Y)_{ijk}=\frac2{\sqrt k}\delta_{ij},\quad
T(Y)_{ikk}=0,\quad T(Y)_{kkk}=\frac2{\sqrt k}.
$$

Accounting for all three placements of the final index gives
$\|T(Y)\|_{\mathrm{HS}}^2=(k+2)^2\|T(X)\|_{\mathrm{HS}}^2/[k(k+1)]+12-8/k$.
Apply the general bounds in dimension $k$ and solve these two affine inequalities
for $v$ and $\|T(X)\|^2$. The constants in the theorem follow. This verifies
source Lemma 4.2 and the deduction of Corollary 1.3.

For the equality assertion, let $v_1,\ldots,v_k$ be the vertices of a centered
isotropic simplex. The change of variables from independent exponentials
$E_1,\ldots,E_k$ to their sum $G$ and proportions has Jacobian $G^{k-1}$.
Its density factors into the Gamma density and constant density on the standard
simplex. Thus the proportions are independent of $G$, and
$X=\sum_r(E_r/G)v_r$ has the required uniform law.
The displayed $Y$ is then $B(E-\mathbf1)$, where the $r$th column of $B$ is
$(v_r/\sqrt{k(k+1)},1/\sqrt k)$. Both random vectors are isotropic, so
$BB^T=I_k$, and the square matrix $B$ is orthogonal. Orthogonal invariance of
$|Y|$ and of the full tensor norm transfers both exponential equalities to $Y$.
The exact cone identities then force equality in both convex-body bounds.
For $n=1$ this gives tensor zero for the centered uniform interval, as required.
:::

## Hypothesis usage, limits, and handoff

| Hypothesis or input | Where it is used | What is not licensed without it |
|---|---|---|
| Centered full-dimensional target | Moment measure and zero means | Isotropy cannot be imposed on a singular ambient covariance |
| Covariance $I$ | $\int H=I$, orthonormal $\psi_i$, subtraction of $n$ | Unnormalized covariance versions with unchanged constants |
| Bounded open convex $K$ and bounded smooth $V$ with all derivatives bounded | Published regularity and Hessian bound; bounded $\nabla\psi$; $L\psi\le C_0$ | Global integrations based only on formal smoothness |
| Convex $V$ | $A\succeq0$ and log-concave approximation | The bootstrap for non-log-concave targets |
| Complete symmetry of $D^3\psi$ | Cyclic identity (3) | A corresponding inequality for an arbitrary three-index array |
| Brascamp–Lieb and finite entrywise energy | (2), after cutoff closure | Entrywise Poincaré before energy has been controlled |
| Centered derivatives in Barthe–Klartag | $f=|x|^2$ in (6) | The same reduction for arbitrary noncentered derivatives |
| Fourth-moment convergence | General thin-shell limit | Passage from weak convergence alone of the fourth moment |

The Hessian bottleneck is precisely $N-n\le D\le N/2$. The thin-shell mechanism
is Stein row control followed by the negative-Sobolev inequality; it does not give
a Poincaré bound for arbitrary functions. The tensor mechanism is Bessel applied
to centered Hessian entries; it produces a summed Euclidean norm. In particular
$\sum_{i,j,k}T_{ijk}^2\le4n$ does not yield the conjectural directional bound $2$
or a Loewner bound $\mathbb E H^2\preceq2I$.

**Fences respected.** None of the three ledger nodes has a `bounded_by` entry.
The two child nodes name the Hessian node in `depends_on`; the proof above supplies
that parent within the same dossier. There are no `assumes` antecedents.
The brief's thin-shell/KLS distinction and trace/operator distinction are respected;
no CMH, gate-zero, or KLS claim is inferred. Exponential examples outside the regular
class are treated explicitly rather than used to justify a regular-class argument.
Isotropic laws have full affine support; if discussing a singular law one must first
work on its affine hull, with its intrinsic dimension. No singular ambient whitening
is used in the approximation above.

**Dependencies actually used.** The only internal mathematical parent is
`thm:chen-klartag-moment-hessian` for the two consequences, proved above rather than
assumed open. External inputs are moment-measure existence, the published compact-target
regularity and bounded-Hessian theorem, Brascamp–Lieb, Barthe–Klartag Proposition 10,
and standard log-concavity under convolution and affine maps and finite moments.
No Letwin import, Klartag–Lehec import, CMH assumption, or other draft dossier is used.
Source Appendix A and the cone/equality arguments have been expanded above.

**Unresolved issues.** No unclosed step in the three claimed conclusions is asserted
by this author. The published inputs are identified rather than reproved from first
principles. This is not an independent review. In particular, extension of the
Hessian-square bound itself to arbitrary nonsmooth moment maps is not claimed or
needed. The general conclusions established by approximation are the moment inequalities.
No manuscript, ledger, bibliography or other dossier changes are proposed.
