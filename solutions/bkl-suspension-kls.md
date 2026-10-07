---
title: 'BKL: suspension, uniform coefficients and KLS'
ledger-node: [prop:bkl-suspension, thm:bkl-tilt-bound, conj:kls]
numbering:
  enumerator: '135.%s'
---

*Part of the Bizeul–Klartag–Lehec proof, Chapter [](#sec:bkl-proof); the reading order is on the [full proofs](#sec:proofs-bkl) page.*

**Author.** `bkl_suspension_author, gpt-6-astra, 2026-10-06` (researcher).

**Overview.** We reconstruct [@BizeulKlartagLehec2026KLS, Section 7]. A
log-concave suspension places an arbitrary smooth affine-orthogonal test in
one additional coordinate. Replicating the original coordinates makes the
curvature cost arbitrarily small. A cumulant contraction then bounds the
Taylor tensor. We supply the density argument, treat the affine component,
and extend the resulting coefficient bound to every covariance contraction,
including measures supported on proper subspaces. The spectral criterion is
used only after the coefficient estimate has been established.

**Dependencies.** The conventions are [](#def:bkl-tilt-cumulants). The
suspension implication itself uses no spectral-gap theorem. Its application
uses [](#thm:bkl-cumulant-bound). Approximation with convergence of all
polynomial moments and scalar Poincaré stability use
[](#lem:bkl-analytic-foundations). The final KLS conclusion uses
[](#thm:bkl-tilt-criterion). None of the Song–Zhang KLS theorem, the
exponential-coefficient equivalence, CMH, or an occupation hypothesis is
used. These are exact interfaces; their proof dossiers require independent
certification along with this dossier.

:::{prf:theorem} Suspension implication
:label: thm:sol-bkl-suspension
Fix an integer $d\ge2$ and $b>0$. Suppose that every isotropic log-concave
probability $\nu$ in every finite dimension satisfies
$R_{d+1}^{\nu}\preceq bI$. Then, for every regular isotropic log-concave
probability $\mu$ and every real $f\in L^2(\mu)$,

$$
|\mathcal T_d^\mu f|^2\le \frac{2b}{(d!)^2}\|f\|_2^2.
$$

Here $F_f(z)=\int fe^{\langle z,x\rangle}\,d\mu(x)/
\int e^{\langle z,x\rangle}\,d\mu(x)$,
$\mathcal T_df=\nabla^dF_f(0)/d!$, and
$\langle R_k^\nu v,v\rangle=|\kappa_k^\nu(v,\cdot,\ldots,\cdot)|^2$.
All tensor norms sum over all ordered indices. This proves the implication
[](#prop:bkl-suspension), without asserting its premise on its own.
:::

:::{prf:proof}
Write $d\mu=e^{-V}dx$ and $D^2V\succeq aI$ with $a>0$. Initially suppose
$f$ is smooth, has bounded Hessian, and satisfies

$$
\int f\,d\mu=0,\qquad \int f^2\,d\mu=1,\qquad
\int xf(x)\,d\mu(x)=0.
$$

For $\beta>0$, take independent $X_1,\ldots,X_N$ of law $\mu$ and an
independent real variable $\eta_\beta$ of density
$(\beta/2)e^{-\beta|t|}$. Put

$$
F_N=N^{-1/2}\sum_i f(X_i),\qquad
\sigma_\beta^2=1+2\beta^{-2},\qquad
S=(F_N+\eta_\beta)/\sigma_\beta.
$$

The law $\nu$ of $(S,X_1,\ldots,X_N)$ has potential, up to a constant,

$$
W(s,x_1,\ldots,x_N)=\sum_iV(x_i)+
\beta\left|\sigma_\beta s-N^{-1/2}\sum_i f(x_i)\right|.
$$

Choose an integer $N$ so large that
$\beta N^{-1/2}\sup_x\|D^2f(x)\|_{\rm op}\le a$.
The displayed potential is the maximum of the two convex functions

$$
\sum_i\bigl(V(x_i)\pm\beta N^{-1/2}f(x_i)\bigr)
\mp\beta\sigma_\beta s.
$$

Thus $\nu$ is log-concave, although regularity of $\nu$ is not claimed or
needed. Independence and the three normalizations give
$\mathbb ES=0$, $\mathbb ES^2=1$,
$\mathbb ESX_i=0$, and $\operatorname{Cov}(X_i,X_j)=\delta_{ij}I$.
Consequently $\nu$ is isotropic.

Bounded Hessian gives $|f(x)|\le C(1+|x|^2)$; strong convexity gives
$V(x)\ge a|x|^2/2-C(1+|x|)$. Hence the joint Laplace transform is finite
in a neighborhood of the origin: the coefficient of each quadratic term
from $w f/(\sigma_\beta\sqrt N)$ is absorbed by $a|x|^2/2$, and the
Laplace variable of $\eta_\beta$ has modulus less than $\beta$ there.
These bounds, with slightly enlarged parameters, dominate every finite
number of derivatives, so differentiation under the integrals is valid.
For the logarithmic Laplace transform $\Lambda$ of $\nu$, independence
and $\mathbb E\eta_\beta=0$ give

$$
\partial_w\Lambda(0,z_1,\ldots,z_N)
=\frac1{\sigma_\beta\sqrt N}\sum_{i=1}^N F_f(z_i).
$$

Let index $0$ denote $S$, and $(i,j)$ denote coordinate $j$ of $X_i$.
Differentiating $d$ more times yields

$$
\kappa_{d+1}^\nu{}_{0,(i_1,j_1),\ldots,(i_d,j_d)}
=\begin{cases}
\dfrac{d!}{\sigma_\beta\sqrt N}(\mathcal T_df)_{j_1,\ldots,j_d},
 &i_1=\cdots=i_d,\\
0,&\text{otherwise}.
\end{cases}
$$

The $N$ indicated tensor blocks have disjoint ordered-index supports.
Entries involving another index $0$ form an orthogonal residual tensor
$U$, so

$$
|\kappa_{d+1}^\nu(e_0)|^2
=\frac{(d!)^2}{\sigma_\beta^2N}\sum_{i=1}^N|\mathcal T_df|^2+|U|^2
\ge\frac{(d!)^2}{\sigma_\beta^2}|\mathcal T_df|^2.
$$

The assumed bound in dimension $Nn+1$ makes the left side at most $b$.
This holds for each $\beta$, with a possibly different $N$, and the
quantity $\mathcal T_df$ does not depend on either parameter. Taking the
infimum over $\beta>0$ proves $|\mathcal T_df|\le\sqrt b/d!$.
No limit of the suspension measures is taken.

We justify passage to all affine-orthogonal tests. For each fixed ordered
index $J$ of length $d$, differentiation of the quotient at zero writes
$(\mathcal T_df)_J=\int f p_J\,d\mu$, where $p_J$ is a polynomial of
degree at most $d$ whose coefficients are finite combinations of moments
of $\mu$. Gaussian tails imply $p_J\in L^2(\mu)$. Thus
$\mathcal T_d:L^2(\mu)\to(\mathbb R^n)^{\otimes d}$ is continuous
at this fixed measure and degree, with no uniform bound assumed.

Let $h$ be a unit vector in the orthogonal complement of the affine
functions. Choose $g_j\in C_c^\infty$ with $g_j\to h$ in $L^2(\mu)$.
This density follows by first truncating the function and its support,
then approximating on compact sets, where the smooth positive density is
bounded above and below. The orthogonal projection onto the affine
functions is explicitly

$$
Pg=\int g\,d\mu+\left\langle\int xg(x)\,d\mu(x),x\right\rangle.
$$

It is bounded since $1,x_1,\ldots,x_n$ are orthonormal. Hence
$g_j-Pg_j\to h$, its norm tends to one, and its Hessian is the Hessian of
$g_j$, therefore bounded. Normalize these functions for all sufficiently
large $j$ and pass through the continuous map $\mathcal T_d$.
We obtain $|\mathcal T_dh|\le\sqrt b/d!$, and by homogeneity the same
bound multiplied by $\|h\|_2$ for every affine-orthogonal $h$.

For a linear function $\ell(x)=\langle v,x\rangle$, isotropy gives
$\|\ell\|_2=|v|$, and

$$
F_\ell(z)=\langle v,\nabla\Lambda_\mu(z)\rangle,
\qquad \mathcal T_d\ell=\kappa_{d+1}^\mu(v)/d!.
$$

The same cumulant premise gives
$|\mathcal T_d\ell|\le\sqrt b\|\ell\|_2/d!$.
For $f=c+\ell+h$ its orthogonal affine decomposition, constants have
$\mathcal T_dc=0$ and consequently

$$
|\mathcal T_df|\le\frac{\sqrt b}{d!}(\|\ell\|_2+\|h\|_2)
\le\frac{\sqrt{2b}}{d!}\sqrt{\|\ell\|_2^2+\|h\|_2^2}
\le\frac{\sqrt{2b}}{d!}\|f\|_2.
$$

This completes the suspension implication.
:::

:::{prf:theorem} Uniform coefficients, including singular covariance contractions
:label: thm:sol-bkl-global-tilt
Let $K\ge1$ be the universal constant in [](#thm:bkl-cumulant-bound),
so $R_{d+1}^\nu\preceq K^d(d!)^2I$ for every isotropic log-concave
$\nu$ and every integer $d\ge2$. Set $A=\sqrt{2K}$.
For every centered log-concave probability $\mu$ in every dimension with
$\operatorname{Cov}(\mu)\preceq I$, every integer $d\ge1$, and every
$f\in L^2(\mu)$,

$$
|\mathcal T_d^\mu f|\le A^d\|f\|_2.
$$

Equivalently the symmetric Appell coefficient obeys
$c_d(\mu)=\sqrt{K_d(\mu)}/d!\le A^d$, with
$K_d(\mu)=\sup_{T=T^{\rm sym},\,|T|=1}
\operatorname{Var}_\mu P_d^\mu[T]$. This is [](#thm:bkl-tilt-bound).
:::

:::{prf:proof}
For regular isotropic $\mu$ and $d\ge2$ the suspension theorem gives
$|\mathcal T_df|^2\le2K^d\|f\|_2^2\le(2K)^d\|f\|_2^2$.
For $d=1$,

$$
|\mathcal T_1f|=\sup_{|v|=1}\left|\int\langle v,x\rangle f\,d\mu\right|
\le\|f\|_2
$$

by isotropy and Cauchy–Schwarz.

We give the precise duality needed to pass through approximation. In a
neighborhood of zero the Appell generating identity is

$$
e^{\langle z,x\rangle-\Lambda_\mu(z)}
=\sum_{d\ge0}\frac1{d!}\langle P_d^\mu(x),z^{\otimes d}\rangle.
$$

Differentiating at zero and integrating shows
$\mathbb EP_d^\mu=0$ for $d\ge1$, and

$$
\langle\mathcal T_df,T\rangle
=\frac1{d!}\int fP_d^\mu[T]\,d\mu.
$$

All entries are polynomial moment identities; hence they also define the
same tensors without any complex-analytic convention. Taking first the
supremum over unit $f\in L^2(\mu)$ and then over unit symmetric $T$ shows

$$
\|\mathcal T_d\|_{L^2\to\mathrm{HS}}^2
=\frac1{(d!)^2}\sup_{|T|=1,\,T=T^{\rm sym}}
\int(P_d^\mu[T])^2\,d\mu=c_d(\mu)^2.
$$

Restricting to symmetric tensors loses nothing because $\mathcal T_df$
is symmetric and orthogonal projection onto that subspace decreases norm.

Now take an arbitrary isotropic log-concave $\mu$ and regular isotropic
$\mu_j$ converging weakly and in every polynomial moment, furnished by
[](#lem:bkl-analytic-foundations). For fixed $d$ and $T$,
$P_d^{\mu_j}[T]$ is a polynomial in $x$ of degree at most $d$ whose
coefficients are polynomial expressions in moments of order at most $d$.
This follows directly by formal inversion of the Laplace series, whose
constant term is one. Its coefficients therefore converge to those of
$P_d^\mu[T]$. The square has degree at most $2d$; moment convergence then
gives

$$
\int(P_d^\mu[T])^2\,d\mu
=\lim_j\int(P_d^{\mu_j}[T])^2\,d\mu_j
\le(d!)^2A^{2d}|T|^2.
$$

This is for every $T$, with the same constant. Taking its supremum gives
$c_d(\mu)\le A^d$. No convergence of suprema or of varying test functions
is asserted. Duality returns the bound for every $f\in L^2(\mu)$.
For such $f$ its tilted integral is indeed defined near zero: a log-concave
law on its linear support has an exponential moment in some neighborhood
of zero, and Cauchy–Schwarz controls
$\int |f|e^{\langle z,x\rangle}d\mu$ by
$\|f\|_2(\int e^{2\langle z,x\rangle}d\mu)^{1/2}$.
The same estimate with polynomial factors justifies its finite derivatives.

Finally let $C=\operatorname{Cov}(\mu)\preceq I$ be possibly singular and
put $E=\operatorname{ran}C$. Centering implies $X\in E$ almost surely:
for each $v\in\ker C$, $\mathbb E\langle v,X\rangle^2=0$.
If $E=\{0\}$, the law is a point mass and all positive-degree Taylor
coefficients vanish. Otherwise $C_E$ is positive definite on $E$, and
$Y=C_E^{-1/2}X$ is isotropic log-concave on $E$. Write
$B:E\to\mathbb R^n$ for the inclusion composed with $C_E^{1/2}$.
Then $X=BY$ and $\|B\|_{\rm op}\le1$. For $g(y)=f(By)$,
$\|g\|_{L^2(Y)}=\|f\|_{L^2(X)}$ and

$$
F_f^\mu(z)=F_g^{\mathcal L(Y)}(B^*z),\qquad
\mathcal T_d^\mu f=B^{\otimes d}\mathcal T_d^{\mathcal L(Y)}g.
$$

The ordered-index Hilbert–Schmidt tensor norm satisfies
$\|B^{\otimes d}\|_{\rm op}=\|B\|_{\rm op}^d\le1$
(for example, diagonalize $B^*B$ on $E$).
This proves the claimed estimate and then its equivalent coefficient bound
for every covariance contraction. All arguments up to this point are
independent of KLS.
:::

:::{prf:theorem} KLS from the reconstructed BKL chain
:label: thm:sol-bkl-kls
There is a finite universal constant $C_*$ such that every isotropic
log-concave probability $\mu$ in every dimension satisfies

$$
\operatorname{Var}_\mu f\le C_*\int|\nabla f|^2\,d\mu
$$

for every locally Lipschitz $f$, with the finite-energy interpretation
specified in [](#lem:bkl-analytic-foundations). This is [](#conj:kls).
:::

:::{prf:proof}
For a regular isotropic $\mu$, the preceding theorem supplies simultaneously
in every degree the hypothesis of [](#thm:bkl-tilt-criterion), with
$R=A=\sqrt{2K}$. If $C$ is the universal constant of that criterion, it
gives $C_P(\mu)\le CA^2=2CK$.

For arbitrary isotropic log-concave $\mu$, take regular isotropic
$\mu_j\Rightarrow\mu$ as above. For fixed $q\in C_c^\infty$, the
functions $q$, $q^2$ and $|\nabla q|^2$ are bounded continuous, so their
integrals converge and yield
$\operatorname{Var}_\mu q\le2CK\int|\nabla q|^2d\mu$.
The scalar stability clause of [](#lem:bkl-analytic-foundations) extends
this inequality to every locally Lipschitz finite-energy $f$, including
its $L^2$ integrability. The infinite-energy case has no finite upper-bound
assertion. Thus $C_*=2CK$ is universal.
:::

**Fences respected.** These nodes have no additional `bounded_by` edges.
The circularity fence [](#rem:profile-circularity) is respected because no
moving-competitor profile is used. The ceiling distinction
[](#rem:relative-ceiling) is respected: no covariance-time converse is
asserted. The projection barrier [](#rem:projection-ceiling) is respected
because the suspension controls the full ordered-index tensor norm, not
only diagonal directional evaluations. [](#rem:crude-insufficient) is not
used or upgraded. No CMH, sharp gate-zero, occupation, or Song–Zhang
bounded-loss antecedent is discharged by this proof.
