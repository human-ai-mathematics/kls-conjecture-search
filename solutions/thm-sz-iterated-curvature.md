---
title: "Iterating polynomial and curvature estimates with uniform constants"
ledger-node: thm:sz-iterated-curvature
numbering:
  enumerator: "122.%s"
---

*Part of the first version of Song–Zhang, Chapter [](#sec:polynomial-curvature); the reading order is on the [full proofs](#sec:proofs-sz-v1) page.*

**Overview.** This reconstructs Section 6 of [@SongZhang2026IteratedLogKLS].
First a curvature bound is extended to affine normalizations of possibly
nonsmooth localization posteriors. Next the derivative hierarchy gives new
polynomial coefficients. Retaining its zero initial data makes the additional
coefficient loss tend to one at large depth. Finally the comparison
[](#thm:sz-curvature-comparison) closes a finite-depth induction, with every
initialization and admissibility threshold paid explicitly.

:::{prf:theorem} All finite depths, with one universal envelope
:label: thm:sol-sz-iterated-curvature
Put $g(x)=\log(e+x)$, $\ell_0(x)=x$ and $\ell_r=g^{\circ r}$.
There exist a universal $C_0>0$ and universal constants $\Gamma_r\le C_0 4^r$
such that, in every dimension, every centered probability measure
$\nu=e^{-W}dx$ with smooth $W$, covariance at most $I$, and
$aI\preceq D^2W\preceq bI$ for some $0<a\le b<\infty$, satisfies
$$
 C_P(\nu)\le\Gamma_r^2\ell_r(a^{-1})^2\qquad(r\ge1).
$$
This is [](#thm:sz-iterated-curvature).
:::

## Extending a regular curvature profile

:::{prf:lemma} Affine inflation of a profile
:label: lem:sol-sz-profile-inflation
Suppose a continuous $F:(0,\infty)\to(0,\infty)$ satisfies
$C_P(\eta)\le F(a)$ for every centered regular measure with covariance at most
$I$ and curvature at least $aI$. If $\nu$ has positive covariance $A$ and
density proportional to $\exp(-x^TBx/2-V(x))$, with $B\succ0$ and
extended-valued convex $V$, then, for every $\delta>0$ and every locally
Lipschitz finite-energy $f$,
$$
 \operatorname{Var}_\nu f\le F(\delta)
 \mathbb E_\nu[\nabla f^T(A+\delta B^{-1})\nabla f].
$$
:::

:::{prf:proof}
First take a centered, possibly nonsmooth measure $\eta$ of covariance at most
$I$ and curvature at least $aI$. Convolving with $N(0,tI)$ gives a smooth
positive density with potential Hessian
$t^{-1}I-t^{-2}\operatorname{Cov}(X\mid X+\sqrt tZ=y)$.
The conditional law has curvature at least $(a+t^{-1})I$; the constant-curvature
Brascamp--Lieb inequality [@BrascampLieb1976; @BakryGentilLedoux2014, Theorem 4.9.1] bounds this conditional covariance
by $(a+t^{-1})^{-1}I$. Thus the Hessian lies between
$a/(1+at)I$ and $t^{-1}I$. This use of Brascamp--Lieb on an extended-valued
convex potential is the same nonsmooth form used in the polynomial proof.
Dividing the convolved vector by $\sqrt{1+t}$ makes its covariance at most $I$
and curvature at least $a_t=a(1+t)/(1+at)$. The regular profile gives
$C_P\le F(a_t)$, and $F(a_t)\to F(a)$. Weak convergence passes the inequality
to compact smooth tests. The clipping and cutoff argument of
[](#lem:sz-analytic-foundations) extends it to every finite-energy locally
Lipschitz test. To handle varying constants directly, use the common bound
$F(a)+\zeta$ for all sufficiently small $t$, then let $\zeta\downarrow0$.

Now put $M=A+\delta B^{-1}$ and $Y=M^{-1/2}(X-\mathbb EX)$.
Its covariance is $M^{-1/2}AM^{-1/2}\preceq I$. Since
$M\succeq\delta B^{-1}$, inversion gives $B\succeq\delta M^{-1}$,
so the potential of $Y$ has curvature at least $\delta I$.
Applying the extended profile to
$y\mapsto f(\mathbb EX+M^{1/2}y)$ gives the stated gradient form.
No matrices were commuted. Strong convexity supplies Gaussian tails, so
polynomial tests have finite energy as well.
:::

We record elementary estimates used uniformly in the depth. Concavity and
$g(0)=1$ imply $g(cx)\le c g(x)$ for $c\ge1$; induction gives
$$
 \ell_r(x)\ge1,\quad \ell_r(cx)\le c\ell_r(x),\quad
 \ell_r(2308d^2)\le10\ell_r(d)\quad(r,d\ge1). \tag{1}
$$
For the last assertion,
$e+2308d^2\le2309(e+d)^2$ and $\log2309<8$ give
$g(2308d^2)\le10g(d)$; apply the scaling estimate to the remaining compositions.
Furthermore
$$
 {xg'(x)\over g(x)}\le\tfrac12\quad(x>0).
$$
Indeed, setting $t=e+x$, the required inequality is
$t\log t-2t+2e\ge0$; its derivative is $\log t-1\ge0$ for $t\ge e$,
and its value at $e$ is $e$. Integration of this logarithmic derivative and
composition yield
$$
 \log{\ell_r(u)\over\ell_r(v)}\le2^{-r}\log(u/v)
 \quad(u\ge v>0, r\ge0). \tag{2}
$$

## A coarse coefficient improvement

Suppose for some $r\ge1$ and $\Gamma\ge1$ we have the curvature profile
$F(a)=\Gamma^2\ell_r(a^{-1})^2$ for every regular covariance contraction.
Write $\ell=\ell_r$, $b_0=1$, and $b_s=\ell(s)^s/(s+1)^2$ for $s\ge1$.
Monotonicity gives
$$
 \sum_{k=1}^s{b_kb_{s-k}\over b_s}\le16,
 \qquad {b_d\over b_{d-1}}\ge\ell(d){d^2\over(d+1)^2}
 \ge\ell(d)/4. \tag{3}
$$
The ratio statement includes $d=1$ by the definition of $b_0$.
For the convolution sum, replace all logarithmic factors by $\ell(s)$ and
split the index set at $s/2$. The reciprocal square from the larger index
contributes at most $4/(s+1)^2$; summing the other reciprocal squares on each
half gives a bound smaller than $16$, including the endpoint $s-k=0$.

We prove, simultaneously for all isotropic log-concave measures,
$$
 c_d\le R^db_d,\qquad R=2^{12}\Gamma. \tag{4}
$$
Here $c_d=\sqrt{K_d}/d!$ has the Appell normalization of
[](#thm:sz-polynomial-variance). Degree one follows from $c_1=1$ and $R\ge4$.
For the induction step take a compactly supported isotropic initial law and
$f=P_d[T]$, $T\ne0$. Use the global covariance-adapted localization
[](#lem:sol-sz-localization) and its derivative hierarchy
[](#lem:sol-sz-hierarchy), both proved in the polynomial dossier.
Explicitly, $A_t$ is the posterior covariance, $\Lambda_t=\int_0^tA_s^{-1}ds$
is its curvature matrix, $h_j(t)=\mathbb E_tD^jf$, and
$$
 N_j(t)=\mathbb E_{\rm loc}\langle h_j,A_t^{\otimes j}h_j\rangle,
 \quad L_j(t)=\mathbb E_{\rm loc}\mathbb E_t
 \langle D^jf-h_j,A_t^{\otimes j}(D^jf-h_j)\rangle.
$$
The hierarchy gives $N_j'\le4j^2N_j+9j^2L_j$ almost everywhere.
The lower-degree inductive bounds apply to every whitened posterior.
The Appell expansion, followed by the $L^2$ triangle inequality over its full
output tensor direct sum and over localization randomness, gives
$$
 \sqrt{L_j(t)}\le\sum_{k=1}^{d-j}R^kb_k\sqrt{N_{j+k}(t)}. \tag{5}
$$
Each additional derivative index carries the same covariance factor as the
original derivative indices; this is an affine change of variables, not a
scalar covariance bound.

Put $Q=(d!)^2\|T\|_{\rm HS}^2$, $w_s=R^{2s}b_s^2$, and
$M(t)=\max_{1\le j\le d}N_j(t)/(Qw_{d-j})$.
Appell centering implies $N_d(0)=Q$, $N_j(0)=0$ for $j<d$, and $M(0)=1$.
Equations (3),(5) give $L_j\le256Qw_{d-j}M$, with $L_d=0$.
Integrating the hierarchy gives
$M(t)\le1+2308d^2\int_0^tM(s)ds$, hence $M(t)\le e^{2308d^2t}$.
At $\tau=1/(2308d^2)$, for $0\le s\le\tau$,
$$
 G_1(s):=\mathbb E_{\rm loc}\mathbb E_s[\nabla f^TA_s\nabla f]
 =N_1(s)+L_1(s)\le257eQ R^{2d-2}b_{d-1}^2. \tag{6}
$$

Here are the variance and terminal-transfer identities needed in both
coefficient inductions. The localization martingales for $f,f^2$ give
$V'(t)=-\mathbb E_{\rm loc}|\operatorname{Cov}_t(f,\xi_t)|^2\ge-V(t)$,
where $V(t)=\mathbb E_{\rm loc}\operatorname{Var}_t f$ and
$\xi_t=A_t^{-1/2}(X-m_t)$ is isotropic. Bessel's inequality supplies the last
bound. Therefore $V(\tau)\ge e^{-\tau}\operatorname{Var}_0f$.
Also
$$
 \Lambda_\tau^{-1}\preceq\tau^{-2}\int_0^\tau A_sds. \tag{7}
$$
To verify (7) test on $v$ and expand
$\int_0^\tau|A_s^{1/2}v-\tau A_s^{-1/2}\Lambda_\tau^{-1}v|^2ds$.
The result is
$\int_0^\tau v^TA_svds-\tau^2v^T\Lambda_\tau^{-1}v$.
For $s\le\tau$, the posterior martingale of each fixed product
$\partial_if\partial_jf$ and the $\mathcal F_s$-measurability of $A_s$ give
$$
 \mathbb E_{\rm loc}\mathbb E_\tau[\nabla f^TA_s\nabla f]=G_1(s). \tag{8}
$$
All quantities are integrable because the initial support is compact.
The profile-inflation lemma at time $\tau$, together with (7),(8), consequently
gives for any $\delta>0$
$$
 \operatorname{Var}_0f\le e^\tau\Gamma^2\ell_r(\delta^{-1})^2
 \left(G_1(\tau)+\delta\tau^{-2}\int_0^\tau G_1(s)ds\right). \tag{9}
$$
This identity retains the correlation between the earlier covariance and the
terminal derivative products.

Choose $\delta=\tau$. Equations (1),(6),(9) bound the variance by
$2e^2\cdot257\cdot100\Gamma^2\ell_r(d)^2 Q R^{2d-2}b_{d-1}^2$.
By (3) this is at most $Q R^{2d}b_d^2$ because
$16\cdot2e^2\cdot257\cdot100<2^{24}=R^2/\Gamma^2$
(use $e^2<8$ for the strict comparison). This proves (4) at degree $d$ for
compact initial laws. Condition any isotropic law on increasing centered balls,
then center and whiten. All fixed moments converge, as do the recursively
specified Appell coefficients, so the degree-$d$ inequality passes to the limit.
This completes induction over all measures. Finally, a centered covariance
contraction inherits the estimate from its isotropic whitening, since the map
$T\mapsto(\operatorname{Cov}\nu)^{\otimes d/2}T$ contracts Hilbert--Schmidt
norm. Singular covariances are treated on their affine support. Thus (4) holds
for every centered covariance contraction as well.

## The coefficient improvement with summable additional loss

:::{prf:lemma} Uniformity in both degree and iteration depth
:label: lem:sol-sz-sharp-coefficients
There exist universal $K\ge1$ and an integer $r_0\ge2$ such that the following
holds. Suppose $r\ge r_0$, $\Gamma\ge Kr^2$, and
$C_P(\nu)\le\Gamma^2\ell_r(a^{-1})^2$ for every centered regular measure of
covariance at most $I$ and curvature at least $aI$.
Then all centered log-concave covariance contractions satisfy
$$
 c_d\le R^d{\ell_r(d)^d\over(d+1)^2}\quad(d\ge1),
 \qquad R=(1+r^{-2})\Gamma.
$$
:::

:::{prf:proof}
Put $\alpha=r^{-2}$ and $D_r=\lceil32r^2\rceil$. Use the same $b_s,w_s,Q,N_j,L_j$
and induct on degree, starting the hierarchy step only at $d\ge D_r$.
The estimates preceding (6) remain valid with this new $R$, as they use only
the inductive lower-degree bounds. But keeping the zero initial conditions in
the integrated hierarchy improves them to
$$
 N_j(t)\le2304d^2t e^{2308d^2t}Qw_{d-j}\quad(j<d),
 \qquad N_d(t)\le Qe^{4d^2t}. \tag{10}
$$
Indeed variation of constants gives
$N_j(t)\le2304j^2Qw_{d-j}\int_0^t
 e^{4j^2(t-s)+2308d^2s}ds$, whose integrand is at most $e^{2308d^2t}$.

For $0<\eta<1$, set $\tau=\eta/d^2$. In (5) at $j=1$, separate the last term
$k=d-1$, which contains $N_d$, from all others, to which the first bound of
(10) applies. Using (3), for $0\le t\le\tau$,
$$
 \sqrt{L_1(t)}\le Q^{1/2}R^{d-1}b_{d-1}
 \left(e^{2\eta}+16\sqrt{2304\eta}\,e^{1154\eta}\right).
$$
It follows that
$$
 G_1(t)\le A(\eta)QR^{2d-2}b_{d-1}^2,
 \quad A(\eta)=2304\eta e^{2308\eta}
 +(e^{2\eta}+16\sqrt{2304\eta}\,e^{1154\eta})^2. \tag{11}
$$
In particular there exist universal $M,\eta_0>0$ such that
$\log[e^\eta(1+\eta)A(\eta)]\le M\sqrt\eta$ for
$0<\eta\le\eta_0$. This follows directly by expanding the finitely many
exponential factors at zero; alternatively the quotient by $\sqrt\eta$
extends continuously to zero and is bounded on any sufficiently short compact
interval.

Apply (9) with $\delta=\eta\tau$. Since $\tau\le\eta$,
$\delta^{-1}=d^2/\eta^2$, and the integral term adds at most $\eta$ times the
bound for $G_1$, the induction closes whenever
$$
 e^\eta(1+\eta)A(\eta)
 {\ell_r(d^2/\eta^2)^2\over\ell_r(d)^2}
 {(d+1)^4\over d^4}\le(1+\alpha)^2. \tag{12}
$$
Choose a universal $0<c<\min(1,\eta_0)$ so small that
$M\sqrt c\le1/2$, and set $\eta=c\alpha^2$.
The first factor of (12) is then at most $e^{\alpha/2}$ for every
$0<\alpha\le1$. For all $d\ge1$,
$$
 g(d^2/\eta^2)\le2g(d)+2\log(1/\eta)
 \le[2+2\log(1/\eta)]g(d).
$$
The first inequality follows from
$e+d^2/\eta^2\le(e+d)^2/\eta^2$; the second uses $g(d)\ge1$.
Apply (2) to the remaining $r-1$ compositions:
$$
 \log{\ell_r(d^2/\eta^2)\over\ell_r(d)}
 \le2^{-(r-1)}\log[2+2\log(1/\eta)]\le\alpha/8 \tag{13}
$$
for all $r$ above one universal $r_0$. The uniformity in $d$ is explicit:
$d$ has disappeared from the upper bound. Existence of such $r_0$ follows
from $r^2 2^{-(r-1)}\log[2+2\log(r^4/c)]\to0$.
For $d\ge D_r$, also $4\log(1+1/d)\le4/d\le\alpha/8$.
Together (12)'s left side is at most
$e^{\alpha/2+\alpha/4+\alpha/8}=e^{7\alpha/8}\le(1+\alpha)^2$,
since $2\log(1+\alpha)\ge\alpha$ on $[0,1]$.

It remains to initialize the entire range $d<D_r$ independently of the
hierarchy. The universal polynomial theorem gives $c_d\le32^dd!$.
If $\Gamma\ge128D_r$, then
$$
 32^dd!\le{(128D_r)^d\over(d+1)^2}\le R^db_d;
$$
use $d!\le D_r^d$, $(d+1)^2\le4^d$, and $\ell_r(d)\ge1$.
As $D_r\le33r^2$, choose $K\ge128\cdot33$.
This initializes every smaller degree before the step at $d\ge D_r$.
Conditioning, whitening, fixed-order moment convergence and affine contraction
remove compactness and isotropy exactly as in the preceding induction.
:::

## Closing the depth induction

:::{prf:proof} Proof of the theorem
The universal polynomial estimate gives
$c_k\le32^kk!\le128^kk^k/(k+1)^2$.
Use [](#thm:sz-curvature-comparison) with $\varepsilon=1$, $R=2^{40}$,
and $\ell(k)=k$. Let $h=g(a^{-1})\ge1$ and choose dyadic $d$ with
$\max(2,h)\le d<2\max(2,h)\le6h$.
Because $\log(a^{-1})\le h$ when $a^{-1}\ge1$,
$\max(1,a^{-1/(d+1)})\le e$.
The comparison therefore gives
$$
 C_P(\nu)\le36e\,2^{85}h^2\le(2^{48})^2\ell_1(a^{-1})^2.
$$
This is the depth-one profile and makes no use of the final KLS conclusion.

Suppose a profile is available at depth $r$ with constant $\Gamma\ge2^{48}$.
The coarse coefficient improvement gives radius $R=2^{12}\Gamma\ge2^{40}$.
Apply the comparison again with $\varepsilon=1$ and the same dyadic choice.
By (1), $\ell_r(d)\le6\ell_r(h)=6\ell_{r+1}(a^{-1})$.
Consequently
$$
 C_P(\nu)\le36e\,2^{29}\Gamma^2\ell_{r+1}(a^{-1})^2
 \le(2^{30}\Gamma)^2\ell_{r+1}(a^{-1})^2.
$$
Finite induction supplies preliminary constants
$\widehat\Gamma_r=2^{48+30(r-1)}$ at every fixed depth.

For $r\ge r_0$, put $\alpha_r=r^{-2}$ and suppose $\Gamma\ge Kr^2$.
The sharp coefficient lemma supplies $R=(1+\alpha_r)\Gamma$.
Use the curvature comparison with $\varepsilon=\alpha_r$;
its additional hypothesis is $R\ge2^{40}r^4$.
Choose dyadic $d$ with $h/\alpha_r\le d<2h/\alpha_r$.
Since $r\ge2$, this automatically has $d\ge2$.
Then $\max(1,a^{-1/(d+1)})\le e^{\alpha_r}$ and, by (2),
$$
 \log{\ell_r(d)\over\ell_r(h)}
 \le2^{-r}\log(2/\alpha_r)\le\alpha_r
$$
for all sufficiently large $r$, after increasing the fixed $r_0$.
Taking square roots of the comparison gives
$$
 C_P(\nu)^{1/2}
 \le4(1+\alpha_r)^{3/2}e^{3\alpha_r/2}
       \Gamma\ell_{r+1}(a^{-1})
 \le4e^{3/r^2}\Gamma\ell_{r+1}(a^{-1}).
$$
Thus define $\Gamma_{r+1}=4e^{3/r^2}\Gamma_r$ for $r\ge r_0$.
To justify every application, choose the initial constant large enough that
$$
 \Gamma_{r_0}\ge\widehat\Gamma_{r_0},\qquad
 4^{r-r_0}\Gamma_{r_0}\ge\max(Kr^2,2^{40}r^4)
 \quad\hbox{for all }r\ge r_0. \tag{14}
$$
One finite choice exists because each polynomial divided by $4^r$ is bounded.
The recurrence implies $\Gamma_r\ge4^{r-r_0}\Gamma_{r_0}$, so (14)
pays both thresholds before the next step is applied.
Also
$$
 \Gamma_r=4^{r-r_0}\Gamma_{r_0}
 \exp\!\left(3\sum_{j=r_0}^{r-1}j^{-2}\right)\le C_0 4^r.
$$
For $r<r_0$, take $\Gamma_r=\widehat\Gamma_r$ and enlarge $C_0$ to cover
these finitely many values. Every profile used to obtain the next coefficient
bound has already been established at the previous finite depth, for all
regular covariance contractions. The profile-inflation lemma supplies its
extension to every posterior needed in that coefficient induction.
:::

**Dependencies and fences.** The argument uses
[](#lem:sz-analytic-foundations), [](#thm:sz-polynomial-variance) (including its
proved localization and hierarchy lemmas), and [](#thm:sz-curvature-comparison).
Brascamp--Lieb is an established literature input [@BrascampLieb1976; @BakryGentilLedoux2014, Theorem 4.9.1]. There are
no `bounded_by` edges on this node. In the brief's threshold test, (14) is the
explicit discharge for an exponentially growing sequence; it is not a
construction of an admissible bounded sequence. The argument neither proves
CMH nor provides universal-time occupation estimates. No infinite-depth limit
or dimension-free KLS conclusion is taken.
