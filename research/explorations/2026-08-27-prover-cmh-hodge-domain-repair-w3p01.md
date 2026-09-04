---
type: exploration
date: "2026-08-27"
outcome: proposed
nodes:
  - prop:cmh-hodge
---
# CMH Hodge operator-domain repair

- Date: 2026-08-27
- Role: `/root/repair_cmh_hodge_domain_w3`
- Dossier: `solutions/thm-cmh-normalization.tex`
- Refined node: `prop:cmh-hodge`
- Previous dossier SHA-256: `53c94a296e3efb2bce3f8bd3f3fb353c40b55c06f2748e50cbfd0457f401ead7`
- Repaired dossier SHA-256: `1a241c1b1e1dfa2b417626661d9cc555f5cefeeb480b21b37695a56726826a38`
- Certification state: `checked_by: none`

## Repair

The Hodge subsection now defines
$\mathcal A_1=-\operatorname{Div}_\mu(\Sigma\nabla\,\cdot\,)$ as the closed nonnegative
self-adjoint operator associated with the covariance form, sets
$L^2_0(\mu)=(\ker\mathcal A_1)^\perp$, and records the centered inverse

$$
\mathcal A_1^{-1}:L^2_0(\mu)\longrightarrow
\operatorname{Dom}(\mathcal A_1)\cap L^2_0(\mu).
$$

The proposition now assumes exactly that $g\in\operatorname{Dom}(\mathcal A)$,
$u=H\nabla g\in L^2(\mu;\Sigma^{-1})$, and
$h=\mathcal A g=-\operatorname{Div}_\mu u\in L^2_0(\mu)$, then defines
$\psi=\mathcal A_1^{-1}h$ and $w=u-\Sigma\nabla\psi$.

For the domain check, the proof introduces the closed covariance gradient
$G_\Sigma f=\Sigma\nabla f$ from $H^1_\Sigma(\mu)$ to
$L^2(\mu;\Sigma^{-1})$. Its adjoint is the weak operator
$G_\Sigma^*=-\operatorname{Div}_\mu$ and
$\mathcal A_1=G_\Sigma^*G_\Sigma$. Thus $u,G_\Sigma\psi,w$ lie in the required adjoint
domains, $G_\Sigma^*w=0$, and the Hodge orthogonality is the valid adjoint pairing
$\langle G_\Sigma\psi,w\rangle=\langle\psi,G_\Sigma^*w\rangle=0$. The same Pythagorean
calculation proves the claimed minimal-field property.

Finally,

$$
\|G_\Sigma\psi\|^2
=\langle h,\mathcal A_1^{-1}h\rangle,
$$

and the spectral variational formula gives
$\|\mathcal A_1^{-1}\|=\mathsf C_{P,\mathrm{aff}}(\mu)$. This uses only the ordinary
dimension-dependent finiteness of the spectral gap for a fixed full-dimensional log-concave
measure, not a dimension-free KLS estimate.

## Scope and fences

The repair changes no theorem beyond the stated regular moment-map class and introduces no
unstated premise. Route C has no applicable `bounded_by` edge. In particular, no projection-only
or fixed-cut estimate is used, and no equivalence with the trace-upgrade cluster is asserted.
The other six nodes covered by the dossier were not mathematically altered.

## Validation

`cd solutions && latexmk -pdf -outdir=../build thm-cmh-normalization.tex` succeeded and produced
`build/thm-cmh-normalization.pdf` (6 pages). The remaining unresolved cross-manuscript references
are the standalone behavior allowed by `solutions/README.md`; the log contains no TeX error,
undefined control sequence, emergency stop, or fatal error. `git diff --check` passes for the
dossier.

No ledger delta is applicable before independent review. The future solution path remains
`solutions/thm-cmh-normalization.tex`.

```yaml
outcome: complete
artifacts:
  - solutions/thm-cmh-normalization.tex
  - research/explorations/2026-08-27-prover-cmh-hodge-domain-repair-w3p01.md
proposed_deltas:
  - none until an independent proof-checker certifies dossier SHA-256 1a241c1b1e1dfa2b417626661d9cc555f5cefeeb480b21b37695a56726826a38
next_role: proof-checker
next_prompt: |
  Cold-review solutions/thm-cmh-normalization.tex at SHA-256
  1a241c1b1e1dfa2b417626661d9cc555f5cefeeb480b21b37695a56726826a38, focusing on
  prop:cmh-hodge. Verify the closed covariance generator setup, the domains of G_Sigma and
  its adjoint, the weak divergence identities, Hodge orthogonality and minimality, and the
  spectral variational identity ||A_1^{-1}||=CP_aff. The statement assumes g in Dom(A),
  H grad g in L^2(mu;Sigma^{-1}), and A g in L^2_0; Route C has no bounded_by fence. The
  standalone build succeeds with only expected unresolved cross-manuscript references.
```
