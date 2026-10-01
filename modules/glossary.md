(sec:glossary)=
# Glossary of recurring terms

Each entry says what the object is and where it is fixed. Where a normalization is at stake the pointer is to the `prf:definition` that fixes it, because an exponent or a constant quoted without its convention is not a statement.

:::{glossary}
Approaches E, S, C, F
: The four approaches to [](#conj:kls) this manuscript develops, in the order they appear. **E** follows a fixed candidate bottleneck cut under stochastic localization (Section [](#sec:introduction)); **S** follows a fixed first eigenfunction instead of a cut (Section [](#sec:spectral-approach)); **C** is deterministic and works in moment-map coordinates, with no localization at all (Section [](#sec:moment-map-cmh)); **F** replaces Euclidean directions by one test-independent isotropic frame of conditional line resamplings (Section [](#sec:conditional-fiber-frame)). The letters are a reading aid.

Subroutes E–A and E–B
: The two branches of {term}`Approach E <Approaches E, S, C, F>`: E–A is the all-cut Carleson estimate (Section [](#sec:carleson)), E–B the weighted near-Cheeger package (Section [](#sec:stein)). See Section [](#subsec:two-variants).

CMH
: The canonical moment-Hessian constant $\CMH$: the deterministic quantity {term}`Approach C <Approaches E, S, C, F>` is built on, fixed with its operator data in [](#def:cmh). It dominates the affine Poincaré constant $\CPaff$ by [](#thm:cmh-implies-affine-poincare), and it is *not* a reformulation of KLS: [](#prop:cmh-hodge) shows it additionally charges a solenoidal excess.

QCTS
: The quadratic-chaos two-tail statement: the static input isolated in [](#def:qcts), together with the two-tail obstruction ([](#rem:two-tail-slice-bounds)) that limits what it can supply.

Two-colour notation
: The two-colour covariance and its bookkeeping, which separate the contribution of the cut being followed from that of everything else, so that a source term can be told from a damping term. Fixed in Section [](#subsec:two-color-notation), used throughout Approaches E and S.

Stein source and damping
: In the scalar Riccati equation $\dd r_t=\dd M_t+(S_t-D_t)\dd t$ of [](#thm:scalar-riccati), $S_t$ is the only positive source and $D_t$ the coercive damping. “Absorbing the source into the damping” is what every fixed-cut argument is trying to do; Section [](#sec:stein-dictionary) gives the Stein representation of the source.

Interface functional
: The bridge object $\Xi_T(\mu)$ of the bootstrap comparison, defined at [](#eq:interface-def) and evaluated in Section [](#sec:bootstrap). It is this manuscript's version of “replace $\log$-trace-exp by an effective rank”; why the crude evaluation cannot suffice is [](#rem:insufficiency).

Gate zero
: The cheapest necessary consequence of the {term}`Approach C <Approaches E, S, C, F>` endpoint, [](#conj:gate-zero): in isotropic position it asks $\lmax(\E H^2)\le4$ where the literature supplies only the trace bound $\Tr(\E H^2)\le2n$. That trace bound is attained, so the natural operator statement is the *sharp* form $\E H^2\preceq2\Id$ ([](#conj:gate-zero-sharp)), which refines and implies the other. Only the constant $4$ is what $\mathrm{CMH}(4)$ requires, so the two are not interchangeable as falsification targets. Section [](#subsec:gate-zero).

Exponential cone measure
: The law $\bar\mu_{K,\beta}$ with density $\propto x_1^{\beta-n}e^{-x_1}$ on the cone over a centered convex body $K$, centered; [](#def:exponential-cone). Its moment map is explicit in terms of the base's ([](#prop:cone-moment-map)), and at $\beta=n$ it saturates sharp {term}`gate zero <Gate zero>` along its axis, which makes the family the first non-product equality set of that statement. Section [](#subsec:cmh-cones).

Covariance spike
: The obstruction of [](#prop:covariance-spike): products of centered exponentials are dimension-free by tensorization, yet their conditional covariance spikes. It is why no uniform operator-norm bound on $\norm{A_t}_\op$ can exist, and it is the single sharpest constraint on what a correct argument may look like.

Conditional theorem
: A statement that holds under a hypothesis which is itself not settled here, such as [](#prop:spectral-sufficiency). Once proved it is a theorem, and it brings [](#conj:kls) exactly as close as its hypothesis does: whether a statement is true and whether it applies are separate questions.
:::

% Agent notes. In the portfolio each approach keeps its route's letter in its id (`ap:e-…`, `ap:s-…`, `ap:c-…`, `ap:f-…`); the portfolio is search state and carries no truth value.
% A candidate (`cand:` id) is a statement proposed in a checkpoint but not yet a ledger node: no manuscript anchor, no status, no certification.
% "Conditional theorem" is what SPECIFICATION.md calls applicability-blocked: `proved` with a non-empty `assumes`.
