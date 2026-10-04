---
title: "Gaussian transfer and the all-depth Song–Zhang Poincaré bound"
ledger-node:
  - thm:sz-curvature-transfer
  - thm:song-zhang-kls
  - cor:sz-affine-poincare
numbering:
  enumerator: "123.%s"
---

**Overview.** We reconstruct Section 7 of [@SongZhang2026IteratedLogKLS],
including the bounded test function used to transfer a curvature estimate to an
arbitrary isotropic law. Gaussian observations produce a regular posterior;
Letwin's quadratic inequality controls its covariance on a short interval.
One bounded Lipschitz test retains a fixed amount of variance on a posterior
with controlled covariance. This proves a transfer for **any** curvature
profile, not only the iterated-logarithm profiles. We then apply
[](#thm:sz-iterated-curvature), select a finite depth, and whiten to obtain the
affine assertion. Approximation passes only scalar Poincaré inequalities to
limits; no continuity of spectral objects or of the profile is required.

## A bounded test detecting the Poincaré constant

The established bounded-witness theorem of [@KLnotes, Theorem 20], in the
version arXiv:2406.01324v2, states that for a log-concave law there is a
$1$-Lipschitz $g$ with
$$
 \operatorname{Var}_\mu(g)\ge c_1\psi_\mu^2,
 \qquad \|g\|_\infty^2\le C_1\operatorname{Var}_\mu(g),
$$
where $c_1,C_1>0$ are universal and $\psi_\mu$ is the reciprocal Cheeger
constant. Corollary 21 and its following remark give
$$
 C_P(\mu)\le4\psi_\mu^2,\qquad \psi_\mu^2\le\pi C_P(\mu). \tag{1}
$$
These are literature inputs, not consequences of the new preprint.
If the bound for $g$ is essential, clip to its essential range; this preserves
its almost-everywhere values and Lipschitz constant and makes its bound global.
For $0<k=C_P(\mu)<\infty$, put $\sigma^2=\operatorname{Var}_\mu g$ and
$f=(g-\mathbb E g)/\sigma$. Since $\sigma^2\ge c_1k/4$, there is a universal
$B_0\ge1$ such that
$$
 \mathbb Ef=0,\quad \mathbb Ef^2=1,\quad
 \sup|f|\le B_0,\quad \operatorname{Lip}(f)\le B_0/\sqrt k. \tag{2}
$$
For instance take $B_0=\max(1,2\sqrt{C_1},2/\sqrt{c_1})$.
The global bound in (2) is what pays for the exceptional covariance paths.

## Gaussian observations and posterior martingales

Take a regular isotropic initial law $\mu=e^{-W}dx$ with
$aI\preceq D^2W\preceq bI$. Let $X\sim\mu$ be independent of standard
Brownian motion $B_t$, set $Y_t=tX+B_t$, and let $\mathcal F_t$ be the usual
augmentation of its observation filtration. The conditional distribution is
$$
 \mu_t(dx)=Z_t^{-1}e^{Y_t\cdot x-t|x|^2/2}\mu(dx),\qquad
 Z_t=\int e^{Y_t\cdot x-t|x|^2/2}\mu(dx). \tag{3}
$$
For fixed $x$, multiplying likelihood ratios of independent Gaussian increments
on any finite partition gives the factor $e^{x\cdot Y_t-t|x|^2/2}$.
Cylinder events generate the path sigma-field, so Bayes' formula proves (3)
for the entire observation filtration. In particular
$\mathbb E_tq=\mathbb E[q(X)\mid\mathcal F_t]$.
For every Borel $q$ of polynomial growth these are square-integrable
martingales: strong convexity of $\mu$ gives all polynomial moments, and
conditional Jensen applies.

Write $m_t=\mathbb E_tX$, $A_t=\operatorname{Cov}_tX$, and
$\mathcal W_t=Y_t-\int_0^tm_sds$. For $s<t$, the future increments of $B$
are independent of $X$ and the past, while
$\mathbb E[m_u\mid\mathcal F_s]=m_s$ for $u\ge s$. Consequently
$\mathbb E[\mathcal W_t-\mathcal W_s\mid\mathcal F_s]=0$.
All these quantities are integrable by
$\mathbb E|m_u|^2\le\mathbb E|X|^2$. The process is continuous and has
quadratic covariation $tI$, so Lévy's characterization makes it Brownian in the
observation filtration.

For completeness define
$I_q(t,y)=\int q(x)e^{y\cdot x-t|x|^2/2}\mu(dx)$.
Gaussian tails permit differentiation locally in $(t,y)$, including around
$t=0$. We have $\partial_tI_q+\Delta_yI_q/2=0$ and
$\nabla_yI_q=I_{qx}$. Itô's formula followed by the quotient rule therefore
gives
$$
 d\mathbb E_tq=\operatorname{Cov}_t(q,X)\cdot d\mathcal W_t. \tag{4}
$$
These computations can first be stopped on $|Y_t|\le R$. To remove the stop,
conditional Cauchy--Schwarz, ordinary Cauchy--Schwarz and conditional Jensen
bound, for each finite $T$,
$$
 \mathbb E\int_0^T|\operatorname{Cov}_t(q,X)|^2dt
 \le T\big(\mathbb E q(X)^4\,\mathbb E|X|^4\big)^{1/2}<\infty.
$$
Indeed the conditional squared covariance is at most
$\mathbb E_tq^2\,\mathbb E_t|X|^2$. Continuity of $Y$ and Itô isometry
then justify (4) without the stop. Bounded Borel tests, including the witness
$f$ and $f^2$, are included.

Taking $q=x_i$ and $q=x_ix_j$ in (4) yields
$$
 dm_t=A_t\,d\mathcal W_t,\qquad
 dA_t=\sum_jU_{j,t}\,d\mathcal W_{j,t}-A_t^2dt, \tag{5}
$$
where $U_{j,t}=\mathbb E_t[(X_j-m_{j,t})(X-m_t)(X-m_t)^T]$.
The negative drift is $-dm_tdm_t^T$; expanding $X=m_t+(X-m_t)$ in the remaining
martingale terms leaves exactly the displayed third centered moment.
Every posterior is regular, with potential Hessian $D^2W+tI$.

## Covariance exit from a fixed interval

:::{prf:lemma} Uniform covariance control on a logarithmic time interval
:label: lem:sol-sz-gaussian-exit
Let $\tau$ be the first exit of $A_t$ from $(I/2,2I)$. For $0<t\le1/16$,
$$
 \mathbb P(\tau\le t)\le2n\exp[-1/(2048t)].
$$
:::

:::{prf:proof}
For any centered log-concave $Z$ of positive covariance $A$, the whitened
form of [](#thm:letwin-qcts) gives
$$
 \operatorname{Var}(Z^TDZ)\le8\|A^{1/2}DA^{1/2}\|_{\rm HS}^2
 \le8\|A\|_{\rm op}^2\|D\|_{\rm HS}^2
$$
for symmetric $D$. For $S_z=\mathbb E[(z\cdot Z)ZZ^T]$, trace duality and
Cauchy--Schwarz give
$$
 |\langle D,S_z\rangle|
 =|\mathbb E[(z\cdot Z)(Z^TDZ-\operatorname{tr}(DA))]|
 \le\sqrt{8z^TAz}\|A\|_{\rm op}\|D\|_{\rm HS}.
$$
Thus $\|S_z\|_{\rm HS}^2\le8\|A\|_{\rm op}^2z^TAz$.
Symmetry in all three indices of the third moment yields
$\sum_j|U_jz|^2=\|S_z\|_{\rm HS}^2$, so before $\tau$
$$
 \sum_jU_{j,t}^2\preceq64I. \tag{6}
$$
Set $M_u=\int_0^{u\wedge\tau}\sum_jU_{j,s}d\mathcal W_{j,s}$.
For symmetric matrices $M,T$ and $\theta>0$,
$$
 D^2\operatorname{tr}(e^{\theta M})[T,T]
 \le\theta^2\operatorname{tr}(e^{\theta M}T^2). \tag{7}
$$
Diagonalize $M$. The coefficient of $T_{ij}^2$ on the left is $\theta^2$
times the logarithmic mean of $e^{\theta m_i},e^{\theta m_j}$.
This mean equals $\int_0^1e^{\theta[(1-s)m_i+sm_j]}ds$ and is at most their
arithmetic mean by convexity. Summing the coefficients proves (7).
Itô's formula and (6) now show that
$Z_u=e^{-32\theta^2u}\operatorname{tr}(e^{\theta M_u})$ is a nonnegative
local supermartingale, hence a supermartingale. At the first crossing of
$\lambda_{\max}(M_u)\ge\rho$ before time $t$, its value is at least
$e^{\theta\rho-32\theta^2t}$. Optional stopping, with $Z_0=n$, gives the
one-sided probability bound $n e^{-\theta\rho+32\theta^2t}$.
Optimize at $\theta=\rho/(64t)$, repeat for $-M$, and take the union:
$$
 \mathbb P\left(\sup_{u\le t}\|M_u\|_{\rm op}\ge\rho\right)
 \le2n e^{-\rho^2/(128t)}. \tag{8}
$$
The stopped integrand is square integrable by (6), and all optional stopping
arguments can first be made with bounded localizing stops; nonnegativity and
Fatou then pass to the displayed estimates.

On $\{\tau\le t\}$, continuity gives
$M_\tau=A_\tau-I+\int_0^\tau A_s^2ds$.
An upper exit supplies a unit vector with quadratic form at least $1$.
A lower exit supplies one with quadratic form at most
$-1/2+4t\le-1/4$. Hence this event implies the event in (8) with $\rho=1/4$,
which proves the result.
:::

## A transfer for an arbitrary curvature profile

:::{prf:theorem} Universal profile transfer
:label: thm:sol-sz-curvature-transfer
There are universal constants $c,C>0$ such that the following implication holds.
Let $F:(0,\infty)\to(0,\infty)$ satisfy $C_P(\nu)\le F(a)$, in every
dimension, for every isotropic regular measure $\nu=e^{-W}dx$ and every
$a>0$ such that $aI\preceq D^2W\preceq bI$ for some finite $b$.
Then every isotropic log-concave probability measure $\mu$ on $\mathbb R^n$
satisfies
$$
 C_P(\mu)\le C F(c/\log(en)).
$$
Neither monotonicity nor continuity of $F$ is required. This proves
[](#thm:sz-curvature-transfer).
:::

:::{prf:proof}
First take regular isotropic $\mu$ and let $k=C_P(\mu)$, finite and positive
by [](#lem:sz-analytic-foundations). Choose the witness (2) and form the stopped
Gaussian posteriors above. Put
$V_t=\operatorname{Var}_{\mu_{t\wedge\tau}}f$ and
$S(t)=\mathbb E_{\rm loc}V_t$. Applying Itô's formula to the bounded
martingales $\mathbb E_tf$ and $\mathbb E_tf^2$ gives
$$
 S(t)=1-\int_0^t\mathbb E_{\rm loc}
 [\mathbf1_{\{s<\tau\}}|\operatorname{Cov}_{\mu_s}(X,f)|^2]ds.
$$
Before exit, directional Cauchy--Schwarz yields
$|\operatorname{Cov}_{\mu_s}(X,f)|^2\le\|A_s\|_{\rm op}V_s\le2V_s$.
Thus $S'(t)\ge-2S(t)$ almost everywhere and
$$
 S(t)\ge e^{-2t},\qquad 0\le V_t\le B_0^2. \tag{9}
$$
The second assertion follows from the global supremum bound of $f$.

Set
$$
 c_0={1\over2048\log(16B_0^2)},\qquad t={c_0\over\log(en)}.
$$
Then $0<t<1/16$. With $q=1/(2048c_0)=\log(16B_0^2)>1$, the exit lemma gives
$$
 \mathbb P(\tau\le t)\le2n e^{-1/(2048t)}
 =2e^{-q}n^{1-q}\le{1\over8B_0^2}.
$$
Since $e^{-2t}\ge1-2t\ge7/8$, subtracting the exit contribution in (9)
gives
$\mathbb E_{\rm loc}[\mathbf1_{\{\tau>t\}}\operatorname{Var}_{\mu_t}f]\ge3/4$.
There is consequently a realization with $\tau>t$ and
$\operatorname{Var}_{\mu_t}f>1/2$.
Fix it, write $m,A$ for its mean and covariance, and let $\eta$ be the law of
$A^{-1/2}(X-m)$ under this posterior. This is regular isotropic and its
potential Hessian is
$$
 A^{1/2}(D^2W+tI)A^{1/2}\succeq(t/2)I.
$$
It also has a finite upper Hessian bound. The transformed witness
$z\mapsto f(m+A^{1/2}z)$ has variance greater than $1/2$ and gradient energy
at most $\|A\|_{\rm op}\operatorname{Lip}(f)^2\le2B_0^2/k$.
The definition of $C_P(\eta)$ therefore gives
$$
 k\le4B_0^2 C_P(\eta)\le4B_0^2 F(t/2). \tag{10}
$$
This uses the hypothesis at the particular admissible lower curvature bound
$t/2$; it never compares values of $F$ at nearby arguments.

For arbitrary isotropic log-concave $\mu$, choose the regular isotropic
approximation of [](#lem:sz-analytic-foundations). The regular-law argument
bounds every approximant by the same number
$K=4B_0^2F(c_0/(2\log(en)))$. The isotropic limit is full-dimensional and
absolutely continuous. The scalar stability part of that lemma passes the
inequality to the limit and all locally Lipschitz finite-energy tests.
Taking $c=c_0/2$ and $C=4B_0^2$ proves the claim. No regularity of $F$ enters
this limit either, since its argument is unchanged along the approximants.
:::

## All depths, finite stabilization, and affine coordinates

:::{prf:theorem} Song–Zhang bound and its affine consequence
:label: thm:sol-song-zhang-kls
There are universal $C,C'>0$, independent of $r,n$, such that every isotropic
log-concave measure $\mu$ on $\mathbb R^n$ satisfies, for every integer $r\ge1$,
$$
 C_P(\mu)\le C16^r\ell_r(\log(en))^2,
 \qquad \Psi_{\mathrm{KLS},n}\le C'4^r\ell_r(\log(en)).
$$
In particular $C_P(\mu)\le C16^{\log^*(n+2)}$ and
$\Psi_{\mathrm{KLS},n}\le C'4^{\log^*(n+2)}$.
For a log-concave $\mu$ with positive definite covariance $\Sigma$, the
Poincaré estimates remain valid after multiplying their right sides by
$\|\Sigma\|_{\rm op}$.
These are [](#thm:song-zhang-kls) and [](#cor:sz-affine-poincare).
:::

:::{prf:proof}
For each fixed finite $r$, [](#thm:sz-iterated-curvature) supplies the profile
$F_r(a)=\Gamma_r^2\ell_r(a^{-1})^2$, with $\Gamma_r\le C_0 4^r$.
The transfer theorem with its constants just constructed gives
$$
 C_P(\mu)\le4B_0^2\Gamma_r^2
   \ell_r((2/c_0)\log(en))^2.
$$
The elementary scaling inequality $\ell_r(cx)\le c\ell_r(x)$ for $c\ge1$
was proved in the iteration dossier. Hence this is bounded by
$$
 4B_0^2(2/c_0)^2C_0^2\,16^r\ell_r(\log(en))^2. \tag{11}
$$
All constants here are independent of both $r$ and $n$. By (1),
$\psi_\mu\le\sqrt{\pi C_P(\mu)}$. Taking the supremum over isotropic laws
in dimension $n$ gives the asserted reciprocal-Cheeger estimate.

We now choose a finite depth. For $y\ge4$,
$$
 g(y+1)=\log y+\log(1+(e+1)/y)\le\log y+1, \tag{12}
$$
since $e+1<4$ and $\log(1+u)\le u$.
Let $x_0=n+2$ and $m$ be the least nonnegative integer for which its $m$th
ordinary logarithmic iterate $x_m$ is at most $4$.
When $m\ge1$, $\log(en)\le1+x_1$. For $1\le j<m$ we have $x_j>4$,
so (12) inductively yields
$\ell_{m-1}(\log(en))\le1+x_m\le5$.
When $m=0$, $n+2\le4$ and $\log(en)<5$ directly.
Also $g$ maps $[0,5]$ into $[0,5]$. Therefore
$$
 r=\max(1,m-1)\quad\hbox{satisfies}\quad
 \ell_r(\log(en))\le5,\qquad r\le\log^*(n+2). \tag{13}
$$
Indeed reaching $4$ occurs no later than reaching $1$, and
$\log^*(n+2)\ge1$ for $n\ge1$. Inserting (13) into (11) proves the
$16^{\log^*}$ bound after absorbing $25$ into the universal constant, and the
$4^{\log^*}$ reciprocal-Cheeger bound follows likewise. Each dimension uses
one finite depth; the argument takes no infinite-depth limit.

Finally, let $\mu$ have mean $m$ and positive definite covariance $\Sigma$,
and let $\rho$ be the law of $\Sigma^{-1/2}(X-m)$, which is isotropic and
log-concave. For a locally Lipschitz finite-energy test $f$, put
$h(y)=f(m+\Sigma^{1/2}y)$. Then
$$
 \operatorname{Var}_\mu f=\operatorname{Var}_\rho h,
 \qquad \int|\nabla h|^2d\rho
 =\int\nabla f^T\Sigma\nabla f\,d\mu
 \le\|\Sigma\|_{\rm op}\int|\nabla f|^2d\mu.
$$
The isotropic inequality, which includes $L^2$ membership of finite-energy
tests, applies to $h$ and proves both affine Poincaré estimates.
:::

**Dependencies and fences.** The generic transfer uses only
[](#lem:sz-analytic-foundations), [](#thm:letwin-qcts), and the established
bounded-witness and Cheeger comparison from [@KLnotes]. The all-depth result
adds [](#thm:sz-iterated-curvature); its affine corollary only uses the all-depth
result. There are no `bounded_by` edges on these nodes. These estimates retain
dimension dependence and prove no CMH statement or universal-time occupation
bound. The transfer has a profile hypothesis within its universally quantified
implication; applying it here discharges that hypothesis separately at every
finite depth using the iterated-curvature theorem.
