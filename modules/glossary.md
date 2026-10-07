(sec:glossary)=
# Glossary of recurring terms

Each entry says what the object is and where it is fixed. Where a normalization is at stake the pointer is to the `prf:definition` that fixes it, because an exponent or a constant quoted without its convention is not a statement.

:::{glossary}
Alternative mechanisms
: The three mechanisms for the Poincaré bound this manuscript develops besides the three proofs of [](#conj:kls), each named by the object it keeps, each resting on a sufficient condition that implies KLS, with no converse known. **The moment map** is deterministic and asks for one inequality for the Hessian of the moment map, with no localization at all (Chapter [](#sec:moment-map-cmh)); **the fixed eigenfunction** follows a first eigenfunction under Eldan's stochastic localization (Chapter [](#sec:spectral-approach)); **conditional fibers** replace Euclidean directions by one test-independent isotropic frame of conditional line resamplings (Chapter [](#sec:conditional-fiber-frame)). They are compared in Chapter [](#sec:frontier-atlas). **The fixed cut**, which follows one would-be bottleneck set under localization, is kept as an archive for its obstructions and counterexamples (Chapter [](#sec:introduction)).

All-cut and near-Cheeger variants
: The two variants of the {term}`fixed cut <Alternative mechanisms>`: the all-cut variant asks for the all-cut Carleson estimate for every balanced set (Chapter [](#sec:carleson)), the near-Cheeger variant only for near-minimizers of the isoperimetric profile, through the weighted near-Cheeger package (Chapter [](#sec:stein)). See Section [](#subsec:two-variants).

CMH
: The canonical moment-Hessian constant $\CMH$: the deterministic quantity the {term}`moment-map mechanism <Alternative mechanisms>` is built on, fixed with its operator data in [](#def:cmh). It dominates the affine Poincaré constant $\CPaff$ by [](#thm:cmh-implies-affine-poincare); it also charges a solenoidal excess ([](#prop:cmh-hodge)), discussed in Chapter [](#sec:moment-map-cmh).

QCTS
: Quadratic-chaos thin shell: the bound $\Var(X^TMX)\le C\norm M_{\HS}^2$ for isotropic log-concave $X$ and every symmetric matrix $M$, defined in [](#def:qcts); Letwin's [](#thm:letwin-qcts) gives $C=8$. What it can supply to the fixed cut is limited by the anisotropic two-tail cut of [](#prop:two-tail) ([](#rem:two-tail-slice-bounds)).

Two-color notation
: The two-color covariance and its bookkeeping, which separate the contribution of the cut being followed from that of everything else, so that a source term can be told from a damping term. Fixed in Section [](#subsec:two-color-notation), used throughout the fixed-eigenfunction and fixed-cut arguments.

Stein source and damping
: In the scalar Riccati equation $\dd r_t=\dd M_t+(S_t-D_t)\dd t$ of [](#thm:scalar-riccati), $S_t$ is the only positive source and $D_t$ the coercive damping. “Absorbing the source into the damping” is what every fixed-cut argument is trying to do; Section [](#sec:stein-dictionary) gives the Stein representation of the source.

Interface functional
: The bridge object $\Xi_T(\mu)$ of the bootstrap comparison, defined at [](#eq:interface-def) and evaluated in Chapter [](#sec:bootstrap). It is this manuscript's version of “replace $\log$-trace-exp by an effective rank”; why the crude evaluation cannot suffice is [](#rem:insufficiency).

Linear test
: The moment-Hessian inequality tested on linear functions only, its cheapest necessary condition: in isotropic position, $\lmax(\E H^2)\le4$ ([](#conj:gate-zero)), where the literature gives the trace bound $\Tr(\E H^2)\le2n$. Its sharp form is $\E H^2\preceq2\Id$ ([](#conj:gate-zero-sharp)). Some statements and labels call it *gate zero*. Section [](#subsec:gate-zero).

Endpoint
: The word is used in three senses. (1) Mostly, in the moment-map mechanism, the inequality $\mathrm{CMH}(4)$ itself: the last statement of the chain, which everything else in that mechanism serves to prove; the *endpoint reduction* is [](#thm:cmh-implies-affine-poincare), from it to the affine Poincaré inequality (Chapter [](#sec:moment-map-cmh)). The *product endpoint* is the extreme case of that inequality, the product of centered one-sided exponentials, where it holds with equality ([](#cor:cmh-product-saturation)). (2) A statement of the same strength as the conclusion, usable as a final target but not as a first step: the $H^{-1}$ residual bound of Section [](#subsec:spectral-h-minus-one). (3) For a time scale, the largest one a method can reach: $1/\log n$ is the natural endpoint of covariance-only control (Chapter [](#sec:product-stress)), because the covariance of a product of exponentials spikes to order $\log n$ at that time.

Lift
: Two unrelated senses. (1) The *homogeneous lift*: a function on the simplex rewritten as a degree-zero homogeneous function of independent Gamma variables, which replaces the Dirichlet law by a product of Gamma laws (Section [](#subsec:cmh-gamma-lift)); the *cone lift* goes the other way, attaching a Gamma radial variable to a base so that the cone's moment map is built from the base's ([](#prop:cone-moment-map)). (2) The *invariant multiplier lift* of [](#conj:mm-invariant-lift): the tensor through which a Haar multiplier, defined on one block of a Schur split of the moment-map Hessian, acts on the whole space; it is computed in coordinates and in low split dimensions, and the open question is to identify it intrinsically in every split dimension.

Full-damping occupation
: The hypothesis [](#conj:mm-spectral-occupation) of the fixed eigenfunction. *Occupation* is the source the eigenfunction accumulates over localization time, $\E\int_0^t\norm{H_s}_{\HS}^2\dd s$; *full damping* means it may be charged against the whole damping term $\E\int_0^t2g_s^TA_sg_s\dd s$ with coefficient one, where the fixed cut needs a fraction $\alpha<1$ of its damping. With coefficient one the two cancel exactly in the equation for $\E\abs{g_t}^2$, which is why no surplus is needed ([](#prop:spectral-sufficiency)).

Exponential cone measure
: The law $\bar\mu_{K,\beta}$ with density $\propto x_1^{\beta-n}e^{-x_1}$ on the cone over a centered convex body $K$, centered; [](#def:exponential-cone). Its moment map is explicit in terms of the base's ([](#prop:cone-moment-map)), and at $\beta=n$ it saturates sharp {term}`linear test <Linear test>` along its axis, which makes the family the first non-product equality set of that statement. Section [](#subsec:cmh-cones).

Covariance spike
: The obstruction of [](#prop:covariance-spike): products of centered exponentials are dimension-free by tensorization, yet their conditional covariance spikes. It is why no uniform operator-norm bound on $\norm{A_t}_\op$ can exist, and it is the single sharpest constraint on what a correct argument may look like.

Appell coefficients
: For a regular measure $\nu$, $c_k(\nu)=\sqrt{K_k(\nu)}/k!$, where $K_k(\nu)$ is the largest variance of a degree-$k$ Appell polynomial $\langle T,\mathcal A_k^\nu\rangle$ with $\|T\|_{\mathrm{HS}}=1$. Defined in Section [](#sec:sz-notation); KLS is equivalent to $c_k\le A^k$ with one universal $A$ ([](#prop:sz-exponential-coefficients-equivalence)).

Compatible tensor field
: A symmetric tensor field whose distributional derivative is fully symmetric, so that its entries satisfy the curl-free relations in [](#def:bk-compatible-calculus). BK's argument integrates these fields repeatedly after choosing centered primitives. Its Hodge estimate controls the loss when weighted divergence is projected back onto compatible fields ([](#lem:bk-compatible-hodge)); it is distinct from the moment-Hessian comparison [](#cor:cmh-hodge-comparison).

Common integration prefactor
: The factor $Q_D(B)$ in [](#lem:bk-uniform-power-bound), independent of the power $k$ in $\|R^k\|^2\le B^kQ_D(B)$. The BK proof uses finitely many polynomial observations to obtain this bound simultaneously for all powers. Replacing it by separate bounds on each integration would multiply the prefactor repeatedly and discard the gain.

Curvature profile
: A function $F$ with $\CP(\nu)\le F(a)$ for every regular isotropic measure of curvature $a$ ($aI\preceq D^2W$), in every dimension. Bakry–Émery gives $F(a)=1/a$; [](#thm:sz-iterated-curvature) gives iterated logarithms, and [](#thm:sz-curvature-transfer) turns a profile into a bound for every isotropic log-concave measure by localizing to curvature of order $1/\log(en)$. That transfer gives the first-version bound [](#thm:song-zhang-kls) and the intermediate [](#thm:sz-v2-dimension-bound); the final argument of the second version, [](#thm:sz-v2-kls), does not use it, but transfers coefficient caps ([](#prop:sz-v2-static-coefficient-transfer)) and passes to general measures by regular approximation. Section [](#sec:sz-notation).

Conditional theorem
: A statement that holds under a hypothesis which is itself not settled here, such as [](#prop:spectral-sufficiency). Once proved it is a theorem, and it brings [](#conj:kls) exactly as close as its hypothesis does: whether a statement is true and whether it applies are separate questions.
:::

% Agent notes. In the portfolio each approach keeps its route's letter in its id (`ap:e-…`, `ap:s-…`, `ap:c-…`, `ap:f-…`); the portfolio is search state and carries no truth value.
% A candidate (`cand:` id) is a statement proposed in a checkpoint but not yet a ledger node: no manuscript anchor, no status, no certification.
% "Conditional theorem" is what SPECIFICATION.md calls applicability-blocked: `proved` with a non-empty `assumes`.
