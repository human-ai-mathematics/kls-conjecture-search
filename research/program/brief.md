---
target: conj:kls
---

# Problem brief

The harness remembers, validates and certifies; it does not supply mathematical pressure.
This file does: it knows how the target usually fails, what would count as finishing, and
which disguises a dead route wears. It owns none of the mathematics — the statement lives in
`modules/`, its status in the ledger.

## The target

Bizeul–Klartag–Lehec's proof in arXiv:2610.05474v1 (4 October 2026)
has been reconstructed and certified through independent agent reviews.
`conj:kls` is now proved here, through `thm:bkl-tilt-criterion`,
`thm:bkl-cumulant-bound` and `thm:bkl-tilt-bound`. The current composition review is
`research/reviews/2026-10-06-kls-proof-dependency-extension-review.md`;
the earlier `2026-10-06-bkl-kls-second-proof-review.md` is retained as history. This is local
agent certification, distinct from refereed publication. The remaining
programme concerns alternative proofs and structural inequalities.

Song–Zhang arXiv:2610.01447v2 (4 October 2026) supplies a second source
proof, reconstructed and independently checked as `thm:sz-v2-kls`.
Its separate composition into `conj:kls` is currently recorded in
`research/reviews/2026-10-06-kls-proof-dependency-extension-review.md`;
the original `2026-10-06-sz-v2-kls-composition-review.md` remains in the history. The final
profile estimates are checked in
`research/reviews/2026-10-06-sz-v2-profile-review.md`. The two proofs share
earlier spectral foundations but use distinct closing mechanisms. The v1
citation and certified statements retain their original meanings. The SZ v2
chain uses neither `conj:kls`, BKL nodes, nor their consequences as inputs. In particular the proved
`cor:bkl-uniform-conditional-initialization` cannot initialize an independent
SZ v2 proof. Common analytic and polynomial foundations can be reused after
checking exact hypotheses. Pointwise finiteness of the coefficient radius
in `prop:sz-v2-common-radius` must not be confused with a uniform bound.

Balasubramanian–Kasiviswanathan supplies a third source proof, reconstructed
and independently reviewed as `thm:bk-explicit-poincare`, with explicit
constant $1+2\cdot10^{16}$. Its separate composition into `conj:kls` is recorded
in `research/reviews/2026-10-06-bk-kls-composition-review.md`. The source commit
and PDF hash are pinned in the BK integration checkpoint. The reconstruction
uses no KLS, BKL, SZ v2 or their consequences as inputs; it shares Appell
conventions and the certified quadratic inequality of Letwin. Its Hodge
estimate on compatible tensors and common integration-power prefactor are
distinct from the existing CMH Hodge analysis. No existing alternative
mechanism is settled by this integration. This is local independent agent
review, not journal refereeing.

`conj:kls`, stated at `:label: conj:kls` in the overview — read it there; this
file never copies it.

Three formulations are used interchangeably, and the manuscript fixes their equivalence: the
isotropic form of `conj:kls`, the affine form `eq:kls-affine`, and the geometric form
$\inf_n h^*_n>0$ via `eq:hstar-def`. The two-sided comparison `eq:cheeger-two-sided`
($\tfrac14\le\Psi^2/C_P\le\pi$) is what makes the Poincaré and Cheeger statements
interchangeable.

Where the statement is vulnerable is in its conventions, the most common source of an apparent
contradiction with a quoted result. `rem:psi-convention` fixes the $\psi$/$h$ normalization — an
exponent quoted from the literature is meaningless without it. `def:qcts` and `def:cmh` fix the
quadratic-chaos and canonical-moment-Hessian quantities in which the fixed-cut archive and the
moment-map mechanism are stated.

## The exact negation

$$\forall C<\infty\ \exists n\ge1,\ \exists\ \mu\ \text{isotropic log-concave on }\mathbb R^n,\
\exists f \text{ locally Lipschitz}:\quad \operatorname{Var}_\mu(f)>C\int_{\mathbb R^n}|\nabla f|^2\,\mathrm d\mu.$$

Equivalently $\sup_n C_{\mathrm P,n}=\infty$, equivalently $\inf_n h^*_n=0$.

**The quantifier order decides the shape of the refutation, and here it is the hard shape.** The
constant is universally quantified in front. So a single measure, a single test function, or any
finite battery refutes nothing whatever the numbers say. A refutation requires a **certified
family** $(\mu_n)$ with the ratio in `eq:kls-affine` shown to diverge (`SPECIFICATION.md`,
*Refutation*). A lower bound on $C_P(\mu)$ at fixed $n$ is not a divergence. The certified BKL proof rules out such a divergent family. This negation remains
an audit tool for checking conventions and purported counterexamples.

## What counts as complete

Certifying the target and completing the research programme are distinct.
After `conj:kls` is proved, alternative proofs and structural inequalities may
remain active objectives. A sufficient condition is not automatically established
by the truth of its conclusion. No CMH, occupation, or conditional-fiber premise
is discharged by the BKL announcement alone.

**A complete proof** establishes `conj:kls`, or equivalently the affine form for every
log-concave measure. The following are real advances and are *not* completion; each is named by
the node that currently instantiates it, so the list stays checkable:

| does not complete the target | instantiated by |
|---|---|
| any dimension-dependent bound | `cor:loglog`, `thm:klartag-logn`, `thm:letwin-kls`, `thm:song-zhang-kls`, `prop:mm-window-occupation` ($C_P\le C\log^2 n$) |
| an implication whose antecedent is open | `cor:dichotomy`, `prop:spectral-sufficiency`, `prop:cmh-approximation-closure`, `cor:cmh-recovery-sequence-suffices` — all `proved` with a non-empty `assumes` |
| a restricted subclass | `thm:cmh-1d`, `thm:cmh-product`, `thm:cmh-dirichlet`, the exponential cones of `cor:cube-cone-gate-zero` (linear sector only), the regular-approximant class, the regular split class of `prop:split-screened-supply`, the strongly log-concave case |
| a sufficient-condition surrogate proved without its bridge | CMH — its bridge `thm:cmh-implies-affine-poincare` *is* certified, so an independent proof of $\mathrm{CMH}(4)$ would yield another proof of the target; the fiber route's bridge is `lem:conditional-fiber-form` |

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
   $\Lambda_{m,2}\ge(m+2)(m+3)/(5m^2)$. More generally, `lem:fiber-polynomial-floor` gives
   $\Lambda_{m,k}\ge3/[k(k+1)^2(k+2)]$ for every fixed degree $k$ and every $m\ge2$.
   No fixed-degree polynomial upper certificate can refute the all-frame gate asymptotically;
   degree must grow with dimension, or tests must be nonpolynomial.
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
   fully explicit. `prop:product-simplex-cone-gate` now proves the sharp linear bound on
   all product-simplex bases (intervals included), with the complete equality set.
   This does not control nonlinear CMH tests or arbitrary convex bases.
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
2. **A KLS-sufficient covariance input** (`rem:relative-ceiling`, from `prop:ceiling`). A universal
   all-measure $\Xi_{T_0}\le\kappa T_0$ bound at sufficiently small fixed time implies KLS.
   No converse or equivalence is established. Proving this bound would be a sufficient-condition
   route; its failure would not refute KLS. Distinguish it from near-worst weighted propagation
   and from the actual excess controlled by the bootstrap.
3. **Crude bootstrap** (`rem:crude-insufficient`). $\Xi_T\lesssim\log n$ is too large at known
   lower-bound scales; the available polylogarithmic technology reaches only `cor:loglog`.
4. **Projection ceiling** (`rem:projection-ceiling`). Radial and projection-only tests lose a logarithm;
   dimension-free quadratic-chaos control needs tensor-aware information.
5. **Keep the mechanism of a reduction explicit.** `eq:kls-implies-thin-shell`
   records the direct KLS-to-thin-shell argument. BKL now proves KLS independently
   of an assumed thin-shell conclusion; citing that theorem is not a new mechanism
   converting the radial variance bound alone into a spectral estimate.
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
    not by itself a proof of either assertion without its premise. BKL now
    establishes the coefficient assertion by a separate mechanism. Its one coefficient
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

- `thm:bkl-cumulant-bound`, `prop:bkl-suspension`, `thm:bkl-tilt-bound` and
  `thm:bkl-tilt-criterion` — the certified BKL import, with explicit analytic
  foundations and inverse-covariance dynamics. Its proof records identify the
  independently checked scope; the source and its version remain explicit.
- `prop:bkl-tilt-appell-duality` — the precise comparison with the existing
  Appell coefficients, separating identification of the endpoint from the
  mechanism that establishes it.
- `cor:bkl-uniform-conditional-initialization` — the certified unconditional
  consequence for all degrees. Its BKL provenance must remain visible: using
  it to obtain KLS is not an independent alternative to BKL. Neither this
  consequence nor the coefficient bound supplies every comparison estimate
  in the older iteration.

- `prop:sz-exponential-coefficients-equivalence` — an exact quantitative
  reformulation of the target in the full Appell hierarchy. It identifies the
  required improvement over `thm:sz-polynomial-variance`; it does not establish
  the uniform coefficient premise by itself. BKL now establishes that premise;
  an independent route still needs its own mechanism.
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
  the moment-map programme on linear tests. The constant-four gate is necessary for
  $\mathrm{CMH}(4)$; the sharp form at two is stronger. Refuting the constant-four gate
  falsifies that CMH target without touching KLS, whereas refuting the sharp form alone
  does not.
- `conj:trace-upgrade` — the tight-prefix operator-to-trace upgrade that would carry the fixed-cut route.
- `conj:conditional-fiber-frame` — a universal form gap for one test-independent frame, which
  implies the target through `lem:conditional-fiber-form`.

## Budget policy

- **Preserve viable alternatives.** In this programme an existing open route is
  not closed because another proof succeeds or because its priority decreases.
  Record accomplished objectives separately from certified obstructions to a
  particular attempt. Repeated failures and elapsed time prove no impossibility.
- **Truth and provenance, not a prescribed outcome.** An unresolved reconstruction
  records the exact gap; a certified proof records its source and dependencies.
  A proved target need not end research on alternative proofs or stronger
  properties. A lack of priority never certifies impossibility.
- **Waves.** Work is organized in waves: no route runs without a stated gate, and a wave ends in a
  synthesis checkpoint plus the route changes it justifies.
- **An interruption is a harness event, not a mathematical outcome.** A rate limit or a crash
  changes no status; the resume queue belongs in a checkpoint.
- **Numerical budget.** Runs are directional evidence and are never a stopping criterion. Check a
  statement's open `bounded_by` fences — its heuristic barriers — before spending one.
- **What a new route owes before it enters the portfolio.** A thesis — the mechanism, in one
  sentence; a first precise target, written so it could be a ledger node today; its boundary
  against the obstruction set, fence by fence; an explicit statement of whether it is
  *sufficient* or *equivalent* — a sufficient condition has no claimed converse without proof
  (trap 2), and an actual equivalence still needs a distinct mechanism (trap 11); and the
  fastest way to kill it. The classical needles,
  transport, Bochner/$H^{-1}$ and parallel-coupling approaches surveyed in `sec:family-needles`–`sec:family-coupling` are the landscape this program
  works against, not routes; the polynomial–curvature frontier of `sec:polynomial-curvature` is
  not a fifth approach; the routes on its loss live in the portfolio.
