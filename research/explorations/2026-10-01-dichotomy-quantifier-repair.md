---
---

# Quantified completion for the residual dichotomy

## Question examined

Prove `cor:dichotomy` on the near-worst fixed-cut route `ap:e-taming-splitting`, after determining whether its exact antecedent and its matched-time KLS sentence define sufficient hypotheses. Starting lens: prove. Author: dichotomy researcher, gpt-6-astra, 2026-10-01.

## What we learned

*Established, uncertified:* the implication now stated in `cor:dichotomy` has the full argument in `solutions/cor-dichotomy.md`. Its theorem repeats the stabilized canonical statement verbatim. The original `ass:absolute-geometric-completion` left the stopping width free and used an undefined balanced near-Cheeger class. The orchestrator's repair fixes the width to the clean bootstrap choice and introduces a positive uniform initial-excess tolerance. Its quantifiers cover every dimension at least two, every near-worst isotropic log-concave law, and every balanced measurable cut within that tolerance. No exact perimeter minimizer is assumed.

*Established, uncertified:* choosing the dimension threshold so that the published covariance window lies below the completion time resolves the time restriction in `cor:loglog`. Choosing the near-worst tolerance below the bootstrap and completion tolerances resolves both measure restrictions. The supply threshold and the contradiction threshold require separate smallness choices; their minimum supplies a constant with dependence on the completion constants, rather than a misleading dependence on its error parameter alone.

*Established, uncertified:* the separate matched-time remark in the dossier proves that a sufficiently small covariance-interface estimate at the completion's exact time would yield KLS. The quantifiers in `conj:taming` alone do not match that time. This sentence was removed from the canonical corollary and retained as a precise conditional discussion. The proof takes balanced near-minimizers first and then arbitrarily accurate near-worst measures; the latter limit is necessary for its stated sharp perimeter-derived lower bound.

*Observed from repository metadata:* before these changes, the completion assumption had no existing certification fingerprint referring to it. Its only dependent node was the open corollary. Thus repairing these two statements did not lift an existing certification. The implication's completion belongs in `assumes`, not `depends_on`. There are no registered `bounded_by` edges on the target; the dossier checks the contextual circularity, crude-input, relative-scale and spectator constraints explicitly.

## What resists

`ass:absolute-geometric-completion` remains an open antecedent. `conj:taming` remains open and also requires a matched-time condition for the separate KLS argument. Certifying the implication does not establish either premise or close `ap:e-taming-splitting`.

## Proposed next step

Have a fresh reviewer check the stabilized `cor:dichotomy`, `ass:absolute-geometric-completion`, and `solutions/cor-dichotomy.md`, including the infimum arguments, finite-dimensional positivity, constant choices, window restriction, and stopping width. Keep the separate matched-time remark outside any assertion that the completion or covariance estimate has been established. No route-state change is proposed.
