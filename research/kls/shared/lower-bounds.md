# Universal lower bounds & refuted forms — route-agnostic

Facts that bind **every** route to KLS, independent of the proof strategy. A new route in
[`../routes.md`](../routes.md) must respect these; a route whose central hypothesis collides
with one is dead on arrival (mark it `refuted`). Distinguished from the *mechanism* no-gos in
`routes/eldan-localization/obstructions.md`, which forbid specific localization proof moves —
those are route-internal. The items here are true of any attack. Math in LaTeX (`$…$`).

These facts are numerically gated by `finum` (SDE-free); see [`../gating.md`](../gating.md) for
the node → quantity → verdict map and the artifact `research/runs/<date>-kls.jsonl`.

## The sound lower bound (the universal refuter)

For any measure, every test function gives a certified Poincaré lower bound
$C_P\ge \mathrm{Var}(f)/\mathbb E\lVert\nabla f\rVert^2$; the linear test
$f=\langle v,\theta\rangle$ gives $C_P\ge\lambda_{\max}(\mathrm{Cov})$ (`lem:linear-test-lower`
in `../../knowledge/lemmas.md`). For isotropic measures $\lambda_{\max}(\mathrm{Cov})=1$, so
this says $C_P\ge 1$ — KLS is the matching *upper* bound $C_P\le 1/c^2$. Consequence for
routes: any claimed dimension-free upper bound must survive this lower bound on every test
instance; `finum` uses it as the go/no-go gate when numerically vetting a route.

## Refuted forms (any route must avoid)

- **Single-coordinate counterexample — refuted** (`obs:rank-one-refuted`,
  `cor:refutation`). The natural "one inflated coordinate breaks the product budget" attempt
  does **not** refute the program: the product coordinate-budget theorem (`thm:budget`)
  absorbs a rank-one inflation. A route built on engineering a single bad coordinate is dead;
  the surviving danger is the *adapted alignment* problem (`q:alignment`), which is subtler.
- **Relative-scale-for-all-measures is KLS-equivalent, not intermediate**
  (`obs:relative-ceiling`). Demanding the covariance-excess bound $\Xi_T\le\kappa T$ for
  *every* measure is logically equivalent to KLS itself — so a route that "reduces" KLS to it
  has reduced KLS to KLS. Real progress must use *extremality* (near-worst structure), e.g.
  `q:taming`.

## Why these live here, not in a route

These are statements about the **target and its counterexamples**, not about how localization
estimates behave. They were discovered inside the Eldan route but are facts about KLS itself,
so a future non-localization route inherits them unchanged. When a new refuted form is found
that is route-agnostic, add it here; when it forbids a specific *proof mechanism*, it belongs
in that route's `obstructions.{yaml,md}`.
