---
title: 'BKL: cumulant energy estimates'
ledger-node: lem:bkl-cumulant-energy
numbering:
  enumerator: "133.%s"
---

*Part of the Bizeul–Klartag–Lehec proof, Chapter [](#sec:bkl-proof); the reading order is on the [full proofs](#sec:proofs-bkl) page.*

**Overview.** This dossier reconstructs Section 5 of
[@BizeulKlartagLehec2026KLS, version 1]. An Itô computation in the inverse
covariance metric produces a positive next-order energy. The moving metric costs
only a quadratic factor in the cumulant order. The infinite-time conclusion is
taken along a sequence on which the terminal expectation tends to zero.

**Author.** plan_framework researcher, unknown, 2026-10-06.

**Dependencies.** [](#def:bkl-tilt-cumulants) and
[](#lem:bkl-cumulant-dynamics), including its finite-time integrability and
third-order matrix bound. No dimension-free estimate for higher cumulants or KLS
bound is used.

:::{prf:theorem} Energy inequality
:label: thm:sol-bkl-cumulant-energy
For the localization process of [](#lem:bkl-cumulant-dynamics), a deterministic
unit vector $u$, and $m\ge3$, let
$\mathcal E_m(t)=|\kappa_m(t)(u)|_t^2$. There is a universal constant $C\ge1$
such that
$$
 \operatorname{drift}\mathcal E_m(t)\ge
 \tfrac12\mathcal E_{m+1}(t)-Cm^2\mathcal E_m(t)
 -2\langle\kappa_m(t)(u),L_m(t)(u)\rangle_t.
$$
In particular, if
$$
 I_m:=\int_0^\infty\mathbb E\mathcal E_m(t)\,dt<\infty,
 \qquad J_m:=\int_0^\infty\mathbb E|L_m(t)(u)|_t^2\,dt<\infty,
$$
then
$$
 \mathcal E_m(0)+\tfrac12\int_0^\infty\mathbb E\mathcal E_{m+1}(t)\,dt
 \le Cm^2 I_m+2\sqrt{I_mJ_m}.
$$
The choice $C=17$ is sufficient.
:::

:::{prf:proof}
Put $r=m-1$, $T_t=\kappa_m(t)(u)$ and
$W_{i,t}=\kappa_{m+1}(t)(u,\cdot,\ldots,\cdot,A_t^{-1/2}e_i)$.
The dynamics give
$$
 dA=\sum_iH_i\,dB_i-A\,dt,\qquad
 dT=\sum_iW_i\,dB_i-(mT+L_m(u))\,dt.
$$
For positive definite $A$ define
$F(A,T)=\langle T,(A^{-1})^{\otimes r}T\rangle$. For any fixed symmetric
positive definite $P$,
$$
 F(A,T)=F(PAP,P^{\otimes r}T).
$$
This identity follows from $P(PAP)^{-1}P=A^{-1}$ and also holds for the
directional derivatives of $F$, with the corresponding congruence applied to
directions. At the particular time where the generator is evaluated choose
$P=A^{-1/2}$. This is a change of variables in a derivative at a fixed point,
not a stochastic change of coordinates; it adds no drift.
Use tildes for the transformed tensors, and let $G_i=PH_iP$.
The first derivative is evaluated in the direction
$(-I,-m\widetilde T-\widetilde L)$ and the quadratic directions are
$(G_i,\widetilde W_i)$.

For symmetric $H$, write $H^{(s)}$ for its action on slot $s$ of an order-$r$
tensor, and put $S_H=\sum_{s=1}^r H^{(s)}$. Different slots commute. Multiplying
the expansions of $(I+\varepsilon H)^{-1}$ in the $r$ slots gives
$$
 ((I+\varepsilon H)^{-1})^{\otimes r}
 =I-\varepsilon S_H+\frac{\varepsilon^2}{2}
 \left(S_H^2+\sum_{s=1}^r(H^{(s)})^2\right)+O(\varepsilon^3).
$$
It follows by multiplying on each side by $\widetilde T+\varepsilon W$ that
the coefficient of $\varepsilon$ in $F(I+\varepsilon H,\widetilde T+\varepsilon W)$
is
$$
 2\langle\widetilde T,W\rangle-\langle\widetilde T,S_H\widetilde T\rangle,
$$
and its coefficient of $\varepsilon^2$ is
$$
 |W|^2-2\langle W,S_H\widetilde T\rangle
 +\tfrac12|S_H\widetilde T|^2
 +\tfrac12\sum_{s=1}^r|H^{(s)}\widetilde T|^2.
$$
These are the first derivative and half the second derivative respectively.
The deterministic direction has $S_{-I}=-rI$ and therefore contributes
$-(m+1)|\widetilde T|^2-2\langle\widetilde T,\widetilde L\rangle$.
Consequently the full drift equals
$$
 \begin{split}
 &-(m+1)|\widetilde T|^2-2\langle\widetilde T,\widetilde L\rangle
 +\sum_i|\widetilde W_i|^2
 -2\sum_i\langle\widetilde W_i,S_{G_i}\widetilde T\rangle\\
 &\hspace{12mm}+\tfrac12\sum_i|S_{G_i}\widetilde T|^2
 +\tfrac12\sum_{i,s}|G_i^{(s)}\widetilde T|^2.
 \end{split}
$$
Discard the last two nonnegative sums. Young's inequality bounds the absolute
value of the cross term by
$\frac12\sum_i|\widetilde W_i|^2+2\sum_i|S_{G_i}\widetilde T|^2$.
The third-order matrix estimate is $\sum_iG_i^2\le8I$. Thus
$$
 \sum_i|S_{G_i}\widetilde T|^2
 \le r\sum_{s=1}^r\sum_i|G_i^{(s)}\widetilde T|^2
 \le8r^2|\widetilde T|^2.
$$
Also $|\widetilde T|^2=\mathcal E_m$,
$\sum_i|\widetilde W_i|^2=\mathcal E_{m+1}$ and
$\langle\widetilde T,\widetilde L\rangle=
\langle\kappa_m(u),L_m(u)\rangle_t$. The drift lower bound follows because
$m+1+16(m-1)^2\le17m^2$ for $m\ge3$.

By the finite-time integrability established in [](#lem:bkl-cumulant-dynamics),
the expectation of the Itô stochastic integral on $[0,T]$ is zero. Equivalently,
one may first stop in the parameter space and then remove the stop using its
deterministic finite-order posterior energy bounds. Integrating the drift gives
$$
 \begin{split}
 \mathcal E_m(0)+\tfrac12\int_0^T\mathbb E\mathcal E_{m+1}(t)\,dt
 \le{}&\mathbb E\mathcal E_m(T)+Cm^2\int_0^T\mathbb E\mathcal E_m(t)\,dt\\
 &+2\int_0^T\mathbb E\langle\kappa_m(t)(u),L_m(t)(u)\rangle_t\,dt.
 \end{split}
$$
The absolute value of the last integral is at most $\sqrt{I_mJ_m}$ by
Cauchy–Schwarz on the product of time and probability spaces. Since the
nonnegative function $t\mapsto\mathbb E\mathcal E_m(t)$ is integrable, there
exists an increasing deterministic sequence $T_j\to\infty$ for which
$\mathbb E\mathcal E_m(T_j)\to0$. In fact one can select $T_j$ in successive
unit intervals whose energy integral tends to zero. Monotone convergence on
the two nonnegative energy integrals along this sequence proves the claimed
inequality, and proves finiteness of the next-order integral at the same time.
Integrability alone is not being used to assert terminal decay at every time.
For arbitrary fixed $u$, all terms are homogeneous of degree two in $u$, so the
same conclusions follow by scaling; the case $u=0$ has all terms zero.
:::

**Fences respected.** There is no assigned `bounded_by` fence. The conclusion
requires both explicitly stated integrability hypotheses. They are discharged
by the coupled induction, not by an assumption of the desired higher-order
estimate.
