---
---

# Letwin's general KLS bridge and its admissible time

## Question examined

Lens `prove`, point 2 of `TODO-letwin-follow-up.md`: reconstruct the passage
from `prop:letwin-kappa` and `thm:letwin-qcts` to the new
`thm:letwin-kls`. Author: researcher_letwin, gpt-6-astra. The work concerns
the route-agnostic literature bound, not completion of `conj:kls`.

## What we learned

*Established, awaiting independent review:* the argument is written in
`solutions/thm-letwin-kls.md`. Gaussian observation and conditional
variance give the full factor $2+tC_P(\mu)$ in the transfer. Milman's
published Lipschitz-variance comparison and the improved Lichnerowicz
input then give a spectral bound when that factor is bounded.

*Established, awaiting independent review:* choose the minimum of the
Klartag--Lehec covariance-window time and $1/C_P(\mu)$. One branch gives
the desired window bound; the other bounds $C_P(\mu)$ by a universal
constant. This removes any need to assume the unknown spectral gap is
large enough to permit the whole covariance-window time. The constant
branch is absorbed using centered exponential products and $n\ge2$.

The sources are pinned to Letwin 2607.24164v1, Klartag 2303.14938v2
(the published version), and Klartag--Lehec 2203.15551v2. The dossier
records the exact published theorem inputs and all normalization changes.
Klartag's regular approximation, followed by affine whitening, removes
the temporary regularity hypothesis without a limit of eigenfunctions.
The edge to `thm:letwin-qcts` explicitly discharges the antecedent of
`prop:letwin-kappa`. `thm:klartag-logn` is not used.

## What resists

No further proof step is left as an author-identified gap in this draft.
This is not a certification. The covariance-window theorem, improved
Lichnerowicz, Milman's comparison, qualitative finiteness, and regular
approximation remain explicitly identified published inputs. The method
retains its logarithmic dimension dependence and supplies no KLS proof.

## Proposed next step

Request a fresh independent `certify` review of `thm:letwin-kls` against
the canonical statement in module 04. Check the direction and scope of
each published input, the conditional-variance bridge, the minimum-time
dichotomy, uniformity of constants, affine approximation, and the
reverse-Cheeger normalization. Run the full checker and record fresh
dossier and canonical-statement fingerprints in a new review. Leave the
node open until the review passes.
