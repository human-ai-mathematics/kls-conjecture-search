---
numbering:
  enumerator: "23.%s"
---

% This heading keeps "Route": a statement links to this section, and the checker's
% fingerprint includes a linked heading's text, so renaming it would lift certifications.
(sec:stein)=
# Route E–B: the failed literal weighted package and boundary Stein traces

The geometric variant Eldan–B trades the all-cut hypothesis for near-minimality. Its stochastic currency is the two-color covariance functional $\calS_\nu(E)=s^2\norm K_\HS^2$ of the Stein dictionary (Section [](#sec:stein-dictionary)); here we give its second exact form as a boundary flux and give the argument for [](#thm:intro-weighted), using the results of Section [](#sec:excess). The conversion between the Stein functional and the Riccati source ([](#lem:stein-vs-source)) is lossless on the tight window and is recorded with the dictionary.

## The boundary representation and the trace estimate

The name “Stein trace” refers to the second exact form of $\ell_{\nu,E}$, as a boundary flux.

:::{prf:lemma} Boundary representation
:label: lem:boundary-rep
Let $K$ be a smooth bounded convex domain and $\nu=Z^{-1}e^{-V}\one_Kdx$, with $V$ smooth and convex on $\overline K$. Let $E$ be smooth relative to $K$, put $\Sigma=\partial^*E\cap\operatorname{int}K$, and let $n$ be its inner unit normal. For smooth $f$ with $\nu$-mean $\bar f$, let $u_f$ be the mean-zero weak solution of the Neumann Poisson problem

$$
Lu_f=f-\bar f\quad\text{in }K,
\qquad \partial_{n_K}u_f=0\quad\text{on }\partial K,
\qquad L=\Delta-\nabla V\cdot\nabla .
$$

Then

```{math}
:label: eq:boundary-rep
\Cov_\nu(\one_E,f)
=\int_E(f-\bar f)\dd\nu
=-\int_\Sigma \partial_nu_f\dd\sigma_\nu ,
```

and in particular, by Cauchy–Schwarz on the weighted surface measure of total mass $\nu^+(E)$,

```{math}
:label: eq:trace-CS
\abs{\ell_{\nu,E}(M)}^2
\;\le\;\nu^+(E)\,\int_\Sigma\abs{\partial_nu_{M}}^2\dd\sigma_\nu ,
\qquad u_M:=u_{f_M} .
```

Here $f_M(x)=(x-a_\nu)^TM(x-a_\nu)-\Tr(MA_\nu)$ is the centered quadratic from [](#prop:stein-rep).
:::

:::{prf:proof}
$\int_E(f-\bar f)\dd\nu=Z^{-1}\int_E\operatorname{div}(e^{-V}\nabla u_f)dx$. The divergence theorem on $E\cap K$ gives the displayed flux on $\Sigma$ with the inner normal; the contribution on $\partial K\cap E$ vanishes by the Neumann condition. Existence and uniqueness up to constants are the standard centered Neumann problem on the smooth bounded weighted domain; the mean-zero normalization fixes the constant.
:::

:::{prf:remark} What the stable Stein-trace estimate is
:label: rem:what-stein-is
Estimate [](#eq:intro-weighted-stein) is, through [](#eq:stein-norm-def)–[](#eq:trace-CS), a *trace estimate for Poisson solutions with quadratic data*, integrated along the localization and tested against near-minimal cuts: the boundary energy $\int_\Sigma\abs{\partial_nu_M}^2\dd\sigma_\nu$ must, after absorption of the damped modes, be controlled at the Carleson scale. The natural tool for converting boundary traces into interior energies is the weighted Reilly identity, and the natural geometric input for near-minimal $\Sigma$ is the second-variation stability of Section [](#sec:jacobi). Two warnings constrain any such proof: by [](#prop:two-tail) it cannot proceed one time-slice at a time with an absolute-scale excess term, and by the consumption audit ([](#prop:intro-audit)(b)) an absolute-scale excess term would carry no logical weight anyway. The covariance-weighted trace estimate [](#eq:intro-weighted-stein) remains a meaningful geometric target, but it is not by itself part of a working package: [](#prop:weighted-spectator-obstruction) shows that its paired global-operator-norm propagation clause fails on spectator products, while [](#prop:spectator-excess-rate-obstruction) rules out the same uniform superlinear remainder even at weight one. Any replacement must first choose a cut-local or tensor-stable scale and a surviving remainder or near-worst premise, then re-audit the trace estimate against both.
:::

(subsec:consumption)=
## Consumption: the argument for [](#thm:intro-weighted)

:::{prf:proof} Proof of [](#thm:intro-weighted)
Assume the weighted package ([](#ass:weighted-package)). Thus its fixed tight-window parameter satisfies $2\beta+64\eta^2<1$. Suppose, for contradiction, that KLS fails, and let $(\mu_k,E_k)$ be a sequence of isotropic log-concave measures and balanced near-Cheeger cuts with $\mu_k^+(E_k)\to0$ and $e_0(E_k)\le1$; this is the near-minimizer reduction in the remark following [](#thm:centroid-implies-kls). Choose once and for all $\alpha\in(2\beta+64\eta^2,1)$. In particular, the assumed value of $\eta$ is small enough for the tight-window conversion below; no stopping window is chosen after the two package estimates have been supplied.

By [](#lem:stein-vs-source) and the weighted Stein-trace estimate [](#eq:intro-weighted-stein),

$$
\begin{aligned}
\E\int_0^{T\wedge\tau_\eta}S_t\dd t
&\le2C_0T+2C_1\E\int_0^{T\wedge\tau_\eta}r_t\dd t \\
&\quad
+\bigl(2\beta+64\eta^2\bigr)\E\int_0^{T\wedge\tau_\eta}D_t\dd t \\
&\quad
+2C_2\,\E\int_0^{T\wedge\tau_\eta}
e_t\bigl(1+\norm{A_t}_\op\bigr)^{5/2}\dd t ,
\end{aligned}
$$

where the additional $64\eta^2D$ comes from the conversion. By weighted excess propagation [](#eq:intro-weighted-excess), the last term is at most $2C_2^2\bigl(Te_0+T^{1+\gamma}\bigr)\le2C_2^2(1+T^\gamma)\,T\le4C_2^2\,T$ for $T\le T_0\wedge1$. This is an absorptive two-color Carleson estimate on the tight window with universal constants $C_0'=2C_0+4C_2^2$, $C_1'=2C_1$ and damping coefficient $\alpha<1$, on the tight window from time zero. Since $\eta$ was fixed above (universally, with $\eta<\tfrac16$), this is exactly the hypothesis [](#eq:tight-carleson) of the tight-window consumption [](#cor:tight-window-consumption), applied to each $(\mu_k,E_k)$ (which has $p_0=\tfrac12$). It produces a universal constant $c'>0$ with $\mu_k^+(E_k)\ge c'$ for all $k$, contradicting $\mu_k^+(E_k)\to0$. Hence $\inf_n\hstar_n>0$.
:::

:::{prf:remark}
The proof shows that the only place the excess enters the consumption is through the single scalar $\E\int e_t(1+\norm{A_t}_\op)^{5/2}\dd t$, and that any bound of size $O(T)$ for it, with universal constant, suffices. The stronger $T^{1+\gamma}$ remainder in [](#eq:intro-weighted-excess) is not needed for consumption, and the literal uniform premise fails on spectator products ([](#prop:weighted-spectator-obstruction)). The unweighted spectator obstruction ([](#prop:spectator-excess-rate-obstruction)) shows that merely replacing the covariance weight does not rescue that remainder. A replacement may instead allow an $O(T)$ supply tied to a near-worst hypothesis, or use a remainder that vanishes with a genuinely cut-local source deficit; either choice requires a new consumption audit.
:::
