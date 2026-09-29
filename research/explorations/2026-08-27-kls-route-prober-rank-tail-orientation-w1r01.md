---
---
# KLS route probe: rank tails versus source orientation

Date: 2026-08-27

Role: `kls-route-prober`

Concurrency key: singleton trace-upgrade-cluster ownership for this wave

Primary target: `q:upgrade`

Comparison scope: only the high-rank residues of `q:stein-weighted` and `q:alignment`, under
the single-owner rule of `CLAUDE.md` constraint 6.  No equivalence among the three nodes is
asserted.

Artifact ownership: this file only.  No ledger, manuscript, route-control, bibliography,
solution, review, knowledge, or numerical file is changed.

## Outcome

The Klartag--Lehec rank-indexed stopping scheme gives a real new input to `q:upgrade`, but it
does not close the gate.  Conditional on the intrinsic quadratic-chaos estimate, it improves
the worst-oriented incident-high occupation from the naive order-$n$ trace budget to
$O((1+\log n)^8)$.  More importantly, it gives a dimension-free **interval-density** bound if
the whitened cut tensor has stable rank comparable to $n$ at every relevant slice.  That premise
cannot follow from a universal pointwise slice theorem: the certified anisotropic two-tail
configuration has stable rank one, is perfectly aligned with the unique inflated covariance
direction, and has zero instantaneous Riccati damping.  This static example does not rule out a
trajectory-specific replacement using the localization coupling.

The sharp surviving gate is temporal orientation, not eigenvalue counting.  For a fixed soft
spectral cutoff $F_t=\chi(A_t)$, the exact potential

$$
Y_t=\operatorname{Tr}(F_tR_t),\qquad R_t=A_t-B_t,
$$

has all favorable Riccati signs.  Its drift contains the desired high-row $G_t$ source with
coefficient one.  After the favorable terms are discarded, the entire upper bound is the sum
of:

1. the oriented interval decrement of the boundary value $Y_t$;
2. a cutoff-curvature contraction of the covariance third-moment tensor with $R_t$; and
3. the quadratic-covariation contraction between covariance motion and the cut-dependent
   martingale part of $R_t$.

For a hard projector these become divided-difference/eigenvector-motion and threshold-local-time
terms.  Neither imported Klartag--Lehec theorem controls any of them.  Their results are
unitarily invariant statements about the ordered covariance eigenvalues; they contain no
cut tensor, no within-color matrix, and no transported eigenspace.  This is a precise
irreducible orientation gate, rather than a missing manipulation of the rank tails.

## Gates, quoted verbatim

The primary gate from `research/kls/gating.md` is:

> Produce a uniform absorptive trace estimate that directly discharges
> `ass:all-cut-carleson`, with every source and damping term matched to
> `thm:scalar-riccati`. The estimate must use cut-aware information and handle small-time
> high-rank occupation.

The comparison gate for `q:stein-weighted` is:

> Supply the exact weighted input required by `ass:weighted-package`: a
> localization-uniform almost-stability trace theorem modulo Jacobi zero modes, with explicit
> domains, boundary conventions, and controlled Reilly terms.

The comparison gate for `q:alignment` is:

> Give either a uniform analytic incident-high bound for fixed balanced product cuts or a
> certified counterexample. A finite tail-union diagnostic is not a universal conclusion.

The exact ledger target consumed by `q:upgrade` is the all-cut interval estimate

$$
\mathbb E\int_{I\cap[0,\tau]}S_t\,dt
\le C_0|I|+C_1\mathbb E\int_{I\cap[0,\tau]}r_t\,dt
+\alpha\mathbb E\int_{I\cap[0,\tau]}D_t\,dt,
\qquad \alpha<1,
\tag{AC}
$$

for every interval $I\subset[0,T_0]$, every fixed balanced cut, and the coarse balance exit
$\tau$.  The strict deficit $1-\alpha$ is load-bearing.

## Provenance and source audit

The read-only literature handoff produced no separate artifact.  The source-checked repository
imports are:

- `thm:kl-stopped-rank-tail`, corresponding to Proposition 5.1 and Corollary 6.1 of
  Klartag--Lehec, *Thin-shell bounds via parallel coupling*,
  [arXiv:2507.15495v2](https://arxiv.org/abs/2507.15495v2);
- `thm:kl-integrated-rank-covariance`, corresponding to Theorem 6.2 of the same version.

The source is version 2 dated 23 February 2026 and remains an unreviewed preprint import.  The
exact repository statements, rather than any stronger reconstruction, are used below.  They
apply to simplified stochastic localization of an isotropic compactly supported log-concave
law.

The archived attempts read for this comparison include:

- `2026-08-27-kls-route-prober-upgrade-par-01.md`;
- `2026-08-27-synthesizer-kls-first-wave-par-04.md`;
- `2026-08-20-kls-eigenfunction-localization.md`;
- `2026-08-20-kls-tail-union-asymptotics.md`;
- `2026-08-20-kls-program-cycle-1.md`; and
- the frontier and R2 audit records cited by those files.

The old numerical observations are not used.  In particular, no finite product diagnostic is
treated as evidence for or against a universal gate.

## Exact cut normalization and the previously isolated residue

On the balanced window, write

$$
Z_t^K=\sqrt{s_t}\,A_t^{-1/2}K_tA_t^{-1/2},
\qquad
X_t^K=\sqrt{s_t}\,K_t=A_t^{1/2}Z_t^KA_t^{1/2}.
\tag{1}
$$

For a threshold $L>1$, let

$$
P_{t,L}=\mathbf 1_{(L,\infty)}(A_t),
\qquad Q_{t,L}=I-P_{t,L},
\tag{2}
$$

and define the complete incident-high energy

$$
\mathcal H^K_{t,L}
=\|P_{t,L}X_t^KP_{t,L}\|_{\mathrm{HS}}^2
+2\|P_{t,L}X_t^KQ_{t,L}\|_{\mathrm{HS}}^2.
\tag{3}
$$

The factor two retains both high--low matrix entries.  Orthogonality of the matrix blocks gives

$$
\|X_t^K\|_{\mathrm{HS}}^2
=\|Q_{t,L}X_t^KQ_{t,L}\|_{\mathrm{HS}}^2+\mathcal H^K_{t,L}.
\tag{4}
$$

Conditional on the imported Letwin quadratic-chaos theorem, the certified two-color duality
gives

$$
\|Z_t^K\|_{\mathrm{HS}}^2\le 8,
\qquad
\|Q_{t,L}X_t^KQ_{t,L}\|_{\mathrm{HS}}^2\le 8L^2.
\tag{5}
$$

On the coarse window $p_t\in[1/3,2/3]$, the earlier probe established the pointwise conversion

$$
S_t=s_t\|G_t\|_{\mathrm{HS}}^2
\le 3\|X_t^K\|_{\mathrm{HS}}^2+\frac34D_t.
\tag{6}
$$

At the Klartag--Lehec threshold $L=3$, equations (4)--(6) become

$$
S_t\le216+3\mathcal H^K_{t,3}+\frac34D_t.
\tag{7}
$$

Consequently the exact original target is

$$
\mathbb E\int_{I\cap[0,\tau]}\mathcal H^K_{t,3}\,dt
\le C_H|I|+C_r\mathbb E\int_{I\cap[0,\tau]}r_t\,dt
+\beta\mathbb E\int_{I\cap[0,\tau]}D_t\,dt,
\qquad \beta<\frac1{12}.
\tag{8}
$$

Indeed, (7)--(8) give (AC) with damping coefficient $3/4+3\beta<1$.  Every calculation below
is measured against this budget.

## What the Klartag--Lehec rank scheme actually supplies

Write $\lambda_1(t)\ge\cdots\ge\lambda_n(t)$ for the ordered eigenvalues of $A_t$ and

$$
\sigma_k=\inf\{t>0:\lambda_k(t)\ge3\}.
$$

The imported stopped theorem says, for every stopping time $\sigma$ and $t>0$,

$$
\sum_{i=1}^n
\mathbb P\bigl(\lambda_i(t\wedge\sigma)\ge3\bigr)
\le C_{\mathrm{KL}}n e^{-t^{-1/8}}.
\tag{9}
$$

It implies

$$
\mathbb P(\sigma_k\le t)
\le C_{\mathrm{KL}}\frac nk e^{-t^{-1/8}},
\qquad
\mathbb E\sigma_k^{-2}
\le C_{\mathrm{KL}}\left(1+\log\frac nk\right)^{16}.
\tag{10}
$$

Taking $\sigma=\tau$ in (9) gives the following genuine one-way consequence for the cut-stopped
window:

$$
\mathbb E\left[
\mathbf1_{\{t<\tau\}}\operatorname{rank}P_{t,3}
\right]
\le C_{\mathrm{KL}}n e^{-t^{-1/8}}.
\tag{11}
$$

The integrated theorem gives

$$
\mathbb E\sum_{i=1}^n
\exp\left(2\int_0^1\lambda_i(t)\,dt\right)
\le C'_{\mathrm{KL}}n.
\tag{12}
$$

The proof in the source first controls the entrance times, uses the Brascamp--Lieb cap
$\lambda_k(t)\le t^{-1}$ after entrance, and then sums the rank profile
$(1+\log(n/k))^{16}$.  Proposition 4.6 in that paper controls a noncommutative product integral
by the **ordered eigenvalue integrals** through a von Neumann majorization argument.  Thus (12)
is robust to eigenvector rotation, but precisely because it discards the transported
eigenvectors.  The index $k$ labels order at each time; it is not a Lagrangian direction.

Neither (9) nor (12) contains $K_t$, $G_t$, $R_t$, a cut, or a spectral projector.  They control
how many covariance eigenvalues are large and for how long, but not which matrix entries of
$Z_t^K$ occupy them.

## First extraction: a polylogarithmic worst-orientation bound

The imported estimates do improve the naive trace bound.  The improvement is not enough for
(8), but it identifies exactly how much is lost by arbitrary orientation.

### Lemma 1 (worst-oriented consequence of the imports)

On the compactly supported domain of `thm:kl-stopped-rank-tail`, conditional on (5), for every
stopping time $\tau$ and $T\le1$,

$$
\mathbb E\int_0^{T\wedge\tau}\mathcal H^K_{t,3}\,dt
\le C\bigl(1+\log(en)\bigr)^8.
\tag{13}
$$

The same right side bounds the integral over every subinterval, but it is an additive lump, not
the required $C|I|$ density.

#### Proof

If $P_{t,3}=0$, then $\mathcal H^K_{t,3}=0$.  Otherwise, by (1), (5), and the
Brascamp--Lieb cap,

$$
\mathcal H^K_{t,3}
\le\|X_t^K\|_{\mathrm{HS}}^2
\le\lambda_1(t)^2\|Z_t^K\|_{\mathrm{HS}}^2
\le8t^{-2}.
$$

On $\{t<\tau\}$, the event $P_{t,3}\ne0$ is contained in
$\{\lambda_1(t\wedge\tau)\ge3\}$.  Hence (9) gives

$$
\mathbb E\left[\mathbf1_{\{t<\tau\}}\mathcal H^K_{t,3}\right]
\le8t^{-2}\min\{1,C_{\mathrm{KL}}n e^{-t^{-1/8}}\}.
\tag{14}
$$

Set $a_n=\max\{1,\log(C_{\mathrm{KL}}n)\}$ and $t_n=a_n^{-8}$.  Above $t_n$, integrating the
first term in the minimum costs at most $t_n^{-1}=a_n^8$.  Below $t_n$, the substitution
$u=t^{-1/8}$ gives

$$
C_{\mathrm{KL}}n\int_0^{t_n}t^{-2}e^{-t^{-1/8}}\,dt
=8C_{\mathrm{KL}}n\int_{a_n}^{\infty}u^7e^{-u}\,du
\le C(1+a_n^7),
$$

because the last incomplete gamma tail is
$7!e^{-a_n}\sum_{j=0}^7a_n^j/j!$.  This proves (13).  Equivalently, (10) gives
$\mathbb E\sigma_1^{-1}\le C(1+\log(en))^8$ and the same scale. $\square$

Inserted into (7), this yields only

$$
\mathbb E\int_0^{T\wedge\tau}S_t\,dt
\le216T+C(1+\log(en))^8
+\frac34\mathbb E\int_0^{T\wedge\tau}D_t\,dt.
\tag{15}
$$

This is strictly better than $O(n)$, but it neither has a dimension-free constant nor an
interval density.  It does not advance the logical status of `q:upgrade`.

## Second extraction: what pointwise effective rank would buy

The rank profile in (9) is average-summable.  One direct way it closes the source is when the cut
tensor is sufficiently spread across covariance ranks.

For a nonzero symmetric matrix $Z$, write

$$
r_{\mathrm{st}}(Z)=\frac{\|Z\|_{\mathrm{HS}}^2}{\|Z\|_{\mathrm{op}}^2}.
$$

### Lemma 2 (rank-delocalized sufficient estimate)

Assume, in addition to (5), that on $\{t<\tau\}\cap[0,1]$, whenever
$P_{t,3}\ne0$ and $Z_t^K\ne0$,

$$
r_{\mathrm{st}}(Z_t^K)\ge\rho
\tag{16}
$$

Then every interval $I\subset[0,1]$ satisfies

$$
\mathbb E\int_{I\cap[0,\tau]}\mathcal H^K_{t,3}\,dt
\le C\left(1+\frac n\rho\right)|I|.
\tag{17}
$$

In particular, the additional pointwise premise $r_{\mathrm{st}}(Z_t^K)\ge c n$ gives (8)
with $C_r=0$ and $\beta=0$, and therefore closes `q:upgrade` conditional on its imported
inputs.

#### Proof

Work in an eigenbasis of $A_t$ and write $Z_t^K=(z_{ij})$.  Let
$w_i=\sum_jz_{ij}^2=|Z_t^Ke_i|^2$.  Symmetry and $2\lambda_i\lambda_j\le
\lambda_i^2+\lambda_j^2$ give

$$
\mathcal H^K_{t,3}
\le72+\sum_{i:\lambda_i(t)>3}\lambda_i(t)^2w_i.
\tag{18}
$$

Indeed, the high--high entries are charged to their two high row weights; in a high--low entry,
the low eigenvalue is at most $3$, and the resulting low part is at most
$9\|Z_t^K\|_{\mathrm{HS}}^2\le72$.  From (5) and (16),

$$
w_i\le\|Z_t^K\|_{\mathrm{op}}^2
\le\frac{\|Z_t^K\|_{\mathrm{HS}}^2}{\rho}
\le\frac8\rho.
$$

On $\{t<\tau\}$, $\lambda_i(t)\le t^{-1}$, so (9) with stopping time $\tau$ yields

$$
\begin{aligned}
\mathbb E\left[\mathbf1_{\{t<\tau\}}\mathcal H^K_{t,3}\right]
&\le72+\frac8\rho t^{-2}
\sum_{i=1}^n\mathbb P\bigl(\lambda_i(t\wedge\tau)\ge3\bigr)\\
&\le72+8C_{\mathrm{KL}}\frac n\rho
t^{-2}e^{-t^{-1/8}}.
\end{aligned}
\tag{19}
$$

The scalar function $t^{-2}e^{-t^{-1/8}}$ is uniformly bounded on $(0,1]$ (under
$u=t^{-1/8}$ it is $u^{16}e^{-u}$).  Integrating (19) over $I$ proves (17). $\square$

Within this row-weight argument, Lemma 2 is the full effective-rank gain available from the
stopped tail without an additional correlation theorem.  A stable rank $\rho=o(n)$ still leaves
$n/\rho$; merely asking for a polylogarithmic stable rank does not remove the dimension.  The
rank-average

$$
\frac1n\sum_{k=1}^n\left(1+\log\frac nk\right)^8=O(1)
$$

explains the threshold $\rho\asymp n$.

## Adversarial audit of pointwise effective-rank ideas

The premise (16) cannot be justified by a universal pointwise theorem for arbitrary
log-concave slices and cuts.  For $\Lambda>3$, the example below supplies a static orientation
obstruction in the active high block.  Whether an aligned high slice of this form is reached
along an isotropic localization path is a separate dynamical question; no counterexample to such
a trajectory-specific statement is claimed here.

### Certified slice obstruction

In `prop:two-tail`, for

$$
A=\operatorname{diag}(\Lambda,1,\ldots,1),
\qquad
E=\{|x_1|\ge a\sqrt\Lambda\},
$$

one has $p=q=1/2$, $\delta=0$, $r=D=0$, and

$$
K=G=8a\varphi(a)\Lambda e_1e_1^T.
$$

Therefore

$$
Z^K=4a\varphi(a)e_1e_1^T,
\qquad
r_{\mathrm{st}}(Z^K)=1,
\qquad
\mathcal H^K_{3}=16a^2\varphi(a)^2\Lambda^2
$$

when $\Lambda>3$.  The intrinsic bound is satisfied with room to spare, the high covariance
rank is one, and the full tensor energy is aligned with that rank.  Consequently each of the
following pointwise assertions is false:

- $\mathcal H^K_{t,3}\lesssim\operatorname{rank}P_{t,3}$;
- a dimension-free lower bound on $r_{\mathrm{st}}(Z_t^K)$;
- a $1/\operatorname{rank}P_{t,3}$ sharing of the intrinsic energy; or
- absorption of the aligned slice by $r_t$ or $D_t$.

This is a slice obstruction, not a stochastic-localization counterexample.  The certified
`cor:refutation` proves that a fixed one-coordinate product cut self-extinguishes in total time.
The correct lesson is that low effective rank must be treated **temporally**; it cannot be
excluded pointwise.

### Eigenvalue-only separation model

There is also a deterministic separation showing why (12) does not control the two-covariance
source weight.  This is an information-content countermodel, not a claimed localization path.

For sufficiently large $n$, let $a_n=\log(C_{\mathrm{KL}}n)$ and
$\varepsilon_n=a_n^{-8}$.  Construct a continuous
positive-semidefinite path with $A_0=I$, all but one eigenvalue rapidly decreasing below one, and
one eigenvalue which:

- stays below $3$ until time $\varepsilon_n$;
- rises to $h_n=(4\varepsilon_n)^{-1}$;
- remains there for a time comparable to $\varepsilon_n$; and
- falls before time $4\varepsilon_n$.

The path may be chosen under the cap $A_t\preceq t^{-1}I$.  It has high rank at most one.  Before
$\varepsilon_n$ the stopped-rank left side is zero, while after $\varepsilon_n$ its value is at
most one and

$$
C_{\mathrm{KL}}n e^{-t^{-1/8}}\ge1.
$$

Thus its eigenvalue data obey the numerical conclusion (9), including after deterministic
stopping.  Its top eigenvalue has $\int_0^1\lambda_1(t)\,dt=O(1)$, so after making the harmless
low-eigenvalue integrals sufficiently small it also obeys an estimate of the form (12), with
any fixed slack in the universal constant.  But with $Z_t^K$ rank one and aligned with the top
eigenspace,

$$
\int_0^1\mathcal H^K_{t,3}\,dt
\gtrsim \varepsilon_nh_n^2
\asymp \varepsilon_n^{-1}
=\bigl(\log(C_{\mathrm{KL}}n)\bigr)^8.
\tag{20}
$$

The $L^1$ eigenvalue integral in (12) cannot control the $L^2$ covariance weight forced by the
Euclidean source.  Any spectral scalar potential that dominates (3) must, on a rank-one aligned
tensor, dominate $\lambda_1^2\|Z^K\|_{\mathrm{HS}}^2$ and therefore inherits this separation.
A weight weak enough to use only $\int\lambda_1$ no longer dominates the Riccati source.

Along dimensions for which $n\ge m$, one may further subdivide the high plateau into
$m\asymp\varepsilon_n^{-1}$ pieces and rotate the rank-one eigenspace and $Z_t^K$ through $m$
orthogonal directions.  Each direction then receives source occupation at most a universal
constant while the trace occupation is $\asymp m$.  The eigenvalue data are unchanged.  (In
smaller dimensions the same construction uses $\min\{n,m\}$ directions.)  This abstract variant
shows why combining rank tails with fixed-direction budgets still needs a theorem controlling
the **motion or selection** of the source direction.  It does not impose the full coupled
covariance/two-color SDE and therefore is not a refutation of `q:upgrade`; that missing coupling
is exactly what the next potential exposes.

## The exact moving-projector Riccati potential

The rank-one branch suggests tracking the high covariance space dynamically.  A hard projector
is avoidable at first: fix once and for all a nondecreasing $C^2$ function
$\chi:\mathbb R\to[0,1]$ such that

$$
\chi(x)=0\quad(x\le3),
\qquad
\chi(x)=1\quad(x\ge4),
$$

and set $F_t=\chi(A_t)$.  Moving the soft transition above the imported threshold $3$ is useful:
every nonzero divided difference then touches an eigenvalue $>3$, while the entire block below
$4$ can still be paid by the intrinsic low-block estimate.  Write the two matrix SDEs as

$$
dA_t=\sum_k\Theta_{t,k}\,dW_{t,k}-A_t^2\,dt,
$$

$$
dR_t=\sum_k\Gamma_{t,k}\,dW_{t,k}
-\bigl(R_t^2+s_tG_t^2\bigr)\,dt,
\qquad R_t=A_t-B_t\succeq0.
\tag{21}
$$

Here $\Theta_{t,k}$ is the covariance third-moment matrix and $\Gamma_{t,k}$ is the
cut-dependent martingale coefficient of the within-color covariance.  It is not an independent
black box.  If $e_k$ is the $k$th Brownian coordinate, $\alpha_t=q_t-p_t$, and
$v_t=s_t\delta_t$, direct differentiation of $B_t=v_tv_t^T/s_t$ gives

$$
\Gamma_{t,k}
=\Theta_{t,k}
-s_t\left((K_te_k)\delta_t^T+\delta_t(K_te_k)^T\right)
+\alpha_t(\delta_t)_kB_t.
\tag{21a}
$$

Thus the cross variation below contains a pure covariance-motion square, a third-moment--cut
tensor contraction, and a third-moment--centroid contraction.  Define

$$
Y_t=\operatorname{Tr}(F_tR_t)\ge0.
\tag{22}
$$

### Lemma 3 (exact soft-projector identity)

On the compact regularized process, after the usual bounded martingale stopping, every interval
$I=[a,b]$ satisfies

$$
\begin{aligned}
&\mathbb E\int_{I\cap[0,\tau]}
s_t\operatorname{Tr}(F_tG_t^2)\,dt\\
&=\mathbb E\bigl[Y_{a\wedge\tau}-Y_{b\wedge\tau}\bigr]
-\mathbb E\int_{I\cap[0,\tau]}\operatorname{Tr}(F_tR_t^2)\,dt\\
&\quad
-\mathbb E\int_{I\cap[0,\tau]}
\operatorname{Tr}\bigl(A_t^2\chi'(A_t)R_t\bigr)\,dt\\
&\quad
+\frac12\mathbb E\int_{I\cap[0,\tau]}
\sum_k\operatorname{Tr}\left(
D^2\chi(A_t)[\Theta_{t,k},\Theta_{t,k}]R_t
\right)\,dt\\
&\quad
+\mathbb E\int_{I\cap[0,\tau]}
\sum_k\operatorname{Tr}\left(
D\chi(A_t)[\Theta_{t,k}]\Gamma_{t,k}
\right)\,dt.
\end{aligned}
\tag{23}
$$

#### Proof

Matrix Itô calculus gives

$$
dF_t=\sum_kD\chi(A_t)[\Theta_{t,k}]\,dW_{t,k}
+D\chi(A_t)[-A_t^2]dt
+\frac12\sum_kD^2\chi(A_t)[\Theta_{t,k},\Theta_{t,k}]dt.
$$

Apply the product rule to $\operatorname{Tr}(F_tR_t)$.  The quadratic covariation of the two
martingale parts is the last line of (23).  Since $-A_t^2$ commutes with $A_t$,

$$
D\chi(A_t)[-A_t^2]=-A_t^2\chi'(A_t).
$$

Insert (21), integrate the stopped identity, and take expectations. $\square$

The two middle terms in (23) are favorable: $F_t,R_t\succeq0$ implies
$\operatorname{Tr}(F_tR_t^2)\ge0$, while monotonicity of $\chi$ makes
$A_t^2\chi'(A_t)\succeq0$ and hence
$\operatorname{Tr}(A_t^2\chi'(A_t)R_t)\ge0$.  Moreover $A_0=I$ gives $F_0=0$ and $Y_0=0$.
Thus on intervals starting at zero the exact Riccati potential creates the desired high-row
source with **zero damping expenditure**, except for the two projector-motion terms.  On a
general interval, the signed decrement $Y_a-Y_b$ is an additional local boundary term; an
upper bound that estimates it separately must control its positive part.

### Exact sufficient injection gate

Let

$$
\begin{aligned}
\mathfrak J_\chi(I)
&=\mathbb E[Y_{a\wedge\tau}-Y_{b\wedge\tau}]\\
&\quad+\frac12\mathbb E\int_{I\cap[0,\tau]}
\sum_k\operatorname{Tr}\left(
D^2\chi(A_t)[\Theta_{t,k},\Theta_{t,k}]R_t
\right)dt\\
&\quad+\mathbb E\int_{I\cap[0,\tau]}
\sum_k\operatorname{Tr}\left(
D\chi(A_t)[\Theta_{t,k}]\Gamma_{t,k}
\right)dt.
\end{aligned}
\tag{24}
$$

Equation (23) shows that

$$
\mathbb E\int_{I\cap[0,\tau]}
s_t\operatorname{Tr}(F_tG_t^2)dt
\le\mathfrak J_\chi(I).
\tag{25}
$$

There is also an exact alternative reduction to (AC).  Put $P=P_{t,4}$ and $Q=I-P$.  Since
$F_t\succeq P$,

$$
s_t\left(\|PG_tP\|_{\mathrm{HS}}^2
+2\|PG_tQ\|_{\mathrm{HS}}^2\right)
\le2s_t\operatorname{Tr}(F_tG_t^2).
\tag{26}
$$

For the low block, use $G=K-(q-p)\delta\delta^T$, Young's inequality with parameter $2$,
$|q-p|^2/s\le1/2$, and $r_t^2\le D_t$ to obtain

$$
s_t\|QG_tQ\|_{\mathrm{HS}}^2
\le384+\frac34D_t.
\tag{27}
$$

Here the intrinsic contribution is
$3s_t\|QK_tQ\|_{\mathrm{HS}}^2\le3\cdot8\cdot4^2=384$; the rank-one centroid
correction contributes at most $(3/2)(|q-p|^2/s)r_t^2\le3D_t/4$.

Combining (25)--(27), the estimate

$$
\mathfrak J_\chi(I)
\le C_\chi|I|+C_r\mathbb E\int_{I\cap[0,\tau]}r_tdt
+\gamma\mathbb E\int_{I\cap[0,\tau]}D_tdt,
\qquad \gamma<\frac18,
\tag{28}
$$

would imply (AC) with damping coefficient $3/4+2\gamma<1$.  This is a rigorous sufficient
reduction with the exact damping threshold and its dependence on the fixed cutoff displayed.  It
is not a proof of (28).

Equation (28) is the irreducible orientation gate exposed by this wave.  The imported rank tails
do not control any term in $\mathfrak J_\chi(I)$ at the required scale:

- $Y_t=\operatorname{Tr}(\chi(A_t)R_t)$ depends on the orientation of the within-color matrix
  relative to the high covariance space, and its positive interval decrement is not controlled
  by the rank of that space;
- the $D^2\chi$ term is a complete Brownian-coordinate third-moment contraction multiplied by
  the random cut matrix $R_t$;
- after (21a) is inserted, the $D\chi$ term contains
  $\sum_k\operatorname{Tr}(D\chi(A)[\Theta_k]\Theta_k)$ together with contractions against
  $K$, $\delta$, and $B$; and
- neither term is present in (9), (10), or (12).

The Letwin third-moment input controls a fixed directional contraction of the whitened third
tensor.  It does not control the complete sum above after multiplication by $R_t$ or
$\Gamma_t$.  Bounding those contractions by global operator norms reinstates the covariance
spike and the trace/projection losses already fenced in the repository.

### Subtracting the cut-free spectral injection does not repair the budget

There is one natural cancellation to test.  Put

$$
\Psi_\chi(A)=\operatorname{Tr}(A\chi(A)),
\qquad
Z_t=\operatorname{Tr}(F_tB_t).
$$

Then $Y_t-\Psi_\chi(A_t)=-Z_t$.  The two cut-free pieces

$$
\frac12\sum_k\operatorname{Tr}\left(
D^2\chi(A)[\Theta_k,\Theta_k]A\right)
+\sum_k\operatorname{Tr}\left(D\chi(A)[\Theta_k]\Theta_k\right)
$$

are exactly the Itô correction of $\Psi_\chi(A)$.  Hence subtracting this scalar spectral
potential cancels the pure covariance injection algebraically.  It does not yield an upper
potential with a favorable endpoint.  To see the precise price, write

$$
\mathcal N_{t,k}
=s_t\left((K_te_k)\delta_t^T+\delta_t(K_te_k)^T\right)
-\alpha_t(\delta_t)_kB_t,
$$

so that $\Gamma_{t,k}=\Theta_{t,k}-\mathcal N_{t,k}$.  A direct product rule for
$Z_t=\operatorname{Tr}(F_tB_t)$ gives

$$
\begin{aligned}
\mathbb E\int_{I\cap[0,\tau]}s_t\operatorname{Tr}(F_tG_t^2)dt
&=\mathbb E[Z_{b\wedge\tau}-Z_{a\wedge\tau}]\\
&\quad+2\mathbb E\int_{I\cap[0,\tau]}\operatorname{Tr}(A_tF_tB_t)dt
-\mathbb E\int_{I\cap[0,\tau]}r_t\operatorname{Tr}(F_tB_t)dt\\
&\quad+\mathbb E\int_{I\cap[0,\tau]}
\operatorname{Tr}(A_t^2\chi'(A_t)B_t)dt\\
&\quad-\frac12\mathbb E\int_{I\cap[0,\tau]}\sum_k
\operatorname{Tr}\left(D^2\chi(A_t)[\Theta_{t,k},\Theta_{t,k}]B_t\right)dt\\
&\quad-\mathbb E\int_{I\cap[0,\tau]}\sum_k
\operatorname{Tr}\left(D\chi(A_t)[\Theta_{t,k}]\mathcal N_{t,k}\right)dt.
\end{aligned}
\tag{28a}
$$

The immediate unconditional comparison for the new deterministic term is

$$
2\operatorname{Tr}(AFB)
\le2\operatorname{Tr}(AB)
=D+r^2
\le2D.
\tag{28b}
$$

This available estimate spends twice the full scalar damping, whereas (AC) requires a coefficient
strictly below one; no strict-budget refinement follows from the repository inputs.  The
transition term obeys
$\operatorname{Tr}(A^2\chi'(A)B)\le16\|\chi'\|_\infty r$ and is admissible as an $r$-term, but
(28a) also has a positive terminal increment $Z_b-Z_a$ and retains the two cut-dependent
contractions.  Thus the obvious spectral renormalization trades the cut-free motion term for a
wrong-sign endpoint and a nonabsorptive damping estimate; it does not evade the orientation
gate.

### Hard projectors and local time

The fixed-width soft cutoff shows that local time is not the only obstruction: one may avoid it
and still be left with (24).  If one nevertheless sends the transition width to zero in order to
differentiate the exact $P_{t,4}$, then

$$
D\chi(A)[H]_{ij}=\chi^{[1]}(\lambda_i,\lambda_j)H_{ij}
$$

develops inverse-gap divided differences across the threshold, $D^2\chi$ develops their second
order analogues, and the diagonal eigenvalue terms converge to threshold local times.  At
eigenvalue collisions the moving basis itself is not differentiable without a cluster/gap
construction.  Klartag--Lehec control the number of eigenvalues above $3$; they give no
threshold local-time, eigenvalue-gap, or eigenspace-rotation estimate.  Thus a hard cutoff adds
real terms and supplies no shortcut.

## Frozen-projector stopping: a second dead end

At an entrance time $\sigma_k$, one can freeze the then-current high eigenspace
$P_{\sigma_k}$ and use the matrix Riccati equation conditionally after $\sigma_k$.  For that
fixed random projector, the per-direction argument gives a future source budget paid by
$\operatorname{Tr}(P_{\sigma_k}R_{\sigma_k})$.  This does not control the contemporaneous
$P_{t,3}$:

1. rank entrance times see a new eigenvalue crossing $3$, not rotation of the already-high
   eigenspace;
2. a rank-one high eigenspace may sweep through many directions without any new $\sigma_k$;
3. repeatedly freezing projectors pays the same changing subspace from a trace-scale initial
   budget; and
4. comparing the frozen and moving projectors is exactly a gap/motion estimate of the type in
   (24).

Thus optional stopping does not turn a rank tail into a cut-aware Carleson embedding.

## Product alignment audit

For the product node `q:alignment`, $A_t$ is diagonal in the fixed coordinate basis.  This
removes eigenvector rotation, but not source selection.  With threshold $3$ (the bounded band
$[2,3]$ can be assigned to the intrinsic low block), the imported theorem gives only

$$
\sum_i\mathbb P(A_t^{(i)}\ge3)\le Cn e^{-t^{-1/8}}.
\tag{29}
$$

The certified coordinate budgets give

$$
\mathbb E\int_0^\infty s_t|G_te_i|^2dt\le1
\qquad\text{for each fixed }i.
\tag{30}
$$

What `q:alignment` needs is the joint, source-weighted statement

$$
\sum_i\mathbb E\int_{I\cap[0,\tau]}
\mathbf1_{\{A_t^{(i)}\ge3\}}s_t|G_te_i|^2dt
\lesssim |I|+\int_I\mathbb E r_tdt+\alpha\int_I\mathbb E D_tdt,
\tag{31}
$$

with the high--low entries counted twice and $\alpha<1$.  Marginal rarity (29) and total budget
(30) do not imply (31): the coordinate budget may be spent precisely on its rare high event.
An $L^1$ budget has no interpolation with an event probability without a higher conditional
moment or a reverse-Carleson estimate.

The product structure makes (31) more approachable than the all-measure motion gate: the
eigenvectors are fixed and the threshold motion is scalar.  It remains strictly narrower.
The fixed-coordinate result `cor:refutation` handles one coordinate in total time, while an
arbitrary balanced cut may select among unboundedly many independently inflating coordinates.
No implication from (29) to (31) is established.

A proof of the full all-cut estimate (AC) would imply the displayed `q:alignment` bound simply
because $S_t^H\le S_t$ and products are a subclass.  The reverse implication is impossible on
scope alone.  This is a proved one-way logical containment, not an equivalence and not a status
change.

## Boundary/Stein high-rank audit

At the algebraic source level, `q:stein-weighted` uses exactly the same cut tensor:

$$
\frac{\mathcal S_{\mu_t}(E)}{s_t}=s_t\|K_t\|_{\mathrm{HS}}^2
=\|X_t^K\|_{\mathrm{HS}}^2.
\tag{32}
$$

Thus (4)--(5) split its ambient quadratic data into a bounded covariance block and the same
$\mathcal H^K_{t,L}$.  A direct estimate (8) would, on the tighter window, supply the **numerical
Stein-trace inequality** with a damping coefficient below $1/2$ and no excess term.  It would
not prove the node as presently worded: no Jacobi almost-stability theorem, zero-mode
projection, Reilly boundary convention, or support/corner term follows from (8).

Conversely, the boundary representation writes each matrix test as

$$
\ell_{\mu_t,E}(M)
=-\int_{\partial^*E}\partial_nu_M\,d\sigma_{\mu_t}.
$$

The high covariance projector acts on the ambient quadratic-data matrix $M$.  The geometric
decomposition acts on scalar boundary functions $\partial_nu_M$ through the Jacobi operator.
No repository theorem intertwines these two spectral decompositions.  In particular:

- covariance rank does not count Jacobi zero modes;
- the Klartag--Lehec eigenvalue process does not see $H_{\mu_t}$, $II$, $L_\Sigma$, or
  support-boundary terms in Reilly's formula;
- the mixed Reilly term $2u_NL_\Sigma u$ has no sign supplied by a covariance tail; and
- a fixed cut transported under localization is not automatically a critical or stable
  surface.

Therefore the rank imports do not give even a one-way implication to the boundary
almost-stability statement.  The common object is the numerical Stein tensor (32), not an
identified boundary high-rank mode.  A proof of the boundary statement is restricted to
near-Cheeger cuts and cannot imply the all-cut gate or the product all-cut node in reverse.

## Directional implication audit

Only the following directions have been established at the level stated here:

1. `thm:kl-stopped-rank-tail` + intrinsic (5) $\Rightarrow$ the dimension-dependent bound
   (13).
2. The same inputs + the explicit pointwise premise
   $r_{\mathrm{st}}(Z_t^K)\ge cn$ $\Rightarrow$ the dimension-free incident estimate (17)
   with damping coefficient zero.
3. The projector-injection estimate (28) $\Rightarrow$ `ass:all-cut-carleson`, conditional on
   the intrinsic low block, with exact damping coefficient $3/4+2\gamma<1$.
4. `ass:all-cut-carleson` $\Rightarrow$ the product incident-high conclusion of
   `q:alignment`, by restriction and $S_t^H\le S_t$.
5. An incident-$K$ estimate of the strength (8) $\Rightarrow$ the numerical Stein-trace
   component of `ass:weighted-package` on the tighter window; it does not imply the geometric
   theorem demanded by `q:stein-weighted` or the weighted-excess component.

No reverse direction is proved.  In particular, no relation among `q:upgrade`, the high-rank
boundary mechanism of `q:stein-weighted`, and `q:alignment` is proposed as an equivalence.

## Exact residue

- **Needs new idea — source-weighted rank tail.**  Replace the eigenvalue count (11) by a
  cut-weighted estimate for the row energies of $Z_t^K$, or prove an equivalent bound on the
  projector injection $\mathfrak J_\chi(I)$.  This is the first unsupported mathematical step.
- **Fenced — pointwise effective rank.**  Lemma 2 closes only under stable rank $\Omega(n)$;
  `prop:two-tail` gives admissible rank-one aligned slices with $r=D=0$.
- **Needs new idea — low-rank temporal motion.**  Once the high-stable-rank branch is removed by
  Lemma 2, the residue is control of a few adapted source directions as they rotate through or
  are selected by the inflated covariance space.  Fixed-direction Carleson budgets do not
  apply to those adapted directions.
- **Fenced — smooth projector injection.**  The two complete contractions in (24) are not
  controlled by the imported rank tails or fixed-direction third-moment estimates.  A global
  operator-norm estimate recreates the covariance-spike loss.
- **Technical gap plus new idea — hard threshold.**  An exact hard projector additionally needs
  threshold local-time and eigenvalue-gap control.  A fixed soft transition avoids this
  technical layer but leaves the genuine cross-variation gate unchanged.
- **Needs new idea — interval locality.**  Even a total estimate from $Y_0=0$ is insufficient
  for (AC).  The positive part of the decrement $Y_a-Y_b$ must have a Carleson density on every
  subinterval, unless it is cancelled directly by the two motion terms in (24).
- **Needs new idea — product conditional embedding.**  For `q:alignment`, combine (29) and (30)
  through a cut-aware conditional moment estimate; marginal rank rarity is not enough.
- **Needs new idea — boundary intertwining.**  For `q:stein-weighted`, identify how ambient
  covariance-high quadratic data map into Jacobi mean-zero/zero-mode sectors and control every
  Reilly term.  No such map is supplied by rank-indexed covariance technology.
- **Technical/epistemic gap.**  Both Klartag--Lehec results and the Letwin intrinsic estimate are
  unreviewed preprint imports.  Any consumer remains conditional on those imports and must keep
  the compact-support/regularization domain explicit.

## Fence-by-fence evasion check

### `obs:proj-ceiling`

The low block uses the full symmetric-matrix quadratic-chaos input, not projection tests.  The
high block is retained entry by entry.  The failed attempt is explicitly identified: replacing
the row weights by eigenvalue counts without a source-delocalization theorem is another
projection/rank-only argument and cannot close the trace.

### `obs:two-tail`

No slice-wise high-state bound is asserted.  The certified two-tail configuration is used to
refute the pointwise effective-rank premise and to show why damping cannot absorb an aligned
slice.  The proposed gate (28) is dynamic and cut-aware.

### `obs:relative-ceiling`

No all-measure bound on $\Xi_T$ or on relative covariance occupation is inserted.  Both (8) and
(28) retain the fixed cut through $K_t$, $R_t$, and $\Gamma_t$.

### `obs:rank-one-refuted`

The two-tail slice and the deterministic separation model are not claimed as product dynamic
counterexamples.  The certified self-extinguishing theorem is respected.  The surviving product
question is explicitly the many-coordinate conditional embedding (31).

### Remaining catalogued fences

No crude $\Xi_T\lesssim\log n$ bootstrap is used (`obs:crude-insufficient`), and no localized
isoperimetric-profile lower bound or moving competitor is inserted (`obs:circularity`).  The
boundary comparison does not assume almost-stability of the transported cut.

## Route viability and proposed gate update

The all-cut route remains viable.  The imported rank theorem now closes one branch exactly:
source tensors delocalized across a linear fraction of covariance ranks have a dimension-free
incident-high density.  The remaining branch consists of low- or intermediate-stable-rank
source tensors whose adapted directions may align with, move through, or be selected by the
covariance eigenspaces.  The soft-projector identity (23) isolates the complete price of that
adaptation and shows that the deterministic covariance drift and matrix Riccati terms have
favorable signs.

Proposed one-line update for the orchestrator:

> At threshold $3$, Klartag--Lehec rank tails plus intrinsic QCTS give the required incident
> density whenever $r_{\mathrm{st}}(Z_t^K)\gtrsim n$, but rank-one two-tail slices rule out a
> universal pointwise derivation of that premise.  Close the low-rank branch by proving the
> soft-projector injection estimate for one fixed cutoff $\chi=0$ on $(-\infty,3]$ and
> $\chi=1$ on $[4,\infty)$,
> $\mathfrak J_\chi(I)\le C_0|I|+C_1\int_I\mathbb E r_t+
> \gamma\int_I\mathbb E D_t$ with $\gamma<1/8$; the exact identity then gives
> `ass:all-cut-carleson` with damping $3/4+2\gamma<1$.  Eigenvalue rank tails alone do not control
> the curvature, cross-variation, or interval-boundary terms in $\mathfrak J_\chi$.

## Numerical disposition

No `finum` run is proposed.  The obstruction is an analytic information mismatch between
eigenvalue-only tails and a source-weighted cross variation.  No fixed finite observable with a
universal refuting threshold would decide (28), and the registered product diagnostic cannot
certify the all-measure gate.

## Proposed ledger delta

None.  Lemmas 1--3 and the sufficient implication (28) are new analytic reductions in a probe,
not certified dossiers.  They warrant no status, dependency, solution, review, or cross-route
edge.  If the orchestrator wants them promoted as formal nodes, their exact compact-support and
preprint-conditional hypotheses must first be accepted, followed by a standalone prover and a
distinct cold proof-checker.

```yaml
outcome: blocked
artifacts:
  - research/explorations/2026-08-27-kls-route-prober-rank-tail-orientation-w1r01.md
proposed_deltas:
  - no ledger, manuscript, bibliography, route-control, or status delta
  - consider replacing the q:upgrade gate text by the proposed one-line soft-projector injection target after independent review of Lemmas 1--3
next_role: orchestrator
next_prompt: |
  Read the rank-tail orientation probe and preserve singleton ownership of the trace-upgrade
  cluster.  Do not add an equivalence among q:upgrade, q:stein-weighted, and q:alignment.  The
  imported rank tails yield only the conditional dimension-dependent bound (13), while the
  stable-rank branch (17) requires a false universal pointwise premise.  If promoting the new
  reduction, first accept a candidate lemma statement for the exact soft-projector identity
  (23) and the sufficient injection estimate (28), with compact-support and imported-input
  provenance explicit; then dispatch one prover and a distinct cold proof-checker.  Until that
  review, make no status or dependency change.  The next mathematical attack should target the
  cut-dependent cross variation in (24), including interval-boundary control, rather than
  another eigenvalue tail or effective-rank count.
```
