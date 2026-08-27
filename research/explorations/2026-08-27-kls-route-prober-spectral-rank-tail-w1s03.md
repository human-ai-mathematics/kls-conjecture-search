# Route-S probe: rank tails do not control the energy-weighted spectral residue

Date: 2026-08-27

Role: `kls-route-prober`

Concurrency key: `kls-gate:q:mm-spectral-occupation`

Scope: the eigenfunction-oriented Route-S residue only. This report makes no assertion about
`q:upgrade`, `q:stein-weighted`, `q:alignment`, or any implication among those nodes.

Status: the gate is not closed. The new Klartag--Lehec rank inputs give genuine cut-free
information about the eigenvalue profile of the covariance process, but they do not control the
test-dependent tensor energy carried by those ranks. More sharply, at the full-damping endpoint
the requested high-residue estimate is quantitatively equivalent, up to the already-controlled
low block, to the original local-growth estimate for $\mathbb E|g_t|^2$. A one-sided moving
projector does not weaken that target: it sees the mixed block only once, while the residue sees
it twice, and already overspends the coefficient-one damping budget before projector-motion
errors are considered. No numerical evidence is used.

## The gate, verbatim

From `research/kls/gating.md`:

> Prove the universal-time full-damping source estimate uniformly on regular approximants,
> preserving tensor orientation under unwhitening. The source may consume the entire exact
> damping; a strict damping surplus is not required for the KLS bridge.

The exact manuscript target is the following. On every smooth, strongly log-concave, centered
isotropic regular approximant, let
$$
  -Lf=\lambda f,
  \qquad \mathbb E_\mu f=0,
  \qquad \mathbb E_\mu f^2=1
$$
be a first nonconstant eigenfunction, and along the planted localization channel put
$$
  g_t=\operatorname{Cov}_{\mu_t}(f,X),
  \qquad
  H_t=\mathbb E_t[(f-\mathbb E_tf)(X-a_t)^{\otimes2}],
  \qquad
  A_t=\operatorname{Cov}_{\mu_t}(X).
$$
The gate asks for universal $T_0,C_0,C_1>0$ such that, for every $T\le T_0$,
$$
 \mathbb E\int_0^T\|H_t\|_{\mathrm{HS}}^2\,dt
 \le C_0T+C_1\int_0^T\mathbb E|g_t|^2\,dt
 +2\mathbb E\int_0^T g_t^TA_tg_t\,dt. \tag{G}
$$
The coefficient of the last term is exactly one times the full exact damping. It cannot be
increased in an argument that claims to prove the current gate.

This probe tests the proposed high-covariance reduction. Fix $L>1$ and write
$$
 P_t=P_{t,L}=\mathbf 1_{(L,\infty)}(A_t),
 \qquad Q_t=I-P_t,
$$
and
$$
 \mathcal R_{t,L}
 =\|P_tH_tP_t\|_{\mathrm{HS}}^2
  +2\|P_tH_tQ_t\|_{\mathrm{HS}}^2. \tag{1}
$$
The requested intermediate estimate is
$$
 \mathbb E\int_0^T\mathcal R_{t,L}\,dt
 \le C_0T+C_1\int_0^T\mathbb E|g_t|^2\,dt
 +2\alpha\mathbb E\int_0^Tg_t^TP_tA_tP_tg_t\,dt,
 \qquad \alpha\le1. \tag{R}
$$

## Standing of every input

The current control plane has the following exact state.

1. `q:mm-spectral-occupation` is open, has no formal `bounded_by` edge, and is consumed only by
   `prop:spectral-sufficiency`.
2. `prop:spectral-sufficiency` is agent-certified and remains conditional on the open occupation
   node. Its dossier, `solutions/prop-spectral-sufficiency.tex`, proves that coefficient one in
   (G) is sufficient, with explicit constants, and passes a uniform Poincare inequality rather
   than eigenfunctions through regularization.
3. `lem:mm-posterior-defect` is agent-certified in
   `solutions/lem-mm-posterior-defect.tex`. It supplies all posterior eigenfunction identities
   and budgets used below.
4. `lem:mm-time-weighted-fixed-source` is agent-certified in
   `solutions/lem-mm-time-weighted-fixed-source.tex`. At $\kappa=0$ it gives
   $\mathbb E\int_0^\infty t\|H_t\|_{\mathrm{HS}}^2dt\le1$, but expressly gives no
   unweighted initial-layer estimate.
5. `thm:kl-stopped-rank-tail` and `thm:kl-integrated-rank-covariance` are imported from version 2
   of Klartag--Lehec, *Thin-shell bounds via parallel coupling*,
   [arXiv:2507.15495v2](https://arxiv.org/abs/2507.15495). Both are classified
   `preprint-unreviewed` and currently have no consumers.
6. The intrinsic estimate
   $$
     \|A_t^{-1/2}H_tA_t^{-1/2}\|_{\mathrm{HS}}^2
     \le8\operatorname{Var}_{\mu_t}(f) \tag{2}
   $$
   is conditional on the imported unreviewed node `thm:letwin-qcts`. Whenever (2) is used below,
   that conditional standing is explicit.

Thus even a successful proof through the rank inputs would inherit preprint debt. The negative
conclusion of this report is stronger: granting both Klartag--Lehec imports and (2) still does not
produce (R).

## Term-by-term decomposition

Put
$$
 \begin{aligned}
 S_t&=\|H_t\|_{\mathrm{HS}}^2,\\
 B_{t,L}&=\|Q_tH_tQ_t\|_{\mathrm{HS}}^2,\\
 q(t)&=\mathbb E|g_t|^2,\\
 D^P_t&=g_t^TP_tA_tP_tg_t,\\
 D^Q_t&=g_t^TQ_tA_tQ_tg_t.
 \end{aligned} \tag{3}
$$
Because $P_t,Q_t$ are spectral projectors of $A_t$ and $H_t$ is symmetric,
$$
 S_t=B_{t,L}+\mathcal R_{t,L},
 \qquad
 g_t^TA_tg_t=D_t^P+D_t^Q. \tag{4}
$$
Every part of the desired estimate has a distinct role.

- **Low source.** Conditional on (2), the covariance-threshold block extraction gives
  $$
    B_{t,L}\le L^2
    \|A_t^{-1/2}H_tA_t^{-1/2}\|_{\mathrm{HS}}^2
    \le8L^2v_t,
    \qquad v_t=\operatorname{Var}_{\mu_t}(f). \tag{5}
  $$
  Since $\mathbb Ev_t=1-\int_0^tq(s)ds\le1$,
  $$
    \mathbb E\int_0^T B_{t,L}\,dt\le8L^2T. \tag{6}
  $$
  This is the complete controlled low block.
- **High source.** The residue (1) counts every $H_t$ entry incident to the high covariance
  space. A high--low entry occurs twice in the Frobenius norm of the symmetric tensor and must
  therefore occur with coefficient two in (1).
- **High damping.** $2D_t^P$ is the only damping offered in (R). At the accepted endpoint its
  coefficient is exactly one. There is no surplus with which to absorb a positive fraction of
  the source or a projector-motion error.
- **Low damping.** Since $Q_tA_tQ_t\preceq LQ_t$,
  $$
    0\le D_t^Q\le L|g_t|^2. \tag{7}
  $$
  This term may be placed in the lower-order $\int q$ budget, but only once.
- **Boundary.** The fixed-function SDE gives the exact expected energy identity
  $$
    q(T)-|g_0|^2
    =\mathbb E\int_0^T(S_t-2D_t^P-2D_t^Q)\,dt. \tag{8}
  $$
  Isotropy and normalization give $|g_0|^2\le1$, but (G) needs a local increment bound, not
  merely an absolute bound on $q(T)$.
- **Approximation.** All constants must be independent of the approximant's curvature floor.
  The direct posterior cap $A_t\preceq(\varepsilon+t)^{-1}I$ is therefore inadmissible at the
  initial endpoint.

## A proved equivalence: the rank split does not weaken the full-damping gate

No differentiation of $P_t$ is needed for the following exact conclusion.

### Proposition (residue estimate versus local growth)

Fix $L>1$. Suppose the low block satisfies
$$
  \mathbb E\int_0^T B_{t,L}\,dt\le C_LT \tag{9}
$$
for all $T\le T_0$.

If universal $a_0,a_1$ give
$$
 q(T)-|g_0|^2\le a_0T+a_1\int_0^Tq(t)\,dt, \tag{10}
$$
then (R) holds with
$$
  \alpha=1,
  \qquad C_0=a_0,
  \qquad C_1=a_1+2L. \tag{11}
$$
Conversely, if (R) holds with any $\alpha\le1$, then
$$
 q(T)-|g_0|^2
 \le(C_0+C_L)T+C_1\int_0^Tq(t)\,dt. \tag{12}
$$

### Proof

Equations (4) and (8) give the exact identity
$$
 \mathbb E\int_0^T\mathcal R_{t,L}\,dt
 =q(T)-|g_0|^2
 +2\mathbb E\int_0^T(D_t^P+D_t^Q)\,dt
 -\mathbb E\int_0^TB_{t,L}\,dt. \tag{13}
$$
Insert (10), discard the last nonpositive term, and use (7). This proves (11).

In the other direction, solve (8) for the increment of $q$, use $S=B+\mathcal R$, then insert
(R) and (9):
$$
 \begin{aligned}
 q(T)-|g_0|^2
 &\le(C_0+C_L)T+C_1\int_0^Tq(t)\,dt\\
 &\quad+2(\alpha-1)\mathbb E\int_0^TD_t^P\,dt
       -2\mathbb E\int_0^TD_t^Q\,dt.
 \end{aligned}
$$
Both terms on the second line are nonpositive when $\alpha\le1$, proving (12). $\square$

Conditional on (2), one may take $C_L=8L^2$ by (6). Consequently the proposed rank-tail
residue estimate is, up to explicit low-sector constants, equivalent to the original
Gronwall-compatible growth bound for $q$. The spectral split identifies where the difficulty
lives but does not turn it into a weaker statement at the full-damping endpoint.

## What the new rank inputs actually control

Take $L=3$, the threshold in the imported theorem, and let
$$
 a_1(t)\ge\cdots\ge a_n(t)>0
$$
be the ordered eigenvalues of $A_t$. Let
$$
 \sigma_k=\inf\{t>0:a_k(t)\ge3\}.
$$
Klartag--Lehec prove, for every stopping time $\sigma$,
$$
 \sum_{k=1}^n
 \mathbb P(a_k(t\wedge\sigma)\ge3)
 \le Cn e^{-t^{-1/8}}, \tag{14}
$$
and hence
$$
 \mathbb P(\sigma_k\le t)
 \le C\frac nk e^{-t^{-1/8}},
 \qquad
 \mathbb E\sigma_k^{-2}
 \le C\left(1+\log\frac nk\right)^{16}. \tag{15}
$$
They also prove
$$
 \mathbb E\sum_{k=1}^n
 \exp\left(2\int_0^1a_k(t)\,dt\right)\le Cn. \tag{16}
$$
These are rank-sensitive eigenvalue statements. They contain no eigenvector, $f$, $g_t$, or
$H_t$.

To see the exact missing weight, work in an instantaneous eigenbasis of $A_t$ and put
$$
 h_k(t)=\sum_{j=1}^n(H_t)_{kj}^2.
$$
If $r_t=\operatorname{rank}P_t$, then
$$
 \|P_tH_t\|_{\mathrm{HS}}^2=\sum_{k\le r_t}h_k(t),
 \qquad
 \mathcal R_{t,3}\le2\sum_{k\le r_t}h_k(t). \tag{17}
$$
The theorem controls the unweighted count
$\sum_k\mathbf1_{\{k\le r_t\}}$. The source needs the energy-weighted count
$$
 \sum_kh_k(t)\mathbf1_{\{k\le r_t\}}. \tag{18}
$$
There is no repository inequality comparing (18) to the unweighted count with a universal
constant. The weights $h_k(t)$ are random, depend on the same observation path as $A_t$, and can
concentrate in one rank.

The same point is visible in whitened coordinates. With
$\widehat H_t=A_t^{-1/2}H_tA_t^{-1/2}$,
$$
 \mathcal R_{t,3}
 =\sum_{\{i\le r_t\ \mathrm{or}\ j\le r_t\}}
   a_i(t)a_j(t)(\widehat H_t)_{ij}^2. \tag{19}
$$
Estimate (2) controls the total unweighted matrix energy
$\sum_{i,j}(\widehat H_t)_{ij}^2$, while (14)--(16) control the covariance eigenvalue profile.
Neither controls their joint coupling in (19).

### The marginal-probability attempt fails before integration

The crudest consequence of (2) and posterior Brascamp--Lieb is
$$
 \mathcal R_{t,3}
 \le8v_ta_1(t)^2\mathbf1_{\{a_1(t)>3\}}
 \le8t^{-2}v_t\mathbf1_{\{a_1(t)>3\}}. \tag{20}
$$
The rank tail bounds $\mathbb P(a_1(t)>3)$, not
$\mathbb E[v_t\mathbf1_{\{a_1(t)>3\}}]$. Conditional variance is nonnegative and decreases only
in expectation; it is not pathwise bounded by its initial value. Thus multiplying (14) by the
mean bound $\mathbb Ev_t\le1$ would be an invalid independence step.

Even under the fictitious extra bound $v_t\le1$, (14) would give only
$$
 \mathbb E\int_0^T\mathcal R_{t,3}\,dt
 \lesssim
 \int_0^Tt^{-2}\min\{1,Cne^{-t^{-1/8}}\}\,dt
 \lesssim(1+\log n)^8. \tag{21}
$$
Indeed the substitution $u=t^{-1/8}$ turns $t^{-2}dt$ into $8u^7du$, and the transition occurs
at $u\asymp\log n$. Hence the marginal rank tail would retain a polylogarithmic loss even after
granting a false pathwise variance cap.

### Rank entrance plus the time-weighted budget also fails

Since high rank $k$ can occur only after $\sigma_k$, one might try to deweight the certified
estimate $\mathbb E\int tS_tdt\le1$. In the worst rank-one orientation this requires control of
an expression of the form
$$
 \mathbb E\left[
   \sigma_1^{-1}\int_0^TtS_t\,dt
 \right]. \tag{22}
$$
The source budget controls only the expectation of the second factor. The rank theorem controls
negative moments of the first factor, with
$\mathbb E\sigma_1^{-2}\lesssim(1+\log n)^{16}$. It gives no joint moment and no conditional
source budget at rank entrance. Even a hypothetical pathwise bound on the second factor would
leave order $(\log n)^8$ after Cauchy--Schwarz.

Restarting the weighted lemma at $\sigma_1$ does not fix this. Conditional on
$\mathcal F_{\sigma_1}$, the right side is the random posterior variance
$v_{\sigma_1}$ (minus a nonnegative term); deweighting again asks for
$\mathbb E[v_{\sigma_1}/\sigma_1]$. Nonnegative-supermartingale optional sampling controls
$\mathbb Ev_{\sigma_1}$, not this product.

The integrated exponential estimate (16) has the same limitation. It is a sum over unweighted
ranks. A source tensor concentrated in the top current rank sees the largest exponential term,
for which (16) permits an $n$-sized expectation and a logarithmic integrated eigenvalue. A
dimension-free conclusion would require deterministic or independent averaging of the tensor
energy across ranks. No such averaging is known, and rank-one product eigenfunctions show that
stable-rank spreading cannot be imposed universally.

## The frozen-projector coefficient obstruction

Before treating motion, freeze a spectral projection $P$ commuting with a fixed covariance path
and put $Q=I-P$. The projected fixed-function equation is
$$
 d(Pg_t)=PH_t\,dW_t-PA_tPg_t\,dt,
$$
and hence
$$
 \mathbb E\int_0^T\|PH_t\|_{\mathrm{HS}}^2dt
 =\mathbb E|Pg_T|^2-|Pg_0|^2
  +2\mathbb E\int_0^Tg_t^TPA_tPg_t\,dt. \tag{23}
$$
But
$$
 \|PH_t\|_{\mathrm{HS}}^2
 =\|PH_tP\|_{\mathrm{HS}}^2+\|PH_tQ\|_{\mathrm{HS}}^2, \tag{24}
$$
whereas
$$
 \mathcal R_{t,L}
 =\|PH_tP\|_{\mathrm{HS}}^2+2\|PH_tQ\|_{\mathrm{HS}}^2. \tag{25}
$$
Thus the one-sided projected energy sees the mixed block only once. The generic inequality
$\mathcal R_{t,L}\le2\|PH_t\|_{\mathrm{HS}}^2$ inserted in (23) produces
$4\int D_t^Pdt$, which corresponds to $\alpha=2$, not $\alpha\le1$. This failure occurs with a
constant projector, with no eigenvalue crossing, third-moment term, or approximation issue.

The missing copy of the mixed block is the source of the complementary energy $|Qg_t|^2$:
$$
 \|QH_t\|_{\mathrm{HS}}^2
 =\|QH_tQ\|_{\mathrm{HS}}^2+\|QH_tP\|_{\mathrm{HS}}^2.
$$
Adding the $P$ and $Q$ energy identities counts the mixed block correctly, but it also restores
the full terminal increment $q(T)-|g_0|^2$ and gives exactly (13). All projector information has
then cancelled. This is another proof of the equivalence proposition above.

There is no scalar quadratic energy $g^TWg$ that directly produces (25): if a diagonal weight is
$1$ on the high space and $0$ on the low space, a high--high entry receives the correct weight
but a high--low pair receives total row weight one rather than two. Giving the low row weight one
fixes the mixed block but incorrectly charges the low--low block. The residue is genuinely a
two-index incidence functional, while the damping acts on the one-index state $g_t$.

## Moving projectors: the exact error ledger

A hard projector is not an Ito test at a threshold crossing. The rigorous smooth replacement
makes the missing terms explicit. Let $\chi\in C^2([0,\infty))$, put
$$
 F_t=\chi(A_t),
$$
and choose $\chi=0$ below a lower buffer and $\chi=1$ on $(L,\infty)$. Write the covariance SDE
as
$$
 dA_t=\sum_{k=1}^n\mathcal T_{t,k}\,dW_{t,k}-A_t^2dt, \tag{26}
$$
where
$$
 \mathcal T_{t,k}
 =\mathbb E_t[(X_k-a_{t,k})(X-a_t)^{\otimes2}].
$$
Define the Frechet-derivative terms
$$
 U_{t,k}=D\chi(A_t)[\mathcal T_{t,k}], \tag{27}
$$
and
$$
 V_t=D\chi(A_t)[-A_t^2]
 +\frac12\sum_{k=1}^n
 D^2\chi(A_t)[\mathcal T_{t,k},\mathcal T_{t,k}]. \tag{28}
$$
Matrix Ito calculus and the cross-variation between $F_t$ and $g_t$ give, for
$z_t=F_tg_t$,
$$
 \begin{aligned}
 dz_t
 &=\sum_k\bigl(F_tH_te_k+U_{t,k}g_t\bigr)dW_{t,k}\\
 &\quad+left(
   -F_tA_tg_t+V_tg_t+
   \sum_kU_{t,k}H_te_k
 \right)dt. 
 \end{aligned} \tag{29}
$$
Consequently the finite-variation part of $d|z_t|^2$ is
$$
 \begin{aligned}
 &\|F_tH_t\|_{\mathrm{HS}}^2
 -2g_t^TF_t^2A_tg_t\\
 &\quad+sum_k|U_{t,k}g_t|^2
 +2\sum_k\langle F_tH_te_k,U_{t,k}g_t\rangle\\
 &\quad+2g_t^TF_tV_tg_t
 +2\sum_kg_t^TF_tU_{t,k}H_te_k.
 \end{aligned} \tag{30}
$$
The first line is the desired one-sided source and exact damping. Every term in the remaining
two lines is a moving-projector error.

The Klartag--Lehec proof applies Daleckii--Krein calculus to the unitarily invariant scalar
potential $\operatorname{Tr}\varphi(A_t)$. In that scalar trace, the Ito curvature is a sum of
squared covariance third moments with divided-difference coefficients, and Guan's tensor bound
controls the complete sum. Formula (30) is different. It contains the test-dependent
contractions
$$
 \sum_k|U_{t,k}g_t|^2,
 \qquad
 \sum_kg_t^T(U_{t,k}F_t+F_tU_{t,k})H_te_k,
 \qquad
 g_t^TF_tV_tg_t. \tag{31}
$$
Neither imported rank theorem bounds (31). The scalar trace estimates contain no $g_t$ or
$H_t$, supply no sign for the mixed contractions, and do not preserve the coefficient-one
damping budget.

Young's inequality is not a harmless repair. Absorbing any positive fraction
$\eta\|F_tH_t\|_{\mathrm{HS}}^2$ of the $H$--third-moment cross terms leaves
$(1-\eta)$ times the source but still only the original $2g_t^TF_t^2A_tg_t$ damping. Dividing by
$1-\eta$ makes the damping coefficient strictly larger than one. In addition, the factor-two
mixed-block loss in (25) is already present before this absorption.

There are two equivalent rigorous ways to see the boundary problem.

1. If the transition band has width $\delta$, then
   $\|D\chi\|=O(\delta^{-1})$ and
   $\|D^2\chi\|=O(\delta^{-2})$. No available estimate makes the terms in (31) uniformly
   integrable as $\delta\downarrow0$.
2. On an interval where the spectrum has a gap around $L$, the Riesz projector is smooth and,
   in an eigenbasis,
   $$
     (DP_A[E])_{ij}
     =\frac{p_i-p_j}{a_i-a_j}E_{ij}. \tag{32}
   $$
   Stopping before the gap closes bounds the denominator, but produces the same cross-block
   third-moment contractions. At the band boundary one must control repeated crossings or
   spectral local time. The first-entrance bounds (14)--(15) control neither.

Using both complementary smooth energies can cancel all projector-motion terms, because their
sum is $|g_t|^2$. It simultaneously cancels all benefit of the projector and returns (8). Thus
projector motion is not the only obstruction, but no rigorous treatment of it presently closes
the coefficient budget either.

## The exact eigenfunction identities do not supply the missing joint estimate

The certified posterior-defect calculus writes
$$
 \lambda g_t=b_t+u_t,
 \qquad
 \lambda H_t=2\operatorname{sym}C_t+K_t, \tag{33}
$$
with
$$
 \mathbb E\int_0^T\|C_t\|_{\mathrm{HS}}^2dt
 \le\lambda-\lambda^2|g_0|^2, \tag{34}
$$
and
$$
 \mathbb E\operatorname{Var}_t(R_t^{\mathrm{def}})
 =t\lambda-\lambda^2\int_0^tq(s)ds. \tag{35}
$$
Conditional on `thm:letwin-qcts`, the defect tensor obeys
$$
 \mathbb E\|A_t^{-1/2}K_tA_t^{-1/2}\|_{\mathrm{HS}}^2
 \le8\left(t\lambda-\lambda^2\int_0^tq(s)ds\right). \tag{36}
$$
The initial eigenfunction also has the fixed energies
$$
 \mathbb E|\nabla f|^2=\lambda,
 \qquad
 \mathbb E\|\nabla^2f\|_{\mathrm{HS}}^2\le\lambda^2,
$$
and consequently
$$
 \mathbb E\mathbb E_t|\nabla R_t^{\mathrm{def}}|^2
 \le t\lambda^2+t^2\lambda. \tag{37}
$$

These estimates are sharp in the intrinsic metric but fail at the same unwhitening step.

- Dividing (34) by $\lambda^2$ after using (33) costs $O(1/\lambda)$ in the small-gap branch.
- Crude unwhitening of (36) with $A_t\preceq t^{-1}I$ gives a $K_t$ contribution of order
  $\lambda/t$ before division by $\lambda^2$; its time integral diverges at zero and its final
  scale has the wrong power of $\lambda$.
- Multiplying (36) by the marginal rank-entry probability is invalid because the defect energy
  and the covariance event are generated by the same posterior.
- Estimate (37) returns (35) through posterior Poincare/Brascamp--Lieb. No available asymmetric
  quadratic covariance theorem converts it into Euclidean high-incidence control with one
  covariance factor and the required orientation.

Thus the eigenfunction equation identifies the two pieces of $H_t$, but neither piece has an
energy-weighted rank-entrance estimate.

The time-weighted fixed-function lemma also contains no hidden local-growth estimate. Combining
its $\kappa=0$ inequality with (8) gives exactly
$$
 Tq(T)+\int_0^Tq(t)dt\le1. \tag{38}
$$
This is the posterior terminal covariance cap in integrated form. It permits $q(T)$ to become
order one at arbitrarily small $T$ and therefore does not imply (10).

### A scale-consistent budget model

The limitation can be seen without claiming a log-concave counterexample. On a short terminal
window at time $t\asymp\varepsilon$ of length $\varepsilon^2$, consider the sizes
$$
 a_1\asymp\varepsilon^{-1},
 \qquad
 H_{11}\asymp\varepsilon^{-1},
 \qquad
 \lambda\asymp\varepsilon,
 \qquad
 g_1\text{ rising from }0\text{ to order }1. \tag{39}
$$
Then the unweighted source spent in the window is order one, while its time-weighted cost and
the accumulated damping are only order $\varepsilon$. The whitened tensor has order-one size.
Taking $C=0$ and $K=\lambda H$ gives $K_{11}\asymp1$ and
$A^{-1/2}KA^{-1/2}\asymp\varepsilon$, whose squared size matches the
$t\lambda\asymp\varepsilon^2$ defect budget. Likewise $u=\lambda g$ is compatible with the
intrinsic vector defect bound. Equation (38) is also respected.

This is not asserted to arise from an actual log-concave localization path and therefore is not
a refutation of (G). It is an inequality-level non-implication: all currently certified scalar
eigenfunction budgets permit an order-one source burst on the natural $a_1^{-2}$ time scale,
whereas (R) would allow only $O(\varepsilon)$. Excluding precisely this joint burst requires new
orientation-sensitive dynamics. The two marginal rank imports do not exclude its scales either:
for dimensions with $n\gtrsim\exp(\varepsilon^{-1/8})$, (14) permits one entered rank with
order-one probability at time $\varepsilon$, while a rank of size $\varepsilon^{-1}$ lasting
$\varepsilon^2$ contributes only $O(\varepsilon)$ to its integrated eigenvalue in (16).

## Gaussian, product, and anisotropic calibrations

### Gaussian

For $\mu=N(0,I)$ and a first eigenfunction $f(x)=u\cdot x$,
$$
 A_t=(1+t)^{-1}I,
 \qquad H_t=0.
$$
For every $L>1$, $P_t=0$ and $\mathcal R_{t,L}=0$. More generally, a Gaussian first
eigenfunction is linear even in anisotropic coordinates, so covariance anisotropy alone does not
create spectral source. Any proof that charges Gaussian covariance eigenvalues without the
$H_t$ incidence is necessarily wasteful.

### Products and spectators

Let $\mu=\nu^{\otimes n}$ in a regular product setting and suppose the bottom eigenspace is
spanned by factor eigenfunctions $f_i$. For
$$
 f=\sum_{i=1}^n\theta_if_i,
 \qquad \sum_i\theta_i^2=1,
$$
the planted localization factorizes pathwise and
$$
 A_t=\operatorname{diag}(a_i(t)),
 \qquad
 (g_t)_i=\theta_i g_i(t),
 \qquad
 (H_t)_{ij}=0\ (i\ne j),
 \qquad
 (H_t)_{ii}=\theta_i h_i(t). \tag{40}
$$
Hence
$$
 \mathcal R_{t,L}
 =\sum_i\theta_i^2h_i(t)^2\mathbf1_{\{a_i(t)>L\}}. \tag{41}
$$
For identical factors the coefficients $\theta_i^2$ average the identically distributed
coordinate paths, so the expectation in (41) has no multiplicity loss. In contrast, the
unweighted rank count in (14) sums all spectator spikes and carries the factor $n$.

This calibration identifies what a successful theorem must retain: the fixed function's energy
weights, not merely the rank of the inflated covariance space. A large covariance in a factor
with $\theta_i=0$ contributes nothing. Products also show that the source tensor may be rank one,
so no universal stable-rank hypothesis can be inserted to average the rank tail.

The one-sided-exponential product behind `prop:covariance-spike` makes the warning concrete. At
Gaussian-noise scale $s=1/t$, one of $n$ spectator coordinates has covariance of order $1/t$ with
universal probability near $t\asymp1/\log n$, even though the product satisfies KLS. A fixed
factor eigenfunction does not follow the maximizing spectator. The missing general theorem would
have to express this nonadaptivity without assuming product structure or independence.

### Static anisotropic orientation

At a fixed matrix state, take
$$
 A=\operatorname{diag}(M,1,\ldots,1),
 \qquad M>L.
$$
Two whitened rank-one tensors of the same Hilbert--Schmidt norm can be placed respectively in
the first and second coordinate. After unwhitening, the first has high residue of order $M^2$
and the second has residue zero. The covariance eigenvalues, high rank, and intrinsic tensor norm
are identical. This is only an algebraic calibration, not a posterior counterexample, but it
proves that eigenvalue-profile information cannot determine (19) without a relative-orientation
input.

The truncated-exponential first-eigenfunction calculations in the archive provide a second
warning: relevant eigenfunction residuals can be asymptotically rank one. Effective rank and
first-eigenspace multiplicity therefore cannot be treated as a generic source of gain.

## The precise irreducible gate

Granting all imported inputs, the first unsupported statement is a **joint, energy-weighted rank
entrance/rotation estimate**. One equivalent form is the local growth inequality (10). A more
geometric form would have to control, with universal constants, the random measure
$$
 \sum_{i,j}
 a_i(t)a_j(t)(\widehat H_t)_{ij}^2
 \mathbf1_{\{a_i(t)>3\ \mathrm{or}\ a_j(t)>3\}}\,dt \tag{42}
$$
against $T$, $\int q$, and at most the full high damping. It must remain valid when the tensor
energy has rank one, must ignore independent spectator spikes, and must include the mixed block
with coefficient two.

The Klartag--Lehec results control the marginal rank process underneath (42), but not the random
energy weights or their rotation. The certified eigenfunction identities control intrinsic
energy, but not its coupling to that rank process. Neither family supplies the missing joint
Carleson estimate.

## Residue

1. **Needs new idea — energy-weighted rank entrance.** Prove a joint estimate for (42), or
   equivalently the local growth bound (10), which distinguishes a fixed eigenfunction from an
   adaptively chosen top covariance direction. Marginal entrance probabilities are insufficient.
2. **Fenced — mixed-block coefficient.** A one-sided projected $g$ energy counts
   $P_tH_tQ_t$ once; the tensor residue counts it twice. The factor-two repair forces
   $\alpha\ge2$ even for a frozen projector, beyond the accepted full-damping budget.
3. **Fenced — moving-projector errors.** A smooth or resolvent projector creates the terms (31).
   Current scalar rank potentials do not control their test-dependent signs or complete
   contractions. Young absorption overspends coefficient one; hard limits additionally require
   transition-band or spectral-local-time control.
4. **Needs new idea — defect unwhitening.** The $C_t$ budget loses $1/\lambda$ after (33), and the
   intrinsic $K_t$ budget loses covariance factors. A new asymmetric quadratic covariance
   theorem would have to retain the high-space orientation and the exact damping coefficient.
5. **Technical gap — import and approximation interface.** Both rank inputs are unreviewed
   preprint imports and are stated first for compactly supported isotropic laws. Even after a
   joint estimate is found, its stopping, smoothing, isotropization, and curvature-floor
   uniformity must be audited. This is downstream of the analytic failure above, not its cause.

There is no route-fatal log-concave counterexample. The conclusion is that the currently imported
rank information does not discharge, or genuinely weaken, the Route-S gate.

## Fence-by-fence evasion check

The live node has no formal `bounded_by` edge. Every registered fence was nevertheless checked.

- `obs:two-tail`: no cut, slice, or absolute-scale excess estimate is used. The analogous
  anisotropy lesson is respected by keeping the full tensor incidence (42).
- `obs:proj-ceiling`: no quadratic-chaos theorem is inferred from radial or projection-only
  tests. The low block uses the full symmetric-matrix input (2), conditionally on its actual
  preprint standing. The failure of rank-only information is recorded rather than promoted.
- `obs:crude-insufficient`: no crude covariance integral $\Xi_T$ is used to bootstrap the gate.
- `obs:relative-ceiling`: no all-measure relative covariance occupation bound is inserted as a
  supposedly weaker premise.
- `obs:circularity`: no localized isoperimetric profile or changing competitor family occurs.
- `obs:rank-one-refuted`: that obstruction concerns fixed product cuts. This report makes no cut
  assertion; rank-one eigenfunction tensors are used only as a calibration against an unjustified
  stable-rank assumption.
- `prop:covariance-spike`: the product calculation explicitly respects spectator spikes and shows
  why a global $\|A_t\|_{\mathrm{op}}$ route is too strong.
- The truncated-exponential Stein-unweighting shortcut is not used. Its archived model analysis
  is cited only for the permitted rank-one calibration.

This probe does not compare, transfer, or assert equivalence with any member of the trace-upgrade
cluster.

## Route viability and proposed gate update

Route S remains viable, but the new rank imports do not move its logical gate. Their useful role
is diagnostic: they say that covariance inflation has a controlled rank profile, so the missing
theorem must be an energy-weighted refinement that uses the fixed eigenfunction. They do not
supply that refinement.

Proposed one-line gate update for the orchestrator:

> At $L=3$, prove the local growth bound
> $q(T)-|g_0|^2\le C_0T+C_1\int_0^Tq$ (equivalently, up to the certified low block, the
> coefficient-one high-residue estimate), by a joint energy-weighted rank
> entrance/rotation theorem for $H_t$; unweighted Klartag--Lehec rank tails, one-sided projector
> energies that count the mixed block once, and uncontrolled $D\chi,D^2\chi$ errors are
> inadmissible.

## Proposed ledger delta

None. The proposition above is a proved structural equivalence inside this exploration, but it
does not discharge a premise, certify a new solution, or justify wiring either preprint import to
the live gate. If the orchestrator wants it promoted as a named internal lemma, it should first
receive a standalone dossier and independent review; no status or certification metadata is
proposed here.

## Numerical handoff

None. The obstruction is a lack of a universal joint analytic estimate, and no actual
log-concave refuting family with a fixed threshold was obtained. The registered `kls-align`
diagnostic concerns a designated cut family and cannot certify or refute the eigenfunction tensor
statement (42). No private computation was performed.

```yaml
outcome: blocked
artifacts:
  - research/explorations/2026-08-27-kls-route-prober-spectral-rank-tail-w1s03.md
proposed_deltas:
  - none; do not wire the Klartag--Lehec rank imports to q:mm-spectral-occupation
next_role: orchestrator
next_prompt: |
  Keep q:mm-spectral-occupation open and do not add dependency edges from the two imported
  Klartag--Lehec rank nodes. If updating the Route-S gate text, use the proposed one-line update
  verbatim: the coefficient-one high-residue estimate is quantitatively equivalent, up to the
  controlled low block, to local growth of q(T)=E|g_T|^2. Any next analytic owner must target a
  joint energy-weighted rank entrance/rotation estimate for the fixed eigenfunction tensor,
  including the mixed block with coefficient two. It may not infer source occupation from
  unweighted rank probabilities, use a one-sided projector bound that forces alpha>=2, or hide
  the Dchi/D2chi third-moment contractions in a hard-projector limit. Treat both Klartag--Lehec
  nodes and Letwin QCTS with their current preprint-unreviewed standing, preserve the trace-cluster
  ownership separation, and make no numerical request without a fixed analytic diagnostic.
```
