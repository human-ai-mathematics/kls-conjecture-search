---
---

# Completion of the residual-dichotomy certification task

## Question examined

Complete the temporary `TODO-cor-dichotomy.md` on branch `certify-open-results`, following the researcher, independent certification, orchestrator, writer, and read-only sync circuit. The node is `cor:dichotomy`; the related research route is `ap:e-taming-splitting` and the program target remains `conj:kls`.

## What we learned

*Established, independently certified:* `cor:dichotomy` now has a proof record selecting `solutions/cor-dichotomy.md` and `research/reviews/2026-10-01-cor-dichotomy-certification.md`. Its sole antecedent is `ass:absolute-geometric-completion`, recorded in `assumes`, while its proof dependencies remain proved or defined. The review checks the complete argument and the separate matched-time discussion.

*Established:* the original premise required a mathematical repair, not just a ledger change. The stopping width and a uniform positive tolerance for balanced near-minimizers are now explicit. The corollary states its large-dimension threshold and the dependence of its constants. Exactly these two canonical statements changed; no prior certification was lifted. The reasons are recorded in `research/explorations/2026-10-01-dichotomy-quantifier-repair.md`. The Letwin comparison and the separate matched-time sufficient condition were moved to explanatory prose.

*Observed from the audit and checks:* the fresh sync reviewer found agreement between the canonical statements, dossier, selected review, ledger, and brief. Its single requested prose correction was applied verbatim by the writer: the Summary now points to `prop:intro-audit` rather than asserting a status by hand. The initial and final statement snapshots differ only at the two intended nodes. Both writer passes preserve all canonical statement fingerprints. The final full check passed with 132 nodes: 4 defined, 20 open, 106 proved, and 2 refuted. There are no draft dossiers, and `git diff --check` passes.

*Observed:* all requested items of the temporary TODO are accounted for; the TODO is removed following its own deletion instruction. Existing branch work is preserved. No commit, publication, or human acceptance was performed.

## What resists

`ass:absolute-geometric-completion` remains open. The certified implication does not discharge it or settle `conj:kls`. The separate KLS discussion needs the additional covariance estimate at the completion's exact time; `conj:taming` does not automatically supply a matching time. Consequently `ap:e-taming-splitting` stays active: its geometric/covariance bridge objective has not been completed, and no portfolio transition is justified by certifying this conditional consequence.

## Proposed next step

Future work on `ap:e-taming-splitting` must address its geometric bridge and the exact quantified completion or matched-time covariance estimate. No further certification action remains from this TODO.
