# CMH Gamma-completion Bochner provenance repair

- Date: 2026-08-27
- Role: `/root/repair_cmh_hodge_domain_w3`
- Dossier: `solutions/thm-cmh-dirichlet.tex`
- Refined node: `lem:cmh-gamma-completion`
- Previous dossier SHA-256: `093a075de109d732f711468b3879cf5e2cda2c931027e15e0464e23d92704f46`
- Repaired dossier SHA-256: `d7289c45bac18b0faea999d2642cfe04b4b7b1341526a25f69722e05c3a756ec`
- Certification state: `checked_by: none`

## Repair and coefficient audit

The Gamma-lift subsection now identifies its input explicitly as
`prop:cmh-bochner`. For independent $Y_i\sim\Gamma(\alpha_i,1)$, center by
$X_i=Y_i-\alpha_i$. Translation leaves derivatives unchanged, and the canonical product-Gamma
moment Hessian is

$$
H_\Gamma=\operatorname{diag}(Y_1,\ldots,Y_m).
$$

Writing $\rho_\Gamma$ for the product density gives

$$
\operatorname{Div}_\Gamma(H_\Gamma\nabla G)
=\sum_i\rho_\Gamma^{-1}\partial_i(\rho_\Gamma Y_iG_i)
=\sum_i\bigl(Y_iG_{ii}+(\alpha_i-Y_i)G_i\bigr)
=\mathcal L_\Gamma G.
$$

Specializing the integrated Bochner identity therefore yields

$$
N_\Gamma(G)=\mathbb E(\mathcal L_\Gamma G)^2
=\mathbb E\left[\sum_iY_iG_i^2+\sum_{i,j}Y_iY_jG_{ij}^2\right].
$$

The Hessian sum is over ordered pairs because
$\operatorname{Tr}(H_\Gamma D^2G H_\Gamma D^2G)
=\sum_{i,j}Y_iY_jG_{ij}G_{ji}$ and $D^2G$ is symmetric. Thus each off-diagonal square occurs
twice when grouped by unordered pairs; there is no missing factor of $2$ or $1/2$. The proof of
the row completion now explicitly identifies
$\mathbb E[Y_iG_i^2+\sum_jY_iY_jG_{ij}^2]$ as the $i$th Bochner row. Summing rows therefore
produces exactly $N_\Gamma$, after which the existing coefficient
$\alpha_i^2/(\alpha_i+1)^2$ and
$\delta_i=\alpha_i^2/(\alpha_i+1)^2-1/4$ remain unchanged.

No theorem statement, constant, parameter range, or downstream argument was changed. The dossier
has no applicable `bounded_by` fence and uses no numerical evidence.

## Validation

`cd solutions && latexmk -pdf -outdir=../build thm-cmh-dirichlet.tex` succeeded and produced a
6-page PDF. The log contains no TeX error, undefined control sequence, emergency stop, or fatal
error; unresolved cross-manuscript references are expected for a standalone dossier.
`git diff --check` passes for the dossier.

No ledger delta is applicable before independent review. The future solution path remains
`solutions/thm-cmh-dirichlet.tex`.

```yaml
outcome: complete
artifacts:
  - solutions/thm-cmh-dirichlet.tex
  - research/explorations/2026-08-27-prover-cmh-gamma-bochner-repair-w3p01.md
proposed_deltas:
  - none until an independent proof-checker certifies dossier SHA-256 d7289c45bac18b0faea999d2642cfe04b4b7b1341526a25f69722e05c3a756ec
next_role: proof-checker
next_prompt: |
  Cold-review solutions/thm-cmh-dirichlet.tex at SHA-256
  d7289c45bac18b0faea999d2642cfe04b4b7b1341526a25f69722e05c3a756ec, focusing on
  lem:cmh-gamma-completion. Verify that the product-Gamma law, centered by X_i=Y_i-alpha_i,
  has H_Gamma=diag(Y_i), that Div_Gamma(H_Gamma grad)=L_Gamma, and that specializing
  prop:cmh-bochner gives exactly sum_i Y_i G_i^2 plus the ordered-pair Hessian sum
  sum_ij Y_i Y_j G_ij^2 with no coefficient error. Then verify that these rows sum to
  N_Gamma in the existing completion proof. The statement is unconditional on alpha_i>=1,
  has no bounded_by fence, and the standalone build succeeds.
```
