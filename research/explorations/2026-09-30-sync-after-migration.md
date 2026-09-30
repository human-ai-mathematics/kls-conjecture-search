---
---

# Sync after the v0.3.0 migration

This checkpoint closes the open items of `2026-09-30-migration-v0.3.0.md` and
`2026-09-29-migration-v0.2.0.md`, except the fresh `certify` reviews, which the maintainer
waived for this migration. It changes no status of a remaining node: the ledger now holds
131 nodes (86 proved, 39 open, 4 defined, 2 refuted); the seven nodes removed were `open`.

## Question examined

Do the statements converted from the LaTeX harness, their kinds, labels and ledger edges,
and the prose around them say what the mathematics says — and can the ids be made to name
what each statement is?

## What we learned

Three `reviewer` sub-agents with the `sync` lens (claude-opus-5-5, 2026-09-30, fresh
contexts, no file written) audited: the thirteen converted questions and the sign of the
second variation; the six obstructions and the kinds of the `rem:`/`q:` labels; the
product stress test and the four open implications. A `writer` then updated the prose;
`check.py --statements` was identical before and after its pass.

**Sign of the CMH second variation** (*established*). With $\CMH(\mu)=\sup_g N/D$ and
$\CMH(\mu_0)=4$ at the one-sided-exponential ⊗ Gaussian endpoint, $\mathrm{CMH}(4)$ makes
$\eps=0$ a local maximum of $\eps\mapsto\CMH(\mu_\eps)$ along log-concave perturbations, so
a strictly *positive* second variation refutes $\mathrm{CMH}(4)$. The statement was right
and the gateway of `modules/40-moment-map-cmh.md` wrong, already in the LaTeX. The
statement, now `conj:cmh-second-variation`, requires $\mu_\eps$ log-concave (without it the
conjecture is not implied by $\mathrm{CMH}(4)$) and uses the symmetric second difference,
since the supremum is not attained.

**Kinds and edges.**
- The six obstructions restated proved results (`prop:two-tail`, `prop:ceiling`,
  `cor:single-coordinate-cuts`, `rem:insufficiency`) or were method warnings; none was a
  precise open claim. They are now remarks and left the ledger, with the 22 `bounded_by`
  edges that pointed at them, none redirected: a proved fence would bind, and none of the
  consumers could violate them. Their content stays in the remarks and in the brief's traps.
- The former `rem:gate-zero-trace-upgrade` restated `thm:chen-klartag-moment-hessian`; it
  is a remark and left the ledger.
- `thm:centroid-implies-kls`, `thm:carleson-implies-centroid`, `thm:intro-all-cut` and
  `thm:intro-weighted` are implications whose antecedents were in `depends_on` (one of
  them refuted): the antecedents are now in `assumes`, and `thm:intro-all-cut` rests on
  `cor:tight-window-consumption` (the case $I=[0,T]$, $\eta=1/6$). They stay `open`: the
  manuscript argues them, but no dossier proves them.
- Smaller edges: `conj:taming` no longer depends on `thm:bootstrap` (used only for a
  consequence); `conj:cmh-second-variation` and `conj:mm-square-root-commutator` depend on
  `def:cmh`; `cor:cmh-product-saturation` on `thm:cmh-1d`.

**Statements changed.** `conj:cmh-second-variation` (above);
`conj:mm-square-root-commutator` (“There is $R$” made the inequality trivially true; $R$
is now defined); `prop:cmh-approximation-closure` (states the bound $\CPaff(\mu)\le C$ with
the constant of the assumption, which the dossier's theorem gives); `conj:product-alignment`
(its failure bears on the prefix form only through prefixes, and selects no other
approach); `conj:conditional-fiber-frame` (the constant $C$ is quantified first, as
“universal” meant); `conj:trace-upgrade`, `conj:stein-weighted` and
`conj:weighted-excess-rate` lost the commentary and the statuses of other nodes that sat
inside the statement, now prose after each directive. The kind of seven statements changed
(six conjectures and one corollary to remarks).

**The product stress test** (*established*). A failure of `ass:all-cut-carleson` on
products would force nothing: it bears on `ass:tight-prefix-carleson` only if the
violating intervals are prefixes on the tight window; the literal weighted package is
already refuted on the same product witnesses (`prop:weighted-spectator-obstruction`); and
a fixed single-coordinate cut cannot be a witness (`cor:single-coordinate-cuts`). The
remark `rem:product-stress-test`, `modules/16`, `modules/20`, `modules/22` and
`modules/27` now say so.

**Ids.** At the maintainer's request, and as an exception to the append-only rule made
for this migration only, every id below was replaced throughout the repository —
manuscript, dossiers, ledger, brief, portfolio, checkpoints, reviews, `research/lib/` and
the run outputs — so that the prefix names the kind. Before this checkpoint, the old ids
are readable in git history (commit `1b7550e`).

| old | new |
|---|---|
| `q:alignment` | `conj:product-alignment` |
| `q:cmh-solenoidal-perturbation` | `conj:cmh-second-variation` |
| `q:conditional-fiber-frame` | `conj:conditional-fiber-frame` |
| `q:mm-invariant-lift` | `conj:mm-invariant-lift` |
| `q:mm-spectral-occupation` | `conj:mm-spectral-occupation` |
| `q:mm-square-root-commutator` | `conj:mm-square-root-commutator` |
| `q:splitting` | `conj:splitting` |
| `q:stein-weighted` | `conj:stein-weighted` |
| `q:taming` | `conj:taming` |
| `q:upgrade` | `conj:trace-upgrade` |
| `q:weighted` | `conj:weighted-excess-rate` |
| `rem:almost-stability-gap` | `conj:almost-stability-gap` |
| `q:cmh-approximation` | `prop:cmh-approximation-closure` |
| `rem:cmh-saturation-risk` | `cor:cmh-product-saturation` |
| `rem:cmh-stronger-than-kls` | `cor:cmh-hodge-comparison` |
| `cor:refutation` | `cor:single-coordinate-cuts` |
| `obs:two-tail` | `rem:two-tail-slice-bounds` |
| `obs:proj-ceiling` | `rem:projection-ceiling` |
| `obs:crude-insufficient` | `rem:crude-insufficient` |
| `obs:relative-ceiling` | `rem:relative-ceiling` |
| `obs:circularity` | `rem:profile-circularity` |
| `obs:rank-one-refuted` | `rem:single-coordinate-cuts` |
| `q:cmh-normalization` | `rem:cmh-normalization` |
| `q:literature-PsQs` | `rem:literature-psqs` |
| `q:gate-zero` | `rem:gate-zero-dichotomy` |
| `prog:cmh-route` | `rem:cmh-program` |
| `prog:product-test` | `rem:product-stress-test` |
| `rem:covariance-route-dead` | `rem:covariance-only-saturates` |
| `heur:V2-fails` | `rem:v2-fails` |
| `hyp:absolute-geometric-completion` | `ass:absolute-geometric-completion` |
| `hyp:KI` | `ass:KI` |
| `hyp:sol-sfm-frontier`, `hyp:sol-sws-letwin` (dossiers) | `ass:sol-sfm-frontier`, `ass:sol-sws-letwin` |
| `subsec:{atlas,qcts,product,excess,bootstrap,spectral}-fences` | `subsec:…-barriers` |
| `subsec:atlas-routes`, `subsec:two-subroutes` | `subsec:atlas-approaches`, `subsec:two-variants` |
| `sec:spectral-route`, `sec:appendix-route-e` | `sec:spectral-approach`, `sec:appendix-approach-e` |

Files renamed with them: `solutions/q-cmh-approximation.md` →
`solutions/prop-cmh-approximation-closure.md`, its review
`2026-08-27-q-cmh-approximation-proof-review.md` →
`2026-08-27-prop-cmh-approximation-closure-proof-review.md`,
`modules/30-spectral-route.md` → `modules/30-spectral-approach.md`,
`modules/60-appendix-route-e.md` → `modules/60-appendix-approach-e.md`. References to the
former LaTeX files (`*.tex`) in older records were left as they were.

**Fingerprints recorded without a reading.** The renames changed the bytes of 22 dossiers
and the fingerprints of the statements citing a renamed id; the statement changes above
changed three certified statements (`prop:cmh-approximation-closure`,
`conj:weighted-excess-rate`, which the refuter's reviews fingerprint, and
`prop:weighted-spectator-obstruction`). By the maintainer's decision, the 49 affected
entries in the reviews were set to the values of the tree at this commit, without a new
review; the maintainer ran the update. For `prop:cmh-approximation-closure` the sync
review checked that the dossier's theorem implies the sharpened statement, with the same
constant; it did not re-read the proof.

## What resists

- **The four open implications** need a dossier. `thm:centroid-implies-kls`,
  `thm:carleson-implies-centroid` and `thm:intro-all-cut` can share one, citing only
  `lem:survival-implies-kls`, `thm:scalar-riccati` and `cor:tight-window-consumption`; the
  step that needs care is the finiteness of $\E\int D$ before $(1-\alpha)\E\int D$ is
  discarded. `thm:intro-weighted` rests on a refuted antecedent and has little value.
- **`conj:mm-square-root-commutator`** is still not exact: where its “dimension-free
  constant” enters the displayed inequality, and what “supplies the global analytic input”
  asserts, are questions for its author.
- **`conj:cmh-second-variation` may be vacuous.** `2026-09-06-synthesizer-kls-wave-five-w5y01.md`
  observes numerically that the product-potential family leaves the log-concave class for
  both signs of $\eps$; if no admissible perturbation exists, a general perturbation
  $\psi_0+\eps\chi$ is the statement to ask.
- `conj:trace-upgrade` asserts exactly `ass:tight-prefix-carleson`: two nodes, one
  statement.
- `prop:spectator-excess-rate-obstruction` still ends with commentary inside its
  statement; `solutions/thm-cmh-normalization.md` and
  `solutions/kls-qcts-stein-boundary-core.md` keep a few harness words in their prose.
- The certifications rest on the LaTeX reviews, the conversion oracle and the mechanical
  updates of both migrations and of this checkpoint; fresh `certify` reviews would replace
  them. A person reads the manuscript before the `pages` workflow is dispatched.

## Proposed next step

The maintainer reads the manuscript. Then a `researcher` (`prove`) writes the shared
dossier of the three all-cut implications, for a fresh `certify` review.
