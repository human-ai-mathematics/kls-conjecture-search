---
title: "Solution: quadratic chaos, two-color source, and covariance reduction"
ledger-node:
  - cor:qcts-source
  - thm:covariance-bound
  - cor:V2-implies
numbering:
  enumerator: "106.%s"
---

*Part of the shared technical foundations, Chapters [](#sec:qcts) and [](#sec:product-stress); the reading order is on the [full proofs](#sec:proofs-archive) page.*

**Overview.** Whitening and duality convert the quadratic-chaos theorem into
a bound on the two-color contrast. Unwhitening costs exactly the square of
the largest covariance eigenvalue; removing the off-balance correction
gives the constant in the manuscript. Applied separately to every posterior,
this gives the pathwise covariance reduction and its integrated version.
Product posteriors admit the same argument using the certified product
quadratic-chaos estimate, without Letwin's input.

**Logical scope.** The unconditional statement [](#cor:qcts-source) uses
[](#thm:letwin-qcts) as a proof dependency. Its certification therefore
requires that input to be established. The general-measure branches of
[](#thm:covariance-bound) and [](#cor:V2-implies) retain the explicit
antecedent [](#thm:letwin-qcts). Their product branches use no such
antecedent. This dossier does not certify Letwin's source theorem.

:::{prf:theorem} Whitened two-color control
:label: thm:sol-letwin-whitened-source
Let $\nu$ be centered log-concave with positive-definite covariance $A$,
and let $E$ have mass $p\in(0,1)$. Put $q=1-p$, $s=pq$,
$\delta=m^E-m^{E^c}$, $G=\Sigma^E-\Sigma^{E^c}$ and
$K=G+(q-p)\delta\delta^T$. Then the conclusion of [](#cor:qcts-source) is

$$
s\|A^{-1/2}KA^{-1/2}\|_{\mathrm{HS}}^2\le8,
\qquad s\|K\|_{\mathrm{HS}}^2\le8\|A\|_{\mathrm{op}}^2.
$$

If $p\in[1/3,2/3]$, then $s\|G\|_{\mathrm{HS}}^2\le17\|A\|_{\mathrm{op}}^2$;
at $p=1/2$ the constant is $8$.
:::

:::{prf:proof}
Write $Y=A^{-1/2}X$ for $X\sim\nu$, and transport the cut by this invertible
map. Its mass does not change. Conditional means and covariances transform
linearly and by congruence respectively, so the new contrast is
$H=A^{-1/2}KA^{-1/2}$. All moments used below exist because log-concave
probabilities have finite polynomial moments. Let
$g=(\mathbf1_E-p)/\sqrt{s}$ on the whitened probability space. Then
$\mathbb Eg=0$, $\mathbb Eg^2=1$. For symmetric $N$, the certified
identity [](#prop:stein-rep) gives

$$
\sqrt{s}\langle H,N\rangle_{\mathrm{HS}}
=\mathbb E\big[g(Y^TNY-\operatorname{Tr}N)\big].
$$

Cauchy--Schwarz and [](#thm:letwin-qcts) give
$s\langle H,N\rangle^2\le8\|N\|_{\mathrm{HS}}^2$.
If $H\ne0$, take $N=H/\|H\|_{\mathrm{HS}}$; for $H=0$ the conclusion
is immediate. This proves the whitened estimate. For every matrix $L$,
$\|A^{1/2}LA^{1/2}\|_{\mathrm{HS}}
\le\|A^{1/2}\|_{\mathrm{op}}^2\|L\|_{\mathrm{HS}}$,
as follows by applying the operator norm bound successively to left and
right multiplication. With $L=H$ this proves the second estimate.

Covariance decomposition gives
$A=p\Sigma^E+q\Sigma^{E^c}+s\delta\delta^T$, so
$B=s\delta\delta^T\preceq A$. Since $B$ has rank at most one,
$r=s|\delta|^2\le\|A\|_{\mathrm{op}}$. Consequently

$$
\begin{aligned}
s\|G\|_{\mathrm{HS}}^2
&\le2s\|K\|_{\mathrm{HS}}^2+2s(q-p)^2|\delta|^4\\
&\le16\|A\|_{\mathrm{op}}^2+\frac{2(q-p)^2}{s}r^2.
\end{aligned}
$$

On the coarse window, $s\ge2/9$ and $|q-p|\le1/3$, hence the last
coefficient is at most one. This gives $17$. At exact balance $K=G$,
so the previous estimate gives $8$ without this loss.
:::

:::{prf:theorem} Pathwise covariance reduction
:label: thm:sol-letwin-pathwise-covariance
Conditional on [](#thm:letwin-qcts), for the localization of any isotropic
log-concave initial measure and any fixed measurable cut, at every finite
time in the coarse balanced window,

$$
S_t=s_t\|G_t\|_{\mathrm{HS}}^2\le C(1+X_t^2),
\qquad X_t=(\|A_t\|_{\mathrm{op}}-1)_+,
$$

with universal $C$. The assertion is unconditional for products of isotropic
one-dimensional log-concave laws. This proves [](#thm:covariance-bound).
:::

:::{prf:proof}
For any finite posterior realization, the likelihood
$\exp(c_t\cdot x-t|x|^2/2)$ is strictly positive on the support of the
initial law. An isotropic initial law is not supported on a proper affine
hyperplane, and equivalence under positive likelihood preserves this
property. Thus its posterior covariance is positive definite at finite
times. At $t>0$ the Gaussian factor makes every polynomial moment finite;
at zero this follows from log-concavity. No singular inverse or infinite-time
posterior is being used. The posterior, centered at its mean, is log-concave,
and translating both law and cut does not change $G$ or $K$.

Apply the preceding two-color bound to that posterior: on the coarse window
$S_t\le17\|A_t\|_{\mathrm{op}}^2$. Since
$\|A_t\|_{\mathrm{op}}\le1+X_t$ and
$(1+X_t)^2\le2(1+X_t^2)$, one can take $C=34$ in the general branch.
This is a deterministic inequality for each admissible posterior, hence
holds pathwise without taking a supremum of exceptional events over times.

For the independent product branch, the posterior density factorizes:

$$
\mu_t(dx)=\bigotimes_i
\frac{e^{c_{t,i}x_i-tx_i^2/2}\mu_i(dx_i)}
{\int e^{c_{t,i}z-tz^2/2}\mu_i(dz)}.
$$

Center its coordinates. By [](#lem:product-qcts), for every symmetric $M$,
the centered posterior $Y$ with diagonal covariance $A_t$ satisfies
$\operatorname{Var}(Y^TMY)\le C_*\|A_t^{1/2}MA_t^{1/2}\|_{\mathrm{HS}}^2
\le C_*\|A_t\|_{\mathrm{op}}^2\|M\|_{\mathrm{HS}}^2$.
The same color identity and duality just used therefore give
$s_t\|K_t\|_{\mathrm{HS}}^2\le C_*\|A_t\|_{\mathrm{op}}^2$.
The off-balance calculation gives
$S_t\le(2C_*+1)\|A_t\|_{\mathrm{op}}^2
\le2(2C_*+1)(1+X_t^2)$, as required. Product structure of the cut
itself is not assumed.
:::

:::{prf:theorem} Integrated covariance reduction
:label: thm:sol-letwin-v2-implication
Let $T_0>0$ and $K\ge0$ be finite, and suppose an isotropic log-concave
initial law satisfies

$$
\int_I\mathbb EX_t^2\,dt\le K|I|
\quad\hbox{for every interval }I\subset[0,T_0].
$$

Conditional on [](#thm:letwin-qcts), every balanced cut satisfies the
all-cut inequality on that horizon with $C_0=C(1+K)$, $C_1=0$ and
$\alpha=0$. For product initial laws the implication is unconditional.
This proves [](#cor:V2-implies).
:::

:::{prf:proof}
Before its coarse exit time $\tau$, the cut is in the window where the
preceding pathwise estimate applies. All integrands are nonnegative, so
Tonelli and the premise give

$$
\mathbb E\int_{I\cap[0,\tau]}S_t\,dt
\le C\int_I(1+\mathbb EX_t^2)\,dt
\le C(1+K)|I|.
$$

This is exactly the claimed all-cut bound, without any damping or $r$ term.
It holds for each fixed cut, with a constant independent of the cut.
For products use the unconditional branch instead. Furthermore each
coordinate posterior is driven by its own one-dimensional localization:
the drift of $c_{t,i}$ is its posterior mean, a function only of $(t,c_{t,i})$,
and the Brownian coordinates are independent. Thus the variance processes
are independent one-dimensional processes, and $\|A_t\|_{\mathrm{op}}$
is their maximum. The condition contains no cut variable.
:::

**Hypotheses and fences.** Positive definiteness is used only for static
whitening and follows from isotropy and positive likelihood on finite
posterior paths. Balance is used only for the bounded off-balance correction.
Product independence is used only in the preprint-independent branch. None
of these targets has a `bounded_by` edge. The covariance loss is retained:
no intrinsic estimate is mistaken for a universal Euclidean source bound,
and a dimension-dependent time horizon is not a universal Carleson horizon.
