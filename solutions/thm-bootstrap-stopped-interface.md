---
title: 'Solution: the stopped covariance interface in the near-worst bootstrap'
label: sec:sol-bootstrap-stopped-interface
ledger-node: thm:bootstrap-stopped-interface
numbering:
  enumerator: D28.%s
---

**Overview.** This dossier proves [](#thm:bootstrap-stopped-interface) ([](#thm:sol-bootstrap-stopped-interface)). For a near-worst isotropic log-concave law and a balanced cut, the stopped Cheeger excess is bounded by $Te_0$ plus $h_\mu$ times window, exit and covariance terms ([](#eq:sol-bootstrap-stopped-interface)). In that bound the covariance interface enters only through the cut-stopped quantity $\widehat\Xi_{T,\eta}$ of [](#eq:sol-stopped-interface-definition). With $\eta=T^{1/3}$ it becomes $Te_0+2h_\mu(T^{4/3}+\widehat\Xi_{T,\eta})$ ([](#eq:sol-bootstrap-stopped-interface-clean)). The result is only a comparison: no dimension-free bound on $\widehat\Xi_{T,\eta}$ is proved and KLS is not inferred.

1. At each deterministic time, [](#lem:perimeter-martingale) and [](#lem:half) bound the expected stopped perimeter by $h_\mu/2+e_0$ ([](#eq:sol-stopped-interface-perimeter)).
2. [](#lem:whitening) and the tangent inequality [](#eq:sol-stopped-interface-tangent) bound the posterior Cheeger term from below on $\{t<\tau_\eta\}$ with covariance error $Z_t$, stopped rather than unstopped ([](#eq:sol-stopped-interface-whitening)).
3. The near-worst ratio $\rho\ge1-\varepsilon$ ([](#eq:sol-stopped-interface-rho)) and a two-case sign analysis combine steps 1–2 into the pointwise comparison [](#eq:sol-stopped-interface-pointwise).
4. Doob's weak $L^2$ inequality for the stopped mass martingale and the bracket bound [](#eq:sol-stopped-interface-qv) control the exit probability $P_t$ by $t+\int_0^tZ_s\,\dd s$ ([](#eq:sol-stopped-interface-exit)). Tonelli then integrates this in time ([](#eq:sol-stopped-interface-integrated-exit)).
5. Integrating step 3 and inserting step 4 gives [](#eq:sol-bootstrap-stopped-interface). The choice $\eta=T^{1/3}$ with $\varepsilon\le T^{1/3}$ and $T<1/8$ gives the clean form with $C=2$.

**Setup and integrability.** For a log-concave probability measure $\nu$ on $\mathbb R^n$, let $h_\nu$ denote its Cheeger constant, and let $h_n^\star$ be the infimum of $h_\nu$ over isotropic log-concave laws in dimension $n$. Fix an isotropic log-concave law $\mu$ and a measurable cut $E$. Along stochastic localization write

$$
p_t=\mu_t(E),\qquad q_t=1-p_t,\qquad s_t=p_tq_t,
\qquad A_t=\operatorname{Cov}(\mu_t),
$$

and let

$$
\bar e_t(E)=\mu_t^+(E)-h_{\mu_t}\min(p_t,q_t),
\qquad X_t=(\lambda_{\max}(A_t)-1)_+.
$$

The process $p_t$ is a bounded continuous martingale. If $\delta_t=m_t^E-m_t^{E^c}$ and $r_t=s_t|\delta_t|^2$, then the standard two-color identities give

```{math}
:label: eq:sol-stopped-interface-qv
\dd[p]_t=s_tr_t\,\dd t,
\qquad s_tr_t\leq\frac14\lambda_{\max}(A_t)
\leq\frac14(1+X_t).
```

Indeed, $s_t\delta_t\delta_t^T\preceq A_t$, its sole nonzero eigenvalue is $r_t$, and $s_t\leq1/4$.

For $0<\eta<1/2$, set

$$
\tau_\eta=\inf\{t:|p_t-1/2|>\eta\}.
$$

The process $(t,\omega)\mapsto X_t\mathbf1_{\{t<\tau_\eta\}}$ is nonnegative and jointly measurable. Moreover, taking traces in the covariance SDE, localizing its martingale part, and then using Fatou gives $\mathbb E\operatorname{Tr}A_t\leq\operatorname{Tr}A_0=n$. Hence

$$
0\leq\mathbb E[X_t\mathbf1_{\{t<\tau_\eta\}}]\leq n,
$$

so all deterministic-time expectations and finite-horizon integrals below are finite. If $\mu^+(E)=\infty$, the claimed estimate is automatic in the extended sense. We therefore prove the only nontrivial case $\mu^+(E)<\infty$, where [](#lem:perimeter-martingale) makes $\mu_t^+(E)$ an integrable nonnegative supermartingale.

:::{prf:theorem} Stopped covariance-interface refinement; [](#thm:bootstrap-stopped-interface)
:label: thm:sol-bootstrap-stopped-interface
Let $n\geq2$, let $\varepsilon\in(0,1]$, and let $\mu$ be isotropic and log-concave on $\mathbb R^n$, with

$$
h_\mu\leq(1+\varepsilon)h_n^\star.
$$

Let $E$ be any measurable set with $\mu(E)=1/2$, put

$$
e_0=e_0(E)=\bar e_0(E),
$$

and fix $\eta\in(0,1/2)$. For $T>0$, define the cut-stopped covariance interface

```{math}
:label: eq:sol-stopped-interface-definition
\widehat\Xi_{T,\eta}(\mu,E)
:=\int_0^T\mathbb E\!\left[X_s\mathbf1_{\{s<\tau_\eta\}}\right]\dd s.
```

Then

```{math}
:label: eq:sol-bootstrap-stopped-interface
\begin{split}
\int_0^T\mathbb E\!\left[
\bar e_t(E)\mathbf1_{\{t<\tau_\eta\}}\right]\dd t
\leq{}&T e_0+h_\mu\left[
\left(\frac\varepsilon2+\eta\right)T
+\frac{T^2}{16\eta^2}\right.\\
&\left.\hspace{31mm}
+\left(\frac{T}{8\eta^2}+\frac14\right)
\widehat\Xi_{T,\eta}(\mu,E)\right].
\end{split}
```

Consequently, if $0<T<1/8$, $\eta=T^{1/3}$, and $\varepsilon\leq T^{1/3}$, then

```{math}
:label: eq:sol-bootstrap-stopped-interface-clean
\int_0^T\mathbb E\!\left[
\bar e_t(E)\mathbf1_{\{t<\tau_\eta\}}\right]\dd t
\leq T e_0+C h_\mu\left(
T^{4/3}+\widehat\Xi_{T,\eta}(\mu,E)\right)
```

with a universal constant; for example, $C=2$ is valid.
:::

:::{prf:proof}
For a fixed deterministic time $t>0$, abbreviate

$$
\mathcal A_t=\{t<\tau_\eta\},\qquad
P_t=\mathbb P(\tau_\eta\leq t),\qquad
Z_t=\mathbb E[X_t\mathbf1_{\mathcal A_t}],
\qquad a=\frac12-\eta.
$$

The perimeter supermartingale is used only at the deterministic time $t$:

```{math}
:label: eq:sol-stopped-interface-perimeter
\begin{split}
\mathbb E[\mu_t^+(E)\mathbf1_{\mathcal A_t}]
&\leq\mathbb E\mu_t^+(E)\leq\mu^+(E)\\
&=\frac{h_\mu}{2}+e_0.
\end{split}
```

The last equality follows from balance and [](#lem:half). In particular, no optional-stopping assertion for the perimeter process is used.

On $\mathcal A_t$ one has $\min(p_t,q_t)\geq a$. The posterior covariance remains nondegenerate at finite times because localization changes the initial law by a strictly positive density on the same full-dimensional support. [](#lem:whitening) and

```{math}
:label: eq:sol-stopped-interface-tangent
\lambda^{-1/2}\geq1-\frac12(\lambda-1)_+,
\qquad \lambda>0,
```

therefore yield the stopped lower bound

```{math}
:label: eq:sol-stopped-interface-whitening
\begin{split}
\mathbb E\!\left[
h_{\mu_t}\min(p_t,q_t)\mathbf1_{\mathcal A_t}\right]
&\geq h_n^\star a\,
\mathbb E\!\left[
\lambda_{\max}(A_t)^{-1/2}\mathbf1_{\mathcal A_t}\right]\\
&\geq h_n^\star a\left(1-P_t-\frac{Z_t}{2}\right).
\end{split}
```

Crucially, the covariance error here is $Z_t$, not the larger unstopped expectation $\mathbb E X_t$.

Set

$$
\rho=\frac{h_n^\star}{h_\mu},
\qquad B_t=1-P_t-\frac{Z_t}{2}.
$$

By isotropy and near-worstness,

```{math}
:label: eq:sol-stopped-interface-rho
\frac1{1+\varepsilon}\leq\rho\leq1,
\qquad\text{so}\qquad \rho\geq1-\varepsilon.
```

Because the lower bound in [](#eq:sol-stopped-interface-whitening) can be negative, the sign of $B_t$ must be retained.

Suppose first that $B_t\geq0$. Combining [](#eq:sol-stopped-interface-perimeter)– [](#eq:sol-stopped-interface-rho), and multiplying by the lower bound for $\rho$ only in this nonnegative case, gives

$$
\begin{split}
\mathbb E[\bar e_t(E)\mathbf1_{\mathcal A_t}]-e_0
&\leq h_\mu\left\{\frac12-(1-\varepsilon)aB_t\right\}\\
&\leq h_\mu\left(
\eta+\frac{P_t}{2}+\frac{Z_t}{4}+\frac\varepsilon2\right).
\end{split}
$$

Indeed,

$$
\frac12-a(1-P_t)=\eta+aP_t\leq\eta+\frac{P_t}{2},
\qquad \frac{aZ_t}{2}\leq\frac{Z_t}{4},
\qquad \varepsilon aB_t\leq\frac\varepsilon2,
$$

where $0\leq B_t\leq1$ in this case.

If instead $B_t<0$, discard the nonnegative posterior Cheeger term in [](#eq:sol-stopped-interface-perimeter). Since the case assumption is precisely $P_t/2+Z_t/4>1/2$, one obtains

$$
\mathbb E[\bar e_t(E)\mathbf1_{\mathcal A_t}]-e_0
\leq\frac{h_\mu}{2}
<h_\mu\left(
\eta+\frac{P_t}{2}+\frac{Z_t}{4}+\frac\varepsilon2\right).
$$

Thus both cases prove the stopped pointwise comparison

```{math}
:label: eq:sol-stopped-interface-pointwise
\mathbb E[\bar e_t(E)\mathbf1_{\{t<\tau_\eta\}}]
\leq e_0+h_\mu\left(
\frac\varepsilon2+\eta+\frac{P_t}{2}+\frac{Z_t}{4}\right).
```

It remains to estimate $P_t$ without discarding the stopping indicator on $X_s$. The process

$$
M_u=p_{u\wedge\tau_\eta}-\frac12
$$

is a bounded continuous square-integrable martingale. On $\{\tau_\eta\leq t\}$, continuity of $p$ implies $\sup_{u\leq t}|M_u|\geq\eta$. The weak $L^2$ maximal inequality, martingale isometry at the bounded stopping time, and [](#eq:sol-stopped-interface-qv) give

```{math}
:label: eq:sol-stopped-interface-exit
\begin{split}
P_t
&\leq\eta^{-2}\mathbb E M_t^2
=\eta^{-2}\mathbb E[p]_{t\wedge\tau_\eta}\\
&\leq\frac1{4\eta^2}\int_0^t
\mathbb E\!\left[
\mathbf1_{\{s<\tau_\eta\}}(1+X_s)\right]\dd s\\
&\leq\frac1{4\eta^2}\left(t+\int_0^t Z_s\,\dd s\right).
\end{split}
```

The bracket integral naturally carries the indicator of the stopped interval. Whether its value at $s=\tau_\eta$ is included is immaterial for Lebesgue integration. Boundedness of $M$ and the integrability recorded above justify the isometry; no unbounded optional-stopping theorem is used.

All remaining integrands are nonnegative, so Tonelli's theorem and [](#eq:sol-stopped-interface-exit) imply

```{math}
:label: eq:sol-stopped-interface-integrated-exit
\begin{split}
\int_0^T P_t\,\dd t
&\leq\frac1{4\eta^2}\left[
\frac{T^2}{2}+
\int_0^T\int_0^t Z_s\,\dd s\,\dd t\right]\\
&=\frac1{4\eta^2}\left[
\frac{T^2}{2}+
\int_0^T(T-s)Z_s\,\dd s\right]\\
&\leq\frac1{4\eta^2}\left[
\frac{T^2}{2}+T\widehat\Xi_{T,\eta}(\mu,E)\right].
\end{split}
```

Integrating [](#eq:sol-stopped-interface-pointwise), using $\int_0^T Z_t\,\dd t=\widehat\Xi_{T,\eta}(\mu,E)$, and inserting [](#eq:sol-stopped-interface-integrated-exit) gives exactly [](#eq:sol-bootstrap-stopped-interface): the $P_t/2$ term contributes $T^2/(16\eta^2)$ and $T\widehat\Xi_{T,\eta}/(8\eta^2)$, while the $Z_t/4$ term contributes $\widehat\Xi_{T,\eta}/4$.

Finally, when $0<T<1/8$, the choice $\eta=T^{1/3}$ satisfies $0<\eta<1/2$. If also $\varepsilon\leq T^{1/3}$, then

$$
\left(\frac\varepsilon2+\eta\right)T
\leq\frac32T^{4/3},
\qquad
\frac{T^2}{16\eta^2}=\frac1{16}T^{4/3},
$$

and

$$
\frac{T}{8\eta^2}+\frac14
=\frac{T^{1/3}}8+\frac14<\frac5{16}.
$$

Thus the whole bracket in [](#eq:sol-bootstrap-stopped-interface) is at most $2(T^{4/3}+\widehat\Xi_{T,\eta})$, which proves [](#eq:sol-bootstrap-stopped-interface-clean) with $C=2$.
:::

**Hypotheses and dependency audit.** The proof uses exactly: balance of $E$; log-concavity and isotropy of $\mu$; the near-worst comparison $h_\mu\leq(1+\varepsilon)h_n^\star$; the range $\varepsilon\in(0,1]$; the deterministic-time conclusion of [](#lem:perimeter-martingale); [](#lem:half); [](#lem:whitening); and the standard localization identities displayed in [](#eq:sol-stopped-interface-qv). Finite initial perimeter is needed only for the nontrivial finite-valued case; infinite perimeter makes the assertion automatic. The clean specialization additionally uses exactly $0<T<1/8$, $\eta=T^{1/3}$, and $\varepsilon\leq T^{1/3}$. No smoothness of the density or cut, no near-minimality of the cut, and no unstated covariance estimate are used.

**Obstructions respected.** The fence `obs:circularity` is respected: the proof never treats the random mass-constrained isoperimetric profile as a supermartingale and never inserts a lower bound for that moving profile. Its only posterior isoperimetric input is the certified whitening comparison with the external worst-case constant $h_n^\star$, coupled to the explicit near-worst hypothesis at time zero.

The fence `obs:relative-ceiling` is also respected. The theorem is only a comparison whose right-hand side contains the cut-dependent stopped interface $\widehat\Xi_{T,\eta}(\mu,E)$. It proves no dimension-free or relative-scale upper bound for that interface (the elementary $nT$ integrability bound above is dimension dependent), and it does not infer KLS. In particular, stopping the interface does not by itself discharge the remaining covariance-occupation problem.
