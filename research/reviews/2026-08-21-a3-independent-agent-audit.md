# A3 independent-agent proof audit

- **Date:** 2026-08-21
- **Proof author:** `/root/a3`
- **Independent reviewer:** `/root/cross_review`
- **Certification:** `checked_by: agent`
- **Verdict:** pass for the two nodes listed below

## Certified scope

1. `prop:a3-horseshoe` — the exact weighted horseshoe Poincaré constant
   $C_{\mathrm{HS}}(\tau)=4$.
2. `thm:a3-block-gibbs` — conditional weighted tensorization with loss
   $1/\gamma_{\mathrm{blk}}$, including
   $\gamma_{\mathrm{blk}}=1-\rho_{\max}$ for two blocks.

The reviewed standalone artifacts are
[`solutions/prop-a3-horseshoe.tex`](../../solutions/prop-a3-horseshoe.tex) and
[`solutions/thm-a3-block-gibbs.tex`](../../solutions/thm-a3-block-gibbs.tex).

## Checks performed

The review checked the positive $E_1$ remainder identity, the induced intrinsic drift bound,
closure at the logarithmic pole, the trace-zero half-line estimate, the even-sector trace shift,
and the mean-corrected tail sequence proving sharpness. It separately checked conditional
variance tensorization, the two-projections identity, the HGR norm convention, non-attainment,
and the product endpoint. The final dossiers compile standalone.

The parity/trace argument in the final horseshoe proof replaces an unnecessary Sturm-theoretic
step and directly controls both even and odd sectors. No substantive gap remains within the
stated hypotheses.

## Explicit exclusions

This audit does not certify `thm:a3-product`, `prop:a3-hierarchical-prior`, the fixed-marginal
counterexample proof, the bounded-likelihood corollary, or a posterior-specific positive lower
bound on $\gamma_{\mathrm{blk}}$. Those items retain their previous status.

The fixed-marginal counterexample subsequently received a separate independent review on
2026-08-22; see
[`2026-08-22-a3-marginals-independent-audit.md`](2026-08-22-a3-marginals-independent-audit.md).
That later audit does not alter the scope of this report.
