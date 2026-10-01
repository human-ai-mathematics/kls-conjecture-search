---
title: "Solution: stopped centroid and all-cut implications"
ledger-node:
  - thm:centroid-implies-kls
  - thm:intro-all-cut
numbering:
  enumerator: "100.%s"
---

**Overview.** This dossier proves two conditional implications. A stopped centroid
bound controls the quadratic variation of the bounded mass martingale, hence the
probability that a balanced cut leaves its window. The certified survival lemma
then yields KLS. Separately, the all-cut assumption supplies exactly the premise
of the certified tight-window consumption corollary at its coarse-window endpoint.
Neither antecedent is discharged here.

**Conventions.** All horizons in the antecedents are strictly positive and all
constants are finite. Let $\mu$ be isotropic log-concave on $\mathbb R^n$, and
let $E$ be a fixed measurable cut. Under the localization of the manuscript, write
$p_t=\mu_t(E)$, $q_t=1-p_t$, $s_t=p_tq_t$, and
$\delta_t=m_t^E-m_t^{E^c}$. The continuous process $p_t$ is a bounded martingale.
Its stochastic differential and quadratic variation are

$$
dp_t=s_t\delta_t\cdot dW_t,
\qquad d[p]_t=s_t^2|\delta_t|^2\,dt.
$$

Indeed the localization differential for the fixed indicator is
$dp_t=\operatorname{Cov}_{\mu_t}(\mathbf1_E,X)\cdot dW_t$; the covariance
is $p_t(m_t^E-a_t)=p_tq_t\delta_t$. The identities hold locally, and the boundedness
of $p_t$ makes its stopped increments square integrable. Thus the usual
martingale isometry applies at every bounded stopping time. These are the
mass-martingale conventions of [](#eq:qv-p).

:::{prf:theorem} Stopped centroid control implies KLS
:label: thm:sol-stopped-centroid-implication
Under [](#ass:stopped-centroid), with universal $T_0>0$ and $C\ge0$,
every isotropic log-concave probability measure has a Cheeger constant bounded
below by a positive universal constant. This is [](#thm:centroid-implies-kls).
:::

:::{prf:proof}
It suffices, by [](#lem:survival-implies-kls), to obtain a universal balanced
posterior event for every cut with $p_0=1/2$. Set

$$
\tau=\inf\{t\ge0:p_t\notin[1/3,2/3]\}.
$$

For $T\le T_0$, let $M_t=p_{t\wedge\tau}-p_0$ for $0\le t\le T$.
Continuity implies that on $\{\tau\le T\}$ the supremum of $|M_t|$ is at
least $1/6$. The nonnegative submartingale $M_t^2$ satisfies the weak maximal
inequality; therefore

$$
\mathbb P(\tau\le T)
\le36\mathbb E M_T^2
=36\mathbb E\int_0^{T\wedge\tau}s_t^2|\delta_t|^2\,dt
\le36CT.
$$

The last inequality uses $s_t^2\le1$ and the assumed centroid estimate.
In particular it requires no unproved integrability of a local martingale:
$M$ is bounded, and the displayed occupation is finite by the antecedent.
Choose

$$
T_* =\min\{T_0,\,[72(C+1)]^{-1}\}>0.
$$

Then $\mathbb P(\tau>T_*)\ge1/2$. On that event both posterior masses are
at least $1/3$. The survival lemma applies with $c_0=1/2$, $b_0=1/3$ and
time $T_*$. These quantities depend only on the universal antecedent constants,
so its final assertion proves KLS.
:::

:::{prf:theorem} All-cut Carleson control implies KLS
:label: thm:sol-all-cut-implication
Under [](#ass:all-cut-carleson), with universal $T_0>0$, finite
$C_0,C_1\ge0$ and $\alpha<1$, KLS holds. This is [](#thm:intro-all-cut).
:::

:::{prf:proof}
Fix any isotropic log-concave $\mu$ and any measurable cut of mass $1/2$.
In [](#cor:tight-window-consumption) take $\eta=1/6$. Its exit time
$\tau_\eta=\inf\{t:|p_t-1/2|>\eta\}$ is precisely the coarse exit time
$\tau$, with the continuous-exit convention in the manuscript. The initial
condition $|p_0-1/2|\le\eta/2$ holds. For each deterministic $0<T\le T_0$,
apply the all-cut assumption with $I=[0,T]$. It gives

$$
\mathbb E\int_0^{T\wedge\tau_\eta}S_t\,dt
\le C_0T+C_1\mathbb E\int_0^{T\wedge\tau_\eta}r_t\,dt
+\alpha\mathbb E\int_0^{T\wedge\tau_\eta}D_t\,dt,
$$

which is exactly the premise of the certified corollary. That corollary gives
a balanced survival event at a positive time depending only on
$T_0,C_0,C_1,\alpha,\eta$. Its conclusion, together with
[](#lem:survival-implies-kls), proves the desired universal Cheeger lower bound.
No extra stopping time has been inserted into the Carleson assumption.
:::

**Dependencies and applicability.** The first implication uses
[](#lem:survival-implies-kls) and assumes [](#ass:stopped-centroid).
The second uses [](#cor:tight-window-consumption) and
[](#lem:survival-implies-kls), and assumes [](#ass:all-cut-carleson).
The tight-window corollary is consumed as a certified result, rather than
reproved here. In particular this dossier does not certify the analytic
details of its existing dossier anew.

**Fences respected.** Neither target has a `bounded_by` edge. No universal
centroid or Carleson estimate is proved here, and no trace upgrade or spectral
occupation hypothesis is silently assumed. The universal KLS conclusions
remain conditional on their displayed antecedents.
