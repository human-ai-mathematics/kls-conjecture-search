---
type: exploration
date: "2026-08-27"
outcome: directional
nodes:
  - ass:all-cut-carleson
---
# KLS Wave 3: exact tight-prefix trace gate

Date: 2026-08-27

Role: orchestrator

## Sharpened target

The certified `cor:tight-window-consumption` does not need the every-interval quantifier in
`ass:all-cut-carleson`. It consumes only prefixes from time zero. The ledger and manuscript now
therefore expose the strictly weaker open shell `ass:tight-prefix-carleson`:

$$
\mathbb E\int_0^{T\wedge\tau_\eta}S_t\,dt
\le C_0T+C_1\mathbb E\int_0^{T\wedge\tau_\eta}r_t\,dt
+\alpha\mathbb E\int_0^{T\wedge\tau_\eta}D_t\,dt,
\qquad \alpha<1.
$$

This is now the target of `q:upgrade`. It remains `open`; no soft-projector result is wired to it.
Its fences are `obs:two-tail`, `obs:relative-ceiling`, and `obs:proj-ceiling`.

## Exact next gate

Fix one $C^2$ cutoff with $\chi=0$ on $(-\infty,3]$ and $\chi=1$ on $[4,\infty)$, and use the
notation of the rank-tail orientation probe:

$$
F_t=\chi(A_t),\qquad R_t=A_t-B_t,\qquad
Y_t=\operatorname{Tr}(F_tR_t)\ge0.
$$

On a prefix, $A_0=I$ gives $F_0=0$ and hence $Y_0-Y_T=-Y_T\le0$. Thus the positive
interval-boundary decrement from the all-interval formulation disappears. After discarding the
favorable Riccati and deterministic covariance-drift terms, the remaining injection consists of
exactly two cut-dependent projector-motion contractions:

$$
\begin{aligned}
\mathfrak J_\chi^0(T)
&=\frac12\mathbb E\int_0^{T\wedge\tau_\eta}
\sum_k\operatorname{Tr}\!\left(
D^2\chi(A_t)[\Theta_{t,k},\Theta_{t,k}]R_t
\right)dt\\
&\quad+\mathbb E\int_0^{T\wedge\tau_\eta}
\sum_k\operatorname{Tr}\!\left(
D\chi(A_t)[\Theta_{t,k}]\Gamma_{t,k}
\right)dt.
\end{aligned}
$$

The exact sufficient estimate is

$$
\mathfrak J_\chi^0(T)
\le C_\chi T+C_r\mathbb E\int_0^{T\wedge\tau_\eta}r_t\,dt
+\gamma\mathbb E\int_0^{T\wedge\tau_\eta}D_t\,dt,
\qquad \gamma<\frac18.
$$

Conditional on the already identified intrinsic low-block input, this yields final damping
$3/4+2\gamma<1$ and therefore the tight-prefix assumption. Rank-indexed covariance tails do not
control either contraction by themselves.

## Coordination rule

This is the singleton active owner for the trace-upgrade cluster. No parallel probe is launched
on high-rank `q:stein-weighted` or `q:alignment`, and no equivalence among those nodes is assumed.
The assigned prober must first independently audit the exact Itô identity and constants, then
attack or refute the two contractions. It may propose proof-ready sublemmas, but it may not edit
the ledger, manuscript, route control, or claim a status change.
