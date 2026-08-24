# A1/A2 independent-agent proof audit

- **Date:** 2026-08-21
- **Proof author:** `/root/a1_a2`
- **Independent reviewer:** `/root/cross_review`
- **Certification:** `checked_by: agent`
- **Verdict:** pass for the five nodes listed below

## Certified scope

1. `prop:a1-euclidean-harmonic` — factor-one inverse-minimum-curvature bound under
   $U\in C^\infty$ and $mI\preceq\nabla^2U\preceq MI$.
2. `prop:a1-mode-leverage` — mode-Hessian sandwich, radial potential/tail bounds, and the direct
   $K_d(\eta)$ Poincaré certificate.
3. `cor:a1-leverage-asymptotic` — the fixed-dimensional exact mode-Hessian coefficient under
   vanishing maximal leverage.
4. `prop:a2-subquadratic-global` — exact Gaussian-prior $C_{\mathrm{LS}}=C_{T_2}$ rigidity under
   directional Gaussian-tube subquadratic growth.
5. `prop:a2-logistic-global` — the finite binary-logistic corollary.

The reviewed standalone artifacts are
[`solutions/a1-harmonic-mode-leverage.tex`](../../solutions/a1-harmonic-mode-leverage.tex) and
[`solutions/a2-subquadratic-tail-rigidity.tex`](../../solutions/a2-subquadratic-tail-rigidity.tex).

## Checks performed

The review checked spectral localization, the Bochner--Kato calculation, the Schrödinger
operator-core/domain passage, Hessian and potential sandwiches, radial normalization and tail
ratios, integrability of $K_d(\eta)$, covariance convergence, and the matching linear lower
bound. For A2 it checked Gaussian completion, both bounds on the likelihood correction, centering,
the $T_2\Rightarrow T_1$ lower bound, Bakry--Émery/Otto--Villani upper bounds, and the
shrinking-prior matrix tradeoff. Both final dossiers compile standalone and match the audited
manuscript statements.

The review requested explicit $0\le p<2$, $b\ge0$, an accurate curvature-versus-score caveat for
moving priors, and correction of two TeX transcription defects. Those corrections are present in
the final artifacts.

## Explicit exclusions

This audit does not certify `prop:a1-bulk-tail` or `thm:a2-target`. It also does not extend the
A1 factor-one theorem to unbounded Hessians, nonsmooth losses, growing dimension, or high maximal
leverage. Those items remain open.
