---
verdict: pass
authors:
  - /root/prove_lyapunov_stein_duality_w2
  - /root/repair_lyapunov_stein_duality_w2
reviewer: /root/review_lyapunov_stein_duality_w2
fingerprints:
  solutions/lem-lyapunov-stein-duality.md: ae84f79fdf8592f8f30915efe881a59ff99cae41befb5a5bd2fcd0a6a80c68ff
  lem:lyapunov-stein-duality: 053e29d7fe7f570d943da7b4c27630eed5d4519a07957ef9b8374692fd518213
  lem:pathwise-BL: 5b8de97a90772764778ad79fc4a9f56642c732304f4792a95b6cc493c7a95d6a
  prop:two-tail: 85de1f26b16a82f85696ec5a655749365c0f036976c11265cee235f780c44d7b
---

*Follows up* `research/reviews/2026-08-27-lem-lyapunov-stein-duality-proof-review.md`.

# Cut-oriented Lyapunov--Stein duality — repaired proof review

This is a fresh independent review of `solutions/lem-lyapunov-stein-duality.tex` at SHA-256
`ea4680b012c611bb99af21639f885e05103e610e698139ee2f55445d5d28dc33`.  The earlier append-only
audit named in `follows_up` remains an audit and certifies nothing; the repaired bytes were
reconstructed and checked anew.  The two dossier authors and this reviewer are distinct, and
the authorship records name no reviewer as an author.  The repair exploration was used only to
check provenance and the pinned hash, not as mathematical evidence.

## Findings

### Repaired scope and three-way statement agreement

The formal dossier lemma at lines 53--77 now ends after exactly three claims:

1. on the covariance support,
   $$
   s_t\langle K_t,\mathscr L_{A_t}^{-1}K_t\rangle\le \frac4t;
   $$
2. with the quotient defined for $K\ne0$ and
   $\lambda_{\rm cut}(A,0)=0$,
   $$
   s_t\|K_t\|_{\mathrm{HS}}^2
   \le \frac{4\lambda_{\rm cut}(A_t,K_t)}t;
   $$
3. for positive-semidefinite covariance blocks and a supported active tensor,
   $$
   \lambda_{\rm cut}(A\oplus B,K\oplus0)=\lambda_{\rm cut}(A,K).
   $$

These are mathematically identical to the labeled manuscript lemma at
`modules/kls/21-carleson.tex:141`--`165` and the synchronized ledger statement at
`research/kls/ledger.yaml:201`--`207`.  The manuscript phrases the last assertion as invariance
under independent spectator blocks in the covariance-support context; the dossier and ledger
merely spell out the implicit positive-semidefinite and support domain.  They neither narrow nor
strengthen the manuscript claim.

The weighted-harmonic-mean identity and exact two-tail calibration are no longer in the formal
lemma or its proof.  They occur in the explicitly auxiliary remark at dossier lines 149--194,
which says they are not assertions of the lemma, matching the adjacent non-lemma manuscript
prose at lines 167--172.  Thus the formal theorem scope now agrees on all three proof planes.

### Covariance support and Moore--Penrose convention

Put $Y=X-a_t$ and $H_t=\operatorname{Ran}(A_t)$.  If $v\in\ker A_t$, then

$$
0=v^TA_tv=\mathbb E_{\mu_t}(v\cdot Y)^2.
$$

Applying this identity to a finite orthonormal basis of the kernel gives $Y\in H_t$ almost
surely.  Conditional translated means, conditional centered vectors, and hence
$\delta_t$, $\Sigma_t^E$, and $\Sigma_t^F$ are supported on $H_t$.  Therefore
$K_t=P_tK_tP_t$, as required before applying the support inverse.

In an orthonormal $A$-eigenbasis, the Lyapunov operator
$\mathscr L_A(M)=(AM+MA)/2$ has eigenvalue $\lambda_i$ on a diagonal symmetric mode and
$(\lambda_i+\lambda_j)/2$ on the normalized off-diagonal symmetric mode.  Its ambient
Moore--Penrose inverse consequently has entries

$$
(\mathscr L_A^\dagger C)_{ij}
=\begin{cases}
2C_{ij}/(\lambda_i+\lambda_j),&\lambda_i+\lambda_j>0,\\
0,&\lambda_i+\lambda_j=0.
\end{cases}
$$

For $K=PKP$, every entry involving an ambient null direction vanishes.  This is exactly the
inverse on $\operatorname{Sym}(\operatorname{Ran}A)$ followed by zero extension, including
singular ambient covariances.  No full-rank convention is hidden.

### Exact anisotropic inequality and factor four

For $M\in\operatorname{Sym}(H_t)$, let

$$
f_M(x)=(x-a_t)^TM(x-a_t)-\operatorname{Tr}(MA_t),
\qquad
g=\frac{\mathbf1_E-p_t}{\sqrt{s_t}}.
$$

The assumptions $p_t,q_t>0$ make $g$ well defined, with
$\mathbb Eg=\mathbb Ef_M=0$ and $\mathbb Eg^2=1$.  The certified two-color covariance identity
gives

$$
\mathbb E[f_M\mid E]=q_t\langle K_t,M\rangle,
\qquad
\mathbb E_{\mu_t}[g f_M]=\sqrt{s_t}\langle K_t,M\rangle.
$$

On its affine support the posterior is $t$-uniformly log-concave.  Cauchy--Schwarz and
Brascamp--Lieb therefore yield

$$
s_t\langle K_t,M\rangle^2
\le \operatorname{Var}_{\mu_t}(f_M)
\le \frac1t\mathbb E_{\mu_t}|\nabla_{H_t}f_M|^2
=\frac4t\operatorname{Tr}(MA_tM).
$$

The constant $4$ comes exactly from $\nabla_{H_t}f_M=2M(X-a_t)$; there is no operator-norm
scalarization in this step.  At fixed $t>0$, the posterior Gaussian factor gives the required
polynomial moments.  Smooth truncation and closure of the Brascamp--Lieb form justify the
unbounded quadratic test, including nonsmooth log-concave data on an affine support.

The invoked inverse-Hessian variance inequality is a published result of Brascamp and Lieb,
*Journal of Functional Analysis* 22 (1976), DOI
[`10.1016/0022-1236(76)90004-5`](https://doi.org/10.1016/0022-1236(76)90004-5).  Its exact
constant-one form was also checked in equation (1.3) of the published primary paper of
Carlen--Cordero-Erausquin--Lieb, *Ann. Inst. H. Poincar\'e Probab. Statist.* 49 (2013), DOI
[`10.1214/11-AIHP462`](https://doi.org/10.1214/11-AIHP462).  There is no preprint or numerical
premise.

### Lyapunov energy duality, positivity, and $K=0$

On $H=\operatorname{Ran}A$, the restriction $A|_H$ is positive definite and, for symmetric $M$,

$$
\langle M,\mathscr L_AM\rangle
=\operatorname{Tr}(MAM)
=\|A^{1/2}M\|_{\mathrm{HS}}^2.
$$

Thus $\mathscr L_A$ is self-adjoint and positive definite on $\operatorname{Sym}(H)$.  Weighted
Cauchy--Schwarz gives the exact finite-dimensional duality formula

$$
\sup_{M\ne0}\frac{\langle K,M\rangle^2}{\langle M,LM\rangle}
=\langle K,L^{-1}K\rangle,
$$

with equality at $M=L^{-1}K$ for $K\ne0$.  Setting
$d_t=\langle K_t,\mathscr L_{A_t}^{-1}K_t\rangle>0$ in the nonzero case produces

$$
s_td_t^2\le\frac4t d_t,
$$

and division gives the first claimed inequality.  Multiplication by
$\|K_t\|_{\mathrm{HS}}^2/d_t$ gives the source-scale inequality with the same factor $4$.
When $K_t=0$, the two assertions are respectively $0\le4/t$ and $0\le0$ under the separate
zero convention.  If $H_t=\{0\}$, support already forces $K_t=0$, so no empty-space supremum or
undefined quotient occurs.

### Direct sums and the auxiliary calibrations

For $A,B\succeq0$, work on $H_A\oplus H_B$.  The $AA$, mixed, and $BB$ symmetric block spaces
are invariant under $\mathscr L_{A\oplus B}$.  Since the input is $K\oplus0$, its support inverse
has $AA$ block $\mathscr L_A^{-1}K$ and zero mixed and $BB$ blocks.  Hence both the
Hilbert--Schmidt numerator and Lyapunov denominator are unchanged.  This remains true for
singular spectator blocks, while $K=0$ is covered by the totalized convention.

The auxiliary eigenbasis formula was also checked.  Ordered-pair summation gives

$$
\langle K,\mathscr L_A^{-1}K\rangle
=\sum_{i,j}\frac{2|K_{ij}|^2}{\lambda_i+\lambda_j}
=\sum_{i,j}\frac{|K_{ij}|^2}{(\lambda_i+\lambda_j)/2}.
$$

For $i<j$, the two ordered entries contribute $2|K_{ij}|^2$ to the Hilbert--Schmidt numerator
and $4|K_{ij}|^2/(\lambda_i+\lambda_j)$ to the denominator.  The printed harmonic-mean quotient
therefore has the correct off-diagonal multiplicity.

For the certified anisotropic two-tail pair,

$$
A_\Lambda=\operatorname{diag}(\Lambda,1,\ldots,1),
\qquad
K_\Lambda=8a\varphi(a)\Lambda e_1e_1^T.
$$

Since $\mathscr L_{A_\Lambda}(e_1e_1^T)=\Lambda e_1e_1^T$, the inverse sends
$K_\Lambda$ to $K_\Lambda/\Lambda$, and the auxiliary quotient is exactly
$\lambda_{\rm cut}(A_\Lambda,K_\Lambda)=\Lambda$.  It is not a dimension-free scale.

### Hypotheses, dependency closure, and fences

The proof uses finite dimension; fixed $t>0$; a finite-time log-concave localization posterior
on its affine covariance support; a fixed measurable cut with $p_t,q_t>0$; the two-color
identity; Brascamp--Lieb with curvature $t$; and elementary Hilbert-space duality.  The
structural direct-sum statement uses $A,B\succeq0$ and support of $K$ on
$\operatorname{Ran}A$.  Initial isotropy is unused sharpening slack.  No smooth-cut,
finite-perimeter, compact-support, full-rank, occupation, or numerical hypothesis is used.

The dossier header and synchronized ledger both declare
`[lem:pathwise-BL, prop:two-tail]`.  `lem:pathwise-BL` is proved and agent-certified, with
dependency `prop:stein-rep`; `prop:two-tail` is proved and agent-certified, with the same
dependency.  All three nodes and both upstream dossiers are covered by the passing front matter
and mathematical checks in `research/reviews/2026-08-25-kls-core-r2-audit.md`.  The
`prop:two-tail` edge accounts for the auxiliary calibration rather than the formal lemma proof;
it is conservative closed dependency accounting, not a conditional premise.  No open,
conditional, refuted, imported-unreviewed, or citation-debt node remains in the closure.

The target has no formal `bounded_by` edge.  It nevertheless respects the relevant two-tail and
projection fences: the bound keeps the full cut-oriented tensor, the two-tail calibration grows
as $\Lambda$, and direct-sum invariance removes only a block on which the cut tensor is exactly
zero.  It claims no operator-to-trace upgrade or high-rank occupation estimate.  Both dossier
lines 196--211 and manuscript lines 167--172 explicitly retain the singular $t^{-1}$ factor.
There is no assertion at $t=0$, no limit as $t\downarrow0$, and no initial-time integrability,
time-occupation, or expectation claim.

### Standalone build and archive validation

From `solutions/`, the forced command

```text
latexmk -g -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=../build lem-lyapunov-stein-duality.tex
```

returned exit code zero.  The resulting three-page PDF was inspected page by page.  It has no
TeX error, overfull box, underfull box, clipped display, or malformed equation.  The unresolved
parent-manuscript labels are the expected standalone-subfile references allowed by
`solutions/README.md`; the Brascamp--Lieb citation renders.  A final
`python3 research/check_ledger.py` run reported 2 ledgers, 190 nodes, 662 labels, and 0 errors.
The dossier hash remained the pinned value after the build.

## Corrections

None.  The formal-scope, dependency, and ledger-totalization defects recorded by the prior audit
are fully repaired in the reviewed state.

## Exclusions

This review certifies only `lem:lyapunov-stein-duality` and the dossier named in the front
matter.  It does not recertify the upstream localization or two-tail dossiers, promote the
auxiliary harmonic-mean prose to a separate ledger theorem, establish a bound at $t=0$, prove
initial-layer integrability or covariance occupation, prove an operator-to-trace upgrade, or
establish any implication in the trace-upgrade cluster.  No dossier, manuscript, ledger,
bibliography, exploration, knowledge file, or prior review was edited by this reviewer.
