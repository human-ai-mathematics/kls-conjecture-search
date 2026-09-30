---
verdict: pass
authors:
  - /root/kls_bootstrap_author
reviewer: /root/review_bootstrap_sync_w0
fingerprints:
  solutions/kls-bootstrap-interface.md: d6d28dffa0742e79a6a11db2f959c4c03e1bdec07666ffd2f37ce7b2cde7c4c1
  lem:half: 1d4daf2283e1a1022580a067533d1cc3aae4194fa319d223aa00e4112d031a2f
  lem:whitening: 3df7fc9dc6144b5c2ca23c0e9d21fc7a2132c0d494e03c75213cdc7ad7f72573
  thm:bootstrap: c63a5b4f893d86e70e67812caeccaa0015e754febda8a6a832909f82b015492b
  lem:perimeter-martingale: c0e1c3539694fe07c6ebe7c767bafeeadef66ac4778e02f7d217b6c9d3ad3daa
  lem:crude: 4596fedb12dae4093deded196b84f7f3f624d96f97cc69158a7eca583e997a6f
  cor:loglog: 035f1b7e266cba0c09dde33f9f0decf8f76e155da637c66068245423c77ef827
  hyp:KI: 19c8922790211e205d6eda530efc90f61707e276482b5179d2254928e394f7c4
  cor:KI-discharged: 2411e9c586f6ecbbb44f141b7f0b3a7733942614025262b49fcebc385b3f58d5
  prop:ceiling: c7e236675ff7d66fb1c5a49176dc3bbf67d6c775106f721568f6790b67d42b16
  lem:survival-implies-kls: fcc0ff284f00b4f7d903900409e37db884463ad15f1f7cbb2c48ecb254e4cc64
---

*Follows up* `research/reviews/2026-08-25-kls-excess-bootstrap-r2-audit.md`.

# Bootstrap semantic repair — cold proof review

This review was reconstructed from the repository artifacts, independently of the proof author's
conversation.  It reviews only `thm:bootstrap`, using the current dossier
`solutions/kls-bootstrap-interface.tex` (SHA-256
`caeb3bca1435e5c4633d7d46e3640dcb82f7a459e33cf37230619884ee77ae58`) and the repaired manuscript
statement and proof in `modules/kls/25-bootstrap.tex`.  The earlier report remains historical
provenance for its broader eleven-node scope; this report is the fresh semantic-agreement check for
the repaired bootstrap manuscript.

## Findings

### Statement agreement

The manuscript theorem at `modules/kls/25-bootstrap.tex:56`--`83`, the dossier theorem at
`solutions/kls-bootstrap-interface.tex:128`--`164`, and the ledger statement at
`research/kls/ledger.yaml:458`--`468` agree mathematically.  All three have the same quantifiers and
hypotheses: $n\ge2$, $\varepsilon\in(0,1]$, isotropic log-concave $\mu$ with
$h_\mu\le(1+\varepsilon)h_n^\star$, an arbitrary balanced cut $E$, and
$\eta\in(0,1/2)$.  They assert the same pointwise excess bound, the same exit bound with constant
$1/(4\eta^2)$, the same integrated coefficients $1/16$, $1/8$, and $1/4$, and the same clean
$T^{4/3}$ consequence under $0<T<1/8$, $\eta=T^{1/3}$, and
$\varepsilon\le T^{1/3}$.  The dossier's $e_0=e_0(E)=\bar e_0(E)$ is exactly the balanced identity
used by the manuscript; the ledger's phrase “balanced cut” is the same scope.

### Line-by-line proof check

1. For $A=\{t<\tau_\eta\}$, the deterministic-time perimeter supermartingale consequence gives
   $\mathbb E[\mu_t^+(E)\mathbf1_A]\le\mu^+(E)=h_\mu/2+e_0$.  There is no perimeter optional
   stopping step.

2. On $A$, $\min(p_t,q_t)\ge a:=1/2-\eta$.  Whitening and
   $\lambda^{-1/2}\ge1-(\lambda-1)_+/2$ give, with
   $P=\mathbb P(\tau_\eta\le t)$ and $Y=\mathbb E X_t$,
   $$
   \mathbb E[h_{\mu_t}\min(p_t,q_t)\mathbf1_A]
   \ge h_n^\star a(1-P-Y/2).
   $$
   The replacement of $\mathbb E[X_t\mathbf1_A]$ by $Y$ has the correct lower-bound direction.

3. Put $B=1-P-Y/2$ and $\rho=h_n^\star/h_\mu$.  Isotropy and near-worstness give
   $1/(1+\varepsilon)\le\rho\le1$, hence $\rho\ge1-\varepsilon$.  The repaired sign split is
   necessary and correct.  If $B\ge0$, multiplication by the lower bound for $\rho$ preserves the
   direction and
   $$
   \frac12-(1-\varepsilon)aB
   =\bigl[\tfrac12-a(1-P)\bigr]+\frac{aY}{2}+\varepsilon aB
   \le \eta+\frac P2+\frac Y4+\frac\varepsilon2.
   $$
   Here $a\le1/2$ and $0\le B\le1$.  If $B<0$, the proof does not multiply by a lower bound for
   $\rho$: it uses nonnegativity of the posterior Cheeger term, while
   $P/2+Y/4>1/2$, so the desired right side is strictly larger than $h_\mu/2$.  This is exactly the
   two-case logic in the dossier at lines 194--226.

4. The process $M_u=p_{u\wedge\tau_\eta}-1/2$ is a bounded continuous square-integrable
   martingale.  With the strict-exit convention
   $\tau_\eta=\inf\{u:|p_u-1/2|>\eta\}$, continuity implies that on
   $\{\tau_\eta\le t\}$ the stopped path reaches the boundary $|M|=\eta$.  The weak $L^2$
   maximal inequality (equivalently, optional sampling of $M^2-[M]$ at the hitting time) therefore
   gives the sharp factor
   $$
   \mathbb P(\tau_\eta\le t)\le\eta^{-2}\mathbb E M_t^2
   =\eta^{-2}\mathbb E[p]_{t\wedge\tau_\eta}.
   $$
   The mass quadratic variation and covariance decomposition give
   $d[p]_s=s_sr_s\,ds\le\lambda_{\max}(A_s)\,ds/4\le(1+X_s)\,ds/4$.
   Replacing $\mathbf1_{\{s\le\tau_\eta\}}$ by
   $\mathbf1_{\{s<\tau_\eta\}}$ changes only one Lebesgue-time point on each path.  This proves
   the displayed $1/(4\eta^2)$ exit estimate with no unbounded optional-stopping argument.

5. Tonelli gives
   $$
   \int_0^T\mathbb P(\tau_\eta\le t)\,dt
   \le\frac1{4\eta^2}\left(\frac{T^2}{2}
       +\int_0^T(T-s)\mathbb E X_s\,ds\right)
   \le\frac1{4\eta^2}\left(\frac{T^2}{2}+T\Xi_T\right).
   $$
   Multiplication by the $P/2$ coefficient in the pointwise estimate yields exactly
   $T^2/(16\eta^2)$ and $T\Xi_T/(8\eta^2)$; integrating $Y/4$ yields $\Xi_T/4$.

6. For $\eta=T^{1/3}$,
   $$
   (\varepsilon/2+\eta)T\le\tfrac32T^{4/3},\qquad
   \frac{T^2}{16\eta^2}=\frac1{16}T^{4/3},\qquad
   \frac{T\Xi_T}{8\eta^2}=\frac18T^{1/3}\Xi_T\le\frac18\Xi_T.
   $$
   Since $T<1/8$ makes $\eta<1/2$, the choice is admissible; together with $\Xi_T/4$, the clean
   form holds, for example with $C=2$.

### Hypotheses, dependencies, citations, and fence

The proof uses balance of $E$, log-concavity, isotropy, the near-worst comparison, the stated
window range, the perimeter supermartingale, the whitening comparison, and the mass quadratic
variation/covariance decomposition.  For a cut of infinite initial perimeter the claimed bound is
trivial in the extended sense; the nontrivial case is finite perimeter.  No unstated
near-minimality of $E$ is used.  The restrictions $n\ge2$ and $\varepsilon\le1$ are not needed by
the displayed argument (the proof works in dimension one and for every $\varepsilon\ge0$); these
are harmless sharpening opportunities, not defects.

The ledger dependencies are exactly `lem:half`, `lem:whitening`, and
`lem:perimeter-martingale`.  The first two retain agent-certified proofs in the unchanged bootstrap
dossier.  The generalized profile concavity used by `lem:half` was checked in Emanuel Milman's
published *Inventiones Mathematicae* article (Theorem 1.8 and the ensuing deduction
$D_{\mathrm{Che}}=2I(1/2)); no unreviewed preprint enters this theorem.  The separately edited
`solutions/kls-excess-audit.tex`, which owns `lem:perimeter-martingale`, is currently
`checked_by: none` pending a fresh cold review.  Consequently this passing review certifies the
bootstrap implication but permits only `status: conditional` until that dependency is freshly
certified.  It does not inherit the stale historical certification of changed dependency bytes.

The sole fence is `obs:circularity`.  It is respected: the proof does not claim a supermartingale
property for the random mass-constrained profile.  Its posterior Cheeger lower bound comes from
whitening to the external worst-case constant $h_n^\star$ and comparing that constant to the
explicitly near-worst starting measure; no dimension-free lower bound for $h_n^\star$ is assumed.

## Corrections

None to the reviewed bootstrap theorem, proof, or dossier.  The repaired manuscript sign split and
stopped-martingale exit argument agree with the dossier.

## Validation

- `cd solutions && latexmk -pdf -outdir=../build kls-bootstrap-interface.tex`: exit code 0; only
  expected standalone cross-manuscript references remain unresolved.
- `cd modules/kls && latexmk -pdf -outdir=../../build 25-bootstrap.tex`: exit code 0; only expected
  standalone cross-module references remain unresolved.
- `latexmk -pdf -outdir=build main.tex` typeset `modules/kls/25-bootstrap.tex` successfully, then
  stopped on the unrelated malformed citation at `modules/kls/27-eldan-open-targets.tex:34`.
- `python3 research/check_ledger.py`: 0 structural errors before this report was added.

## Proposed active-review delta

The exact delta currently justified for `thm:bootstrap` is:

```yaml
status: conditional
solution: solutions/kls-bootstrap-interface.tex
checked_by: agent
review: research/reviews/2026-08-27-thm-bootstrap-semantic-repair-proof-review.md
```

Leave its statement, `depends_on`, and `bounded_by` edges unchanged.  Replace the active review
pointer only for `thm:bootstrap`; the 2026-08-25 report remains active historical provenance for
the other nodes it covers.  Once `lem:perimeter-martingale` receives a fresh passing review, this
same bootstrap certification may take `status: proved` without rechecking the unchanged bootstrap
argument.

## Exclusions

This report does not certify `lem:half`, `lem:whitening`, `lem:crude`, `cor:loglog`,
`prop:ceiling`, any node in `solutions/kls-excess-audit.tex`, the full manuscript build, the nearby
pathwise feature remark, any covariance-interface evaluation, any weighted excess statement, or
KLS.  It does not certify the currently repaired perimeter dependency; that dossier requires its
own distinct cold reviewer.  Bibliography metadata and the unrelated module-27 TeX failure are
outside this review's write scope.

```yaml
outcome: complete
artifacts:
  - research/reviews/2026-08-27-thm-bootstrap-semantic-repair-proof-review.md
proposed_deltas:
  - "For thm:bootstrap, set status: conditional, solution: solutions/kls-bootstrap-interface.tex, checked_by: agent, and review: research/reviews/2026-08-27-thm-bootstrap-semantic-repair-proof-review.md; preserve its statement and graph edges."
next_role: orchestrator
next_prompt: |
  Activate the fresh review pointer only for thm:bootstrap.  Until the changed
  solutions/kls-excess-audit.tex receives a distinct passing proof review certifying
  lem:perimeter-martingale, record thm:bootstrap as conditional rather than proved.  After that
  dependency is freshly certified, thm:bootstrap may be promoted to proved with this same review;
  preserve its statement, depends_on, and bounded_by edges, and leave the historical broad review
  active for its other nodes.  Run python3 research/check_ledger.py after the atomic ledger update.
```
