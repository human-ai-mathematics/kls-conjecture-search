---
---

# Repair round on `solutions/lem-cmh-linear-spectral-resolution.tex` (run w5p03)

Researcher `/w5/researcher-clsr-repair`, lens `prove`, concurrency key
`solution:solutions/lem-cmh-linear-spectral-resolution.tex`. Correction contract: the cold
audit `research/reviews/2026-09-06-lem-cmh-linear-spectral-resolution-audit.md`
(reviewer `/w5/reviewer-clsr`, run w5r01), items D1-D3 plus the `prop:cmh-bochner` note.
No mathematics was changed; every proof step the audit checked is untouched.

## What was done

**D1, route (b).** The orchestrator had already reworded the manuscript lemma
(`modules/kls/41-cmh-normalization.tex`, `lem:cmh-linear-spectral-resolution`) and the ledger
summary to the weak column equation, defined $Q_{\rm lin}$ and $(\mathrm{AB})_{\rho,\beta}$
before the lemma, and declared $\langle v,\mathsf A_{\rm op}v\rangle$ the closed-form value
$\calE(v,v)$. The dossier now states exactly that:

- `thm:sol-clsr-main`(c) (lines 193-215) asserts $(A+Q)a\in L^1(\eta;\R^n)$, columns
  $Ha=\nabla\langle a,\nabla\psi\rangle\in\Dom(\calE)$ componentwise, and
  $\calE(f,(Ha)_i)=\langle f,(Ha)_i\rangle-\langle f,((A+Q)a)_i\rangle$ for every bounded
  smooth finite-energy $f$, where "finite energy" is spelled out as
  $\int\langle H^{-1}\nabla f,\nabla f\rangle d\eta<\infty$ (the class $\mathfrak B$ of
  `lem:sol-clsr-form-membership`, which is what the proof actually covers). It says explicitly
  that no membership $(Ha)_i\in\Dom(\mathsf A_{\rm op})$ is asserted.
- `thm:sol-clsr-main`(d) (line ~231) names $\langle v,\mathsf A_{\rm op}v\rangle=\sum_i\calE(v_i)$
  as the closed-form value $\calE(v,v)$ of the manuscript.
- `rem:sol-clsr-weak-vs-strong` (lines 287-301) and `rem:sol-clsr-gap` (lines 748-760) now say
  the lemma states the weak form, that the strong operator-domain form
  $(1-\mathsf A_{\rm op})(Ha)=(A+Q)a$ is not a claim of the lemma, that it is equivalent to
  $\Tr Q\in L^2(\eta)$ (a separate open question on the class), and that it holds on products.
- The "Flagged gaps" paragraph (lines 1109-1118) now reads "None" with the agreement recorded.

Route (a) — proving $\Tr Q\in L^2(\eta)$ on the compact-target class — was not attempted:
$Q_{kk}=\|H^{-1/2}\partial_kH\,H^{-1/2}\|_{\HS}^2$ involves $H^{-1}$ where $H$ degenerates at
infinity, and nothing in the dossier's cutoff calculus controls that beyond $L^1$. The
question stays open and is not a blocker for the lemma as now stated.

**D2.** `lem:sol-clsr-ibp`(ii) (line 440) now requires only "$X'$ vanishing on $[t,\infty)$
for some $t\in\R$"; its proof (lines 450-454) cites the compact sublevel set $\{\psi\le t\}$
of `lem:sol-clsr-coercive`. This matches the application in `lem:sol-clsr-cutoff` with
$X'=\chi_m$, whose support is $(-\infty,2m]$.

**D3.** `rem:sol-clsr-klartag-import` (lines 99-110) now states Klartag's Theorem 1.1 as
$\Delta\psi\le2R(P)^2$ under his conditions (1) (matched to the class: $V\in C^\infty(\R^n)$,
$\overline P$ compact) and deduces $H\preceq(\Tr H)\Id\preceq2R(P)^2\Id$ from $H\succ0$.

**Audit trail** item (5) (lines ~1095-1099) records that `prop:cmh-bochner` is a listed
`depends_on` entry not consumed by the proof and that this handoff proposes dropping it.

Header: `date : 2026-09-06`, second `author` line added, original author kept.

## Verification

- `cd solutions && latexmk -pdf -interaction=nonstopmode -outdir=../build lem-cmh-linear-spectral-resolution.tex`: exit 0, no LaTeX errors, cross-module `??` only.
- `python3 scripts/check.py`: 0 errors.

## Proposed deltas (orchestrator)

- `research/program/ledger.yaml`, node `lem:cmh-linear-spectral-resolution`: drop
  `prop:cmh-bochner` from `depends_on` when the `proofs[]` record is wired
  (CLAUDE.md constraint 8; the dossier uses no identity from it).
- No `proofs[]` record yet: the dossier is a draft until a new cold `certify` review passes.

## Portfolio delta

`ap:cmh-anisotropic-bootstrap`: unchanged state; its structural lemma is awaiting a second
cold review of the repaired dossier. No new blocker, no candidate, no retirement.
