---
numbering:
  enumerator: "26.%s"
---

(sec:models)=
# Model geometries: the Gaussian and product brackets

The architecture should be tested where the answer is known. This section records the exact behavior of the program's quantities on the two canonical models and identifies the genuine stress test.

## Gaussian initial data: deterministic covariance, active damping, zero excess

:::{prf:proposition} Gaussian model
:label: prop:gaussian-model
Let $\mu=\gamma_n$ be the standard Gaussian. Then:

(i) the covariance is deterministic: $A_t=(1+t)^{-1}I_n$ for all $t$;

(ii) the centroid mechanism closes unconditionally: $\E\int_0^T\lmax(A_t)\dd t\le T$, hence by [](#eq:qv-p) and Doob, $\Prob(\tau\le T)\le9T\le\tfrac12$ for $T\le\tfrac1{18}$, and the conclusion of [](#thm:centroid-implies-kls) holds — recovering the Gaussian isoperimetric bound up to universal constants, without any Carleson input;

(iii) for every halfspace cut $E=\{x_1\le x_0\}$, the excess vanishes identically along the flow: $e_t(E)\equiv0$;

(iv) for every halfspace cut, the damping is strictly active: writing $\sigma_t^2=(1+t)^{-1}$ and $r_t=\sigma_t^2\varphi(\alpha_t)^2/s_t$ with $\alpha_t$ the normalized cut level,

$$
r_t\le\frac2\pi\,\sigma_t^2,
\qquad
D_t=r_t\bigl(2\sigma_t^2-r_t\bigr)\ \ge\ \Bigl(2-\frac2\pi\Bigr)\sigma_t^2\,r_t\ >\ 0 .
$$
:::

:::{prf:proof}
(i) For Gaussian $\mu_t$ all third moments vanish, so the martingale part of the covariance SDE [](#eq:cov-sde) vanishes and $\dot A_t=-A_t^2$, $A_0=I$, giving $A_t=(1+t)^{-1}I$. (ii) is [](#eq:trivial-lambda) with the deterministic bound $\lmax\le1$. (iii) $\mu_t=N(a_t,\sigma_t^2I)$, and after the similarity $x\mapsto(x-a_t)/\sigma_t$ the measure is standard Gaussian while Minkowski content scales by $\sigma_t^{-1}$; halfspaces are exact Gaussian isoperimetric minimizers at every volume, so $\mu_t^+(E)=\varphi(\beta_t)/\sigma_t=I_{\mu_t}(p_t)$ with $p_t=\Phi(\beta_t)$. (iv) For the one-dimensional Gaussian marginal cut at normalized level $\alpha$, $\abs{\delta_t}=\sigma_t\varphi(\alpha)/s$, so $r=s\abs\delta^2=\sigma^2\varphi(\alpha)^2/s$ and, since $A_t$ is scalar, $D=2s\,\delta^TA\delta-r^2=2\sigma^2r-r^2=r(2\sigma^2-r)$. The even function $\alpha\mapsto\varphi(\alpha)^2/(\Phi(\alpha)\Phi(-\alpha))$ has maximum value $4\varphi(0)^2=\tfrac2\pi$ at $\alpha=0$: since $\varphi(\alpha)^2=\tfrac1{2\pi}e^{-\alpha^2}$ and $4\Phi(\alpha)\Phi(-\alpha)=1-(2\Phi(\alpha)-1)^2$, the bound $\varphi(\alpha)^2\le\tfrac2\pi\Phi(\alpha)\Phi(-\alpha)$ is equivalent to $(2\Phi(\alpha)-1)^2\le1-e^{-\alpha^2}$, i.e. to the elementary error-function inequality $\operatorname{erf}(x)^2\le1-e^{-2x^2}$ at $x=\alpha/\sqrt2$. Hence $r\le\tfrac2\pi\sigma^2<2\sigma^2$.
:::

:::{prf:remark}
The Gaussian model validates the consumption machinery — the centroid reduction, the role of $\lmax$, and the sign of the damping — but it does not test [](#ass:all-cut-carleson): the covariance never inflates, so the dangerous regime is never visited. The model in which the dangerous regime is provably visited while the answer is still known is the product model.
:::

## Product measures: the genuine stress test

:::{prf:proposition} Product structure under localization; KLS for products
:label: prop:products
Let $\mu=\bigotimes_{i=1}^n\mu^{(i)}$ be a product of isotropic one-dimensional log-concave measures. Then:

(i) $\mu_t$ is a product measure for every $t$, pathwise: the localization tilt $\exp(c_t\cdot x-\tfrac t2\abs x^2)$ factorizes across coordinates; consequently $A_t$ is diagonal, with entries $A_t^{(i)}=\Var(\mu_t^{(i)})$ evolving as one-dimensional variance processes;

(ii) each $A^{(i)}$ is a nonnegative supermartingale (drift $-(A^{(i)})^2$), so $\Prob(\sup_{s\le t}A_s^{(i)}\ge\lambda)\le1/\lambda$ for every $\lambda\ge1$;

(iii) $h_{\mu_t}\ \ge\ c\,\min_i\bigl(A_t^{(i)}\bigr)^{-1/2} =c\,\lmax(A_t)^{-1/2}$ pathwise, with $c$ universal; in particular KLS holds for products, and the excess of any cut propagates through the direct profile bound, with no bootstrap needed.
:::

:::{prf:proof}
(i) The density of $\mu_t$ is proportional to $\prod_ie^{-V_i(x_i)}\cdot\exp(c_{t,i}x_i-\tfrac t2x_i^2)$, a product; the coordinates remain independent and the variance dynamics decouple. (ii) is the scalar case of the covariance SDE. (iii) The Poincaré constant tensorizes, $\CP(\mu_t)=\max_i\CP(\mu_t^{(i)})$, each one-dimensional log-concave factor satisfies $\CP(\mu_t^{(i)})\le C\Var(\mu_t^{(i)})$, and for log-concave measures the Cheeger and Poincaré constants are equivalent up to universal factors (Buser–Ledoux; see [@BakryGentilLedoux2014; @LeeVempala2018]). Hence $h_{\mu_t}\ge c\min_i\Var(\mu_t^{(i)})^{-1/2}$, which is (iii) since $\lmax(A_t)=\max_iA_t^{(i)}$.
:::

:::{prf:remark} Why products are the stress test
:label: rem:product-stress
It is known that for products of two-sided exponentials a single eigenvalue of $A_t$ can reach size of order $\log n$ at times of order $1/\log n$; see the discussion of covariance growth in [@Chen2021; @KlartagLehec2022Polylog]. Thus, on the product model, $\lmax(A_t)$ provably enters the regime against which [](#eq:trivial-lambda) warns, while the KLS conclusion is nevertheless true by [](#prop:products)(iii). Consequently:
:::

:::{prf:remark} Product stress test of the all-cut estimate
:label: rem:product-stress-test
Decide whether [](#ass:all-cut-carleson) holds for product measures. A proof cannot go through $\lmax(A_t)$ control — the operator norm genuinely reaches $\log n$ — and is therefore forced to exploit the cut-specific quantities $G_t,K_t,D_t$, which is exactly the discipline the general case demands; the available structure is independence, one-dimensional log-concave estimates, and the explicit variance dynamics of [](#prop:products). A counterexample cannot use a fixed cut depending on a single coordinate, even one whose variance later inflates ([](#cor:single-coordinate-cuts)); it needs a fixed cut of unbounded coordinate complexity whose source is aligned with the inflation excursions of many coordinates at once ([](#conj:product-alignment)). The two outcomes do not weigh the same. A proof for products would exhibit, on a model where the dangerous covariance regime is visited, the cut-aware mechanism that [](#ass:tight-prefix-carleson) needs in general. A failure would be a counterexample to the every-interval estimate on measures that satisfy KLS ([](#prop:products)). It would not by itself decide [](#ass:tight-prefix-carleson), the prefix form that [](#cor:tight-window-consumption) consumes: [](#ass:all-cut-carleson) implies it, and no converse is known, so the product cut would have to violate the prefix form on the tight window as well. Nor would a failure select the near-Cheeger variant: the product witnesses of [](#prop:weighted-spectator-obstruction) already violate the propagation clause of its literal package [](#ass:weighted-package), removing the weight does not save the superlinear remainder ([](#prop:spectator-excess-rate-obstruction)), and its trace clause [](#conj:stein-weighted) yields nothing toward KLS until a propagation statement that survives such products is formulated. A witness cut of large excess would only leave untouched the estimates restricted to near-minimizing cuts, where such a statement would live.
:::

## The non-model obstruction

The two-tail family of [](#prop:two-tail) marks the boundary of what model verification can establish: it is a family of perfectly explicit Gaussian configurations on which the slice-wise form of the Stein-trace estimate fails, while every genuinely dynamical question about it (the expected occupation of the inflated states from isotropic initial data) is of Carleson type. Model geometries can validate machinery and falsify formulations — both have happened in this manuscript, the second through the product witnesses of [](#prop:weighted-spectator-obstruction) — but the Carleson hypotheses [](#ass:all-cut-carleson) and [](#ass:tight-prefix-carleson), and the trace estimate [](#conj:stein-weighted), are irreducibly dynamical.
