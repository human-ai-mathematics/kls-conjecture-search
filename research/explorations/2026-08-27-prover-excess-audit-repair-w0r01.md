---
---
# Excess-audit dossier repair W0R01

Date: 2026-08-27  
Role: prover (`/root/repair_excess_dossier`)  
Artifact: `solutions/kls-excess-audit.tex`  
Nodes: `prop:intro-audit`, `prop:trivial-excess`, `lem:perimeter-martingale`,
`lem:excess-identity`, `lem:inf-martingales`

## Trigger and scope

The previous dossier used the correct noncompact fixed-cut inequality

$$
\mathbb E[P_t(E)\mid\mathcal F_s]\le P_s(E),
$$

but the proof of `lem:inf-martingales` subsequently replaced this inequality by equality.
The purpose of this repair was to decide whether the fixed-family infimum is nevertheless a
supermartingale, audit the other four claims in the dossier, and identify the exact ledger
dependency used by `prop:trivial-excess`.

No ledger, manuscript, route-control, review, or other solution file was edited. The dossier's
header was reset to `checked_by: none`; the original author and historical review provenance are
retained, but that review is not presented as certifying the repaired source.

## Contract and fences checked

The exact ledger statements and their manuscript labels were read in full. None of these five
nodes has a ledger `bounded_by` edge. The dossier nevertheless respects `obs:circularity`:

- the exact excess identity is restricted to compact support, where the fixed-cut perimeter is a
  true martingale;
- only an infimum over a fixed competitor family is shown to be a supermartingale;
- no monotonicity is claimed for the random, time-dependent family selected by a posterior mass
  window.

The use of `prop:two-tail` in `prop:intro-audit` only refutes the specified one-time-slice
unweighted proof shape. It does not assert a no-go result for time-nonlocal estimates.

## The repaired conditional-expectation argument

Let $\mathfrak S$ be fixed and nonempty and set
$J_t=\inf_{S\in\mathfrak S}P_t(S)$. For every fixed $S\in\mathfrak S$,

$$
J_t\le P_t(S).
$$

Therefore the noncompact fixed-cut supermartingale property gives, for $0\le s\le t$,

$$
\mathbb E[J_t\mid\mathcal F_s]
\le \mathbb E[P_t(S)\mid\mathcal F_s]
\le P_s(S).
$$

Taking the infimum over the same fixed family on the right yields

$$
\mathbb E[J_t\mid\mathcal F_s]\le J_s.
$$

The second inequality is an equality in the compact-support class, but equality is not used.
If $S_0\in\mathfrak S$, then

$$
0\le J_t\le P_t(S_0),
\qquad
\mathbb E P_t(S_0)\le P_0(S_0)<\infty,
$$

so the conditional expectation is well-defined. Countability makes the infimum measurable; the
uncountable version retains the dossier's explicit measurability convention.

The attempted alternative of upgrading every noncompact $P_t(S)$ to a true martingale was
discarded. It would require a uniform-integrability argument not supplied by the pointwise
nonnegative-local-martingale construction, and it is unnecessary for the conclusion.

## Full dossier audit

### `lem:perimeter-martingale`

For compact support, $|x-a_t|$ is bounded. Novikov makes every fixed-$x$ density factor a true
martingale on bounded intervals, conditional Tonelli transfers the equality to the boundary
integral, and a perimeter-level stopping gives stochastic Fubini. For noncompact support, the
density factors are only used as nonnegative local martingales and hence supermartingales;
conditional Tonelli gives the correct inequality. No noncompact equality or uniform
integrability is asserted.

### `prop:trivial-excess`

The proof uses $0\le e_t(E)\le P_t(E)$, Tonelli, and the deterministic-time consequence
$\mathbb E P_t(E)\le P_0(E)$. The stopping time is handled only through the indicator
$\mathbf 1_{\{t<\tau\}}$; optional stopping is not used. Isotropy supplies a unit-variance
one-dimensional marginal, and the standard log-concave density bound gives
$I_\mu(1/2)\le1$. Thus

$$
\mathbb E\int_0^{T\wedge\tau}e_t(E)\,dt\le(1+e_0)T.
$$

This proof does use the mathematical content of `lem:perimeter-martingale`, specifically its
noncompact supermartingale clause. The current ledger lists no dependency for
`prop:trivial-excess`. The exact proposed dependency delta, to be applied by the orchestrator
only together with a future valid certification, is:

```yaml
  - id: prop:trivial-excess
    # existing fields unchanged
    depends_on: [lem:perimeter-martingale]
```

### `lem:excess-identity`

The equality $\mathbb E P_t(E)=P_0(E)$ is used only under compact support. The dossier explicitly
states that the noncompact argument gives only an inequality, so the ledger and manuscript
scope is preserved.

### `lem:inf-martingales`

The repaired two-inequality argument above proves the same supermartingale conclusion for
general log-concave data. The pointwise profile comparison uses only containment of the exact-mass
competitor class in the windowed competitor class. It remains separate from the fixed-family
conditional-expectation argument.

The corresponding manuscript proof still says that every fixed-cut perimeter is a martingale.
For semantic synchronization after independent review, the orchestrator should replace that
sentence-level argument by

```tex
For each fixed $S$, Lemma~\ref{lem:perimeter-martingale} gives
$\E[\mu_t^+(S)\mid\mathcal F_s]\le\mu_s^+(S)$. Since
$J_t\le\mu_t^+(S)$, it follows that
$\E[J_t\mid\mathcal F_s]\le\mu_s^+(S)$; take the infimum over $S$.
```

### `prop:intro-audit`

The proposition consumes the unconditional excess estimate in an assumed unweighted
Stein-trace estimate, applies the exact Stein/source conversion with absorption coefficient
$2\beta+64\eta^2<1$, and invokes the separately stated tight-window consumption result. The
near-Cheeger contradiction and the two-tail exclusion retain their original scopes. No new
hypothesis or unresolved step was found.

## Outcome and status

All five mathematical statements are preserved; no downgrade is required. There are no
unclosed proof steps in the repaired dossier. The dependency edge above is a semantic ledger
repair, not a mathematical strengthening.

The standalone command

```bash
cd solutions && latexmk -pdf -outdir=../build kls-excess-audit.tex
```

completed with exit code zero and produced `build/kls-excess-audit.pdf`. The log contains no TeX
error, fatal error, emergency stop, or undefined control sequence. Its remaining warnings are the
expected unresolved cross-manuscript labels of a standalone subfile and a harmless empty
standalone citation destination.

This source is an unreviewed candidate with `checked_by: none`. It has no ledger value until a
distinct proof checker audits the repaired artifact. A future certified ledger update may again
use `solution: solutions/kls-excess-audit.tex`, atomically with a valid `checked_by` and review
record.
