---
verdict: revise
authors:
  - kls_core_author, unknown, 2026-08-25
reviewer: reviewer, gpt-6-astra, 2026-10-04
fingerprints:
  solutions/kls-localization-riccati-core.md: 1bb625d625802df0ca05a338d3038a48ff8a0d2ca112f2fe1a2a4d9877690dff
  lem:survival-implies-kls: fcc0ff284f00b4f7d903900409e37db884463ad15f1f7cbb2c48ecb254e4cc64
  lem:matrix-riccati: b529c0f736b4dce32a7843e81f8edb6569491781941e3b8aecdc1be0ddf7a023
  thm:scalar-riccati: 83fdb94d00721fdfab219b0a417b1ac815c170925d051a187929c3635241286d
  cor:per-direction: 41aeb34aa0f748e931a100d435bb6cbba97772f149ce25c2e089fc77974c1e43
  cor:tight-window-consumption: 7d0f9e5dce52482fc3b8f93155bb46e66596d3aac7d92a63f7e508bc25b59946
  lem:pathwise-BL: 5b8de97a90772764778ad79fc4a9f56642c732304f4792a95b6cc493c7a95d6a
  prop:stein-rep: 809545792ca08860114a8276ff5b61febda2930cfd2b8b0f3a1a5ca1a0d00e6a
  cor:away-from-zero: d15055503849fa299724c5cb1640fab8f4b60ebc491621b6ffb1d34480e0dd95
  lem:stein-vs-source: 6bd84bc399d194fcb26d5a831feb198bcda29c1beaa21a9d1ebe64320eca30b5
---

# Independent Wave A examination of balanced posterior survival

## Findings

**Revise for [](#lem:survival-implies-kls).** This is a full fresh examination,
not a re-review retaining an earlier verdict. The assignment supplied repository
paths and scope only, with no authoring conversation. The historical report was
used only for the author's identity. No node receives certification here.

The dossier's survival lemma agrees with the canonical statement, including the
arbitrary measurable cut, positive finite time, numerical constant, and uniform
quantifiers in the KLS consequence. Its ledger node has no `depends_on`, `assumes`,
or `bounded_by` edges. The survival event is an explicit hypothesis, not a claim
that such universal constants have been established.

The scope is Section 2 of the dossier and its required setup and regularity
conventions. The whole dossier was read to determine whether a later passage
supplied the missing justifications. It does not. The full fingerprint command
includes all seven header nodes and their dependencies automatically; this is
version identification, not certification of those additional claims.

### Steps checked

The posterior potential is $V(x)+T_0|x|^2/2-c_{T_0}\cdot x$ up to normalization.
For a smooth convex potential on all of Euclidean space its Hessian is at least
$T_0I$. The classical curvature comparison therefore supplies the stated
$c\sqrt{T_0}\min(p,1-p)$ bound, with a dimension-independent $c$.

Actual sources examined were:

- [Bobkov (1999), pp. 1903 and 1906](https://www-users.cse.umn.edu/~bobko001/papers/1999_AOP_Isop.pdf): the perimeter is lower outer Minkowski content, and the discussion on p. 1906 attributes the stronger Gaussian comparison under a positive Hessian bound to Bakry--Ledoux. Bobkov's general log-concave Cheeger theorem alone is not the required dimension-free curvature estimate.
- [Bakry--Ledoux (1996), Corollary 2.2 and (2.11), pp. 267--268](https://www.math.univ-toulouse.fr/~ledoux/LevyGromov.pdf): the functional comparison has the $\sqrt R$ scaling and yields lower outer Minkowski isoperimetry. This is the actual published source underlying Bobkov's attribution.
- [Milman (2009), Theorem 1.8, Corollaries 6.5 and 6.12, and Appendix A](https://arxiv.org/pdf/0712.4092): the published result, accessed through its author preprint mirror, supplies symmetry and concavity for general absolutely continuous log-concave laws, with the non-smooth extension addressed in Section 6. This is an established published import, not an uncertified new-preprint dependency.

The BGL 2014 author-hosted PDF available in this session contains only front
matter; the publisher chapter was not retrievable. No claim about the contents
of that book is certified. It is supplementary to the accessible original
Bakry--Ledoux theorem, so no necessary external theorem is left inaccessible.
The defects below concern applying these inputs at the dossier's full scope.

Given the perimeter expectation inequality and posterior isoperimetry, the
three inequalities in the proof are correct: nonnegativity allows expectation,
and the event implies $\mathbb E\min(p_{T_0},q_{T_0})\ge c_0b_0$. There is no
hidden factor depending on dimension. Feasibility forces $b_0\le1/2$ and
$c_0\le1$; outside those ranges the premise is impossible.

The balanced-cut conclusion is also correct. A bound $L$ for every cut of mass
$1/2$ gives $I_\mu(1/2)\ge L$ without existence of a minimizer. Concavity,
symmetry and nonnegativity give
$I_\mu(p)\ge2L\min(p,1-p)$ and hence $h_\mu\ge2L$. For dimension one no
continuity at the endpoints is needed: apply concavity between an interior
$\varepsilon$ and $1/2$, then let $\varepsilon\downarrow0$. The assertion that
the profile vanishes at the endpoints is valid as an assigned endpoint value,
but must not be read as asserting endpoint continuity in dimension one.

Hypotheses used are: a deterministic measurable cut; a log-concave,
full-dimensional probability law; its usual stochastic-localization posterior;
$T_0>0$ finite; and the stated event. Full dimensionality follows from
isotropy. Isotropy is unused in the individual survival-to-perimeter estimate;
it identifies the family needed for KLS. Smooth density and regular boundary
are extra hypotheses in the written justifications, absent from the statement.
No occupation estimate, Riccati identity, or infinite-time uniform integrability
is needed for this implication.

### Defects

1. **Lower outer Minkowski content is not the reduced-boundary integral for an
   arbitrary measurable cut.** Dossier line 33 claims the perimeter expectation
   inequality follows directly by integrating the likelihood over the reduced
   boundary. That proves a statement about weighted BV perimeter in an
   appropriate finite-perimeter class, not the claimed Minkowski statement.
   For example, for standard Gaussian measure on the line and
   $E=(-\infty,0]\cup\{1\}$, the mass is $1/2$ and the lower outer Minkowski
   content is $\varphi(0)+2\varphi(1)$, whereas the weighted reduced-boundary
   integral is only $\varphi(0)$. This follows by examining the two disjoint
   added intervals in $E^\varepsilon\setminus E$ for small $\varepsilon$.
   Thus the identification fails even for a balanced set with finite outer
   Minkowski content. This is not a counterexample to the lemma or to the
   expectation inequality itself.

2. **The general-density passage is not specified.** Line 140 literally uses a
   classical Hessian, while the canonical class includes convex potentials
   taking $+\infty$ off a convex support and non-smooth potentials. The blanket
   truncation/smoothing/Fatou paragraph at line 26 addresses nonnegative
   occupation terms; it does not establish preservation of curvature and
   passage of an isoperimetric inequality for a fixed arbitrary cut. Nor does
   it justify preservation of the survival-event premise if the entire
   localization experiment is approximated. An exact general strongly
   log-concave comparison theorem or a specified approximation argument is
   needed here.

`uv run scripts/check.py` completed successfully with exit code 0 on the tree
examined, with no MyST error. The fresh fingerprint block above is the exact
output of `uv run scripts/check.py --fingerprint
solutions/kls-localization-riccati-core.md`. Initial sandbox runs failed because
Node subprocess execution was blocked; the successful checks used the approved
execution path. A successful build does not close either analytic defect.

## Corrections

Researcher repair instructions, referring to the examined dossier's line numbers:

1. **Lines 26--33:** define the lower outer Minkowski convention explicitly and
   replace the reduced-boundary justification with a proof for the actual
   measurable-set statement. One route is to use the nonnegative neighborhood
   increments $\mu_t(E^\varepsilon\setminus E)/\varepsilon$, the bounded
   indicator-mass martingale, and Fatou along a deterministic sequence realizing
   the initial liminf. Supply the measurability and liminf details, address
   infinite initial content, and explain the convention for completed-measurable
   cuts if these are included. Alternatively prove a complete BV-to-Minkowski
   bridge with the needed direction; do not identify the two perimeters.
2. **Lines 140--146, with line 26:** state the exact comparison theorem used for
   extended-valued convex potentials, including arbitrary convex support and
   the same outer Minkowski convention. Cite a precise accessible source that
   has this scope, or write the curvature-preserving approximation and justify
   the limit of its functional or set inequality. Prefer applying this theorem
   directly to each original posterior; if instead approximating the stochastic
   experiment, prove transfer of the event hypothesis as well.
3. **Line 154:** give the explicit $2I_\mu(1/2)$ Cheeger deduction and cite the
   general-density profile result precisely. Clarify the endpoint convention
   so it does not require one-dimensional endpoint continuity. This final
   clarification is expository, not an additional mathematical obstruction.
4. **Line 146 bibliography:** name the accessible original curvature source
   and its theorem when repairing the citation, or provide the relevant BGL
   text for a later source audit. No new source-only blockage is asserted here.

Do not alter the canonical lemma: no false quantified conclusion was found.
After repair, obtain a fresh independent review and new fingerprints.

## Exclusions

This verdict rejects the adequacy of the historical certification **for the
survival lemma at its full measurable-set scope**. It does not declare the
lemma false. It neither certifies nor invalidates the other six header nodes,
their dependencies, or other dossiers covered by the historical grouped report.
Downstream uses of survival inherit the unresolved proof obligation, but those
proofs and their ledger transitions were not independently audited here.
In particular no Riccati, tight-window, Brascamp--Lieb-source, or KLS theorem
receives a new certification from this report.

## Handoff

```yaml
files:
  - research/reviews/2026-10-04-wave-a-survival-independent.md
next: |
  Assign a researcher the four line-specific corrections above, preserving
  other agents' edits to the shared dossier. Review the repaired survival
  implication independently at its canonical general-measurable-set scope.
```
