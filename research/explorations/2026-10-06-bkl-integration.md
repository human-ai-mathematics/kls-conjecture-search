---
---

# BKL v1: reconstruction and continued alternative-proof research

## Question examined

Integrate Bizeul–Klartag–Lehec, arXiv:2610.05474v1, into the claim graph while
preserving the open objectives of the existing programme. The porter's explicit
instruction is to preserve mathematically viable alternatives after KLS is
settled. This checkpoint records import decisions, not a proof certification.

## What we learned

*Observed in the versioned source.* Theorem 1.1 announces a dimension-free
Poincaré bound. The source is pinned at
<https://arxiv.org/abs/2610.05474v1>; its HTML was downloaded from the matching
arXiv URL to a temporary local file for reconstruction.

*Established as a structural change.* The framework permits active alternative
routes after a target is proved, while preserving the checks on refuted targets
and resolved blockers. See the separate framework checkpoint. This changes no
mathematical status. The full baseline validation passed outside the sandbox;
inside it the Node subprocess returned no npm version. No dependency upgrade
or alteration of MyST was needed.

*Decision.* `ap:bkl-reconstruction` is the first priority, with six dossiers
covering sections 2–7. The interfaces are `lem:bkl-analytic-foundations`,
`lem:bkl-tensor-symmetrization`, `thm:bkl-tilt-criterion`,
`prop:bkl-tilt-appell-duality`, `lem:bkl-cumulant-dynamics`,
`lem:bkl-cumulant-energy`, `thm:bkl-cumulant-bound`,
`prop:bkl-suspension` and `thm:bkl-tilt-bound`. Definitions are fixed in
`def:bkl-tilt-cumulants`. All non-definition imports start open. `conj:kls`
is kept as the sole canonical target; no duplicate KLS statement is introduced.

*Decision.* All ten existing active routes and six blocked routes retain their
states on import. `ap:sz-induction-contract` was already closed; its successor
is `ap:sz-conditional-initialization`. In particular, a certification of
`cor:bkl-uniform-conditional-initialization` would settle a mathematical
objective without making an independent proof attempt impossible.

*Clarification of the suspension reconstruction checkpoint.* Its proposed
closing of the accomplished startup route is not adopted. Only the candidate's
promotion/resolution is to be recorded after review; the route remains active
with an explicit independent-proof objective. A BKL-dependent proof cannot
serve as evidence that the older method supplies a BKL-independent proof.

## What resists

Every imported proof requires independent review of the source argument and
its local formulation. The degree/dimension quantifiers, analytic domains,
localization martingales and limit passages are audit obligations, not assumed
consequences of the source's announcement. The current statement-level DAG
cannot automatically certify independence of several proofs.

## Proposed next step

Finish the dossiers, review foundations and dynamics first, then energy,
cumulant induction, suspension and the spectral conclusion. Register only
passing records, and review the composed chain before changing `conj:kls`.
Bring `sec:bkl-proof`, the overview, the atlas and the synthesis into agreement
with the final ledger, and record that milestone in a new checkpoint. Do not
rewrite this import snapshot or close viable alternative routes.
