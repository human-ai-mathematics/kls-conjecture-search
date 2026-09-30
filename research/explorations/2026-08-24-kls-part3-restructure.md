---
---
# 2026-08-24 — Part III restructure: groups, literature survey, Route S promotion

Type: **exposition / organization**. No new mathematics, no ledger status change, no new claim.
Every `\label` in `modules/kls/` was preserved verbatim; the KLS ledger was edited only in its
`file:` fields.

## Why

Part III had grown to 17 flat `\section`s over ~50 pages with no visible grouping: the reader
could not see that some sections were shared machinery, some belonged to one Eldan subroute, and
one belonged to a different route entirely. That grouping existed only in `%` comments in
`main.tex`. There was also no general presentation of KLS anywhere in the document — the reader
went from `\begin{conjecture}` to two-color Riccati identities in about four pages — and the
three live routes were represented at wildly different depths (Eldan 14 sections,
moment-map-cmh 1 section, moment-map-spectral a single `\begin{question}`).

## What was done

**1. Six visible groups.** New `\klsgroup{}{}` macro in `shared/preamble.tex`: a divider plus a
TOC entry above `\section` level. It introduces no numbering of its own, so section numbers,
theorem numbers, and labels are untouched. Part III is now Group 0 orientation · Group 1
literature survey · Group 2 shared machinery · Group 3 Route E · Group 4 Route S · Group 5
Route C · Group 6 synthesis.

**2. Files renamed** to make the grouping legible on disk (`1x-` shared, `2x-` Route E, `30-`
Route S, `40-` Route C, `50-` synthesis). All 78 KLS ledger `file:` fields were rewritten in the
same change; `check_ledger.py` validates their existence, and it returns 0 errors / 0 warnings.

**3. `00-strategy-map.tex` dissolved.** Its nine labels were rehomed rather than renamed:
`conj:kls`, `eq:hstar-def`, `eq:kls-implies-thin-shell`, `sec:kls-strategy-map` →
`00-orientation.tex`; the four imported July-2026 theorems → `04-family-moment-map.tex`;
`conj:mm-spectral-occupation` → `30-spectral-route.tex`. Verified by diffing the sorted label set
before and after: **zero labels lost**, 114 added.

**4. Group 0 (new), `00-orientation.tex`.** Conjecture in three forms (isotropic, affine,
geometric); the $\psi$-convention trap stated once as `rem:psi-convention`; status table
separating best *published* (Klartag) from best *preprint* (Letwin v1); the 1995→2026 history
table with $\Psi_n$ and $C_{P,n}$ side by side; slicing and thin shell as solved neighbours that
do not imply KLS, with Eldan's reverse estimate showing why; a TikZ redraw of the four-ingredient
architecture; the exact bridge $C_{P,n}\lesssim\kappa_n\sqrt{\log n}$ and the localization of the
surviving logarithm in the log-trace-exp softmax; the covariance-spike obstruction; and the
reading map.

**5. Group 1 (new), five family sections** with a common template — object followed / what it
buys / sharpest result / precise missing estimate / why it stalls. Full derivations: the
localization lemma and the $\mathrm{Tr}$-vs-$\|\cdot\|_{\mathrm{op}}$ counting obstruction; the SL
SDE triple, the Lee–Vempala transfer criterion, the $\mathrm{Tr}(A_t^2)$ Itô computation; the
improved-Lichnerowicz proof sketch and the Barthe–Klartag $H^{-1}$ inequality; the differentiated
Monge–Ampère identity, the fixed-matrix bound, the Stein kernel and the $|M|^{1/2}$-conjugation
trick; Caffarelli / Brownian transport / entropic barrier.

**6. Route S promoted** from `research/kls/routes/moment-map-spectral/README.md` to
`30-spectral-route.tex`: fixed-function SDE $dg_t=H_tdW_t-A_tg_t\,dt$, the whitened tensor
estimate, `conj:mm-spectral-occupation` with its sufficiency statement, the audited $H^{-1}$
endpoint (kept explicitly as a *calibrated endpoint*, not a preliminary lemma, since it is
quantitatively implied by KLS), and the fence comparison. The brief remains the control-plane
status page and records the promotion.

**7. Group 6 (new), `50-synthesis.tex`.** The residue table by family, and four next targets each
mapped to a ledger node: function-adapted localization → `conj:mm-spectral-occupation` /
`conj:trace-upgrade`; nonlinear moment-map extension → `rem:cmh-program` and its three sub-targets;
effective-rank replacement for log-trace-exp → `conj:taming` and the interface functional $\Xi_T$;
parallel coupling beyond linear tilts → **no repository node** (recorded as a gap in the route
registry).

**8. Deduplication.** `research/kls/strategy-map.md` §1–2 restated the target and frontier that
the manuscript now states. It was reduced to a status registry that points at the manuscript
sections; the mathematics is no longer duplicated across the two planes.

## Rigour notes — what was deliberately *not* asserted

- **Bibliography.** ~11 entries added. Journal volume/page/DOI metadata was **omitted rather
  than reconstructed from memory**; author, title, year, and the arXiv eprint are the only
  fields, with the eprint as the authoritative pointer. A first attempt at these entries did
  include volume/page/DOI reconstructed from memory and was rewritten for exactly this reason.
- `Zhang2026HitAndRun` (arXiv:2608.13487) carries an explicit **UNVERIFIED METADATA** note: the
  author's full name and exact title were not confirmed. It is cited once, only as secondary
  evidence that the published/preprint status distinction is drawn elsewhere.
- The history table's $O(n^{5/12})$ row is flagged in `rem:history-table-caveats` as a summary of
  a sequence of thin-shell improvements, not a single paper. The same remark flags
  `vempala2016kls` — a 2016 announcement of a proof of the full conjecture — as *not* a milestone
  in the table.
- **Import discipline preserved.** Every imported July-2026 statement is attributed individually
  and marked version-1-preprint; `subsec:mm-audit` lists the four delicate points for independent
  checking, including that Letwin obtains $C_P\lesssim\kappa_n\sqrt{\log n}$ by *tracing*
  Klartag's estimates rather than quoting a theorem in that form. The synthesis closes by noting
  that three of its four targets take $\kappa_n=O(1)$ as premise, and what changes if that
  premise does not survive review.

## Verification

```
python3 research/check_ledger.py     # 2 ledgers, 150 nodes, 562 labels. 0 errors, 0 warnings.
latexmk -pdf -outdir=build main.tex  # 0 errors, 0 undefined refs/citations, 136 pages
```

Label-set diff before/after the restructure: no label removed.

Note: `biber` needed one explicit rerun after the bibliography grew, because `latexmk` exited 0
while 16 citations were still undefined. If new `\cite` keys appear undefined after an edit, run
`biber --output-directory build main` once and rebuild.

## What this did not touch

No status was promoted or downgraded; the 41-node legacy Eldan certification debt is unchanged;
no numerical claim was made or consumed; `research/reviews/` and earlier `research/explorations/`
entries were left as written, including their references to the old file names, since both are
dated records of the state at the time.

## Open follow-ups

1. Target 4 of the synthesis (parallel coupling beyond linear tilts) has no route directory and
   no ledger node. Either open a route or record explicitly that it is out of scope.
2. Verify the bibliographic metadata of `Zhang2026HitAndRun` against arXiv, or drop the citation.
3. The constants in `eq:cheeger-two-sided` ($\tfrac14\le\Psi^2/C_P\le\pi$) and Eldan's reverse
   estimate `eq:eldan-reverse` are cited to sources but were not re-derived here; a reviewer
   should confirm both against `Klartag2023Logarithmic` and `Eldan2013ThinShell` before either is
   used quantitatively rather than as orientation.
