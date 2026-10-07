---
title: "Solution: consumption of the weighted near-Cheeger package"
ledger-node: thm:intro-weighted
numbering:
  enumerator: "102.%s"
---

*Part of the fixed-cut archive, Chapter [](#sec:introduction); the reading order is on the [full proofs](#sec:proofs-archive) page.*

**Overview.** The weighted package supplies an integrated Stein-trace estimate
and bounds its error by a multiple of time for cuts whose initial excess is
at most one. The certified source conversion then gives an absorptive
Carleson premise on the package's fixed window. Tight-window consumption
forces a uniform positive perimeter for balanced near-minimizers, which
implies KLS by the certified half-mass identity. The package itself is not
proved here; its recorded refutation is not used to make the implication
vacuous.

:::{prf:theorem} Weighted package consumption with a positive horizon
:label: thm:sol-weighted-package-implication
Assume [](#ass:weighted-package) with a strictly positive universal horizon
$T_0>0$ and finite nonnegative constants $C_0,C_1,C_2$. Then every isotropic
log-concave probability measure has a universal positive Cheeger lower bound.
These are the constants required by the canonical antecedent, and this
proves precisely the implication [](#thm:intro-weighted).
:::

:::{prf:proof}
Retain the fixed window parameter $\eta$ and constants $\beta,\gamma$ of the
package. Write

$$
\alpha=2\beta+64\eta^2<1,\qquad T_1=\min\{T_0,1\}>0.
$$

Since $\beta\ge0$, its absorption margin implies $\eta<1/8<1/6$.
Thus the package's window is already admissible for
[](#cor:tight-window-consumption); it need not and must not be changed after
the assumptions have been supplied.

Fix an isotropic log-concave $\mu$ and a finite-perimeter cut $E$ with
$p_0=\mu(E)=1/2$ and $e_0(E)\le1$. Let $\tau_\eta$ be the fixed tight
exit time. Use the notation $r,S,D,s$ of the manuscript and put

$$
W_t=(1+\|A_t\|_{\mathrm{op}})^{5/2},\qquad
\mathcal S_t=\mathcal S_{\mu_t}(E).
$$

On $\{t<\tau_\eta\}$, [](#lem:stein-vs-source) gives
$S_t\le2\mathcal S_t/s_t+64\eta^2D_t$. Integrate this nonnegative
pointwise inequality and apply clause (ii-w) of the package. For every
$0<T\le T_1$ this yields

$$
\begin{aligned}
\mathbb E\int_0^{T\wedge\tau_\eta}S_t\,dt
&\le2C_0T+2C_1\mathbb E\int_0^{T\wedge\tau_\eta}r_t\,dt
+\alpha\mathbb E\int_0^{T\wedge\tau_\eta}D_t\,dt\\
&\quad+2C_2\mathbb E\int_0^{T\wedge\tau_\eta}e_t(E)W_t\,dt.
\end{aligned}
$$

No damping term has been subtracted in this step. Clause (i-w), $e_0\le1$,
$\gamma>0$, and $T\le1$ give

$$
2C_2\mathbb E\int_0^{T\wedge\tau_\eta}e_t(E)W_t\,dt
\le2C_2^2(Te_0+T^{1+\gamma})\le4C_2^2T.
$$

Consequently the source satisfies exactly the prefix premise of
[](#cor:tight-window-consumption), with universal data

$$
C'_0=2C_0+4C_2^2,\qquad C'_1=2C_1,\qquad
\alpha<1,\qquad T_1>0,
$$

and the unchanged universal $\eta$. The initial nested-window condition is
automatic because $p_0=1/2$. The certified corollary supplies a constant
$c_*>0$, depending only on these universal data, such that

$$
\mu^+(E)\ge c_*
$$

for every such pair $(\mu,E)$.

To pass from these cuts to the Cheeger constant, fix $\mu$ and let
$I=I_\mu(1/2)$. If $I=+\infty$, the required lower bound follows directly
from [](#lem:half). Otherwise, by the definition of the infimum defining
the profile, choose measurable half-mass sets $E_k$ of finite perimeter with

$$
I\le\mu^+(E_k)\le I+1/k.
$$

These sets have $0\le e_0(E_k)\le1/k\le1$, so the preceding argument
applies to each of them. Letting $k$ tend to infinity gives $I\ge c_*$.
Finally [](#lem:half) gives $h_\mu=2I\ge2c_*$. The constant is universal,
which is the asserted KLS conclusion.
:::

:::{prf:remark} Role of the positive horizon
:label: rem:sol-weighted-positive-horizon
The explicit requirement $T_0>0$ in [](#ass:weighted-package) supplies
the positive interval $[0,T_1]$ consumed by the proof. It excludes a vacuous
premise with no times $0<T\le T_0$. This clarification retains the same
weighted propagation clause and the same fixed stopping window; it introduces
no alternative package and discharges no part of the antecedent.
:::

**Dependencies and fences.** The proof uses [](#lem:stein-vs-source),
[](#cor:tight-window-consumption), and [](#lem:half), with
[](#ass:weighted-package) as its antecedent. The target has no `bounded_by`
edge. The tight-window result is used as a certified implication, including
its analytical consumption step, rather than reproved here. The two-tail
and spectator obstructions are respected: no slice-wise estimate beyond
the certified conversion is asserted, no global covariance weight is
claimed to be valid, and the refuted package is not discharged. The
implication provides no unconditional progress on KLS.
