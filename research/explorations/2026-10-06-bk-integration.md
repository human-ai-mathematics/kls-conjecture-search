---
---

# BK: pinned source and reconstruction interfaces

## Question examined

Integrate the proposed Balasubramanian–Kasiviswanathan proof of `conj:kls`,
including its explicit constant, along `ap:bk-reconstruction`. The user approved
full reconstruction and independent review, with an honest unresolved outcome if
an argument fails. Publication and merging are outside this task.

## What we learned

*Observed.* The source is K. Balasubramanian and S. Kasiviswanathan,
*A Dimension-Free Bound on the Poincaré Constant of Isotropic Log-Concave Measures*,
53 pages, pinned to GitHub `kriznakumar/paper` commit
`4837c33649ba2271f43c9684e9350ecbdd725f95` (commit timestamp
2026-10-06 03:15:17 UTC), consulted 6 October 2026:
<https://github.com/kriznakumar/paper/blob/4837c33649ba2271f43c9684e9350ecbdd725f95/KLS.pdf>.
The PDF SHA-256 is
`8b298d3b4fd7b565fd35e43032990840c94faa7e03e3bc9aa980b476b2adc14c`.
The commit timestamp is not an assertion about priority or first public availability.
The PDF and extracted text are temporary working copies; the permanent URL and
hash identify the examined source.

*Established by direct comparison, not a new certification.* Source equations
(2.2)–(2.4) give exactly the existing Appell normalization, since positive-degree
polynomials are centered and tensor norms use ordered indices. Source (2.8) is
exactly the certified input `thm:letwin-qcts`. The covariance-at-most-identity
extension is by linear contraction on the support.

*Decision.* Register source claims as open, definitions as defined. Reconstruct
Hodge (Lemma 3.1, Appendices A–B), integration (§4), powers (Lemma 5.1,
Appendix C), localization (§6, Appendix D), reverse transfer (Proposition 7.1),
coefficient closure (Theorem 8.1, Appendix E), approximation (Appendix F),
and scalar conversion (§9, Appendix G). The last two conclusions are distinct:
`thm:bk-appell-bound` fits `prop:sz-exponential-coefficients-equivalence`, but
the explicit constant requires BK's own conversion.

*Observed.* The initial sandboxed full check failed at npm discovery; its
missing-anchor errors were consequences of that build failure. Repeating the
full checker with the required environment access completed with zero errors
before any repository edit. The two untracked TODO files predate this work.

## What resists

None of the new proof assertions is certified by this import. The coefficient
supremum must not be assumed finite in the induction; the operator comparison
must hold on its actual domains, uniformly in rank; localization must justify
its martingales and moments. Each proof must exclude the already proved KLS
conclusion and the BKL/SZ v2 coefficient bounds as inputs.

## Proposed next step

Reconstruct independent blocks and review the stabilized statements and dossiers.
Only passing independent reviews may change statuses. Bring `sec:bk-proof` and
the comparison into agreement with the resulting status. Existing CMH Hodge
analysis does not identify BK's rank-uniform compatible-tensor mechanism; record
that distinction without a priority claim.
