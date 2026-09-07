---
type: brief
target: conj:kls
---

# Problem brief

The harness remembers, validates and certifies. It does not supply mathematical pressure. That is
this file's job: it is the one document that knows how the target usually fails, what would count
as finishing, and which disguises a dead route wears.

| what | where |
|---|---|
| the canonical quantified target | `../../modules/kls/00-orientation.tex`, under `\label{conj:kls}` |
| its identity, status, provenance and relations | [`ledger.yaml`](ledger.yaml) |
| what the search is doing about it | [`portfolio.yaml`](portfolio.yaml) |
| its negation, completion criteria, edge cases, traps and search policy | this file |

## The target

The blockquote is a **copy, not a source**: if it and the manuscript disagree, the manuscript is
right and the copy is the defect, which is what the `reviewer`'s `sync` lens checks. Never sharpen
the statement here — sharpen it in `modules/` and re-copy.

> **Target** `conj:kls`, stated at `\label{conj:kls}` in
> [`../../modules/kls/00-orientation.tex`](../../modules/kls/00-orientation.tex):
>
> There is a universal constant $C<\infty$ such that, for every dimension, every isotropic
> log-concave $\mu$, and every locally Lipschitz $f$,
> $\Var_\mu(f)\le C\int_{\R^n}|\nabla f|^2\dd\mu$.
> Equivalently up to universal constants, the Cheeger constants of all such measures are bounded
> below uniformly in the dimension.

Three formulations are used interchangeably, and the manuscript fixes their equivalence: the
isotropic form above, the affine form `eq:kls-affine`, and the geometric form
$\inf_n h^*_n>0$ via `eq:hstar-def`. The two-sided comparison `eq:cheeger-two-sided`
($\tfrac14\le\Psi^2/C_P\le\pi$) is what makes the Poincaré and Cheeger statements interchangeable.

Two conventions do real work and are the most common source of an apparent contradiction with a
quoted result. `rem:psi-convention` fixes the $\psi$/$h$ normalization — an exponent quoted from
the literature is meaningless without it. `def:qcts` and `def:cmh` fix the quadratic-chaos and
canonical-moment-Hessian quantities that two of the four routes are stated in.

## The exact negation

$$\forall C<\infty\ \exists n\ge1,\ \exists\ \mu\ \text{isotropic log-concave on }\R^n,\
\exists f \text{ locally Lipschitz}:\quad \Var_\mu(f)>C\int_{\R^n}|\nabla f|^2\dd\mu.$$

Equivalently $\sup_n C_{\mathrm P,n}=\infty$, equivalently $\inf_n h^*_n=0$.

**The quantifier order decides the shape of the refutation, and here it is the hard shape.** The
constant is *not* fixed in the statement: it is universally quantified in front. So a single
measure, a single test function, or any finite battery refutes nothing whatever the numbers say.
A refutation requires a **certified family** $(\mu_n)$ with the ratio in `eq:kls-affine` shown to
diverge — see `CLAUDE.md` constraint 10. A lower bound on $C_P(\mu)$ at fixed $n$ is not a
divergence. The manuscript records that no family is known which forces that ratio to grow, and
that the entire remaining gap is in the upper bound.

## What counts as complete

**A complete proof** is the statement above, or equivalently the affine form for every log-concave
measure. The following are real advances and are *not* completion; each is named by the node that
currently instantiates it, so the list stays checkable:

| does not complete the target | instantiated by |
|---|---|
| any dimension-dependent bound | `cor:loglog`, `thm:klartag-logn`, `prop:mm-window-occupation` ($C_P\le C\log^2 n$) |
| an implication whose antecedent is open | `prop:spectral-sufficiency`, `q:cmh-approximation`, `cor:cmh-recovery-sequence-suffices`, `lem:mm-stopped-window-source`, `prop:mm-window-occupation` — all `proved` with a non-empty `assumes` |
| a restricted subclass | `thm:cmh-1d`, `thm:cmh-product`, `thm:cmh-dirichlet`, the exponential cones of `cor:cube-cone-gate-zero` (linear sector only), the regular-approximant class, the regular split class of `prop:split-screened-supply`, the strongly log-concave case |
| a sufficient-condition surrogate proved without its bridge | CMH — its bridge `thm:cmh-implies-affine-poincare` *is* certified, so CMH(4) would close the target; the fiber route's bridge is `lem:conditional-fiber-form` |

A node that is `proved` with a non-empty `assumes` is progress on a *route*, never on the target
(`CLAUDE.md` P2). Emptying `assumes` requires the antecedent discharged in every certification
mode in use, including Lean in the companion `kls-lean` formalization.

**A complete refutation** takes the ordinary channel: the refuter is an ordinary `proved` node
appearing in the target's `refuted_by` and never in its `depends_on`, with a standalone dossier and
an independent review. A numerical artifact is never a step in it (constraint 2); exact arithmetic
emitted by a target is a candidate until checked in the proof workflow.

**Refuting a route is not refuting the target, and this has already happened once.** `q:weighted`
and `ass:weighted-package` are `refuted` by `prop:weighted-spectator-obstruction`, whose own
witnesses satisfy a dimension-free KLS bound. Likewise `rem:cmh-stronger-than-kls`: refuting
CMH(4) would close the CMH route without touching `conj:kls`.

## Edge cases and audit tests

The calibration and adversarial registry is [`../instances.md`](../instances.md); this section is
the reasoning a new route needs before it runs anything.

1. **Anisotropic Gaussian two-tail cut** (`obs:two-tail`, from `prop:two-tail`). $r=D=0$ while the
   Stein source is order $\Lambda^2$ and the excess order $\Lambda^{-1/2}$. Any slice-wise
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
4. **Single-coordinate balanced product cuts self-extinguish** (`obs:rank-one-refuted`, from
   `cor:refutation`): total expected source budget at most $1$. An occupation counterexample must
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
   fully explicit, and the first exact sweep found no violation and no CMH(4) pressure from
   the base.
8. **The five failure lenses a refutation attempt should sweep**, one per attempt and blind to the
   others: remote curvature loss and saturating likelihood (tail); separated scales and
   operator-versus-trace gaps (anisotropy); polynomial tails where Poincaré survives but stronger
   inequalities fail (heavy tail); metastable wells and symmetry-versus-physical barriers
   (multimodality); reparameterization and scale-mixing degeneracies (funnel).

## Traps and circular reductions

1. **Circularity** (`obs:circularity`). Excess propagation wants a lower bound on the expected
   isoperimetric profile of the random posterior; the available supermartingale covers a *fixed*
   competitor family while the balanced family moves with time. Inserting the bound directly
   assumes the Cheeger control being proved.
2. **The equivalent-strength ceiling** (`obs:relative-ceiling`, from `prop:ceiling`). A universal
   $\Xi_{T_0}\le\kappa T_0$ at small fixed time *already implies KLS*. A route aiming at it has
   replaced the target by a restatement of it. This is the canonical shape to check a new route
   against.
3. **Crude bootstrap** (`obs:crude-insufficient`). $\Xi_T\lesssim\log n$ is too large at known
   lower-bound scales; the available polylogarithmic technology reaches only `cor:loglog`.
4. **Projection ceiling** (`obs:proj-ceiling`). Radial and projection-only tests lose a logarithm;
   dimension-free quadratic-chaos control needs tensor-aware information.
5. **Thin shell is not KLS.** `eq:kls-implies-thin-shell` runs one way; no dimension-free converse
   is known and none is disproved. A thin-shell improvement is not a partial proof of the target.
6. **Sufficient-condition routes prove but cannot refute.** CMH and the conditional-fiber frame
   both carry certified bridges *into* KLS and none out of it.
7. **The trace-upgrade cluster** (`CLAUDE.md` P1). `q:upgrade`, the high-rank part of
   `q:stein-weighted` and `q:alignment` share one high-rank occupation difficulty, and
   `rem:trace-upgrade-unification` proves no equivalence between them;
   `rem:gate-zero-trace-upgrade` records `conj:gate-zero` as related but not known equivalent.
   Transferring a partial result across the cluster is the trap; one owner compares them.
8. **Static algebra is not the stochastic residue.** The commutator split of
   `prop:letwin-not-gate-zero` is not the high-incidence block, not a moving-projector Itô
   residue, and not the Haar commutator of `q:mm-square-root-commutator`.
9. **An exact number is still a candidate.** Exact Loewner verdicts emitted by a `numerics` target
   refute nothing until a reviewed dossier says so.
10. **The sharp linear sector is not the CMH constant.** Gate zero at constant $4$ is what
    $\mathrm{CMH}(4)$ needs; the natural sharp form is `conj:gate-zero-sharp` at constant $2$,
    the operator form of the Chen–Klartag trace bound, and by `cor:gate-zero-third-moment` it
    already contains the sharp directional third-moment bound $\kappa_n\le2$ that the literature
    proves only at $2\sqrt2$. A proof of the sharp form is therefore at least as hard as a sharp
    third-moment estimate, and refuting it leaves $\mathrm{CMH}(4)$ untouched.

## Initial families and their reopening criteria

Live state is [`portfolio.yaml`](portfolio.yaml); this section is the reasoning behind the seeding
and the standard a new family must meet.

The four live families are the four routes the manuscript develops: fixed-cut stochastic
localization, fixed-eigenfunction spectral localization, the deterministic moment-map/CMH route,
and conditional-fiber frames. A fifth family holds parked probes that are not yet routes.

**What a new route owes before it becomes a family.** Five things, and the fifth is the one most
often skipped:

1. a thesis — the mechanism, in one sentence;
2. a first precise target, written so it could be a ledger node today;
3. its boundary against the obstruction set, fence by fence, not in general terms;
4. an explicit statement of whether it is *sufficient* or *equivalent* — a route that lands on an
   equivalent-strength statement has renamed the problem (trap 2); and
5. the fastest way to kill it.

There is deliberately no family for the classical needles, transport, or Bochner/$H^{-1}$
approaches surveyed in `modules/kls/01`–`05`. They are the landscape this program works against
rather than open routes: Caffarelli covers only the strongly log-concave case, and the
$H^{-1}$ route's precise missing estimate is recorded in `modules/kls/03` along with why it stalls.

## Budget policy

- **Terminate on saturation, never on a clock.** A family closes with a `closure_checkpoint` and a
  reopening condition, and saturation is a judgment that costs a synthesis checkpoint — it is
  never inferred from attempt counts or elapsed time (constraint 11).
- **The honest terminal state is "unresolved, with certified advances and exact remaining gaps".**
  That is the current state, and it is a result, not a failure.
- **Waves.** Work is organized in waves: no route runs without a stated gate, and a wave ends in a
  synthesis checkpoint plus a portfolio delta.
- **An interruption is a harness event, not a mathematical outcome.** A rate limit or a crash
  changes no status; the resume queue belongs in a checkpoint. Wave four ended this way.
- **Numerical budget.** Runs are directional evidence and are never a stopping criterion. Check a
  statement's `heuristic_barriers` before spending one.
- **No fan-out across a merge barrier.** One owner, comparisons only, proved implications
  propagated (P1).
