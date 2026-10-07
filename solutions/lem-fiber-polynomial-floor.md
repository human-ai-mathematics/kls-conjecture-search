---
title: 'Solution: a uniform fixed-degree floor for simplex fiber forms'
ledger-node: lem:fiber-polynomial-floor
numbering:
  enumerator: 128.%s
---

*Part of the conditional-fiber mechanism, Chapter [](#sec:conditional-fiber-frame); the reading order is on the [full proofs](#sec:proofs-fibers) page.*

**Overview.** A polynomial on a uniform interval satisfies a reverse Poincaré
inequality with a constant depending only on its degree. Applying it on every
chord and averaging with the frame identity bounds the fiber form below by
the ordinary gradient energy. The established affine Poincaré bound for the
uniform simplex then gives a dimension-independent floor at every fixed degree.
No optimization over frames and no computation enter this argument.

:::{prf:theorem} Fixed-degree floor for every simplex frame
:label: thm:sol-fiber-polynomial-floor
For integers $m\ge2$ and $k\ge1$, let $\mu_m$ be the law on
$H_0=\mathbf1^\perp\subset\mathbb R^m$ of
$X=\sqrt{m(m+1)}(P-\mathbf1/m)$, where $P$ is uniform on
$\{p_i\ge0:\sum_i p_i=1\}$. Set $d=m-1$ and
$A_k=k(k+1)^2(k+2)$. For every even Borel probability $\rho$ on the unit
sphere of $H_0$ with $d\int\theta\theta^T\,d\rho=I_{H_0}$, and every real
polynomial $f$ on $H_0$ of total degree at most $k$, $f$ belongs to the maximal
form domain of [](#eq:conditional-fiber-form) and

$$
\mathcal D_{\mu_m,\rho}(f)
\ge \frac{12}{A_k}\int_{H_0}|\nabla_{H_0}f|^2\,d\mu_m
\ge \frac{3}{A_k}\operatorname{Var}_{\mu_m}(f).
$$

In particular, defining

$$
\Lambda_{m,k}
=\sup_{\rho\ \mathrm{admissible}}
\inf_{\substack{\deg f\le k\\\operatorname{Var}_{\mu_m}(f)>0}}
\frac{\mathcal D_{\mu_m,\rho}(f)}{\operatorname{Var}_{\mu_m}(f)},
$$

one has $3/A_k\le\Lambda_{m,k}\le1$. For every $m\ge2$,
$\Lambda_{m,3}\ge1/80$. Thus no sequence of valid all-frame upper
certificates supported on polynomials of one fixed finite degree can have
objectives tending to zero as $m\to\infty$.
:::

:::{prf:lemma} Reverse polynomial inequality on an interval
:label: lem:sol-fiber-interval-reverse
Let $I$ be a nondegenerate bounded interval of length $L$, let $T$ be
uniform on $I$, and let $q$ be a real polynomial of degree at most $k\ge1$.
Then

$$
\mathbb E|q'(T)|^2\le\frac{A_k}{L^2}\operatorname{Var}(q(T)),
\qquad
\frac{\operatorname{Var}(q(T))}{\operatorname{Var}(T)}
\ge\frac{12}{A_k}\mathbb E|q'(T)|^2.
$$
:::

:::{prf:proof}
Let $U$ be uniform on $[-1,1]$ and let $P_n$ denote the Legendre
polynomial normalized by $P_n(1)=1$. Its standard elementary identities are

$$
\mathbb E[P_n(U)P_j(U)]=\frac{\delta_{nj}}{2n+1},
\qquad P_n(-1)=(-1)^n.
$$

These identities follow from Rodrigues' formula
$P_n(u)=(2^n n!)^{-1}(d/du)^n(u^2-1)^n$: integration by parts
$n$ times proves orthogonality, since the boundary terms vanish; its leading
coefficient is $(2n)!/(2^n(n!)^2)$. Integrating Rodrigues' formula against
$P_n$ gives
$\int_{-1}^1P_n^2= (2n)!/[2^{2n}(n!)^2]\int_{-1}^1(1-u^2)^n\,du
=2/(2n+1)$, where the last integral follows by the beta integral (or its
integration-by-parts recurrence). Evaluating Rodrigues' formula at the endpoints
gives the displayed endpoint values.

For $0\le j<n$, integration by parts and orthogonality yield

$$
\int_{-1}^1P_n'(u)P_j(u)\,du
=[P_nP_j]_{-1}^1-\int_{-1}^1P_nP_j'\,du
=1-(-1)^{n+j}.
$$

Expanding the polynomial $P_n'$ in $P_0,\ldots,P_{n-1}$ therefore gives

$$
P_n'=\sum_{\substack{0\le j<n\\n-j\ \mathrm{odd}}}(2j+1)P_j,
\qquad
\mathbb E|P_n'(U)|^2
=\sum_{\substack{0\le j<n\\n-j\ \mathrm{odd}}}(2j+1)
=\frac{n(n+1)}2.
$$

The last equality is the sum of an arithmetic progression, for either parity
of $n$. Thus $e_n=\sqrt{2n+1}P_n$ form an orthonormal basis, and a centered
polynomial $h=\sum_{n=1}^k a_ne_n$ satisfies, by pointwise Cauchy–Schwarz,

$$
\mathbb E|h'(U)|^2
\le\left(\sum_{n=1}^ka_n^2\right)
\sum_{n=1}^k\mathbb E|e_n'(U)|^2
=\operatorname{Var}(h(U))\sum_{n=1}^k\frac{n(n+1)(2n+1)}2
=\frac{A_k}{4}\operatorname{Var}(h(U)).
$$

The final sum telescopes because the difference of
$n(n+1)^2(n+2)/4$ at consecutive $n$ is $n(n+1)(2n+1)/2$.
For $I=[a,a+L]$ substitute $T=a+L(U+1)/2$ and
$h(u)=q(a+L(u+1)/2)$. The derivative transformation supplies $4/L^2$,
proving the first inequality. Since $\operatorname{Var}(T)=L^2/12$, it
also proves the second.
:::

:::{prf:proof} Proof of the fixed-degree floor
The support of $\mu_m$ is a compact convex body with nonempty interior
relative to $H_0$. For every fixed direction $\theta$, orthogonal Fubini
shows that its conditional law on almost every chord is uniform on a
nondegenerate bounded interval. Parameterize that interval by the Euclidean
arc-length coordinate $t$ in $z+t\theta$; its variance is exactly $L^2/12$.
Restriction of $f$ to it has degree at most $k$, and derivative
$\partial_\theta f$. The interval inequality therefore gives

$$
\int_{\theta^\perp}
\frac{\operatorname{Var}(f(z+T\theta)\mid z)}
{\operatorname{Var}(T\mid z)}\,d\bar\mu_\theta(z)
\ge\frac{12}{A_k}\int|\partial_\theta f|^2\,d\mu_m.
$$

Exceptional null fibers are assigned zero, as in the form definition. All
polynomials have bounded gradients on the support, hence are Lipschitz on
that convex support. If $M$ bounds this gradient, the independent-copy
variance formula on each chord gives
$\operatorname{Var}(f(z+T\theta)\mid z)\le M^2\operatorname{Var}(T\mid z)$.
Consequently $\mathcal D(f)\le dM^2<\infty$, proving maximal-domain
membership directly.

Integrate the preceding lower bound against $d\rho(\theta)$. Tonelli and
frame isotropy give

$$
d\int\!\int|\partial_\theta f|^2\,d\mu_m\,d\rho(\theta)
=\int\nabla f^T\left(d\int\theta\theta^T\,d\rho\right)\nabla f\,d\mu_m
=\int|\nabla_{H_0}f|^2\,d\mu_m.
$$

This proves the first theorem inequality. The law $\mu_m$ is an isotropic
linear image of a log-concave Dirichlet law. By
[](#cor:cmh-dirichlet-poincare), its ordinary Poincaré constant on $H_0$
is at most $4$, giving the second inequality. This use has no unresolved
CMH premise: it invokes the established Dirichlet corollary, not universal CMH.

Taking the infimum over nonconstant polynomials, then the supremum over
admissible frames, preserves the lower bound. Every nonzero linear function
has quotient one by [](#lem:conditional-fiber-form), so each infimum is at
most one. Admissible frames exist, for example the even uniform measure on
an orthonormal basis of $H_0$. Finally $A_3=240$.

A valid all-frame upper certificate has objective at least $\Lambda_{m,k}$
by its defining upper-bound property. At fixed $k$, the lower bound $3/A_k$
is independent of $m$ and strictly positive, so these objectives cannot
tend to zero.
:::

:::{prf:remark} Scope and remaining optimization
:label: rem:sol-fiber-polynomial-floor-scope
The exact values of $\Lambda_{m,3}$ for $m=3,\ldots,8$ are not determined.
The estimate tends to zero with increasing degree; it gives no full
$L^2$ form gap and does not settle [](#conj:conditional-fiber-frame).
No step of the stated inequalities is left open. Extending a fixed-degree
conclusion to degrees increasing with dimension is not asserted.
:::

**Hypotheses and fences.** Uniform density and convex support supply uniform
interval conditional laws; bounded support ensures domain membership;
polynomial degree supplies the inverse inequality; the test-independent frame
identity recovers the full gradient energy; isotropy and the certified
Dirichlet Poincaré bound supply the dimension-independent variance comparison.
No additional hypothesis is used. Neither the proposed node nor
[](#conj:conditional-fiber-frame) has a recorded `bounded_by` edge.
The root cap obstruction [](#prop:conditional-fiber-root-obstruction) and
negative exchange obstruction [](#prop:sasada-negative-exchange) concern
unrestricted $L^2$ tests and are compatible with a degree-dependent floor.
The exact quadratic floor [](#lem:fiber-root-degree-two) is stronger at
that degree and is not used. This does not reverse the sufficient-only
bridge from fiber gaps to KLS.
