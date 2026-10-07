---
title: "BK: composition with the canonical KLS statement"
ledger-node: conj:kls
numbering:
  enumerator: "158.%s"
---

*Part of the Balasubramanian–Kasiviswanathan proof, Chapter [](#sec:bk-proof); the reading order is on the [full proofs](#sec:proofs-bk) page.*

**Overview.** The explicit BK Poincaré estimate implies the unchanged
canonical KLS statement. The sole domain extension is to locally Lipschitz
functions with infinite Dirichlet integral; the equivalent Cheeger assertion
uses the established two-sided comparison.

**Dependencies.** The only theorem input is [](#thm:bk-explicit-poincare).
For the equivalent Cheeger formulation use [](#eq:cheeger-two-sided)
[@Klartag2023Logarithmic; @Milman2009Isoperimetric]. Neither the existing
status of [](#conj:kls), another proof of KLS, nor a BKL or SZ v2 theorem
is used. This composition does not certify its upstream theorem.

:::{prf:theorem} Canonical KLS from the BK estimate
:label: thm:sol-bk-kls-composition
Assuming [](#thm:bk-explicit-poincare), there is a universal constant
$C=1+2\cdot10^{16}$ such that for every dimension, every isotropic
log-concave law $\mu$, and every real locally Lipschitz function $f$,
$$\operatorname{Var}_\mu f\le C\int|\nabla f|^2\,d\mu.$$
For $f\notin L^2(\mu)$, variance means the extended nonnegative quantity
$\inf_{c\in\mathbb R}\int|f-c|^2d\mu$.
Equivalently up to universal constants, these laws have Cheeger constants
bounded below uniformly in dimension. This is [](#conj:kls).
:::

:::{prf:proof}
Fix $\mu$ and $f$ as stated. Isotropy makes the affine support all of
$\mathbb R^n$, and the law is absolutely continuous, so the almost
everywhere gradient has a well-defined energy $E\in[0,\infty]$.
If $E<\infty$, the explicit BK estimate gives $f\in L^2(\mu)$ and the
claimed inequality with this single $C$. For an $L^2$ function,
$$\int|f-c|^2d\mu=\operatorname{Var}_\mu f+
\left(c-\int f\,d\mu\right)^2,$$
so the extended convention agrees with ordinary variance. If $E=\infty$,
the inequality holds in the extended nonnegative reals. For completeness,
a function outside $L^2$ cannot have $\int|f-c|^2d\mu<\infty$ at any
finite $c$, since $|f|^2\le2|f-c|^2+2c^2$ would contradict that fact.
Thus no undefined expectation is being subtracted.

The Cheeger comparison gives $h_\mu^{-2}\le\pi C_P(\mu)\le\pi C$, hence
$h_\mu\ge(\pi C)^{-1/2}$. Conversely a uniform lower bound $h_\mu\ge b>0$
implies $C_P(\mu)\le4h_\mu^{-2}\le4b^{-2}$ by the other side of the
same comparison. These are precisely the two equivalent assertions of the
canonical target.
:::

**Fences respected.** This is a composition of the explicitly named BK
input only. It establishes no sharper structural inequality or unrelated
conditional premise. The explicitly named BK input is proved separately;
this composition does not replace its proof or independent review.
