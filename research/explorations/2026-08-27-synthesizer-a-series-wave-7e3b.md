# A-series convergence after the 2026-08-27 proof wave

**Date:** 2026-08-27
**Role:** `synthesizer`
**Concurrency key:** singleton `knowledge`, granted by the orchestrator
**Scope:** A1--A5 only; no numerical work

## Sources and status boundary

This synthesis read the root and role contracts, the live A-series frontier, the complete current
A1--A5 ledger, manuscripts, and target briefs, and every new 2026-08-27 A-series exploration,
proof dossier, and review. The current ledger already records the independently certified A2,
A3, and A4 promotions and the two published A4/A5 imports. This record does not alter a ledger,
manuscript, target brief, bibliography, review, dossier, or shared instance.

The proof-miner report
`research/explorations/2026-08-27-proof-miner-a-series-mechanisms-c7f4.md` is now superseded only
where it classified `thm:a2-target`, `thm:a3-product`, `prop:a3-hierarchical-prior`, and
`prop:a4-logistic-global` as proof-ready but open. The corresponding dossiers have since passed
independent review. Its remaining mechanism and bottleneck analysis is not superseded. The first
A3 audit remains the append-only record of a failed artifact; the fresh follow-up review certifies
the one-character repair and no other change. Three later post-promotion audits found only stale
formal-fence provenance in the dossier headers and obstruction paragraphs, not mathematical
defects. Those fields were synchronized, and the three post-promotion proof reviews certify the
current dossier bytes.

## A1 $\leftrightarrow$ A2 consistency in a common normalization

For a posterior sequence with mode Hessian $H_n\succ0$, use
$$
 R_{P,n}:=\frac{C_P(\pi_n)}{\lambda_{\max}(H_n^{-1})}.
$$
When $H_n/n\to I(\theta_0)\succ0$, the common Fisher target is
$R_{P,n}\to1$, equivalently
$nC_P(\pi_n)\to\lambda_{\max}(I(\theta_0)^{-1})$.

- The A1 route assumes fixed dimension, the bounded-Hessian log-curvature-Lipschitz contract,
  and vanishing maximal mode leverage $\eta_n\to0$.
- The A2 strong-Laplace route assumes fixed dimension and a globally vanishing oscillation of the
  whitened log-density ratio relative to $N(0,I_d)$.

These hypotheses are not identified. They are two sufficient routes to the same normalized
Poincaré conclusion; the A2 route additionally transfers LSI and $T_2$.

| implication direction | status | exact boundary |
|---|---|---|
| A1 `cor:a1-leverage-asymptotic` $\Rightarrow$ the A2 Fisher-scale Poincaré conclusion on the same bounded-Hessian, vanishing-leverage sequence | **proved (dossier)** | `solutions/a1-harmonic-mode-leverage.tex` proves $R_{P,n}\to1$ and the Fisher limit. It does not prove the A2 global LSI/$T_2$ lines. |
| A2 `thm:a2-target` $\Rightarrow$ the finite-sample A1 selection/sharpness programme (`conj:a1`, `q:a1-sharp`) | **open** | `solutions/thm-a2-target.tex` transfers constants once global oscillation is supplied; it does not construct a computable $\bar W$, certify a useful GLM tail correction, handle high leverage, or extend the factor-one domain argument to unbounded Hessians. |

No reverse-equivalence claim and no new `depends_on` edge follows. The existing
`q:a2-poincare` dependence on `cor:a1-leverage-asymptotic` already records the certified A1
subclass contribution without pretending it proves all of `conj:a2`.

## Stable knowledge promoted

All promotions go to `research/knowledge/lemmas.md` and retain their limiting hypotheses.

| source | promoted mechanism | guardrail retained |
|---|---|---|
| `solutions/thm-a2-target.tex`; `research/reviews/2026-08-27-a2-strong-laplace-post-promotion-proof-review.md` | sharp global-oscillation transfer for $C_P$, $C_{\mathrm{LS}}$, and $C_{\mathrm{TCI}}$ | fixed dimension and global essential oscillation, not TV or local Laplace control |
| `solutions/a3-product-hierarchical-prior.tex`; `research/reviews/2026-08-27-a3-product-hierarchical-prior-post-promotion-proof-review.md` | tensorize the Gaussian/log-half-Cauchy base, then pull its energy through noncentering | exact pullback metric with every cross term; no posterior dependence claim |
| `solutions/prop-a4-logistic-global.tex`; `research/reviews/2026-08-27-a4-logistic-global-post-promotion-proof-review.md` | remote Gaussian translations force the exact prior-scale restricted and mean constants | location-rich global family only; localized compact sublevels remain distinct |
| `research/explorations/2026-08-27-literature-scout-a4-a5-imports-lit-01.md` (`thm:a4-modified-transport-1d`) | real-line integrability/cost matching and the polynomial-tail global obstruction | one-dimensional, existential scale, no Student/horseshoe localized coefficient |
| `research/explorations/2026-08-27-literature-scout-a4-a5-imports-lit-01.md` (`thm:a5-two-well-eyring-kramers`) | exact fixed-landscape two-well raw Poincaré asymptotic | no random orbit network, collision, capacity, or quotient conclusion |

The generic Holley--Stroock and tensorization entries were not repeated. The new A2 entry records
the matching covariance lower-bound mechanism, while the A3 entry records the nontrivial
pullback metric and its structural cross terms. The earlier A1 attribution correction was already
present and was left untouched.

## What is now known jointly

1. A1 and A2 give the same Fisher coefficient for $C_P$ in their certified overlap, but by
   different stability mechanisms. Agreement of the coefficient is proved; equivalence of the
   hypotheses is not asserted.
2. The A2 global-tail theorem and the A4 translation theorem separate bulk from remote-tail
   geometry sharply: global Gaussian comparison transfers all three Fisher-scale constants,
   whereas finite logistic data with a fixed Gaussian prior and a location-rich family force the
   A4 global conversion constants back to $\lambda_{\max}(\Sigma_0)$.
3. A3 now has a certified dimension-free product closure and an optimal constant-$4$
   hierarchical-prior inequality in the full noncentered pullback metric. The remaining posterior
   difficulty is dependence after a likelihood tilt, not the prior coordinate calculation.
4. The A4 and A5 imports close two model anchors without closing their programmes: global
   real-line modified transport is classified for generalized-normal tails, and the raw fixed
   two-well Eyring--Kramers law is available with its prefactor.

## The new concrete A4 residual

The accepted residual for `q:a4-modified` is now the named Student-logistic posterior and
fixed-scale Gaussian location family
$$
 \pi_{\nu,n}(dx)\propto
 \left(1+\frac{x^2}{\nu}\right)^{-(\nu+1)/2}\operatorname{sigmoid}(x)^n\,dx,
 \qquad \nu>2,\ n\ge1,
 \qquad
 \mathcal Q_s=\{N(m,s^2):m\in\mathbb R\}.
$$
With $K(m)=\mathrm{KL}(N(m,s^2)\|\pi_{\nu,n})$, $\delta=\min_mK(m)$, and
$M_\rho=\{m:K(m)\le\delta+\rho\}$, the next proof must:

1. prove continuity and coercivity of $K$, $\delta>0$, and nonempty compactness of every complete
   $M_\rho$;
2. prove explicit matching upper and lower bounds, including the sharp large-$\rho$ order, for
   $$
   C_{\nu,n,s}(\rho)
   =\sup_{m\in M_\rho}
   \frac{W_2^2(N(m,s^2),\pi_{\nu,n})}{2K(m)};
   $$
3. derive finiteness from this family's compact sublevels and $\nu>2$, never from a KL cutoff
   alone.

This residual remains open. It is a family/sublevel improvement over the global value $+\infty$,
not a global polynomial-tail TCI.

## Unresolved bottlenecks by stream

- **A1:** replace maximal-row leverage in high-leverage regimes, certify a useful finite-sample
  improvement over the prior, and close the factor-one domain argument for unbounded Hessians.
- **A2:** verify a useful model-level stability contract weaker than global oscillation, and make
  it uniform in growing dimension; global LSI/$T_2$ still require a tail classification.
- **A3:** obtain conditional weighted inequalities and a positive quantitative block gap for a
  named likelihood-tilted hierarchy in the complete pullback metric.
- **A4:** prove the Student-logistic residual above and, more broadly, finite-radius family
  coercivity/tail control plus a separate computable upper-KL certificate.
- **A5:** prove uniform random empirical barrier/capacity estimates on the repeated orbit network,
  collision and tail control, and an independent quotient Bernstein--von Mises theorem.

## Merge barriers and rerun hygiene

- **A1 $\leftrightarrow$ A2:** consistency is certified only in the displayed overlap; high
  leverage, unbounded Hessians, weaker spectral stability, and growing dimension remain blocked.
- **A1-bis $\leftrightarrow$ KLS:** untouched. A structured-posterior result would not prove KLS,
  and this wave supplied no dossier-backed implication in either direction.
- **Trace-upgrade cluster:** untouched. No formal equivalence among `q:upgrade`, the high-rank
  part of `q:stein-weighted`, and `q:alignment` was proved or proposed.

No two agents independently reran the same fenced A-series shape in this wave. The A3 second
review was the required repair cycle after a recorded failed audit, not duplicate exploration.

## Ledger and route-control conclusion

No new edge is warranted. In particular, the A1/A2 coefficient agreement does not prove an
equivalence of hypotheses, the A4/A5 imports create no cross-stream dependency, and neither
untouched merge barrier received new evidence.

The current ledger already contains the complete dossier-backed metadata for this wave:

- `thm:a2-target`: `status: proved`, `solution: solutions/thm-a2-target.tex`, `checked_by: agent`,
  and `review: research/reviews/2026-08-27-a2-strong-laplace-post-promotion-proof-review.md`;
- `thm:a3-product` and `prop:a3-hierarchical-prior`: `status: proved`, their shared dossier,
  `checked_by: agent`, and
  `review: research/reviews/2026-08-27-a3-product-hierarchical-prior-post-promotion-proof-review.md`;
- `prop:a4-logistic-global`: `status: proved`, its dossier, `checked_by: agent`, and the passing
  `review: research/reviews/2026-08-27-a4-logistic-global-post-promotion-proof-review.md`.

The imported A4/A5 nodes are correctly `status: imported` with published references, not
dossier-certified implications. Therefore there is no additional ledger or route-control delta
to propose from this synthesis.

```yaml
outcome: complete
artifacts:
  - research/explorations/2026-08-27-synthesizer-a-series-wave-7e3b.md
  - research/knowledge/lemmas.md
proposed_deltas:
  - none
next_role: orchestrator
next_prompt: |
  Review the synthesis and retain the current dossier-backed ledger promotions. Add no
  A1/A2 reverse dependency, no A1-bis/KLS edge, and no trace-cluster equivalence. Run
  python3 research/check_ledger.py and the repository validation appropriate to the full wave
  before committing the dedicated branch.
```
