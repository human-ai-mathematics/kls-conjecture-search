---
title: "Song–Zhang v2: composition with the canonical KLS statement"
ledger-node: conj:kls
numbering:
  enumerator: "147.%s"
---

*Part of the second version of Song–Zhang, Chapter [](#sec:sz-v2-proof); the reading order is on the [full proofs](#sec:proofs-sz-v2) page.*

**Overview.** This dossier composes [](#thm:sz-v2-kls) with the unchanged
canonical target [](#conj:kls). The only domain adjustment is to interpret
the Poincaré inequality for locally Lipschitz functions whose Dirichlet
integral is infinite. The Cheeger formulation then follows from the
established two-sided comparison.

**Dependencies.** The only theorem input is [](#thm:sz-v2-kls).
For the equivalent Cheeger formulation we use [](#eq:cheeger-two-sided),
with the normalization and references recorded there
[@Klartag2023Logarithmic; @Milman2009Isoperimetric]. There is no BKL
premise, no consequence of BKL, and no invocation of the already recorded
status of [](#conj:kls). The upstream Song–Zhang reconstruction supplies
its own universal Poincaré theorem. This composition does not certify that
upstream theorem or substitute for its independent review.

:::{prf:theorem} Canonical KLS from the Song–Zhang theorem
:label: thm:sol-sz-v2-kls-composition
There is a universal constant $C<\infty$ such that, for every dimension,
every isotropic log-concave probability measure $\mu$, and every real
locally Lipschitz function $f$,
$$
 \operatorname{Var}_\mu(f)\le C\int|\nabla f|^2\,d\mu.
$$
For functions not in $L^2(\mu)$, the variance is understood as the
extended nonnegative quantity
$\inf_{c\in\mathbb R}\int|f-c|^2\,d\mu$.
Equivalently up to universal constants, the Cheeger constants of all
such measures are bounded below uniformly in the dimension.
This proves exactly [](#conj:kls).
:::

:::{prf:proof}
Let $C$ be the universal constant of [](#thm:sz-v2-kls), and fix $n$,
$\mu$ and $f$ as in the statement. The isotropic assumption implies
that the affine hull of the support is all of $\mathbb R^n$; a
full-dimensional log-concave measure has a Lebesgue density. Hence the
a.e. gradient of the locally Lipschitz function is defined $\mu$-a.e.
and its squared norm has a well-defined integral in $[0,\infty]$.

If $E=\int|\nabla f|^2d\mu$ is finite, [](#thm:sz-v2-kls) applies
with exactly this function and measure. It gives both $f\in L^2(\mu)$
and $\operatorname{Var}_\mu(f)\le CE$. For $f\in L^2$, expansion of
the square gives
$$
 \int|f-c|^2d\mu
 =\int|f-\textstyle\int f\,d\mu|^2d\mu
       +\bigl(c-\textstyle\int f\,d\mu\bigr)^2,
$$
so the displayed extended convention equals ordinary variance.
If $E=\infty$, the right-hand side of the claimed inequality is
$\infty$, and the inequality holds in the extended nonnegative reals.
This includes nonintegrable functions without attempting to subtract
an undefined mean. Indeed if $\int|f-c|^2d\mu$ were finite for any
finite $c$, the inequality $|f|^2\le2|f-c|^2+2c^2$ would imply
$f\in L^2(\mu)$. Thus the extended variance is $\infty$ for every
function outside $L^2$, as required. The same single constant $C$
works in every dimension and for every allowed measure and function.

It follows that $C_P(\mu)\le C$ for all isotropic log-concave $\mu$.
In the manuscript convention $\Psi_{\mathrm{KLS},\mu}=h_\mu^{-1}$,
[](#eq:cheeger-two-sided) gives
$$
 h_\mu^{-2}\le\pi C_P(\mu)\le\pi C,
 \qquad h_\mu\ge(\pi C)^{-1/2}.
$$
Conversely, if $h_\mu\ge c>0$ uniformly, the other side of that same
comparison gives $C_P(\mu)\le4h_\mu^{-2}\le4c^{-2}$.
This is precisely the equivalence asserted in the canonical target.
:::

**Fences respected.** This composition claims only a universal constant.
It establishes no sharper structural inequality and does not discharge
any unrelated conditional premise. Its proof uses the Song–Zhang theorem
and the earlier Cheeger comparison, rather than the other proof record
attached to the same target.
