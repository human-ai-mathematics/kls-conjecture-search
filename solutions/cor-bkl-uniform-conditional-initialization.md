---
title: 'Solution: uniform conditional initialization from BKL coefficients'
ledger-node: cor:bkl-uniform-conditional-initialization
numbering:
  enumerator: '136.%s'
---

*Part of the Bizeul–Klartag–Lehec proof, Chapter [](#sec:bkl-proof); the reading order is on the [full proofs](#sec:proofs-bkl) page.*

**Author.** `bkl_suspension_author, gpt-6-astra, 2026-10-06` (researcher).

**Overview.** The full BKL coefficient bound supplies a stronger,
unconditional estimate than the startup candidate requested. An elementary
exponential allowance absorbs the denominator $(d+1)^2$ simultaneously in
all degrees. No induction on the depth is involved.

**Dependencies.** This proof uses [](#thm:bkl-tilt-bound) and its coefficient
normalization [](#def:bkl-tilt-cumulants). It does not use KLS or the premise
$\mathcal H_r(\Gamma)$. The iteration notation is defined explicitly below;
the symmetric Appell normalization agrees with
[](#thm:sz-polynomial-variance), but its variance bound is not an input.

:::{prf:theorem} Uniform startup in every degree
:label: thm:sol-bkl-uniform-initialization
Let $A\ge1$ be a universal constant such that
$c_d(\mu)\le A^d$ for every integer $d\ge1$ and every centered log-concave
probability $\mu$ in every dimension with
$\operatorname{Cov}(\mu)\preceq I$, as supplied by
[](#thm:bkl-tilt-bound). Put $G=4A$, $r_0=2$, and define
$\ell_0(x)=x$, $\ell_{r+1}(x)=\log(e+\ell_r(x))$ for $x\ge0$.
For every integer $r\ge r_0$, every $\Gamma\ge G$, every such $\mu$, and
every integer $d\ge1$,

$$
c_d(\mu)\le
\frac{((1+r^{-2})\Gamma)^d\ell_r(d)^d}{(d+1)^2}.
$$

In particular the conclusion holds for
$1\le d<\lceil32r^2\rceil$ whenever $\mathcal H_r(\Gamma)$ holds,
where $\mathcal H_r(\Gamma)$ says that every centered regular log-concave
covariance contraction with potential Hessian at least $aI$ satisfies
$C_P\le\Gamma^2\ell_r(a^{-1})^2$ for every $a>0$.
Here regularity in this premise means a smooth potential with positive
lower and finite upper Hessian bounds. The conclusion is independent of
this premise and thus establishes [](#cor:bkl-uniform-conditional-initialization).
:::

:::{prf:proof}
For all integers $d\ge1$, $d+1\le2^d$. The base case is equality; if the
inequality holds at $d$, then
$d+2\le2(d+1)\le2^{d+1}$. Squaring gives $(d+1)^2\le4^d$.
For $x\ge0$, $\log(e+x)\ge1$, so $\ell_r(d)\ge1$ for every $r\ge1$.
Consequently

$$
\frac{((1+r^{-2})\Gamma)^d\ell_r(d)^d}{(d+1)^2}
\ge\frac{\Gamma^d}{4^d}
\ge A^d
\ge c_d(\mu).
$$

All constants are chosen before the quantifiers over $r,\Gamma,d$, dimension,
and measure. This proves the stronger unconditional statement, and hence
its restriction to the finite startup range under any additional premise.
:::

**Fences respected.** There are no additional `bounded_by` edges. The
uniform-admissibility warning in the research brief is respected: the same
$G$ works for every depth and every degree, including the entire moving
startup range. This settles only the initialization estimate. It does not
supply the other comparison and propagation hypotheses of a bounded-loss
Song–Zhang iteration. The coefficient/KLS equivalence is not invoked as a
proof of its own premise; the coefficient input here has the independent
cumulant-and-suspension provenance stated in its dossier.
