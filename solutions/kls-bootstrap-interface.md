---
title: 'Solution: the near-worst bootstrap and its covariance interface'
label: sec:sol-kls-bootstrap-interface
ledger-node:
- lem:half
- lem:whitening
- thm:bootstrap
- lem:crude
- cor:loglog
- prop:ceiling
numbering:
  enumerator: D3.%s
---

**Overview.** This dossier proves [](#lem:half), [](#lem:whitening), [](#thm:bootstrap), [](#lem:crude), [](#cor:loglog) and [](#prop:ceiling). It uses two deterministic isoperimetric comparisons to bound the Cheeger-line excess of a near-worst measure along stochastic localization. The covariance overshoot $\Xi_T$ is the only interface quantity. It is then evaluated crudely, and polylogarithmically under [](#hyp:KI). Finally, the dossier shows that an all-measure relative-scale bound on $\Xi_T$ would already imply KLS.

1. [](#lem:sol-half): concavity and symmetry of the profile give $h_\nu=2I_\nu(1/2)$.
2. [](#lem:sol-whitening): whitening gives [](#eq:sol-whitening), and $\hstar_n$ is nonincreasing in $n$.
3. [](#thm:sol-bootstrap): the perimeter supermartingale, Steps 1–2 and a two-case argument prove [](#eq:sol-bootstrap-main). The second case is needed because the lower bound can be negative. The $L^2$ maximal inequality with [](#eq:sol-mass-qv-bound) gives the exit bound [](#eq:sol-bootstrap-exit). Integration gives [](#eq:sol-bootstrap-integrated) and [](#eq:sol-bootstrap-clean).
4. [](#lem:sol-crude): the trace SDE and the Brascamp–Lieb cap give $\Xi_T\le1+\log(nT)$. This is recorded only as an insufficient fence.
5. [](#cor:sol-loglog): under [](#hyp:KI), which is discharged by [](#cor:KI-discharged), $\Xi_T\lesssim1+\log\log n$ [](#eq:sol-loglog-interface). Step 3 then gives [](#eq:sol-loglog-supply).
6. [](#prop:sol-ceiling): if [](#eq:sol-ceiling-assumption) held for all measures, balanced mass would survive, and [](#lem:survival-implies-kls) would give KLS. Only this sufficient implication is claimed.

**Setup.** For a log-concave probability measure $\nu$, let

$$
I_\nu(p)=\inf\{\nu^+(E):\nu(E)=p\},\qquad
h_\nu=\inf_E\frac{\nu^+(E)}{\min(\nu(E),1-\nu(E))},
$$

and let $\hstar_n$ be the infimum of $h_\nu$ over isotropic log-concave laws on $\mathbb R^n$. Along stochastic localization write

$$
p_t=\mu_t(E),\quad q_t=1-p_t,\quad s_t=p_tq_t,
\quad A_t=\operatorname{Cov}(\mu_t),
$$

$$
\bar e_t(E)=\mu_t^+(E)-h_{\mu_t}\min(p_t,q_t),qquad
X_t=(\lambda_{\max}(A_t)-1)_+,qquad
\Xi_T=\int_0^T\mathbb E X_t\,\dd t.
$$

For $0<\eta<1/2$ set $\tau_\eta=\inf\{t:|p_t-1/2|>\eta\}$. The mass martingale satisfies

```{math}
:label: eq:sol-mass-qv-bound
\dd[p]_t=s_t r_t\,\dd t,
\qquad s_t r_t\leq\frac14\lambda_{\max}(A_t)
\leq\frac14(1+X_t).
```

All stopping and expectation arguments below are first made in the compact smooth class and then passed through the manuscript's uniform approximation convention. Since $0\leq p_t\leq1$, the stopped mass martingales are uniformly integrable; no unbounded optional-stopping theorem is being invoked.

## 1\. Two deterministic isoperimetric comparisons

:::{prf:lemma} Balance pins the Cheeger ratio; [](#lem:half)
:label: lem:sol-half
For every log-concave $\nu$,

$$
h_\nu=2I_\nu(1/2).
$$

If $\nu(E)=1/2$, then the profile excess and Cheeger-line excess agree:

$$
\nu^+(E)-I_\nu(1/2)
=\nu^+(E)-h_\nu\min(\nu(E),1-\nu(E)).
$$
:::

:::{prf:proof}
The generalized isoperimetric profile of a log-concave measure is symmetric, $I_\nu(p)=I_\nu(1-p)$, is concave on $(0,1)$ in the standard generalized sense, and has $I_\nu(0+)=0$ [@Bobkov1999LogConcave; @Milman2009Isoperimetric]. Concavity at the origin implies that $p\mapsto I_\nu(p)/p$ is nonincreasing on $(0,1/2]$: if $0<p<q\leq1/2$, then $I_\nu(p)\geq(p/q)I_\nu(q)$. Therefore

$$
\inf_{0<p\leq1/2}\frac{I_\nu(p)}p=2I_\nu(1/2).
$$

Symmetry gives the same infimum on $[1/2,1)$ after division by $1-p$, proving the first identity. The second is immediate because $\min(1/2,1/2)=1/2$.
:::

:::{prf:lemma} Whitening comparison; [](#lem:whitening)
:label: lem:sol-whitening
Let $\nu$ be log-concave on $\mathbb R^n$ with nondegenerate covariance $A_\nu$. Then

```{math}
:label: eq:sol-whitening
h_\nu\geq\frac{\hstar_n}{\lambda_{\max}(A_\nu)^{1/2}}.
```

In particular, almost surely $h_{\mu_t}\geq\hstar_n\lambda_{\max}(A_t)^{-1/2}$ for $t>0$. Moreover, $\hstar_n$ is nonincreasing in $n$.
:::

:::{prf:proof}
Let $a_\nu$ be the centroid, $T=A_\nu^{1/2}$, and $\widetilde\nu=(A_\nu^{-1/2})_\#(\nu-a_\nu)$. Then $\widetilde\nu$ is isotropic and log-concave, so $h_{\widetilde\nu}\geq\hstar_n$, and $\nu=T_\#\widetilde\nu+a_\nu$. Put $L=\|T\|_{\mathrm{op}}$. For every Borel set $S$ and every $\delta>0$,

$$
T^{-1}(S_\delta-a_\nu)
\supseteq\bigl(T^{-1}(S-a_\nu)\bigr)_{\delta/L}.
$$

After subtracting the common mass, dividing by $\delta$, and taking the lower limit,

$$
\nu^+(S)\geq L^{-1}\widetilde\nu^+(T^{-1}(S-a_\nu))
\geq\frac{\hstar_n}{L}\min(\nu(S),1-\nu(S)).
$$

Taking the infimum in $S$ and using $L=\lambda_{\max}(A_\nu)^{1/2}$ proves [](#eq:sol-whitening). An isotropic starting law is full-dimensional, and the localization density is positive on the same support, so $A_t$ remains nondegenerate at finite $t$.

For monotonicity, if $m\leq n$ and $\rho$ is isotropic log-concave on $\mathbb R^m$, then $\rho\otimes\gamma_{n-m}$ is isotropic log-concave on $\mathbb R^n$. Cylinder competitors give $h_{\rho\otimes\gamma_{n-m}}\leq h_\rho$. Taking first the infimum over all $\rho$ and then using the definition in dimension $n$ yields $\hstar_n\leq\hstar_m$.
:::

## 2\. The bootstrap comparison

:::{prf:theorem} Bootstrap comparison; [](#thm:bootstrap)
:label: thm:sol-bootstrap
Let $n\geq2$, $\varepsilon\in(0,1]$, and let $\mu$ be isotropic log-concave on $\mathbb R^n$ with $h_\mu\leq(1+\varepsilon)\hstar_n$. Let $E$ be any measurable set with $\mu(E)=1/2$ and $e_0=e_0(E)=\bar e_0(E)$, and fix $\eta\in(0,1/2)$. For every $t>0$,

```{math}
:label: eq:sol-bootstrap-main
\mathbb E[\bar e_t(E)\mathbf 1_{\{t<\tau_\eta\}}]
\leq e_0+h_\mu\left(
\frac\varepsilon2+\eta+\frac12\mathbb P(\tau_\eta\leq t)
+\frac14\mathbb E X_t\right),
```

```{math}
:label: eq:sol-bootstrap-exit
\mathbb P(\tau_\eta\leq t)
\leq\frac1{4\eta^2}\left(t+\int_0^t\mathbb E X_s\,\dd s\right).
```

Consequently,

```{math}
:label: eq:sol-bootstrap-integrated
\begin{split}
\int_0^T\mathbb E[\bar e_t(E)\mathbf 1_{\{t<\tau_\eta\}}]\,\dd t
\leq{}&Te_0+h_\mu\left[
\left(\frac\varepsilon2+\eta\right)T+
\frac{T^2}{16\eta^2}+
\frac{T\Xi_T}{8\eta^2}+\frac{\Xi_T}{4}\right].
\end{split}
```

If $0<T<1/8$, $\eta=T^{1/3}$, and $\varepsilon\leq T^{1/3}$, then for a universal $C$,

```{math}
:label: eq:sol-bootstrap-clean
\int_0^T\mathbb E[\bar e_t(E)\mathbf 1_{\{t<\tau_\eta\}}]\,\dd t
\leq Te_0+C h_\mu(T^{4/3}+\Xi_T).
```
:::

:::{prf:proof}
Write $A=\{t<\tau_\eta\}$ and $P=\mathbb P(A^c)$. The perimeter supermartingale gives

```{math}
:label: eq:sol-bootstrap-perimeter
\mathbb E[\mu_t^+(E)\mathbf 1_A]
\leq\mathbb E\mu_t^+(E)
\leq\mu^+(E)=\frac{h_\mu}{2}+e_0,
```

where the last equality is [](#lem:sol-half). This uses a deterministic time $t$; there is no optional-stopping step for the perimeter process.

On $A$, $\min(p_t,q_t)\geq1/2-\eta$. [](#lem:sol-whitening) and the elementary inequality

```{math}
:label: eq:sol-sqrt-tangent
\lambda^{-1/2}\geq1-\frac12(\lambda-1)_+,
\qquad \lambda>0,
```

give

```{math}
:label: eq:sol-bootstrap-profile-raw
\begin{split}
\mathbb E[h_{\mu_t}\min(p_t,q_t)\mathbf 1_A]
&\geq\hstar_n(1/2-\eta)
\mathbb E[\lambda_{\max}(A_t)^{-1/2}\mathbf 1_A]\\
&\geq\hstar_n(1/2-\eta)(1-P-\tfrac12\mathbb E X_t).
\end{split}
```

The last lower bound may be negative. The manuscript's abbreviated proof silently multiplied it by a lower bound for $\hstar_n/h_\mu$, which is only legitimate when its bracket is nonnegative. We now record the required two-case argument.

Set $Y=\mathbb E X_t$, $a=1/2-\eta$, and $\rho=\hstar_n/h_\mu$. Near-worstness and the definition of $\hstar_n$ give

```{math}
:label: eq:sol-rho-range
\frac1{1+\varepsilon}\leq\rho\leq1,
\qquad\text{hence}\qquad \rho\geq1-\varepsilon.
```

If $1-P-Y/2\geq0$, combine [](#eq:sol-bootstrap-perimeter)–[](#eq:sol-rho-range) to obtain

$$
\begin{split}
\mathbb E[\bar e_t\mathbf 1_A]-e_0
&\leq h_\mu\{1/2-(1-\varepsilon)a(1-P-Y/2)\}\\
&\leq h_\mu(\eta+P/2+Y/4+\varepsilon/2).
\end{split}
$$

Indeed, $1/2-a(1-P)=\eta+aP\leq\eta+P/2$, the $Y$ contribution is at most $Y/4$, and the $\varepsilon$ contribution is at most $\varepsilon/2$.

If $1-P-Y/2<0$, use only the nonnegativity of $h_{\mu_t}\min(p_t,q_t)\mathbf 1_A$ in [](#eq:sol-bootstrap-perimeter). The case assumption gives $P/2+Y/4>1/2$, and therefore

$$
\mathbb E[\bar e_t\mathbf 1_A]-e_0
\leq h_\mu/2
<h_\mu(\eta+P/2+Y/4+\varepsilon/2).
$$

Thus [](#eq:sol-bootstrap-main) holds in both cases.

For the exit estimate, stop the bounded continuous martingale $M_u=p_{u\wedge\tau_\eta}-1/2$. On $\{\tau_\eta\leq t\}$, continuity gives $\sup_{u\leq t}|M_u|\geq\eta$. The $L^2$ maximal inequality, the martingale isometry for the bounded stopping time, and [](#eq:sol-mass-qv-bound) yield

$$
\begin{split}
\mathbb P(\tau_\eta\leq t)
&\leq\eta^{-2}\mathbb E M_t^2
=\eta^{-2}\mathbb E[p]_{t\wedge\tau_\eta}\\
&\leq\frac1{4\eta^2}\int_0^t
\mathbb E[\mathbf 1_{\{s<\tau_\eta\}}(1+X_s)]\,\dd s\\
&\leq\frac1{4\eta^2}\left(t+\int_0^t\mathbb E X_s\,\dd s\right).
\end{split}
$$

This proves [](#eq:sol-bootstrap-exit). All integrands are nonnegative, so Tonelli gives

$$
\begin{split}
\int_0^T\mathbb P(\tau_\eta\leq t)\,\dd t
&\leq\frac1{4\eta^2}\left\{
\frac{T^2}{2}+\int_0^T(T-s)\mathbb E X_s\,\dd s\right\}\\
&\leq\frac1{4\eta^2}\left(\frac{T^2}{2}+T\Xi_T\right).
\end{split}
$$

Integrating [](#eq:sol-bootstrap-main) and inserting this estimate gives exactly [](#eq:sol-bootstrap-integrated), including the constants $1/16$, $1/8$, and $1/4$.

Finally, $T<1/8$ ensures $\eta=T^{1/3}<1/2$. With $\varepsilon\leq T^{1/3}$,

$$
(\varepsilon/2+\eta)T\leq\tfrac32T^{4/3},\qquad
\frac{T^2}{16\eta^2}=\frac1{16}T^{4/3},\qquad
\frac{T\Xi_T}{8\eta^2}=\frac18T^{1/3}\Xi_T\leq\frac18\Xi_T.
$$

Together with the remaining $\Xi_T/4$, this proves [](#eq:sol-bootstrap-clean), for example with $C=2$.
:::

## 3\. Evaluating the interface

:::{prf:lemma} Crude evaluation; [](#lem:crude)
:label: lem:sol-crude
For every isotropic log-concave $\mu$ on $\mathbb R^n$ and every $1/n\leq T\leq1$,

$$
\Xi_T(\mu)\leq1+\log(nT).
$$
:::

:::{prf:proof}
Taking the trace in the covariance SDE gives

$$
\dd\operatorname{Tr}A_t=\dd N_t-\operatorname{Tr}(A_t^2)\,\dd t
$$

for a continuous local martingale $N$. After localization, expectation kills $N$ and the drift is nonpositive. Since $\operatorname{Tr}A_t\geq0$, Fatou on removing the localization gives $\mathbb E\operatorname{Tr}A_t\leq\operatorname{Tr}A_0=n$. Hence $\mathbb E X_t\leq\mathbb E\lambda_{\max}(A_t)\leq n$.

For $t>0$, the Brascamp–Lieb covariance cap $A_t\preceq t^{-1}I$ gives $X_t\leq(t^{-1}-1)_+\leq t^{-1}$. Therefore

$$
\mathbb E X_t\leq\min(n,t^{-1}),
$$

and, because $T\geq1/n$,

$$
\Xi_T\leq\int_0^{1/n}n\,\dd t+
\int_{1/n}^T\frac{\dd t}{t}
=1+\log(nT).
$$

This is only the crude upper fence. In accordance with `obs:crude-insufficient`, it is not used as a dimension-free KLS input.
:::

:::{prf:corollary} Polylogarithmic evaluation; [](#cor:loglog)
:label: cor:sol-loglog
Under [](#hyp:KI), for $t_1(n)=c_0(\log n)^{-C_2}$, $\mathbb E\|A_t\|_{\mathrm{op}}\leq C_1$ on $[0,t_1(n)]$. If $t_1(n)\leq T\leq1$, then

```{math}
:label: eq:sol-loglog-interface
\Xi_T(\mu)\leq C_1t_1(n)+\log(T/t_1(n))
\leq C(1+\log\log n).
```

If also $T<1/8$, $\varepsilon\leq T^{1/3}$, and $\mu,E$ satisfy the hypotheses of [](#thm:sol-bootstrap), then

```{math}
:label: eq:sol-loglog-supply
\int_0^T\mathbb E[\bar e_t(E)\mathbf 1_{\{t<\tau_\eta\}}]\,\dd t
\leq Te_0+C h_\mu(T^{4/3}+1+\log\log n),
\qquad \eta=T^{1/3}.
```
:::

:::{prf:proof}
On $[0,t_1]$, $X_t\leq\|A_t\|_{\mathrm{op}}$, so the assumed expectation bound contributes at most $C_1t_1$. On $[t_1,T]$, Brascamp–Lieb gives $X_t\leq t^{-1}$. Integration proves the first inequality in [](#eq:sol-loglog-interface). Since $T\leq1$ and $t_1=c_0(\log n)^{-C_2}$,

$$
\log(T/t_1)\leq C_2\log\log n-\log c_0,
$$

and the fixed low-dimensional cases can be absorbed into the universal constant. This proves the second inequality. Substitution into [](#eq:sol-bootstrap-clean) proves [](#eq:sol-loglog-supply). The published discharge [](#cor:KI-discharged) establishes [](#hyp:KI) with $C_2=2$; no numerical evidence is used here.
:::

## 4\. The all-measure relative-scale ceiling

:::{prf:proposition} Relative-scale ceiling; [](#prop:ceiling)
:label: prop:sol-ceiling
Fix $\kappa\in(0,1]$ and a universal $T_0>0$ such that $9(1+\kappa)T_0\leq1/2$. If

```{math}
:label: eq:sol-ceiling-assumption
\Xi_{T_0}(\mu)\leq\kappa T_0
```

held for every isotropic log-concave $\mu$, then KLS would follow directly, with no geometric input. Thus using the clean bootstrap upper bound to certify a relative-scale propagation estimate would demand an all-measure covariance input already sufficient for KLS; no converse or equivalence is asserted.
:::

:::{prf:proof}
For every positive semidefinite $A$, $\lambda_{\max}(A)\leq1+(\lambda_{\max}(A)-1)_+$. Hence [](#eq:sol-ceiling-assumption) gives

```{math}
:label: eq:sol-ceiling-lambda
\int_0^{T_0}\mathbb E\lambda_{\max}(A_t)\,\dd t
\leq(1+\kappa)T_0.
```

Fix a balanced cut, $p_0=1/2$, and let $\tau=\inf\{t:p_t\notin[1/3,2/3]\}$. The stopped mass martingale is bounded. If $\tau\leq T_0$, its displacement reaches $1/6$, so the $L^2$ maximal inequality and the martingale isometry give

$$
\begin{split}
\mathbb P(\tau\leq T_0)
&\leq36\,\mathbb E[p]_{T_0\wedge\tau}\\
&\leq9\int_0^{T_0}\mathbb E[\mathbf 1_{\{t<\tau\}}
\lambda_{\max}(A_t)]\,\dd t\\
&\leq9(1+\kappa)T_0\leq\frac12,
\end{split}
$$

where the second line is [](#eq:sol-mass-qv-bound) without the last replacement by $X_t$, and the third is [](#eq:sol-ceiling-lambda). Therefore, with probability at least $1/2$, $\min(p_{T_0},q_{T_0})\geq1/3$. The balanced-survival lemma ([](#lem:survival-implies-kls)) now supplies a universal lower bound for the perimeter of every balanced cut and hence proves KLS.

Finally, [](#eq:sol-bootstrap-clean) bounds the bootstrap error by $C h_\mu(T^{4/3}+\Xi_T)$. Making this particular certificate no larger than $\kappa h_\mu T$ at a sufficiently small universal time asks, term by term, for $\Xi_T\lesssim\kappa T$ (as well as $T^{1/3}\lesssim\kappa$). The implication just proved shows why such an *all-measure* input is already KLS-strength. This is the precise method-specific meaning of the proposition's final sentence; it is not a logical necessity for every possible propagation proof.
:::

**Obstructions respected.** [](#thm:sol-bootstrap) respects `obs:circularity`: its profile lower bound comes from the external worst-case constant $\hstar_n$ and the explicit near-worst assumption $h_\mu\leq(1+\varepsilon)\hstar_n$, not from an assumed lower bound on the random localized profile. [](#lem:sol-crude) respects `obs:crude-insufficient` by proving and labeling the $\log n$ estimate only as an insufficient fence; the actual corollary uses the published small-time covariance input. [](#prop:sol-ceiling) proves only the sufficient implication that generates `obs:relative-ceiling`; it does not claim an equivalence and does not confuse the all-measure condition with the near-worst route.
