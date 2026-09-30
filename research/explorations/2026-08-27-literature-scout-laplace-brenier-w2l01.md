---
---
# Literature scout: the Laplace--Brenier simplex gate

Date: 2026-08-27

Role: literature-scout

Run id: w2l01

## Exact search target

For $d\geq 1$, let
$$
 d\lambda_d(z)=2^{-d/2}\exp(-\sqrt2\|z\|_1)\,dz,
 \qquad \operatorname{Cov}(\lambda_d)=I_d,
 \qquad C_P(\lambda_d)=2.
$$
For $U\in O(d)$ put $\eta_U=U_\#\lambda_d$.  Given an isotropic log-concave target
$\mu$, let $T_U=\nabla\Phi_U$ be the quadratic-cost Brenier map from $\eta_U$ to
$\mu$.  The direct-transfer target is
$$
 \inf_{U\in O(d)}\operatorname*{ess\,sup}_{x\in\mathbb R^d}
 \|D^2\Phi_U(x)\|_{\rm op}\leq C
 \tag{LB}
$$
with a universal $C$.  Indeed, (LB) and the source Poincare inequality give
$$
 \operatorname{Var}_\mu f
 =\operatorname{Var}_{\eta_U}(f\circ T_U)
 \leq 2C^2\int |\nabla f|^2\,d\mu.
$$

The proposed kill test is the uniform law on the isotropic regular simplex $K_d$ in
$H=\{y\in\mathbb R^{d+1}:\sum_i y_i=0\}$, whose vertices are
$$
 v_i=\sqrt{(d+1)(d+2)}
 \left(e_i-\frac{1}{d+1}{\bf 1}\right).
$$
Thus
$$
 \operatorname{diam}(K_d)=\sqrt{2(d+1)(d+2)},
 \qquad
 |K_d|=\frac{\sqrt{d+1}\,((d+1)(d+2))^{d/2}}{d!}.
$$
The exact literature question was whether a theorem proves or refutes
$$
 \inf_{U\in O(d)}\operatorname{Lip}(T_U)=O(1)
 \tag{S}
$$
for this target, and in particular whether simplex corners, the Laplace cusp, or a rotation-invariant
lower bound settles (S).

Weaker neighbours searched for were an $L^p(\eta_U)$ operator-Hessian bound, a directional bound
paired with simplex widths, and a dimension-free estimate for a one-sided-exponential source.  The
stronger neighbour was a universal bound for every compactly supported log-concave target.

## Found 1: Gwozdz's support--curvature estimate

**Source and classification.** Maja Gwozdz, *Dimension-Free Lipschitz Bounds for Brenier Maps to
Compactly Supported Log-Concave Targets*, arXiv:2608.15906v1, submitted 16 August 2026,
[abstract and version record](https://arxiv.org/abs/2608.15906),
[paper](https://arxiv.org/pdf/2608.15906).  Classification:
`preprint-unreviewed`.  I read Theorem 1.1, the proof outline, the source-smoothing and stability
lemmas in Section 7, and the proof of Theorem 1.1 in the actual v1 paper, not only the abstract.

**Exact statement in local normalization.** Let
$d\sigma=Z^{-1}e^{-V(x)}dx$ have finite second moment, let $Q\succ0$, and assume that
$$
 x\longmapsto \frac12\langle Qx,x\rangle-V(x)
 \quad\text{is convex.}
 \tag{G1}
$$
Let $\nu$ be any compactly supported log-concave probability measure with support $K$, including a
lower-dimensional or singular target, and let $\nabla\Phi$ be the Brenier map from $\sigma$ to $\nu$.
Then, in distributions, for every $v\in\mathbb R^d$,
$$
 \partial_{vv}\Phi
 \leq 0.587\sqrt{\langle Qv,v\rangle}\,w_K(v),
 \qquad
 w_K(v)=\sup_{y\in K}\langle y,v\rangle-
          \inf_{y\in K}\langle y,v\rangle,
 \tag{G2}
$$
and $\nabla\Phi$ has an everywhere-defined representative satisfying
$$
 \operatorname{Lip}(\nabla\Phi)
 \leq 0.587\sqrt{\|Q\|_{\rm op}}\operatorname{diam}(K).
 \tag{G3}
$$
The paper also gives a fully analytic constant $1.828$; the sharper decimal $0.587$ uses the paper's
interval-arithmetic certificate.  No numerical observation from that certificate is treated here as a
repository proof.

**Conversion.** Condition (G1) is exactly the distributional upper Hessian condition
$D^2V\preceq Q$.  For the standard Gaussian, $Q=I$, and for the isotropic simplex (G3) becomes
$$
 \operatorname{Lip}(T_{\gamma\to K_d})
 \leq 0.587\sqrt{2(d+1)(d+2)}=O(d).
$$
Thus the preprint removes Kolesnikov's additional $\sqrt d$ loss but does not give the $O(1)$ scale
needed by the direct KLS transfer on an isotropic simplex.

**Decisive applicability check for the Laplace source.** For
$$
 V_U(x)=\sqrt2\|U^Tx\|_1,
$$
(G1) fails for every finite $Q$ and every $U$.  Write $u_j=Ue_j$.  At any $x$ on the cusp hyperplane
$u_j^\perp$ and away from the other cusp hyperplanes,
$$
 V_U(x+tu_j)+V_U(x-tu_j)-2V_U(x)=2\sqrt2|t|.
$$
The semiconcavity consequence of (G1) would bound this by
$\langle Qu_j,u_j\rangle t^2$, which is impossible as $t\downarrow0$.  Equivalently,
$D^2V_U$ contains positive surface-measure terms on the cusp hyperplanes and is not bounded above by
any matrix.  Rotation merely rotates these hyperplanes.

The approximation step in Gwozdz does not repair this failure.  Its Gaussian smoothing lemma preserves
an *already existing* uniform upper Hessian bound.  For the usual smoothing
$\sqrt2\sqrt{s^2+\varepsilon^2}$ of a one-dimensional Laplace cusp, the second derivative at zero is
$\sqrt2/\varepsilon$, so the required source constant diverges.  Hence the theorem is not a hidden
proof of the Laplace route.

**Boundary bearing.** The theorem applies to a uniform law on a nonsmooth simplex.  Therefore simplex
facets and vertices alone do not force a Brenier map from every reasonable full-support source to lose
global Lipschitz regularity.  The unresolved feature in (S) is the interaction between those corners and
the source's codimension-one cusps, not ordinary target-boundary regularity.

## Found 2: Kolesnikov's 2010 estimates and the still-explicit exponential-source problem

**Source and classification.** Alexander V. Kolesnikov, *Global Holder Estimates for Optimal
Transportation*, *Mathematical Notes* **88** (2010), 678--695,
DOI [10.1134/S0001434610110076](https://doi.org/10.1134/S0001434610110076);
the source version is arXiv:0810.5043v4, revised 12 January 2010,
[version record](https://arxiv.org/abs/0810.5043),
[paper](https://arxiv.org/pdf/0810.5043).  Classification: `published`.  I read the statements and
proofs in Sections 3--4 of v4 and verified the publication metadata at MathNet.  This is the paper
referred to as “Kolesnikov 2010” in the proposed route.

**Exact relevant statement.** Theorem 4.2 assumes a *smooth* source potential.  In a unit direction
$h$, it requires $V_{hh}\leq\Lambda$; its dimension-free directional refinement additionally uses
$|V_h|\leq M$.  For a product source $\mu_0^{\otimes d}$ with
$d\mu_0=e^{-V}dx$, $|V'|\leq1$, and $V''\leq1$, Corollary 4.3(2) yields, for any $-1<p<0$,
$$
 \|D^2\Phi\|_{\rm op}
 \leq
 \frac{\sqrt{-p\left(1+\frac{d}{4(1+p)}\right)}}
 {2\int_0^{\pi/2}\sin^{-1-1/p}(s)\,ds}
 \operatorname{diam}(K)
 \tag{K1}
$$
for transport to normalized Lebesgue measure on a bounded convex $K$.  The source examples in the
corollary are only *Laplace-like*: $V$ may agree with $|x|$ for large $|x|$ but is quadratic near zero.

The survey *Mass Transportation and Contractions*, arXiv:1103.1479v1,
[paper](https://arxiv.org/pdf/1103.1479), Section 4, restates these estimates and poses as Problem 4.3
the dimension-free control problem both for a Gaussian source and for a product of exponential
distributions.  Gwozdz resolves the Gaussian support-controlled problem up to the unavoidable
$\operatorname{diam}(K)$ scale, but does not resolve the exponential-source problem.

**Conversion and gap.** For the exact rotated Laplace potential, every nonzero direction has an
unbounded distributional second derivative on at least one cusp hyperplane.  Smooth approximants have
$\Lambda\to\infty$.  Moreover,
$$
 \sup_x |\nabla V_U(x)|=\sqrt{2d},
$$
independently of $U$.  Thus a worst-direction use of Kolesnikov's $M$ loses the rotation information
that (S) is designed to exploit.  Neither (K1) nor its proof supplies a uniform limit at the exact cusp.

Kolesnikov's paper therefore confirms that the proposed route attacks a genuine old transport question;
it does not settle the simplex test in either direction.

## Found 3: multiplicative eigenvalue concentration does not control the gate

**Source and classification.** Bo'az B. Klartag and Alexander V. Kolesnikov, *Eigenvalue Distribution
of Optimal Transportation*, *Analysis & PDE* **8** (2015), 33--55,
DOI [10.2140/apde.2015.8.33](https://doi.org/10.2140/apde.2015.8.33),
[source paper](https://arxiv.org/pdf/1402.2636).  Classification: `published`.  I read Theorems
1.1, 1.2, and 1.5 and their hypotheses in the source.

Under the paper's $C^2$ Brenier-potential hypothesis, if
$0<\lambda_1(x)\leq\cdots\leq\lambda_d(x)$ are the eigenvalues of $D^2\Phi(x)$ and $X$ has the source
law, then
$$
 \operatorname{Var}(\log\lambda_i(X))\leq4
 \qquad(1\leq i\leq d).
 \tag{KK}
$$
The paper also proves a Poincare inequality for the joint log-eigenvalue vector and the analogous
variance bound for $\log\langle D^2\Phi(X)v,v\rangle$.

This is dimension-free control of *fluctuations around an unspecified scale*.  It neither bounds the
typical value of $\lambda_d$ nor an essential supremum, and hence does not imply (LB).  It also does not
optimize over $U$.  It is a possible tool only after a separate scale estimate and a tail-to-$L^\infty$
upgrade, neither of which was found.

## Analytic simplex checks that delimit any claimed obstruction

These checks are derivations from the local normalization, not literature imports.

### The Monge--Ampere determinant gives only a constant lower bound

For the uniform simplex target, at almost every twice differentiability point,
$$
 \det D^2\Phi_U(x)
 =|K_d|\,2^{-d/2}\exp(-\sqrt2\|U^Tx\|_1).
$$
If $\|D^2\Phi_U\|_{\rm op}\leq L$ essentially, taking the essential supremum of the right-hand side
gives
$$
 L\geq \left(|K_d|2^{-d/2}\right)^{1/d}
 =\frac{(d+1)^{1/(2d)}\sqrt{(d+1)(d+2)}}
        {\sqrt2\,(d!)^{1/d}}
 \longrightarrow \frac{e}{\sqrt2}.
$$
This is rotation-invariant, but it is compatible with (S).  Thus determinant balance at the common cusp
intersection does **not** kill the route.

### One-sided exponentials give a non-Brenier comparison, not the desired map

If $E_1,\ldots,E_{d+1}$ are independent standard one-sided exponentials and
$S=\sum_iE_i$, then $(E_i/S)_i$ is uniform on the standard simplex.  This exact representation explains
why one-sided exponentials are geometrically tempting.  However, normalization by $S$ is a
dimension-reducing, non-injective map, is not the quadratic Brenier map in (S), and its derivative contains
$S^{-1}$, hence is unbounded as $S\downarrow0$.  It may motivate an averaged-derivative or quotient route,
but it does not establish the pointwise direct-transfer gate.

## What the literature does not give

No source read in this search proves any of the following:

1. a dimension-free $L^\infty$ Hessian bound for the Brenier map from exact product Laplace measure to
   an arbitrary bounded log-concave target;
2. such a bound for the regular simplex after optimizing the rotation $U$;
3. a rotation-invariant lower bound diverging with $d$ for the same simplex map;
4. an approximation theorem that passes Kolesnikov's or Gwozdz's estimates through the Laplace cusp
   with constants uniform in the smoothing scale;
5. a theorem turning multiplicative eigenvalue concentration into the required essential supremum.

Accordingly, the simplex kill gate remains open.  The most precise residual statement is:

> Determine whether there are $U_d\in O(d)$ and a universal $C$ such that the Brenier solution of
> $$
> \det D^2\Phi_d(x)=|K_d|2^{-d/2}e^{-\sqrt2\|U_d^Tx\|_1},
> \qquad \nabla\Phi_d(\mathbb R^d)=K_d,
> $$
> satisfies $\|D^2\Phi_d\|_{L^\infty({\rm op})}\leq C$; or prove that the infimum over $U_d$ diverges.

The new preprint makes one strategic point sharp: adapting its translation--Schur-complement coercivity
would require replacing the quadratic source-semiconcavity error by a mechanism that can absorb the
linear cusp increment $2\sqrt2|t|$.  Merely smoothing the source cannot do this uniformly.

## Proposed ledger delta

None.  The published results above are relevant baselines but do not discharge or refute the active gate.
The Gwozdz result is an unreviewed preprint and, even if imported, would be inapplicable to the Laplace
source.  Creating a dependency node for it now would therefore add citation debt without advancing the
route.  If the orchestrator wants a literature node for transport-family completeness, it must remain
`import_class: preprint-unreviewed` and downstream consumers must remain `conditional`.

## Exact bibliography proposals

These keys are absent from the current `fi_references.bib`.  The orchestrator may append the entries if
the route or manuscript cites the results.

```bibtex
@article{Kolesnikov2010GlobalHolder,
  author        = {Kolesnikov, Alexander V.},
  title         = {Global {H}\"older Estimates for Optimal Transportation},
  journal       = {Mathematical Notes},
  volume        = {88},
  number        = {5--6},
  pages         = {678--695},
  year          = {2010},
  doi           = {10.1134/S0001434610110076},
  eprint        = {0810.5043},
  archivePrefix = {arXiv},
  primaryClass  = {math.FA}
}

@misc{Gwozdz2026DimensionFreeBrenier,
  author        = {Gw{\'o}{\'z}d{\'z}, Maja},
  title         = {Dimension-Free {Lipschitz} Bounds for {Brenier} Maps to Compactly Supported Log-Concave Targets},
  year          = {2026},
  eprint        = {2608.15906},
  archivePrefix = {arXiv},
  primaryClass  = {math.AP},
  note          = {Version 1, 16 August 2026; unreviewed preprint}
}

@article{KlartagKolesnikov2015EigenvalueTransport,
  author        = {Klartag, Bo'az B. and Kolesnikov, Alexander V.},
  title         = {Eigenvalue Distribution of Optimal Transportation},
  journal       = {Analysis \& PDE},
  volume        = {8},
  number        = {1},
  pages         = {33--55},
  year          = {2015},
  doi           = {10.2140/apde.2015.8.33},
  eprint        = {1402.2636},
  archivePrefix = {arXiv},
  primaryClass  = {math.AP}
}
```

## Citation debt

- The repository did not previously cite any of the three sources above, so no existing ledger claim was
  found to depend on an unverified version of them.
- The proposed route's informal reference to “Kolesnikov 2010” should resolve to
  `Kolesnikov2010GlobalHolder`, not to the distinct Kolesnikov--Milman Orlicz-ball paper already in the
  bibliography.
- Any use of the numerical constant $0.587$ must cite arXiv:2608.15906v1 and be classified
  `preprint-unreviewed`.  The paper separately supplies the analytic constant $1.828$; neither version
  covers the Laplace source.
- No collision with a repository `bounded_by` fence was found.  The constant determinant lower bound is
  compatible with the conjectural $O(1)$ gate.

## Searched and not found

Primary-source and bibliographic searches included:

- `Kolesnikov 2010 mass transportation exponential measure convex body Lipschitz`;
- `Global Holder estimates optimal transportation Kolesnikov PDF`;
- `Brenier map product exponential to simplex Lipschitz`;
- `optimal transport Laplace measure uniform simplex Lipschitz Brenier`;
- `regular simplex optimal transport exponential measure Hessian Monge Ampere`;
- `lower bound Lipschitz Brenier map simplex exponential source`;
- `Brenier map to regular simplex Lipschitz lower bound`;
- `optimal transport source nonsmooth bounded gradient compact convex target Lipschitz`;
- `dimension-free Hessian Brenier compact log-concave target`;
- `Gwozdz Brenier Laplace log-concave simplex`;
- `rotation optimization Brenier map product exponential convex body`;
- `uniform simplex normalized independent exponentials Lipschitz transport`.

I found no paper analyzing the rotation-optimized quadratic Brenier map from product Laplace measure to a
regular simplex, and no simplex-specific pointwise lower bound for its operator Hessian.  Papers on
Monge--Ampere equations *on the boundary* of a simplex concern different source and target spaces and do
not address (S).  “Dirichlet transport” papers use a different multiplicative/logarithmic cost on the
simplex and likewise do not provide the Euclidean quadratic Brenier estimate.

## Handoff

```yaml
outcome: complete
artifacts:
  - research/explorations/2026-08-27-literature-scout-laplace-brenier-w2l01.md
proposed_deltas:
  - "No ledger delta: no verified source resolves or refutes the rotation-optimized Laplace-to-simplex gate."
  - "Optionally append bibliography keys Kolesnikov2010GlobalHolder, Gwozdz2026DimensionFreeBrenier, and KlartagKolesnikov2015EigenvalueTransport exactly as specified above when the route is cited."
next_role: orchestrator
next_prompt: |
  Keep the Laplace--Brenier proposal at the simplex kill gate. Record that Gwozdz arXiv:2608.15906v1 proves a dimension-free support--curvature estimate for sources with D^2V preceq Q, including nonsmooth simplex targets, but that every rotated product-Laplace potential violates this hypothesis by a linear cusp second difference. Do not claim that target corners kill the route, and do not use source smoothing: its upper-Hessian constant diverges. Ask the route prober to attack the exact residual PDE with rotation optimization, using the constant determinant lower bound only as a calibration, not a refutation. If citing the literature, apply the three BibTeX entries above through the bibliography orchestrator and classify Gwozdz as preprint-unreviewed.
```
