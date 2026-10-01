---
---

# Terminology in four statements, carried over without new review

This checkpoint records an editorial exception, decided by the project's maintainer as part
of the reorganisation around the four approaches. It changes no mathematical status: the
ledger keeps 131 nodes (86 proved, 39 open, 4 defined, 2 refuted).

## What changed

The editorial pass glossed internal jargon and unified the approach names in the prose,
but it could not touch a labelled statement. The maintainer authorised renaming the
leftovers inside statements, and carrying the certifications over without a new review,
because only wording changed and the mathematics did not.

- Fingerprinted statements, with their title or sentence:
  - `conj:mm-spectral-occupation`: "Fixed-eigenfunction full-damping occupation" became
    "Occupation bound for a fixed eigenfunction, against the full damping".
  - `conj:cmh-second-variation`: "Second variation of CMH at the product endpoint" became
    "Second variation of CMH at products, where it equals 4".
  - `thm:cmh-implies-affine-poincare`: "Endpoint reduction for [](#rem:cmh-normalization)"
    became "CMH bounds the affine Poincaré constant, normalized as in
    [](#rem:cmh-normalization)".
  - `cor:single-coordinate-cuts`: "the conclusion that the program derives" became "the
    conclusion that the fixed-cut approach derives".
- Remarks, which are not fingerprinted:
  - `rem:cmh-normalization`: "…and endpoint reduction" became "…and the reduction to KLS".
  - `rem:cmh-program`: title "Program of the moment-map approach"; "the CMH endpoint and
    its KLS reduction" became "the target inequality CMH and its reduction to KLS".
  - `rem:trace-upgrade-unification`: "the Eldan–A gap" became "the gap of variant E–A".

## The exception

`research/reviews/` is append-only, and an edited statement normally loses its
certification until a new review. Here, ten reports had only the recorded fingerprint of
the renamed statements replaced, from the old value to the new one. Nothing else in them
changed: verdicts, authors, bodies and the other fingerprints are as before.

| Statement | Old fingerprint | New fingerprint |
|---|---|---|
| `conj:cmh-second-variation` | `2175a5534f35115640c3409f698948e52920594ceb958557496c73a88252bb6d` | `7d114bd6b5093fe463a530e4bfbdca19af579254709892c1f7f897d53937c628` |
| `conj:mm-spectral-occupation` | `fd459923a0b85e2a9af9179faa1e1e80bbe2357831a49d986221586cfd268249` | `faf6c8299eb2e6ec3ac6c1489b1b6541ae018312780e3afe1fd47b43d0448ee3` |
| `cor:single-coordinate-cuts` | `50f836a8a6885da08f837ec667d19b41a722b0e356f8c44acf5bd11b745a8a67` | `2bcff88762d7f2da4e2f52f0181f2fbdc0c5ded77931063daf7352b5bab575ae` |
| `thm:cmh-implies-affine-poincare` | `a977e03d84125ce8a015dfb75d67908808162ecd70b71221781d8a750ec5d9c4` | `9210ad8934e1f76e3f1f621274c0be2dc1c9e5fa106146b66584871844acd5e0` |
