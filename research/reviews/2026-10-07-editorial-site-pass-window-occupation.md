---
verdict: editorial
amends:
  - research/reviews/2026-10-01-window-occupation-empty-branch-review.md
authors:
  - orchestrator, claude-opus-5-5, 2026-10-07
reviewer: reviewer, claude-opus-5-5, 2026-10-07
changes:
  solutions/prop-mm-window-occupation.md: {from: 84396ef917be9eaa7bc45cf05f0a6f9e83424a6625d55416658d7c05c09100ed, to: b60447ac207a5bcb305b59df9c24faa34a6e0611743a83055217b3944f4a7752}
---

# Editorial note on `research/reviews/2026-10-01-window-occupation-empty-branch-review.md`

Companion to `2026-10-07-editorial-site-pass.md`, examined in the same pass. It is a separate note because that note also amends `2026-10-01-spectral-window-letwin-discharge-review.md`, which fingerprints this dossier at an older version than the one the empty-branch review certifies; one note cannot give this dossier two `from` values. This note carries over only the empty-branch review's certification of `solutions/prop-mm-window-occupation.md`.

## `solutions/prop-mm-window-occupation.md`

```diff
@@ -6,6 +6,8 @@
    enumerator: D22.%s
 ---
 
+*Part of the fixed-eigenfunction mechanism, Chapter [](#sec:spectral-approach); the reading order is on the [full proofs](#sec:proofs-eigenfunction) page.*
+
 **Overview.** This dossier gives the occupation implication [](#thm:sol-prop-mm-window-occupation) with constants $C_0=34$, $C_1=0$ on $[0,T_0(n)]$, […]
```

Why the mathematics is unchanged: the statement, formulas, hypotheses, quantifiers, constants and steps read the same; only one navigational line was added after the front matter, outside every `prf:` directive. It names the chapter and the reading-order page; it asserts nothing about the dossier's theorem, and no step refers to it. `check.py --diff` shows no other change to this dossier.

## Findings

The mathematics is unchanged; the certification of the amended report carries over.

## Corrections

None.

## Exclusions

The proof was not re-examined. The older fingerprint of this dossier recorded in `2026-10-01-spectral-window-letwin-discharge-review.md` is not addressed here.
