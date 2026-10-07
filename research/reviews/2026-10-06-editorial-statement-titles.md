---
verdict: editorial
amends:
  - research/reviews/2026-09-06-lem-linear-sector-third-moment-proof-review.md
  - research/reviews/2026-08-30-lem-mm-smallgap-fourth-moment-proof-review.md
  - research/reviews/2026-10-01-window-occupation-empty-branch-review.md
  - research/reviews/2026-10-01-cor-dichotomy-certification.md
authors:
  - orchestrator, claude-opus-5-5, 2026-10-06
reviewer: reviewer, claude-sonnet-5-5, 2026-10-06
changes:
  cor:gate-zero-third-moment: {from: 8ce2b303350d3cb2ee258251dc5a644f3b518c5bce6efa2369d129b50ff389a2, to: 4b2ae17f349b79d4a68e649970595debb6a72dd6deb0fb98df502fa6b0f4cced}
  lem:mm-smallgap-fourth-moment: {from: 5efc054693b4557b794756da70c6b5a5ba03e38dc8bd743eca82855cc796d1df, to: 1a3b3aa3baa88388617697d0cd9d3d865cb47c2000acb14c13ffc93267d44ce9}
  prop:mm-window-occupation: {from: b13fcfb79f741c03ddd93e3c526e8022bd1a7c55efce5eac9a5126b0b1d292e1, to: c009dc4048e1f0f03aa5071c827f7f46c90e78c21bc926344c20ef94f8e60b1f}
  thm:klartag-logn: {from: 70dd5528111bc813bcfa6750d3afcfcdc31121dbf564fb0681db32265b576b60, to: 7a1d449894090dbb2b7e97bfa20856aa6d83878a29a4e5f9e227cc2c1be96bee}
---

# Editorial note on the four reports above

Four statement titles were renamed. Each diff touches only the title line of the directive.

## `cor:gate-zero-third-moment`

```diff
-:::{prf:corollary} Gate zero controls the directional third moment
+:::{prf:corollary} The linear test controls the directional third moment
```

Why the mathematics is unchanged: the statement, formulas, hypotheses, quantifiers,
constants and steps read the same; only the name of the condition in the title did.

## `lem:mm-smallgap-fourth-moment`

```diff
-:::{prf:lemma} Small-gap fourth moment from the published frontier
+:::{prf:lemma} Small-gap fourth moment from the published logarithmic bound
```

Why the mathematics is unchanged: the body is untouched (it already cites the constant
$K_n$ of `thm:klartag-logn`); only the descriptive word "frontier" became "logarithmic bound".

## `prop:mm-window-occupation`

```diff
-:::{prf:proposition} Window occupation and frontier reproduction
+:::{prf:proposition} Window occupation and recovery of the published bound
```

Why the mathematics is unchanged: the body (the occupation hypothesis with $C_0=34$,
$C_1=0$, and the conclusion $\CP\le C\log^2 n$) is untouched; only the title wording changed.

## `thm:klartag-logn`

```diff
-:::{prf:theorem} Isoperimetric $\log n$ frontier; [@Klartag2023Logarithmic]
+:::{prf:theorem} Isoperimetric $\log n$ bound; [@Klartag2023Logarithmic]
```

Why the mathematics is unchanged: the bound $\hstar_n\ge C^{-1}(\log n)^{-1/2}$ and
$\CP\le C\log n$ and the citation are untouched; only "frontier" became "bound" in the title.
