---
---
# Prover: posterior eigenfunction-defect calculus

Date: 2026-08-27

Role: `prover`

Concurrency key: `solution:lem-mm-posterior-defect`

Author: `/root/prove_posterior_defect_par_06`

Status: complete candidate dossier, `checked_by: none`; no proof certification or ledger delta
is applicable before an independent review.

## Node, statement, and dependency audit

The accepted ledger node is `lem:mm-posterior-defect`, with manuscript anchor
`lem:mm-posterior-defect` in `modules/kls/30-spectral-route.tex`. The ledger node is `open`, has
no `depends_on` edge, has no `bounded_by` edge, and has no consumers. The dossier theorem matches
the manuscript lemma: on a smooth strongly log-concave centered isotropic regular approximant,
for a normalized first nonconstant eigenfunction $-Lf=\lambda f$, it proves
$$
\mathbb E_tR_t=\lambda m_t,
\qquad
\lambda g_t=b_t+u_t,
\qquad
\lambda H_t=2\operatorname{sym}C_t+K_t,
$$
$$
\mathbb E\operatorname{Var}_t(R_t)
=t\lambda-\lambda^2\int_0^t\mathbb E|g_s|^2\,ds,
\qquad
\mathbb E\int_0^t\|C_s\|_{\mathrm{HS}}^2\,ds
\le \lambda-\lambda^2|g_0|^2,
$$
and
$$
\mathbb E\mathbb E_t|\nabla R_t|^2\le t\lambda^2+t^2\lambda.
$$
Here $R_t(x)=(c_t-tx)\cdot\nabla f(x)$ in the planted observation channel
$c_t=tX+B_t^{\mathrm{obs}}$, and all centered quantities and tensor orientations are stated in
the dossier.

No imported or unresolved mathematical node is used. In particular, `thm:letwin-qcts` is
explicitly excluded. The result is therefore unconditional on the regular class stated in the
manuscript; it does not include a limit to arbitrary log-concave measures.

## Analytic proof supplied

The dossier reconstructs the planted filter and innovation Brownian motion. It derives the
posterior density and the fixed-integrand martingale equation
$$
d\mathbb E_t\phi=\operatorname{Cov}_t(\phi,X)\cdot dW_t.
$$
For the posterior generator
$$
L_t=L+(c_t-tx)\cdot\nabla,
$$
the eigenfunction equation gives
$$
-L_tf=\lambda f-R_t.
$$
Posterior integration by parts against the constant, each centered coordinate, and every
centered quadratic
$$
Q_D(x)=(x-a_t)^TD(x-a_t)-\operatorname{Tr}(DA_t),\qquad D=D^T,
$$
then yields the three tensor identities. The orientation convention is
$(v\otimes w)_{ij}=v_iw_j$, so
$C_t=\mathbb E_t[(X-a_t)\otimes\nabla f]$ and
$db_t=C_t^T\,dW_t$; this is why the quadratic pairing returns
$2\operatorname{sym}C_t$.

At the planted point,
$$
R_t(X)=B_t^{\mathrm{obs}}\cdot\nabla f(X).
$$
Independence gives $\mathbb E\mathbb E_tR_t^2=t\lambda$. Combining this with
$dm_t=g_t\cdot dW_t$ and $\mathbb E_tR_t=\lambda m_t$ gives the exact variance budget. Applying
the same fixed-integrand martingale formula to $\nabla f$ gives
$$
\mathbb E\int_0^t\|C_s\|_{\mathrm{HS}}^2\,ds
=\mathbb E|b_t|^2-|b_0|^2,
$$
after which conditional Jensen, $\mathbb E|\nabla f|^2=\lambda$, and
$b_0=\lambda g_0$ give the stated inequality. Finally,
$$
\nabla R_t(X)=\nabla^2f(X)B_t^{\mathrm{obs}}-t\nabla f(X),
$$
so independence reduces its second moment to
$t\mathbb E\|\nabla^2f\|_{\mathrm{HS}}^2+t^2\lambda$. The integrated weighted Bochner identity
and $\nabla^2V\succeq0$ give
$\mathbb E\|\nabla^2f\|_{\mathrm{HS}}^2\le\lambda^2$.

No numerical evidence appears anywhere in the argument.

## Domains, stopping, and hypotheses actually used

The hypotheses actually used, all stated in the theorem, are:

- $\mu(dx)=Z^{-1}e^{-V(x)}dx$ on $\mathbb R^n$, with $V\in C^\infty$ and
  $\nabla^2V\succeq\varepsilon I$;
- $\mu$ is centered and isotropic, matching the route's regular approximants;
- $f$ belongs to the Friedrichs generator domain, satisfies $-Lf=\lambda f$,
  $\mathbb E f=0$, and $\mathbb E f^2=1$;
- the planted observation Brownian motion is standard and independent of $X$;
- standard closed Dirichlet-form integration by parts and the integrated weighted Bochner
  identity for this smooth strongly confining generator.

There are no hypotheses used but omitted from the theorem. The dossier treats the generator as
the Friedrichs realization, so it imposes no unmentioned boundary condition at infinity.
Posterior integrations by parts are first made with compact spatial cutoffs. Strong posterior
convexity supplies polynomial moments, while the planted $L^2$ identities put $f$, $\nabla f$,
and $R_t$ in the needed posterior spaces; closedness removes the cutoffs. Filtering identities
are first proved for bounded truncations and before a stopping time at level $N$. The conditional
expectation martingales for $f$ and $\nabla f$ are square-integrable, so the stochastic integrals
and stopped It\^o isometries converge in $L^2$ as $N\to\infty$. Thus all exact equalities survive
stopping removal.

No analytic step remains unclosed in the stated regular class.

## Fence-by-fence check

There is no formal `bounded_by` edge. Every route warning was nevertheless checked:

- `obs:two-tail`: no cut, slice, excess, or absolute Stein-source estimate occurs.
- `obs:proj-ceiling`: the proof uses exact coordinate and arbitrary symmetric-matrix pairings; it
  claims no quadratic-chaos bound from radial or projection-only tests.
- `obs:crude-insufficient`: no crude covariance integral $\Xi_T$ is used.
- `obs:relative-ceiling`: no relative covariance occupation estimate is claimed.
- `obs:circularity`: no localized isoperimetric profile or changing competitor family occurs.
- `obs:rank-one-refuted`: no fixed-cut product counterexample or conclusion occurs.
- `prop:covariance-spike` and the spectral unwhitening fence: no operator-norm covariance bound,
  Euclidean unwhitening, or high-incidence estimate is claimed.
- The truncated-exponential variable-weight Stein shortcut is not used.
- The transport and needle warnings are not engaged.

The dossier expressly does not prove `q:mm-spectral-occupation`,
`prop:spectral-sufficiency`, an approximation passage, or KLS. It does not claim any implication
for the trace-upgrade cluster.

## Build and attempt record

Artifact: `solutions/lem-mm-posterior-defect.tex`.

The first standalone compile exposed a TeX-structure defect: repeated `\paragraph` sectioning
commands inside the `proof` trivlist caused `Something's wrong--perhaps a missing \item` at the
second internal heading. Replacing the internal headings by emphasized inline headings and
giving the labeled $L_t$ display an `equation` environment fixed the build. This was a typesetting
dead end only; no mathematical step was changed or suppressed.

The required command
```text
cd solutions && latexmk -pdf -outdir=../build lem-mm-posterior-defect.tex
```
now exits with status 0 and produces `build/lem-mm-posterior-defect.pdf` (four pages). The log has
no TeX error, overfull box, underfull box, or package warning. Its only LaTeX warning is the
expected unresolved cross-module reference `lem:mm-posterior-defect` in the standalone build.
`git diff --check` is clean for the dossier.

## Certification and deferred ledger candidate

The dossier header remains `checked_by: none`, with an empty reviewer and review field. Therefore
there is **no applicable ledger delta**. Only after a distinct proof-checker passes the complete
argument could the orchestrator atomically consider the deferred candidate
`solution: solutions/lem-mm-posterior-defect.tex` together with real certification metadata.

```yaml
outcome: complete
artifacts:
  - solutions/lem-mm-posterior-defect.tex
  - research/explorations/2026-08-27-prover-mm-posterior-defect-par-06.md
proposed_deltas:
  - none
next_role: proof-checker
next_prompt: |
  Cold-review `solutions/lem-mm-posterior-defect.tex` for the sole ledger node
  `lem:mm-posterior-defect`, independently of author `/root/prove_posterior_defect_par_06`.
  The theorem must match manuscript label `lem:mm-posterior-defect`: for a smooth strongly
  log-concave centered isotropic regular approximant and normalized first eigenfunction
  `-Lf=lambda f`, the planted posterior defect must satisfy `E_t R_t=lambda m_t`,
  `lambda g_t=b_t+u_t`, `lambda H_t=2 sym(C_t)+K_t`, the exact variance identity
  `E Var_t(R_t)=t lambda-lambda^2 int_0^t E|g_s|^2 ds`, the martingale budget
  `E int_0^t ||C_s||_HS^2 ds <= lambda-lambda^2|g_0|^2`, and
  `E E_t|grad R_t|^2 <= t lambda^2+t^2 lambda`.

  Reconstruct and audit every step from repository artifacts. In particular verify: the endpoint
  posterior density for the full observation filtration; the innovation Brownian motion and
  fixed-integrand filtering SDE; the sign in `-L_t f=lambda f-R_t`; the coordinate and centered
  quadratic integration-by-parts pairings; the tensor orientation
  `C_ij=E_t[(X_i-a_i) partial_j f]`, hence `db=C^T dW` and the factor
  `2 sym(C)`; the planted cancellation `R_t(X)=B_t^obs dot grad f`; exact stopped Ito isometries
  and their L2 removal; `b_0=lambda g_0`; the spatial formula for `grad R_t`; and the weighted
  Bochner bound `E||Hess f||_HS^2 <= lambda^2`. Check that the Friedrichs/domain and spatial
  cutoff discussion is sufficient and that no unstated integrability or boundary hypothesis is
  used.

  The node has no `depends_on` and no formal `bounded_by` edge. Check all route fences anyway:
  the dossier must use no cut/slice estimate, projection-only quadratic-chaos claim, crude or
  relative covariance occupation input, localized-profile insertion, product-cut conclusion,
  posterior operator-norm bound, tensor unwhitening, or truncated-exponential Stein shortcut.
  It must not use the unreviewed `thm:letwin-qcts` and must not claim high-incidence occupation,
  `q:mm-spectral-occupation`, `prop:spectral-sufficiency`, an arbitrary-measure approximation
  limit, or KLS. The result is unconditional only within the stated regular class.

  Re-run `cd solutions && latexmk -pdf -outdir=../build lem-mm-posterior-defect.tex`; the author
  reports a successful four-page build with only the expected unresolved manuscript reference.
  Persist a structured proof-review under `research/reviews/` with a reviewer identity distinct
  from the author. Certify only if every displayed identity, domain passage, and exclusion is
  complete; otherwise return a verbatim `next_prompt` naming every required repair.
```
