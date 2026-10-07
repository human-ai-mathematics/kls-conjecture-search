---
title: "Reverse transfer from integration to Appell coefficients"
ledger-node: prop:bk-reverse-transfer
numbering:
  enumerator: "155.%s"
---

*Part of the Balasubramanian–Kasiviswanathan proof, Chapter [](#sec:bk-proof); the reading order is on the [full proofs](#sec:proofs-bk) page.*

**Overview.** This reconstructs Proposition 7.1 of
[@BalasubramanianKasiviswanathan2026KLS], at commit
`4837c33649ba2271f43c9684e9350ecbdd725f95`. A terminal Appell polynomial is
recovered from its lower-degree derivative. One matrix controls both the
curvature normalization and the derivative norm. Ordered covariance moments
and moving variance then transfer the estimate back to the original measure.

**Dependencies.** We use [](#def:bk-uniform-appell-coefficients),
[](#def:bk-compatible-calculus), [](#prop:bk-integration-calculus),
[](#lem:bk-regular-approximation), [](#lem:bk-localization-covariance),
and [](#lem:bk-moving-appell-variance). No KLS, BKL, or SZ v2 assertion is
used. The integration product bound and lower-degree constants below are
explicit hypotheses, not conclusions imported from any of those proofs.

:::{prf:theorem} Quantified reverse transfer
:label: thm:sol-bk-reverse-transfer
Fix integers $d\ge2$ and $1\le q\le d-1$, and $0<\eta\le1$.
Set $\delta=\eta^2/d^2$. Suppose $M_q\ge0$ is finite and, for every
centered regular log-concave law $\nu$ in every dimension with covariance
at most $I$ and curvature at least $\delta I$,
$$
 \|J_0^\nu J_1^\nu\cdots J_{q-1}^\nu\|_{\rm op}\le M_q.
$$
Suppose finite $C_1,\ldots,C_{d-1}\ge0$ satisfy $c_k(\nu)\le C_k$
for every isotropic log-concave law in every dimension and $1\le k<d$.
Put $\Sigma_d=\sum_{k=2}^{d-1}(d-k+1)C_kC_{d-k+1}$, with empty sum zero.
Then
$$
 c_d^*\le e^{3\eta}\left[(1+\eta)^{q/2}M_qC_{d-q}
                 +\frac{\eta}{d^2}\Sigma_d\right].
$$
This is [](#prop:bk-reverse-transfer), with $c_d^*$ the supremum over
all centered log-concave laws of covariance at most identity in all dimensions.
:::

:::{prf:proof}
For a regular law $\nu$, let $p$ be a degree-$d$ Appell polynomial.
All derivatives $D^jp$, $0\le j\le q$, are centered, since $q<d$.
They are compatible symmetric fields, and polynomial integrability places
them in the required weighted Sobolev domains. The centered-primitive identity
of [](#prop:bk-integration-calculus) applied successively gives
$$
 p=J_0^\nu J_1^\nu\cdots J_{q-1}^\nu D^qp,
 \qquad E_\nu p^2\le M_q^2 E_\nu\|D^qp\|^2.
$$
Here the final derivative is centered too; this is precisely where $q<d$
is required. There is no assertion of this product identity on constant fields.

The same inequality holds for a full-dimensional centered, possibly
nonsmooth law with covariance at most $I$ and curvature at least $\delta I$.
Indeed [](#lem:bk-regular-approximation) gives regular laws with these exact
same two bounds and convergence of all fixed moments. Apply the inequality
to their Appell polynomials with fixed leading tensor. Coefficients of an
Appell polynomial are polynomials in moments through degree $d$, obtained by
formal reciprocal expansion with constant coefficient one. Its squared norm
and that of its derivative therefore depend continuously on moments through
$2d$. Passing to the limit proves the assertion without approximating any
integration operator. The applicability condition $\delta\le1$ holds here.

Let now $\mu$ have mean $m$, positive covariance $A$, and positive curvature
matrix $B$. Set
$$
 M=A+\delta B^{-1},\qquad Y=M^{-1/2}(X-m),\qquad \nu=\mathcal L(Y).
$$
Then $\operatorname{Cov}(\nu)=M^{-1/2}AM^{-1/2}\preceq I$.
Moreover $M\succeq\delta B^{-1}$ gives $B\succeq\delta M^{-1}$,
so the curvature of $\nu$ is at least $M^{1/2}BM^{1/2}\succeq\delta I$.
For $\bar p(y)=p(m+M^{1/2}y)$ the Appell affine identity preserves all
centering conditions. The derivative chain rule gives
$D_y^q\bar p=(M^{1/2})^{\otimes q}D_x^qp$. Consequently
$$
 E_\mu p^2\le M_q^2 E_\mu\langle D^qp,M^{\otimes q}D^qp\rangle.
$$
This argument also applies to nonsmooth full-dimensional $\mu$ by the
preceding approximation after the coordinate change.

Start with a compactly supported isotropic law and run the localization
of [](#lem:bk-localization-covariance). Fix $T\in\operatorname{Sym}^d\mathbb R^n$,
and set $p_t=P_d^{\mu_t}[T]$. For every positive semidefinite matrix $M$,
$$
 E_t\langle D^qp_t,M^{\otimes q}D^qp_t\rangle
 \le(d!)^2C_{d-q}^2
  \langle T,(M^{\otimes q}\otimes A_t^{\otimes(d-q)})T\rangle.
$$
To see every tensor factor and factorial, put
$S=((M^{1/2})^{\otimes q}\otimes(A_t^{1/2})^{\otimes(d-q)})T$.
For each ordered derivative index tuple $I$, the remaining slice $S_I$ is
symmetric of rank $d-q$. Differentiation gives $d!/(d-q)!$, and the
coefficient bound in isotropic coordinates gives $(d-q)!C_{d-q}$.
Squaring and summing these scalar bounds over $I$ gives the displayed formula,
since $\sum_I\|S_I\|^2=\|S\|^2$. No symmetry between the two groups of
slots is required, and no commutation of $M$ with $A_t$ is asserted.

For $t>0$ the curvature is at least $\Lambda_t\succ0$. Choose
$M=A_t+\delta\Lambda_t^{-1}$ and apply both preceding inequalities.
With $V(t)=\mathbb E E_tp_t^2$, the ordered mixed covariance estimate gives
$$
 V(t)\le(d!)^2C_{d-q}^2M_q^2(1+\delta/t)^q e^{4d^2t}\|T\|^2.
$$
Substitute its square root in [](#lem:bk-moving-appell-variance).
For $T\ne0$, divide by $d!\|T\|$ to obtain
$$
 \frac{\sqrt{V(0)}}{d!\|T\|}
 \le e^{(2d^2+d+1)t}
       \left[(1+\delta/t)^{q/2}M_qC_{d-q}+t\Sigma_d\right].
$$
Set $t=\eta/d^2$. Then $\delta/t=\eta$ and
$(2d^2+d+1)t\le3\eta$ for $d\ge2$. Supremizing in $T$ proves the
claimed bound for compactly supported isotropic laws.

For an arbitrary isotropic log-concave $X$, condition on $|X|\le R$.
For large $R$, its conditional law has positive definite covariance $A_R$;
its mean $m_R$ tends to zero and $A_R\to I$. All polynomial moments
converge by dominated convergence, using finite log-concave moments.
The whitened vector $A_R^{-1/2}(X_R-m_R)$ is compactly supported,
isotropic and log-concave, and all its fixed moments converge to those of $X$.
The degree-$d$ Appell Gram matrix in a fixed orthonormal basis of
$\operatorname{Sym}^d\mathbb R^n$ consequently converges entrywise, hence in
operator norm. Its largest eigenvalue is $(d!c_d)^2$, so $c_d$ converges.
This passes the same bound to every isotropic law.

Finally, if a centered law has covariance at most $I$, restrict to its
linear support. Unless it is a point mass, it is the image $BY$ of an
isotropic law on that support with $\|B\|_{\rm op}\le1$. The Appell
transformation law sends $T$ to $(B^T)^{\otimes d}T$, whose norm is at most
$\|T\|$. Thus the same bound holds. For a point mass all positive-degree
Appell variances vanish. Taking the supremum over all dimensions and all
such laws finishes the proof.
:::

**Fences respected.** No `bounded_by` edge is assigned to this new proposition.
The brief's uniform-admissibility warning is met by requiring one $M_q$ for
all laws at the prescribed $\delta$ and one $C_k$ for each lower degree over
all isotropic laws. The statement is an implication and does not silently
provide these bounds. It makes no comparison of existing fixed-cut or gate-zero
routes and does not use a conclusion of KLS to initialize the coefficients.

**Dependencies and scope.** The argument uses preservation of both exact
bounds by the regular approximation input, the centered domain at the last
integration, the two separate tensor metrics, the source's $\eta/d^2$ error
term, and the truncation and affine-support passages. The approximation and
integration inputs are proved separately; this dossier does not replace
their proofs or independent reviews.
