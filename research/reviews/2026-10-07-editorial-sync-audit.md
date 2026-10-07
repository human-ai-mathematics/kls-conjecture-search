---
verdict: editorial
amends:
  - research/reviews/2026-08-27-kls-excess-repair-w0r2-proof-review.md
  - research/reviews/2026-08-27-kls-geometry-models-repair-proof-review.md
  - research/reviews/2026-09-06-lem-cmh-linear-spectral-resolution-proof-review.md
  - research/reviews/2026-09-06-lem-linear-sector-third-moment-proof-review.md
  - research/reviews/2026-10-01-chen-klartag-imports-review.md
  - research/reviews/2026-10-01-kl-rank-imports-review.md
  - research/reviews/2026-10-01-letwin-source-consequences-review.md
  - research/reviews/2026-10-04-aug25-grouped-pass.md
  - research/reviews/2026-10-04-aug25-repaired-review.md
  - research/reviews/2026-10-04-cmh-aug25-grouped-normalization-pass.md
authors:
  - orchestrator, claude-opus-5-5, 2026-10-07
reviewer: reviewer, claude-opus-5-5, 2026-10-07
changes:
  solutions/kls-excess-audit.md: {from: 7bee7f4a1a9b8ba39caa0e5e7531e98c2dc881820ab8c351cc34d3acfe1f19a2, to: e4d6c016bff97d1099c8ef8051730b5ef3a1f0d75d61baea86af0b35c33a24d1}
  solutions/kls-geometry-models.md: {from: 1965ddc1f7327dd2c2306f69421474aa1db15802a9a9eb0c11a1150a89d06a36, to: de8ac6d86f0695299309441a56a55dda8f6ebd83f48b7fb1b1e05b1e84d45c71}
  solutions/kls-localization-riccati-core.md: {from: ccedecb4338e4e6a9d9014a8405567e1f0dc0eb54048163cace46ee2af0b00c8, to: 1e3c71aece5d0b4c24c83d6311856b6c5515dfd2bb9503811c35508a85216881}
  solutions/kls-qcts-stein-boundary-core.md: {from: e8cf9f5d20ad409fe8039a4b5be3b5fa452e449e582f32f1bdb240a50e77628b, to: e31e3ec693b661cab83a1f932cc5c031db01f086c92d21ecccc3fc753d8e31e0}
  solutions/letwin-source-consequences.md: {from: 2c7a0adac8100dbb8da8035aaedb61db89333fa57496eda60ea8e44810184d2c, to: cd73a5be8b3531a4c237fd29a598f7be92f6a5ea7db571ff7a5cdfbd5a69c7a4}
  solutions/lem-cmh-linear-spectral-resolution.md: {from: 55d116e6f500be0c9e994e040ef840819021d5d27faf4797e4d4fc20a4dd18ad, to: 39e35c2937aaee3c550a9e3559163774b9edd196e3f8922fe8878d54b6685acb}
  solutions/lem-linear-sector-third-moment.md: {from: e8848fe4bd2a0acdf0e4860e41052129299cd9da4f71867f95453a0190d98329, to: 96c8408d830b267840269a175a60364e8eb0a0301d336f9dbd6eb14176ef83f5}
  solutions/thm-chen-klartag-imports.md: {from: 1cd92f8e0465b47d6d93837fdcc10890587522c44b784d9d2e4ecdb1d5e8a282, to: d09b6764955ca7c1edb36151bbbf3bb53b710691c69590a0ceb695a1e3ff3ae6}
  solutions/thm-cmh-normalization.md: {from: 429edd03fdd8a12bb845108ccb1149ff7638b895452d49548ca95e9836d35c43, to: d6f7cd40248d27e7d838a21223e7c34bba3aca0e4654e82c677dc548129812cc}
  solutions/thm-kl-rank-imports.md: {from: 4ada5470a4a7e9b21fd5e68ce6736af21ee25e83df2e5aed2f6bb6ac3f2ee50c, to: 135dbe486bac6dd30f8822b5db15152a583e7d71301b5f6de623e19037fc64f2}
---

# Editorial note on the sync follow-up to the site pass of 2026-10-07

After `2026-10-07-editorial-site-pass.md` and `2026-10-07-editorial-site-pass-window-occupation.md`, the orchestrator edited ten dossiers again following a sync audit: (a) five orientation lines now name two chapters instead of one; (b) six cross-references to chapter-level targets read "Chapter" instead of "Section". This note does not edit or replace the earlier notes; each `from` is the `to` recorded for that dossier in `2026-10-07-editorial-site-pass.md`, which is the fingerprint the checker currently expects.

The examination read only the diffs. Because `check.py --diff` finds no Git baseline for the intermediate versions (the earlier notes are uncommitted), the intermediate text was rebuilt by hand: undoing exactly the edits listed below in the current files reproduces, under the checker's fingerprint (`common.text_digest`), each recorded `from` value, for all ten dossiers. So no line other than those shown changed since the earlier note. Every target named in (a) and (b) labels a top-level `#` heading of a module, that is a chapter.

## (a) Orientation lines naming two chapters

```diff
 solutions/kls-excess-audit.md
-*Part of the fixed-cut archive, Chapter [](#sec:introduction); the reading order is on the [full proofs](#sec:proofs-archive) page.*
+*Part of the fixed-cut archive, Chapters [](#sec:introduction) and [](#sec:stein); the reading order is on the [full proofs](#sec:proofs-archive) page.*
 solutions/kls-geometry-models.md
-*Part of the fixed-cut archive, Chapter [](#sec:jacobi); the reading order is on the [full proofs](#sec:proofs-archive) page.*
+*Part of the shared technical foundations and the fixed-cut archive, Chapters [](#sec:models) and [](#sec:jacobi); the reading order is on the [full proofs](#sec:proofs-archive) page.*
 solutions/kls-localization-riccati-core.md
-*Part of the shared technical foundations, Chapter [](#sec:riccati); the reading order is on the [full proofs](#sec:proofs-archive) page.*
+*Part of the shared technical foundations, Chapters [](#sec:riccati) and [](#sec:carleson); the reading order is on the [full proofs](#sec:proofs-archive) page.*
 solutions/kls-qcts-stein-boundary-core.md
-*Part of the shared technical foundations, Chapter [](#sec:qcts); the reading order is on the [full proofs](#sec:proofs-archive) page.*
+*Part of the shared technical foundations, Chapters [](#sec:qcts) and [](#sec:stein); the reading order is on the [full proofs](#sec:proofs-archive) page.*
 solutions/letwin-source-consequences.md
-*Part of the shared technical foundations, Chapter [](#sec:qcts); the reading order is on the [full proofs](#sec:proofs-archive) page.*
+*Part of the shared technical foundations, Chapters [](#sec:qcts) and [](#sec:product-stress); the reading order is on the [full proofs](#sec:proofs-archive) page.*
```

Why the mathematics is unchanged: the statements, formulas, hypotheses, quantifiers, constants and steps read the same; only the navigational line after the front matter, outside every `prf:` directive, changed. It names where in the manuscript the dossier's statements are presented and asserts nothing about them; no step refers to it.

## (b) "Section" to "Chapter" for chapter-level targets

```diff
 solutions/lem-cmh-linear-spectral-resolution.md
-**Scope.** This dossier proves the candidate [](#lem:cmh-linear-spectral-resolution) of Section [](#sec:cmh-normalization): […]
+**Scope.** This dossier proves the candidate [](#lem:cmh-linear-spectral-resolution) of Chapter [](#sec:cmh-normalization): […]
-**Operator data.** Following [](#def:cmh) and the certified conventions of Section [](#sec:cmh-normalization), the Stein generator […]
+**Operator data.** Following [](#def:cmh) and the certified conventions of Chapter [](#sec:cmh-normalization), the Stein generator […]
 solutions/lem-linear-sector-third-moment.md
-$(\mathrm H1)$ and $(\mathrm H3)$ are the hypotheses. In the convention of Section [](#sec:notation), a log-concave measure […]
+$(\mathrm H1)$ and $(\mathrm H3)$ are the hypotheses. In the convention of Chapter [](#sec:notation), a log-concave measure […]
 solutions/thm-chen-klartag-imports.md
-The three manuscript directives in Section [](#sec:family-moment-map) read as follows
+The three manuscript directives in Chapter [](#sec:family-moment-map) read as follows
 solutions/thm-cmh-normalization.md
-**Scope.** This dossier discharges [](#rem:cmh-normalization) of Section [](#sec:moment-map-cmh): […]
+**Scope.** This dossier discharges [](#rem:cmh-normalization) of Chapter [](#sec:moment-map-cmh): […]
 solutions/thm-kl-rank-imports.md
-in Section [](#sec:covariance-tech).
+in Chapter [](#sec:covariance-tech).
```

Why the mathematics is unchanged: each edit replaces the word naming the kind of a cross-reference target; the target label, and hence the conventions or statements referred to, is the same. The one edit inside a proof (`lem-linear-sector-third-moment.md`) points to the same notation convention for log-concave densities, which the step uses unchanged. No formula, hypothesis, quantifier or constant changed.

## Findings

Re-reading only the diffs, no statement, formula, hypothesis, quantifier, constant or step of proof changed in any of the ten dossiers. The certifications of the ten amended reports carry over.

## Corrections

None.

## Exclusions

The proofs were not re-examined. No manuscript statement changed in this edit, so none is listed. Whether each orientation line names the most fitting chapters is an editorial question not examined here.
