---
title: "Song–Zhang v2: transferring the polynomial depth cost to dimension"
ledger-node: thm:sz-v2-dimension-bound
numbering:
  enumerator: "138.%s"
---

**Overview.** The new input is the improved curvature profile of
[](#thm:sz-v2-iterated-curvature). The Gaussian localization transfer already
proved in [](#thm:sz-curvature-transfer) accepts exactly this input. This
reconstruction of the implication in Section 7 of
[@SongZhang2026ConstantKLS] therefore needs no new stochastic calculation.
The proof below makes the uniformity in depth and the finite stopping depth
explicit.

**Dependencies.** The argument uses [](#thm:sz-curvature-transfer), the
curvature assertion [](#thm:sz-v2-iterated-curvature), and the established
Cheeger–Poincaré comparison [](#eq:cheeger-two-sided) [@KLnotes]. The curvature
assertion is an unresolved input until its own reconstruction is independently
certified. No BKL result, consequence of BKL, or dimension-free KLS assertion
is used.

:::{prf:theorem} Dimension estimates from the improved curvature profile
:label: thm:sol-sz-v2-dimension
Set $g(x)=\log(e+x)$, $\ell_r=g^{\circ r}$, and $L_n=\log(en)$.
Assume the curvature profile in [](#thm:sz-v2-iterated-curvature).
There are universal constants $C,C'>0$ such that, for every $n\ge1$, every
isotropic log-concave probability measure $\mu$ on $\mathbb R^n$, and every
integer $r\ge1$,
$$
 C_P(\mu)\le C(r+1)^{1/3}\ell_r(L_n)^2,
 \qquad \Psi_{\mathrm{KLS},n}\le C'(r+1)^{1/6}\ell_r(L_n).
$$
In particular,
$$
 C_P(\mu)\le C(1+\log^*(n+2))^{1/3},
 \qquad \Psi_{\mathrm{KLS},n}\le C'(1+\log^*(n+2))^{1/6}.
$$
Here $\log^*x$ is the number of natural logarithms needed to reach a number
at most one. Constants may be enlarged between the two displays.
This is the implication needed for [](#thm:sz-v2-dimension-bound).
:::

:::{prf:proof}
Let $A$ denote the universal constant in the curvature input. Fix any finite
$r\ge1$ and define
$$F_r(a)=A(r+1)^{1/3}\ell_r(a^{-1})^2\qquad(a>0).$$
Every isotropic regular measure is centered and has covariance at most $I$.
Thus the assumed curvature estimate applies to every measure and every
admissible lower Hessian bound required by the transfer theorem. Write
$c_T,C_T>0$ for that theorem's universal constants. It gives
$$
 C_P(\mu)\le C_T A(r+1)^{1/3}\ell_r(c_T^{-1}L_n)^2.
$$
This transfer already includes arbitrary nonsmooth isotropic log-concave
laws and all locally Lipschitz tests of finite energy. In particular no
regularity of the initial law needs to be imposed here.

To absorb the change of argument uniformly in $r$, put
$D=\max(1,c_T^{-1})$. Concavity of $g$ implies
$$g(x)=g(D^{-1}Dx+(1-D^{-1})0)
 \ge D^{-1}g(Dx)+(1-D^{-1})g(0)\ge D^{-1}g(Dx).$$
Consequently $g(Dx)\le Dg(x)$. Monotonicity and induction give
$\ell_r(Dx)\le D\ell_r(x)$ for every integer $r\ge1$.
Thus the first asserted estimate holds with $C=C_TAD^2$, independent
of both $n$ and $r$. The comparison
$\psi_\mu^2\le\pi C_P(\mu)$ followed by the supremum over isotropic
laws gives the asserted estimate for $\Psi_{\mathrm{KLS},n}$.

For completeness, choose a finite depth without making a limit in $r$.
Put $x_0=n+2$, and let $m$ be the first index at which the ordinary
logarithmic iterates $x_{j+1}=\log x_j$ satisfy $x_m\le4$.
The sequence is defined until that index and $m\le\log^*(n+2)$.
For $y\ge4$,
$$g(y+1)=\log y+\log(1+(e+1)/y)\le\log y+1,$$
because $e+1<4$ and $\log(1+t)\le t$.
When $m\ge1$, $L_n\le1+x_1$; while $j<m$, $x_j>4$, so induction gives
$\ell_{m-1}(L_n)\le1+x_m\le5$. When $m=0$, $n+2\le4$ and
$L_n<5$ directly. Since $g([0,5])\subset[0,5]$, the choice
$r=\max(1,m-1)$ in either case satisfies
$$\ell_r(L_n)\le5,\qquad r\le\log^*(n+2).$$
Substitute this single depth in the preceding estimates and absorb the
factors $25$ and $5$ in the constants. This proves both optimized estimates.
:::

:::{prf:remark} Applicability blocker
:label: rem:sol-sz-v2-dimension-blocker
The implication above is fully reduced to the stated curvature input, but
this dossier alone does not establish that input. In particular it must not
be registered as an unconditional proof while the inner refinement dossier
has not yet been independently certified. One may independently certify this
conditional implication with its curvature premise retained explicitly.
:::

**Fences respected.** No new assertion discharges any CMH, occupation or
trace-upgrade antecedent. The dimension bounds retain dimension dependence.
The small-degree and uniform-admissibility issues are delegated to the
explicit curvature premise, not assumed solved by this transfer.
