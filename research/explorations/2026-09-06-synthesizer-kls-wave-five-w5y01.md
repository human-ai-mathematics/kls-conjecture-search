---
artifacts:
  - research/runs/2026-09-06T175558.606924Z-cmh-cone.jsonl
  - research/runs/2026-09-06T175611.501834Z-cmh-cone.jsonl
  - research/runs/2026-08-30T180751.811560Z-cmh-ab.jsonl
  - research/runs/2026-08-30T173244.394413Z-fiber-frame-dual.jsonl
  - research/runs/2026-08-30T175419.597477Z-kls-screen.jsonl
---

# Synthesizer: wave five converged — portfolio, registry, and the linear sector of Route C

Role `synthesizer`, identity `/w5/synthesizer`, run `w5y01`, holding the singleton `portfolio`
and `instances` keys. Write surface: `research/program/portfolio.yaml`, `research/instances.md`,
this record. No ledger, manuscript, dossier or review file was touched.

This record supersedes nothing. Every wave-five checkpoint is the provenance of a certified
dossier or a run artifact and remains the record to read for that; the orchestrator's
`2026-09-06-orchestrator-kls-cone-lift-wave-w5.md` is the mathematical account of the wave and
this is its search-state counterpart.

## 1. Inputs

The orchestrator record for `w5`; the researcher checkpoints `w5p01`, `w5p04` (cone dossier
and its repair), `w5p02` (third-moment dossier), `w5p03` (spectral-resolution repair); the
numerics record `w5n01`; the literature sweep `w5l01`; the six review files dated 2026-09-06
(two audits, four passing certifications); the wave-four orchestrator record and the
`w4c02` record whose instance proposals were never curated; and the live state from
`check.py status`, `portfolio`, `candidates`, `checkpoints`. Ledger at entry: 138 nodes,
0 errors, nine nodes moved to `proved` today; the portfolio had not yet been told.

## 2. Portfolio delta, route by route

**`ap:fiber-simplex-dual`: `blocked` → `queued`.** Its blocker `lem:fiber-root-degree-two`
is certified (`research/reviews/2026-09-06-lem-fiber-root-degree-two-proof-review.md`, pass),
which is the first disjunct of its own reopen condition. The certified content is negative
for the route as written: every degree-two dual certificate has objective at least
$(m+2)(m+3)/(5m^2)>1/5$, so the objective now reads "degree at least three". No live
candidate states a degree-three certificate, so the route cannot honestly be re-blocked; it
is planned work nobody has started. Rests on
`2026-08-30-prover-fiber-root-degree-two-w4p04.md` (kept in `checkpoints:`).

**`ap:cmh-anisotropic-bootstrap`: `blocked` → `queued`.** Its blocker
`lem:cmh-linear-spectral-resolution` is certified in the weak-column-equation form
(`2026-09-06-lem-cmh-linear-spectral-resolution-proof-review.md`, pass, after the audit that
caught the statement-scope mismatch). The reopen condition was a disjunction and its first
disjunct is met. What was *not* obtained: the strong operator-domain form
$(1-\mathsf A_{\rm op})(Ha)=(A+Q)a$, which the dossier shows is equivalent to
$\Tr Q\in L^2(\eta)$ on the compact-target class and proves only on products; and the
integrated corrector or nonlocal coercivity that the second disjunct asks for. Neither is a
live candidate, so the route is not re-blocked; its objective now says it works from the weak
form and may not assume the strong one. A researcher who wants to block on the strong form
must first state $\Tr Q\in L^2(\eta)$ on the class as a `cand:` — it has no precise home yet
and this record does not invent one. Rests on `w4c01` and `w5p03`, both now listed.

**`ap:cmh-gate-zero`: `queued` → `active`.** Three things changed at once. It has a first
precise target, `conj:gate-zero-sharp`, refining `conj:gate-zero`. It has a certified tool:
`lem:linear-sector-third-moment` splits the gate matrix's quadratic form into
$1+\tfrac14\|T_3(a)\|_{\mathrm{HS}}^2+\E|v_a|^2$, and `cor:gate-zero-third-moment` turns any
gate-zero constant into a directional third-moment bound. And it has an equality set with an
exact decision procedure: `def:exponential-cone`, `prop:cone-moment-map`,
`prop:cone-linear-sector`, `cor:cube-cone-gate-zero` (all certified) plus the `cmh-cone`
battery, which decides the Loewner test by rational $LDL^\top$ in both directions. The
objective is rewritten to name the sharp form first. Rests on `w5p01`, `w5p04`, `w5p02`,
`w5n01`, `w5l01` and this record, all now listed.

**`ap:cmh-solenoidal-perturbation`: stays `queued`, objective re-aimed.** Two records say the
base direction is spent. `w4c02` §3.4: a moment-potential perturbation of the saturator leaves
the log-concave class for both signs (219 of 342 instances `violated`; the $4.052$ near-miss is
the fence `fence-cmh-m9-boundary` below), so an admissible perturbation must be target-side.
`w5n01` channel 4: realising a base perturbation as an exponential cone over a polytopal base
puts the CMH Galerkin quotient strictly *below* the exponential product at every degree
tested, with the gap growing in $n$ and in $\beta-n$, and channel 2 finds the gate spectrum
of every product base strictly below $2$ off the axis. Every quantity that touches $2$ or $4$
in this family is the Gamma factor's. The objective now says "target-side, radial Gamma
factor rather than the base". No checkpoint declares this approach, so none can be attached;
the reasons are here. Nothing here resolves `q:cmh-solenoidal-perturbation`.

**Relations added.** `ap:cmh-gate-zero` `overlaps` `ap:cmh-anisotropic-bootstrap`: the
certified `lem:cmh-linear-spectral-resolution` writes $a^\top\mathsf Na=1+|M_a|^2+|v|^2$ and
`lem:linear-sector-third-moment` writes the same column energy as
$1+\tfrac14\|T_3(a)\|^2+\E|v_a|^2$ — one object, two certified decompositions, two routes.
`ap:cmh-gate-zero` `overlaps` `ap:cmh-solenoidal-perturbation`: the cone battery's Galerkin
channel is the instrument both use. The pre-existing `overlaps` with `ap:eldan-trace-upgrade`
stays as a coordination note and asserts nothing (P1; §5).

**Sweep of everything else.** No duplicates found: the two audit-then-review sequences were
sequential repairs, not parallel attacks on one shape. No family closes: `fam:mm-cmh` has one
active route plus one now-active route and five queued; `fam:conditional-fiber` has one active
and one queued; `fam:mm-spectral` one active and one completed; `fam:eldan-localization` two
active, three queued, one blocked; `fam:novel-routes` stays `parked` on its two candidates,
which nothing has picked up in two waves. Saturation is declared nowhere.

## 3. Instance registry

Fourteen proposals curated into `research/instances.md`. All fourteen were accepted; the
reasons, and the two curation decisions that were not pure acceptance, follow. The `numerics`
column names emitted ids read from the artifacts, not the ids the proposals used, wherever the
two differ.

| proposed | decision | reason |
|---|---|---|
| `stress-fiber-frame-simplex-pencil` (w4f01) | accept, and **split**: a calibration row `cal-fiber-root-degree-two` added | the exact floor $(m+2)(m+3)/(5m^2)$ is now the certified `lem:fiber-root-degree-two`, so the target's `cal-root-anchors-m{m}-k2` records have an analytic oracle; the stress row keeps the $k\ge3$ pencil and the directional `sph-` frame |
| `stress-tailunion-cut-scale` (w4a01) | accept | the model on which the cut-local repair provably buys nothing; not a happy path for any route |
| `stress-cylinder-spectator-excess` (w4a01) | accept | separates weight stability from excess stability; the `kls-screen` target emits no instance ids, so the row cites the `model` field — a harness defect noted in §7 |
| `stress-cmh-ab-exponential-limit` (w4c02) | accept, not merged into `dir({alpha})` | the generic Dirichlet row records gate-zero ratios; this row's property is the lockstep approach to the $(\mathrm{AB})$ equality case inside the compact-target class, which the cone battery (outside that class) cannot supply |
| `stress-cmh-ab-reservoir-split` (w4c02) | accept | adverse to the bootstrap route: shows any proof of $(\mathrm{AB})$ near $\rho=\tfrac12$ must consume target log-concavity |
| `fence-cmh-m9-boundary` (w4c02) | accept as a fence | the false refutation candidate an averaged admissibility test emits; directly motivates the re-aim of `ap:cmh-solenoidal-perturbation` |
| `cal-cmh-cone-axis`, `cal-cmh-cone-cube-closed-form`, `cal-cmh-cone-simplex-product`, `cal-cmh-cone-ball-1d` (w5n01) | accept | each oracle is a certified node or a closed form derived in a certified dossier; the simplex-product row is cross-referenced to `cal-kls-centered-exp`, the same measure with no backend |
| `cal-cmh-cone-galerkin-chebyshev` (w5n01) | accept **with the oracle marked as a candidate** | $2+2\cos(\pi/(d+1))$ is `cand:cmh-exponential-galerkin-rate`, exact on the line and unproved for the product; a new interpretation rule says a candidate-backed calibration row is provisional and leaves the tier if the candidate is retired |
| `stress-cmh-cube-cone`, `stress-cmh-simplex-product-cone`, `stress-cmh-ball-cone` (w5n01) | accept | they fill the hole the numerics record identified: the CMH battery had no non-compactly-supported instance, none with base geometry as a free parameter, and no non-product instance saturating the sharp linear sector in $n\ge3$; the ball row is quadrature and is marked directional |

The wave-four orchestrator record and the migration record both listed these six as an
open close-out item; that item is closed.

## 4. Live candidates: what would decide each

Six are live. Four were created this wave; none is promoted or retired here, because no
checkpoint gives grounds.

- **`cand:cmh-exponential-galerkin-rate`** (w5n01). The one-dimensional statement is an
  elementary tridiagonal eigenvalue computation on the Laguerre basis and could be a short
  dossier today. What decides the candidate is the product transfer: that no genuinely
  multivariate polynomial of total degree $d$ beats the best univariate one for the product
  quotient. A proof of that (a tensorization argument on polynomial spaces, in the spirit of
  `thm:cmh-product`) promotes it; a single $n=2$ polynomial exceeding
  $2+2\cos(\pi/(d+1))$ at some $d$ retires it and moves the calibration row of §3 to the
  stress tier. The run found none for $n\le4$, $d\le10$.
- **`cand:cone-transverse-equality-simplex`** (w5n01). Its stated reason to doubt — that
  `prop:cone-moment-map` was open — is gone: the node is certified, so every number in the
  sweep is computed from a proved kernel. What remains is the finite-slice issue. By the
  certified kernel the transverse block of the gate matrix of a product base is assembled
  from the blocks' own kernels, and for simplex and interval blocks those are the Dirichlet
  closed forms of `thm:cmh-dirichlet`; the candidate is therefore a finite exact computation
  in $(k_1,\dots,k_r,s,\beta)$, and a researcher can decide it by algebra. That is the
  cheapest promotion on the table.
- **`cand:directional-h-minus-one-two`** (w5l01). Precise and stable; it is the directional
  form of Chen–Klartag Theorem 1.4 and is implied by `conj:gate-zero-sharp` through Letwin's
  Lemma 2.9 (the comparison `eq:stein-hminus1`). Decided by: a proof through the
  Klartag–Lehec directional coupling with a top-eigenvalue control of the covariance process
  (the scout's §4), or a counterexample. It is strictly weaker than the sharp gate because
  it discards the solenoidal channel, so it is a legitimate *intermediate* target for
  `ap:cmh-gate-zero`, and it is ready to be a `conj:` node whenever the orchestrator wants
  the route to be able to block on it; the implication from `conj:gate-zero-sharp` would
  stay prose until a dossier carries the Stein-kernel comparison.
- **`cand:letwin-rank-one-second-moment`** (w5l01). A one-line specialisation
  ($B=vv^\top$) of `thm:letwin-moment-map`, itself an unreviewed-preprint import. It bounds
  the scalar Rayleigh quotient $v^\top\tau v$, which `prop:letwin-not-gate-zero` already
  fences off from the column energy the gate needs. Nothing on the frontier depends on it.
  Decided by: a route citing it (then a corollary node with `depends_on:
  thm:letwin-moment-map`) or one more wave without a citation, after which it should be
  retired as a remark rather than kept as memory.
- **`cand:cone-seam-capacity`**, **`cand:brenier-simplex-hessian`** (migration record,
  2026-09-04). Unchanged; nobody has touched either in two waves. They are what keeps
  `fam:novel-routes` parked and are not pruned here, because nothing has been learned about
  them either way.

## 5. The merge barrier (P1) and the comparison table

Common normalisation: $\mu$ isotropic log-concave, $\tau=\tau_\mu$ its canonical Stein
kernel, $G=\E[\tau^2]$ the gate matrix, $T_3(a)=\E[\langle X,a\rangle X\otimes X]$.

| from | to | status |
|---|---|---|
| `conj:gate-zero-sharp` ($G\preceq2$) | `conj:gate-zero` ($G\preceq4$) | proved (trivial; `refines` in ledger) |
| `conj:gate-zero-sharp` | $\|T_3(a)\|_{\mathrm{HS}}\le2$ for every unit $a$, on the lemma's class | proved (dossier `solutions/lem-linear-sector-third-moment.tex`, `cor:gate-zero-third-moment`) |
| `conj:gate-zero` | $\|T_3(a)\|_{\mathrm{HS}}\le2\sqrt3$ for every unit $a$, on the class | proved (same dossier) |
| directional third-moment bound at $2$ | `conj:gate-zero-sharp` | open — not even conjectured as an equivalence: the remainder $\E|v_a|^2$ is nonzero off the cone axis |
| `conj:gate-zero-sharp` | `cand:directional-h-minus-one-two` | open in this repository (no dossier; Letwin Lemma 2.9 is the cited route, preprint) |
| `conj:gate-zero` or `conj:gate-zero-sharp` | `q:upgrade`, high-rank `q:stein-weighted`, `q:alignment` (either direction) | open; `rem:gate-zero-trace-upgrade` records the shape, no edge |
| $(\mathrm{AB})_{\rho,\beta}$ | linear-sector bound $Q_{\rm lin}\le(1+\beta)/\rho$ | proved (dossier `solutions/lem-cmh-linear-spectral-resolution.tex`, weak form) |
| $\mathsf R_Q\succeq\mathsf D$ (integrated matrix cyclic square) | — | directionally false on `stress-cmh-ab-reservoir-split`; no node, no fence |

What P1 still blocks, in one line: no implication between the gate (sharp or not) and any
member of the trace-upgrade cluster is proved, so the wave's certified gate-side results
transfer nothing to `ap:eldan-trace-upgrade`, `ap:eldan-stein-weighted` or
`ap:eldan-alignment`. `cor:gate-zero-third-moment` is an intra-Route-C implication toward
the third-moment parameter $\kappa_n$ of `prop:letwin-kappa`; it is not a cluster comparison
and is not read as one. The scout's §4.1 (Liu's operator-to-trace upgrade on the space of
symmetric matrices) was checked and does not give the gate; it is reported, not acted on.

**Proposed ledger delta: none.** Every implication in the table marked proved already
carries its edge or is trivially the recorded `refines`; nothing else is warranted.

## 6. Frontier assessment

What the wave established is confined to the linear sector of Route C, and there it is
exact: the gate matrix's quadratic form is a third-moment term plus a named high-mode
remainder, so any gate-zero constant is at least as hard as a sharp directional third-moment
bound; the sharp form $\E[H\Sigma^{-1}H]\preceq2\Sigma$ now has a stated node, an equality set
beyond products (every exponential cone at $\beta=n$, on its axis), an explicit
non-product family (cube cones) on which it is verified in closed form, and an exact battery
of 264 polytopal cones on which it is decided true with the maximum attained at $2$ and never
exceeded. The literature has the trace of the sharp statement and nothing directional. On
the CMH side, the base direction of the perturbation experiment is flat-to-downhill and the
saturation question `q:cmh-solenoidal-perturbation` is untouched. `conj:kls` is untouched:
every certified node is structural or exact-case, none has an `assumes`, and none is
progress on the target (P2). No family is saturated, and the honest state remains
"unresolved, with certified advances and exact remaining gaps", now with one more exact gap
named.

## 7. Where the search is thin, and harness notes

- `fam:mm-spectral` has a single active route; `fam:conditional-fiber` has one active and one
  queued. The brief's standard for a new family (thesis, first target, fence-by-fence
  boundary, sufficient-versus-equivalent, fastest kill) is not met by anything on the table,
  so no family is seeded. Within `fam:mm-cmh` the next route-worthy statement is
  `cand:directional-h-minus-one-two` as an intermediate target; within `fam:conditional-fiber`
  it is a degree-three certificate, which nobody has stated.
- The `kls-screen` target emits no per-instance ids; two registry rows cite its `model` field.
  A `numerics` run touching that target should mint ids so the rows can name them.
- No two agents attacked the same fenced shape this wave; the two audit-then-review sequences
  were repairs, not reruns.
- Non-blocking items carried from the orchestrator record: journal numbering of the
  Cordero-Erausquin–Klartag uniqueness theorem; the `sync` items on module 15 and on the cone
  integrability sentence.
