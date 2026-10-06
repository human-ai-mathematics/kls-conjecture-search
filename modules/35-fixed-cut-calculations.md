---
numbering:
  enumerator: "35.%s"
---

(sec:appendix-fixed-cut)=
# Product stress-test and bootstrap calculations

*Appendix to the fixed cut, Section [](#sec:introduction).*

The long computations of the fixed-cut approach. Their statements, what each one contributes, and a summary of how each proof goes are Sections [](#sec:product-stress) and [](#sec:bootstrap); nothing is decided here that is not decided there.

:::{prf:proof} Proof of [](#thm:budget)
(i) Since $\mu_t$ is a product pathwise and $E$ is $J$-measurable, [](#lem:block) applies to $(\mu_t,E)$ at every time: $G_t$ is supported on the $J\times J$ block, so

$$
S_t=s_t\norm{G_t}_\HS^2=\sum_{i\in J}s_t\abs{G_te_i}^2 .
$$

The per-direction Carleson estimate [](#cor:per-direction) gives, for each fixed $i$ and every $T$,

$$
\E\int_0^T s_t\abs{G_te_i}^2\dd t\le e_i^TR_0e_i=(R_0)_{ii}\le1,
$$

using $R_0=A_0-B_0\preceq A_0=I$. Sum over $i\in J$ and let $T\to\infty$ by monotone convergence.

(ii) The scalar Riccati identity [](#thm:scalar-riccati) gives, after stopping and taking expectations within the regularity convention, $\E r_{t\wedge\tau}\le r_0+\E\int_0^{t\wedge\tau}S_s\dd s\le1+k$, using $D\ge0$ and $r_0\le1$ (rank-one $B_0\preceq I$).

(iii) By [](#eq:qv-p), $\dd[p]_t=s_tr_t\dd t$ with $s_t\le\tfrac14$, so

$$
\E[p]_{T\wedge\tau}\le\frac14\int_0^T\E r_{t\wedge\tau}\dd t\le\frac{(1+k)T}4 .
$$

Doob's $L^2$ inequality for the exit of the nested coarse window gives $\Prob(\tau\le T)\le C_1(1+k)T$ with a universal $C_1$; choose $T_k=1/(2C_1(1+k))$ so that $\Prob(\tau>T_k)\ge\tfrac12$, on which event $\min(p_{T_k},q_{T_k})\ge\tfrac13$. The $T_k$-uniform log-concavity of $\mu_{T_k}$ and the perimeter supermartingale then give, as in [](#thm:centroid-implies-kls), $\mu^+(E)\ge\E\mu_{T_k}^+(E)\ge c\sqrt{T_k}\cdot\tfrac13\cdot\tfrac12\ge c'/\sqrt{1+k}$.
:::

:::{prf:proof} Proof of [](#lem:product-qcts)
Expand $Y^TMY=\sum_iM_{ii}Y_i^2+\sum_{i\ne j}M_{ij}Y_iY_j$. By independence and centering, all cross-covariances vanish: $\Cov(Y_i^2,Y_iY_j)=\E[Y_i^3]\E[Y_j]=0$, $\Cov(Y_iY_j,Y_iY_k)=\E[Y_i^2]\E[Y_j]\E[Y_k]=0$ for $j\ne k$, and disjoint pairs are independent. Hence, using $M_{ij}=M_{ji}$ so that each unordered pair $\{i,j\}$ contributes $\Var\bigl(2M_{ij}Y_iY_j\bigr)=4M_{ij}^2\sigma_i^2\sigma_j^2$,

$$
\Var(Y^TMY)=\sum_iM_{ii}^2\Var(Y_i^2)
+\sum_{i<j}4M_{ij}^2\sigma_i^2\sigma_j^2
=\sum_iM_{ii}^2\Var(Y_i^2)+2\sum_{i\ne j}M_{ij}^2\sigma_i^2\sigma_j^2 .
$$

For one-dimensional log-concave $Y_i$, the reverse Hölder inequalities (see e.g.\ [@KLnotes, Cor. 5]) give $\E Y_i^4\le C_4\sigma_i^4$ with $C_4$ universal, so $\Var(Y_i^2)\le(C_4-1)\sigma_i^4$. Both sums are dominated by $C_*\sum_{ij}M_{ij}^2\sigma_i^2\sigma_j^2=C_*\norm{A^{1/2}MA^{1/2}}_\HS^2$ with $C_*=\max(C_4-1,2)$.
:::

:::{prf:proof} Proof of [](#thm:V2-window)
On $t\le c_0/\log n$, [](#cor:letwin-window) with $p=2$ gives $\E\norm{A_t}_\op^2\le C_2$, hence $\E X_t^2\le C_2$. This pointwise estimate integrates over every subinterval and proves (V2). The consequences follow from [](#cor:V2-implies).

For the preprint-independent fallback, on the event $\{\norm{A_t}_\op<2\}$ one has $X_t\le1$. On the complement, of probability at most $e^{-1/(Ct)}$ by [](#thm:KL-window), the Brascamp–Lieb cap [](#eq:BL-cap) gives $X_t\le t^{-1}$, and therefore

$$
\E X_t^2\le1+t^{-2}e^{-1/(Ct)}\le1+\sup_{u>0}u^2e^{-u/C}=1+(2C/e)^2=:K_0 .
$$
:::

:::{prf:proof} Proof of [](#thm:bootstrap)
*Step 1.* By the perimeter supermartingale [](#eq:perimeter-supermartingale) and [](#lem:half), $\E[\mu_t^+(E)\one_{\{t<\tau_\eta\}}]\le\mu^+(E)=\tfrac{h_\mu}2+e_0$.

*Step 2.* On $\{t<\tau_\eta\}$, $\min(p_t,q_t)\ge\tfrac12-\eta$. By [](#lem:whitening) and the elementary bound $\lambda^{-1/2}\ge1-\tfrac12(\lambda-1)_+$ for $\lambda>0$ (trivial when the right side is negative),

$$
\E\bigl[h_{\mu_t}\min(p_t,q_t)\one_{\{t<\tau_\eta\}}\bigr]
\ \ge\
\hstar_n\Bigl(\frac12-\eta\Bigr)\Bigl(\Prob(\tau_\eta>t)-\frac{\E X_t}2\Bigr).
$$

*Step 3.* Write

$$
P=\Prob(\tau_\eta\le t),\qquad Y=\E X_t,\qquad
a=\frac12-\eta,\qquad \rho=\frac{\hstar_n}{h_\mu}.
$$

Near-worstness and the definition of $\hstar_n$ give

$$
\frac1{1+\eps}\le\rho\le1,
\qquad\text{hence}\qquad \rho\ge1-\eps.
$$

If $1-P-Y/2\ge0$, Steps 1–2 give

$$
\begin{split}
\E[\bar e_t\one_{\{t<\tau_\eta\}}]-e_0
&\le h_\mu\left\{\frac12-(1-\eps)a(1-P-Y/2)\right\}\\
&\le h_\mu\left(\eta+\frac P2+\frac Y4+\frac\eps2\right).
\end{split}
$$

Indeed, $\frac12-a(1-P)=\eta+aP\le\eta+P/2$, the $Y$ contribution is at most $Y/4$, and the $\eps$ contribution is at most $\eps/2$.

If $1-P-Y/2<0$, use only the nonnegativity of $h_{\mu_t}\min(p_t,q_t)\one_{\{t<\tau_\eta\}}$ in Step 1. The case assumption gives $P/2+Y/4>1/2$, and therefore

$$
\E[\bar e_t\one_{\{t<\tau_\eta\}}]-e_0
\le\frac{h_\mu}{2}
<h_\mu\left(\eta+\frac P2+\frac Y4+\frac\eps2\right).
$$

Thus [](#eq:bootstrap-main) holds in both cases.

*Step 4.* The stopped process $M_u=p_{u\wedge\tau_\eta}-\tfrac12$ is a bounded continuous martingale. On $\{\tau_\eta\le t\}$, continuity gives $\sup_{u\le t}|M_u|\ge\eta$. Hence the $L^2$ maximal inequality, martingale isometry, [](#eq:qv-p), and $s_tr_t\le\tfrac14\lmax(A_t)\le\tfrac14(1+X_t)$ give

$$
\begin{split}
\Prob(\tau_\eta\le t)
&\le\eta^{-2}\E M_t^2
=\eta^{-2}\E[p]_{t\wedge\tau_\eta}\\
&\le\frac1{4\eta^2}\int_0^t
\E[\one_{\{s<\tau_\eta\}}(1+X_s)]\dd s\\
&\le\frac1{4\eta^2}\left(t+\int_0^t\E X_s\dd s\right).
\end{split}
$$

This proves [](#eq:bootstrap-exit).

*Step 5.* Integrate [](#eq:bootstrap-main) over $[0,T]$ using $\int_0^T\Prob(\tau_\eta\le t)\dd t\le\tfrac1{4\eta^2}(\tfrac{T^2}2+T\Xi_T)$.
:::
