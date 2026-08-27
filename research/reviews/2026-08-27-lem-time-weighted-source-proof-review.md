---
type: proof-review
date: "2026-08-27"
verdict: pass
authors:
  - /root/prove_time_weighted_par_05
reviewer: /root/review_time_weighted_cold_07
nodes:
  - lem:time-weighted-source
solutions:
  - solutions/lem-time-weighted-source.tex
---

# Scale-weighted all-cut source budget — independent proof review

This is a cold review of `solutions/lem-time-weighted-source.tex`, whose reviewed SHA-256 is
`8ff6151b44cf646ad2e8a4604cbc4e065a8dc4fce12289440b2c3af2c84e1289`. The proof was
reconstructed from the dossier, ledger, manuscript, certified dependencies, route controls,
obstruction registry, and primary literature; the prover's narrative was not used as evidence.
The author and reviewer identities are distinct.

## Findings

### Statement agreement and logical closure

The dossier theorem, the ledger statement for `lem:time-weighted-source`, and the manuscript
lemma at `\label{lem:time-weighted-source}` agree mathematically. For every isotropic
log-concave initial law on $\mathbb R^n$, every fixed measurable cut $E$ with
$0<\mu(E)<1$, and every $T>0$, all three assert

$$
\mathbb E\int_0^T t^2(S_t+r_t^2)\,dt
\le T^2\mathbb E r_T\le T.
$$

The manuscript and ledger record the consequence for a balanced stopped window and explicitly
retain the quadratic weight at the initial endpoint. The dossier states the formally stronger
consequence for every stopping time and every deterministic subinterval. This does not change
the theorem's mathematical scope: it follows immediately from the common full-interval estimate
because $S_t+r_t^2\ge0$, and in particular contains the recorded balanced-window statement.
No balance hypothesis is imposed on the cut in the main estimate.

The ledger's sole dependency is `thm:scalar-riccati`. That node is `proved`, points to
`solutions/kls-localization-riccati-core.tex`, is `checked_by: agent`, and has the active passing
review `research/reviews/2026-08-25-kls-core-r2-audit.md`. Its only dependency,
`lem:matrix-riccati`, has the same proved status, dossier, and passing review, and has no further
dependency. Both nodes and the active dossier occur in that review's certifying front matter,
with distinct author and reviewer. The present proof consumes only the scalar identity
$dr_t=dM_t+(S_t-D_t)dt$, which agrees exactly in the dependency dossier, ledger, and manuscript;
the adjacent coercivity assertion $D_t\ge r_t^2$ is not used here. No dependency is open,
conditional, imported from an unreviewed preprint, or supported by numerical evidence. The new
node is therefore unconditional and may become `proved` once the certification pointers are
applied.

### Hypothesis accounting

The proof uses the hypotheses as follows.

1. The cut is fixed and measurable, so the certified two-color Riccati identity applies to its
   indicator without an adaptive-cut correction. The conditions $0<\mu(E)<1$ and strict
   positivity of the finite-time localization likelihood keep $p_t,q_t>0$, so all conditional
   moments are defined.
2. Log-concavity makes each finite-time posterior $t$-uniformly log-concave and supplies the
   Brascamp--Lieb covariance cap for $t>0$.
3. The finite horizon $T>0$ permits the proof to work first on $[\varepsilon,T]$ and then remove
   the singular endpoint.
4. The certified stochastic-localization/Riccati setup supplies a continuous local martingale and
   locally finite drift terms.

No used hypothesis is unstated. Isotropy is invoked in the dossier only for the redundant
observation $B_0\preceq A_0=I$ and $r_0\le1$. The displayed estimate itself uses instead
$\varepsilon^2\mathbb E r_\varepsilon\le\varepsilon$ and never spends the time-zero bound.
Thus isotropy is harmless route-context slack and a possible sharpening opportunity, not a
defect. No balance, smoothness, compact-support, or finite-perimeter hypothesis remains.

### Covariance decomposition, rank one, and the posterior cap

Writing $a_t=p_tm_t^E+q_tm_t^{E^c}$ gives
$m_t^E-a_t=q_t\delta_t$ and $m_t^{E^c}-a_t=-p_t\delta_t$. Hence the between-class covariance is

$$
p_tq_t^2\delta_t\delta_t^T+q_tp_t^2\delta_t\delta_t^T
=p_tq_t\delta_t\delta_t^T=B_t,
$$

so

$$
A_t=p_t\Sigma_t^E+q_t\Sigma_t^{E^c}+B_t,
\qquad 0\preceq B_t\preceq A_t.
$$

Since $B_t=s_t\delta_t\delta_t^T$, it has rank at most one and its only possible nonzero
eigenvalue is
$s_t|\delta_t|^2=\operatorname{Tr}B_t=r_t$. For $t>0$, the posterior potential is the original
convex potential plus $t|x|^2/2-c_t\cdot x$. Brascamp--Lieb applied to linear tests therefore gives

$$
A_t\preceq t^{-1}I,
\qquad 0\le r_t=\lambda_{\max}(B_t)\le\lambda_{\max}(A_t)\le t^{-1}.
$$

All constants and Loewner directions are correct.

Finally, $\operatorname{Tr}(A_tB_t)=s_t\delta_t^TA_t\delta_t$. Because
$t^{-1}I-A_t\succeq0$ and $B_t\succeq0$,

$$
\operatorname{Tr}(A_tB_t)\le t^{-1}\operatorname{Tr}B_t=\frac{r_t}{t},
$$

and consequently

$$
D_t=2\operatorname{Tr}(A_tB_t)-r_t^2
\le \frac{2r_t}{t}-r_t^2.
$$

No commutativity of $A_t$ and $B_t$ is being assumed; positivity of the trace of the product of
two positive semidefinite matrices is enough.

### Weighted It\^o inequality

The certified scalar Riccati identity gives
$dr_t=dM_t+(S_t-D_t)dt$. The deterministic product rule has no quadratic-covariation term, so

$$
d(t^2r_t)=t^2dM_t+(2tr_t+t^2S_t-t^2D_t)dt.
$$

Substitution of the checked upper bound on $D_t$ cancels the two $tr_t$ terms exactly and yields

$$
d(t^2r_t)\ge t^2dM_t+t^2(S_t+r_t^2)dt,
\qquad t>0.
$$

The sign is essential and correct: this argument uses an upper bound on the damping, not the
usual coercive lower bound.

### Bounded localization and the two limiting passages

Fix $0<\varepsilon<T$ and put
$L_t=\int_\varepsilon^t u^2\,dM_u$. A standard increasing localization sequence
$\rho_k\ge\varepsilon$, $\rho_k\uparrow\infty$, makes the stopped increments of $L$ true
martingales on $[\varepsilon,T]$. With $\theta_k=T\wedge\rho_k$, integration and expectation give

$$
\mathbb E\int_\varepsilon^{\theta_k}t^2(S_t+r_t^2)\,dt
\le \mathbb E[\theta_k^2r_{\theta_k}]-\varepsilon^2\mathbb E r_\varepsilon.
$$

The pathwise cap at the random time $\theta_k\ge\varepsilon$ is

$$
0\le\theta_k^2r_{\theta_k}\le\theta_k\le T.
$$

Since $r$ is continuous and $\theta_k\uparrow T$, the terminal variables converge to $T^2r_T$
and are dominated by $T$. The occupation integrands are nonnegative and their stopped domains
increase to $[\varepsilon,T]$. Dominated convergence for the terminal term and monotone
convergence for the occupation term therefore give

$$
\mathbb E\int_\varepsilon^Tt^2(S_t+r_t^2)\,dt
\le T^2\mathbb E r_T-\varepsilon^2\mathbb E r_\varepsilon.
$$

There is no optional-stopping claim at an infinite horizon and no unproved uniform-integrability
step.

### Initial endpoint, terminal bound, and stopped consequence

For every $\varepsilon>0$, the same posterior cap gives

$$
0\le\varepsilon^2\mathbb E r_\varepsilon\le\varepsilon.
$$

As $\varepsilon\downarrow0$, the nonnegative occupation integrals increase to the integral on
$[0,T]$, while the endpoint term tends to zero. This proves the first inequality without using a
Brascamp--Lieb assertion at $t=0$. At the terminal time,
$0\le T^2r_T\le T$ pathwise, which gives the second inequality. For any nonnegative stopping
time $\tau$,

$$
\int_0^{T\wedge\tau}t^2(S_t+r_t^2)\,dt
\le\int_0^Tt^2(S_t+r_t^2)\,dt
$$

pathwise. Thus the stopped consequence uses positivity only; it does not use optional stopping,
balance, or a terminal variable evaluated at $T\wedge\tau$.

### General-law passage and citation debt

The argument is already valid for an arbitrary isotropic log-concave law and arbitrary measurable
nontrivial cut. The consumed scalar Riccati identity is certified in that generality. Every new
algebraic inequality above is pathwise, and Brascamp--Lieb for the $t$-strongly log-concave
posterior holds by form closure for $t>0$. Thus the dossier's explicit regularization paragraph is
a redundant stable route, not an additional premise.

That route is nevertheless sound under the repository convention. On each strip
$[\varepsilon,T]$, truncation/smoothing and isotropization give convergence, after a subsequence,
of posterior masses and first and second cut moments, hence of $r_t$ and $S_t$ for almost every
$(\omega,t)$. Fatou applies to the nonnegative occupation term. The uniform terminal bound
$0\le T^2r_T\le T$ gives uniform integrability, so convergence of the terminal cut moments passes
their expectations. The constants are approximation-independent, and the already checked
$\varepsilon\downarrow0$ step removes the endpoint. No regularity residue survives.

The external source input has no preprint debt:

- Brascamp and Lieb's Theorem 4.1 is a published, peer-reviewed 1976 *Journal of Functional
  Analysis* result (DOI `10.1016/0022-1236(76)90004-5`). The publisher's full text was not
  accessible, so the exact inequality was additionally checked in the published primary paper of
  Carlen--Cordero-Erausquin--Lieb, *Ann. Inst. H. Poincar\'e Probab. Statist.* 49 (2013),
  DOI `10.1214/11-AIHP462`: equation (1.3) states the inverse-Hessian variance inequality, its
  Theorem 1.1 proves a stronger covariance form, and its Appendix explicitly reconstructs the
  induction in Brascamp--Lieb Theorem 4.1. For $\nabla^2V_t\succeq tI$, a linear test gives exactly
  $A_t\preceq t^{-1}I$ with constant one.
- The posterior density, density martingale, and covariance SDE underlying the certified Riccati
  dependency were checked in the author manuscript of the published Lee--Vempala paper
  (*Annals of Mathematics* 199 (2024), DOI `10.4007/annals.2024.199.3.2`): Definition 26 and
  Lemmas 27--28 give the same Gaussian tilt, signs, and $-A_t^2dt$ covariance drift. Eldan's
  foundational stochastic-localization paper is likewise published. These inputs already sit
  inside the active certified dependency chain.

No numerical run or empirical agreement is used as evidence.

### Fences and excluded route claims

The ledger gives `lem:time-weighted-source` no formal `bounded_by` edge. Every relevant
Eldan-route obstruction was nevertheless checked.

- `obs:two-tail` forbids an absolute-scale slice-wise source estimate. This proof is dynamic,
  expected, and retains $t^2$; it allows the source to be of order $t^{-2}$ and makes no
  unweighted assertion at the initial endpoint.
- `obs:proj-ceiling` is not crossed because no radial or projection-only estimate is promoted to
  tensor trace control.
- `obs:crude-insufficient` and `obs:relative-ceiling` are not consumed: the proof never invokes
  $\Xi_T$, never treats the crude logarithmic covariance integral as a closing input, and never
  asserts a universal relative-scale covariance bound.
- `obs:circularity` is untouched because no localized isoperimetric profile or moving
  near-minimizer is used.
- `obs:rank-one-refuted` is untouched because the proof neither proposes nor rules out a product
  single-coordinate counterexample; its all-cut weighted budget is compatible with that
  obstruction.

The dossier proves no unweighted source estimate, all-cut absorptive Carleson estimate,
operator-to-trace upgrade `q:upgrade`, weighted Stein theorem `q:stein-weighted`, adapted product
alignment result `q:alignment`, equivalence among the trace-upgrade cluster, balanced survival,
Cheeger bound, or KLS conclusion.

### Standalone build and archive validation

From `solutions/`,

```text
latexmk -g -pdf -outdir=../build lem-time-weighted-source.tex
```

completed successfully and produced a two-page PDF. The only TeX warnings are the expected
standalone unresolved cross-manuscript references to `lem:time-weighted-source` and
`thm:scalar-riccati`. Before this report was added, `python3 research/check_ledger.py` reported
0 errors.

## Corrections

None.

## Exclusions

This review certifies only `lem:time-weighted-source` in the dossier and immutable scope named in
the front matter. It inspected the active certificates needed for dependency closure but does not
recertify every theorem in `solutions/kls-localization-riccati-core.tex`. It certifies no unweighted
occupation estimate, no Carleson or high-rank trace upgrade, no Stein/alignment bridge, no KLS
implication, and no numerical artifact. Updating the dossier header, ledger, manuscript, route
control, or knowledge files is outside this reviewer's write surface.
