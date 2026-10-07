---
---

# BK integration: final independent synchronization audit

## Question examined

Check agreement of the three-proof manuscript with the ledger, dossiers,
references, brief and portfolio after completing `ap:bk-reconstruction`.
The reviewer used its independent context and the `sync` lens, which returns
a handoff rather than writing a proof certificate. This checkpoint persists
that audit and the resulting corrections; it is not a new proof review.

## What we learned

*Observed by the independent reviewer.* All 192 canonical statement fingerprints
match the snapshot taken after the explicit approximation clarification. All
178 preexisting statements are unchanged from the initial snapshot. Twelve BK
assertions and two definitions agree with their dossiers and dependency edges.
The three KLS compositions agree with their certified inputs. Their actual
proof dependency closures contain neither the target as a premise nor another
proof's closing inputs. All preexisting portfolio entries retain their states
and objectives; only the completed BK reconstruction route was added and closed.

The final proof certificates and editorial notes are recorded in the ledger
and under `research/reviews/`. Certification of the three source proofs means
independent agent review of the specified versions, not journal refereeing.
The final comparison places all three proofs side by side and distinguishes
the qualitative exponential endpoint from BK's own quantitative scalar conversion.

*Corrections made following the audit.*

- The reading path now presents SZ v1 as preparation for the three complete
  proofs, rather than ambiguously listing it as one of them.
- A remaining overview sentence now names all three closing mechanisms.
- The TODO no longer says BK avoids all higher cumulants: cumulants occur in
  the moving-Appell calculation, but no uniform higher-cumulant theorem is an
  input and no suspension is used.
- The induction scales are $q=1$ initially, then $q=\lfloor d/2\rfloor$ with
  observation degree $D=\lfloor\sqrt d\rfloor$. A preliminary suggestion to
  replace $q$ by $\lfloor\sqrt d\rfloor$ was withdrawn after checking the
  source and dossier; it was never applied.
- The brief names the current dependency-extension review for the two older
  KLS compositions, while retaining the earlier reports as history.
- Obsolete draft-status sentences were replaced by timeless descriptions of
  dependencies. Three append-only editorial notes independently verified the
  exact baseline hashes and unchanged mathematical scope: the outer,
  input-status and localization-status notes. No old report was rewritten.

*Provenance correction.* Extend the correction in
`2026-10-06-bk-provenance-correction.md` to
`research/reviews/2026-10-06-kls-proof-dependency-extension-review.md` as well:
the supplied canonical-author model tag `gpt-6.1-sol` was not verified by
runtime metadata and should be read as `unknown`. This changes no author or
reviewer identity, role separation, mathematical text or certification. The
configured researcher and reviewer model is `gpt-6-astra`.

## What resists

No remaining mathematical or prose discrepancy was identified in the BK
integration scope after those corrections. No claim is made that agent review
replaces human scrutiny. No stronger structural statement about the alternative
mechanisms or optimal KLS constant follows from this integration.

## Proposed next step

Run the final full structural check on this state and keep publication manual.
The human reading checklist includes the BK chapter, explicit-constant dossier,
KLS composition and comparison. No deployment, merge or publication was performed.
