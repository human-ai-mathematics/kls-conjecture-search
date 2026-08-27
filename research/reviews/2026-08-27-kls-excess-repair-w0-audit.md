---
type: audit
date: "2026-08-27"
---

# Repaired KLS perimeter/excess dossier — cold W0 audit

This is a fresh review of `solutions/kls-excess-audit.tex`, SHA-256
`afaed5aa1c54602fed15764a7c7e7692f74f7aafae8b003b1adc70cb1c3d86b6`.  The original author is
`/root/kls_bootstrap_author`, the repair author is `/root/repair_excess_dossier`, and the reviewer
is `/root/review_excess_w0`.  The historical 2026-08-25 report was not used as mathematical
evidence.  The reviewed scope was `prop:intro-audit`, `prop:trivial-excess`,
`lem:perimeter-martingale`, `lem:excess-identity`, and `lem:inf-martingales`.

This report does not certify the repaired source.  The central replacement

$$
\mathbb E[J_t\mid\mathcal F_s]
\leq \mathbb E[P_t(S)\mid\mathcal F_s]
\leq P_s(S)
$$

is correct for every fixed competitor, and it proves the countable-family conclusion, but three
regularity/selection steps and two statement/dependency synchronizations remain unresolved.

## Findings

### Statement agreement

| Node | Dossier, ledger, and manuscript comparison |
|---|---|
| `prop:trivial-excess` | The dossier and manuscript agree on the bound for isotropic log-concave data, mass one half, arbitrary $T$, and arbitrary stopping time.  The ledger summary at `research/kls/ledger.yaml:351` states only the formula and omits the hypotheses that make the constant $1$ valid.  Its graph also omits a dependency actually used by the proof. |
| `lem:excess-identity` | All three statements restrict the exact expectation identity to compact support.  The dossier uses true-martingale equality only in this class and explicitly records that the noncompact argument supplies only an inequality. |
| `prop:intro-audit` | The three assertions agree mathematically.  Item 2 is an implication whose antecedent is the full unweighted stable Stein-trace estimate on one fixed tight window with the stated absorption margin; it is not an assertion that this estimate has been proved.  Its ledger graph omits the balanced-profile lemma explicitly used in the contradiction. |
| `lem:perimeter-martingale` | The dossier and ledger include the noncompact process inequality $\mathbb E[P_t(E)\mid\mathcal F_s]\leq P_s(E)$.  The labeled manuscript statement at `modules/kls/24-excess-propagation.tex:58`--`67` states only the compact-support martingale/SDE result.  The separate convention at `modules/kls/10-notation.tex:180`--`188` displays only the $s=0$ expectation inequality.  The labeled statement therefore does not yet contain the full ledger clause. |
| `lem:inf-martingales` | The dossier correctly requires a nonempty family; the labeled manuscript statement at `modules/kls/24-excess-propagation.tex:93`--`107` says “any” family and hence includes the empty family, for which the infimum is not integrable.  The ledger summary calls all fixed-cut processes martingales rather than allowing the noncompact supermartingale case.  The manuscript proof at lines 109--114 also still invokes noncompact equality.  Moreover, the uncountable-family clause is not proved under measurability alone, as detailed below. |

The five ledger nodes declare no `bounded_by` edge.  That metadata is accurate, but it does not
remove the statement-agreement defects above.

### Perimeter martingale and supermartingale

The following parts of `solutions/kls-excess-audit.tex:84`--`136` were checked.

- In the compact smooth class, $P_t(E)=\int F_t\,d\sigma_0$ and
  $d\sigma_t=F_t\,d\sigma_0$ have the correct weighted-surface form.
- Compact support gives $|x-a_t|\leq D$.  For fixed $x$, Novikov therefore makes $F_t(x)$ a true
  martingale on every bounded interval.  Conditional Tonelli then gives
  $\mathbb E[P_t(E)\mid\mathcal F_s]=P_s(E)$ and integrability.
- Without compact support, each fixed-$x$ density factor is used only as a nonnegative local
  martingale, hence as a supermartingale.  Conditional Tonelli gives only
  $\mathbb E[P_t(E)\mid\mathcal F_s]\leq P_s(E)$.  No noncompact equality or uniform-integrability
  assertion occurs in the repaired dossier.

The stochastic-Fubini justification at `solutions/kls-excess-audit.tex:113`--`121` is incomplete.
The estimate on the already-integrated candidate coefficient,

$$
\left|\int F_t(x)(x-a_t)\,d\sigma_0(x)\right|\leq DN,
$$

does not by itself verify a stochastic-Fubini hypothesis before interchange.  A valid compact
support repair is short: boundedness of $x-a_t$ and Itô/Gronwall after localization give
$\mathbb E F_u(x)^2\leq e^{D^2u}$, and hence, for finite $T$,

$$
\mathbb E\int_0^T\int_{\partial^*E}
 |F_u(x)(x-a_u)|^2\,d\sigma_0(x)\,du
\leq D^2\sigma_0(\partial^*E)\int_0^T e^{D^2u}\,du<\infty.
$$

This is a genuine pre-interchange square-integrability bound and supplies stochastic Fubini.

The sentence at `solutions/kls-excess-audit.tex:134`--`135` also asserts the passage from the
smooth weighted-surface representation to arbitrary log-concave data and general finite-perimeter
sets without proving the required common coupling and perimeter limit.  This is delicate because
the manuscript uses Minkowski boundary measure, while the displayed surface representation uses
weighted reduced-boundary perimeter.  For the noncompact inequality, a direct countable repair
avoids that gap.  For positive rational $q$, put
$X_{q,t}=\mu_t(E_q\setminus E)/q$ and
$Y_{n,t}=\inf\{X_{q,t}:q\in\mathbb Q,\,0<q<1/n\}$.  Each $X_q$ is a bounded-test mass
martingale, so the already-valid countable-infimum argument makes $Y_n$ a supermartingale.
Moreover $Y_{n,t}\uparrow\mu_t^+(E)$ by the one-sided continuity of
$q\mapsto\mu_t(E_q)$ and the definition of lower Minkowski content.  Conditional monotone
convergence then gives
$\mathbb E[\mu_t^+(E)\mid\mathcal F_s]\leq\mu_s^+(E)$.  If the authors instead retain the
weighted De Giorgi convention, they must state it precisely and justify its
identification/approximation to the manuscript boundary convention.  The exact compact-support
identity must likewise identify the perimeter convention under which the surface representation
and expectation equality hold.

### Unconditional excess and exact identity

The proof of `prop:trivial-excess` at `solutions/kls-excess-audit.tex:151`--`170` is otherwise
correct.  It uses

$$
0\leq e_t(E)\leq P_t(E),\qquad
\mathbb E P_t(E)\leq P_0(E),
$$

Tonelli, and the indicator of $\{t<\tau\}$; it does not use optional stopping or independence of
$\tau$.  Isotropy supplies a variance-one coordinate marginal, log-concavity is preserved under
marginalization, mass one half makes a median coordinate halfspace admissible, and the
one-dimensional density bound gives $I_\mu(1/2)\leq1$.  The mean-zero part of isotropy and the
stopping-time property beyond measurability of the stopped integral are unused and are harmless
sharpening opportunities.

The cited one-dimensional input was checked in S. G. Bobkov, *Annals of Probability* 27 (1999),
Proposition 4.1 and (4.2), DOI
[`10.1214/aop/1022874820`](https://doi.org/10.1214/aop/1022874820).  It is a published source and
directly gives $\operatorname{Is}(\nu)=2f(m)$ together with
$\operatorname{Is}(\nu)^2\leq2/\operatorname{Var}(\nu)$, hence
$f(m)\leq1/\sqrt2<1$ at variance one.  This proves the constant needed in the dossier.  The
dossier instead attributes the distinct sharp assertion $\lVert f\rVert_\infty\leq1$ to this
paper; that assertion is true, but the checked passage does not state it.  The proof should cite
the median estimate actually checked or supply a precise source for the supremum estimate.  The
repository BibTeX entry currently carries the noncanonical DOI `10.1214/aop/1022677553`; the
orchestrator should send the exact metadata correction through the bibliography owner.  No
unreviewed preprint enters this step.

For `lem:excess-identity`, the algebra at `solutions/kls-excess-audit.tex:183`--`192` is exact once
the compact-support perimeter equality is available:

$$
\mathbb E e_t(E)=\mathbb E P_t(E)-\mathbb E I_{\mu_t}(p_t)
=P_0(E)-\mathbb E I_{\mu_t}(p_t).
$$

The proof never substitutes a noncompact equality.  Thus there is no defect in the algebra or in
the compact-support restriction; the remaining issue is the perimeter-convention/approximation
step identified above.

### Fixed competitor families

For a fixed nonempty **countable** family, `solutions/kls-excess-audit.tex:213`--`226` is correct.
Countability makes $J_t$ measurable and permits one common null set for the fixed-cut conditional
inequalities.  For each $S$,

$$
\mathbb E[J_t\mid\mathcal F_s]
\leq\mathbb E[P_t(S)\mid\mathcal F_s]
\leq P_s(S),
$$

so taking the countable infimum gives the supermartingale inequality.  Choosing
$S_0\in\mathfrak S$ gives
$0\leq J_t\leq P_t(S_0)$ and
$\mathbb E P_t(S_0)\leq P_0(S_0)<\infty$, which proves integrability.

The uncountable extension at `solutions/kls-excess-audit.tex:200`--`202` and 222--227 is not
justified by measurability of the pointwise infimum alone.  Each inequality for a fixed $S$ holds
outside an $S$-dependent null set, and an uncountable intersection of these full-measure sets need
not have full measure.  Measurability does not repair that problem.  The statement and proof must
instead do one of the following:

1. define $J_t=\operatorname*{ess\,inf}_{S\in\mathfrak S}P_t(S)$, in which case the defining
   order property gives the conclusion directly;
2. assume and prove that the pointwise infimum is determined almost surely by a fixed countable
   subfamily (equivalently, agrees with the essential infimum); or
3. supply joint measurability, measurable $\varepsilon$-selectors, and a proved conditional
   inequality for the resulting $\mathcal F_s$-measurable random selection.

The pointwise comparison
$I_{\mu_t}(p_t)\geq J_t(\eta)$ has the correct direction: the exact-mass class is contained in the
window class on $\{t<\tau_\eta\}$.  The dossier correctly declines to infer any supermartingale
property for this random, time-dependent family.

### Consumption audit

The consumption calculation at `solutions/kls-excess-audit.tex:257`--`311` was recomputed.  From
`lem:stein-vs-source` and the assumed unweighted Stein-trace estimate one gets

$$
\mathbb E\int S_t\,dt
\leq (2C_0+4C_2)T
 +2C_1\mathbb E\int r_t\,dt
 +(2\beta+64\eta^2)\mathbb E\int D_t\,dt
$$

for $e_0\leq1$.  The strict margin $2\beta+64\eta^2<1$ is exactly what
`cor:tight-window-consumption` consumes.  Failure of KLS supplies balanced near-minimizers with
perimeter tending to zero, while tight-window consumption supplies a universal positive lower
bound, giving the contradiction.  The two-tail construction is invoked only against a universal
one-time-slice inequality with the unweighted proof shape; the dossier makes no claim against a
time-nonlocal proof or the covariance-weighted formulation.

The direct dependency closure through `prop:two-tail`, `lem:stein-vs-source`, and
`cor:tight-window-consumption` consists of agent-certified proved nodes and contains no open,
conditional, refuted, or `preprint-unreviewed` premise.  The two-tail step used here is the
elementary Gaussian construction, not the nearby Letwin preprint input.

There are, however, two missing graph edges under `research/ledger-schema.md`, which defines
`depends_on` as the same-ledger claims actually used in the proof:

- `prop:trivial-excess` uses the deterministic-time consequence of
  `lem:perimeter-martingale`, so its ledger node at `research/kls/ledger.yaml:346`--`354` requires
  `depends_on: [lem:perimeter-martingale]`.
- `prop:intro-audit` explicitly invokes $h_\nu=2I_\nu(1/2)$ at
  `solutions/kls-excess-audit.tex:298`--`301`, so both its dossier header at lines 17--18 and its
  ledger node at `research/kls/ledger.yaml:332`--`341` require `lem:half` in `depends_on`.
  `cor:tight-window-consumption` supplies the boundary conclusion for a given cut; it does not
  supply this balanced-near-minimizer existence step.

Both omitted premises are proved, so adding the edges would not make either result conditional.
`prop:intro-audit` remains an unconditional theorem about an explicit implication; its
unweighted estimate is the antecedent, not an unrecorded discharged assumption.

### Fences

None of the five reviewed nodes has a ledger `bounded_by` edge.  The dossier nevertheless respects
the two nearby obstructions that matter.

- `obs:circularity` is respected: exact perimeter equality is used only in the compact-support
  identity, the fixed-family argument is not transferred to the moving mass-constrained family,
  and no lower bound for the localized profile is inserted as an input.
- `prop:two-tail` is used only to reject the slice-wise unweighted estimate.  It is not promoted to
  a no-go theorem for all time-dependent proofs and is not used against the weighted formulation.

## Corrections required before a new review

1. Repair the stochastic-Fubini step at `solutions/kls-excess-audit.tex:113`--`121` with a genuine
   pre-interchange integrability estimate, such as the $L^2$ estimate displayed above.
2. Replace or prove the general approximation sentence at
   `solutions/kls-excess-audit.tex:134`--`135`; explicitly reconcile the Minkowski and weighted
   reduced-boundary perimeter conventions.  The rational-boundary-layer/countable-infimum
   construction above is a direct route for the noncompact inequality.
3. Repair the uncountable clause at `solutions/kls-excess-audit.tex:199`--`227` by essential
   infimum, fixed countable determination, or a complete selector/kernel argument.  Mere
   measurability is insufficient.  Retain the already-correct nonemptiness, integrability, and
   two-inequality argument.
4. Add `lem:half` to the dossier header dependency list for `prop:intro-audit`.
5. At `solutions/kls-excess-audit.tex:163`--`168`, cite Bobkov's checked median/isoperimetric
   estimate directly (which gives the stronger $f(m)\leq1/\sqrt2$ needed here), or provide a
   precise published source for the stated sharp supremum-density bound.
6. Through the orchestrator, synchronize `modules/kls/24-excess-propagation.tex`: add the
   noncompact conditional supermartingale clause to the labeled perimeter statement; make the
   fixed competitor family nonempty; replace the manuscript's noncompact martingale invocation by
   the two inequalities; and state the same rigorous uncountable selection convention adopted by
   the dossier.
7. Through the orchestrator, make the ledger summaries mathematically explicit: add the isotropic
   log-concave and half-mass hypotheses to `prop:trivial-excess`; describe `lem:inf-martingales`
   using fixed-cut supermartingales in the noncompact case and the repaired countable/essential-inf
   convention; and add the two missing dependency edges described above.  Apply certification
   provenance only after a new proof review succeeds.  This audit proposes no certification
   delta.
8. Through the bibliography owner, correct `Bobkov1999LogConcave` to DOI
   `10.1214/aop/1022874820` after source verification.

## Validation and exclusions

The required standalone build

```bash
cd solutions && latexmk -pdf -outdir=../build kls-excess-audit.tex
```

was forced from scratch and completed with exit code zero.  The log has no TeX error, undefined
control sequence, emergency stop, or fatal error; its unresolved cross-manuscript references are
the expected standalone-subfile warnings.  `python3 research/check_ledger.py` reports 0 structural
errors on the current graph, which does not detect the semantic dependency omissions above.

This audit does not certify the historical 2026-08-25 source or report, any weighted excess/Stein
estimate, any supermartingale property for the random windowed family, an arbitrary raw
uncountable pointwise infimum, or any general rough-set limit not proved in the dossier.  No
solution, manuscript, bibliography, route-control, or ledger file was changed by the reviewer.
