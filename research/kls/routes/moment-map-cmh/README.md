# Route: deterministic moment map, Haar aggregation, and CMH

Status: **live, two layers, one of them now proved-in-part**. This route is represented in the
central [`../../ledger.yaml`](../../ledger.yaml). Its headline conjecture — universal
$\mathrm{CMH}(4)$ — remains **open**, and the route makes no claim to have proved KLS.

## Thesis

Chen--Klartag control the trace direction $B=I$, while Letwin controls the moment-map Hessian
against every **constant symmetric matrix** $B$. The proposed extension is to allow the
multiplier to depend on the test function and to pay for the resulting noncommutation with
positive Monge--Ampère and variable-multiplier squares. If this can be done dimension-freely, an
appropriate covariance--moment--Hessian estimate (CMH) implies a universal Poincaré bound.

The route is deterministic: its principal objects are the moment-map Hessian metric, weighted
elliptic operators, Schur fibers, Stein-kernel residuals, and square-root commutators. It is not
the [`moment-map-spectral`](../moment-map-spectral/) route, which follows a fixed first
eigenfunction under stochastic localization.

## The two layers

As of 25 August 2026 the route has two layers with almost no shared machinery. They must not be
conflated: a result in one does not transfer to the other.

| layer | manuscript | objects | status |
|---|---|---|---|
| **normalization** | `modules/kls/41-cmh-normalization.tex`, `modules/kls/42-cmh-exact-cases.tex` | Stein generator, Hodge splitting, gate zero, exact model classes | regular-class endpoint reduction and exact model classes **proved**; approximation and headline open |
| **construction** | `modules/kls/40-moment-map-cmh.tex` | Haar/Bessel tree, Schur--Piola transport, Airy residuals, $[N^{1/2},K_M]$ | entirely open; several route-level retractions |

The normalization layer is logically prior and was added second. A reader starting Route C should
read `41-cmh-normalization.tex` first.

### What the normalization layer settled

The originating exploration proposed the schema
$\lVert\Sigma^{-1/2}H\nabla g\rVert_2^2\le4\lVert{-Lg}\rVert_2^2$ without defining $\Sigma$, $L$,
the $L^2$ space, or the admissible class. The regular-class part of task **M0** is now
discharged; its approximation residue is the open node `q:cmh-approximation`:

- `def:cmh` fixes the data: $\Sigma$ is the covariance, $L_\mu=\operatorname{div}_\mu(H\nabla\cdot)$
  is the Stein generator, the space is $L^2(\mu)$, the class is $\operatorname{Dom}(\mathsf A)$
  with $\mathsf A=-L_\mu$, and every inverse is the pseudoinverse on $(\ker\mathsf A)^\perp$.
  For simplex laws $\Sigma^{-1}$ is the Moore--Penrose inverse on the affine tangent space.
- `thm:cmh-implies-affine-poincare` proves $C_{\mathrm P}^{\mathrm{aff}}(\mu)\le C_{\mathrm{CMH}}(\mu)$
  by one Cauchy--Schwarz step plus a spectral truncation, with **no** spectral gap assumed.
  Dossier: [`solutions/thm-cmh-normalization.tex`](../../../../solutions/thm-cmh-normalization.tex).
- `thm:cmh-1d`, `thm:cmh-product`, `thm:cmh-dirichlet` compute the constant exactly on the line,
  on products, and on **every log-concave Dirichlet law** — the route's first nonproduct theorem.
  Dossier: [`solutions/thm-cmh-dirichlet.tex`](../../../../solutions/thm-cmh-dirichlet.tex).

### Two risks exposed by the normalization layer

1. **CMH has an additional channel not directly controlled by KLS.** `prop:cmh-hodge` splits the
   CMH numerator into the affine Poincaré inverse-divergence part plus a nonnegative
   **solenoidal excess**, which vanishes identically in dimension one under the no-flux
   convention. This proves $C_{\mathrm{CMH}}\ge C_P^{\mathrm{aff}}$, but it does not prove a
   strict separation at constant $4$: no separating log-concave measure is known. The route is
   pursuing a sufficient condition of unknown truth value, not a proved reformulation of KLS.
2. **Letwin's theorem cannot supply even the linear sector.** Testing on linear functions gives
   the necessary *gate zero* condition $\mathbb E[H\Sigma^{-1}H]\preceq4\Sigma$
   (`conj:gate-zero`). `prop:letwin-not-gate-zero` is an exact countermodel: a random PSD matrix
   law with $\mathbb EH=I$ satisfying $\mathbb E\operatorname{tr}(BHBH)\le2\operatorname{tr}(B^2)$
   for **every** symmetric $B$, yet with $\lambda_{\max}(\mathbb EH^2)>4$ for $m\ge18$. The whole
   gap is the static commutator
   $\operatorname{tr}(B^2H^2)=\operatorname{tr}(BHBH)+\tfrac12\lVert[B,H]\rVert_{\mathrm{HS}}^2$.

Both are gains: the route now has two explicit probes instead of only the end of the Haar
programme, while neither probe is promoted beyond what has actually been shown.

## Where gate zero sits in the repository's difficulty map

In isotropic position gate zero reads $\mathbb EH^2\preceq4I$, while Chen--Klartag already give
$\operatorname{tr}(\mathbb EH^2)\le2n$. So the *average* eigenvalue is $\le2$ and gate zero asks
the *maximum* to be $\le4$: an operator-to-trace upgrade with a factor-2 budget. That places it in
the same family as `q:upgrade`, the high-rank part of `q:stein-weighted`, and `q:alignment`
(`rem:trace-upgrade-unification`), and **hard constraint 6 of `CLAUDE.md` applies**: no fan-out
across that cluster, and no claim of equivalence. Practically the verdict splits — gate zero is
cheap to *test* on a model, and expected to be as hard to *prove* as the rest of the program.

## Route chain

```text
external moment-map matrix bounds  (Letwin, Chen-Klartag)
        |
        +-- NORMALIZATION LAYER ------------------------------+
        |   define CMH; regular-class CMH => affine Poincare  |  DONE
        |   approximation/closure to arbitrary laws           |  OPEN
        |   Hodge split => nonnegative solenoidal channel      |  DONE
        |   strict separation from KLS                         |  OPEN
        |   exact: line, products, log-concave Dirichlet      |  DONE
        |   gate zero (necessary) + algebraic countermodel    |  DONE
        |        |                                            |
        |        v                                            |
        |   falsification layer: q:gate-zero,                 |  OPEN
        |   q:cmh-solenoidal-perturbation                     |
        +-----------------------------------------------------+
        |
        +-- CONSTRUCTION LAYER -------------------------------+
            Haar/Bessel aggregation + one-edge Schur/Hodge     |  OPEN
            local invariant multiplier algebra                 |  OPEN
            dimension-free square-root commutator              |  OPEN
            full-tree summation => CMH                         |  OPEN
        +-----------------------------------------------------+
```

## Files

- [`claims.md`](claims.md): normalized formulas and an epistemic audit of every major claim.
- [`open-problems.md`](open-problems.md): dispatchable proof tasks and their acceptance gates.
- [`models.md`](models.md): regression models, what each detects, and what it cannot decide.
- [`../../strategy-map.md`](../../strategy-map.md): comparison with the other KLS strategies.
- [`../../../explorations/2026-08-24-kls-moment-map-cmh-consolidation.md`](../../../explorations/2026-08-24-kls-moment-map-cmh-consolidation.md):
  the construction-layer consolidation.
- [`../../../explorations/2026-08-25-kls-cmh-normalization-layer.md`](../../../explorations/2026-08-25-kls-cmh-normalization-layer.md):
  the normalization-layer integration, including what was *not* imported and why.
- [`../../../reviews/2026-08-25-kls-cmh-normalization-audit.md`](../../../reviews/2026-08-25-kls-cmh-normalization-audit.md):
  the original partial audit, retained as proof history; its correction requirements are not an
  unqualified promotion certificate.
- [`../../../reviews/2026-08-25-kls-cmh-normalization-repair-audit.md`](../../../reviews/2026-08-25-kls-cmh-normalization-repair-audit.md):
  the current unqualified certificate for the seven repaired normalization nodes.
- [`../../../reviews/2026-08-25-kls-cmh-exact-cases-repair-audit.md`](../../../reviews/2026-08-25-kls-cmh-exact-cases-repair-audit.md):
  the current unqualified certificate for the ten repaired exact-case nodes.

## Promotion gate

Unchanged, and it now has precedent. No structural identity from an independent summary becomes a
proved ledger node merely by being copied here. Promotion requires:

1. a fully quantified statement with conventions and domains;
2. a standalone dossier in `solutions/`;
3. an independent reviewer and persisted report under `research/reviews/`;
4. matching ledger metadata; and
5. a green `python3 research/check_ledger.py` run.

Only nodes receiving an unqualified node-level verdict may clear this gate. A green checker
validates paths, provenance metadata, and a syntactic pass header naming the node and reviewer;
it does not validate the review's mathematics. The construction-layer claims in `claims.md`
tagged **reported** have cleared none of these gates and remain unpromoted.

Regression calculations may refute or guide the route. Sampled/FEM calculations must flow through
`finum` (target `cmh-gate-zero` for this route); exact finite-dimensional algebra may be recorded
analytically. Neither is a substitute for a proof.
