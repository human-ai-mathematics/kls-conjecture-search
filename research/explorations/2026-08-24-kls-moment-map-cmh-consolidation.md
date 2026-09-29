---
---
# KLS consolidation: July quadratic sector and the deterministic CMH route

Date: 2026-08-24

Status: repository consolidation and independent audit. This record does **not** prove KLS,
certify CMH(4), or promote an internal CMH statement to `proved`.

## Supersession and scope

This note supersedes the **route ranking**, but not the mathematics or historical record, in the
20 August 2026 KLS cycle. The fixed-eigenfunction stochastic-localization route remains live as a
secondary route. The new primary deterministic route follows moment-map Hessian geometry, Haar
aggregation, Schur--Piola fibers, Hodge residuals, and square-root commutators. The August 20
explorations remain append-only and unchanged.

The consolidation used:

- the independent summary supplied on 24 August;
- every current `modules/kls/` module, KLS route brief, obstruction, ledger node, and earlier KLS
  exploration;
- the primary version-1 preprints
  [Chen--Klartag, arXiv:2607.23307](https://arxiv.org/abs/2607.23307) and
  [Letwin, arXiv:2607.24164](https://arxiv.org/abs/2607.24164), together with the published
  benchmark [Klartag, arXiv:2303.14938](https://arxiv.org/abs/2303.14938); and
- three independent read-only audits: mathematical, claim-graph, and repository-structure.

## Literature audit

The externally checked picture is:

1. Chen--Klartag prove
   $\mathbb E_\nu\lVert D^2\phi\rVert_{\mathrm{HS}}^2\le2n$,
   $\operatorname{Var}(|X|^2)\le8n$, and
   $\lVert T_3(X)\rVert_{\mathrm{HS}}^2\le4n$, with the stated centered one-sided-exponential
   and regular-simplex equality results.
2. Letwin proves
   $\mathbb E_\nu\operatorname{tr}(BHBH)\le2\operatorname{tr}(B^2)$ for constant symmetric
   $B$, and consequently the sharp homogeneous quadratic-form inequality
   $\operatorname{Var}\langle MX,X\rangle\le8\operatorname{tr}(M^2)$.
3. Letwin's directional third-moment bound, combined with Klartag's improved Lichnerowicz
   comparison, gives the version-1-preprint-conditional frontier
   $C_P\lesssim\sqrt{\log n}$ and $h_n^\star\gtrsim(\log n)^{-1/4}$.
4. Letwin's $B=I$ case contains the shared moment-Hessian direction, but neither paper subsumes
   all the results of the other. Letwin's homogeneous quadratic theorem alone does not yield
   Chen--Klartag's sharp $4n$ full third-tensor constant.
5. Neither preprint proves full KLS. Thin shell is one radial consequence of KLS; no
   dimension-free converse is known. It is unsound to call that converse false without a KLS
   counterexample.

The wording “quadratic sector” is now qualified as **homogeneous quadratic forms** or quadratic
chaos. This avoids an incorrect extension to affine degree-two polynomials. The centered
one-sided exponential extremizer is also kept distinct from the two-sided Laplace product used
by the Eldan-A alignment diagnostic.

## Structural reorganization

Part III now begins with a route-neutral theorem frontier and strategy map. The former Route A/B
labels are explicitly **Eldan-A/B**. Three live route directories are preserved:

1. `eldan-localization`: fixed-cut stochastic localization;
2. `moment-map-spectral`: fixed-eigenfunction stochastic localization; and
3. `moment-map-cmh`: deterministic moment-map/Haar/Schur--Piola geometry.

The KLS ledger and obstruction schema were moved from the Eldan directory to `research/kls/`.
There is still exactly one KLS ledger and one writer; route ownership is expressed by `route:`
metadata. The obstruction prose states that its current mechanisms are Eldan-scoped rather than
universal no-go theorems.

The central graph now has a route-neutral `conj:kls` node, four July 2026 imported-preprint nodes,
one open fixed-eigenfunction headline, and four open CMH program/question nodes. No new route node
is `proved`, `conditional`, or `refuted`.
The bridge to `ab/conj:a1-bis` attaches to `conj:kls` rather than to an arbitrary Eldan subroute.

## Audit of the proposed CMH chain

The following displayed calculations survived an independent algebraic audit, subject to the
regularity and domain qualifications recorded in the route inventory:

- the compression identities $R^*R=I$, $Q_M=N^{1/2}K_MN^{1/2}$ and the formal commutator error;
- the Haar--Bessel deficit once the normalized complete multiplier family is fixed;
- the stated Brascamp--Lieb deficit factorization, with
  $\operatorname{Var}(\nabla u)=\sum_i\operatorname{Var}(\partial_i u)$;
- the displayed Schur--Piola block, transport, trace, and target-coordinate identities;
- the fixed-target $1+2$ completion of squares;
- the planar Airy multiplier identity, flux-residual decomposition, and one-edge identity at the
  formal Hilbert-space level;
- the three-exponential density and inherited Stein kernel, including failure of Hessian
  compatibility of $S^{-1}$ on the positive cone; and
- the nonzero cubic commutator symbol and square-root resolvent representation on a suitable
  common core.

These checks are not R2 dossiers. In particular, the two solenoidal residual channels are not
automatically orthogonal in ordinary $L^2$, and low-dimensional positivity does not by itself
give an all-dimensional split reduction.

The headline CMH inequality remains a **schema** because $\Sigma$, $L$, the $L^2$ measure,
domains, centering, inverse conventions, and approximation passage have not been frozen. Thus the
reported implication CMH(4) $\Rightarrow C_P\le4$ is not yet a certified conditional reduction.

## Retractions preserved

The originating exploration withdrew the following shortcuts, and the new route inventory keeps
them visible so that future work does not rerun them:

- Letwin directly proves full KLS;
- sibling positivity can be imposed node by node;
- a fixed fraction of descendant slack can be spent at each split;
- the conformal derivative is a free scalar obstruction;
- the multiplier transport coefficient can be chosen arbitrarily, including the artificial
  value $\alpha=-2$;
- the cubic commutator cancels completely;
- $\mathbb E[\operatorname{cof}(T)a\mid z]$ is a conserved local vector;
- every negative node is explained by the Airy mismatch; and
- corrector slack may be assigned to the conformal sector alone.

Except for the externally false reading of Letwin and the independently expanded coordinate
identities, the supplied model witnesses do not yet have standalone analytic dossiers or
eligible `finum` artifacts. They are therefore recorded as **reported retractions**, not
uppercase `REFUTED` ledger results.

## Stable diagnosis

The exploration supports a global matrix-coupled proof design. It gives no surviving local
conformal obstruction and no sound scalar or nodewise shortcut. The best identified analytic
bottleneck is the complete-tree estimate for the noncommutative errors
$[N^{1/2},K_M]$, retaining the Bessel, Codazzi, Monge--Amp\`ere, corrector, Hodge, and descendant
reservoirs.

It is nevertheless premature to call this the *only* formal gap. The route must also complete:

1. CMH normalization and the endpoint duality;
2. the invariant target-flat multiplier lift;
3. an arbitrary-dimensional irreducible split reduction;
4. Hodge topology, boundary conditions, and flux domains;
5. low/high resolvent-scale control; and
6. exact global spending of every Haar and descendant term.

These tasks are M0--M8 in `research/kls/routes/moment-map-cmh/open-problems.md`.

## Regression and evidence discipline

The Gaussian, aligned-product, rotated-exponential, Laguerre, high-frequency, $45^\circ$ child,
Gamma--Gaussian, and three-exponential models are now frozen in the shared instance registry.
There is no CMH `finum` backend and no CMH R1 artifact. Registration therefore prevents
happy-path model selection but supplies no numerical proof signal. Any future sampled, FEM, or
finite-grid claim must use a provenance-stamped `finum` target; exact counterexamples require an
analytic dossier.

## Certification debt and validation

The audit found 41 legacy KLS nodes marked `proved` whose arguments live inline in the manuscript
but lack the current `solution:` and `checked_by:` metadata. This is an R2 certification debt,
not evidence that the statements are false. The consolidation records the debt and does not
silently recertify, downgrade, or use it to promote new nodes.

At consolidation time:

- `python3 research/check_ledger.py` found 2 ledgers, 150 nodes, 448 labels, 0 errors, and
  0 warnings;
- `python3 -m unittest discover -s research/tests -p 'test_*.py'` passed 13 tests; and
- `latexmk -pdf -outdir=build main.tex` produced the full manuscript PDF.

The independent report is persisted at
`research/reviews/2026-08-24-kls-consolidation-audit.md`.
