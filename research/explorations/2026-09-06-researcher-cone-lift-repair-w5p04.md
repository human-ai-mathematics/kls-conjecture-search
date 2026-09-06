---
type: exploration
date: "2026-09-06"
outcome: proposed
approach: ap:cmh-gate-zero
nodes:
  - prop:cone-moment-map
  - prop:cone-linear-sector
  - cor:cube-cone-gate-zero
---

# Researcher (prove lens, repair round): the exponential-cone dossier after audit w5r04

Run `w5p04`, agent `/w5/researcher-cone-lift-repair`, concurrency key
`solution:solutions/prop-cone-moment-map.tex`. This record does not edit the w5p01 record
(`2026-09-06-researcher-cone-lift-w5p01.md`); it records the repair of the dossier that
record produced, per the audit
`research/reviews/2026-09-06-prop-cone-moment-map-audit.md` (reviewer `/w5/reviewer-cone-lift`,
run `w5r04`, Finding 7 / defect D1). The repair contract was the reviewer's verbatim
`next_prompt`; every listed item is addressed below.

## The defect (D1) and what it touched

The dossier defined "moment potential" as any convex $\psi:\R^d\to\R\cup\{+\infty\}$ with
$\int e^{-\psi}=1$ and $(\nabla\psi)_\#(e^{-\psi}\,dy)=\eta$, but quoted uniqueness up to
translation (Cordero-Erausquin--Klartag) only among *essentially-continuous* potentials, and
then stated "every moment potential of ... is a translate of ..." over the broad class (in
the statements of the base lemma and Theorem A(iii)). Under the broad definition those
clauses are false: the reviewer's witness $\psi_c$ (finite on $[-T_c,T_c]$, $+\infty$
outside) is a non-essentially-continuous potential of $\mathrm{Unif}[-1,1]$ that is not a
translate of the finite one. No proof step of the three nodes was affected; the manuscript's
"the moment potential" is the essentially-continuous one of `eq:moment-measure`.

## What was changed in `solutions/prop-cone-moment-map.tex` (R1 chosen)

Pre-repair SHA-256 `b11f9a1fcda6f07f066e741f8888babe7d95bba1d1bf08d7019afb9193cd1e0a`
(875 lines); post-repair
`799082f3bade3c80277b001f0ea6199aa160a72a3ccefa99d02d89eefff3278a` (911 lines).

1. **Definition (item 1, option R1).** Lines 37--50: essential continuity is defined (CEK
   Definition 2: lower semi-continuous, discontinuity set of zero $\mathcal H^{d-1}$-measure),
   and a *moment potential* is now an essentially-continuous convex
   $\psi:\R^d\to\R\cup\{+\infty\}$ with $\int e^{-\psi}=1$ and moment measure $\eta$. One
   sentence records that a finite convex function on $\R^d$ is continuous, hence essentially
   continuous, so $\varphi$, the rescaled $\lambda$, the product $\Lambda$ and $\phi_T$ are
   all moment potentials in this sense. Every sentence the audit listed (former l. 205, 215,
   233, 243, 253, 277, 329--332, 633) is now a correct consequence of `thm:sol-cone-cek`
   without textual change.
2. **Reconciliation (item 2).** The former "every moment potential produced in this dossier is
   in the class to which the uniqueness applies" sentence is gone; the paragraph after
   `thm:sol-cone-cek` (lines 60--70) now states exactly how the cited theorem's hypotheses
   ($0<\mu(\R^d)<\infty$, not in a lower-dimensional subspace, barycenter $0$) specialise to
   the dossier's (probability, finite first moment, barycenter $0$, not in a hyperplane).
   Remark `rem:sol-cone-hypotheses`(4) (lines 831--847) is reworded to name the class, and
   now records the explicit one-dimensional witness $\psi_c$ showing that the restriction
   to essentially-continuous potentials is necessary for uniqueness; the witness is verified
   inline in five lines (convexity, l.s.c., $\psi_c''=2e^{-\psi_c}$, mass $1$, pushforward
   density $\tfrac12$ on $(-1,1)$, discontinuity at $\pm T_c$).
3. **Citation (item 3).** `thm:sol-cone-cek` (lines 52--58) is now cited as Theorem 2 of the
   arXiv version `1304.0630v1` of `CorderoErausquinKlartag2015MomentMeasures` (line 60), as
   confirmed by `2026-09-06-literature-scout-cone-lift-w5l01.md` §3.1. That checkpoint did
   *not* verify the journal (JFA 268, 2015) numbering, so the "flagged for verification"
   sentence was **not** simply deleted: it was narrowed to the journal numbering only, at
   line 69--70 and in Remark `rem:sol-cone-open`(a), lines 893--897.
4. **Base lemma proof made explicit** (a consequence of R1, not a new item). Lines 240--250:
   `thm:regular-moment-map-compact-target` supplies the canonical potential
   $\lambda_K^0$; `thm:sol-cone-cek` makes the given $\lambda_K$ a translate of it;
   translation preserves smoothness, strict convexity, the gradient image and (by the
   invariance paragraph after `eq:sol-cone-kernel-def`) the kernel. Previously the
   compact-target theorem was applied to $\lambda_K$ directly with a parenthetical.
5. **Theorem C inequality (item 4, inlined).** Line 785--787: "$1+n/\beta\le2\iff n\le\beta$,
   which holds by hypothesis, with equality iff $\beta=n$" is proved in place. Theorem B(ii)
   is no longer cited there, so **no** `depends_on` edge from `cor:cube-cone-gate-zero` to
   `prop:cone-linear-sector` is needed; the existing edge to `prop:cone-moment-map` (kernel
   formula) remains the only internal dependency of Theorem C.
6. **Wording (item 5).** Theorem C statement, line 714: "$\sqrt2$ times an orthogonal map".
   Proof, lines 810--815: $R$ is named an orthogonal map (a reflection, $\det R=-1$), with
   the parenthetical that composing with the coordinate swap, under which the i.i.d. product
   law is invariant, gives $\sqrt2$ times a rotation.
7. Header: second `author` line `/w5/researcher-cone-lift-repair` (line 14), original kept;
   `date : 2026-09-06`. The header parser keeps the first value of a repeated field.

No other mathematics was changed (audit Finding 6 checked every other step).

## Build and check

`cd solutions && latexmk -pdf -interaction=nonstopmode -outdir=../build prop-cone-moment-map.tex`
exits 0; the undefined references are exactly the cross-module labels the audit listed
(`eq:moment-measure`, `eq:MA`, `eq:stein-kernel-def`, `eq:stein-identity`,
`eq:stein-generator`, `eq:cmh-constant`, `eq:gate-zero-sharp`, `eq:cmh-1d-stein`,
`eq:cone-covariance`, `def:cmh`, `def:exponential-cone`, `prop:cmh-hodge`,
`lem:linear-sector-third-moment`, `subsec:cmh-conventions`, `subsec:cmh-hodge`,
`thm:cmh-implies-affine-poincare`, `thm:regular-moment-map-compact-target`, the three node
labels); the new forward references inside the dossier resolve. `python3 scripts/check.py`
reports 0 errors (the dossier is still unnamed by any `proofs[]` record, so it is a draft).

## Deferred ledger artifact

Unchanged from w5p01: after an independent review certifies, the record for each of the
three nodes is `proofs[].artifact: solutions/prop-cone-moment-map.tex`, `mode: agent`,
`review:` supplied by the reviewer. No new edge is proposed (item 5 above). The
manuscript-prose sync item the audit excluded (`41-cmh-normalization.tex` l. 332--333,
$\E_\nu\|D^2\varphi\|_{\HS}^2<\infty$ for a general base) is still the orchestrator's, not
this dossier's.

## Portfolio

`ap:cmh-gate-zero`: no state change. The dossier remains a draft awaiting a cold certify
review with an identity distinct from `/w5/researcher-cone-lift`,
`/w5/researcher-cone-lift-repair` and `/w5/reviewer-cone-lift`; that review should name
`research/reviews/2026-09-06-prop-cone-moment-map-audit.md` in `follows_up`.
