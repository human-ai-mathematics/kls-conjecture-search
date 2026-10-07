---
title: "From bounded coefficient profiles to the universal Poincare inequality"
ledger-node: thm:sz-v2-kls
numbering:
  enumerator: "142.%s"
---

*Part of the second version of Song–Zhang, Chapter [](#sec:sz-v2-proof); the reading order is on the [full proofs](#sec:proofs-sz-v2) page.*

**Overview.** The last composition in the Song–Zhang v2 argument is short
once the bounded-amplitude profiles are available. This text gives that
composition with the order of quantifiers and the approximation step
explicit. Its crucial upstream input,
[](#prop:sz-v2-summable-budgets), is not proved by this composition.

**Dependencies.** Use [](#prop:sz-v2-summable-budgets),
[](#prop:sz-v2-common-radius), and [](#lem:sz-analytic-foundations),
with the scalar threshold and burn-in calculations accompanying
[](#prop:sz-v2-small-loss). No use is made of BKL, of its coefficient
corollaries, or of the already proved KLS statement.

:::{prf:theorem} Universal Poincare bound, the target of the composition
:label: thm:sol-sz-v2-kls
There is a universal $C<\infty$ such that for every $n\geq1$,
every isotropic log-concave probability measure $\mu$ on $\mathbb R^n$,
and every locally Lipschitz $f$ with finite Dirichlet integral,
$f\in L^2(\mu)$ and
$$
 \operatorname{Var}_\mu f\leq C\int|\nabla f|^2\,d\mu.
$$
Consequently $C_P(\mu)\leq C$. This is [](#thm:sz-v2-kls), corresponding to
Theorem 9.1 and Proposition 9.26 of [@SongZhang2026ConstantKLS].
:::

:::{prf:proof} Composition of the reconstructed bounded profiles
First fix one centered regular measure with covariance at most $I$ and
curvature at least $aI$, $a>0$. Set $x=\max\{1,a^{-1}\}$.
Choose a finite $i$ with $W_i(x)=4$, possible by [](#lem:sz-v2-profile-calculus). For a fixed sufficiently large universal integer $C_*$, put
$$
 r=R_i+\lceil C_*t(x)\rceil.
$$
This integer lies in the domain of the profile at index $i$; $i$ and $r$
are chosen after fixing the measure. The burn-in part of
[](#lem:sz-v2-profile-calculus) gives a universal constant
$M$ with $\mathcal L_r(a^{-1})\leq M$, and [](#lem:sz-v2-profile-threshold) gives
$W_i(r)\leq4+b2^{-i}$. Hence the bounded-profile assertion yields
$$
 \mathcal A(\mu)\leq A_0e^{C_A/8}(5+b+2B)^{1/3}M^2=:C_1.
$$
Every quantity on the right is independent of $a,n,\mu,i,r$.
The radius comparison gives $C_P(\mu)\leq2^{85}C_1=:C_2$.
The fixed comparison factor has been used once, after all refinements.

For an arbitrary isotropic log-concave $\mu$, the approximation assertion
of [](#lem:sz-analytic-foundations) gives regular isotropic probabilities
$\mu_j$ converging weakly to $\mu$. For $\phi\in C_c^\infty$,
both $\phi^2$ and $|\nabla\phi|^2$ are bounded continuous. Passing
the common inequality to the limit gives
$$
 \operatorname{Var}_\mu\phi\leq C_2\int|\nabla\phi|^2\,d\mu.
$$
For completeness, the extension to finite-energy locally Lipschitz
functions retains its integrability conclusion. First apply clipping
and compact cutoffs to a bounded locally Lipschitz test; mollify on each
compact set, where the log-concave density is locally integrable, as in
the stated analytic-foundations lemma. Cutoff errors vanish because
the test is bounded and gradients of cutoffs tend uniformly to zero.
This gives the same variance inequality for the clipped tests
$f_N=\max\{-N,\min\{f,N\}\}$, with
$\int|\nabla f_N|^2\,d\mu\leq\int|\nabla f|^2\,d\mu=:E$.

Choose a ball $B$ of positive $\mu$-mass on which $|f|\leq M_B$;
local Lipschitz regularity supplies such a bound. For $N\geq M_B$,
$f_N=f$ on $B$. If $m_N=\int f_N\,d\mu$, then
$$
 \mu(B)(|m_N|-M_B)_+^2
 \leq\int_B|f_N-m_N|^2\,d\mu
 \leq C_2E.
$$
Thus $(m_N)$ is bounded, as is
$\int f_N^2\,d\mu\leq C_2E+m_N^2$. Since $f_N^2\uparrow f^2$,
monotone convergence proves $f\in L^2(\mu)$. Now $f_N\to f$ in
$L^2$, their means converge, and the variance inequality passes to the
limit with the same constant. Taking the supremum of $C_P(\mu)$
over dimensions and isotropic laws concludes the composition.

No supremum over polynomial degrees or internal profile parameters was
passed through weak convergence. Each approximant uses its own finite
parameters, whereas the final scalar constant is common to all of them.
:::

The input [](#prop:sz-v2-summable-budgets) is reconstructed in its own
dossier through finite-chain blocks and near-unit profile induction.
The present composition uses that input and the analytic foundations;
no BKL statement or already established KLS assertion enters its proof.

**Fences respected.** The statement makes no sharper constant claim and
discharges no unrelated structural conjecture. Uniform admissibility
and the finite-versus-uniform quantifier order are kept explicit.
