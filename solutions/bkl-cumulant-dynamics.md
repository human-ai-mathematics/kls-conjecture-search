---
title: 'BKL: inverse-covariance cumulant dynamics'
ledger-node: lem:bkl-cumulant-dynamics
numbering:
  enumerator: "132.%s"
---

*Part of the Bizeul–Klartag–Lehec proof, Chapter [](#sec:bkl-proof); the reading order is on the [full proofs](#sec:proofs-bkl) page.*

**Overview.** This dossier reconstructs Section 4 of
[@BizeulKlartagLehec2026KLS, version 1, equations (67)–(79)]. It derives the
inverse-covariance localization equations and proves that their solution is global
for compactly supported initial laws. A separate, deliberately dimension-dependent
moment estimate justifies the expectation arguments used later. It is not an input
to the dimension-free induction.

**Author.** plan_framework researcher, unknown, 2026-10-06.

**Dependencies.** The conventions are [](#def:bkl-tilt-cumulants). We use
[](#prop:letwin-kappa) together with [](#thm:letwin-qcts), discharging the former's
antecedent, to obtain the third-cumulant estimate. We use ordinary finite-dimensional
Itô calculus, local existence and uniqueness for locally Lipschitz SDE coefficients,
and preservation of log-concavity under linear images. No KLS estimate, Riccati
covariance process, higher-cumulant bound or Song–Zhang criterion is used.

:::{prf:theorem} Dynamics and finite-time integrability
:label: thm:sol-bkl-cumulant-dynamics
Let $\mu$ be a compactly supported isotropic log-concave probability measure on
$\mathbb R^n$. There is a unique global strong solution, starting from $c_0=Q_0=0$,
of
$$
 \frac{d\mu_t}{d\mu}(x)=Z_t^{-1}
 e^{\langle c_t,x\rangle-\langle Q_tx,x\rangle/2},\qquad
 dc_t=A_t^{-1}a_t\,dt+A_t^{-1/2}\,dB_t,\qquad dQ_t=A_t^{-1}\,dt,
$$
where $a_t=\int x\,d\mu_t$ and $A_t=\operatorname{Cov}(\mu_t)$.
The covariance is positive definite at every finite time. Put
$\kappa_m(t)=\kappa_m^{\mu_t}$ and
$H_{i,t}=\kappa_3(t)(\cdot,\cdot,A_t^{-1/2}e_i)$. Then
$$
 da_t=A_t^{1/2}dB_t,\qquad
 dA_t=\sum_iH_{i,t}\,dB_{t,i}-A_t\,dt,\qquad
 \mathbb EA_t=e^{-t}I.
$$
For $m\ge3$, define
$$
 L_m(t)(h_1,\ldots,h_m)=
 \sum_{\substack{J\subset[m],\ 1\in J\\2\le |J|\le m-2}}
 \left\langle\kappa_{|J|+1}(t)(h_J,\cdot),
 A_t^{-1}\kappa_{m-|J|+1}(t)(h_{J^c},\cdot)\right\rangle.
$$
The sum is zero for $m=3$. The cumulants satisfy
$$
 d\kappa_m(t)=\kappa_{m+1}(t)(\cdot,\ldots,\cdot,A_t^{-1/2}dB_t)
 -(m\kappa_m(t)+L_m(t))\,dt.
$$
For a tensor of order $r$ set
$|T|_t^2=\langle T,(A_t^{-1})^{\otimes r}T\rangle$.
For every deterministic unit vector $u$, let
$\mathcal E_m(t)=|\kappa_m(t)(u,\cdot,\ldots,\cdot)|_t^2$.
Then
$$
 \sum_iH_{i,t}A_t^{-1}H_{i,t}\le8A_t,\qquad
 \mathcal E_2(t)=\langle A_tu,u\rangle,\qquad
 \mathcal E_3(t)\le8\langle A_tu,u\rangle.
$$
For every fixed $n,m$ the processes $\mathcal E_m$ and
$|L_m(t)(u)|_t^2$ have deterministic bounds depending on $n,m$ and the initial
support radius. The Itô local martingale term of each $\mathcal E_m$ is a true
square-integrable martingale on every bounded time interval.
:::

:::{prf:proof}
**Local construction and the third-order input.** Suppose the support is contained
in a ball of radius $R$ centered at the origin. For every finite pair $(c,Q)$,
the tilted law has the same support as $\mu$. Its covariance is positive definite
because isotropy makes that support full dimensional. Compact support permits
differentiation of the partition function to every order. Thus its mean and
covariance, the inverse covariance and its positive square root are smooth locally
in $(c,Q)$. The SDE consequently has a unique strong solution up to its explosion
time. Along this solution $Q_t$ is positive semidefinite, so $\mu_t$ is log-concave.

The stated Letwin inputs give, for any isotropic log-concave $\nu$ and any $v$,
$$
 |\kappa_3^\nu(v)|^2\le8|v|^2.
$$
Indeed, for symmetric $M$, the covariance of $\langle v,X\rangle$ with
$X^TMX$ is $\langle\kappa_3^\nu(v),M\rangle$; Cauchy–Schwarz and the
quadratic-chaos variance bound give its square at most $8|v|^2|M|_{\rm HS}^2$.
Take the supremum over symmetric matrices of Hilbert–Schmidt norm one.

**The density and covariance equations.** All calculations initially take place
before an exit time from a compact subset of the finite $(c,Q)$ parameter space.
For $g_t(x)=\exp(\langle c_t,x\rangle-\langle Q_tx,x\rangle/2)$, Itô's formula gives
$$
 \frac{dg_t(x)}{g_t(x)}=\langle x,A_t^{-1}a_t\rangle dt
 +\langle x,A_t^{-1/2}dB_t\rangle.
$$
Integrating gives
$dZ_t/Z_t=\langle a_t,A_t^{-1}a_t\rangle dt+
\langle a_t,A_t^{-1/2}dB_t\rangle$. The quotient rule, including its cross
variation, cancels the drift and yields
$$
 dp_t(x)=p_t(x)\langle A_t^{-1/2}(x-a_t),dB_t\rangle,
 \qquad p_t=g_t/Z_t.
$$
Consequently, for any bounded measurable $f$ on the support,
$$
 d\int f\,d\mu_t=
 \left\langle A_t^{-1/2}\int f(x)(x-a_t)\,d\mu_t(x),dB_t\right\rangle.
$$
Apply this identity to $x$ and $xx^T$, and subtract $d(a_ta_t^T)$.
The barycenter noise is $A_t^{1/2}dB_t$, whose quadratic variation is $A_tdt$.
The centered third moment is the remaining covariance noise. This proves the two
claimed SDEs, initially up to explosion.

Let $\nu_t$ be the image of $\mu_t$ under $x\mapsto A_t^{-1/2}(x-a_t)$.
For $m\ge2$, affine covariance of the derivatives of the logarithmic Laplace
transform gives
$$
 |\kappa_m(t)(v)|_t^2
 =|\kappa_m^{\nu_t}(A_t^{1/2}v)|^2.
$$
In particular, the third-order estimate gives $\mathcal E_3\le8\langle A_tu,u\rangle$.
The quadratic form of $\sum_iH_iA_t^{-1}H_i$ at $v$ is exactly
$|\kappa_3(t)(v)|_t^2$. This proves the matrix inequality.

**No finite-time explosion.** Set $G_i=A_t^{-1/2}H_iA_t^{-1/2}$. The preceding
inequality implies $\sum_iG_i^2\le8I$. Applying Itô to $\log\det A_t$ gives
$$
 d\log\det A_t=\sum_i\operatorname{Tr}(G_i)dB_{t,i}
 -\left(n+\frac12\sum_i\operatorname{Tr}(G_i^2)\right)dt.
$$
Its drift lies between $-5n$ and $-n$, and the bracket of its local martingale
is at most $8n^2dt$, since $(\operatorname{Tr}G_i)^2\le n\operatorname{Tr}(G_i^2)$.
These bounds hold uniformly under stopping. On any deterministic interval $[0,T]$
the stopped stochastic integral extends continuously to the explosion time:
extend its integrand by zero after that time, and use its bounded quadratic
variation. Hence $\log\det A_t$ is bounded below before $T$ on each path.
Compact support gives $A_t\le R^2I$. The determinant lower bound therefore bounds
$A_t^{-1}$ on that path before $T$. It also bounds the coefficients of $c_t,Q_t$,
because $|a_t|\le R$. Their drift integrals and stochastic integrals have finite
limits. Local existence at these finite limiting parameters extends the solution,
contradicting a finite explosion time. The solution is therefore global.

**Expectation of the covariance.** The process $e^tA_t$ is a local martingale by
its SDE, and all its entries are bounded by $e^TR^2$ on $[0,T]$. It is a true
martingale. Since $A_0=I$, its expectation is $I$. This proves
$\mathbb EA_t=e^{-t}I$ and, in particular,
$\mathbb E\mathcal E_2(t)=e^{-t}$ and
$\mathbb E\mathcal E_3(t)\le8e^{-t}$.

**The cumulant equation.** Write
$M_t(z)=\int e^{\langle z,x\rangle}\,d\mu_t(x)$,
$\Lambda_t=\log M_t$, and $v_t(z)=\nabla\Lambda_t(z)-a_t$.
The bounded support and stopped parameter coefficients justify differentiation
and stochastic integration in either order, on compact sets of $z$. The density
equation and scalar Itô formula give
$$
 d\Lambda_t(z)=\langle A_t^{-1/2}v_t(z),dB_t\rangle
 -\tfrac12\langle v_t(z),A_t^{-1}v_t(z)\rangle dt.
$$
At zero, $v_t(0)=0$ and its $r$th derivative, contracted against a further
vector, is $\kappa_{r+1}(t)$. The $m$th derivative of the noise is the asserted
$(m+1)$st cumulant. Leibniz's rule for the quadratic drift is the sum over
nonempty proper subsets $J\subset[m]$. Its $2m$ singleton or co-singleton terms
each equal $\kappa_m(t)$, because one factor is $A_th_j$ and cancels $A_t^{-1}$.
The remaining terms occur in equal complementary pairs. Selecting the member
containing the first index and accounting for the prefactor $1/2$ gives precisely
$L_m(t)$. This proves the equation, including $L_3=0$.

**Crude moment bounds, independent of the induction.** For completeness there are
finite constants $D_{n,m}$ such that every isotropic log-concave $\nu$ on
$\mathbb R^n$ satisfies $|\kappa_m^\nu(v)|^2\le D_{n,m}|v|^2$. No dimension-free
claim is made here. To see this, a centered variance-one one-dimensional
log-concave marginal $Y$ has a log-concave survival function $S(t)$.
This last fact follows either by integration of a log-concave density or directly
from its increasing hazard: for density $f$, the ratio
$S(t)/f(t)=\int_0^\infty f(t+s)/f(t)\,ds$ is nonincreasing, by concavity of
$\log f$. Endpoints follow by limits. Chebyshev gives $S(2)\le1/4$ and
$S(-2)\ge3/4$. Concavity of $\log S$ therefore gives, for $t\ge2$,
$$
 S(t)\le\tfrac14\exp\bigl(-(\log3)(t-2)/4\bigr).
$$
If $S(2)=0$, its upper tail vanishes and the displayed bound is immediate.
The same argument applies to $-Y$. Integration of the two tails gives a finite
universal upper bound for $\mathbb E|Y|^p$ at every fixed $p$.

For unit vectors $v_1,\ldots,v_m$, Hölder bounds every mixed moment
$\mathbb E\prod_{j\in J}\langle v_j,X\rangle$ in terms of $|J|$ alone.
The moment-cumulant formula
$$
 \kappa_m(v_1,\ldots,v_m)=
 \sum_{\pi\in\mathcal P([m])}(-1)^{|\pi|-1}(|\pi|-1)!
 \prod_{J\in\pi}\mathbb E\prod_{j\in J}\langle v_j,X\rangle
$$
then bounds each mixed cumulant by a finite $C_m$. Summing its square over the
$n^{m-1}$ coordinate choices gives $D_{n,m}=n^{m-1}C_m^2$.
Whitening the posterior now gives
$$
 \mathcal E_m(t)\le D_{n,m}\langle A_tu,u\rangle\le D_{n,m}R^2.
$$
For a summand of $L_m$ with $|J|=a$, sum first over the whitened coordinates in
$J^c$, apply the same bound for $\kappa_{m-a+1}$, and then sum over those in
$J\setminus\{1\}$. Its squared weighted norm is at most
$D_{n,m-a+1}\mathcal E_{a+1}(t)$: the contracted vector is
$A_t^{-1}\kappa_{a+1}(t)(u,h_{J\setminus\{1\}},\cdot)$, whose $A_t$-norm
is exactly the sum over the final whitened contraction index. The finite sum
over $J$ therefore bounds $|L_m(t)(u)|_t^2$ deterministically as well.

Finally write $r=m-1$, $T=\kappa_m(t)(u)$,
$W_i=\kappa_{m+1}(t)(u,\cdot,\ldots,\cdot,A_t^{-1/2}e_i)$,
$\widetilde T=(A_t^{-1/2})^{\otimes r}T$, and
$\widetilde W_i=(A_t^{-1/2})^{\otimes r}W_i$.
The noise coefficient of $\mathcal E_m$ is
$$
 \beta_i=2\langle\widetilde T,\widetilde W_i\rangle
 -\left\langle\widetilde T,\sum_{s=1}^rG_i^{(s)}\widetilde T\right\rangle,
$$
where $G_i^{(s)}$ acts on tensor slot $s$. Since $\sum_iG_i^2\le8I$,
$$
 \sum_i\beta_i^2\le8\mathcal E_m\mathcal E_{m+1}
 +16r^2\mathcal E_m^2.
$$
This is bounded deterministically. The drift is integrable on finite intervals
as well: the second derivative of the inverse metric consists of finitely many
terms bounded by $\mathcal E_m$, $\mathcal E_{m+1}$ and
$\sqrt{\mathcal E_m}|L_m(u)|_t$, using the same matrix inequality.
Thus localization may be removed in expectations. These observations establish
the final integrability assertion and supply the precise justification for the
energy argument of [](#lem:bkl-cumulant-energy). All assertions concerning a
fixed vector extend from unit $u$ to arbitrary $u$ by homogeneity; each energy
and squared norm acquires a factor $|u|^2$. In particular,
$\int_0^\infty\mathbb E\mathcal E_2(t)\,dt=|u|^2$.
:::

**Fences respected.** There is no assigned `bounded_by` fence. All stochastic
expectations here are for compactly supported initial laws; passage to noncompact
laws is made only for the final static cumulant estimate. The covariance drift is
$-A_t$, not the $-A_t^2$ drift of another localization clock.
