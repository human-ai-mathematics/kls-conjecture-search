# KLS excess and bootstrap interface — independent R2 audit

- **Date:** 2026-08-25
- **Proof author:** `/root/kls_bootstrap_author`
- **Independent reviewer:** `/root/kls_core_author`
- **Reviewed dossiers:** `solutions/kls-excess-audit.tex` and `solutions/kls-bootstrap-interface.tex`
- **Certification:** `checked_by: agent`
- **Review type:** complete statement/dependency comparison and independent line-by-line mathematical rederivation
- **Verdict:** pass

## Certified scope

This report certifies exactly the following eleven KLS ledger nodes:

1. `prop:intro-audit`
2. `prop:trivial-excess`
3. `lem:perimeter-martingale`
4. `lem:excess-identity`
5. `lem:inf-martingales`
6. `lem:half`
7. `lem:whitening`
8. `thm:bootstrap`
9. `lem:crude`
10. `cor:loglog`
11. `prop:ceiling`

For every node I compared the dossier theorem with the exact statement, dependency edges, and
`bounded_by` metadata in `research/kls/ledger.yaml`, and with the corresponding manuscript
statement in `modules/kls/20-eldan-statements.tex`, `modules/kls/24-excess-propagation.tex`, or
`modules/kls/25-bootstrap.tex`. The dossier statements match the ledger scope and do not rely on
numerical evidence.

## Perimeter and excess checks

- For `lem:perimeter-martingale`, compact support bounds the pointwise localization integrand by
  the support diameter. Novikov therefore makes each density factor a true martingale;
  conditional Tonelli makes the boundary integral a true martingale. Stopping at a perimeter
  level gives the square-integrability needed for stochastic Fubini and yields the displayed
  driftless SDE. In the noncompact case, the proof now uses the conditional supermartingale
  inequality for each nonnegative density factor and conditional Tonelli, proving the full
  process-level perimeter supermartingale asserted in the ledger. No unjustified uniform
  integrability or unbounded optional sampling is used.
- For `prop:trivial-excess`, the pathwise inequalities
  $0\leq e_t(E)\leq P_t(E)$ and deterministic-time perimeter expectation bound justify Tonelli
  for an arbitrary stopping time. The one-dimensional variance-one log-concave marginal bound
  gives $I_\mu(1/2)\leq1$, so the constant is exactly $(1+e_0)T$.
- For `lem:excess-identity`, the equality is correctly restricted to compact support, where the
  true perimeter martingale gives $\mathbb E P_t=P_0$. The proof does not promote the noncompact
  supermartingale inequality to an equality.
- For `lem:inf-martingales`, the fixed competitor family is explicitly nonempty and measurable;
  conditional expectation followed by the fixed infimum has the correct direction. The exact
  mass competitor class is contained in the window class, so the pointwise profile comparison
  also has the correct direction. The proof explicitly refuses to transfer this argument to the
  random, time-dependent balanced-mass family.
- For `prop:intro-audit`, substituting the unconditional excess bound into the unweighted
  Stein-trace estimate and then the exact Stein/source conversion gives coefficients
  $(2C_0+4C_2)$, $2C_1$, and $2\beta+64\eta^2$. The assumed strict absorption margin is preserved.
  The near-Cheeger contradiction uses balanced cuts with $e_0\to0$ and the independently stated
  tight-window consumption result. The two-tail dependency rules out only the asserted
  slice-wise unweighted estimate; it does not claim to rule out time-nonlocal arguments.

## Bootstrap and covariance-interface checks

- `lem:half` follows from symmetry and concavity of the log-concave isoperimetric profile, and
  the balanced excess identity is exact. For `lem:whitening`, the Minkowski-neighborhood
  inclusion under $A_\nu^{1/2}$ loses exactly
  $\lambda_{\max}(A_\nu)^{1/2}$; Gaussian-product cylinder competitors give the claimed
  monotonicity of $\hstar_n$.
- I independently checked the sign-sensitive step in `thm:bootstrap`. When
  $1-P-\mathbb E X_t/2\geq0$, the near-worst estimate
  $\hstar_n/h_\mu\geq1-\varepsilon$ may be multiplied into the profile lower bound and gives
  precisely $\varepsilon/2+\eta+P/2+\mathbb E X_t/4$. When that bracket is negative, the
  desired right-hand side is already larger than $h_\mu/2$, so nonnegativity of the profile
  term closes the second case. Thus there is no reversed $h_\mu$/$\hstar_n$ substitution.
- The exit estimate stops the bounded continuous mass martingale, uses its quadratic variation,
  and needs no unbounded optional-sampling theorem. Integrating the estimate reproduces the
  constants $1/16$, $1/8$, and $1/4$ exactly. With
  $\eta=T^{1/3}$ and $\varepsilon\leq T^{1/3}$, the clean bound follows, for example with
  universal constant $C=2$.
- For `lem:crude`, localization of the covariance trace SDE followed by Fatou gives
  $\mathbb E\operatorname{Tr}A_t\leq n$, while Brascamp--Lieb gives $X_t\leq t^{-1}$.
  Integrating $\min(n,t^{-1})$ on $[0,T]$ gives exactly $1+\log(nT)$. This is used only as the
  insufficient lower fence required by `obs:crude-insufficient`.
- For `cor:loglog`, the imported small-time operator-norm window contributes $C_1t_1$ and the
  later Brascamp--Lieb interval contributes $\log(T/t_1)$. The published discharge is consumed
  as a dependency; no numerical result is substituted for it.
- For `prop:ceiling`, $\lambda_{\max}(A_t)\leq1+X_t$ turns the all-measure hypothesis into an
  integrated covariance bound. The stopped balanced mass must move by $1/6$ to exit
  $[1/3,2/3]$, so the exact factor is $36/4=9$. The stated assumption makes the exit probability
  at most $1/2$, and `lem:survival-implies-kls` then applies with universal constants. The result
  is only the advertised sufficient implication, not a converse or equivalence.

## Obstructions and corrections during review

The bootstrap proof respects `obs:circularity` by using the external floor $\hstar_n$ together
with a near-worst starting measure, rather than assuming a lower bound for the random localized
profile. The crude estimate is not used as a KLS route, respecting `obs:crude-insufficient`.
The ceiling proposition establishes precisely the sufficient condition that unlocks
`obs:relative-ceiling`.

During review, the author corrected three malformed integral separators and one missing
`\leq` in the bootstrap dossier. The author also strengthened the noncompact perimeter
paragraph from its deterministic expectation consequence to the full conditional
supermartingale statement and made the fixed competitor family explicitly nonempty. I checked
the resulting source and rebuilt both dossiers after these changes.

## Validation and exclusions

Both standalone builds completed with exit code 0 in repository-external build directories:

- `/tmp/kls-excess-audit-build/kls-excess-audit.pdf`
- `/tmp/kls-bootstrap-interface-build/kls-bootstrap-interface.pdf`

The remaining warnings are the expected unresolved manuscript-label links produced when these
subfiles are compiled alone; there are no TeX errors. This report does not certify the open
weighted excess package, KLS itself, any universal covariance ceiling, or any KLS node outside
the eleven IDs listed above. It certifies `prop:intro-audit` only as its stated logical
consumption audit using its separately certified dependencies, and `cor:loglog` only with its
stated imported small-time covariance hypothesis and discharge.
