# CMH route — normalized claim inventory

This file consolidates the independent CMH/Haar/Schur--Piola exploration without collapsing its
epistemic levels. Tags used below are:

- **external-v1** — verified against a named July 2026 version-1 preprint;
- **formal** — follows algebraically from the displayed definitions, subject to domains and
  regularity;
- **reported** — supplied by the independent exploration but not yet persisted as an R1/R2
  artifact in this repository;
- **open** — a proposed estimate or implication;
- **retracted** — a form the originating exploration withdrew. Retraction is preserved even when
  its witness still needs a repository dossier.

## 1. External moment-map layer

On the regular moment-map class, where the displayed potentials are smooth, strictly convex,
$\nabla\phi$ is a diffeomorphism, and the required integrations by parts are valid, let

$$
d\nu(y)=e^{-\phi(y)}\,dy,\qquad (\nabla\phi)_\#\nu=\mu,\qquad H=D^2\phi.
$$

If $d\mu=e^{-V(x)}dx$ with normalized potentials, the change of variables gives

$$
\log\det H=-\phi+V(\nabla\phi).
$$

If either density is only specified up to proportionality, an additive normalization constant
must be included. Integration by parts and isotropy give $\mathbb E_\nu H=I$. In target
coordinates,

$$
\tau_\mu(x)=H\bigl((\nabla\phi)^{-1}(x)\bigr)
$$

is Fathi's positive symmetric Stein kernel. Approximation is required before conclusions derived
from this representation are asserted for an arbitrary log-concave law.

The following are **external-v1**. The Hessian formulas are direct regular-map theorems; the
distributional thin-shell, third-tensor, and quadratic Poincaré conclusions extend to arbitrary
isotropic log-concave laws through the approximation arguments in the respective preprints.

1. Chen--Klartag:
   $$
   \mathbb E_\nu\lVert H\rVert_{\mathrm{HS}}^2\le2n,
   \qquad
   \operatorname{Var}(|X|^2)\le8n,
   \qquad
   \lVert T_3(X)\rVert_{\mathrm{HS}}^2\le4n.
   $$
2. Letwin, for every constant symmetric $B$:
   $$
   \mathbb E_\nu\operatorname{tr}(BHBH)\le2\operatorname{tr}(B^2),
   $$
   and for every constant symmetric $M$:
   $$
   \operatorname{Var}\langle MX,X\rangle
   \le2\,\mathbb E|\nabla\langle MX,X\rangle|^2
   =8\operatorname{tr}(M^2).
   $$

Taking $B=I$ recovers the shared moment-Hessian estimate, but not all of Chen--Klartag's sharp
third-tensor, cone, simplex, or equality analysis. Letwin's theorem concerns homogeneous
quadratic forms; it must not be paraphrased as the same sharp inequality for every affine
quadratic polynomial.

For

$$
M_\theta=\mathbb E[\langle X,\theta\rangle X\otimes X],
$$

Letwin obtains $\sup_\theta\lVert M_\theta\rVert_{\mathrm{HS}}\le2\sqrt2$. Combined with
Klartag's improved Lichnerowicz comparison, this gives the current **preprint-conditional**
general bounds

$$
C_P(\mu)\lesssim\sqrt{\log n},
\qquad
h_n^\star\gtrsim(\log n)^{-1/4}.
$$

## 2. Headline CMH target: regular-class normalization discharged, closure and headline open

The originating exploration proposed

$$
\lVert\Sigma^{-1/2}H\nabla g\rVert_2^2
\le4\lVert-Lg\rVert_2^2
\tag{CMH(4)}
$$

and reported that a divergence-duality reduction would yield $C_P(\mu)\le4$. Until 25 August 2026
this was **open in the repository** because the source defined neither $\Sigma$, nor the measure
behind $\lVert\cdot\rVert_2$, nor the domain of $L$, nor the closure used in the duality step.

**The regular-class part of that debt is paid** (`thm:cmh-implies-affine-poincare`, dossier
`solutions/thm-cmh-normalization.tex`). The original audit at
`research/reviews/2026-08-25-kls-cmh-normalization-audit.md` was partial and is retained as
history. The corrected proofs now carry the unqualified certificate
`research/reviews/2026-08-25-kls-cmh-normalization-repair-audit.md`; the exact-case dossier is
separately certified by
`research/reviews/2026-08-25-kls-cmh-exact-cases-repair-audit.md`. The data are:

$$
L_\mu g=\operatorname{div}_\mu(H\nabla g)=\operatorname{tr}(HD^2g)-p\cdot\nabla g,
\qquad
\mathsf A=-L_\mu\ge0,
\qquad
\operatorname{div}_\mu u=\rho^{-1}\operatorname{div}(\rho u),
$$

$$
C_{\mathrm{CMH}}(\mu)
=\sup_{g\in\operatorname{Dom}(\mathsf A)\setminus\ker\mathsf A}
\frac{\mathbb E_\mu\langle H\nabla g,\Sigma^{-1}H\nabla g\rangle}
      {\mathbb E_\mu(L_\mu g)^2},
$$

with $L^2=L^2(\mu)$, every inverse the pseudoinverse on $(\ker\mathsf A)^\perp$, and
$\Sigma^{-1}$ the Moore--Penrose inverse on the affine tangent space for measures on a proper
affine subspace. The symmetry of $L_\mu$ *for $\mu$ itself* is exactly the Stein identity
$\operatorname{div}_\mu H=-p$; this is what makes the definition canonical rather than a choice
of reference measure.

**Status ladder for the headline.** The reduction $C_P^{\mathrm{aff}}\le C_{\mathrm{CMH}}$ is
proved on the regular moment-map class. The passage through approximation
(`q:cmh-approximation`) and universal $\mathrm{CMH}(4)$ are open. The Hodge identity in §12
exhibits an additional nonnegative channel, but does not prove strict non-implication from KLS;
§13 shows that the cheapest necessary consequence is not available from the external inputs by
matrix algebra alone. Do not paraphrase the reduction as an equivalence.

The constant $4$ is the sharp plausible endpoint: the centered one-sided exponential has
$C_P=4$ with unit variance, and by `thm:cmh-1d` its CMH constant is exactly $4$.

## 3. Operator and Haar layer

On the mean-zero subspace of $L^2(\nu)$, let $D$ be the closed gradient, $D_\nu^*$ its weighted
adjoint, and formally set

$$
N=D_\nu^*H^{-1}D,
\qquad
Q_M=D_\nu^*H^{-1/2}MH^{-1/2}D.
$$

With inverses interpreted on the orthogonal complement of the kernel,

$$
R=H^{-1/2}DN^{-1/2},
\qquad
K_M=R^*MR.
$$

Then $R^*R=I$ and, as a quadratic-form identity on a common core,

$$
Q_M=N^{1/2}K_MN^{1/2}.
$$

Consequently the noncommutation error is **formal**:

$$
e_M(u):=Q_Mu-K_MNu
=[N^{1/2},K_M]N^{1/2}u.
$$

For a normalized complete family of Haar contrast multipliers $M_S$, the exploration reports

$$
\sum_S\lVert K_Sh\rVert^2
\le\left(1-\frac1n\right)\lVert h\rVert^2
$$

and the exact Bessel deficit

$$
\mathfrak B(h)
=\left(1-\frac1n\right)\lVert h\rVert^2-
  \sum_S\lVert K_Sh\rVert^2
=\sum_S\lVert(I-RR^*)M_SRh\rVert^2.
$$

The identity is algebraically plausible once
$\sum_SM_S^2=(1-1/n)I$ is fixed. Its normalization, index set, and operator domains must be
included in the dossier; until then it is **reported**, not ledger-proved.

The full sibling form is

$$
\widehat{\mathfrak S}(u)
=\mathfrak B(Nu)
-2\sum_S\operatorname{Re}\langle K_SNu,e_S(u)\rangle
-\sum_S\lVert e_S(u)\rVert^2.
$$

It explains why a complete-tree estimate, not nodewise positivity, is the natural target.

## 4. Positive reservoir and coupling warning

Write

$$
U=D^2u,
\qquad
A=H^{-1/2}UH^{-1/2},
$$

and let $F_i$ solve

$$
(-\Delta+\nabla\phi\cdot\nabla)F_i
=\partial_i u-\mathbb E_\nu\partial_i u.
$$

The exploration reports the exact deficit factorization

$$
\begin{aligned}
4\mathbb E_\nu\lVert A\rVert_{\mathrm{HS}}^2
-\operatorname{Var}_\nu(\nabla u)
={}&\mathbb E_\nu\operatorname{tr}((4I-H)A^2)\\
&+\mathbb E_\nu\lVert UH^{-1/2}-DFH^{1/2}\rVert_{\mathrm{HS}}^2\\
&+\mathbb E_\nu\sum_i\lVert D^2F_i\rVert_{\mathrm{HS}}^2.
\end{aligned}
$$

This is **reported** pending a full integration-by-parts/domain proof. The last two terms form a
global positive reservoir. The exploration also reports an analytic high-frequency
product-exponential obstruction to assigning that reservoir only to the conformal part of the
first term. Therefore conformal, traceless, mixed, and corrector contributions must remain
coupled.

## 5. Schur--Piola geometry

For a $1+d$ split, write

$$
H=\begin{pmatrix}h&b^\top\\b&C\end{pmatrix},\qquad
v=C^{-1}b,\qquad
s=h-b^\top C^{-1}b,\qquad
\Delta=\det C,
$$

and set $X=\partial_r-v\cdot\nabla_q$. Direct block algebra gives

$$
\operatorname{cof}H
=\Delta\begin{pmatrix}
1&-v^\top\\
-v&vv^\top+sC^{-1}
\end{pmatrix}.
$$

Piola's identity and Hessian compatibility formally yield

$$
\operatorname{div}(\Delta X)=0,
\qquad
Xv=C^{-1}\nabla_qs,
$$

and

$$
XC=J^\top C=CJ,
\qquad J^\alpha{}_{\beta}=\partial_\beta v^\alpha.
$$

Thus

$$
T=C^{-1/2}(XC)C^{-1/2}
$$

is symmetric and

$$
\operatorname{tr}T=X\log\det C=\operatorname{div}_qv.
$$

For the child target coordinate $z=\nabla_q\phi$, $Xz=0$. For the full target
$x=\nabla\phi$,

$$
Xx_\perp=0,\qquad Xx_0=s.
$$

Hence $Y=s^{-1}X$ is the pullback of $\partial_{x_0}$. Subject to boundary/domain conditions,

$$
Y^*=-Y+V_0,
\qquad
\lVert Y^*f\rVert_2^2
=\lVert Yf\rVert_2^2+\int V_{00}(\nabla\phi)f^2\,d\nu.
$$

The block, target-coordinate, and trace identities are **formal and algebraically consistent**.
They show that the conformal derivative is the divergence of the Schur connection, not a free
scalar mode.

## 6. Local multiplier algebra

At a Schur-normal $1+2$ point, let $T\in\operatorname{Sym}_2$, $a,g\in\mathbb R^2$, let $R$
be a fixed quarter-turn, and define

$$
B_i=\operatorname{sym}(g\otimes R^\top e_i).
$$

For the fixed-target lift ($Xz=0$), the exploration reports

$$
\begin{aligned}
Q(a,T,g)
={}&8|a|^2+\frac12\sum_i\lVert\{B_i,T\}\rVert_{\mathrm{HS}}^2
-4a\cdot RTg\\
={}&8\left|a-\frac14RTg\right|^2
+\frac32|Tg|^2+\frac14(\operatorname{tr}T)^2|g|^2.
\end{aligned}
$$

The displayed completion of squares has been **independently checked as a coordinate identity**,
but the route still needs an invariant audit showing that this is the actual lift produced by the
global operator calculation. In the conformal specialization $T=\theta I$, the residual
coefficient is $5\theta^2|g|^2/2$. The more general claim

$$
Q\ge0\text{ for all }a,T,g
\quad\Longleftrightarrow\quad
\alpha\ge-1\text{ or }\alpha\le-3
$$

cannot be reproduced from the summary alone because the $\alpha$-dependent definition of $Q$
was omitted. It remains **reported**. The artificial $\alpha=-2$ negative example is therefore
not evidence against the natural geometry.

## 7. Hodge and Stein-kernel residuals

Use divergence in the second tensor index and fix the sign conventions

$$
\operatorname{div}_\rho F=\rho^{-1}\operatorname{div}(\rho F),
\qquad
\delta_\rho=-\operatorname{div}_\rho.
$$

Let $S(z)=\mathbb E[C\mid z]$ be the inherited child block and $K(z)$ the canonical child
moment-map Stein kernel. Since both solve the same Stein equation,

$$
\mathsf D=S-K,
\qquad
\partial_\beta(\rho\mathsf D_{\alpha\beta})=0.
$$

Locally in two dimensions, and globally subject to topology/boundary normalization, a symmetric
divergence-free tensor has an Airy representation

$$
\rho\mathsf D=R^\top D^2\lambda R.
$$

With

$$
g=2\rho^{-1}R\nabla\lambda,
\qquad
B_i=\operatorname{sym}(g\otimes R^\top e_i),
$$

the exploration reports

$$
\operatorname{div}_\rho B_i=\mathsf D e_i,
\qquad
\sum_i\lVert B_i\rVert_{\mathrm{HS}}^2=\frac32|g|^2.
$$

For datum $h$, let $F_h$ be the canonical parent flux,
$\bar h=\mathbb E[h\mid z]$, and
$\bar F=\mathbb E[(F_h)_z\mid z]$. With

$$
F_K=K\nabla A_K^{-1}\bar h,
\qquad
r_h=\bar F-F_K,
$$

one has $\delta_\rho r_h=0$. Writing

$$
v=A_S^{-1}\bar h,
\quad
r_{\mathrm{cond}}=\bar F-S\nabla v,
\quad
\Pi_K=K\nabla A_K^{-1}\delta_\rho,
$$

the reported exact decomposition is

$$
r_h=r_{\mathrm{cond}}+(I-\Pi_K)\mathsf D\nabla v.
$$

This separates a conditional-flux channel from a canonical-versus-inherited Stein-kernel
mismatch. It also explains why a purely local vector stress cannot encode the full problem.

## 8. One-edge deficit

With the flux notation fixed as above, the exploration reports

$$
\begin{aligned}
4\lVert h\rVert^2-\lVert F_h\rVert^2
={}&\underbrace{4\lVert h-\bar h\rVert^2-\lVert F_0\rVert^2
-\lVert(F_h)_z-\bar F\rVert^2}_{\Delta_{\mathrm{fiber}}}\\
&+\underbrace{4\lVert\bar h\rVert^2-\lVert F_K\rVert^2}_{\Delta_{\mathrm{child}}}\\
&-\underbrace{\left(2\langle F_K,r_h\rangle+\lVert r_h\rVert^2\right)}
_{\mathcal H_{\mathrm{sibling}}}.
\end{aligned}
$$

The identity is **reported** because $F_0$, all Hilbert spaces, and the conditional projection
conventions need to be supplied. Its content is clear: the sibling cross term must be absorbed by
the joint fiber, Airy, corrector, and descendant reservoirs.

## 9. The noncommutative commutator

For $A_M=H^{-1/2}MH^{-1/2}$, the exploration corrects an earlier cancellation claim and reports
the cubic symbol

$$
C_3(\xi)=2\left[
(H^{-1}\xi)^r(\partial_rA_M)(\xi,\xi)
-(A_M\xi)^r(\partial_rH^{-1})(\xi,\xi)
\right].
$$

Writing

$$
\Omega_k=\frac12\left(
H^{-1/2}\partial_kH^{1/2}-(\partial_kH^{1/2})H^{-1/2}
\right),
$$

the proposed invariant form is

$$
C_3(\xi)=2(H^{-1}\xi)^k
\xi^\top H^{-1/2}[\Omega_k,M]H^{-1/2}\xi.
$$

Thus the symbol measures eigenframe rotation and vanishes under purely conformal metric
variation. This formula is **reported pending an invariant symbol dossier**.

For a positive self-adjoint $N$, the standard form-level resolvent representation is

$$
[N^{1/2},K_M]
=\frac1\pi\int_0^\infty
t^{1/2}(N+t)^{-1}[N,K_M](N+t)^{-1}\,dt,
$$

under the hypotheses needed to define the commutators and integral. This is the bridge from local
symbol control to the global square-root error.

## 10. Exact remaining target

The route aims to define a nonnegative retained remainder
$\mathfrak R_{\mathrm{Letwin}}(u)$ containing all applicable variable-multiplier, Codazzi,
Monge--Ampère, corrector, and descendant squares, and then prove

$$
2\sum_S\operatorname{Re}\langle K_SNu,e_S(u)\rangle
+\sum_S\lVert e_S(u)\rVert^2
\le
\mathfrak B(Nu)+\mathfrak R_{\mathrm{Letwin}}(u)
$$

dimension-freely over the complete Haar tree. This is **open**. It is not yet a fully quantified
conjecture because the retained remainder, lift convention, common core, and tree normalization
must be frozen first. Even a proof for the listed $1+2$, $1+3$, and $2+2$ coefficient forms is
not automatically dimension-free: the route also needs a proved irreducible reduction covering
all higher-dimensional splits (or a genuinely higher-dimensional stress-potential argument).

## 11. Retraction ledger

| proposal | status after exploration | repository status |
|---|---|---|
| Letwin directly proves full KLS | retracted | externally false as a reading of the paper |
| nodewise sibling positivity | retracted | reported witness; no persisted dossier yet |
| fixed fractional descendant allocation | retracted | reported Laguerre near-extremizers |
| free bad conformal scalar | retracted locally | Schur--Piola and local algebra oppose it |
| arbitrary multiplier derivative / $\alpha=-2$ | retracted | geometrically inadmissible in originating analysis |
| cubic symbol cancels completely | retracted | corrected nonzero symbol reported above |
| $\mathbb E[\operatorname{cof}(T)a\mid z]$ is conserved | retracted | reported Gamma--Gaussian counterexample |
| Airy mismatch explains every negative node | retracted | conditional/scalar channel remains |
| corrector controls conformal sector alone | retracted | reported high-frequency counterexample |
| natural local $1+2$ algebra is positive | survives provisionally | invariant lift audit still required |
| one global matrix-coupled approach remains plausible | open | commutator is the best identified bottleneck, not yet the only formal gap |

Retractions are kept to prevent dead-end reruns. They do not become uppercase `REFUTED` ledger
claims unless their analytic witness or an eligible `finum` artifact is persisted.

---

# Part B — the normalization layer (added 25 August 2026)

Sections 1--11 above are the **construction layer**: Haar compression, Schur--Piola geometry, and
the square-root commutator. Sections 12--15 are the **normalization layer**, which shares the
target $\mathrm{CMH}(4)$ and almost none of the machinery. Manuscript:
`modules/kls/41-cmh-normalization.tex` and `modules/kls/42-cmh-exact-cases.tex`.

Epistemic tags in this part differ from Part A: **proved** here means the repository's full R2
contract (dossier + independent reviewer + persisted report + green checker), not "formal".

## 12. Hodge content: an extra solenoidal channel — **proved; strict separation open**

Set $u=H\nabla g$, $h=-\operatorname{div}_\mu u$, let $\psi$ solve
$-\operatorname{div}_\mu(\Sigma\nabla\psi)=h$ on the centered subspace, and $w=u-\Sigma\nabla\psi$.
Then $\operatorname{div}_\mu w=0$, the two fields are orthogonal in $L^2(\mu;\Sigma^{-1})$, and

$$
\mathbb E_\mu\langle u,\Sigma^{-1}u\rangle
=\mathbb E_\mu\langle\Sigma\nabla\psi,\nabla\psi\rangle
+\mathbb E_\mu\langle w,\Sigma^{-1}w\rangle .
$$

The operator norm of $h\mapsto\mathbb E_\mu\langle\Sigma\nabla\psi,\nabla\psi\rangle$ on the
centered subspace is **exactly** $C_P^{\mathrm{aff}}(\mu)$. Hence CMH = affine Poincaré **plus**
control of the solenoidal excess $w$.

In dimension one the no-flux convention forces $w=0$, which is why `thm:cmh-1d` is an identity.
In higher dimension the divergence-free subspace need not be trivial, but this decomposition does
not show that the solenoidal term is positive at a CMH extremizer, nor does it exhibit a measure
with $C_P^{\mathrm{aff}}\le4<C_{\mathrm{CMH}}$.

Thus the certified conclusion is $C_{\mathrm{CMH}}\ge C_P^{\mathrm{aff}}$ together with an exact
description of the extra channel. Equivalence and strict non-implication at a fixed constant are
open. A future CMH counterexample would close this sufficient-condition route but, by itself,
would not refute KLS.

## 13. Gate zero and the algebraic countermodel — **proved**

Testing the definition on $g(p)=a\cdot p$ (so $D^2g=0$, $L_\mu g=-a\cdot p$) gives the necessary
condition

$$
\mathbb E[H\Sigma^{-1}H]\preceq4\Sigma
\qquad\text{(gate zero, `conj:gate-zero`)},
$$

equivalently $\mathbb EH^2\preceq4I$ in isotropic position. This is **necessary** for universal
$\mathrm{CMH}(4)$ and is **not** a known consequence of KLS.

The gap between gate zero and Letwin's theorem is exactly one commutator:

$$
\operatorname{tr}(B^2H^2)=\operatorname{tr}(BHBH)
+\tfrac12\lVert[B,H]\rVert_{\mathrm{HS}}^2 ,
$$

valid for symmetric $B,H$ because $[B,H]$ is antisymmetric. Letwin controls the first term with
constant $2$; the second is the **static transverse commutator**, and it is unconstrained by
matrix moments:

> **Countermodel (exact).** For $m\ge18$, let $z$ be uniform on $S^{m-1}$,
> $d=m/\sqrt{2m-1}$, $c=1-d/m$, and
> $H(z)=\begin{pmatrix}1&\sqrt d\,z^\top\\ \sqrt d\,z&cI_m+dzz^\top\end{pmatrix}$.
> Then $H\succeq0$, $\mathbb EH=I$, and
> $\mathbb E\operatorname{tr}(BHBH)\le2\operatorname{tr}(B^2)$ for **every** symmetric $B$
> (the three $O(m)$ sectors decouple; the scalar-sector deficit is exactly $(a-dt)^2$, a perfect
> square, because $d^2=m^2/(2m-1)$). Yet $e_1^\top\mathbb EH^2e_1=1+d>4$ iff $m^2-18m+9>0$,
> i.e. iff $m\ge18$.

**Scope discipline.** These matrices are *not* claimed to be moment-map Hessians; no
Monge--Ampère or Codazzi compatibility is imposed. The proposition does **not** refute gate zero.
What it proves is that any proof of gate zero must consume differential moment-map structure —
equivalently, must bound $\mathbb E\lVert[B,H]\rVert_{\mathrm{HS}}^2$. It is the elementary,
static, finite-dimensional shadow of `q:mm-square-root-commutator`, and it places a floor under
that task's difficulty: the commutator may not be treated as a lower-order correction.

**Placement warning.** In isotropic position gate zero asks $\lambda_{\max}(\mathbb EH^2)\le4$
while Chen--Klartag already give $\operatorname{tr}(\mathbb EH^2)\le2n$. It is therefore an
operator-to-trace upgrade with a factor-2 budget and belongs to the ownership cluster of
`rem:trace-upgrade-unification`. Hard constraint 6 of `CLAUDE.md` applies.

## 14. Exact classes — **proved**

| class | result | note |
|---|---|---|
| line | $C_{\mathrm{CMH}}(\mu)=C_P(\mu)/\operatorname{Var}(\mu)$ | an **identity**; $\le4$ for log-concave, sharp at the one-sided exponential |
| products | $C_{\mathrm{CMH}}=\max_i C_P(\mu_i)/\operatorname{Var}(\mu_i)$ | cross terms $\mathbb E[(L_ig)(L_jg)]=\mathbb E[\tau_i\tau_j(\partial_{ij}g)^2]\ge0$ |
| log-concave Dirichlet | $A(A+1)\,d_\alpha(g)\le4\,n_\alpha(g)$ for all $\alpha_i\ge1$ | the route's **first nonproduct theorem** |

The Dirichlet proof lifts $g$ homogeneously to independent
$Y_i\sim\Gamma(\alpha_i,1)$ with $S=\sum_iY_i$, $P=Y/S$, $S\perp P$; uses the exact Gamma row
completion

$$
N_\Gamma(G)-\tfrac14D_\Gamma(G)=\sum_i\mathbb ER_i+\sum_i\delta_iD_i(G),
\qquad
\delta_i=\frac{\alpha_i^2}{(\alpha_i+1)^2}-\frac14 ;
$$

minimizes each Hessian row under the differentiated Euler constraint
$\sum_jY_jG_{ij}=-G_i$ (reciprocal weights sum to $S/Y_i$); and closes with a two-branch scalar
minimization giving the surplus form

$$
n_\alpha(g)\ \ge\ \Bigl(\frac{A(A+1)}4+s_A\Bigr)d_\alpha(g),
\qquad
s_A=\begin{cases}(z_A-2)/4,&z_A\le4\\ \sqrt{z_A}-3/2,&z_A\ge4\end{cases},
\quad z_A=(A-1)(A-2).
$$

**Log-concavity is consumed twice.** For the product-Gamma consequence,
$\delta_i\ge0\iff\alpha_i\ge1$ is the required sign. In the Dirichlet proof, however,
$\delta_i$ is retained exactly inside the angular coefficient, and the separate hypothesis
$a=\alpha_i\ge1$ is load-bearing in its two-branch minimization. The differential identities
remain algebraic beyond that range where their moments exist, but the Dirichlet bound does not.

Two readings matter and are easy to get backwards:

- $s_A>0$ for $A>3$ means the Dirichlet family sits **strictly inside** the bound
  (`cor:cmh-dirichlet-surplus`). It is a family theorem, **not** evidence for universal
  $\mathrm{CMH}(4)$.
- The saturating cases are elsewhere. By the product formula, products of one-sided exponentials
  hit $C_{\mathrm{CMH}}=4$ **exactly**, with zero slack. Sharpness on the simplex is inherited
  from the same one-dimensional exponential mechanism through the face law
  $\mathrm{Beta}(1,b)$, whose CMH constant is
  $(b+1)^2(b+2)/(b\,j_{b/2,1}^2)\to4$.

## 15. The exposed endpoint — **open, and the sharpest available probe**

Combining §12 and §14: a product of centered one-sided exponentials saturates
$\mathrm{CMH}(4)$ with zero slack, and the CMH numerator splits into a gradient part plus a
solenoidal excess. This motivates a perturbative test, but increasing the solenoidal component
alone does not control the Poincar\'e component, the denominator, or the optimizing direction.

The open node `q:cmh-solenoidal-perturbation` therefore asks for the second variation of the
*full CMH Rayleigh quotient*. A certified perturbation for which that quotient exceeds $4$ would
refute universal CMH(4) without refuting KLS. See task **M9** in
[`open-problems.md`](open-problems.md).
