# Persistent-splitting dossier repair (`w0r03`)

- Date: 2026-08-27
- Role: prover (`/root/repair_splitting_dossier`)
- Primary node: `prop:persistent-splitting`
- Coupled dossier: `solutions/kls-geometry-models.tex`
- Numerical evidence: none

## Preflight

The ledger records `prop:persistent-splitting` as a proved proposition refining
`modules/kls/26-jacobi-splitting.tex`, with no `depends_on` and no `bounded_by` entries. Its
conclusion is that a split direction persists pathwise under stochastic localization, that the
posterior covariance is block diagonal, and that a fixed orthogonal halfspace has
$K_t=\kappa_t\theta\theta^T$ and hence rank at most one.

The coupled dossier also contains candidates for `lem:profile-bound`,
`cor:generic-degeneracy`, `prop:exact-splitting`, `prop:gaussian-model`, and `prop:products`.
Only `cor:generic-degeneracy` has an internal dependency, namely `lem:profile-bound`; that
dependency is already proved in the same dossier. None of these six nodes has a `bounded_by`
fence. The other five theorem statements and proofs were read in full and are unchanged by this
repair.

## Defect and discarded interpretation

The old persistent-splitting statement assumed only that
$V(y,z)=V_1(y)+V_2(z)$ "across" $\theta^\perp\oplus\mathbb R\theta$. If this is read merely as
an equality of finite functions on the support, it does not imply a product law. For example,
the uniform law on a Euclidean disk has finite potential $V=0=0+0$ on its support, but the disk
is not a product support and the law is not a product. A Gaussian-linear localization tilt does
not repair that defect. Thus the proof step "the posterior factorizes" was unjustified under
that weak reading.

The manuscript's reference to the global split model in `prop:exact-splitting` suggests a product
support was intended, but the hypothesis must say so mathematically. I discarded the
support-blind interpretation rather than silently importing a cylindrical-support premise.

## Repaired statement

The dossier now treats potentials globally as extended-valued convex functions. In orthogonal
coordinates $x=y+z\theta$, it assumes proper lower-semicontinuous convex functions

$$
V_1:\theta^\perp\to(-\infty,+\infty],\qquad
V_2:\mathbb R\to(-\infty,+\infty]
$$

with positive finite normalizers and the identity

$$
V(y+z\theta)=V_1(y)+V_2(z)
$$

for every $(y,z)$, including the value $+\infty$ off the effective domain. Consequently

$$
\overline{\operatorname{dom}V}
=\overline{\operatorname{dom}V_1}\times
 \overline{\operatorname{dom}V_2},
\qquad
\mu=\mu_1\otimes\mu_2.
$$

For a fixed halfspace $E_a=\{z\le a\}$ the theorem also explicitly assumes
$0<\mu(E_a)<1$, so every conditional mean and covariance used to define
$\delta_t,G_t,K_t$ exists at every localized time.

## Analytic verification

For each realized localization vector write $c_t=c_t'+c_t''\theta$. The localized potential
splits pointwise in the extended reals as

$$
V_t(y,z)
=\left(V_1(y)+\frac t2|y|^2-c_t'\cdot y\right)
 +\left(V_2(z)+\frac t2z^2-c_t''z\right).
$$

At $t=0$, $c_0=0$ and integrability is assumed. For $t>0$, completing the square gives

$$
e^{c_t'\cdot y-t|y|^2/2}\le e^{|c_t'|^2/(2t)},
\qquad
e^{c_t''z-tz^2/2}\le e^{|c_t''|^2/(2t)},
$$

so both factor normalizers remain positive and finite. Tonelli therefore yields the pathwise
identity $\mu_t=\mu_{1,t}\otimes\mu_{2,t}$, and $A_t$ is block diagonal.

The localization density is strictly positive on the original effective domain, so it preserves
null sets and $0<p_t,q_t<1$. Conditioning the product law on $E_a$ or $E_a^c$ leaves the
$y$ factor unchanged. Hence the two conditional $y$ means and covariances agree and all cross
covariances vanish. For scalar differences $d_t$ and $g_t$ in the $z$ conditional mean and
variance,

$$
\delta_t=d_t\theta,\qquad G_t=g_t\theta\theta^T,
$$

and the exact definition of $K_t$ gives

$$
K_t=G_t+(q_t-p_t)\delta_t\delta_t^T
=\bigl(g_t+(q_t-p_t)d_t^2\bigr)\theta\theta^T.
$$

Thus the claimed rank is at most one, including the possible zero-rank case. The result is
unconditional under its stated global factorization hypothesis and uses no unresolved premise.

## Coupled-dossier preservation and certification consequence

The statement and proof of `prop:persistent-splitting` are the only mathematical content changed
in `solutions/kls-geometry-models.tex`. The five other candidate proofs remain byte-for-byte
unchanged in their mathematical sections. Their mathematical conclusions need no downgrade from
this audit.

Nevertheless, the shared dossier itself has changed after the 2026-08-25 review. Its header now
correctly says `checked_by: none`, leaves the current reviewer and review fields empty, and
retains the old author, reviewer, and review path explicitly as prior-version provenance. Until a
fresh independent review passes, the current file is an unreviewed candidate for all six nodes
that point to it. No ledger edit is applicable from this prover.

The nodes in the separate unchanged dossier `solutions/kls-product-covariance.tex` are not
mathematically affected by this repair, even though their historical review was bundled with the
old geometry dossier.

## Exact synchronization proposals for the orchestrator

These are proposals only; this prover did not edit the manuscript or ledger.

1. In `prop:persistent-splitting`, replace the ambiguous opening hypothesis by:

   > Regard $V$ as a proper extended-valued convex potential on $\mathbb R^n$. Suppose that in
   > orthogonal coordinates $x=y+z\theta$ there are proper lower-semicontinuous convex
   > potentials $V_1,V_2$, with positive finite normalizers, such that
   > $V(y+z\theta)=V_1(y)+V_2(z)$ for all $(y,z)$ in the extended-real sense. Equivalently, both
   > the effective support and the density factor across
   > $\theta^\perp\oplus\mathbb R\theta$.

   Also qualify the halfspace as fixed and nontrivial. The localization formula and conclusions
   currently displayed may then remain, with "rank at most one" retained.

2. Replace the ledger statement for `prop:persistent-splitting` by:

   > If the extended-valued convex potential globally factorizes across
   > $\theta^\perp\oplus\mathbb R\theta$ (so the effective support and law are products), then
   > localization preserves that factorization pathwise, $A_t$ is block diagonal, and every
   > fixed nontrivial orthogonal halfspace has
   > $\delta_t=d_t\theta$ and $K_t=\kappa_t\theta\theta^T$, hence rank at most one.

3. After a cold reviewer passes the current coupled dossier, atomically restore a current
   `checked_by: agent` header and wire the fresh persisted review for all six geometry-dossier
   nodes. Before that review, `solutions/kls-geometry-models.tex` is only the deferred artifact
   candidate.

## Validation

The standalone command

```text
cd solutions && latexmk -pdf -outdir=../build kls-geometry-models.tex
```

returned exit code 0 and produced `build/kls-geometry-models.pdf`. The log contains only the
expected unresolved references to labels in other manuscript subfiles; there is no TeX error.
The first attempted build exposed an undefined local macro `\dom`; it was replaced by
`\operatorname{dom}` before the successful build.

## Unclosed items

There is no flagged analytic gap in the repaired proposition. The only open items are independent
proof review and orchestrator-owned manuscript/ledger synchronization. No numerical claim,
regularization argument, quantitative splitting converse, or implication from
$\mathfrak K_\Sigma=0$ is used.
