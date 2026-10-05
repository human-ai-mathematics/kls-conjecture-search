---
title: "Solution: deterministic Carleson control implies stopped centroid control"
ledger-node: thm:carleson-implies-centroid
numbering:
  enumerator: "101.%s"
---

**Overview.** We first use the certified directional dissipation estimate to
obtain a finite, dimension-dependent total source budget. Localizing the
scalar Riccati identity and using Fatou then establishes all the finiteness
needed for absorption. Only after removing this auxiliary stopping do we
apply the assumed Carleson estimate on deterministic prefixes. Gronwall gives
a dimension-free bound and hence the stopped centroid estimate and KLS.

**Setup.** Fix an isotropic log-concave probability measure $\mu$ on
$\mathbb R^n$ and a measurable cut $E$ with $p_0=\mu(E)\in[2/5,3/5]$.
Use the two-color localization quantities of [](#thm:scalar-riccati):

$$
s_t=p_t(1-p_t),\quad
B_t=s_t\delta_t\delta_t^T,\quad r_t=\operatorname{Tr}B_t,
\quad R_t=A_t-B_t,
$$

$$
S_t=s_t\|G_t\|_{\mathrm{HS}}^2,\qquad
D_t=2s_t\delta_t^TA_t\delta_t-r_t^2.
$$

Here $p_t$ is the mass martingale, $A_t$ the full covariance, and $G_t$
the difference of the two conditional covariances. Covariance decomposition
gives $0\preceq B_t\preceq A_t$, $R_t\succeq0$, and the scalar Riccati
theorem gives

$$
dr_t=dM_t+(S_t-D_t)\,dt,\qquad D_t\ge r_t^2\ge0,
$$

where $M$ is a continuous local martingale with $M_0=0$.
At time zero, $B_0\preceq I_n$ and $B_0$ has rank at most one, so $r_0\le1$.
Put $\tau=\inf\{t:p_t\notin[1/3,2/3]\}$, using continuous exit.

:::{prf:lemma} Finiteness before invoking Carleson
:label: lem:sol-carleson-prefix-finiteness
For every finite $T\ge0$, writing $u(T)=\mathbb E r_{T\wedge\tau}$,

$$
u(T)+\mathbb E\int_0^{T\wedge\tau}D_t\,dt
\le r_0+\mathbb E\int_0^{T\wedge\tau}S_t\,dt
\le1+n.
$$

Moreover $u$ is measurable and locally integrable, and
$\mathbb E\int_0^{T\wedge\tau}r_t\,dt\le\int_0^T u(t)\,dt<\infty$.
No Carleson assumption is used in this lemma.
:::

:::{prf:proof}
Apply [](#cor:per-direction) to the deterministic coordinate vectors and sum.
Since $S_t=\sum_{j=1}^n s_t|G_te_j|^2$, Tonelli gives

$$
\mathbb E\int_0^\infty S_t\,dt
\le\sum_{j=1}^n e_j^TR_0e_j
=\operatorname{Tr}R_0\le n.
$$

To justify the expectation inequality for $r$, take an increasing sequence of
localizing times $\sigma_k\uparrow\infty$ for the Riccati identity. They can be
chosen to bound the stopped local martingale and the accumulated integrals
of $S+D$ as well as $r$, by intersecting the usual localizers with their
level hitting times and with the deterministic time $k$. The continuous
semimartingale identity is valid on bounded horizons, and its drift integrals
are locally finite; hence these extra level times also tend to infinity.
At $T\wedge\tau\wedge\sigma_k$ the martingale has zero expectation and all
terms are integrable, so

$$
\mathbb E r_{T\wedge\tau\wedge\sigma_k}
+\mathbb E\int_0^{T\wedge\tau\wedge\sigma_k}D_t\,dt
=r_0+\mathbb E\int_0^{T\wedge\tau\wedge\sigma_k}S_t\,dt.
$$

Continuity gives almost sure convergence of the terminal $r$ values, without
asserting they are monotone. Apply Fatou to the nonnegative left-hand side
and monotone convergence to the source integrals on the right. The resulting
inequality is the first assertion; its right side is bounded by $1+n$ by
the source budget above. In particular $u(T)\le1+n$ for every $T$.
The stopped process is continuous and adapted, so its expectation is
measurable; this bound makes $u$ locally integrable. Finally, nonnegativity
and the pointwise inequality
$\mathbf1_{\{t<\tau\}}r_t\le r_{t\wedge\tau}$ give the occupation claim
by Tonelli. Endpoints do not affect time integrals.
:::

:::{prf:theorem} Carleson control implies the stopped centroid estimate and KLS
:label: thm:sol-carleson-centroid-implication
Assume [](#ass:all-cut-carleson), with universal finite constants
$T_0>0$, $C_0,C_1\ge0$ and $\alpha<1$. Then [](#ass:stopped-centroid)
holds with the same $T_0$ and with

$$
C=\frac92(1+C_0T_0)e^{C_1T_0}.
$$

Consequently KLS holds. This proves [](#thm:carleson-implies-centroid).
:::

:::{prf:proof}
Fix $\mu,E$ as in the setup. For each deterministic $0<T\le T_0$, the
finiteness lemma establishes that all three occupation expectations in the
Carleson premise are finite. Apply that premise with $I=[0,T]$, after
the auxiliary localization has already been removed. Combining the premise
with the lemma gives

$$
u(T)+(1-\alpha)\mathbb E\int_0^{T\wedge\tau}D_t\,dt
\le r_0+C_0T+C_1\mathbb E\int_0^{T\wedge\tau}r_t\,dt
\le1+C_0T+C_1\int_0^T u(t)\,dt.
$$

Because $1-\alpha>0$ and the damping expectation is finite and nonnegative,
we may discard it. Integral Gronwall applies to the nonnegative, locally
integrable function $u$ and yields

$$
u(T)\le(1+C_0T)e^{C_1T}\le C_*:=(1+C_0T_0)e^{C_1T_0}.
$$

For completeness, set $v(T)=1+C_0T+C_1\int_0^T u(t)\,dt$. Then $u\le v$,
$v(0)=1$, and $v'\le C_0+C_1v$ almost everywhere. Multiplication by
$e^{-C_1T}$ and integration gives
$v(T)\le e^{C_1T}(1+C_0\int_0^T e^{-C_1t}\,dt)
\le e^{C_1T}(1+C_0T)$, including the case $C_1=0$.

On $t<\tau$, $s_t\ge2/9$ and $r_t=s_t|\delta_t|^2$. Hence for every
$0<T\le T_0$,

$$
\mathbb E\int_0^{T\wedge\tau}|\delta_t|^2\,dt
\le\frac92\mathbb E\int_0^{T\wedge\tau}r_t\,dt
\le\frac92 C_*T.
$$

The constants are independent of dimension, the measure, and the cut;
the argument covered the entire initial range $p_0\in[2/5,3/5]$. This is
the asserted stopped centroid assumption.

To conclude KLS without importing another conditional implication, restrict
to cuts with $p_0=1/2$. The localization identity for their mass martingale is
$dp_t=s_t\delta_t\cdot dW_t$, since
$\operatorname{Cov}_{\mu_t}(\mathbf1_E,X)=s_t\delta_t$.
The stopped martingale $p_{t\wedge\tau}-1/2$ is bounded. Its quadratic
variation and the weak maximal inequality for its square give

$$
\mathbb P(\tau\le T)
\le36\mathbb E(p_{T\wedge\tau}-1/2)^2
=36\mathbb E\int_0^{T\wedge\tau}s_t^2|\delta_t|^2\,dt
\le36CT.
$$

Continuity supplies the displacement $1/6$ on exit. Choose
$T_* =\min\{T_0,[72(C+1)]^{-1}\}>0$. Then with probability at least
$1/2$ the cut survives, and its masses at $T_*$ are at least $1/3$.
[](#lem:survival-implies-kls) now yields the universal Cheeger lower bound.
:::

**Dependencies and fences.** The proof uses [](#thm:scalar-riccati),
[](#cor:per-direction), and [](#lem:survival-implies-kls), with
[](#ass:all-cut-carleson) as an antecedent. The target has no `bounded_by`
edge. The dimension-dependent bound $1+n$ is used only to establish finiteness
before absorption; it is never asserted to be universal. The operator-to-trace
difficulty is not discharged. No estimate on an additional random interval,
no uniform integrability of the terminal Riccati process, and no transfer of
Carleson through an approximation are required.
