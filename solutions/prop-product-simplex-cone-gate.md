---
title: 'Solution: sharp linear gate on cones over products of simplices'
ledger-node: prop:product-simplex-cone-gate
numbering:
  enumerator: '127.%s'
---

*Part of the moment-map mechanism, Chapter [](#sec:cmh-exact-cases); the reading order is on the [full proofs](#sec:proofs-moment-map) page.*

**Overview.** We use the certified cone kernel of [](#prop:cone-moment-map),
compute three moments of an isotropic uniform simplex, and assemble the product
blocks. A polynomial with positive coefficients gives the sharp inequality and
all equality directions. Intervals count as one-dimensional simplices. This is
a family-specific linear-sector result, not a claim about universal CMH.

:::{prf:theorem} Product-simplex cone gate
:label: thm:sol-product-simplex-cone-gate
Let $q\ge1$, let $k_1,\ldots,k_q\ge1$ be integers, let
$n=1+\sum_{j=1}^q k_j$, and let $\beta\ge n$ be real. In
[](#def:exponential-cone), take the centered base $K$ to be a Cartesian product
of simplices of dimensions $k_1,\ldots,k_q$. Let $\Sigma$ and $\tau$ be the
covariance and canonical Stein kernel of $\bar\mu_{K,\beta}$, and put
$G=\Sigma^{-1/2}\mathbb E[\tau\Sigma^{-1}\tau]\Sigma^{-1/2}$.
Then $G$ has axis eigenvalue $1+n/\beta$ and, on each transverse factor of
dimension $k$, the eigenvalue

$$
\lambda_k(n,\beta)=
\frac{a_k\beta^2+(1+2b_k)\beta+n-k+c_k}{\beta(\beta+1)},
\quad
a_k=\frac{2(k+2)}{k+4},\qquad
b_k=\frac{2(k+1)(k+2)}{(k+3)(k+4)},\qquad
c_k=\frac{(k+2)(k^2+9k+2)}{(k+3)(k+4)}.
$$

In particular $G\preceq2I$. If $\beta>n$, then $G\prec2I$.
If $\beta=n$ and $q=1$, then $G=2I$. If $\beta=n$ and $q>1$,
then the eigenspace at $2$ is exactly the cone axis. Thus a nonzero transverse
equality direction exists exactly when $q=1$ and $\beta=n$.
The same spectral and inequality conclusions hold after any invertible linear
change of coordinates, with equality subspaces transported in covariance-normalized
coordinates.
:::

:::{prf:proof}
**Normalization and the simplex kernel.** Under an invertible linear map $L$,
the canonical kernel and covariance transform as $\tau\mapsto L\tau L^\top$
and $\Sigma\mapsto L\Sigma L^\top$. Indeed a moment potential $\phi$ transforms
to $\phi(L^\top y)-\log|\det L|$; its gradient and Hessian give these formulas.
The resulting normalized gate is conjugate to $G$ by the orthogonal matrix
$(L\Sigma L^\top)^{-1/2}L\Sigma^{1/2}$. We may therefore make each base factor
isotropic and regular by a block linear transformation, preserving the axis.

For a factor of dimension $k$, put $N=k+1$, let
$P=(P_1,\ldots,P_N)$ be uniform on the probability simplex, and write
$H=\{v\in\mathbb R^N:\sum_i v_i=0\}$ and $\mathbf e=(1,\ldots,1)$.
An isotropic copy is

$$
V=\sqrt{N(N+1)}(P-\mathbf e/N)\in H.
$$

Its canonical kernel on $H$ is

$$
T=(N+1)C(P),\qquad C(p)=\operatorname{diag}(p)-pp^\top.
$$

For completeness, the Dirichlet moment-potential computation underlying
[](#thm:cmh-dirichlet) can be verified here without its inequality. On $H$ take
$\phi(y)=N\log\sum_i e^{y_i/N}$ plus a normalizing constant. Its gradient is
$p-\mathbf e/N$ and its Hessian on $H$ is $C(p)/N$, where
$p_i=e^{y_i/N}/\sum_j e^{y_j/N}$. The gradient is a diffeomorphism onto the
centered open simplex. The determinant lemma gives a principal minor
$\det C_{[N-1]}=\prod_i p_i$; since $\ker C=\mathbb R\mathbf e$,
$\det_H C=N\prod_i p_i$. Also $e^{-\phi}$ is proportional to $\prod_i p_i$
because $\sum_i y_i=0$. Change of variables therefore gives constant target
density. This finite smooth strictly convex potential is a canonical moment
potential, by uniqueness as used in the certified cone dossier. Scaling by
$\sqrt{N(N+1)}$ gives $T$. The sum of the factor potentials similarly pushes
forward to the product law and has block diagonal Hessian. Consequently the
canonical base kernel is $T_K=\bigoplus_j T_j$. All these kernels are bounded
on their compact bases.

**The three block moments.** The uniform simplex integral, obtained by iterating
the elementary beta integral, is

$$
\mathbb E\prod_{i=1}^N P_i^{r_i}
=\frac{(N-1)!\prod_i r_i!}{(N-1+\sum_i r_i)!}
\qquad(r_i\text{ nonnegative integers}).
$$

It gives $\mathbb EV=0$ and $\mathbb E VV^\top=I_H$. Permutation invariance
implies that an invariant endomorphism of $H$ is scalar: extend it by zero on
$\mathbb R\mathbf e$, and invariance forces all diagonal entries to be equal
and all off-diagonal entries to be equal. In particular the three expectations
below are scalar, and their scalars follow by taking traces:

$$
\mathbb ET^2=a_k I_H,\qquad
\mathbb E[VV^\top T]=\mathbb E[TVV^\top]=b_k I_H,\qquad
\mathbb E[|V|^2VV^\top]=c_k I_H.
$$

Here is the full scalar computation. With $Q_2=\sum_iP_i^2$ and
$Q_3=\sum_iP_i^3$, the displayed simplex integral gives

$$
\mathbb E Q_2=\frac2{N+1},\qquad
\mathbb E Q_3=\frac6{(N+1)(N+2)},\qquad
\mathbb E Q_2^2=\frac{4N+20}{(N+1)(N+2)(N+3)}.
$$

Since $\operatorname{Tr} C^2=Q_2-2Q_3+Q_2^2$,
$V^\top TV=N(N+1)^2(Q_3-Q_2^2)$, and
$|V|^4=N^2(N+1)^2(Q_2-1/N)^2$, division by $k=N-1$ yields

$$
a_k=\frac{2(N+1)}{N+3},\qquad
b_k=\frac{2N(N+1)}{(N+2)(N+3)},\qquad
c_k=\frac{(N+1)(N^2+7N-6)}{(N+2)(N+3)},
$$

which are the stated expressions. These moment evaluations include $k=1$,
so they cover every interval after centering and scaling.

**Assembly of the cone.** Write $U=(V_1,\ldots,V_q)$, $m=n-1$, and
$T_K=\bigoplus_j T_j$. The base is isotropic. By [](#prop:cone-moment-map),
with $S\sim\Gamma(\beta,1)$ independent of $U$,

$$
\Sigma=\beta\oplus\beta(\beta+1)I_m,\qquad
\tau=S\begin{pmatrix}1&U^\top\\ U&B\end{pmatrix},\qquad
B=UU^\top+\beta T_K.
$$

All expectations below are finite by boundedness on the base and
$\mathbb ES^2=\beta(\beta+1)$. Matrix multiplication shows that the transverse
block of $\mathbb E[\tau\Sigma^{-1}\tau]$ is
$(\beta+1)I_m+\mathbb EB^2$, whereas its axis entry is $\beta+n$.
The off-axis vector is zero: it is invariant under independent permutations
of the vertices of every factor, and the only invariant vector in each $H_j$
is zero. The same invariance forces off-diagonal factor blocks of
$\mathbb EB^2$ to vanish (average permutations in just one factor).

Expand

$$
B^2=|U|^2UU^\top+\beta(UU^\top T_K+T_KUU^\top)+\beta^2T_K^2.
$$

In a factor of dimension $k$, independence and $\mathbb E|V_i|^2=k_i$
show that the first expectation is $(c_k+m-k)I_k$. The remaining two terms
have expectations $2\beta b_k I_k$ and $\beta^2a_k I_k$. Dividing the cone
block by $\beta(\beta+1)$ proves the claimed $\lambda_k$ and axis spectrum.

**The sharp gap.** Put $t=\beta-n\ge0$ and $d=n-k-1\ge0$. Substitution of
the three scalar expressions, followed by expansion, gives the identity

$$
\begin{aligned}
&(k+3)(k+4)\beta(\beta+1)(2-\lambda_k(n,\beta))\\
&\quad=4(k+3)t^2+
\bigl(5k^2+27k+28+8(k+3)d\bigr)t
+4d\bigl((k+3)n+k+1\bigr).
\end{aligned}
$$

Every coefficient is strictly positive for $k\ge1$ and $n\ge k+1$.
The right side is nonnegative, and vanishes exactly when $t=d=0$.
Thus a transverse block reaches two exactly when $\beta=n$ and $k=n-1$,
which means there is just one factor. The axis gap is
$2-(1+n/\beta)=(\beta-n)/\beta$. Together these prove all asserted strict
inequalities and equality subspaces.
:::

**Fences respected.** Neither gate conjecture nor the certified cone input has
a `bounded_by` edge. The proof is restricted to the stated product-simplex
bases. It does not discharge [](#conj:gate-zero-sharp) or [](#conj:gate-zero)
universally, and supplies no inequality for nonlinear CMH tests. The bound two
and the CMH gate threshold four are distinct. No additional hypothesis or
unclosed algebraic step is used.
