---
title: 'BK: approximation with covariance and curvature control'
ledger-node: lem:bk-regular-approximation
numbering:
  enumerator: "150.%s"
---

*Part of the Balasubramanian–Kasiviswanathan proof, Chapter [](#sec:bk-proof); the reading order is on the [full proofs](#sec:proofs-bk) page.*

**Overview.** Gaussian convolution preserves a quantitative lower curvature
bound while supplying an upper bound. A small quadratic tilt followed by
whitening produces regular isotropic approximants. Moment convergence controls
fixed-degree Appell expressions. Finally, mollification, spatial cutoffs and
value truncations pass a common Poincaré bound to all locally Lipschitz
finite-energy tests, including square integrability.
This reconstructs Appendix F of [@BalasubramanianKasiviswanathan2026KLS],
commit `4837c33649ba2271f43c9684e9350ecbdd725f95`.

**Dependencies.** Regularity means precisely
[](#def:bk-compatible-calculus), and the Appell convention is
[](#def:bk-uniform-appell-coefficients). We use the classical Prékopa theorem
that marginals of log-concave functions are log-concave, standard
mollification and the Lipschitz chain rule. No Poincaré bound for a general
log-concave law is assumed; the weak-limit conclusion has a common bound as
its explicit premise. No BKL, SZ v2, or KLS theorem is used.

:::{prf:theorem} Approximation and passage of scalar inequalities
:label: thm:sol-bk-approximation
Let $\mu$ be a centered full-dimensional log-concave law with covariance at
most $I$ and curvature at least $aI$, $0<a\le1$. For independent
$X\sim\mu$ and standard Gaussian $G$, the laws
$$\mu_\varepsilon=\mathcal L((X+\sqrt\varepsilon G)/\sqrt{1+\varepsilon})$$
are centered and regular, with covariance at most $I$ and curvature at least
$aI$. They converge weakly and in all fixed moments to $\mu$.
Every isotropic log-concave law is likewise a weak and fixed-moment limit of
regular isotropic laws. Under these moment convergences, in a fixed dimension
and degree, Appell coefficient norms and integrals of squared derivatives of
Appell polynomials with fixed leading tensors converge.
If full-dimensional log-concave laws $\nu_j$ converge weakly to a
full-dimensional log-concave law $\nu$ and satisfy a common Poincaré bound
$K<\infty$, then that bound holds for every real locally Lipschitz function
on $\mathbb R^n$ with finite Dirichlet energy under $\nu$, and each such
function belongs to $L^2(\nu)$.
This gives [](#lem:bk-regular-approximation); affine supports are handled by
working in their own Euclidean coordinates.
:::

:::{prf:proof}
**Moments.** A full-dimensional log-concave law has exponentially decaying
coordinate tails. To see this directly, Prékopa applied to the density times
$\mathbf1_{\{x_i\ge t\}}$ shows that the survival function $F_i(t)$ is
log-concave. For an unbounded upper tail, choose $b>c$ with
$0<F_i(b)<F_i(c)$. Concavity of $\log F_i$ gives for $t\ge b$
$$F_i(t)\le F_i(c)
\exp\left(\frac{t-c}{b-c}\log\frac{F_i(b)}{F_i(c)}\right).$$
For a bounded upper tail a bound is immediate. Apply the same argument to
$-X_i$ and use the finite-coordinate union bound for $|X|>t$.
Integrating $kt^{k-1}\mathbb P(|X|>t)$ proves $\mathbb E|X|^k<\infty$
for every real $k>0$. The same holds on a proper affine support by using
coordinates there.

**Convolution curvature.** More generally let a full-dimensional law have
curvature at least $aI$ with $a\ge0$, meaning its density is proportional to
$\exp(-a|y|^2/2-W(y))$ for an extended-real convex function $W$.
The law of $X+\sqrt\varepsilon G$ has strictly positive density
$$\rho_\varepsilon(x)=(2\pi\varepsilon)^{-n/2}
\int\exp(-|x-y|^2/(2\varepsilon))\,d\mu(y).$$
Every derivative of the Gaussian kernel is bounded, uniformly in its
argument, so differentiation under the probability integral shows
$\rho_\varepsilon$ is smooth. The completion of squares
$$\frac a2|y|^2+\frac{|x-y|^2}{2\varepsilon}
=\frac{a|x|^2}{2(1+a\varepsilon)}
+\frac{1+a\varepsilon}{2\varepsilon}
\left|y-\frac{x}{1+a\varepsilon}\right|^2$$
expresses $\rho_\varepsilon(x)$ as
$\exp[-a|x|^2/(2(1+a\varepsilon))]$ times a log-concave function of $x$:
the residual integrand is jointly log-concave in $(x,y)$ and Prékopa applies.
Thus $V_\varepsilon=-\log\rho_\varepsilon$ has
$D^2V_\varepsilon\succeq a(1+a\varepsilon)^{-1}I$.

For the upper bound let $\pi_{\varepsilon,x}$ be the probability law with
density proportional to $\exp[-|x-y|^2/(2\varepsilon)]$ relative to $\mu$.
Differentiation of its mean gives
$$D^2V_\varepsilon(x)=\varepsilon^{-1}I
-\varepsilon^{-2}\operatorname{Cov}(\pi_{\varepsilon,x})
\preceq\varepsilon^{-1}I.$$
All derivatives are legitimate: a polynomial in $y$ times this Gaussian
kernel is bounded in $y$, locally uniformly in $x$.
After dividing the random vector by $\sqrt{1+\varepsilon}$, covariance
becomes $(\operatorname{Cov}\mu+\varepsilon I)/(1+\varepsilon)\preceq I$
and the Hessian bounds become
$$\frac{a(1+\varepsilon)}{1+a\varepsilon}I
\preceq D^2V_{\mu_\varepsilon}
\preceq\frac{1+\varepsilon}{\varepsilon}I.$$
For $0<a\le1$ the lower bound is at least $aI$, proving regularity.
In the common coupling, $X+\sqrt\varepsilon G\to X$ almost surely and
for $0<\varepsilon\le1$,
$$|X+\sqrt\varepsilon G|^k\le
2^{\max\{k-1,0\}}(|X|^k+|G|^k).$$
Dominated convergence proves weak convergence, convergence of every
polynomial moment, and convergence of all absolute moments. The extra scale
tends to one and preserves these conclusions.

**Isotropic approximants.** For isotropic $X$ put
$\varepsilon_j=\delta_j=1/j$, $X_j=X+\sqrt{\varepsilon_j}G$, and define
$$d\nu_j(x)=Z_j^{-1}e^{-\delta_j|x|^2/2}\rho_{\varepsilon_j}(x)\,dx,
\qquad Z_j=\mathbb E e^{-\delta_j|X_j|^2/2}.$$
Its smooth potential $W_j$ has
$\delta_jI\preceq D^2W_j\preceq(\delta_j+\varepsilon_j^{-1})I$.
The same coupling gives $Z_j\to1$ and weak and all fixed-moment convergence
of $\nu_j$ to $\mu$ by dominated convergence. In particular its mean $m_j$
and covariance $S_j$ satisfy $m_j\to0$, $S_j\to I$. Every $S_j$ is
positive definite because the density of $\nu_j$ is strictly positive.
Let $\mu_j$ be its image under $x\mapsto S_j^{-1/2}(x-m_j)$. This is
isotropic, and its potential is $W_j(m_j+S_j^{1/2}y)$ up to a constant.
Its Hessian therefore lies between
$\delta_j\lambda_{\min}(S_j)I$ and
$(\delta_j+\varepsilon_j^{-1})\lambda_{\max}(S_j)I$.
These bounds are strictly positive and finite, so $\mu_j$ is regular.
Since $S_j^{-1/2}\to I$ and $m_j\to0$, the coupling proves weak convergence.
For each fixed $k>0$, the quantities
$|S_j^{-1/2}(X_j-m_j)|^k$ are bounded by an integrable constant multiple
of $1+|X|^k+|G|^k$, uniformly in $j$. Thus every fixed moment converges too.

**Appell limits.** In a fixed dimension, each coefficient of the degree-$d$
Appell tensor is a polynomial in moments of orders at most $d$: invert the
formal moment generating series, whose constant coefficient is one, recursively
by degree. Hence moment convergence implies coefficientwise convergence of
these polynomials and all their spatial derivatives. Integrating any product
of two such polynomials uses only finitely many further moments, all
convergent here. In an orthonormal basis of $\operatorname{Sym}^d\mathbb R^n$,
the Gram matrix of the normalized Appell polynomials therefore converges
entrywise. Its largest eigenvalue is $c_d(\mu_j)^2$, so continuity of the
largest eigenvalue proves convergence of the coefficient norms. The same
finite expansion proves convergence of squared derivative norms for any
fixed tensor and derivative order, including mixed Gram entries.

**Weak limits and test functions.** For $u\in C_c^\infty$, the functions
$u,u^2,|\nabla u|^2$ are bounded and continuous. Weak convergence therefore
passes $\operatorname{Var}_{\nu_j}u\le K\int|\nabla u|^2d\nu_j$ to $\nu$.
A full-dimensional log-concave law is absolutely continuous, so it remains
to justify the extension from smooth compact tests for an absolutely
continuous probability measure.

First let $u$ be compactly supported Lipschitz. Its standard mollifications
$u_\varepsilon$ converge uniformly to $u$, their gradients are uniformly
bounded by its Lipschitz constant, and those gradients converge Lebesgue
almost everywhere to $\nabla u$ by differentiation of convolutions.
Absolute continuity and dominated convergence pass the inequality to $u$.
Next let $h$ be bounded and locally Lipschitz with finite energy. Choose
$0\le\chi\le1$ smooth, compactly supported, and equal to one on the unit
ball, and set $h_R(x)=\chi(x/R)h(x)$. These are compactly supported Lipschitz;
$h_R\to h$ in $L^2(\nu)$ and
$$\nabla h_R-\nabla h=(\chi(x/R)-1)\nabla h
+R^{-1}h\nabla\chi(x/R)\longrightarrow0\quad\text{in }L^2(\nu).$$
The first term converges by dominated convergence and the second has norm
at most $R^{-1}\|h\|_\infty\|\nabla\chi\|_\infty$.
Thus the inequality holds for such $h$.

Finally let $f$ be locally Lipschitz with energy
$E=\int|\nabla f|^2d\nu<\infty$, without assuming integrability of $f$.
Its truncations $f_N=\max(-N,\min(f,N))$ satisfy
$\operatorname{Var}_\nu f_N\le KE$ by the chain rule. Choose $b<\infty$
such that $A=\{|f|\le b\}$ has probability $p>0$. For $N\ge b$ write
$m_N=\int f_Nd\nu$. Since $f_N=f$ on $A$,
$$p(|m_N|-b)_+^2\le\int_A|f_N-m_N|^2d\nu\le KE.$$
Consequently
$$\int f_N^2d\nu\le KE+(b+\sqrt{KE/p})^2.$$
Fatou proves $f\in L^2(\nu)$. Then $f_N\to f$ in $L^2(\nu)$, because
$|f_N-f|\le|f|$, and passing the variance to the limit gives
$\operatorname{Var}_\nu f\le KE$ as required.
:::

**Fences respected.** The curvature-preserving convolution requires $a\le1$;
the proof uses that hypothesis exactly in its rescaling step. Isotropic
approximants have no uniform Hessian bounds, nor is such a bound needed.
Moment and derivative claims keep dimension and degree fixed. The weak-limit
argument first uses compact smooth tests; it does not pass arbitrary gradient
integrals by weak convergence. For proper affine supports, absolute
continuity and gradients refer to that support, not the ambient space.
