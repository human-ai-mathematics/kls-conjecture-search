---
title: "Dimension-free bounds for every cumulant order"
ledger-node: thm:bkl-cumulant-bound
numbering:
  enumerator: "134.%s"
---

*Part of the Bizeul–Klartag–Lehec proof, Chapter [](#sec:bkl-proof); the reading order is on the [full proofs](#sec:proofs-bkl) page.*

**Overview.** This dossier reconstructs Theorem 4.1 and Section 6 of
[@BizeulKlartagLehec2026KLS, version 1]. The induction proves a static bound and
an integrated next-order bound together. In a split cumulant contraction the
factor containing the distinguished vector uses the integrated estimate; the
other factor uses the static estimate. The resulting factorial cancellation
closes the induction without a dimension factor.

**Author.** plan_framework researcher, unknown, 2026-10-06.

**Dependencies.** [](#def:bkl-tilt-cumulants),
[](#lem:bkl-cumulant-dynamics) and [](#lem:bkl-cumulant-energy).
The third-order input used in the dynamics is
[](#prop:letwin-kappa) with its antecedent discharged by [](#thm:letwin-qcts).
No KLS estimate, suspension argument or tilt-average criterion is used.

:::{prf:theorem} All-order directional cumulant estimate
:label: thm:sol-bkl-cumulant-bound
There exists a numerical constant $K\ge1$ such that for every $n\ge1$, every
isotropic log-concave probability measure $\mu$ on $\mathbb R^n$, every integer
$m\ge2$ and every $u\in\mathbb R^n$,
$$
 |\kappa_m^\mu(u,\cdot,\ldots,\cdot)|^2
 \le K^{m-1}((m-1)!)^2|u|^2.
$$
Equivalently, $R_m^\mu\le K^{m-1}((m-1)!)^2I$.
:::

:::{prf:proof}
Fix $n$. All constants chosen below are independent of this choice. Initially
restrict to compactly supported isotropic log-concave laws. Let $C$ be the
universal constant in [](#lem:bkl-cumulant-energy), and choose
$$
 K\ge\max\{5,9C,64\},\qquad b_r=K^{r-1}((r-1)!)^2\quad(r\ge2).
$$
We prove, simultaneously for every such law and every unit vector $u$, that
$$
 \mathcal E_r(0)+\tfrac12\int_0^\infty\mathbb E\mathcal E_{r+1}(t)\,dt
 \le b_r\qquad(r\ge2).                                      \tag{A}
$$
For $r=2$, $\mathcal E_2(0)=1$ and
$\mathbb E\mathcal E_3(t)\le8e^{-t}$ by
[](#lem:bkl-cumulant-dynamics), so the left side is at most $5\le b_2$.
This initializes the integrated estimate needed when $r=3$.

Suppose (A) is proved at all orders $2\le r<m$, where $m\ge3$.
It supplies two different consequences:
$$
 \int_0^\infty\mathbb E\mathcal E_{r+1}(t)\,dt\le2b_r,
 \qquad R_r^\nu\le b_rI
 \quad\hbox{for every compactly supported isotropic log-concave }\nu.
                                                               \tag{B}
$$
The first concerns the process started at the law presently under study. The
second can be applied to its whitened posterior at every time. Thus
$$
 |\kappa_r(t)(v)|_t^2\le b_r\langle A_tv,v\rangle
 \quad(2\le r<m),\qquad
 I_m:=\int_0^\infty\mathbb E\mathcal E_m(t)\,dt\le2b_{m-1}.       \tag{C}
$$

It remains to bound the split tensor $L_m$. For a fixed cardinality
$a\in\{2,\ldots,m-2\}$, one summand, after permuting the nondistinguished slots,
is
$$
 P_a(h_2,\ldots,h_m)=
 \left\langle\kappa_{a+1}(t)(u,h_2,\ldots,h_a,\cdot),
 A_t^{-1}\kappa_{m-a+1}(t)(h_{a+1},\ldots,h_m,\cdot)\right\rangle.
$$
To compute its weighted norm put $w_j=A_t^{-1/2}e_j$ and first fix the indices
$i_2,\ldots,i_a$. Let
$z=\kappa_{a+1}(t)(u,w_{i_2},\ldots,w_{i_a},\cdot)$.
Summing over the remaining $m-a$ indices and applying (C) gives
$$
 \begin{split}
 &\sum_{i_{a+1},\ldots,i_m}
  P_a(w_{i_2},\ldots,w_{i_m})^2\\
 &\qquad=|\kappa_{m-a+1}(t)(A_t^{-1}z)|_t^2
 \le b_{m-a+1}\langle z,A_t^{-1}z\rangle
 =b_{m-a+1}\sum_k\kappa_{a+1}(t)(u,w_{i_2},\ldots,w_{i_a},w_k)^2.
 \end{split}
$$
The order $m-a+1$ is at most $m-1$, so the use of (C) is legitimate.
Now sum over $i_2,\ldots,i_a$, and integrate in time and probability. By (B)
at order $a$, this gives
$$
 |P_a(t)|_t^2\le b_{m-a+1}\mathcal E_{a+1}(t),\qquad
 \int_0^\infty\mathbb E|P_a(t)|_t^2\,dt\le2b_ab_{m-a+1}.          \tag{D}
$$
For each $a$ there are $\binom{m-1}{a-1}$ subsets containing the distinguished
index. Each yields a permutation of the other tensor indices and has the same
weighted norm. Apply the triangle inequality in the Hilbert space of whitened
tensors over time and probability. It follows that
$$
 \begin{split}
 \sqrt{J_m}&:=
 \left(\int_0^\infty\mathbb E|L_m(t)(u)|_t^2\,dt\right)^{1/2}\\
 &\le\sqrt2\sum_{a=2}^{m-2}\binom{m-1}{a-1}\sqrt{b_ab_{m-a+1}}.
 \end{split}
$$
There is no dimension factor in this estimate. Substitution of the definition
of $b_r$ shows, term by term, that
$$
 \binom{m-1}{a-1}\sqrt{b_ab_{m-a+1}}
 =\frac{(m-1)!}{(a-1)!(m-a)!}
 K^{(m-1)/2}(a-1)!(m-a)!=\sqrt{b_m}.
$$
There are $m-3$ terms; for $m=3$ the sum is empty. Thus
$\sqrt{J_m}\le\sqrt2(m-3)\sqrt{b_m}$. Both integrability hypotheses of
[](#lem:bkl-cumulant-energy) have now been proved, with no use of (A) at order
$m$. That lemma and (C) imply
$$
 \begin{split}
 \mathcal E_m(0)+\tfrac12\int_0^\infty\mathbb E\mathcal E_{m+1}(t)\,dt
 &\le2Cm^2b_{m-1}+4(m-3)\sqrt{b_{m-1}b_m}\\
 &=b_m\left(\frac{2C}{K}\frac{m^2}{(m-1)^2}
       +\frac4{\sqrt K}\frac{m-3}{m-1}\right)\le b_m.
 \end{split}
$$
Indeed $m^2/(m-1)^2\le9/4$, so the first term in parentheses is at most
$1/2$ when $K\ge9C$, and the second is at most $1/2$ when $K\ge64$.
This closes the simultaneous induction. Since
$\mathcal E_m(0)=|\kappa_m^\mu(u)|^2$, its static part proves the theorem for
compactly supported laws.

**Removal of compact support.** Let now $X$ have any isotropic log-concave law
$\mu$. For sufficiently large $R$ let $X_R$ have its conditional distribution
on the convex ball $\{|x|\le R\}$. These laws are log-concave and full
dimensional. Their means $a_R$ converge to zero and covariance matrices $A_R$
converge to $I$. To justify convergence of all higher moments, each coordinate
of $X$ is a variance-one log-concave marginal, and the elementary tail bound
proved in [](#lem:bkl-cumulant-dynamics) shows that every coordinate has every
absolute moment. Thus $|X|$ has every fixed moment as well. Dominated convergence,
followed by division by $\mathbb P(|X|\le R)\to1$, gives convergence of all
mixed moments of $X_R$.

Set $Y_R=A_R^{-1/2}(X_R-a_R)$. These are compactly supported isotropic
log-concave vectors, and $A_R^{-1/2}\to I$. Expanding each fixed mixed moment
of $Y_R$ as a finite polynomial in the coefficients of $A_R^{-1/2}$, $a_R$ and
mixed moments of $X_R$ proves its convergence to that of $X$. Cumulant entries
are finite polynomials in these moments by the moment-cumulant formula.
Therefore $\kappa_m^{Y_R}$ converges entrywise to $\kappa_m^\mu$ at every
fixed order $m$. In fixed dimension its Hilbert–Schmidt norm and every
directional contraction converge. The compact-support estimate passes to the
limit with the same universal $K$. Homogeneity removes the restriction
$|u|=1$, including $u=0$. No stochastic process for a noncompact initial law is
needed in this limiting argument.
:::

**Fences respected.** There is no assigned `bounded_by` fence. Constants in the
final induction do not depend on support radius, dimension, cumulant order or
the regularity of the density. Dimension-dependent moment constants are used
only to justify finite-time expectations and moment convergence, never in the
recurrence for $b_m$.
