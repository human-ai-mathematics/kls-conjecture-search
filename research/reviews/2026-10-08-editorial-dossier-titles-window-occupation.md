---
verdict: editorial
amends:
  - research/reviews/2026-10-01-window-occupation-empty-branch-review.md
authors:
  - orchestrator, claude-opus-5-5, 2026-10-08
reviewer: reviewer, claude-opus-5-5, 2026-10-08
changes:
  solutions/prop-mm-window-occupation.md: {from: b60447ac207a5bcb305b59df9c24faa34a6e0611743a83055217b3944f4a7752, to: a30c2fcd3a0ad2b9dbf3276b79e93fb0d1c6cf6196bf559e2d3aadf73baf2177}
---

# Editorial note on `research/reviews/2026-10-01-window-occupation-empty-branch-review.md`

Companion to `2026-10-08-editorial-dossier-titles.md`, examined in the same pass. It is separate because that note amends `2026-10-01-spectral-window-letwin-discharge-review.md`, which fingerprints this dossier at an older version than the one the empty-branch review certifies (as in `2026-10-07-editorial-site-pass-window-occupation.md`). This note carries over only the empty-branch review's certification of `solutions/prop-mm-window-occupation.md`.

## `solutions/prop-mm-window-occupation.md`

````diff
--- certified/solutions/prop-mm-window-occupation.md
+++ current/solutions/prop-mm-window-occupation.md
@@ -1,5 +1,5 @@
 ---
-title: 'Solution: window occupation with $C_0=34$, $C_1=0$, and the Route-S reproduction of the polylog frontier'
+title: 'The occupation implication'
 label: sec:sol-prop-mm-window-occupation
 ledger-node: prop:mm-window-occupation
 numbering:
````

Why the mathematics is unchanged: only the title changed. "The occupation implication" is the name the dossier's certified overview already gives `thm:sol-prop-mm-window-occupation` (small-gap branch $\Rightarrow$ occupation with $C_0=34$, $C_1=0$ on $[0,T_0(n)]$); the title omits the $\log^2n$ reproduction and the constants, so it claims less, and it asserts no uniform occupation estimate (the dossier's scope fence "Not the gate" is unchanged).

