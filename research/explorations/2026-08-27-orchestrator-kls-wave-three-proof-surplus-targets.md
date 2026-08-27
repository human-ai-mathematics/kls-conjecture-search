# KLS Wave 3: proof-surplus target staging

Date: 2026-08-27

Role: orchestrator

## `thm:bootstrap-stopped-interface`

The certified bootstrap proof discards stopping indicators when it packages covariance inflation
into $\Xi_T$. Retaining those indicators gives the sharper cut-dependent interface

$$
\widehat\Xi_{T,\eta}(\mu,E)
=\int_0^T\mathbb E[X_s\mathbf 1_{\{s<\tau_\eta\}}],ds.
$$

The staged theorem records the exact constants produced by the same two-case sign argument and
stopped martingale estimate:

$$
\begin{aligned}
\int_0^T\mathbb E[\bar e_t(E)\mathbf1_{\{t<\tau_\eta\}}]dt
\le Te_0+h_\mu\biggl[
&\left(\frac\varepsilon2+\eta\right)T+\frac{T^2}{16\eta^2}\\
&+\left(\frac{T}{8\eta^2}+\frac14\right)
\widehat\Xi_{T,\eta}(\mu,E)\biggr].
\end{aligned}
$$

For $T<1/8$, $\eta=T^{1/3}$, and $\varepsilon\le T^{1/3}$ this gives

$$
Te_0+C h_\mu\bigl(T^{4/3}+\widehat\Xi_{T,\eta}(\mu,E)\bigr).
$$

The node is staged as `open`, with the same certified dependencies as `thm:bootstrap` and fences
`obs:circularity` and `obs:relative-ceiling`. It asserts no universal bound on the stopped
interface and makes no KLS status change. A standalone author and a distinct cold reviewer are
required before promotion.
