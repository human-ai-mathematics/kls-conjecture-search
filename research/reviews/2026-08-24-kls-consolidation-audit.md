# KLS route consolidation — independent audit

- **Date:** 2026-08-24
- **Consolidation author:** `/root` (Codex)
- **Independent mathematical reviewer:** `/root/kls_math_audit` (Mencius)
- **Independent claim-graph reviewer:** `/root/kls_claim_graph_audit` (Aristotle)
- **Independent structural reviewer:** `/root/kls_structure_audit` (Bernoulli)
- **Review type:** literature, mathematics, control-plane, and editorial consolidation audit
- **Verdict:** pass for the scoped consolidation; **no KLS or CMH proof certification**

## Scope

The audit covers:

- the route-neutral manuscript frontier in `modules/kls/00-strategy-map.tex`;
- the deterministic route in `modules/kls/15-moment-map-cmh.tex` and
  `research/kls/routes/moment-map-cmh/`;
- the preserved fixed-eigenfunction route and its new headline node
  `q:mm-spectral-occupation`;
- the move to the central `research/kls/ledger.yaml` and `obstructions.{md,yaml}`;
- the terminal `conj:kls`, imported July 2026 nodes, CMH nodes, route/bridge semantics, and
  navigation changes; and
- the append-only synthesis
  `research/explorations/2026-08-24-kls-moment-map-cmh-consolidation.md`.

This report is not a `checked_by: agent` proof review. It certifies that the consolidation states
its evidence levels and open gaps consistently; it does not promote any KLS node.

## Literature verdict

The constants and division of results were checked against the primary version-1 preprints:

- [Chen--Klartag, arXiv:2607.23307](https://arxiv.org/abs/2607.23307): the regular moment-map
  Hessian estimate, sharp $8n$ radial thin shell, sharp $4n$ third tensor, and the stated
  exponential/simplex equality analyses;
- [Letwin, arXiv:2607.24164](https://arxiv.org/abs/2607.24164): the all-constant-symmetric-$B$
  moment-map estimate, arbitrary-law homogeneous quadratic Poincaré theorem after approximation,
  directional third-moment bound, and the preprint-conditional general KLS improvement; and
- [Klartag, arXiv:2303.14938](https://arxiv.org/abs/2303.14938): the published benchmark used for
  comparison.

The final prose correctly says that Chen--Klartag control the $B=I$ direction while Letwin
controls every constant symmetric $B$; neither paper proves full KLS. It also distinguishes
homogeneous quadratic forms from affine degree-two polynomials, centered one-sided exponential
extremizers from two-sided Laplace localization models, and “no known thin-shell converse” from
an unsupported claim that a converse is false.

## Mathematical audit

The reviewer independently checked, subject to the stated smoothness/domain conventions:

- Haar compression, the formal commutator error, and the exact Bessel deficit;
- the displayed Brascamp--Lieb deficit factorization;
- the Schur--Piola block, transport, target-coordinate, and trace identities;
- the fixed-target $1+2$ completion of squares;
- the planar Airy multiplier and test-dependent residual formulas, with
  $\delta_\rho=-\operatorname{div}_\rho$ and divergence in the second tensor index;
- the one-edge identity at the formal Hilbert-space level;
- the three-exponential density/inherited kernel and failure of Hessian compatibility; and
- the nonzero cubic commutator symbol and the square-root resolvent formula on a common core.

The audit does **not** convert those calculations into R2. It confirms that the files now label
them external, formal, reported, or open at the appropriate level.

## Corrections made during review

The independent reviewers required and then rechecked these material corrections:

1. separated Chen--Klartag's $B=I$ input from Letwin's all-$B$ theorem;
2. added isotropic/log-concave hypotheses to the third-tensor theorem;
3. separated Letwin's regular matrix theorem from the arbitrary-law quadratic consequence;
4. replaced “thin-shell converse is false” by the accurate open-converse statement;
5. removed the claim that the schematic CMH endpoint reduction was already established;
6. froze Hodge divergence signs and warned that the two solenoidal channels need not be ordinary
   $L^2$-orthogonal;
7. narrowed the square-root-commutator node so M8, rather than a mismatched graph edge, performs
   the endpoint combination;
8. treated the commutator as the best identified bottleneck, not the sole certified gap;
9. marked rotated-exponential, Laguerre, high-frequency, and Gamma--Gaussian behavior as
   reported/dossier-pending rather than certified refutations;
10. added the fixed-eigenfunction headline to manuscript and ledger instead of leaving a live
    route outside the graph;
11. made `conj:kls` a route-neutral terminal with conditional entry points rather than claiming
    that conditional theorems already discharge it; and
12. repaired route taxonomy, moved paths, cross-program bridge IDs, and the legacy R2-debt
    disclosure.

## Control-plane verdict

The final KLS graph has 78 nodes: 41 legacy `proved`, 12 `conditional`, 17 `open`, 7 `imported`,
and 1 `heuristic`. Every KLS node ID occurs exactly once as a LaTeX label and occurs in its
declared `file:`. Cross-program bridges resolve reciprocally at
`ab/conj:a1-bis` $\leftrightarrow$ `kls/conj:kls`; all conditional nodes propagate their open or
preprint assumptions correctly. Moved ledger/obstruction links and route navigation were audited.

The 41 legacy `proved` nodes have inline manuscript arguments but lack the current standalone
`solution:` and `checked_by:` metadata. Their status is preserved as historical state, with an
explicit certification-debt annotation; this report does not recertify them.

## Explicit exclusions

This audit does not certify:

- a fully defined CMH(4) or CMH(4) $\Rightarrow C_P\le4$;
- the general transport-coefficient classification, inverse-metric lift, or Codazzi backup;
- the undocumented model counterexamples as analytic or numerical refutations;
- an arbitrary-dimensional irreducible split reduction;
- global Airy/Hodge boundary theory or the full one-edge domain passage;
- a dimension-free resolvent estimate or full Haar-tree slack ledger; or
- full KLS by any route.

There is no CMH `finum` target and no CMH R1 artifact. The registered regression suite therefore
fixes future tests but supplies no proof signal.

## Validation

- `python3 research/check_ledger.py`: 2 ledgers, 150 nodes, 448 labels, 0 errors, 0 warnings.
- `python3 -m unittest discover -s research/tests -p 'test_*.py'`: 13 tests passed.
- `latexmk -pdf -outdir=build main.tex`: full manuscript built successfully, with no undefined
  citations or references introduced by this consolidation.
- `git diff --check`: clean.

## Final reviewer diagnosis

The July preprints close the sharp radial and homogeneous-quadratic layers, not full KLS. The
deterministic CMH program contains a coherent set of formal identities and a genuine
noncommutative cubic symbol. Its leading target is a global square-root commutator/full-tree
estimate, while endpoint normalization, invariant lift, all-split reduction, Hodge domains, and
slack accounting remain open. The repository now communicates that diagnosis without promoting
reported exploration to proof.
