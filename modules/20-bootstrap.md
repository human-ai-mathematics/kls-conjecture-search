---
numbering:
  enumerator: "20.%s"
---

(sec:bootstrap)=
# The bootstrap comparison theorem and the interface functional

## Two elementary lemmas

:::{prf:lemma} Balance pins the Cheeger ratio
:label: lem:half
For log-concave $\nu$, with the generalized concavity of the isoperimetric profile [@Bobkov1999LogConcave; @Milman2009Isoperimetric],

$$
h_\nu=2\,I_\nu(\tfrac12),
$$

and for any $E$ with $\nu(E)=\tfrac12$ the Cheeger excess $\bar e_0(E):=\nu^+(E)-h_\nu\min(p,q)$ equals $e_0(E)$.
:::

:::{prf:proof}
Milman's Theorem 1.8 and Corollaries 6.5 and 6.12 [@Milman2009Isoperimetric] give symmetry and concavity of the profile on $(0,1)$, including for nonsmooth log-concave laws in dimension one. The assigned endpoint value $I(0)=0$ need not equal $I(0^+)$: the uniform law on an interval of length $L$ has $I(p)=1/L$ for $0<p<1$.

For $0<\delta<p<1/2$, interior concavity and nonnegativity give

$$
I(p)\ge\frac{1/2-p}{1/2-\delta}I(\delta)
       +\frac{p-\delta}{1/2-\delta}I(1/2)
\ge\frac{p-\delta}{1/2-\delta}I(1/2).
$$

Letting $\delta\downarrow0$ yields $I(p)\ge2pI(1/2)$; symmetry handles $p>1/2$. Equality of the infimum follows by taking $p=1/2$, so $h_\nu=\inf_{0<p<1}I(p)/\min(p,1-p)=2I(1/2)$. For proper affine support, apply this argument in the affine hull; a Dirac law has no nontrivial-mass competitors. At mass $1/2$, the Cheeger line equals the profile, giving the excess identity. No endpoint continuity or profile minimizer is needed.
:::

:::{prf:definition} Cheeger excess
:label: def:cheeger-excess
$\bar e_t(E)=\mu_t^+(E)-h_{\mu_t}\min(p_t,q_t)\ \ge\ e_t(E)\ \ge0$, the excess over the Cheeger line rather than over the profile. It is the quantity that propagates through the bootstrap; since $\bar e\ge e$, any consumption stated for $e$ is implied.
:::

:::{prf:lemma} Whitening comparison
:label: lem:whitening
Let $\nu$ be log-concave on $\R^n$ with nondegenerate covariance $A_\nu$. Then

$$
h_\nu\ \ge\ \frac{\hstar_n}{\lmax(A_\nu)^{1/2}} ,
$$

so that almost surely $h_{\mu_t}\ge\hstar_n\,\lmax(A_t)^{-1/2}$ for $t>0$. Moreover $\hstar_n$ is nonincreasing in $n$.
:::

:::{prf:proof}
Let $\tilde\nu=A_\nu^{-1/2}{}_\#(\nu-a_\nu)$, isotropic log-concave, so $h_{\tilde\nu}\ge\hstar_n$, and $\nu=T_\#\tilde\nu+a_\nu$ with $T=A_\nu^{1/2}$, $\norm T_\op=\lmax^{1/2}$. For Borel $S$ and $\eps>0$, $T^{-1}(S_\eps)\supseteq(T^{-1}S)_{\eps/\norm T_\op}$, whence $\nu^+(S)\ge\tilde\nu^+(T^{-1}S)/\norm T_\op\ge(\hstar_n/\norm T_\op)\min(\nu(S),1-\nu(S))$. For monotonicity: if $\nu$ is isotropic log-concave on $\R^m$, $m\le n$, then $\nu\otimes\gamma_{n-m}$ is isotropic log-concave on $\R^n$ and cylinder sets give $h_{\nu\otimes\gamma_{n-m}}\le h_\nu$, so $\hstar_n\le\hstar_m$.
:::

## The main inequality

:::{prf:theorem} Bootstrap comparison
:label: thm:bootstrap
Let $n\ge2$, $\eps\in(0,1]$, and let $\mu$ be isotropic log-concave on $\R^n$ with $h_\mu\le(1+\eps)\hstar_n$ (a near-worst measure of its dimension). Let $E$ be *any* measurable set with $\mu(E)=\tfrac12$, $e_0=e_0(E)=\bar e_0(E)$, and let $\eta\in(0,\tfrac12)$. Then, with $X_t=(\lmax(A_t)-1)_+$ as in [](#eq:interface-def), for every $t>0$:

```{math}
:label: eq:bootstrap-main
\E\bigl[\bar e_t(E)\,\one_{\{t<\tau_\eta\}}\bigr]
\ \le\
e_0+h_\mu\Bigl(\frac\eps2+\eta+\frac12\,\Prob(\tau_\eta\le t)+\frac14\,\E X_t\Bigr),
```

```{math}
:label: eq:bootstrap-exit
\Prob(\tau_\eta\le t)\ \le\ \frac1{4\eta^2}\Bigl(t+\int_0^t\E X_s\dd s\Bigr).
```

Consequently, with $\Xi_T=\int_0^T\E X_t\dd t$,

```{math}
:label: eq:bootstrap-integrated
\int_0^T\E\bigl[\bar e_t\,\one_{\{t<\tau_\eta\}}\bigr]\dd t
\ \le\
T e_0+h_\mu\Bigl[\Bigl(\frac\eps2+\eta\Bigr)T
+\frac{T^2}{16\eta^2}+\frac{T\,\Xi_T}{8\eta^2}+\frac{\Xi_T}{4}\Bigr],
```

and, for $0<T<1/8$, the admissible choice $\eta=T^{1/3}<1/2$ together with $\eps\le T^{1/3}$ gives the clean form

```{math}
:label: eq:clean-form
\int_0^T\E\bigl[\bar e_t\,\one_{\{t<\tau_\eta\}}\bigr]\dd t
\ \le\ Te_0+C\,h_\mu\bigl(T^{4/3}+\Xi_T\bigr).
```
:::

*Proof.* Six steps: the perimeter supermartingale bounds the stopped perimeter by $\mu^+(E)$; whitening plus the elementary bound $\lambda^{-1/2}\ge1-\tfrac12(\lambda-1)_+$ converts that into a Cheeger statement on the balanced event; and the remaining steps collect the error terms into the interface functional. The calculation is carried out in Appendix [](#sec:appendix-fixed-cut).

:::{prf:theorem} Stopped covariance-interface refinement
:label: thm:bootstrap-stopped-interface
Under the hypotheses of [](#thm:bootstrap), define

$$
\widehat\Xi_{T,\eta}(\mu,E)
:=\int_0^T\E\bigl[X_s\one_{\{s<\tau_\eta\}}\bigr]\dd s.
$$

Then

```{math}
:label: eq:bootstrap-stopped-interface
\begin{aligned}
\int_0^T\E\bigl[\bar e_t(E)\one_{\{t<\tau_\eta\}}\bigr]\dd t
\le Te_0+h_\mu\biggl[
&\Bigl(\frac\eps2+\eta\Bigr)T+\frac{T^2}{16\eta^2}\\
&+\Bigl(\frac{T}{8\eta^2}+\frac14\Bigr)
\widehat\Xi_{T,\eta}(\mu,E)\biggr].
\end{aligned}
```

Consequently, for $0<T<1/8$, $\eta=T^{1/3}$, and $\eps\le T^{1/3}$,

$$
\int_0^T\E\bigl[\bar e_t(E)\one_{\{t<\tau_\eta\}}\bigr]\dd t
\le Te_0+C h_\mu\bigl(T^{4/3}+\widehat\Xi_{T,\eta}(\mu,E)\bigr).
$$

This is a stopped refinement of [](#thm:bootstrap), not a universal bound on the new interface.
:::

:::{prf:remark} Features
:label: rem:bootstrap-features
(a) The estimate holds for every balanced cut; near-minimality enters only through the size of $e_0$. The hypothesis is on the measure — near-worstness — which is exactly the hypothesis a proof by contradiction is entitled to. (b) All randomness is compressed into the scalar functional $\Xi_T$, and crucially $\Xi_T$ enters multiplied by $h_\mu$: in the contradiction regime $h_\mu\approx\hstar_n$ is small, so the bootstrap tolerates covariance excursions of size up to $\sim1/\hstar_n$ — a genuine weakening of the operator-norm control warned about at [](#eq:trivial-lambda). (c) A pathwise variant holds with constant probability: on $\{\tau_\eta>T\}\cap\{\sup_{t\le T}\lmax(A_t)\le1+\sigma\}\cap\{\sup_{t\le T}\mu_t^+(E)\le (1+\theta)\mu^+(E)\}$ — the last event of probability $\ge\theta/(1+\theta)$ by Doob's maximal inequality for the nonnegative perimeter martingale — the same algebra gives $\sup_{t\le T}\bar e_t\le(1+\theta)e_0+h_\mu(\theta+\tfrac\eps2+\eta+\tfrac\sigma4)$ pathwise. Since the final consumption only requires events of probability $\ge\tfrac12$, constant probability may suffice for a future stability argument needing pathwise near-minimality.
:::

(subsec:interface)=
## Evaluating the interface functional

:::{prf:lemma} Crude evaluation
:label: lem:crude
For every isotropic log-concave $\mu$ on $\R^n$ and $1/n\le T\le1$, $\Xi_T(\mu)\le1+\log(nT)$.
:::

:::{prf:proof}
$\Tr A_t$ has drift $-\Tr A_t^2\le0$ by [](#eq:cov-sde), so $\E\lmax(A_t)\le\E\Tr A_t\le n$; combine with the pathwise cap $X_t\le(t^{-1}-1)_+$ from [](#eq:BL-cap), so $\E X_t\le\min(n,t^{-1})$, and integrate splitting at $t=1/n$.
:::

:::{prf:remark} The crude evaluation is provably insufficient — by Klartag's theorem
:label: rem:insufficiency
For [](#eq:clean-form) to yield even an $O(T)$ excess bound with a small constant one needs $h_\mu\Xi_T\le CT$, which under [](#lem:crude) requires $h_\mu\le CT/\log n$. But, conditional on the July 2026 version-1 preprint of Letwin, $h_\mu\ge\hstar_n\ge c(\log n)^{-1/4}$ [@Letwin2026QuadraticKLS]; even the earlier published bound $c(\log n)^{-1/2}$ [@Klartag2023Logarithmic] exceeds $CT/\log n$ for all large $n$. The crude bound therefore never suffices in high dimension: known lower bounds for KLS are themselves an obstruction to the naive bootstrap. Any useful evaluation of $\Xi_T$ must beat $\log n$.
:::

The polylogarithmic covariance technology does beat it. The required input is the small-time operator-norm control imported in Section [](#sec:covariance-tech) ([](#ass:KI)), discharged there on the published $c/\log^2 n$ window and, conditional on the version-1 input of [](#thm:letwin-qcts), on the larger $c/\log n$ window ([](#cor:KI-discharged) and [](#cor:KI-letwin)).

:::{prf:corollary} Polylog evaluation
:label: cor:loglog
Under [](#ass:KI), for $t_1(n)\le T\le1$, $\Xi_T(\mu)\le C_1t_1(n)+\log(T/t_1(n))\le C(1+\log\log n)$. Hence, when additionally $T<1/8$ and the near-worst parameter satisfies $\eps\le T^{1/3}$, every such $\mu$ and every balanced cut $E$ satisfy, by [](#eq:clean-form),

```{math}
:label: eq:loglog-supply
\int_0^T\E\bigl[\bar e_t\,\one_{\{t<\tau_\eta\}}\bigr]\dd t
\ \le\ Te_0+C\,h_\mu\bigl(T^{4/3}+1+\log\log n\bigr).
```
:::

:::{prf:proof}
On $[0,t_1]$, $\E X_t\le\E\norm{A_t}_\op\le C_1$; on $[t_1,T]$, $X_t\le t^{-1}$ pathwise.
:::

:::{prf:proposition} The relative-scale ceiling
:label: prop:ceiling
Fix $\kappa\in(0,1]$ and a universal $T_0>0$ satisfying

```{math}
:label: eq:ceiling-smallness
9(1+\kappa)T_0\le\frac12.
```

If $\Xi_{T_0}(\mu)\le\kappa T_0$ held for every isotropic log-concave $\mu$, the KLS conjecture would follow directly, with no geometric input. Consequently, a propagation estimate at relative scale — $\int_0^T\E\bar e_t\dd t\le\kappa h_\mu T$ with $\kappa$ small — cannot be expected from [](#thm:bootstrap) alone: deriving it through [](#eq:clean-form) would require $\Xi_T\le c\kappa T$ at a sufficiently small universal time, an input already sufficient for the conclusion of the whole program.
:::

:::{prf:proof}
$\Xi_{T_0}\le\kappa T_0$ gives $\int_0^{T_0}\E\lmax(A_t)\dd t\le(1+\kappa)T_0$. By [](#eq:qv-p) and [](#eq:trivial-lambda), $\dd[p]_t\le\tfrac14\lmax(A_t)\dd t$, so for any balanced cut

$$
\Prob(\tau\le T_0)
\le36\,\E[p]_{T_0\wedge\tau}
\le9\int_0^{T_0}\E\lmax(A_t)\dd t
\le9(1+\kappa)T_0\le\frac12.
$$

[](#lem:survival-implies-kls) applies at the universal time $T_0$ with survival probability at least $1/2$.
:::

:::{prf:remark} The supply curve and the corridor
:label: rem:supply
Assembling this section and the previous one, the propagation estimates available at each scale are:

| Scale of the excess bound | Scope | Source |
|---|---|---|
| Absolute, $\le C(1+e_0)T$ | No hypothesis: all $\mu$, all balanced $E$ | [](#prop:trivial-excess). |
| Absolute with small constant, $\le Te_0+\kappa T$ | Holds for near-worst $\mu$ whenever $h_\mu(1+\log\log n)\le c\kappa T$; conditional on Ass. [](#ass:KI) | [](#cor:loglog); the universal-time near-worst extension is [](#conj:taming). |
| Relative, $\le\kappa\,h_\mu T$ | Making the upper bound in [](#eq:clean-form) small term by term requires $\Xi_T\le c\kappa T$, alongside control of $e_0$ and $T^{1/3}$. If proved for every isotropic log-concave $\mu$ at a sufficiently small universal time, this covariance bound would imply KLS. A large upper bound gives no lower bound on the actual excess. [](#conj:taming) asks instead for near-worst, $h_\mu$-weighted control. | [](#prop:ceiling). |

On the demand side, [](#prop:two-tail) shows the Stein-trace estimate cannot be satisfied slice-wise with absolute-scale excess. The corridor between what can be supplied and what must be demanded is the residual content of the approach, posed precisely in Section [](#sec:open).
:::

:::{prf:remark} Product measures: sanity check, and why the bootstrap is silent there
:label: rem:products-bootstrap
For product $\mu$ (Section [](#sec:models)), $A_t$ is diagonal, each entry a nonnegative supermartingale (drift $-A^2$), so $\Prob(\sup_{s\le t}A^{(i)}_s\ge\lambda)\le1/\lambda$ by the maximal inequality. A more careful small-time analysis of the $n$ independent variance processes — which we do not carry out — suggests $\Xi_T\asymp\log\log n$ for products of two-sided exponentials, matching [](#cor:loglog) and consistent with the known observation that a single eigenvalue can reach order $\log n$, saturating the cap [](#eq:BL-cap) at $t\asymp1/\log n$ [@Chen2021; @KlartagLehec2022Polylog]. For products, however, $h_\mu\asymp1\gg\hstar_n$ in any hypothetical bad regime, so the near-worstness hypothesis fails and the bootstrap is vacuous — correctly so: products cannot be counterexamples, and their excess propagation follows directly from $h_{\mu_t}\ge c\,\lmax(A_t)^{-1/2}$ by tensorization ([](#prop:products)).
:::

(subsec:bootstrap-barriers)=
## Methodological constraints from this section

Both remarks below are methodological constraints on the bootstrap input, warnings rather than theorems; later sections use them as heuristic barriers, never as a step in a proof.

:::{prf:remark} The crude covariance integral cannot bootstrap
:label: rem:crude-insufficient
The crude bound $\Xi_T\lesssim\log n$ of [](#lem:crude), discussed in [](#rem:insufficiency), is too large to yield the required excess estimate at known KLS lower-bound scales. A viable bootstrap input must improve the logarithm; the available polylogarithmic technology reaches only the scale of [](#cor:loglog).
:::

:::{prf:remark} An all-measure relative bound already implies KLS
:label: rem:relative-ceiling
By [](#prop:ceiling), a bound $\Xi_{T_0}(\mu)\le\kappa T_0$ for every isotropic log-concave measure at a sufficiently small universal time is sufficient for KLS. No converse is established here. The proposition explains the strength of that particular covariance input; it does not rule out proving it or obtaining propagation by another argument. [](#conj:taming) instead asks for a near-worst, $h_\mu$-weighted bound.
:::
