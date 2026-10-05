(sec:glossary)=
# Glossary of recurring terms

Each entry says what the object is and where it is fixed. Where a normalization is at stake the pointer is to the `prf:definition` that fixes it, because an exponent or a constant quoted without its convention is not a statement.

:::{glossary}
The four approaches
: The four approaches to [](#conj:kls) this manuscript develops, each named by the object it keeps. **The fixed cut** follows one candidate bottleneck set under Eldan's stochastic localization (Section [](#sec:introduction)); **the fixed eigenfunction** follows a first eigenfunction instead of a set (Section [](#sec:spectral-approach)); **the moment map** is deterministic and asks for one inequality for the Hessian of the moment map, with no localization at all (Section [](#sec:moment-map-cmh)); **conditional fibers** replace Euclidean directions by one test-independent isotropic frame of conditional line resamplings (Section [](#sec:conditional-fiber-frame)). They are compared in Section [](#sec:frontier-atlas).

All-cut and near-Cheeger variants
: The two variants of the {term}`fixed cut <The four approaches>`: the all-cut variant asks for the all-cut Carleson estimate for every balanced set (Section [](#sec:carleson)), the near-Cheeger variant only for near-minimizers of the isoperimetric profile, through the weighted near-Cheeger package (Section [](#sec:stein)). See Section [](#subsec:two-variants).

CMH
: The canonical moment-Hessian constant $\CMH$: the deterministic quantity the {term}`moment-map approach <The four approaches>` is built on, fixed with its operator data in [](#def:cmh). It dominates the affine Poincaré constant $\CPaff$ by [](#thm:cmh-implies-affine-poincare), and it is *not* a reformulation of KLS: [](#prop:cmh-hodge) shows it additionally charges a solenoidal excess.

QCTS
: The quadratic-chaos two-tail statement: the static input isolated in [](#def:qcts), together with the two-tail obstruction ([](#rem:two-tail-slice-bounds)) that limits what it can supply.

Two-colour notation
: The two-colour covariance and its bookkeeping, which separate the contribution of the cut being followed from that of everything else, so that a source term can be told from a damping term. Fixed in Section [](#subsec:two-color-notation), used throughout the fixed-cut and fixed-eigenfunction approaches.

Stein source and damping
: In the scalar Riccati equation $\dd r_t=\dd M_t+(S_t-D_t)\dd t$ of [](#thm:scalar-riccati), $S_t$ is the only positive source and $D_t$ the coercive damping. “Absorbing the source into the damping” is what every fixed-cut argument is trying to do; Section [](#sec:stein-dictionary) gives the Stein representation of the source.

Interface functional
: The bridge object $\Xi_T(\mu)$ of the bootstrap comparison, defined at [](#eq:interface-def) and evaluated in Section [](#sec:bootstrap). It is this manuscript's version of “replace $\log$-trace-exp by an effective rank”; why the crude evaluation cannot suffice is [](#rem:insufficiency).

Gate zero
: The moment-Hessian inequality tested on linear functions only — the cheapest test it must pass, hence the first gate that any proof of it, or any counterexample, goes through. Formally, the cheapest necessary consequence of the {term}`moment-map <The four approaches>` {term}`endpoint <Endpoint>`, [](#conj:gate-zero): in isotropic position it asks $\lmax(\E H^2)\le4$ where the literature supplies only the trace bound $\Tr(\E H^2)\le2n$. That trace bound is attained, so the natural operator statement is the *sharp* form $\E H^2\preceq2\Id$ ([](#conj:gate-zero-sharp)), which refines and implies the other. Only the constant $4$ is what $\mathrm{CMH}(4)$ requires, so the two are not interchangeable as falsification targets. Section [](#subsec:gate-zero).

Endpoint
: The word is used in three senses. (1) Mostly, in the moment-map approach, the inequality $\mathrm{CMH}(4)$ itself: the last statement of the chain, which everything else in that approach serves to prove; the *endpoint reduction* is [](#thm:cmh-implies-affine-poincare), from it to the affine Poincaré inequality (Section [](#sec:moment-map-cmh)). The *product endpoint* is the extreme case of that inequality, the product of centered one-sided exponentials, where it holds with equality ([](#cor:cmh-product-saturation)). (2) A statement of the same strength as the conclusion, usable as a final target but not as a first step: the $H^{-1}$ residual bound of Section [](#subsec:spectral-h-minus-one). (3) For a time scale, the largest one a method can reach: $1/\log n$ is the natural endpoint of covariance-only control (Section [](#sec:product-stress)), because the covariance of a product of exponentials spikes to order $\log n$ at that time.

Lift
: Two unrelated senses. (1) The *homogeneous lift*: a function on the simplex rewritten as a degree-zero homogeneous function of independent Gamma variables, which replaces the Dirichlet law by a product of Gamma laws (Section [](#subsec:cmh-gamma-lift)); the *cone lift* goes the other way, attaching a Gamma radial variable to a base so that the cone's moment map is built from the base's ([](#prop:cone-moment-map)). (2) The *invariant multiplier lift* of [](#conj:mm-invariant-lift): the tensor through which a Haar multiplier, defined on one block of a Schur split of the moment-map Hessian, acts on the whole space; it is computed in coordinates and in low split dimensions, and the open question is to identify it intrinsically in every split dimension.

Full-damping occupation
: The hypothesis [](#conj:mm-spectral-occupation) of the fixed eigenfunction. *Occupation* is the source the eigenfunction accumulates over localization time, $\E\int_0^t\norm{H_s}_{\HS}^2\dd s$; *full damping* means it may be charged against the whole damping term $\E\int_0^t2g_s^TA_sg_s\dd s$ with coefficient one, where the fixed cut needs a fraction $\alpha<1$ of its damping. With coefficient one the two cancel exactly in the equation for $\E\abs{g_t}^2$, which is why no surplus is needed ([](#prop:spectral-sufficiency)).

Exponential cone measure
: The law $\bar\mu_{K,\beta}$ with density $\propto x_1^{\beta-n}e^{-x_1}$ on the cone over a centered convex body $K$, centered; [](#def:exponential-cone). Its moment map is explicit in terms of the base's ([](#prop:cone-moment-map)), and at $\beta=n$ it saturates sharp {term}`gate zero <Gate zero>` along its axis, which makes the family the first non-product equality set of that statement. Section [](#subsec:cmh-cones).

Covariance spike
: The obstruction of [](#prop:covariance-spike): products of centered exponentials are dimension-free by tensorization, yet their conditional covariance spikes. It is why no uniform operator-norm bound on $\norm{A_t}_\op$ can exist, and it is the single sharpest constraint on what a correct argument may look like.

Appell coefficients
: For a regular measure $\nu$, $c_k(\nu)=\sqrt{K_k(\nu)}/k!$, where $K_k(\nu)$ is the largest variance of a degree-$k$ Appell polynomial $\langle T,\mathcal A_k^\nu\rangle$ with $\|T\|_{\mathrm{HS}}=1$. Defined in Section [](#sec:sz-notation); KLS is equivalent to $c_k\le A^k$ with one universal $A$ ([](#prop:sz-exponential-coefficients-equivalence)).

Curvature profile
: A function $F$ with $\CP(\nu)\le F(a)$ for every regular isotropic measure of curvature $a$ ($aI\preceq D^2W$), in every dimension. Bakry–Émery gives $F(a)=1/a$; [](#thm:sz-iterated-curvature) gives iterated logarithms, and [](#thm:sz-curvature-transfer) turns any profile into a general bound. Section [](#sec:sz-notation).

Conditional theorem
: A statement that holds under a hypothesis which is itself not settled here, such as [](#prop:spectral-sufficiency). Once proved it is a theorem, and it brings [](#conj:kls) exactly as close as its hypothesis does: whether a statement is true and whether it applies are separate questions.
:::

% Agent notes. In the portfolio each approach keeps its route's letter in its id (`ap:e-…`, `ap:s-…`, `ap:c-…`, `ap:f-…`); the portfolio is search state and carries no truth value.
% A candidate (`cand:` id) is a statement proposed in a checkpoint but not yet a ledger node: no manuscript anchor, no status, no certification.
% "Conditional theorem" is what SPECIFICATION.md calls applicability-blocked: `proved` with a non-empty `assumes`.
