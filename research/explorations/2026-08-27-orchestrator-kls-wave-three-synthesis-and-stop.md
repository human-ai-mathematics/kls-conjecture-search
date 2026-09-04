---
type: exploration
date: "2026-08-27"
outcome: proposed
nodes:
  - q:upgrade
  - q:stein-weighted
---
# KLS Wave 3 synthesis and stopping checkpoint

Date: 2026-08-27

Role: orchestrator

## Stopping decision

Wave 3 is the stopping boundary for this exploration campaign. Every task already in flight was
allowed to finish, every new proof dossier received a distinct cold review, and the manuscript,
ledger, route controls, and bibliography were synchronized. No Wave 4 task is launched from this
record.

This checkpoint does **not** prove KLS. It replaces several vague or false intermediate targets
by narrower gates, certifies reusable proof surplus, admits one genuinely different live route,
and parks one additional route probe behind a named next obstruction.

## Certified mathematical deltas

### Stopped bootstrap interface

`thm:bootstrap-stopped-interface` is proved and agent-certified. Retaining the stopping
indicator in the covariance supply gives the cut-dependent quantity

$$
\widehat\Xi_{T,\eta}(mu,E)
=\int_0^T\mathbb E[X_s\mathbf 1_{\{s<\tau_\eta\}}],ds
$$

with the exact coefficients $1/16$, $1/8$, and $1/4$ in the near-worst bootstrap. For
$T<1/8$, $\eta=T^{1/3}$, and $\varepsilon\le T^{1/3}$ the universal constant may be taken as
$2$. The theorem claims no universal bound on $\widehat\Xi$ and no KLS conclusion. See the
[dossier](../../solutions/thm-bootstrap-stopped-interface.tex) and
[review](../reviews/2026-08-27-thm-bootstrap-stopped-interface-proof-review.md).

### Conditional-fiber structure and the root-frame obstruction

The new live route `conditional-fiber-frame` now has a certified structural bridge. For a
full-dimensional density with finite second moment, the inverse-conditional-variance line form
is a closed reversible Dirichlet form; for log-concave laws it satisfies

$$
\mathcal D_{\mu,\rho}(f)\le4\int|\nabla f|^2,d\mu.
$$

Linear energy is exactly $|a|^2$, with quotient one only under isotropy. Gaussian frames and
standardized coordinate products have form gap one. On the isotropic simplex, however, the
$A_{m-1}$ root frame has gap at most

$$
\frac{12(m-1)}{m^2(m+1)}=O(m^{-2}).
$$

Only that root implementation is refuted. The all-frame question remains open, and no
equivalence with KLS is asserted. See the
[dossier](../../solutions/conditional-fiber-frame-structure.tex),
[review](../reviews/2026-08-27-conditional-fiber-frame-structure-proof-review.md), and
[route brief](../kls/routes/conditional-fiber-frame.md).

### CMH semantic repairs

The weighted Hodge identity now has a closed-operator formulation with
$L^2_0=(\ker\mathcal A_1)^\perp$ and
$\mathcal A_1^{-1}:L^2_0\to\operatorname{Dom}(\mathcal A_1)\cap L^2_0$. Its orthogonality,
minimality, affine-Poincar\'e Rayleigh identity, and one-dimensional no-flux consequence passed
a supplementary review. The Gamma completion now explicitly derives its Laguerre generator and
Bochner identity from the canonical product-Gamma moment Hessian, with the ordered-pair Hessian
normalization checked independently. See the
[Hodge review](../reviews/2026-08-27-prop-cmh-hodge-domain-repair-proof-review.md) and
[Gamma review](../reviews/2026-08-27-lem-cmh-gamma-bochner-repair-proof-review.md).

## Route conclusions

### Eldan localization

The raw soft-projector contraction proposed for `q:upgrade` is analytically false. A Gaussian
halfspace cylinder with arbitrarily many independent one-sided-exponential spectators has zero
spectator source but positive raw $D^2\chi/D\chi$ injection growing with dimension. This does
not refute `ass:tight-prefix-carleson`, `q:upgrade`, or KLS: the omitted terminal and favorable
drift terms cancel the spectators. The live gate is now a spectator-cancelling cut-relative or
net-injection estimate with a strict damping surplus. See the
[singleton trace-cluster probe](2026-08-27-kls-route-prober-tight-prefix-soft-projector-w3p01.md).

For the weighted branch, the cut-oriented scale $\lambda_{\rm cut}$ passes exact direct-sum
cylinder tests but is discontinuous under arbitrarily small cross-block leakage:

$$
\lambda_{\rm cut}(\operatorname{diag}(1,L),\varepsilon E_{12}^{\rm sym})
=\frac{1+L}{2}\qquad(\varepsilon\ne0).
$$

The preferred unproved interface is source-screened: charge weighted excess only on the aligned
set $Q_t\ge\kappa e_tW_{\rm cut}$ and return an absorbable $\theta Q_t$ off that set, with
$2\beta/(1-\theta)+64\eta^2<1$. See the
[weighted replacement probe](2026-08-27-kls-route-prober-cut-local-weighted-replacement-w3.md).

`q:stein-weighted` is now stated as the actual stopped integral inequality, not as the proposed
Jacobi--Reilly mechanism. It remains an independent open ingredient with no viable KLS consumer
until a tensor-stable propagation package is supplied. No implication among `q:upgrade`, the
high-rank part of `q:stein-weighted`, and `q:alignment` was added.

### Deterministic moment-map / CMH

The linear recovery probe isolates an anisotropic source-retention gate. On a regular isotropic
source, the candidate matrices satisfy

$$
\mathsf N=\mathsf D+\mathsf R,
\qquad
\mathsf N-I\preceq\mathsf D,
$$

so $\mathsf R\succeq\rho\mathsf N-\beta I$ would imply
$Q_{\rm lin}\le(1+\beta)/\rho$. The scalar Chen--Klartag cyclic square has no pointwise Loewner
promotion, as witnessed by an explicit two-dimensional local jet. Published stability results
control potentials, source measures, or almost-everywhere gradients, not the required canonical
Hessian energy. Universal linear recovery is therefore neither proved nor refuted. See the
[probe](2026-08-27-kls-route-prober-cmh-linear-recovery-w3c01.md) and
[literature audit](2026-08-27-literature-scout-cmh-hessian-recovery-w3l01.md).

Proof mining also recovered exact exponential--Gaussian and Dirichlet aggregation deficits,
including the candidate bound
$C_{\rm CMH}(\operatorname{Dir}(k,\ldots,k))\le2(k+1)/k$ before the existing $s_A$ surplus.
These are proof-ready but deliberately unpromoted at the cost boundary. See the
[mining record](2026-08-27-proof-miner-cmh-transverse-deficit-w3t01.md).

### Novel boundary route

The mechanism-distinct `cone-boundary-spectral` idea is registered as a probe, not a live ledger
route. It survived its prescribed cheapest kill: normalized boundary measure on isotropic right
cones has $C_P\le425/12$, and a diagonal family of smooth strictly convex isotropic roundings has
$C_P\le425/6$. The next wall is a dimension-free multi-facet or product seam-capacity estimate.
No theorem or new KLS implication is certified at this checkpoint. See the
[route scout](2026-08-27-kls-route-scout-novel-w2n01.md) and
[cone probe](2026-08-27-kls-route-prober-cone-boundary-spectral-w3b01.md).

## Explicitly parked work

The following proof-ready candidates are recorded but not admitted as ledger nodes or dispatched
to new agents:

- the spectator obstruction to the raw soft-projector injection;
- the CMH linear-bootstrap reduction;
- the exponential--Gaussian transverse deficit and general subcritical product deficit;
- the Dirichlet aggregation-deficit theorem;
- the analytic right-cone boundary-gap theorem;
- a source-screened weighted propagation package.

Parking these items is intentional. Each has a complete handoff in its exploration, so a future
campaign can restart without repeating this wave, while the current branch ends at a clean cost
boundary.

## Validation

- `python3 research/check_ledger.py`: 195 nodes, 675 labels, 0 errors; KLS counts are
  16 conditional, 2 defined, 15 imported, 25 open, 61 proved, and 2 refuted.
- `python3 research/check_agents.py`: 0 errors across 13 roles.
- `python3 -m unittest discover -s research/tests -p 'test_*.py'`: 42 tests passed.
- `git diff --check`: clean.
- Full manuscript build: successful, 161 pages.
- Standalone builds: stopped bootstrap (4 pages), conditional-fiber structure (6 pages), CMH
  normalization (6 pages), and CMH exact cases (6 pages), all successful with only the expected
  cross-manuscript reference warnings in standalone mode.
