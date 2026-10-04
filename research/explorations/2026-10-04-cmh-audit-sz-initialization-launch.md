---
---

# Parallel missions: CMH certification audit and conditional initialization

## Question examined

Launch the user's two requested missions in parallel: a fresh grouped audit of
the twelve CMH nodes still citing the August-25 reports, and a researcher on
`ap:sz-conditional-initialization`. Shared provenance and earlier discovered
defects motivate scrutiny; they are not evidence that a new claim is false.

## What we learned

*Observed from the ledger.* The twelve requested nodes use two dossiers:

| Dossier | August-25 consumers |
|---|---|
| `solutions/thm-cmh-normalization.md` | `prop:cmh-bochner`, `thm:cmh-implies-affine-poincare`, `prop:letwin-not-gate-zero` |
| `solutions/thm-cmh-dirichlet.md` | `thm:cmh-1d`, `thm:cmh-product`, `cor:cmh-linear-images`, `lem:cmh-row-min`, `lem:cmh-angular-coefficient`, `thm:cmh-dirichlet`, `cor:cmh-dirichlet-surplus`, `cor:cmh-dirichlet-poincare`, `cor:cmh-product-saturation` |

Three further current consumers use these same dossiers with August-27
certifications: `prop:cmh-hodge`, `cor:cmh-hodge-comparison`, and
`lem:cmh-gamma-completion`. The reviewer examines the whole two-dossier
argument and explicitly distinguishes the twelve requested nodes from these
three additional claims. Its total scope is fifteen current consumers.

The reviewer must check operator domains and approximation in the CMH bridge,
the exact logical scope of the Letwin matrix countermodel, and every
one-dimensional, product and Gamma-to-Dirichlet input. It must identify the
downstream impact of any defect, especially through
`cor:cmh-dirichlet-poincare` to `lem:fiber-polynomial-floor`.

*Observed from the portfolio.* The active initialization route is already
registered, with its mandate in
[the route checkpoint](2026-10-04-sz-conditional-initialization-route.md).
Its candidate is `cand:sz-uniform-conditional-initialization`, whose canonical
statement is in [the Wave A contract](2026-10-04-wave-a-sz-contract.md).
The researcher starts from the exact terminal-transfer expression, retaining
the adjacent-degree ratio and top Appell derivative. It tests whether the
low-degree loss can be removed or paid uniformly over the entire moving
degree range, under the universal regular-law curvature-profile antecedent.

*Observed (execution).* `cmh_aug25_grouped_review` was launched as a
`reviewer` with `fork_turns: none`, repository paths, and a full `certify`
mission. `sz_conditional_initialization` was launched as a `researcher`
with the `prove` lens and ownership of new research records only. Neither
may edit the shared program state. The CMH dossiers remain frozen during
their first examination. The working tree was clean at launch and the
initial full checker passed.

## What resists

Old unknown model identities do not settle correctness. Passing a source
formula does not settle its domain, closure or quantified consequence.
No certification is withdrawn solely because this audit begins.

On the Song–Zhang side, separate success at fixed degrees does not initialize
the full depth-dependent range. The curvature-profile antecedent cannot be
discarded. Failure of a sufficient scalar estimate is not a counterexample
to the candidate, and initialization alone does not supply the uniform
comparison interfaces of the contract.

## Proposed next step

Integrate the independent review's exact passing scopes or complete repair
instructions, retaining all earlier reports. Evaluate the researcher's
derivation as a proof draft, exact obstruction, or unresolved reduction with
its precise next test. Obtain fresh certification before any mathematical
status change, and keep the recovery probe and occupation comparison outside
these two initial missions.
