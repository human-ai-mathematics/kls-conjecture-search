# A4 modified-transport refinement after the one-dimensional import

## Scope and sources

This refinement owns only `q:a4-modified`.  I read its accepted manuscript question and the
surrounding setup, `research/a-series/ledger.yaml`, the A4 target brief, all of
`research/a-series/obstructions.md`, and the source-verified import record for
`thm:a4-modified-transport-1d`.  No numerical diagnostic was requested or run.

The accepted question asks for the strongest modified cost for every robust-Bayes prior, on a
variational family or on KL sublevels.  That wording now conflates three logically different
regimes:

1. The global one-dimensional generalized-normal regime is already imported and solved up to
   the scale of the cost.
2. The global unbounded-convex-cost regime is impossible for polynomial-tail Student and
   horseshoe laws.
3. A posterior-specific family restriction or localized sublevel can still be useful, but only
   after its own finiteness mechanism is stated and proved.

## Exact candidate statement

Replace `q:a4-modified` by the following question.

For $1\le p\le2$, define
$$
 \theta_p(t)=
 \begin{cases}
 t^2,&|t|\le1,\\[1mm]
 \dfrac2p|t|^p+1-\dfrac2p,&|t|\ge1.
 \end{cases}
$$
Regard the following two global branches as closed boundaries, not as deliverables: for
$\pi_p(dx)\propto e^{-|x|^p}dx$, `thm:a4-modified-transport-1d` gives an $a_p>0$ for which
$$
 \mathcal T_{\theta_p(a_p\,\cdot)}(q,\pi_p)
 \le \KL(q\|\pi_p)
 \qquad\text{for every probability law }q;
$$
and a polynomial-tail Student or horseshoe law admits no global transport--entropy inequality
with a nonzero unbounded convex cost.

For the first residual posterior/family problem, fix
$$
 \pi_{\nu,n}(dx)=Z_{\nu,n}^{-1}
 \left(1+\frac{x^2}{\nu}\right)^{-(\nu+1)/2}
 \operatorname{sigmoid}(x)^n\,dx,
 \qquad \nu>2,\quad n\in\mathbb N,\ n\ge1,
$$
and
$$
 \mathcal Q_s=\{q_m=N(m,s^2):m\in\mathbb R\},\qquad s>0.
$$
Put
$$
 K(m)=\KL(q_m\|\pi_{\nu,n}),\qquad
 \delta=\min_{m\in\mathbb R}K(m),\qquad
 M_\rho=\{m:K(m)\le\delta+\rho\}.
$$
First prove that $K$ is continuous and coercive, that $\delta>0$, and hence that $M_\rho$ is nonempty and compact
for every $\rho\ge0$.  Then determine explicit matching upper and lower bounds, including the
sharp large-$\rho$ order, for
$$
 C_{\nu,n,s}(\rho)
 =\sup_{m\in M_\rho}
 \frac{W_2^2(q_m,\pi_{\nu,n})}{2K(m)}.
$$
The finiteness claim must use compactness of this named parameter sublevel, continuity of the
family in $\mathcal P_2$, and $\nu>2$; it must not infer a finite transport radius from the KL
cutoff alone.  A finite result beats the global value $+\infty$ only for this family and
sublevel.  No positive horseshoe claim is included until a weighted, weak, bounded, or otherwise
finite cost and a family coercivity contract are specified.

## Why this is a defensible first model

The target is a Student-$t_\nu$ prior tilted by $n$ identical one-dimensional logistic
likelihood factors.  The positive tail remains polynomial because
$\operatorname{sigmoid}(x)^n\to1$ as $x\to+\infty$, so the imported global obstruction remains
active.  The condition $\nu>2$ puts the target in $\mathcal P_2$, while the fixed-variance
Gaussian family makes the reverse-KL sublevel a finite-dimensional coercivity question.
Indeed, the negative log target has the form
$$
 \frac{\nu+1}{2}\log\left(1+\frac{x^2}{\nu}\right)
 +n\log(1+e^{-x})+\text{constant},
$$
which grows logarithmically as $x\to+\infty$ and linearly as $x\to-\infty$.  This observation
specifies the analytic route to coercivity; it is not being used here to promote the requested
sharp coefficient to proved status.

## Fence-by-fence check

- `obs:restricted-not-finite`: respected.  The statement does not treat $\KL\le\delta+\rho$ as
  sufficient by itself.  It requires a named finite-dimensional family, proof of coercivity and
  compactness of its complete sublevel, $\mathcal P_2$ tail control, and continuity before any
  finite coefficient is asserted.
- `obs:heavy-tail-no-classical`: respected.  The Student-logistic posterior retains a polynomial
  tail, its global unbounded-convex-cost constant is explicitly left at $+\infty$, and only a
  family-and-sublevel coefficient is requested.
- `obs:flat-direction` (A4 guardrail, not a current edge of this node): respected.  Saturation of
  the logistic factor at $+\infty$ is used to preserve, rather than suppress, the heavy tail; no
  inverse-Hessian or global-curvature conclusion is proposed.
- `obs:gaussian-tail-rigidity` (A4 guardrail, not a current edge): not triggered.  The target has
  a Student prior and no global Gaussian-prior logistic $T_2$ improvement is claimed.
- `obs:symmetry-vs-physical` (A4 guardrail, not a current edge): not triggered.  This is a
  one-parameter location family with no quotient or multimodal improvement claim.

## Gain over the current statement and sibling consistency

The current wording leaves solved and impossible global problems mixed into an unbounded
classification programme.  The delta removes both, names one posterior, one variational family,
the nonempty level $\delta+\rho$, the finiteness mechanism, and the exact coefficient to bound.
On the Student-logistic model, a finite $C_{\nu,n,s}(\rho)$ strictly improves the global baseline
$+\infty$, but only under the stated family/sublevel restriction; it does not reproduce or claim
a global inequality.

The delta does not alter `q:a4-certificate` or `q:a4-restricted`: it supplies a heavy-tail test
case for their coercivity principle without claiming Fisher or posterior-Hessian scaling.  It
does not alter A3's weighted-Poincar\'e programme, and it makes no A5 quotient claim.

## Dead ends rejected

- Keeping “classify the strongest global cost for every robust prior” would ask again for the
  imported generalized-normal result and would violate the polynomial-tail obstruction.
- Restricting only to an unrestricted KL ball would violate `obs:restricted-not-finite`.
- Using a horseshoe target with ordinary $W_2$ would not even meet the $\mathcal P_2$ setup; a
  weighted, weak, or bounded geometry must be fixed before that branch becomes an exact target.
- Optimizing the existential generalized-normal scale $a_p$ is a legitimate separate constants
  problem, but it would not address the posterior/family-restricted gap assigned here.

## Proposed ledger delta

Node: `q:a4-modified`.  Only the following fields change:

```yaml
statement: "Treat the one-dimensional generalized-normal theta_p inequality as solved by thm:a4-modified-transport-1d and the global unbounded-convex-cost programme as impossible for polynomial-tail Student/horseshoe laws. For the first residual target, take the one-dimensional Student-logistic posterior pi_{nu,n}(dx) proportional to (1+x^2/nu)^(-(nu+1)/2) sigmoid(x)^n dx with nu>2 and the fixed-scale Gaussian location family Q_s={N(m,s^2)}: prove reverse-KL coercivity and compactness of every complete sublevel {KL<=delta+rho}, then obtain explicit matching bounds and the sharp large-rho order of the localized restricted W2^2/(2 KL) coefficient. Do not infer finiteness from a KL cutoff alone; use the named family compactness and P2 tail contract."
depends_on: [thm:a4-modified-transport-1d]
```

## Paths written

- `research/a-series/targets/A4-variational-inference.md`
- `research/explorations/2026-08-27-refiner-a4-modified-a4m8c31.md`

```yaml
outcome: complete
artifacts:
  - research/a-series/targets/A4-variational-inference.md
  - research/explorations/2026-08-27-refiner-a4-modified-a4m8c31.md
proposed_deltas:
  - "For q:a4-modified, replace only statement and depends_on by the exact residual Student-logistic/Gaussian-location proposal above; retain kind question, status open, and bounded_by [obs:restricted-not-finite, obs:heavy-tail-no-classical]."
next_role: orchestrator
next_prompt: |
  Decide whether to accept the staged q:a4-modified refinement. If accepted, replace the
  manuscript question and atomically update only the ledger statement and depends_on fields,
  retaining kind question, status open, and bounded_by [obs:restricted-not-finite,
  obs:heavy-tail-no-classical]. Run python3 research/check_ledger.py and perform a semantic
  manuscript/ledger/brief comparison. Do not promote any finite coefficient or sharp-rho claim
  to proved status; those are the residual theorem deliverables.
```
