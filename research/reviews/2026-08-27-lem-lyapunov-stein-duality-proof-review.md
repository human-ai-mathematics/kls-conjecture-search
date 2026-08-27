---
type: audit
date: "2026-08-27"
---

# Cut-oriented Lyapunov--Stein duality — cold proof audit

This is a cold review of `solutions/lem-lyapunov-stein-duality.tex`, whose pinned and reviewed
SHA-256 is `a66f3d93d9af8d38eba1c8ced50adcdb6a744d341af34275ab131f7a15bd69af`.
The proof was reconstructed from the dossier, the current manuscript and ledger, the certified
dependency dossiers and review, the obstruction registry, and the published Brascamp--Lieb
source. The prover's exploration narrative was not used as mathematical evidence. The author
`/root/prove_lyapunov_stein_duality_w2` and reviewer
`/root/review_lyapunov_stein_duality_w2` are distinct, and the exploration record names only the
former as author.

This report does not certify the current dossier. The analytic proof and every requested
constant check out, but the formal dossier theorem has a wider scope than the labeled manuscript
lemma and ledger statement, and the ledger omits a same-ledger dependency used by that wider
claim. Repository constraint 4 makes those semantic defects certification-blocking even though
the extra mathematics is correct.

## Findings

### Statement agreement and dependency blockers

The core statement agrees across all three proof planes:

- `solutions/lem-lyapunov-stein-duality.tex:51`--`74` states, on the covariance support,
  $$
  s_t\langle K_t,\mathscr L_{A_t}^{-1}K_t\rangle\le \frac4t,
  \qquad
  s_t\|K_t\|_{\mathrm{HS}}^2
  \le \frac{4\lambda_{\rm cut}(A_t,K_t)}t,
  $$
  with the support inverse, the separate value $\lambda_{\rm cut}(A,0)=0$, and invariance under
  $A\oplus B,K\oplus0$.
- The labeled manuscript lemma at `modules/kls/21-carleson.tex:141`--`165` states those same
  claims with the same factor $4$, the same Lyapunov normalization
  $\mathscr L_A(M)=(AM+MA)/2$, and the same direct-sum assertion.
- The ledger node at `research/kls/ledger.yaml:190`--`196` records the same core inequality,
  source-scale consequence, quotient, and direct-sum invariance.

The formal scopes nevertheless differ. The dossier keeps its lemma environment open through
lines 75--88 and therefore makes two additional assertions part of the node theorem: the exact
eigenbasis weighted-harmonic-mean formula and
$\lambda_{\rm cut}(A_\Lambda,K_\Lambda)=\Lambda$. The manuscript lemma ends at line 165; it
places those observations only in adjacent explanatory prose at lines 167--172. The ledger
statement does not contain either assertion. A correct strengthening is still a different formal
statement under the repository's three-way statement-agreement gate.

There is a corresponding graph defect. The proof invokes the certified
`prop:two-tail` and its formula for $K_\Lambda$ at dossier lines 170--185, while the ledger lists
only

```yaml
depends_on: [lem:pathwise-BL]
```

at line 196. `research/ledger-schema.md` defines `depends_on` as the same-ledger claims actually
used in the proof, so `prop:two-tail` must be present if the calibration remains in certified
scope. Adding that edge would not make the result conditional:

$$
\texttt{lem:pathwise-BL}\longrightarrow\texttt{prop:stein-rep},
\qquad
\texttt{prop:two-tail}\longrightarrow\texttt{prop:stein-rep},
$$

and all three upstream nodes are proved and agent-certified by the passing report
`research/reviews/2026-08-25-kls-core-r2-audit.md`.

Finally, the ledger's abbreviated quotient does not explicitly say that
$\mathscr L_A^{-1}$ is taken on the covariance support, that the quotient is for $K\ne0$, or
that $\lambda_{\rm cut}(A,0)=0$. The dossier and manuscript agree on those conventions, but the
ledger wording should be made mathematically total before certification metadata is applied.

### Covariance support and Moore--Penrose convention

Let $Y=X-a_t$ and $H_t=\operatorname{Ran}(A_t)$. For every
$v\in\ker A_t$,

$$
0=v^TA_tv=\mathbb E_{\mu_t}(v\cdot Y)^2.
$$

Applying this to a finite orthonormal basis of $\ker A_t$ gives $Y\in H_t$ almost surely.
Conditioning preserves that affine support: $m_t^E-a_t,m_t^F-a_t\in H_t$,
$\delta_t\in H_t$, and the centered conditional vectors defining
$\Sigma_t^E,\Sigma_t^F$ lie in $H_t$. Hence
$G_t=P_tG_tP_t$, $\delta_t\delta_t^T=P_t\delta_t\delta_t^TP_t$, and therefore
$K_t=P_tK_tP_t$. The wording that the conditional means “live on” the support is correctly read
as the translated conditional means lying in $H_t$.

In an orthonormal eigenbasis of a positive-semidefinite $A$, the symmetric modes $E_{ii}$ and
$(E_{ij}+E_{ji})/\sqrt2$ have Lyapunov eigenvalues $\lambda_i$ and
$(\lambda_i+\lambda_j)/2$, respectively. Thus the ambient Moore--Penrose inverse has exactly the
entrywise multiplier

$$
(\mathscr L_A^\dagger C)_{ij}
=\frac{2C_{ij}}{\lambda_i+\lambda_j}
$$

when the denominator is positive and is zero when both eigenvalues vanish. For a supported
$K=PKP$, all entries involving a null direction vanish, so this is precisely the inverse on
$\operatorname{Sym}(\operatorname{Ran}A)$ followed by ambient zero extension. No full-rank
assumption is hidden.

### Exact anisotropic Brascamp--Lieb inequality

For $M\in\operatorname{Sym}(H_t)$, extended by zero off $H_t$, define

$$
f_M(x)=(x-a_t)^TM(x-a_t)-\operatorname{Tr}(MA_t),
\qquad
g=\frac{\mathbf1_E-p_t}{\sqrt{s_t}}.
$$

The assumptions $p_t,q_t>0$ make $g$ well defined, and
$\mathbb Eg=\mathbb Ef_M=0$, $\mathbb Eg^2=1$. Conditional covariance decomposition gives

$$
\mathbb E[f_M\mid E]
=q_t\langle G_t+(q_t-p_t)\delta_t\delta_t^T,M\rangle
=q_t\langle K_t,M\rangle.
$$

Consequently

$$
\mathbb E_{\mu_t}[gf_M]
=\frac{p_tq_t}{\sqrt{s_t}}\langle K_t,M\rangle
=\sqrt{s_t}\langle K_t,M\rangle,
$$

with the printed sign and normalization.

On the affine support, the posterior potential is the initial convex potential plus
$t|x|^2/2-c_t\cdot x$ and is therefore $t$-strongly convex. Brascamp--Lieb and
Cauchy--Schwarz give

$$
s_t\langle K_t,M\rangle^2
\le \operatorname{Var}_{\mu_t}(f_M)
\le \frac1t\mathbb E_{\mu_t}|\nabla_{H_t}f_M|^2.
$$

Here $\nabla_{H_t}f_M=2M(X-a_t)$, so

$$
\mathbb E|\nabla_{H_t}f_M|^2
=4\operatorname{Tr}(MA_tM).
$$

This proves the exact inequality

$$
s_t\langle K_t,M\rangle^2
\le \frac4t\operatorname{Tr}(MA_tM)
$$

without operator-norm scalarization and with no missing factor. The Gaussian posterior factor,
after completing the square against $c_t\cdot x$, gives every polynomial moment at fixed
$t>0$. Thus $f_M$ and its gradient are in the closed Brascamp--Lieb form domain; smooth value and
spatial truncation followed by form closure justifies the unbounded quadratic test. The usual
convex-potential approximation on the affine support supplies the same inequality for nonsmooth
or lower-dimensional log-concave data.

### Lyapunov energy duality, positivity, and the zero case

On $H=\operatorname{Ran}A$, $A|_H$ is positive definite. For symmetric $M$,

$$
\begin{aligned}
\langle M,\mathscr L_AM\rangle
&=\frac12\operatorname{Tr}(MAM+M^2A)\\
&=\operatorname{Tr}(MAM)
=\|A^{1/2}M\|_{\mathrm{HS}}^2.
\end{aligned}
$$

Hence $\mathscr L_A$ is self-adjoint and positive definite on $\operatorname{Sym}(H)$. For a
positive-definite self-adjoint operator $L$, weighted Cauchy--Schwarz gives

$$
\sup_{M\ne0}\frac{\langle K,M\rangle^2}{\langle M,LM\rangle}
=\langle K,L^{-1}K\rangle,
$$

with equality at $M=L^{-1}K$ for $K\ne0$. Put
$d_t=\langle K_t,\mathscr L_{A_t}^{-1}K_t\rangle$. If $K_t\ne0$, then $d_t>0$, and substitution
in the checked anisotropic inequality yields

$$
s_td_t^2\le\frac4t d_t,
\qquad
s_td_t\le\frac4t.
$$

Multiplication by $\|K_t\|_{\mathrm{HS}}^2/d_t$ gives the exact source-scale constant
$4\lambda_{\rm cut}/t$. If $K_t=0$, the dual inequality is $0\le4/t$ and the source-scale
inequality is $0\le0$ under the separate convention $\lambda_{\rm cut}(A_t,0)=0$. If the
covariance support itself has dimension zero, support forces $K_t=0$, so the same separate case
applies without taking a supremum over an empty punctured space.

### Eigenbasis multiplicities, singular direct sums, and two-tail calibration

For a supported symmetric $K$, the ordered-pair sums give

$$
\langle K,\mathscr L_A^{-1}K\rangle
=\sum_{i,j}\frac{2|K_{ij}|^2}{\lambda_i+\lambda_j}
=\sum_{i,j}\frac{|K_{ij}|^2}{(\lambda_i+\lambda_j)/2}.
$$

For $i<j$, the two ordered entries contribute $2|K_{ij}|^2$ to the Hilbert--Schmidt numerator
and $4|K_{ij}|^2/(\lambda_i+\lambda_j)$ to the denominator. The diagonal contribution is
$|K_{ii}|^2/\lambda_i$. Thus the displayed quotient is exactly the
$|K_{ij}|^2$-weighted harmonic mean; no off-diagonal factor two is lost.

For $A,B\succeq0$, work on $H_A\oplus H_B$. The $AA$, mixed, and $BB$ symmetric block spaces are
invariant under $\mathscr L_{A\oplus B}$. Applied to $K\oplus0$, the support inverse has $AA$
block $\mathscr L_A^{-1}K$ and zero mixed and $BB$ blocks. Ambient null directions remain zero
under the Moore--Penrose convention. Hence both the Hilbert--Schmidt numerator and Lyapunov
denominator are unchanged even when either covariance is singular. If $A=0$, support forces
$K=0$, which is already covered by the separate convention.

The certified two-tail proposition gives

$$
A_\Lambda=\operatorname{diag}(\Lambda,1,\ldots,1),
\qquad
K_\Lambda=8a\varphi(a)\Lambda e_1e_1^T.
$$

Since $\mathscr L_{A_\Lambda}(e_1e_1^T)=\Lambda e_1e_1^T$,
$\mathscr L_{A_\Lambda}^{-1}K_\Lambda=K_\Lambda/\Lambda$ and therefore

$$
\lambda_{\rm cut}(A_\Lambda,K_\Lambda)
=\frac{\|K_\Lambda\|_{\mathrm{HS}}^2}
       {\|K_\Lambda\|_{\mathrm{HS}}^2/\Lambda}
=\Lambda.
$$

The calibration is exact, analytic, and independent of the approximate decimal constants printed
in the two-tail manuscript proposition.

### Hypothesis accounting, citations, and logical closure

The proof actually uses: finite dimension; a fixed $t>0$; a finite-time log-concave posterior on
its affine covariance support; a fixed measurable cut with $p_t,q_t>0$; the certified two-color
identity; Brascamp--Lieb with strong-convexity constant $t$; and elementary finite-dimensional
Hilbert-space duality. The structural claims separately use $A,B\succeq0$, support of $K$ on
$\operatorname{Ran}A$, and $\Lambda\ge1$ from `prop:two-tail`.

No used hypothesis is unstated. Initial isotropy is part of the repository localization context
but is not used by this fixed-time argument, so it is harmless sharpening slack. No smoothness or
finite-perimeter property of the cut, full ambient rank, compact support, numerical input, or
occupation hypothesis is used.

The current declared dependency `lem:pathwise-BL` is proved, agent-certified, and covered by the
passing front matter of `research/reviews/2026-08-25-kls-core-r2-audit.md`; its dossier contains
the stronger anisotropic quadratic-form inequality consumed here. Its dependency
`prop:stein-rep` is likewise proved and covered by that same report. The extra formal calibration
uses `prop:two-tail`, also proved and covered by the same report, with transitive dependency
`prop:stein-rep`. Thus the mathematical closure contains no open, conditional, refuted, or
`preprint-unreviewed` premise; the defect is that the current ledger fails to declare all of that
closure.

The only external theorem used directly is the inverse-Hessian variance inequality of Brascamp
and Lieb, Theorem 4.1, a published 1976 *Journal of Functional Analysis* result, DOI
[`10.1016/0022-1236(76)90004-5`](https://doi.org/10.1016/0022-1236(76)90004-5). The publisher's
full text was unavailable, so the exact constant-one formula was additionally checked in the
published primary paper of Carlen--Cordero-Erausquin--Lieb, *Ann. Inst. H. Poincar\'e Probab.
Statist.* 49 (2013), DOI
[`10.1214/11-AIHP462`](https://doi.org/10.1214/11-AIHP462): equation (1.3) states the
inverse-Hessian variance inequality, Theorem 1.1 proves a stronger covariance version, and the
appendix identifies the original Brascamp--Lieb dimensional-induction theorem. No preprint or
numerical evidence enters this proof.

### Fences and initial-time exclusion

The ledger node has no formal `bounded_by` edge. The relevant obstruction is nevertheless
respected. `obs:two-tail` rules out a dimension-free absolute slice scale; the checked result
instead gives $\lambda_{\rm cut}=\Lambda$ on that anisotropic family. The proof retains the full
cut-oriented tensor and therefore does not infer tensor control from radial or projection-only
data. Direct-sum invariance removes only blocks on which the cut tensor is exactly zero.

The theorem is quantified only for fixed $t>0$. Both the dossier at lines 188--202 and the
manuscript at lines 167--172 explicitly retain the singular $t^{-1}$ factor and disclaim an
initial-time occupation estimate. No limit $t\downarrow0$, time integration, expectation,
operator-to-trace upgrade, high-rank occupation estimate, or integrability assertion is made.

### Standalone build and archive check

From `solutions/`, the forced build

```text
latexmk -g -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=../build lem-lyapunov-stein-duality.tex
```

completed successfully and produced a visually inspected three-page PDF. There is no TeX error,
overfull box, underfull box, or malformed equation. The six unresolved cross-manuscript references
are the expected standalone-subfile behavior allowed by `solutions/README.md`; the
Brascamp--Lieb citation renders. An earlier pre-report run of
`python3 research/check_ledger.py` reported 2 ledgers, 189 nodes, 660 labels, and 0 structural
errors. A final rerun after concurrent central-file changes reported one unrelated error:
`ass:weighted-package.refuted_by` was not also present in that node's `depends_on`. This reviewer
did not touch that ledger. In either state, the structural checker does not detect the formal
statement and dependency defects above, as emphasized by repository constraint 4.

## Corrections required before a fresh review

1. Synchronize the formal theorem scope. The smallest dossier-only repair is to end the formal
   lemma after the direct-sum assertion currently at
   `solutions/lem-lyapunov-stein-duality.tex:71`--`74`, matching the manuscript lemma and ledger,
   and move the harmonic-mean and two-tail material at lines 75--88 into an explicitly auxiliary
   post-proof remark. Correspondingly split the derivations at lines 149--158 and 170--185 out of
   the main proof. Alternatively, an orchestrator-owned manuscript/ledger synchronization may
   enlarge the formal node everywhere, but a prover must not make those central edits.
2. If the two-tail calibration remains anywhere in the certified dossier, record
   `prop:two-tail` in the dossier dependency header and hand the same missing edge to the
   orchestrator. Its proved status means this repair does not introduce a conditional premise.
3. Hand the orchestrator the ledger wording debt: the node's statement must make the covariance-
   support inverse, the $K\ne0$ domain of the quotient, and
   $\lambda_{\rm cut}(A,0)=0$ explicit. If the formal scope is enlarged instead of narrowed, the
   harmonic-mean and exact two-tail clauses must also appear in the ledger and labeled manuscript
   statement.
4. Preserve the checked analytic proof, constants, singular-block convention, and explicit
   initial-time exclusion. Recompile, record the repaired hash in a new append-only exploration,
   and request a new cold review. This audit remains immutable and cannot be upgraded in place.

## Exclusions

This audit certifies no ledger node and proposes no `solution`, `checked_by`, `review`, status, or
provenance-header delta. It does not recertify the upstream localization or two-tail dossiers,
prove any initial-time integrability or expected occupation result, prove an operator-to-trace
upgrade, or establish any implication in the trace-upgrade cluster. No dossier, manuscript,
ledger, bibliography, exploration, knowledge file, or prior review was edited by this reviewer.
