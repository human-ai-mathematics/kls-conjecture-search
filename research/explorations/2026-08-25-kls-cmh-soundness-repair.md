---
---
# KLS CMH soundness repair

Date: 2026-08-25

## Trigger and scope

An adversarial audit of the new deterministic moment-map/CMH layer found that the repository had
promoted a partial review as though it were an unqualified proof certificate. The underlying
normalization and exact-case statements were largely repairable, but their manuscript proofs,
scope language, numerical provenance, and ledger metadata did not yet satisfy the R2 contract.
This repair addresses that CMH layer and adjacent KLS control-plane drift. It does **not** prove
universal $\mathrm{CMH}(4)$ or KLS.

The original partial report
`research/reviews/2026-08-25-kls-cmh-normalization-audit.md` remains unchanged as proof history.
Dead ends and corrections below supersede claims operationally without rewriting that record.

## Mathematical repairs

### Normalization dossier

- The integrated Bochner identity is now proved by an explicit target-coordinate index
  calculation. The cancellation uses the moment-map Codazzi tensor
  $H_{mj}\partial_jH_{k\ell}=\varphi_{mk\ell}$ and its total symmetry. The discarded proof idea
  tried to obtain the identity from symmetry, positivity, and the Stein identity alone; the
  historical audit gives a Gaussian non-Hessian Stein-kernel counterexample to that argument.
- The endpoint proof no longer commutes a spectral projection of
  $\mathcal A=-\operatorname{Div}_\mu(H\nabla\cdot)$ with the unrelated constant-$\Sigma$
  Dirichlet form. It instead uses the direct pairing
  $\|\Pi_{\varepsilon,R}f\|_2^2=\langle f,\mathcal A g_{\varepsilon,R}\rangle$ and one
  $\Sigma$-metric Cauchy--Schwarz step.
- The unbounded-$H$ domain gap is closed on
  $\mathbb R+C_c^\infty$: bounded gradients and $\mathbb EH=\Sigma$ give finite $H$-energy.
  Density is then taken in the constant-$\Sigma$ Sobolev norm; no implication from finite
  $\Sigma$-energy to finite $H$-energy is asserted.
- The Hodge signs were corrected. The certified conclusion is
  $C_{\mathrm{CMH}}\ge C_P^{\mathrm{aff}}$ plus a nonnegative solenoidal channel. No separating
  log-concave measure is known, so equivalence and strict non-implication remain open.
- The algebraic countermodel presentation now has the correct block order, strict Schur
  complement, and noninteracting $O(m)$ sectors; the scalar sector remains a two-dimensional
  block with deficit $(a-dt)^2$.

The former all-measures normalization question was split. `q:cmh-normalization` is proved only
on the regular moment-map class. The limiting and affine-support problem is the separate open
node `q:cmh-approximation`. The general-measure paragraph is a conditional template, not a
closure theorem.

### Exact cases

- The one-dimensional sharpness test now uses the centered one-sided exponential and a direct
  family $f_a$ whose Rayleigh quotient tends to $4$. The primary Kannan--Lovász--Simonovits
  attribution is distinguished from the secondary Cattiaux--Guillin pointer.
- The product theorem is stated for general CMH blocks. Its cross terms are the nonnegative
  squares
  $\mathbb E\|H_i^{1/2}D^2_{ij}gH_j^{1/2}\|_{\mathrm{HS}}^2$; the generators are correctly
  called nonpositive.
- The Gamma proof is routed by $A\ge3$, not by $m\ge3$. It therefore covers the two-coordinate
  Dirichlet surplus whenever $A>3$; only $m=2$, $A<3$ uses the one-dimensional branch.
- The text now records both uses of $\alpha_i\ge1$: the sign in the product-Gamma completion and
  the load-bearing constraint in the angular minimization. The unused upper hypothesis
  $\alpha_i\le A-2$ remains removed.
- Exact product-exponential saturation is proved, while perturbative growth of the full CMH
  quotient remains `q:cmh-solenoidal-perturbation`. An increase in one Hodge channel alone is
  not a perturbation theorem.

## Numerical and provenance repair

The existing artifact
`research/runs/2026-08-25T070915.854321Z-cmh-gate-zero.jsonl` was not modified; its SHA-256 is
`19be1fbfcfe91c00d6a03bf71a561b50096b7088ca70554000b9e87390f4dd9f`. Its provenance records
commit `61924764510bde3a4ff581064b5f9823dedd6cea`, but that commit does not contain
`experiments/finum/targets/cmh_gate_zero.py`. It also predates the exact-certificate boundary.
The artifact is therefore retained as unlinked calibration history and supplies no ledger
evidence for `conj:gate-zero` or `thm:cmh-dirichlet`.

The current target was hardened for future runs:

- only `fractions.Fraction` closed forms or exact rational Rayleigh witnesses can reach
  `verdict.falsify` and uppercase `REFUTED`;
- floating generalized eigenvalues, FEM values, and the entire Galerkin channel use
  `compare_directional`;
- exact Dirichlet witness records persist the rational matrices, vector, quadratic numerator
  and denominator, and positive exact $LDL^\top$ pivots;
- provenance records the effective instance lists, dimension ranges, polynomial degrees, grids,
  quadrature tolerances, eigensolver, and rationalization cap;
- all current target models lie inside already-proved classes or are the algebraic fence, so a
  green run is calibration, not evidence for universal CMH or KLS.

## Control-plane repair

- `prop:spectral-sufficiency` is open: the fixed-eigenfunction route currently contains only a
  mechanism sketch, not a certified implication to KLS.
- Missing KLS dependencies and obstruction reverse-parity entries were reconciled; the terminal
  CMH task now explicitly requires approximation closure.
- The 41 inherited Eldan proved nodes without standalone dossiers are frozen in the explicit
  `meta.legacy_proved_without_solution` allowlist. New CMH nodes receive no exception.
- `research/check_ledger.py` now rejects a proved node without a certified solution, documented
  proof provenance, or an explicit legacy exception. For agent certification it also requires a
  dossier header naming the node and a review report with an unqualified
  `- **Verdict:** pass ...` header naming both the node and the declared reviewer.
- Checker regression tests cover partial verdicts, scope-qualified verdicts, wrong reviewers,
  missing dossier-node headers, and the legacy exception boundary.

## Independent certification

Repair authors and reviewers were kept distinct:

- normalization repair author `/root/kls_proof_audit`; independent reviewer
  `/root/kls_evidence_audit`; report
  `research/reviews/2026-08-25-kls-cmh-normalization-repair-audit.md` gives an unqualified pass
  for seven nodes;
- exact-case repair author `/root/kls_ledger_audit`; independent reviewer
  `/root/cmh_exact_reviewer`; report
  `research/reviews/2026-08-25-kls-cmh-exact-cases-repair-audit.md` gives an unqualified pass for
  ten nodes.

The ledger and both dossier headers now point to those reports. The original partial audit is
still cited as historical diagnosis, not certification.

## Validation

- `python3 research/check_ledger.py`: 2 ledgers, 172 nodes, 632 labels, 0 errors, 0 warnings.
- `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s research/tests -p 'test_*.py'`:
  16 passed.
- `cd experiments && UV_CACHE_DIR=/tmp/kls-fix-uv-cache uv run python -m finum selftest`:
  all targets passed, including all CMH calibration/certificate gates.
- `cd experiments && UV_CACHE_DIR=/tmp/kls-fix-uv-cache uv run pytest`: 90 passed.
- `git diff --check`: passed.
- Standalone builds of `solutions/thm-cmh-normalization.tex` and
  `solutions/thm-cmh-dirichlet.tex`: passed (5 pages each; expected standalone unresolved
  cross-manuscript references only).
- Full `main.tex` build: passed (149 pages), with no undefined references or citations.

## Resulting status

The regular-class reduction $C_P^{\mathrm{aff}}\le C_{\mathrm{CMH}}$, the Hodge identity,
the algebraic Letwin fence, the line/product formulas, and the log-concave Dirichlet theorem are
now R2-certified at their stated scopes. Universal $\mathrm{CMH}(4)$, approximation to arbitrary
log-concave measures, gate zero, the solenoidal perturbation test, the invariant lift, the
square-root commutator, and KLS itself remain open.
