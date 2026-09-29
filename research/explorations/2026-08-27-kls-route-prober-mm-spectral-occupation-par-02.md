---
---
# Route-S probe: posterior defect and the surviving high-incidence block

Date: 2026-08-27

Role: `kls-route-prober`

Concurrency key: `kls-gate:q:mm-spectral-occupation`

Status: the gate is not closed. This probe proves an exact posterior-eigenfunction defect
calculus and extracts the entire low-covariance part of the source, but the high-covariance
incident tensor still has no absorptive estimate. No numerical evidence is used.

## The gate, verbatim

From `research/kls/gating.md`:

> Prove the universal-time absorptive source/damping estimate uniformly on regular approximants,
> preserving tensor orientation under unwhitening.

The effective manuscript statement is Question `q:mm-spectral-occupation`. On a smooth,
strongly log-concave, isotropic approximant, let
$$
-Lf=\lambda f,\qquad \mathbb E_\mu f=0,\qquad \mathbb E_\mu f^2=1,
$$
where $f$ is a first nonconstant eigenfunction, and along stochastic localization put
$$
g_t=\operatorname{Cov}_{\mu_t}(f,X),\qquad
H_t=\mathbb E_t[(f-\mathbb E_tf)(X-a_t)^{\otimes2}],\qquad
A_t=\operatorname{Cov}_{\mu_t}(X).
$$
The demanded estimate is that universal $T_0,C_0,C_1>0$ and $\alpha<1$ satisfy, for every
$t\le T_0$,
$$
\mathbb E\int_0^t\|H_s\|_{\mathrm{HS}}^2\,ds
\le C_0t+C_1\mathbb E\int_0^t|g_s|^2\,ds
+\alpha\mathbb E\int_0^t2g_s^TA_sg_s\,ds. \tag{G}
$$
The constants, including $T_0$ and the strict deficit $1-\alpha$, must be independent of the
dimension, the approximant, and its strong-convexity parameter.

## Live graph and provenance audit

`python3 research/check_ledger.py node q:mm-spectral-occupation` reports an open question with
no `depends_on`, no `bounded_by`, and no ledger consumers. The adjacent
`prop:spectral-sufficiency` names it in prose but is itself open. Thus there is no certified
dependency closure to inherit.

The present attack uses the following inputs with their actual repository standing.

1. The fixed-function identities
   $$
   dg_t=H_t\,dW_t-A_tg_t\,dt,
   \qquad
   d|g_t|^2=dM_t+(\|H_t\|_{\mathrm{HS}}^2-2g_t^TA_tg_t)dt
   \tag{1}
   $$
   are derived in `research/explorations/2026-08-20-kls-eigenfunction-localization.md` and stated
   in `modules/kls/30-spectral-route.tex`. They have no standalone spectral dossier or
   certifying review.
2. Conditional on imported node `thm:letwin-qcts` (Letwin, version-1 unreviewed preprint),
   Hilbert--Schmidt duality gives
   $$
   \|\widehat H_t\|_{\mathrm{HS}}^2\le8v_t,
   \qquad
   \widehat H_t=A_t^{-1/2}H_tA_t^{-1/2},
   \qquad
   v_t=\operatorname{Var}_{\mu_t}(f). \tag{2}
   $$
   The literature statement and constant were source-checked in
   `research/reviews/2026-08-24-kls-consolidation-audit.md`, but that audit explicitly supplies no
   proof certification. The certified dossier `solutions/kls-qcts-stein-boundary-core.tex`
   checks related two-color duality and QCTS equivalence, not the imported theorem and not (G).
3. The analogous fixed-cut absorption mechanism is certified in
   `solutions/kls-localization-riccati-core.tex`; it is an analogy only. None of its cut-specific
   estimates controls the eigenfunction tensor here.
4. The earlier exploration also proves that a direct unweighting of the positive moment-map Stein
   form by the Euclidean gradient and Hessian energies is false on truncated-exponential first
   eigenfunctions. That failed estimate is not used below.

Any eventual proof of (G) that consumes (2) must record `thm:letwin-qcts` in its dependency
closure and remain conditional while that preprint is an unreviewed import. The gate itself could
in principle be proved by another method, which is why no dependency edge is proposed merely from
this unsuccessful attack.

## Term-by-term decomposition

Write
$$
S_t=\|H_t\|_{\mathrm{HS}}^2,\qquad
q_t=\mathbb E|g_t|^2,\qquad
D_t=g_t^TA_tg_t.
$$

- **Source.** $S_t$ is the quadratic variation density of the martingale part of $g_t$. In the
  posterior covariance eigenbasis it is
  $$
  S_t=\sum_{i,j}a_i(t)a_j(t)(\widehat H_t)_{ij}^2. \tag{3}
  $$
  Formula (2) controls the unweighted sum of $(\widehat H_t)_{ij}^2$, not the two covariance
  weights in (3).
- **Exact damping.** $2D_t=2\sum_i a_i(t)g_{t,i}^2$ is the full negative drift in (1). The
  coefficient $\alpha<1$ leaves the strictly positive amount $2(1-\alpha)D_t$ after absorption.
- **Linear budget.** $C_0t$ must pay for source in covariance directions of universally bounded
  size and for no approximant-dependent initial layer.
- **Lower-order budget.** $C_1\int_0^tq_s\,ds$ is the term Gronwall may consume. Replacing a
  high-incidence tensor term by a terminal or instantaneous operator norm is not such a
  lower-order estimate.
- **Initial boundary.** Isotropy and normalization give $|g_0|^2\le1$.
- **Terminal term.** Taking expectations in (1) gives
  $$
  \mathbb E\int_0^tS_s\,ds
  =q_t-|g_0|^2+2\mathbb E\int_0^tD_s\,ds. \tag{4}
  $$
  Consequently (G) is exactly equivalent to
  $$
  q_t+2(1-\alpha)\mathbb E\int_0^tD_s\,ds
  \le |g_0|^2+C_0t+C_1\int_0^tq_s\,ds. \tag{5}
  $$
  Thus a proof must control both the terminal energy $q_t$ and a strict fraction of accumulated
  damping. Setting $\alpha=1$ discards the decisive term.
- **Regularization.** For an approximant with $\nabla^2V\succeq\varepsilon I$, posterior
  Brascamp--Lieb gives $A_t\preceq(\varepsilon+t)^{-1}I$. Inserting this into (2) produces
  $$
  \mathbb E\int_0^T S_t\,dt
  \le8\int_0^T(\varepsilon+t)^{-2}\mathbb Ev_t\,dt,
  $$
  whose coefficient is at best
  $8(\varepsilon^{-1}-(\varepsilon+T)^{-1})$. It diverges as
  $\varepsilon\downarrow0$. Strong convexity alone therefore does not give a uniform initial
  layer.
- **Orientation.** The two covariance factors in (3) must be retained entry by entry. The crude
  inequality $S_t\le8v_t\|A_t\|_{\mathrm{op}}^2$ is valid but loses precisely the information
  required by the gate.

All stochastic equalities in this report are first applied after stopping the coefficients and
the relevant martingales at level $N$. On the stated smooth strongly log-concave class the fixed
function has the required moments; localization and then Fatou/local uniform-integrability
arguments remove the auxiliary stopping. No estimate below has an $N$-dependent constant.

## Exact extraction of the low-covariance source

Fix a deterministic threshold $L>0$ and set
$$
P_{t,L}=\mathbf1_{(L,\infty)}(A_t),\qquad Q_{t,L}=I-P_{t,L}.
$$
No differentiation of this projector is needed for the following algebra. Because $P_{t,L}$ and
$Q_{t,L}$ commute with $A_t$, the Hilbert--Schmidt blocks of $H_t$ are orthogonal and
$$
S_t=\|Q_{t,L}H_tQ_{t,L}\|_{\mathrm{HS}}^2+\mathcal R_{t,L}, \tag{6}
$$
where the exact high-incidence source is
$$
\mathcal R_{t,L}
=\|P_{t,L}H_tP_{t,L}\|_{\mathrm{HS}}^2
+2\|P_{t,L}H_tQ_{t,L}\|_{\mathrm{HS}}^2. \tag{7}
$$
The low block obeys, conditional on (2),
$$
\|Q_{t,L}H_tQ_{t,L}\|_{\mathrm{HS}}^2
\le L^2\|Q_{t,L}\widehat H_tQ_{t,L}\|_{\mathrm{HS}}^2
\le8L^2v_t. \tag{8}
$$
Since $dv_t=dN_t-|g_t|^2dt$ and $v_0=1$,
$$
\mathbb Ev_t=1-\int_0^tq_s\,ds.
$$
Therefore
$$
\mathbb E\int_0^tS_s\,ds
\le8L^2\left[t-\int_0^t(t-s)q_s\,ds\right]
+\mathbb E\int_0^t\mathcal R_{s,L}\,ds
\le8L^2t+\mathbb E\int_0^t\mathcal R_{s,L}\,ds. \tag{9}
$$

This is the maximal unconditional extraction presently justified by the repository inputs. It
preserves orientation: no maximum eigenvalue appears in $\mathcal R_{t,L}$. In particular, (G)
would follow with $C_0=8L^2+C_H$ if one proved, for a universal $L$,
$$
\mathbb E\int_0^t\mathcal R_{s,L}\,ds
\le C_Ht+C_1\int_0^tq_s\,ds
+2\alpha\mathbb E\int_0^tD^H_{s,L}\,ds,
\qquad \alpha<1, \tag{10}
$$
where
$$
D^H_{t,L}=g_t^TP_{t,L}A_tP_{t,L}g_t\le D_t. \tag{11}
$$
Unlike the earlier bound by $\|A_t\|_{\mathrm{op}}^2\eta_{t,L}$, (7) is the exact Euclidean
tensor energy incident to the inflated space. Equation (10), not a global covariance-norm
estimate, is the remaining absorptive object.

## New exact input: the posterior eigenfunction defect

The initial eigenfunction equation does yield more structure than an arbitrary fixed function.
The gain and its exact limit are as follows.

Let
$$
L_t=L+(c_t-tx)\cdot\nabla
$$
be the generator reversible for $\mu_t$, and define the posterior eigenfunction defect
$$
R_t(x)=(c_t-tx)\cdot\nabla f(x),
\qquad
\bar R_t=\mathbb E_tR_t,
\qquad
r_t=R_t-\bar R_t. \tag{12}
$$
Also define
$$
\begin{aligned}
b_t&=\mathbb E_t\nabla f,\\
C_t&=\mathbb E_t[(X-a_t)\otimes\nabla f],\\
u_t&=\mathbb E_t[r_t(X-a_t)],\\
K_t&=\mathbb E_t[r_t(X-a_t)^{\otimes2}].
\end{aligned} \tag{13}
$$

### Posterior identities

The generator relation is exact:
$$
-L_tf=\lambda f-R_t. \tag{14}
$$
Posterior integration by parts with the constant function gives
$$
\bar R_t=\lambda m_t,
\qquad m_t=\mathbb E_tf. \tag{15}
$$
Pairing (14) with $X-a_t$ gives
$$
\lambda g_t=b_t+u_t. \tag{16}
$$
Indeed, $\mathbb E_t[(-L_tf)(X-a_t)]=\mathbb E_t\nabla f=b_t$, whereas the
left side of (14) paired with $X-a_t$ is $\lambda g_t-u_t$.

For a symmetric matrix $B$, put
$$
Q_B(x)=(x-a_t)^TB(x-a_t)-\operatorname{Tr}(BA_t).
$$
Then
$$
\mathbb E_t[(-L_tf)Q_B]
=\mathbb E_t[\nabla f\cdot\nabla Q_B]
=2\langle B,\operatorname{sym}C_t\rangle_{\mathrm{HS}}.
$$
The same pairing in (14) is
$\langle B,\lambda H_t-K_t\rangle_{\mathrm{HS}}$. Since this holds for every symmetric $B$,
$$
\boxed{\ \lambda H_t=2\operatorname{sym}C_t+K_t.\ } \tag{17}
$$
At $t=0$, $R_0=0$, so (16)--(17) recover $b_0=\lambda g_0$ and
$\lambda H_0=2\operatorname{sym}C_0$.

### Exact averaged budgets

Use the planted filtering realization: take $X\sim\mu$ and an independent Brownian motion
$B_t^{\mathrm{obs}}$, set
$$
c_t=tX+B_t^{\mathrm{obs}},
$$
and condition on the observation filtration. It has the same posterior process as stochastic
localization, with the usual innovation Brownian motion driving (1). At the planted point,
$$
R_t(X)=B_t^{\mathrm{obs}}\cdot\nabla f(X).
$$
Since $B_t^{\mathrm{obs}}$ is independent of $X$ and
$\mathbb E|\nabla f|^2=\lambda$,
$$
\mathbb E\mathbb E_tR_t^2=t\lambda. \tag{18}
$$
Moreover $dm_t=g_t\cdot dW_t$, $m_0=0$, so
$$
\mathbb Em_t^2=\int_0^tq_s\,ds.
$$
Combining this with (15) and (18) gives the exact centered-defect budget
$$
\boxed{\ \mathbb E\operatorname{Var}_t(R_t)
=t\lambda-\lambda^2\int_0^tq_s\,ds.\ } \tag{19}
$$

There are two immediate orientation-sensitive consequences. The block covariance matrix of
$(r_t,X-a_t)$ is positive semidefinite, hence
$$
u_t^TA_t^{-1}u_t\le\operatorname{Var}_t(R_t). \tag{20}
$$
Conditional on `thm:letwin-qcts`, the same Hilbert--Schmidt duality as in (2) gives
$$
\|A_t^{-1/2}K_tA_t^{-1/2}\|_{\mathrm{HS}}^2
\le8\operatorname{Var}_t(R_t). \tag{21}
$$
Thus the intrinsic defect tensor has the explicit averaged budget
$$
\mathbb E\|A_t^{-1/2}K_tA_t^{-1/2}\|_{\mathrm{HS}}^2
\le8\left(t\lambda-\lambda^2\int_0^tq_s\,ds\right). \tag{22}
$$

The other term in (17) also has an exact occupation budget. Since $b_t$ is the posterior mean of
the fixed vector field $\nabla f$,
$$
db_t=C_t^T\,dW_t.
$$
Consequently
$$
\mathbb E\int_0^t\|C_s\|_{\mathrm{HS}}^2\,ds
=\mathbb E|b_t|^2-|b_0|^2
\le\lambda-\lambda^2|g_0|^2, \tag{23}
$$
where Jensen, the fixed-integrand martingale, and $b_0=\lambda g_0$ were used.

Finally the initial Hessian energy enters the defect at the next derivative. At fixed $c_t$,
$$
\nabla_xR_t=(\nabla^2f)(c_t-tx)-t\nabla f.
$$
In the planted realization, the cross term averages to zero and Bochner gives
$$
\mathbb E\mathbb E_t|\nabla R_t|^2
=t\mathbb E\|\nabla^2f\|_{\mathrm{HS}}^2+t^2\lambda
\le t\lambda^2+t^2\lambda. \tag{24}
$$
Equations (19), (22)--(24) are uniform in the approximant's strong-convexity parameter.

### What these budgets do and do not buy

Equations (17), (19), and (23) are a genuine use of the eigenfunction equation. They show that
the posterior is an approximate eigenfunction in an averaged intrinsic sense and identify both
pieces of its quadratic tensor exactly. They do not prove (10):

- Solving (17) for $H_t$ and applying Young's inequality makes the $C_t$ budget contribute
  $O(1/\lambda)$ after time integration. That is not a universal gate constant in the small-gap
  branch for which the argument is needed.
- Equation (22) controls the whitened $K_t$. Its high block is unwhitened by exactly the same two
  covariance factors as (3). Multiplying (22) by $\|A_t\|_{\mathrm{op}}^2$ both loses tensor
  orientation and illegitimately separates two correlated random quantities.
- Equation (24) is an unweighted gradient budget. Turning it into Euclidean high-incidence
  control for $K_t$ would require a new asymmetric quadratic covariance theorem. Neither
  Letwin's constant-matrix inequality nor posterior Brascamp--Lieb supplies that theorem.

Thus the eigenfunction equation reduces the source to controlled intrinsic defects but does not
perform the high-rank unwhitening. The first unsupported statement remains (10).

## Attempt to consume high incidence by a moving spectral potential

The natural way to match (7) to the high damping (11) is to apply It\^o's formula to the high
part of $g_t$. A hard projector cannot be differentiated at eigenvalue crossings, so let
$\chi$ be a smooth scalar cutoff and put
$$
F_t=\chi(A_t),\qquad z_t=F_tg_t.
$$
Write the covariance SDE as
$$
dA_t=\sum_k\mathcal T_{t,k}\,dW_{t,k}-A_t^2dt,
$$
where $\mathcal T_{t,k}$ is the $k$-th third-moment matrix. Matrix It\^o calculus gives the
martingale coefficient of $z_t$ as
$$
F_tH_te_k+D\chi(A_t)[\mathcal T_{t,k}]g_t, \tag{25}
$$
and its drift as
$$
\begin{aligned}
&-F_tA_tg_t
+D\chi(A_t)[-A_t^2]g_t
+\frac12\sum_kD^2\chi(A_t)[\mathcal T_{t,k},\mathcal T_{t,k}]g_t\\
&\hspace{35mm}
+\sum_kD\chi(A_t)[\mathcal T_{t,k}]H_te_k. \tag{26}
\end{aligned}
$$
Therefore the terms in the $|z_t|^2$ identity are:

1. the desired row-high source $\|F_tH_t\|_{\mathrm{HS}}^2$;
2. the exact damping $2g_t^TF_t^2A_tg_t$;
3. the extra positive source
   $\sum_k|D\chi(A_t)[\mathcal T_{t,k}]g_t|^2$;
4. the source cross term between the two summands in (25);
5. the covariance-drift error $D\chi(A_t)[-A_t^2]g_t$;
6. the It\^o curvature error involving $D^2\chi$ and the complete Haar sum of the
   $\mathcal T_{t,k}$;
7. the $H_t$--third-moment cross term in the last line of (26); and
8. the terminal boundary $\mathbb E|F_tg_t|^2- |F_0g_0|^2$.

For a cutoff approximating $P_{t,L}$, (7) satisfies
$$
\|P_{t,L}H_t\|_{\mathrm{HS}}^2
\le\mathcal R_{t,L}
\le2\|P_{t,L}H_t\|_{\mathrm{HS}}^2. \tag{27}
$$
Thus (25) sees the correct tensor block. It does not close: the terms containing $D\chi$ and
$D^2\chi$ are random, test-dependent contractions of the third-moment tensor with $g_t$ and
$H_t$. The available constant-direction third-moment estimates do not control this complete
sum with the sign and strict damping deficit required by (10). Bounding them by operator norms
reintroduces the covariance-spike/soft-maximum loss that Route S was designed to avoid.

Keeping $\chi$ smooth leaves a transition-band occupation term whose constants scale with the
first two derivatives of the cutoff. Sending the band width to zero is unsupported; using the
hard projector would instead require eigenvalue-crossing local-time or divided-difference
control. This is a boundary error, not a harmless technicality.

This calculation stops at the first unjustified step: no repository theorem bounds terms
3--7 above by $C_Ht+C_1\int q+2\alpha\int D^H$ with $\alpha<1$. That missing estimate is the
unwhitening fence in differential form.

## Tensorization sanity check

The exact block formulation correctly ignores covariance spikes in spectator factors. Let
$\mu=\bigotimes_i\mu_i$ and suppose the bottom eigenspace is spanned by factor eigenfunctions
$f_i$. For a normalized $f=\sum_i\theta_if_i$, localization remains a product pathwise and
$$
A_t=\operatorname{diag}(A_t^{(i)}),\qquad
(g_t)_i=\theta_i g_t^{(i)},\qquad
(H_t)_{ij}=0\ (i\ne j),\qquad
(H_t)_{ii}=\theta_iH_t^{(i)}. \tag{28}
$$
Consequently
$$
S_t=\sum_i\theta_i^2S_t^{(i)},\qquad
|g_t|^2=\sum_i\theta_i^2|g_t^{(i)}|^2,
\qquad
D_t=\sum_i\theta_i^2D_t^{(i)}. \tag{29}
$$
The gate therefore tensorizes without multiplicity loss whenever the factor gates have common
constants. A large posterior covariance in a factor absent from $f$ contributes neither to
$H_t$ nor to $\mathcal R_{t,L}$. This is precisely the behavior lost in the crude
$\|A_t\|_{\mathrm{op}}^2$ bound and confirms that (7) has the right orientation. It proves no
one-dimensional gate and hence no universal conclusion.

## Uniform approximation and terminal interface

For the gate itself, take genuine first eigenfunctions $f_k$ of smooth isotropic strongly
log-concave approximants $\mu_k$. The identities (1), (14)--(24), and the split (6)--(9) have no
constant depending on the strong-convexity modulus. By contrast, the direct
$(\varepsilon_k+t)^{-1}$ Brascamp--Lieb route diverges as shown above.

The remaining approximation requirements are logically downstream and are not proved here:

- a concrete approximation must preserve the Poincare variational value in the limit;
- if the spectral bottom is not attained in the limiting law (the shifted exponential is the
  repository's explicit warning), true $f_k$ need not converge to a limiting eigenfunction;
- an approximate-Rayleigh-minimizer formulation would add the residual
  $-Lf_k-\lambda_kf_k$ to (14), hence extra coordinate and quadratic covariance errors to
  (16)--(17); and
- the terminal variance estimate and passage from a uniform gate to the arbitrary law belong to
  `prop:spectral-sufficiency`, not to this probe.

The exact interface supplied to that node, if (G) were proved, is only: common
$T_0,C_0,C_1,\alpha$ for every regular isotropic approximant, with $\alpha<1$, and enough spectral
convergence or approximate-minimizer control to pass the resulting uniform lower bound on
$\lambda_k$. No terminal variance or limit claim is asserted here.

## Residue

1. **Needs new idea — exact high-incidence absorption.** Prove (10) for one fixed universal
   $L$, uniformly over regular approximants. This is the first missing mathematical statement.
2. **Fenced — moving-projector errors.** In the spectral-cutoff attack, control terms 3--7 after
   (27) without replacing them by $\|A_t\|_{\mathrm{op}}$, a soft maximum, or a dimensionful
   complete third-moment sum. Current inputs do not do this.
3. **Fenced — posterior defect unwhitening.** Equations (19) and (22) give an $O(t\lambda)$
   intrinsic defect budget, but its high Euclidean block is still covariance weighted and
   correlated with the defect. Crude unwhitening is the original fence in disguise.
4. **Technical gap — certification of the new structural lemma.** Equations (14)--(24) have a
   complete analytic derivation above but no standalone dossier or independent review.
5. **Technical gap — regularization consumer.** Spectral/Mosco convergence or a fully tracked
   approximate-minimizer residual is required only for `prop:spectral-sufficiency`; it is not
   supplied by the occupation estimate itself.

The failure is not a route-fatal counterexample. It identifies a narrower deliverable than the
previous global alignment wording.

## Fence-by-fence evasion check

The live node has no formal `bounded_by` edge. For completeness, every obstruction in
`research/kls/obstructions.md` was checked.

- `obs:two-tail`: scoped to fixed cuts and absolute slice-wise Stein source bounds. No cut,
  excess, or slice estimate is used. The analogous lesson is respected by retaining
  $\mathcal R_{t,L}$ rather than asserting an unweighted static bound.
- `obs:proj-ceiling`: (2), (7), and (21) use all symmetric-matrix tests and full tensor blocks,
  not radial or projection-only information.
- `obs:crude-insufficient`: no crude covariance integral $\Xi_T$ or logarithmic bootstrap is
  inserted.
- `obs:relative-ceiling`: no universal relative $\Xi_{T_0}/T_0$ estimate is claimed.
- `obs:circularity`: no localized isoperimetric profile or changing competitor family occurs.
- `obs:rank-one-refuted`: this is a fixed-cut product obstruction. Equation (28) instead checks
  exact spectral tensorization and makes no cut counterexample claim.

Two route-specific warnings also bind the proof shape. Proposition `prop:covariance-spike` in the
manuscript rules out a pathwise global operator-norm proof; (7) evades it, while every failed
norm estimate above does not. The truncated-exponential Stein-unweighting counterexample rules
out the earlier variable-weight shortcut; it is not used or generalized here.

This probe does not touch `q:upgrade`, `q:stein-weighted`, or `q:alignment`, and asserts no
transfer to the trace-upgrade cluster.

## Route viability and proposed gate update

Route S remains viable. The fixed-function SDE, exact damping, tensorization, low-sector
extraction, and posterior-defect budgets all have the right dimension-free form. They do not
control the only block that matters: the Euclidean tensor energy incident to the inflated
posterior covariance space. The route now has a more precise failure point, not a proof.

Proposed one-line gate update for the orchestrator:

> Fix a universal covariance threshold $L$, extract the low block by
> $\mathbb E\int\|Q_{s,L}H_sQ_{s,L}\|_{\mathrm{HS}}^2ds\le8L^2t$, and prove the exact
> high-incidence estimate (10) against a strict fraction of
> $2g_s^TP_{s,L}A_sP_{s,L}g_s$, uniformly through regular approximation; global
> $\|A_s\|_{\mathrm{op}}$ bounds and uncontrolled moving-projector errors are inadmissible.

## Proposed ledger delta

The following is a candidate node only. It is proposed as `open` pending a standalone dossier and
independent review; no proof status or certification metadata is proposed.

```yaml
- id: lem:mm-posterior-defect
  kind: lemma
  status: open
  route: moment-map-spectral
  file: modules/kls/30-spectral-route.tex
  statement: "For a regular normalized first eigenfunction under the planted localization channel, the posterior defect R_t=(c_t-tX)·grad f satisfies E Var_t(R_t)=t lambda-lambda^2 int_0^t E|g_s|^2 ds, lambda g_t=b_t+u_t, lambda H_t=2 sym C_t+K_t, and E int_0^t ||C_s||_HS^2 ds <= lambda-lambda^2|g_0|^2."
```

If the conditional bound (21) is later promoted as a separate corollary, it must depend on
`thm:letwin-qcts` and inherit that node's preprint-conditional standing.

## Numerical handoff

None. The registered `kls-align` target concerns a designated fixed-cut product family, not
first-eigenfunction tensors. A finite spectral experiment would neither certify (10) nor refute
its universal quantifiers, and no fixed analytic refuting threshold emerged from this probe.

```yaml
outcome: blocked
artifacts:
  - research/explorations/2026-08-27-kls-route-prober-mm-spectral-occupation-par-02.md
proposed_deltas:
  - Add candidate open node lem:mm-posterior-defect with the exact ledger statement displayed above, together with its manuscript anchor; do not change q:mm-spectral-occupation status.
next_role: prover
next_prompt: |
  Write a standalone dossier for candidate node lem:mm-posterior-defect only. Work on smooth,
  strongly log-concave, isotropic regular approximants with a normalized first eigenfunction.
  Reconstruct the planted filtering coupling c_t=tX+B_t, prove -L_t f=lambda f-R_t and
  E_t R_t=lambda m_t, then prove lambda g_t=b_t+u_t and
  lambda H_t=2 sym C_t+K_t by posterior integration by parts against coordinates and centered
  quadratics. Prove the exact budget
  E Var_t(R_t)=t lambda-lambda^2 int_0^t E|g_s|^2 ds, the martingale budget
  E int_0^t ||C_s||_HS^2 ds <= lambda-lambda^2|g_0|^2, and the averaged gradient-defect bound
  E E_t|grad R_t|^2 <= t lambda^2+t^2 lambda. State domains and stopping/removal explicitly.
  You may record the whitened K_t consequence only as conditional on imported
  thm:letwin-qcts. Do not claim the high-incidence estimate, q:mm-spectral-occupation,
  prop:spectral-sufficiency, or KLS. Compile the dossier and hand it to a distinct proof-checker.
```
