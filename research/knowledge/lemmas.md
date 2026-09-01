# Shared mathematical tools

This file is a compact index of reusable facts. The cited manuscript or ledger label owns the
formal statement; proof dossiers own full arguments and certification. Entries here record only
the fact, its common use, and the main guardrail.

## Holley--Stroock perturbation

**Source.** Holley--Stroock bounded perturbation principle.

**Fact.** If $d\pi=e^{-W}d\nu/Z$ and $\operatorname{osc}(W)\le A$, then
$C_P(\pi)\le e^A C_P(\nu)$, with the analogous log-Sobolev bound.

**Use.** Transfer constants through a uniform density-ratio comparison.

**Guardrail.** Total variation convergence alone does not provide this comparison.

## Tensorization

**Fact.** For $\mu=\bigotimes_i\mu_i$,
$C_P(\mu)=\max_i C_P(\mu_i)$. If coordinate $i$ has weighted constant $C_i$ with weight $a_i$,
then the product has constant $\max_i C_i$ for the form
$\int\sum_i a_i|\partial_i f|^2d\mu$.

**Use.** Lift one-dimensional estimates to product measures.

**Guardrail.** A hierarchical or otherwise dependent law is not a product.

## $T_2$ covariance constraint

**Fact.** Under the convention
$W_2^2(\nu,\pi)\le2C\,\mathrm{KL}(\nu\|\pi)$,
$$
\operatorname{Cov}_\pi(X)\preceq CI,
\qquad
C_{\mathrm{TCI}}(\pi)\ge\lambda_{\max}(\operatorname{Cov}_\pi(X)).
$$

**Use.** Supply a necessary lower constraint for transportation-cost constants.

**Guardrail.** This is not an upper bound or an estimator of the optimal constant.

## Covariance-threshold block extraction

**Source.** The common algebra isolated in
`research/explorations/2026-08-27-kls-route-prober-upgrade-par-01.md` and
`research/explorations/2026-08-27-kls-route-prober-mm-spectral-occupation-par-02.md`.

**Fact.** Let $A\succeq0$, let $X=X^T=A^{1/2}ZA^{1/2}$, and for $L>0$ put
$P=\mathbf 1_{(L,\infty)}(A)$ and $Q=I-P$. Then
$$
\|X\|_{\mathrm{HS}}^2
=\|QXQ\|_{\mathrm{HS}}^2+\|PXP\|_{\mathrm{HS}}^2
+2\|PXQ\|_{\mathrm{HS}}^2,
$$
and
$$
\|QXQ\|_{\mathrm{HS}}^2\le L^2\|QZQ\|_{\mathrm{HS}}^2
\le L^2\|Z\|_{\mathrm{HS}}^2.
$$

**Use.** Convert an intrinsic or whitened Hilbert--Schmidt estimate into a bounded low-covariance
block while retaining every entry incident to the high-covariance space as one explicit residue.

**Guardrail.** This is algebra at a fixed state only. It gives no occupation estimate for the
high-incidence residue, and differentiating the random projector creates additional terms. The
factorization and the bound on $Z$ must be justified in the application; in the two KLS probes
the latter uses the unreviewed Letwin quadratic-Poincar\'e preprint. The identity does not relate
the cut tensor to the eigenfunction tensor.

## `prop:letwin-not-gate-zero` — static commutator split

**Fact.** For symmetric matrices $B,H$,
$$
\operatorname{Tr}(B^2H^2)
=\operatorname{Tr}(BHBH)+\frac12\|[B,H]\|_{\mathrm{HS}}^2.
$$

**Use.** Separate the constant-matrix channel controlled by the Letwin inequality from the
transverse term required by the CMH linear sector. For $B=a\otimes a$, it reads
$|Ha|^2=(a^THa)^2+\|[a\otimes a,H]\|_{\mathrm{HS}}^2/2$.

**Guardrail.** The algebraic countermodel certifies only that positivity, $\mathbb EH=I$, and
constant-matrix control do not bound the transverse term. It is not a moment-map counterexample.
This static commutator is not the stochastic high-incidence block, a moving spectral-projector
It\^o residue, or the square-root/Haar commutator of `q:mm-square-root-commutator`.

## Cut-oriented Lyapunov dual scale

**Source.** Dualization of the agent-certified `lem:pathwise-BL` in
`solutions/kls-localization-riccati-core.tex`; the direct-sum and two-tail calibrations are
recorded in
`research/explorations/2026-08-27-synthesizer-kls-wave-one.md`.

**Fact.** For $A\succ0$ define the Lyapunov operator on symmetric matrices by
$$
\mathscr L_A(M)=\frac{AM+MA}{2}.
$$
The anisotropic form of the certified pathwise Brascamp--Lieb calculation is
$$
s\langle K,M\rangle^2
\le \frac4t\langle M,\mathscr L_A M\rangle
\qquad(M=M^T),
$$
and Hilbert-space duality therefore gives
$$
s\langle K,\mathscr L_A^{-1}K\rangle\le\frac4t.
$$
For $K\ne0$ put
$$
\lambda_{\mathrm{cut}}(A,K)
=\frac{\|K\|_{\mathrm{HS}}^2}
{\langle K,\mathscr L_A^{-1}K\rangle},
$$
and set it to zero for $K=0$. Then
$$
s\|K\|_{\mathrm{HS}}^2\le\frac{4\lambda_{\mathrm{cut}}(A,K)}t.
$$
In an $A$-eigenbasis, $\lambda_{\mathrm{cut}}$ is the $K_{ij}^2$-weighted harmonic mean of
$(\lambda_i+\lambda_j)/2$. It is invariant under irrelevant direct sums:
$\lambda_{\mathrm{cut}}(A\oplus B,K\oplus0)=\lambda_{\mathrm{cut}}(A,K)$, and on the certified
anisotropic two-tail example it equals the inflated variance $\Lambda$.

**Use.** Separate covariance directions incident to a fixed cut tensor from independent
spectator spikes. It is a calibrated candidate scale for a tensor-stable replacement of the
global operator norm in the weighted-excess route.

**Guardrail.** This is a repackaging of a positive-time static inequality, not an occupation or
excess-propagation theorem. The factor $t^{-1}$ is singular at the initial endpoint, and no
bound for an integral weighted by $\lambda_{\mathrm{cut}}$ follows. The scale depends on the
cut tensor and cannot replace a cut-free covariance functional. For singular $A$, restrict the
operator to the covariance support (or state the corresponding Moore--Penrose convention)
before using the formula.
