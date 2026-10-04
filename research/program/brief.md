---
target: conj:kls
---

# Problem brief

The harness remembers, validates and certifies; it does not supply mathematical pressure.
This file does: it knows how the target usually fails, what would count as finishing, and
which disguises a dead route wears. It owns none of the mathematics — the statement lives in
`modules/`, its status in the ledger.

## The target

`conj:kls`, stated at `:label: conj:kls` in `modules/00-overview.md` — read it there; this
file never copies it.

Three formulations are used interchangeably, and the manuscript fixes their equivalence: the
isotropic form of `conj:kls`, the affine form `eq:kls-affine`, and the geometric form
$\inf_n h^*_n>0$ via `eq:hstar-def`. The two-sided comparison `eq:cheeger-two-sided`
($\tfrac14\le\Psi^2/C_P\le\pi$) is what makes the Poincaré and Cheeger statements
interchangeable.

Where the statement is vulnerable is in its conventions, the most common source of an apparent
contradiction with a quoted result. `rem:psi-convention` fixes the $\psi$/$h$ normalization — an
exponent quoted from the literature is meaningless without it. `def:qcts` and `def:cmh` fix the
quadratic-chaos and canonical-moment-Hessian quantities that two of the four routes are stated
in.

## The exact negation

$$\forall C<\infty\ \exists n\ge1,\ \exists\ \mu\ \text{isotropic log-concave on }\mathbb R^n,\
\exists f \text{ locally Lipschitz}:\quad \operatorname{Var}_\mu(f)>C\int_{\mathbb R^n}|\nabla f|^2\,\mathrm d\mu.$$

Equivalently $\sup_n C_{\mathrm P,n}=\infty$, equivalently $\inf_n h^*_n=0$.

**The quantifier order decides the shape of the refutation, and here it is the hard shape.** The
constant is universally quantified in front. So a single measure, a single test function, or any
finite battery refutes nothing whatever the numbers say. A refutation requires a **certified
family** $(\mu_n)$ with the ratio in `eq:kls-affine` shown to diverge (`SPECIFICATION.md`,
*Refutation*). A lower bound on $C_P(\mu)$ at fixed $n$ is not a divergence. The manuscript
records that no family is known which forces that ratio to grow, and that the entire remaining
gap is in the upper bound.

## What counts as complete

**A complete proof** establishes `conj:kls`, or equivalently the affine form for every
log-concave measure. The following are real advances and are *not* completion; each is named by
the node that currently instantiates it, so the list stays checkable:

| does not complete the target | instantiated by |
|---|---|
| any dimension-dependent bound | `cor:loglog`, `thm:klartag-logn`, `thm:letwin-kls`, `thm:song-zhang-kls`, `prop:mm-window-occupation` ($C_P\le C\log^2 n$) |
| an implication whose antecedent is open | `cor:dichotomy`, `prop:spectral-sufficiency`, `prop:cmh-approximation-closure`, `cor:cmh-recovery-sequence-suffices` — all `proved` with a non-empty `assumes` |
| a restricted subclass | `thm:cmh-1d`, `thm:cmh-product`, `thm:cmh-dirichlet`, the exponential cones of `cor:cube-cone-gate-zero` (linear sector only), the regular-approximant class, the regular split class of `prop:split-screened-supply`, the strongly log-concave case |
| a sufficient-condition surrogate proved without its bridge | CMH — its bridge `thm:cmh-implies-affine-poincare` *is* certified, so $\mathrm{CMH}(4)$ would close the target; the fiber route's bridge is `lem:conditional-fiber-form` |

**A complete refutation** negates the exact quantified statement through a certified dossier:
the refuter is an ordinary `proved` node appearing in the target's `refuted_by` and never in its
`depends_on`, with a standalone dossier and an independent review. A run is never a step in it;
an exact witness a run finds is a candidate until checked by hand in the dossier.

**Refuting a route is not refuting the target, and this has already happened once.**
`conj:weighted-excess-rate` and `ass:weighted-package` are `refuted` by `prop:weighted-spectator-obstruction`,
whose own witnesses satisfy a dimension-free KLS bound. Likewise `cor:cmh-hodge-comparison`:
refuting $\mathrm{CMH}(4)$ would close the CMH route without touching `conj:kls`.

## Edge cases and audit tests

The calibration and stress instances with an analytic oracle or a named failure mode are
registered in [`research/lib/instances.md`](../lib/instances.md), next to the code that emits
them; this section is the reasoning a new route needs before it runs anything.

1. **Anisotropic Gaussian two-tail cut** (`rem:two-tail-slice-bounds`, from `prop:two-tail`). $r=D=0$ while
   the Stein source is order $\Lambda^2$ and the excess order $\Lambda^{-1/2}$. Any slice-wise
   absolute-scale estimate dies here, and covariance weight at least
   $(1+\lVert A\rVert_{\mathrm{op}})^{5/2}$ is forced.
2. **Gaussian halfspace cylinder with many one-sided-exponential spectators.** $B=G=0$ in every
   spectator block, yet the injection grows linearly in the number of spectators. Every weighted
   or cut-relative estimate must be spectator-inert.
3. **Perturbative instability of the cut-local scale.**
   $\lambda_{\rm cut}(\mathrm{diag}(1,L),\varepsilon E_{12}^{\rm sym})=(1+L)/2$ for every
   $\varepsilon\ne0$. Exact cylinder and direct-sum tensorization is not evidence of stability;
   test cross-block leakage. The scale is singular at $t=0$ and uses the Moore–Penrose convention
   for singular $A$.
4. **Single-coordinate balanced product cuts self-extinguish** (`rem:single-coordinate-cuts`, from
   `cor:single-coordinate-cuts`): total expected source budget at most $1$. An occupation counterexample must
   use high-complexity cuts.
5. **Isotropic simplex with the $A_{m-1}$ root frame.** The root-frame gap is $O(m^{-2})$
   (`prop:conditional-fiber-root-obstruction`), while the exact degree-two dual floors give
   $\Lambda_{m,2}\ge(m+2)(m+3)/(5m^2)$. No degree-two certificate can refute the all-frame gate;
   a fixed-degree refuter needs degree at least three.
6. **Conventions that must be stated or the estimate is not a statement.** $0\le\chi\le1$ and
   $\chi'\ge0$ for any retained cutoff; affine-support degeneration in the approximation limit;
   the regular class boundary, with non-smooth laws admissible only as boundary calibrations.
7. **Exponential cone measures** (`def:exponential-cone`, `prop:cone-linear-sector`). The law
   with density $\propto x_1^{\beta-n}e^{-x_1}$ on the cone over a centered convex body $K$ has
   an explicit moment map (`prop:cone-moment-map`) and, for every base $K$, saturates the sharp
   linear-sector inequality of `conj:gate-zero-sharp` in its axis direction exactly when
   $\beta=n$, with the directional third moment attaining $\lVert T_3(e_1)\rVert_{\mathrm{HS}}=2$.
   They are the non-product equality cases of the sharp gate. Any gate-zero or CMH argument
   must survive them; any sharp-constant claim must be tight on them. The cube-cone kernel is
   fully explicit, and the first exact sweep found no violation and no $\mathrm{CMH}(4)$ pressure
   from the base.
8. **The five failure lenses a refutation attempt should sweep**, one per attempt and blind to
   the others: remote curvature loss and saturating likelihood (tail); separated scales and
   operator-versus-trace gaps (anisotropy); polynomial tails where Poincaré survives but stronger
   inequalities fail (heavy tail); metastable wells and symmetry-versus-physical barriers
   (multimodality); reparameterization and scale-mixing degeneracies (funnel).

## Traps and circular reductions

1. **Circularity** (`rem:profile-circularity`). Excess propagation wants a lower bound on the expected
   isoperimetric profile of the random posterior; the available supermartingale covers a *fixed*
   competitor family while the balanced family moves with time. Inserting the bound directly
   assumes the Cheeger control being proved.
2. **The equivalent-strength ceiling** (`rem:relative-ceiling`, from `prop:ceiling`). A universal
   $\Xi_{T_0}\le\kappa T_0$ at small fixed time *already implies KLS*. A route aiming at it has
   replaced the target by a restatement of it. This is the canonical shape to check a new route
   against.
3. **Crude bootstrap** (`rem:crude-insufficient`). $\Xi_T\lesssim\log n$ is too large at known
   lower-bound scales; the available polylogarithmic technology reaches only `cor:loglog`.
4. **Projection ceiling** (`rem:projection-ceiling`). Radial and projection-only tests lose a logarithm;
   dimension-free quadratic-chaos control needs tensor-aware information.
5. **Thin shell is not KLS.** `eq:kls-implies-thin-shell` runs one way; no dimension-free converse
   is known and none is disproved. A thin-shell improvement is not a partial proof of the target.
6. **Sufficient-condition routes prove but cannot refute.** CMH and the conditional-fiber frame
   both carry certified bridges *into* KLS and none out of it.
7. **Static algebra is not the stochastic residue.** The commutator split of
   `prop:letwin-not-gate-zero` is not the high-incidence block, not a moving-projector Itô
   residue, and not the Haar commutator of `conj:mm-square-root-commutator`.
8. **An exact number is still a candidate.** Exact Loewner verdicts emitted by a run refute
   nothing until a reviewed dossier says so.
9. **The sharp linear sector is not the CMH constant.** Gate zero at constant $4$ is what
   $\mathrm{CMH}(4)$ needs; the natural sharp form is `conj:gate-zero-sharp` at constant $2$,
   which refines `conj:gate-zero`, is the operator form of the Chen–Klartag trace bound, and by
   `cor:gate-zero-third-moment` already contains the sharp directional third-moment bound
   $\kappa_n\le2$ that the literature proves only at $2\sqrt2$. A proof of the sharp form is
   therefore at least as hard as a sharp third-moment estimate, and refuting it leaves
   $\mathrm{CMH}(4)$ untouched.

10. **Summable losses require uniform admissibility.** Before using a bounded-product
    improvement of the Song–Zhang iteration, discharge its small-degree initialization
    and curvature-comparison thresholds uniformly in the depth. Merely removing the
    factor four leaves growing thresholds that bounded profile constants cannot meet.
    The exact obstruction and audit tasks are in
    [`2026-10-03-song-zhang-audit-targets.md`](../explorations/2026-10-03-song-zhang-audit-targets.md).
    The conclusion `thm:song-zhang-kls` is not a discharge of CMH, occupation,
    or adaptive trace estimates.

11. **Uniform exponential coefficients already have the strength of KLS.**
    `prop:sz-exponential-coefficients-equivalence` is a certified equivalence,
    not a proof of either assertion without its premise. Its one coefficient
    constant must work simultaneously for every degree, dimension and regular
    isotropic law. Separate constants at each degree or logarithmic depth do
    not meet it. The converse takes the degree limit at one fixed regular
    measure before passing a uniform scalar inequality to approximants.
    Equivalence does not disqualify a proof approach: a distinct mechanism
    and a discriminating intermediate estimate can make a reformulation
    useful. The equivalence alone supplies neither of those.

Two rules are specific to this program. They were constraints P1 and P2 of the v0.1 harness,
and earlier records cite them under those names.

- **P1 — Do not fan out across the trace-upgrade cluster.** `conj:trace-upgrade`, the high-rank part of
  `conj:stein-weighted` and `conj:product-alignment` share one high-rank occupation difficulty, but
  `rem:trace-upgrade-unification` proves no equivalence between them, and
  `rem:gate-zero-trace-upgrade` records that `conj:gate-zero` is related without being known
  equivalent. One owner — the orchestrator — holds the comparison and propagates only proved
  implications. A partial result on one member is not a partial result on another.
- **P2 — An antecedent is discharged, never assumed away.** An implication whose antecedent is
  open is `proved`, with the antecedent in `assumes`. A *route target* is not closed while its
  antecedent is open, so such a node is never reported as progress on `conj:kls`; and emptying
  `assumes` requires the antecedent discharged for every certification mode in use, including
  Lean in the companion `kls-lean` formalization.

## Neighbourhood

- `prop:sz-exponential-coefficients-equivalence` — an exact quantitative
  reformulation of the target in the full Appell hierarchy. It identifies the
  required improvement over `thm:sz-polynomial-variance`; it does not establish
  the uniform coefficient premise or justify a new independent route.
- `thm:song-zhang-kls` — reconstructed from the pinned v1 source and certified
  through independent agent reviews, together with its analytic, polynomial,
  curvature-comparison and iterated-profile dependencies. The affine consequence
  is `cor:sz-affine-poincare`. This is internal proof verification, not a change
  to the source's publication status. No existing CMH, occupation or trace
  antecedent is discharged. See the
  [completed proof-wave checkpoint](../explorations/2026-10-03-sz-wrap-up.md).
- `thm:sz-curvature-transfer` — the reusable interface for applying any improved
  uniform regular curvature profile to general isotropic laws. Its profile is
  evaluated at one deterministic argument; approximation needs no continuity
  or monotonicity of that profile. Improving the input remains a mathematical
  task, not an automatic consequence of the interface.
- `prop:spectral-sufficiency` — proved, with `conj:mm-spectral-occupation` in `assumes`: the
  fixed-eigenfunction occupation estimate implies `conj:kls`, so settling
  `conj:mm-spectral-occupation` settles the target on that side.
- `thm:cmh-implies-affine-poincare` — proved: $\mathrm{CMH}(4)$ implies the affine Poincaré
  bound, which with `prop:cmh-approximation-closure` and a discharged `ass:uniform-cmh-approximants` or
  `ass:cmh-recovery-envelope` would close the target.
- `conj:gate-zero` and `conj:gate-zero-sharp` — the cheapest necessary consequences of
  $\mathrm{CMH}(4)$ on linear tests; the sharp form refines the other, and either falsifies the
  CMH route without touching the target.
- `conj:trace-upgrade` — the tight-prefix operator-to-trace upgrade that would carry the fixed-cut route.
- `conj:conditional-fiber-frame` — a universal form gap for one test-independent frame, which
  implies the target through `lem:conditional-fiber-form`.

## Budget policy

- **Terminate on saturation, never on a clock.** A route closes in a checkpoint that records the
  obstacle and what would reopen it; saturation is a judgment, never inferred from attempt counts
  or elapsed time.
- **The honest terminal state is "unresolved, with certified advances and exact remaining gaps".**
  That is the current state, and it is a result, not a failure.
- **Waves.** Work is organized in waves: no route runs without a stated gate, and a wave ends in a
  synthesis checkpoint plus the route changes it justifies.
- **An interruption is a harness event, not a mathematical outcome.** A rate limit or a crash
  changes no status; the resume queue belongs in a checkpoint.
- **Numerical budget.** Runs are directional evidence and are never a stopping criterion. Check a
  statement's open `bounded_by` fences — its heuristic barriers — before spending one.
- **What a new route owes before it enters the portfolio.** A thesis — the mechanism, in one
  sentence; a first precise target, written so it could be a ledger node today; its boundary
  against the obstruction set, fence by fence; an explicit statement of whether it is
  *sufficient* or *equivalent* — a route that lands on an equivalent-strength statement has
  renamed the problem (trap 2); and the fastest way to kill it. The classical needles,
  transport and Bochner/$H^{-1}$ approaches surveyed in `modules/01`–`05` are the landscape this
  program works against, not routes.
