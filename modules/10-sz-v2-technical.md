---
title: "Song–Zhang, second version: technical estimates"
numbering:
  enumerator: "10.%s"
---

(sec:sz-v2-blocks)=
# Song–Zhang, second version: technical estimates

The estimates in this chapter explain how the bounds of Chapter [](#sec:sz-v2-proof) are realized by actual functions. Three issues recur: removing means loses norm, normalization changes energy, and the derivative tensors are only partly symmetric. These losses must be controlled for the same family of functions. Separate estimates achieved by unrelated functions would not supply the iteration.

## Static transfer and tensor symmetries

Localization transfers a coefficient cap valid simultaneously in every degree to a better cap. The starting threshold below is independent of the size of that cap, which is essential when the cap is improved repeatedly.

:::{prf:proposition} Transfer of a static coefficient cap
:label: prop:sz-v2-static-coefficient-transfer
There is a universal integer $r_*\ge2$ with the following property.
Fix a dimension range consisting either of all positive integers or of
$1,\ldots,n$. Let $r\ge r_*$ and $\Gamma\ge1$, and use $\ell_r$ from
[](#thm:sz-v2-iterated-curvature). Suppose that every measure in
[](#def:sz-v2-common-radius) in this range satisfies, for every admissible
lower curvature bound $a>0$ and every integer $k\ge1$,
$$
c_k(\mu)\le[\Gamma\ell_r(a^{-1})]^{k-1}.
$$
Then every centered log-concave probability measure in the same dimension
range, with covariance at most $I$, satisfies
$$
c_d(\mu)\le[(1+r^{-2})\Gamma\ell_r(d)]^{d-1}\qquad(d\ge1).
$$
The threshold $r_*$ is independent of $\Gamma$, the dimension range and the law.
:::

The factor $1+r^{-2}$ is summable over the inner depths. The transfer retains the exponent $d-1$ from the common-radius normalization and passes to general log-concave laws only after obtaining a uniform regular-law estimate. The next algebraic estimate controls a tensor by one symmetric component and its failures of symmetry on successively larger groups of slots.

:::{prf:lemma} Joint partial symmetrization
:label: lem:sz-v2-joint-frame
Let $d\ge1$ be dyadic and let a finite-dimensional real Hilbert space
carry an orthogonal representation of the symmetric group on $2d$ letters.
For each dyadic $k\le d$, let $\mathsf P_k$ average permutations of the
first $k$ letters. For dyadic $k<d$, let $\mathsf S_k$ average permutations
of the next $3k$ letters, numbered $k+1,\ldots,4k$.
Then every vector $T$ satisfies
$$
\|T\|^2\le10^4\left[d\|\mathsf P_dT\|^2+
\sum_{\substack{k<d\\k\text{ dyadic}}}
k^2\|(I-\mathsf S_k)\mathsf P_kT\|^2\right].
$$
This includes tensor-slot permutations with arbitrary finite output direct sums.
:::

The dyadic groups let the proof charge an error to the scale where symmetry first fails. Finite output direct sums are included, so the same estimate applies to windows of several inverse-gradient iterates. Normalization supplies a second useful cancellation: an antisymmetric covariance term is paid by a deficit between two spectral energies.

:::{prf:lemma} Skew loss paid by normalization
:label: lem:sz-v2-skew-credit
Let $\mu$ be a measure in [](#def:sz-v2-common-radius), with diffusion
operator $H$. Let $U\in H^1(\mu;\mathbb R^n)$ be centered, with
$\|U\|_{L^2(\mu)}=1$ and symmetric $\mathbb E_\mu\nabla U$.
Define
$$
e=\|H^{1/2}U\|_2^2,\qquad
\beta=\|H^{-1/2}U\|_2^{-2},\qquad
LU=\mathbb E_\mu[X\otimes U],
$$
where inverse operators act componentwise and
$\operatorname{Skew}(M)=(M-M^{\mathsf T})/2$.
Then
$$
\beta\|\operatorname{Skew}(LU)\|_{\mathrm{HS}}^2\le1-\beta/e.
$$
:::

The nonnegative difference $1-\beta/e$ measures the slack in the comparison between direct and inverse spectral energies. Using it to pay the skew term avoids charging normalization and antisymmetry independently. This cancellation enters the compensated restart below.

## Exact operator identities and normalized losses

:::{prf:lemma} Restricted operator, orbit defects, and compensated normalization
:label: lem:sz-v2-operator-block-primitives
Let $\mu$ be a measure in [](#def:sz-v2-common-radius), with
$D^2W\succeq aI>0$. Let $H$ be its gradient-form operator on centered
$L^2(\mu)$, $B=H^{-1}$, $Lh=\mathbb E[Xh]$, $P_+h=h-\mathbb Eh$,
$D=P_+\nabla H^{-1/2}$, $\mathcal T=P_+\nabla B$, and
$\lambda=C_P(\mu)^{-1}$. Operators extend componentwise to finite families
and append ordered derivative slots. Define
$$R=\sup_{\substack{f\in H^1(\mu),\ f\text{ nonconstant}\\\mathbb E\nabla f=0}}
 \operatorname{Var}(f)/\mathbb E|\nabla f|^2.$$
Then $\mathcal T$ is compact,
$\mathcal T^*\mathcal T=B-L^*L$, $\|\mathcal T\|^2=R$,
$R\le C_P\le R+1$, and
$\|H^{1/2}\mathcal Th\|\le\|h\|$.

For a centered unit $f$, $z>0$, $w_j=z^{-j/2}\mathcal T^jf$,
$b_j=\|w_j\|^2$, $l_j=\|Lw_j\|^2$, and
$D_j=\|\nabla(B-zI)w_j\|^2$ ($j\ge1$),
$$D_j\le z(b_{j+1}-2b_j+b_{j-1})+l_j,$$
$$w_{j+1}=\sqrt zP_+\nabla w_j+z^{-1/2}P_+\nabla(B-zI)w_j.$$
The swap of the newest two derivative slots in $w_{j+1}$ has norm at most
$2\sqrt{D_j/z}$. Subsequent maps propagate it by $\mathcal T/\sqrt z$.

For a centered unit form-domain vector family $U$ with symmetric
$\mathbb E\nabla U$, of energy
$e=\|H^{1/2}U\|^2$, put $F=\sqrt\beta B^{1/2}U$,
$\beta=\|B^{1/2}U\|^{-2}$. If
$e^{-1}>\|\operatorname{Sym}(LU)\|^2$, centering $DF$, inverse-normalizing,
and rescaling to unit norm produces a family of energy at most
$[e^{-1}-\|\operatorname{Sym}(LU)\|^2]^{-1}$.
:::

The restricted operator identifies the energy scale after means are removed. Its orbit defect satisfies a discrete second-difference inequality, while swapping adjacent derivative slots costs the square root of that defect. The final normalization identity uses the skew credit to retain only the symmetric covariance loss. These identities connect the operator norm, tensor symmetry and energy on the same orbit.

:::{prf:lemma} Normalized hierarchy and exact orbit-window losses
:label: lem:sz-v2-normalized-hierarchy
Use the operator notation of [](#lem:sz-v2-operator-block-primitives).
Start with a centered unit form-domain family $F_0$ of energy $\nu$.
Let $u^j=DF_j$, and when $u^j\ne0$ define
$$\beta_{j+1}=\|u^j\|^2/\|B^{1/2}u^j\|^2,\qquad
 F_{j+1}=\sqrt{\beta_{j+1}}B^{1/2}u^j,\qquad
 \chi_j=\|H^{1/2}u^j\|^2-\beta_{j+1}\|u^j\|^2.$$
After a zero successor set all later families to zero, $\beta=\lambda$,
$\chi=0$. Write $v_j=\|F_j\|^2$, $e_j=\|H^{1/2}F_j\|^2$,
$p_j=\|LH^{1/2}F_j\|^2$, and
$P_N=\sum_{j<N}p_j$, $X_N=\sum_{j<N}\chi_j$, $V_N=\sum_{j<N}v_j$.
Then
$$v_{j+1}=v_j-p_j,\quad e_{j+1}\le e_j-av_j-\chi_j,
 \quad 0\le p_j\le\min(v_j,e_j),\quad\chi_j\ge0,$$
$$\lambda\le\beta_j\le e_{j-1}/v_j\quad(v_j>0),\qquad v_N=1-P_N,$$
$$aV_N+X_N\le\nu-e_N,\quad v_{N+1}\le R e_N,
 \quad aV_N+X_N\le\nu-R^{-1}+R^{-1}P_{N+1}.$$

If $Y$ is a finite centered family and $F_0=B^{1/2}Y/\|B^{1/2}Y\|$,
then at every nonzero generation $F_k$ is a positive scalar multiple of
$B^{1/2}\mathcal T^kY$ and
$$\frac{p_k}{v_k}=
 \frac{\|L\mathcal T^kY\|^2}
 {\langle\mathcal T^kY,B\mathcal T^kY\rangle}.$$
In particular if $Y=\bigoplus_{j=0}^{m-1}w_j$ is a window in a
$z$-normalized orbit, $S_k=\sum_{j=k}^{m+k-1}\|w_j\|^2$ and
$C_k=\sum_{j=k}^{m+k-1}\|Lw_j\|^2$, then
$$p_k/v_k=C_k/(zS_{k+1}+C_k).$$
:::

Here $P_N$ records lost mass and $X_N$ records the normalization deficit. The identity $v_N=1-P_N$ makes their role explicit: a hierarchy survives as long as its accumulated centering loss stays small. For an orbit window the ratio $p_k/v_k$ is exact, not a separate upper estimate. It permits an averaged window with small covariance loss to restart an actual normalized hierarchy.

:::{prf:lemma} Mesoscopic restricted-operator powers
:label: lem:sz-v2-mesoscopic-powers
Use $\mathcal T$ and $R$ from [](#lem:sz-v2-operator-block-primitives).
There are universal constants $R_0,C_*>0$ such that every measure in
that regular class with $R\ge R_0$ satisfies
$$
R-C_*/R\le\|\mathcal T^m\|^{2/m}\le R
\qquad(1\le m\le\lfloor R\rfloor+2).
$$
:::

On the initial range of powers, the squared operator scale stays within $C_*/R$ of $R$. This starts the construction without a bound derived from KLS. Longer blocks require the joint symmetry and loss estimates, which we state next.

## From symmetry to delayed centering losses

:::{prf:lemma} Raw joint frame
:label: lem:sz-v2-raw-joint-frame
Use the regular class and operators of [](#lem:sz-v2-operator-block-primitives),
and set $C_F=10^4$. Let $f$ be a finite centered $L^2$ family and $E\ge1$.
Let $z>0$, $w_j=z^{-j/2}\mathcal T^jf$, $b_j=\|w_j\|^2$,
$l_j=\|Lw_j\|^2$, and $D_j=\|\nabla(B-zI)w_j\|^2$ for $j\ge1$.
If $\|\mathcal T^h\|\le E z^{h/2}$ for $h\ge0$, then for dyadic
$d\ge2$ and $j\ge2d-1$,
$$
 l_j\le C_Fd c_d^2z^{-(d-1)}b_{j-d+1}
 +108C_FE^2\sum_{k<d\ {\rm dyadic}}k^5c_k^2z^{-k}
       \sum_{h=1}^{3k-1}D_{j-k+1-h}.                 \tag{B1}
$$
Without a global power bound, if $0<z\le R$, the same formula holds
with $E^2$ in the $k$ summand replaced by $(R/z)^{3k-2}$.
If instead $\|\mathcal T^h\|\le E(h+1)^\alpha z^{h/2}$ for
$0\le\alpha\le1$, (B1) holds with $E^2$ replaced by
$E^2(3k)^{2\alpha}$ in its $k$ summand.


:::

The symmetric term is controlled by the degree-$d$ coefficient; the remaining terms are orbit defects at smaller dyadic degrees. A bound on operator powers propagates each defect to the required position. The versions with exponential or polynomial propagation make explicit which power estimate is available at each stage of the construction.

:::{prf:lemma} Delayed losses under polynomial propagation
:label: lem:sz-v2-propagated-joint-loss
Use the operators and hierarchy of [](#lem:sz-v2-normalized-hierarchy),
and let $C_F=10^4$, $z>0$, $E\ge1$, and $B_*>0$.
For an actual normalized hierarchy with a centered unit starting family,
suppose instead
$\|\mathcal T^h\|\le E(h+1)^\alpha z^{h/2}$, where $0\le\alpha\le1$.
Let $2\le d_0\le d$ be dyadic and $J=2d_0-1$. On any prefix whose required
normalizers are at most $B_*$ put $t_* =\max\{1,B_*z\}$ and
$$
 \theta=5184C_FE^2\sum_{k<d\ {\rm dyadic}}
       k^8(B_*t_*^3)^k c_k^2,
$$
$$
 \Delta=P_J+2C_F\sum_{d_0\le k<d\ {\rm dyadic}}k^2B_*^kc_k^2,
 \qquad \tau=C_FdB_*^dc_d^2.
$$
Then, on each such justified prefix,
$$P_N\le\Delta+N\tau+(\theta/\lambda)X_{\max\{N-2,0\}}. \tag{B2}$$
For a prefix shorter than $J$, its retained actual losses suffice.
:::

Summing the raw estimate along the normalized hierarchy separates three contributions: actual initial losses $\Delta$, a terminal-degree cost $N\tau$, and delayed normalization deficits. The delay matters because a first-crossing argument may use only estimates justified before the crossing. Short prefixes keep their actual losses rather than being silently discarded.

## Restarting and extending finite blocks

:::{prf:lemma} Green control and the actual averaged restart
:label: lem:sz-v2-orbit-green-restart
The following two assertions hold.

**Sequence estimate.**
Fix $K\geq1$. There are $z_0(K)$, $c_0(K)>0$ and $C(K)$ with the
following property. Let integers $m\geq2d\geq4$ and numbers $z\geq z_0$,
$\gamma\geq0$ satisfy $\gamma m^2/z\leq c_0$.
Suppose nonnegative sequences $b_j$ ($j\geq0$), $l_j,D_j$ ($j\geq1$)
obey
$$
 b_0=b_m=1,\quad b_{j+m}\leq b_j,\quad
 b_{j+1}\leq(1+2/z)b_j,\quad l_1\leq2,
$$
and
$$
 D_j\leq z(b_{j+1}-2b_j+b_{j-1})+l_j.
$$
Let $a_s\geq0$ have finite support and satisfy
$\sum_sa_s\leq K/z$, $\sum_ssa_s\leq K/z$.
Let $h_j\geq0$. With $D_j=0$ for $j\leq0$, assume, for $j\geq2$,
$$
 l_j\leq h_j+\sum_{s\geq1}a_sD_{j-s},\qquad
 \sum_{j=2}^{2d-2}j h_j\leq K/z,\qquad
 h_j=\gamma b_{j-d+1}\quad(j\geq2d-1).
$$
Then $1/2\leq b_j\leq2$ for $0\leq j\leq m$, $b_j\leq2$ for
every $j\geq0$, and for $1\leq J\leq m/4$,
$$
 \sum_{k=2}^{J+1}\sum_{j=k}^{m+k-1}l_j\leq C/z+C\gamma Jm.
$$

**Actual restart.** Use $H$, $B=H^{-1}$, $Lf=\mathbb E[Xf]$,
$\mathcal T=P_+\nabla B$ and the finite-family normalized hierarchy
of [](#lem:sz-v2-normalized-hierarchy), for a centered regular log-concave
law of covariance at most $I$ and curvature at least $aI$, $a>0$.
Suppose $z=\|\mathcal T^m\|^{2/m}>0$ and a unit norm-attaining vector
$f$ gives $w_j=z^{-j/2}\mathcal T^jf$, $b_j=\|w_j\|_2^2$,
and $l_j=\|Lw_j\|^2$. Assume
$$
 b_{j+m}\leq b_j,\quad b_0=b_m=1,\quad
 1/2\leq b_j\leq2\ (0\leq j\leq m),\quad b_j\leq2\ (j\geq0),
$$
$$
 \sum_{j=2}^m l_j\leq K/z+K\gamma m,\qquad
 \sum_{k=2}^{J+1}\sum_{j=k}^{m+k-1}l_j\leq K/z+K\gamma Jm
 \quad(1\leq J\leq J_0),
$$
and $\|\operatorname{Sym}(Lw_1)\|^2\leq K/z$.
Here $1\leq J_0\leq m/4$ and $m\geq4$. Let $p\geq3$ be odd,
$\kappa\geq1$, and assume
$$
 {z^{p-2}\over4\kappa}\leq m\leq {4z^{p-2}\over\kappa},
 \qquad J_0\gamma zm\leq1.
$$
There is $C=C(K)$ such that, if $C\kappa z^{-p}\leq1/8$, one
centered unit starting family for the normalized inverse-gradient
hierarchy has energy $\nu$ and actual centering losses satisfying
$$
 \nu\leq{u\over1-C\kappa u^p},\qquad
 P_J\leq C\kappa u^p\quad(1\leq J\leq J_0),\qquad u=z^{-1},
$$
and the same family satisfies for every $N\geq0$
$$
 aV_N+X_N\leq\nu-u+uP_{N+1}.
$$
:::

The discrete Green estimate turns small forcing and controlled orbit defects into bounds on every shifted window. Averaging these windows provides one family with small centering losses. The compensated normalization then gives that family's energy bound. The matched inequality for $aV_N+X_N$ is retained at every later length, so the restart can be used in the next block without changing the family.

:::{prf:lemma} Finite block extension
:label: lem:sz-v2-block-extension
Use the same operators and hierarchy as in [](#lem:sz-v2-orbit-green-restart).
Let $q\geq3$ be odd, $a_q,s_q\geq0$, $C_F,C_\theta\geq1$, $z>0$, $u=z^{-1}$,
$\lambda\geq u/2$, and suppose an
actual centered unit hierarchy starts in direction $B^{1/2}Y$, with
energy $\nu\leq u/(1-a_qu^q)$ and matched budget
$X_M\leq\nu-u+uP_{M+1}$ for every $M$.
Fix $\kappa_q,\kappa_{q-2}\geq1$ and define
$$
 K_q=4(s_q+C_F\kappa_{q-2}+4C_\theta a_q+1),\quad
 p_*=K_qu^q,\quad T_*=\lfloor z^q/\kappa_q\rfloor.
$$
Assume $p_*\leq1/1024$, $a_qu^q\leq1/1024$, $z\geq8C_\theta$,
and the following delayed estimate is valid before, and at, a first
crossing of $p_*$, including all short prefixes:
$$
 P_N\leq s_qu^q+N\tau+{\theta\over\lambda}X_{\max\{N-2,0\}},
 \qquad \tau\leq C_F\kappa_q\kappa_{q-2}u^{2q},\quad
 \theta\leq C_\theta u.
$$
Then $P_N<p_*/2$ for every $N\leq T_*$, and
$$
 \|\mathcal T^m\|^{2/m}\geq z-(a_q+4K_q)z^{1-q}
 \qquad(1\leq m\leq T_*).
$$
:::

Assume that the centering loss first reaches $p_*$. Before that time, the delayed estimate is valid and the matched energy budget controls its normalization term. The resulting bound is below $p_*/2$, a contradiction. Thus the hierarchy retains mass to length $T_*$, and its survival gives a lower bound on every operator power up to that length.

:::{prf:lemma} Propagation from exact finite block norms
:label: lem:sz-v2-block-propagation
Let $T$ be a bounded operator on a Hilbert space (or a compatible
graded family), $R=\|T\|^2$, and integers
$1<m_0<m_1<\cdots<m_s$ satisfy $m_{l+1}\geq4m_l$.
Put $z_l=\|T^{m_l}\|^{2/m_l}>0$. Let $\Delta_l,\eta,\eta_0\geq0$. Suppose
$$
 z_l\leq R,\quad z_l\geq R/2,\quad
 z_{l+1}\geq z_l-\Delta_l,\quad
 \Delta_{l+1}\leq\Delta_l/2,
$$
and $m_{l+1}\Delta_l/z_l\leq\eta$ for every $l<s$.
If $m_0(R-z_s)/z_s\leq\eta_0$, then for all $h\geq0$,
$$
 \|T^h\|\leq z_s^{h/2}
 \exp\left({\eta_0\over2}+2\eta\min\{s,\log_4(h+1)+1\}\right).
$$
:::

Exact norms at a sequence of increasing block lengths control arbitrary powers by decomposing the length among those blocks. Geometric growth of the lengths and geometric decay of the scale losses prevent a cost proportional to the full length. This gives the polynomial propagation needed when the construction returns to the joint-frame estimate.

## Retaining coefficient caps and controlling terminal degrees

:::{prf:proposition} Finite chains of coefficient floors
:label: prop:sz-v2-finite-chain-blocks
Let $G_*:[1,\infty)\to[1,\infty)$ be a fixed universal coefficient seed. Assume it is
nondecreasing, $G_*\geq1$,
$G_*(k)^2\leq C_*k$, and $G_*(R^R)^2\leq R/2$ for all sufficiently
large $R$, with fixed universal constants and a fixed universal threshold.
The constants below can be chosen depending only on this fixed seed.
Let $N\ge1$ be an integer and let $G,H_0,\ldots,H_{N-1}:[1,\infty)\to[1,\infty)$
be nondecreasing valid coefficient majorants with
$1\leq G\leq H_l\leq G_*$ and $c_k\leq G(k)^{k-1}$.
There are positive universal constants $C_{\rm cut},C_{\rm deg},C_X,C_0,C$
with the following property. Fix $0<\epsilon=\alpha_N\leq\alpha_{N-1}\leq\cdots\leq\alpha_0\leq1/16$.
Put
$$
 K_l=\lceil C_{\rm cut}\alpha_l^{-2}\rceil,\quad
 \Xi_l=\lceil4C_{\rm deg}\alpha_l^{-1}K_{l+1}\rceil,
 \quad X=C_XQ^2,
$$
$$
 F^2=\max\{G(X^X)^2,C_0G_*(16K_0)^2,C_0,
              (1+\alpha_l)H_l(\Xi_l)^2:0\leq l<N\},
 \quad H_Q=(1+2\epsilon)F^2.
$$
Here $Q\geq3$ is odd. Use the regular measure class and operators of
[](#def:sz-v2-common-radius). The joint-frame inputs are
[](#lem:sz-v2-raw-joint-frame) and [](#lem:sz-v2-propagated-joint-loss),
and the initial power estimate is [](#lem:sz-v2-mesoscopic-powers).
There is an assignment $Z_Q$ with
$$
 H_Q\leq Z_Q\leq\max\{H_Q,R\},\qquad \mathcal A\leq Z_Q,
$$
and constants $a_Q,s_Q\geq0$ obeying
$$
 a_Q+s_Q+1\leq C(F^2/4)^{Q-3}\leq F^{2Q}.
$$
If $Z_Q>H_Q$, write $z=Z_Q$, $u=z^{-1}$. One actual centered unit
starting family has energy and losses satisfying
$$
 \nu\leq{u\over1-a_Qu^Q},\qquad
 P_J\leq s_Qu^Q\quad(1\leq J\leq J_Q),\qquad
 aV_M+X_M\leq\nu-u+uP_{M+1}\quad(M\geq0),
$$
and
$$
 \|\mathcal T^h\|\leq4(h+1)z^{h/2}\quad(h\geq0),\qquad
 0\leq R-z\leq\min\{1,C/R\},\qquad a_Qu^Q\leq1/8.
$$
For each odd $3\leq p\leq Q$, choose $d_p,e_p$ to be the least dyadic
integers at least $4p,8p$ when $p\leq K_0$. When
$K_l<p\leq K_{l+1}$ choose both to be the least dyadic integer at
least $C_{\rm deg}p/\alpha_l$; when $p>K_N$ use $\epsilon$ instead.
Set $J_p=4e_p$. Constants are independent of $N$, the margins, majorants
and order. The assertion about an actual family is made only above the floor.
:::

The coefficient caps cover separate degree ranges, chosen by the margins $\alpha_l$. Their contributions enter the common floor $F^2$ through a maximum, rather than a sum over all retained caps. Above that floor, repeated restarts and block extensions produce one actual family with the stated energy, centering and propagation bounds. Below the floor, the coefficient-radius estimate is already sufficient; no such family is asserted there. Uniformity in the number of caps is the feature needed by the summable-cost induction.

:::{prf:lemma} Terminal-degree logarithmic distortion
:label: lem:sz-v2-terminal-distortion
Use $t$ and $\ell_r$ from [](#def:sz-v2-height-profiles).
Let $\eta=(e+1)^{-1}$. For $M,x\ge1$ and integer $r\ge1$,
$$
 0\le\ell_r(Mx)-\ell_r(x)
 \le [v\mapsto\log(1+\eta v)]^{\circ(r-1)}(\log M).
                                                               \tag{B22}
$$
For $r\ge1+\log^*M$ the right side is at most
$2\eta^{r-1-\log^*M}$.
Consequently, for fixed $C_T\ge1$, sufficiently large universal $C_b$
and $r_*\ge2$, set $r_Q=\max\{r_*,\lceil C_bt(Q)\rceil\}$.
For odd integers $Q\ge3$, $0<a\le1$, integers $r\ge r_Q$, and
$1\le d<2C_TQ^2(r+1)^2\log(e+a^{-1})$,
$$
 \ell_r(d)\le\zeta_r\ell_{r+1}(a^{-1}),\qquad
 \zeta_r=1+2\eta^{r/2}.                           \tag{B23}
$$
The products $\prod_{r=r_Q}^R(1+r^{-2})^2\zeta_r^2$ have a universal
upper bound, independent of $Q$ and the finite terminal depth $R$.
:::

Each additional logarithm contracts a multiplicative perturbation of the argument. After a number of logarithms comparable to $\log^*M$, the remaining distortion decays geometrically. Applied to the terminal polynomial degree, this compares its logarithms with those of inverse curvature. The products of these distortions and the static-transfer factors stay bounded independently of the terminal depth.

## Scalar control of changing starting depths

:::{prf:lemma} Scalar calculus of the contracted height profiles
:label: lem:sz-v2-profile-calculus
Use the functions of [](#def:sz-v2-height-profiles). The maps
$\bar t,\bar\chi$ are nondecreasing and $1/4$-Lipschitz on $[1,\infty)$.
For every integer $m\geq0$, $W_m\geq4$, $W_m(4)=4$, and $W_m$ is
nondecreasing and $4^{-m-1}$-Lipschitz. For every $x\geq1$ some finite
$m$ satisfies $W_m(x)=4$.
For fixed real $C,p\geq1$ there is $b_{C,p}<\infty$ such that, uniformly
in $m\geq0$ and $x\geq1$,
$$
W_m(Cx^p)\leq W_m(x)+b_{C,p}4^{-m}.
$$
There is a universal $b$ such that for all $x,y\geq1$ and $m\geq0$,
$$
\max\{W_m(xy),W_m(x+y)\}
\leq\max\{W_m(x),W_m(y)\}+b4^{-m}.
$$
There are universal $C_0,D_0,M<\infty$ such that, for $x\geq1$,
$0<\eta\leq1/16$ and every integer $r\geq C_0t(x)+D_0/\eta$,
$$
\mathcal L_r(x)^2\leq e^\eta,\qquad
\mathcal L_r(0)^2\geq e^{-\eta},\qquad
(1+r^{-2})^2\leq e^\eta.
$$
For every integer $r\geq C_0t(x)$, $\mathcal L_r(x)\leq M$.
:::

The averaging in the definition makes each height map Lipschitz. Iterating its contraction reduces perturbations by $4^{-m}$, while fixed powers, products and sums of arguments change the height by only this order. Separately, iterated logarithms approach their positive fixed point, allowing both upper and lower normalization estimates with arbitrarily small multiplicative loss.

:::{prf:lemma} Absorption of growing starting depths
:label: lem:sz-v2-profile-threshold
Use [](#def:sz-v2-height-profiles) and put $\alpha_i=2^{-i}/16$ for
integers $i\geq0$. For every fixed $C,p\geq1$ there is $b_{C,p}<\infty$
such that
$$
W_i(C\alpha_i^{-p})\leq4+b_{C,p}2^{-i}\qquad(i\geq0).
$$
For every fixed $C_R,C\geq1$, set $R_i=\lceil C_R\alpha_i^{-12}\rceil$.
There is $b<\infty$, depending only on $C_R,C$, such that for all
$i\geq0$ and $x\geq1$,
$$
W_i(R_i+\lceil Ct(x)\rceil)\leq W_i(x)+b2^{-i}.
$$
:::

First apply the fixed-power estimate to $C(16\cdot2^i)^p$, then the contraction estimate at $2^i$. This reduces the growing threshold to a summable error of order $2^{-i}$. The sum estimate then absorbs the additional logarithmic starting depth. This is the scalar estimate used in the final choice of parameters for each fixed measure.

