---
verdict: pass
authors:
  - wave_a_cone_gate, gpt-6-astra, 2026-10-04
reviewer: reviewer, gpt-6-astra, 2026-10-04
fingerprints:
  solutions/prop-product-simplex-cone-gate.md: 18717df1967dff56165d8c432a4319bc887f514ef6d7e32c4a95c6c5af4eddaa
  prop:product-simplex-cone-gate: 3767edfbb36329386b661db200634f52782cf1eeb8c88366630b9efdc5dd8652
  def:exponential-cone: 96db0678f1fbc57b9271f77008bed7769e77ce93f8d94a58892c3459a848f10f
  prop:cone-moment-map: f61cff79312c7ca8ecd34aea5e0eae226e23b605c81ffdd8e3bd5f2b742e0544
---

## Findings

Full independent certification of `prop:product-simplex-cone-gate`. This reviewer
received the repository paths and review assignment in a fresh context, without
the authoring conversation. The checkpoint was used for scope and provenance,
not as proof evidence. The dossier theorem agrees with the canonical statement
in every quantifier, coefficient, strictness claim, and equality subspace.

The two recorded dependencies supply the cone convention and the canonical
cone kernel. They are respectively defined and proved; there are no open
dependencies, conditional antecedents, or `bounded_by` fences. The reference to
`thm:cmh-dirichlet` is explanatory: its inequality is not used.

**Canonical kernel and normalization.** The linear transformation formula has
the correct normalization sign: for
$\phi_L(y)=\phi(L^\top y)-\log|\det L|$, substitution gives
$\int e^{-\phi_L}=1$ and the gradient pushes forward to $L_\#\mu$.
Thus both kernel and covariance transform by congruence, and
$(L\Sigma L^\top)^{-1/2}L\Sigma^{1/2}$ is orthogonal. This proves the claimed
transport of spectra and equality spaces. A centered nondegenerate simplex is
a linear image of the displayed regular simplex; product normalization
preserves the cone axis.

For the intrinsic simplex computation, the gradient on $H$ is indeed
$p-\mathbf e/N$, and the Hessian is $C(p)/N$. The inverse map is
$y_i=N(\log p_i-N^{-1}\sum_j\log p_j)$, proving the stated global
diffeomorphism. The determinant of any principal $(N-1)$ minor is
$\prod_i p_i$; the product of the nonzero eigenvalues is therefore
$N\prod_i p_i$. Consequently
$\det_H(C/N)=N^{2-N}\prod_i p_i$, proportional to $e^{-\phi}$.
The intrinsic change of variables gives finite mass and uniform target
density, so the additive normalizing constant exists. Scaling the target by
$\sqrt{N(N+1)}$ multiplies the kernel by $N(N+1)$ and gives
$T=(N+1)C$. Sums of normalized factor potentials give the product kernel.
Boundary values are immaterial to these absolutely continuous laws; the
polynomial kernels extend boundedly to the closed simplices.

Identification as the canonical kernel uses the published
Cordero-Erausquin–Klartag moment-measure uniqueness theorem, already used by the
certified cone input. I checked Definition 2 and Theorem 2 on pages 3–4 of the
[source text, arXiv:1304.0630v1](https://arxiv.org/pdf/1304.0630v1).
Finite smooth convex potentials are essentially continuous, and all target
laws here have finite first moment, zero barycenter, and full intrinsic
dimension. The uniqueness hypotheses thus hold. This is the established
result published in *Journal of Functional Analysis* 268 (2015), 3834–3866;
the theorem number used here is that of the accessible source text, not a
claim about journal numbering. No unpublished preprint result is imported.

**Moments.** Iterated beta integration gives the factorial formula with the
correct uniform-simplex normalization. In particular it gives covariance
$[N(N+1)]^{-1}I_H$ for $P-\mathbf e/N$. For the fourth-degree sum, the diagonal
contribution is $24/[(N+1)(N+2)(N+3)]$ and the ordered distinct-index
contribution is $4(N-1)/[(N+1)(N+2)(N+3)]$, yielding the stated
$\mathbb E Q_2^2$. The formulas for $\mathbb E Q_2$ and $\mathbb E Q_3$ and
all three trace identities check directly. Dividing the resulting traces by
$N-1$ yields exactly $a_k,b_k,c_k$. The permutation argument is valid even
for the potentially nonsymmetric expectation $\mathbb E[VV^\top T]$:
the commutant of all permutation matrices on $H$ consists of scalars.
The transpose expectation has the same scalar. Nothing fails at $N=2$,
so intervals are included.

**Cone assembly.** The radial Jacobian is $s^{n-1}$, giving independent
$S\sim\Gamma(\beta,1)$ and uniform $U$; its first two moments give the
displayed covariance. Using the certified cone kernel, direct multiplication
gives axis entry $\beta+1+\mathbb E|U|^2=\beta+n$ and transverse block
$(\beta+1)I+\mathbb E B^2$. Independent vertex permutations act orthogonally
on each factor, preserve its joint $(V,T)$ law, and have no invariant vector
on $H$. Averaging in one factor annihilates every mixed factor block and the
axis/transverse vector. Independence gives
$\mathbb E[(|U|^2UU^\top)_{jj}]=(c_{k_j}+m-k_j)I$; the other two terms give
$2\beta b_{k_j}I$ and $\beta^2a_{k_j}I$. Covariance normalization then gives
the stated eigenvalues. Bounded base variables and kernels, together with
$\mathbb E S^2<\infty$, justify every expectation and product used.

**Exact gap and equality.** Writing $D=(k+3)(k+4)$, expansion before the change
of variables gives

$$
D\beta(\beta+1)(2-\lambda_k)
=4(k+3)\beta^2+(-3k^2-5k+4)\beta-D(n-k)-Dc_k.
$$

At $\beta=n$ this factors as
$4(n-k-1)((k+3)n+k+1)$. Substituting $\beta=n+t$ and
$n=k+1+d$ yields exactly the dossier's polynomial. Its coefficients of
$t^2,t,d$ in the displayed decomposition are positive. Thus its zero set on
$t,d\ge0$ is precisely $t=d=0$. Since every other factor has positive
dimension, $d=0$ means $q=1$. Combining this with the axis gap
$(\beta-n)/\beta$ proves all strictness and equality assertions, with no
restriction of $\beta$ to integers.

**Hypotheses and build.** Used hypotheses are: finitely many factors
$q\ge1$; integer dimensions $k_j\ge1$; nondegenerate simplices; the centered
Cartesian-product base; $n=1+\sum_j k_j$; real $\beta\ge n$; and invertibility
of any coordinate change. Nondegeneracy is supplied by “simplex of dimension
$k_j$” and the convex-body convention. Centering gives the covariance block
form, product structure gives independence, and $\beta\ge n$ gives the gap
sign and the prescribed log-concave cone class. No hidden hypothesis or unused
theorem assumption was found. The moment algebra alone works for
$\beta>0$, but that extension is not certified as a separate claim.
`uv run scripts/check.py` completed with exit code 0 and no MyST error.
The recorded fingerprints are the subsequent checker output for this dossier.

## Corrections

None required. The phrase “every coefficient is strictly positive” in the
gap argument is read as referring to the positive multipliers of
$t^2,t,d$ displayed there; the constant term as a polynomial in $t$ is zero
when $d=0$, exactly as the following equality analysis says.

## Exclusions

This certifies only `prop:product-simplex-cone-gate`, not either universal gate
conjecture, nonlinear CMH, general convex bases, or a characterization of
equality outside this family. It does not certify the older candidate's
parametrization or its additional product-law wording. Existing cone results
are used as certified inputs and are not re-certified. The surrounding
manuscript prose and other agents' work were not audited. No numerical run
was used as evidence, and no step of this dossier remains unverified.

## Proposed transition

Set `prop:product-simplex-cone-gate` to `proved`, retain
`depends_on: [def:exponential-cone, prop:cone-moment-map]`, and add:

```yaml
proofs:
  - artifact: solutions/prop-product-simplex-cone-gate.md
    review: research/reviews/2026-10-04-wave-a-cone-gate-review.md
```

No `assumes`, `bounded_by`, or refutation relation is added.
