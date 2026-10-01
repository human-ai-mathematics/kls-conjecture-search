---
title: "Solution: residual dichotomy of the near-worst bootstrap"
ledger-node: cor:dichotomy
numbering:
  enumerator: "109.%s"
---

**Overview.** This dossier proves [](#cor:dichotomy), conditional on the quantified completion in [](#ass:absolute-geometric-completion). The completion remains an antecedent throughout.

1. Match the stopping width and the near-worst parameter to the bootstrap, and choose a dimension threshold on which the published covariance window reaches the fixed completion time.
2. Use [](#cor:loglog) to supply the completion whenever the dimension's worst Cheeger constant is sufficiently small.
3. Apply the completion to an actual sequence of balanced near-minimizers. Its perimeter lower bound contradicts the assumed small Cheeger constant.

**Refined statement.**

:::{prf:theorem} Residual dichotomy; [](#cor:dichotomy)
:label: thm:sol-dichotomy
Under [](#ass:absolute-geometric-completion), there exist constants $a>0$ and an integer $N\ge3$, depending only on its universal constants and those in [](#cor:loglog) and [](#cor:KI-discharged), such that

$$
\hstar_n\ge\frac{a}{1+\log\log n}\qquad(n\ge N).
$$

In particular, $\hstar_n\ge a/(2\log\log n)$ for all sufficiently large $n$.
:::

:::{prf:proof}
Fix constants $T_0\in(0,1/8)$ and $\kappa,c_g,\eps_g,\delta_g>0$ witnessing [](#ass:absolute-geometric-completion). Throughout the proof the stopping width is exactly

$$
\eta=T_0^{1/3}\in(0,1/2).
$$

Choose once and for all

$$
\eps=\frac12\min\{1,\eps_g,T_0^{1/3}\}>0.
$$

The published discharge [](#cor:KI-discharged) supplies [](#ass:KI) with universal constants $c_0,C_1>0$ and $t_1(n)=c_0(\log n)^{-2}$ for $n\ge3$. Since $t_1(n)\to0$, choose an integer $N\ge3$ such that $t_1(n)\le T_0$ for every $n\ge N$. Enlarge $N$ if necessary so that

$$
L_n:=1+\log\log n\ge1\qquad(n\ge N).
$$

Let $C_L>0$ be the universal constant in the supply inequality [](#eq:loglog-supply). Set

$$
a=\min\left\{\frac{\kappa T_0}{4C_L},\frac{c_g}{2}\right\}>0.
$$

Fix $n\ge N$ and suppose, for a contradiction, that $\hstar_n\le a/L_n$. The established finite-dimensional bound [](#thm:klartag-logn) gives $\hstar_n>0$. Also $\hstar_n<\infty$: the standard Gaussian is an admissible isotropic law and a balanced coordinate halfspace has finite perimeter. The definition [](#eq:hstar-def) of the infimum therefore supplies an isotropic log-concave probability $\mu$ on $\mathbb R^n$ with

$$
h_\mu\le(1+\eps)\hstar_n\le2\hstar_n.
$$

This is simultaneously within the near-worst class of the completion and the class of [](#thm:bootstrap), with $\eps\le T_0^{1/3}$.

By [](#lem:half), $I_\mu(1/2)=h_\mu/2$. By the definition of $I_\mu(1/2)$ as an infimum over balanced measurable cuts, for every integer $j\ge1$ there is such a cut $E_j$ with

$$
0\le e_j:=\mu^+(E_j)-I_\mu(1/2)<\min\{\delta_g,j^{-1}\}.
$$

In particular, every $E_j$ has finite initial lower outer Minkowski perimeter, is admissible for the completion, and satisfies $e_0(E_j)=\bar e_0(E_j)=e_j$. No existence of an exactly minimizing cut is needed.

All time, dimension, and near-worst hypotheses of [](#cor:loglog) now hold. Apply its supply estimate separately to each fixed $E_j$, using its own mass process and stopping time $\tau_\eta(E_j)$. Since $T_0^{4/3}\le1\le L_n$, it gives

$$
\begin{aligned}
\int_0^{T_0}\mathbb E\bigl[\bar e_t(E_j)\mathbf1_{\{t<\tau_\eta(E_j)\}}\bigr]\,\mathrm dt
&\le T_0e_j+C_Lh_\mu(T_0^{4/3}+L_n)\\
&\le T_0e_j+4C_L\hstar_nL_n\\
&\le T_0e_j+\kappa T_0.
\end{aligned}
$$

Thus [](#ass:absolute-geometric-completion) implies $\mu^+(E_j)\ge c_g$ for every $j$. Passing to the limit in the scalar perimeter values, which converge to $I_\mu(1/2)$ by construction, gives

$$
h_\mu=2I_\mu(1/2)\ge2c_g.
$$

On the other hand, the hypothesized smallness and the choice of $a$ give

$$
h_\mu\le2\hstar_n\le\frac{2a}{L_n}\le c_g,
$$

a contradiction. We have proved $\hstar_n>a/L_n$, which implies the claimed weak inequality. Finally, once $\log\log n\ge1$, one has $1+\log\log n\le2\log\log n$, proving the last assertion.
:::

:::{prf:remark} Matched-time implication, separate from the corollary
:label: rem:sol-dichotomy-matched-time
Here is the additional quantitative condition needed for the full KLS conclusion mentioned in the surrounding manuscript discussion. Let $C_B>0$ be a universal constant valid in the clean bootstrap inequality [](#eq:clean-form). Suppose, in addition to the completion, that there is a universal $\eps_t>0$ such that, for every $n\ge2$ and every isotropic log-concave $\mu$ with $h_\mu\le(1+\eps_t)\hstar_n$,

$$
h_\mu\bigl(T_0^{4/3}+\Xi_{T_0}(\mu)\bigr)
\le\frac{\kappa}{C_B}T_0,
$$

at the very same $T_0$ fixed by the completion. Then $\hstar_n\ge2c_g$ for every $n\ge2$.

Indeed, fix $n\ge2$ and choose positive $\eps_k\downarrow0$ with $\eps_k\le\min\{1,\eps_g,\eps_t,T_0^{1/3}\}$. Positivity of $\hstar_n$ as above supplies near-worst measures $\mu_k$ with $h_{\mu_k}\le(1+\eps_k)\hstar_n$. The clean bootstrap at $\eta=T_0^{1/3}$ and the displayed additional hypothesis give the completion's supply for every balanced cut of $\mu_k$ with initial excess at most $\delta_g$. Applying the same balanced near-minimizing sequence argument gives $h_{\mu_k}\ge2c_g$. Therefore $(1+\eps_k)\hstar_n\ge2c_g$; letting $k\to\infty$ proves the assertion. Monotonicity from [](#lem:whitening) gives $\hstar_1\ge\hstar_2$, and the Cheeger formulation in [](#conj:kls) yields KLS.

The premise of [](#conj:taming) supplies a time depending on its requested error level. Even choosing that level at most $\min\{1,\kappa/C_B\}$ does not identify its time with the completion's time. This remark does not assert the additional matched-time estimate or a time-uniform completion, and neither is used in the proof of [](#cor:dichotomy).
:::

**Fences respected.** The node has no registered `bounded_by` edges. The contextual constraints are respected as follows. The circularity warning [](#rem:profile-circularity) is met by using the externally defined $\hstar_n$ and certified near-worst bootstrap, without inserting an unknown posterior profile bound. The crude-input warning [](#rem:crude-insufficient) is met by using the published polylogarithmic covariance window and retaining its $\log\log n$ loss. The relative-scale ceiling [](#rem:relative-ceiling) is respected: no all-measure dimension-free covariance bound is claimed. The spectator obstructions [](#prop:weighted-spectator-obstruction) and [](#prop:spectator-excess-rate-obstruction) are not bypassed: the completion is an explicit near-worst antecedent, and no uniform superlinear excess remainder is proved. The completion stays open, and the corollary's dimension-dependent conclusion does not settle KLS.
