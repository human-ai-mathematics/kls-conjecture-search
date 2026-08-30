# Prover: degree-two root-frame pencil identity (candidate node lem:fiber-root-degree-two)

Date: 2026-08-30

Role: `prover`

Run id: `w4p04`

Concurrency key: `solution:lem-fiber-root-degree-two`

Write scope: `solutions/lem-fiber-root-degree-two.tex` and this append-only exploration.
No ledger, manuscript, route-control, bibliography, review, knowledge, or numerical file was
touched.  The target node is a **candidate**; its ledger admission is pending and is an
orchestrator decision.  The dossier ships with `checked_by: none`, which has **no ledger
value**.

## Task

Write an optional structural dossier for the conditional-fiber-frame route (NOT the all-frame
gate) proving, for every $m\ge3$, on the degree-$\le2$ quotient $V_{m,2}$ of the isotropic
uniform simplex, the exact identity

$$\lambda_{\min}(K_{\mathrm{root}},G)\big|_{V_{m,2}}=\frac{(m+2)(m+3)}{5m^2},$$

attained by the radial quadratic $F=|X|^2-d$ — the candidate identity surfaced by the exact
rational `finum` channel at $m=3..15$
(`research/runs/2026-08-30T172853.262299Z-fiber-frame-dual.jsonl` and the deep artifact),
via the $S_m$-isotypic route sketched in the w1f01 probe.  Plus the **conditional** corollary:
the root frame being one admissible frame, $\Lambda_{m,2}\ge(m+2)(m+3)/(5m^2)>1/5$, so no
degree-2 dual certificate (w1f01 eqs. 44–49 at $k=2$) can refute the route, and any
fixed-degree polynomial dual refuter needs $k\ge3$.  Explicitly out of scope: the all-frame
gate itself, $k\ge3$, non-polynomial tests, KLS.

## What was done

Dossier written at `solutions/lem-fiber-root-degree-two.tex`; standalone build clean
(`latexmk -pdf -outdir=../build`, 11 pages, 0 LaTeX errors; the 7 unresolved `\ref`s are
cross-module manuscript labels, expected `??` standalone).

### Proof architecture (all analytic; no numerical step anywhere)

1. **Pair-fiber lemma.**  For a pair $(i,j)$, conditionally on the other coordinates,
   Dirichlet neutrality makes $\delta/s=(p_i-p_j)/(p_i+p_j)$ uniform on $[-1,1]$.  The key
   simplification over the w1f01 presentation: parametrize the fiber by the *symmetric*
   variable $\delta$ rather than by $U=p_i/s$.  Any degree-$\le2$ polynomial restricts to
   $\alpha+\beta\delta+\gamma\delta^2$ with $\mathcal F_{ij}$-measurable coefficients, and
   because $\mathbb E[(\delta/s)^3]=0$ the $\beta$–$\gamma$ cross term vanishes:

   $$\mathbb E\Big[\frac{\mathrm{Cov}_{ij}(f,g)}{s^2}\Big]
     =\tfrac13\,\mathbb E[\beta_f\beta_g]+\tfrac4{45}\,\mathbb E[\gamma_f\gamma_g s^2].$$

   This kills every mixed term that plagued the first (asymmetric, $U$-based) pass.
2. **Isotypic decomposition of $V_{m,2}$ without Specht-module machinery.**
   $V_{m,2}\cong\mathrm{triv}\oplus\mathrm{std}\otimes\mathbb R^2\oplus\mathrm X$
   ($\mathrm X$ absent at $m=3$), proved by elementary orbit counting only:
   $\dim\mathrm{End}$ of the point permutation module is 2, of the 2-subset module is 3, and
   $\dim\mathrm{Hom}$ between them is 2; the kernel of
   (degree-$\le2$ polynomials) $\to L^2(\mu)/\mathbb R$ is identified exactly as
   $\{b_0\Sigma p+(\Sigma p-1)\Sigma b_ip_i\}\cong2\,\mathrm{triv}\oplus\mathrm{std}$, and
   multiplicities subtract.  All irreducibles used have real endomorphism field by the same
   counting, which is exactly what the invariant-pencil reduction needs.
3. **Invariant pencil reduction.**  Distinct isotypic sectors are orthogonal for every
   invariant form; on $\mathrm{std}\otimes\mathbb R^2$ every invariant symmetric form is
   $J\otimes B$ (1-dimensionality of invariant forms on an absolutely irreducible real
   module), so the full sector is controlled by the $2\times2$ Gram matrices of the seeds
   $L=[p_1-p_2]$, $Q=[p_1^2-p_2^2]$ — the multiplicity-space mixing between the linear and
   quadratic standard copies is handled as a genuine $2\times2$ rational pencil, not two
   scalars.
4. **Sector values** (Dirichlet moments $D_r=m(m+1)\cdots(m+r-1)$):
   - trivial: $K(f_0,f_0)=\frac{4(m-1)}{5m^2(m+1)^2}$,
     $G(f_0,f_0)=\frac{4(m-1)}{(m+1)^2(m+2)(m+3)}$, quotient $\lambda^*=\frac{(m+2)(m+3)}{5m^2}$;
   - standard: $K=\frac{2}{m(m+1)}\big[\begin{smallmatrix}1&2/m\\2/m&\frac{4(8m-1)}{5m^2(m+1)}\end{smallmatrix}\big]$,
     $G=\frac{2}{m(m+1)}\big[\begin{smallmatrix}1&4/(m+2)\\4/(m+2)&\frac{20}{(m+2)(m+3)}\end{smallmatrix}\big]$, and
     $5m^2(\widetilde K-\lambda^*\widetilde G)=(m-2)\big[\begin{smallmatrix}4m+3&6\\6&12/(m+1)\end{smallmatrix}\big]\succ0$
     for $m\ge3$ (bracket determinant $=12m/(m+1)$);
   - two-row seed $F=(p_1-p_3)(p_2-p_4)$: quotient
     $\frac{2(5m-4)}{m+1}\lambda^*=\lambda^*\big(1+\frac{9(m-1)}{m+1}\big)>\lambda^*$.
   Hence $K-\lambda^*G\succeq0$ with kernel exactly the radial line; $\lambda_{\min}=\lambda^*$,
   uniquely attained (up to scalar) by $|X|^2-(m-1)=m(m+1)[\Sigma p_i^2]$.
5. **Conditional corollary** (weak duality against the root atoms only, so no
   frame-measurability technicalities): every degree-2 dual certificate has objective
   $\varepsilon\ge\lambda^*>1/5$; no $\varepsilon_m\to0$ sequence at $k=2$; fixed-degree dual
   refuters need $k\ge3$; $\Lambda_{m,2}\ge\lambda^*$.  Stated only conditionally on the
   certified identification of the pair formula with the conditional-fiber root pencil
   (`solutions/conditional-fiber-frame-structure.tex`, nodes `lem:conditional-fiber-form`
   and `prop:conditional-fiber-root-obstruction`, both `checked_by: agent`) and on the
   candidate status of the $\Lambda_{m,k}$/dual-certificate framework.  Explicit non-claims
   recorded in the dossier.

### Verification discipline

- Every Gram entry was derived twice by hand: once in the asymmetric $U$-parametrization
  (matching w1f01 eqs. 26–36 conventions), once in the symmetric $\delta$-parametrization
  used in the dossier; all entries agreed.
- The closed forms match the exact rational values recorded through the proper `finum`
  channel in the two run artifacts: pencil minima $2/3,\,21/40,\,56/125$ at $m=3,4,5$
  ($k=2$) and the radial anchors $(m+2)(m+3)/(5m^2)$ at every computed $m\le15$.  Recorded
  in a dossier remark as **directional evidence only**; no proof step uses it.
- Additionally, as a pure arithmetic self-check of my own algebra (exact `fractions.Fraction`
  linear algebra, no floating point, no randomness, `/tmp`, not committed, not evidence and
  not cited in the dossier), I re-assembled the full pencil independently at $m=3..6$ and
  confirmed: $K-\lambda^*G\succeq0$ with kernel exactly the radial line (via all leading
  principal minors of $M+v_0v_0^T$), the trivial and two-row closed-form eigenvalues are
  roots of $\det(K-\lambda G)$, and all six standard-sector Gram entries and the
  $2\times2$ $M$-matrix entries match the closed forms.  The independent certified check
  remains entirely the proof-checker's.

## Dead ends and notes for the reviewer

1. **Asymmetric fiber parametrization.**  Expanding in $U=p_i/s$ (as in w1f01 eq. 27–29)
   produces $\mathrm{Cov}(U,U^2)=1/12\ne0$ cross terms in every mixed pair energy; the
   computations close but are error-prone.  The symmetric $\delta$-parametrization makes all
   cross terms vanish identically ($\mathbb E V^3=0$ for $V$ uniform on $[-1,1]$) and is the
   form used in the dossier.  Do not redo this with $U$.
2. **Specht-module machinery is unnecessary.**  A first outline invoked Specht modules and
   absolute irreducibility of $S_m$-irreducibles as imported facts; everything actually
   needed ($\mathrm{End}=\mathbb R$ for the three modules involved, multiplicities, sector
   orthogonality, $J\otimes B$ factorization) follows from orbit counting on two permutation
   modules plus Schur, which keeps the dossier self-contained for a cold reviewer.
3. **Seed independence needs $m\ge3$ explicitly.**  The kernel comparison that proves
   $L,Q$ linearly independent in $V_{m,2}$ uses the existence of a third index (the
   $p_1p_3$-coefficient argument); at $m=2$ the quotient degenerates (the theorem is stated
   for $m\ge3$; at $m=2$ the root move resamples the whole 1-simplex and every quotient is 1,
   consistent with the formula's value 1 at $m=2$, but this is not claimed).
4. **The corollary must not be stated as an all-frame or $L^2$ fact.**  The certified
   vertex-cap obstruction gives root-frame $L^2$ gap $O(m^{-2})$; the degree-two floor
   $\to1/5$ is strictly a polynomial-quotient statement.  The two are compatible because the
   cap indicator is not in $V_{m,2}$; the dossier's audit paragraph spells this out.

## Deferred artifact candidate (no applicable ledger delta)

`checked_by: none` has no ledger value.  If (and only if) a cold proof-checker certifies the
dossier and the orchestrator admits the candidate node, the future node would carry
`solution: solutions/lem-fiber-root-degree-two.tex` plus the reviewer's `review:` path; the
corollary part would additionally record its dependence on `lem:conditional-fiber-form` /
`prop:conditional-fiber-root-obstruction`.  No delta is proposed by this role.

```yaml
outcome: complete
artifacts:
  - solutions/lem-fiber-root-degree-two.tex
  - research/explorations/2026-08-30-prover-fiber-root-degree-two-w4p04.md
proposed_deltas:
  - none
next_role: proof-checker
next_prompt: |
  Cold-review the prover dossier solutions/lem-fiber-root-degree-two.tex (candidate ledger
  node lem:fiber-root-degree-two, checked_by: none, author: prover agent w4p04; you must be
  a distinct agent and reconstruct the proof from repository artifacts, not from the
  author's account).  Standalone build is clean: latexmk -pdf -outdir=../build produced
  11 pages with 0 errors; the only warnings are 7 unresolved cross-module \ref targets
  (sec:conditional-fiber-frame, q:conditional-fiber-frame, eq:conditional-root-form,
  prop:conditional-fiber-root-obstruction), expected standalone.

  Claimed theorem (unconditional): for every m >= 3, on the degree-<=2 quotient V_{m,2} of
  L^2 of the isotropic uniform simplex modulo constants, the A_{m-1} root-frame pair form
  K(f,f) = (12/(m^2(m+1))) sum_{i<j} E[Var_{ij}(f)/(p_i+p_j)^2] and G = Var satisfy
  lambda_min(K,G) = (m+2)(m+3)/(5m^2), attained exactly on the radial line
  R.[|X|^2-(m-1)] = R.[sum_i p_i^2].  Claimed corollary (conditional, refutation-channel
  only): assuming the agent-certified identification of K with the conditional-fiber root
  pencil (solutions/conditional-fiber-frame-structure.tex, nodes lem:conditional-fiber-form
  and prop:conditional-fiber-root-obstruction), every degree-2 dual certificate in the
  candidate Lambda_{m,k} framework (w1f01 eqs. 44-49, restated self-containedly in the
  dossier) has objective >= (m+2)(m+3)/(5m^2) > 1/5, hence no eps_m -> 0 refuter sequence at
  k = 2 and any fixed-degree polynomial dual refuter needs k >= 3; and
  Lambda_{m,2} >= (m+2)(m+3)/(5m^2).  The dossier explicitly does NOT claim: upper bounds on
  Lambda_{m,2}, anything at k >= 3, anything about non-polynomial tests or the full L^2 gap
  (the certified vertex-cap O(m^-2) obstruction stands), root-orbit optimality, the gate
  q:conditional-fiber-frame, or KLS.

  Hypotheses actually used: theorem part - Dirichlet(1,...,1) monomial moments (proved in
  the dossier via the classical Gamma-Dirichlet factorization, the only imported classical
  fact), Dirichlet pair neutrality (proved), finite-group facts (F1)-(F5) (proved or
  one-line classical); corollary part - the certified root-form identification above plus
  the candidate framework definitions.  Fence check: the candidate node has bounded_by:
  none; the dossier's audit paragraph verifies consistency with
  prop:conditional-fiber-root-obstruction and prop:sasada-negative-exchange (both concern
  the full L^2 gap; the cap indicator is not degree-2) and non-implication of the six
  Eldan-route obs fences.  No numerical evidence is used in any proof step; a remark cites
  the run artifacts research/runs/2026-08-30T*-fiber-frame-dual.jsonl only as directional
  agreement (exact recorded minima 2/3, 21/40, 56/125 at m=3,4,5 and radial anchors to
  m=15).

  Audit specifically: (1) the pair-fiber lemma (uniformity of delta/s, the
  alpha+beta*delta+gamma*delta^2 decomposition, vanishing cross moments, formula
  E[Cov_ij/s^2] = E[beta_f beta_g]/3 + (4/45)E[gamma_f gamma_g s^2], and the mu-null s=0
  face); (2) the orbit-counting module decomposition V_{m,2} = triv + 2 std + X including
  the kernel identification and the m=3 degeneration; (3) the invariant pencil reduction
  (sector orthogonality, J tensor B factorization, seed-Gram equivalence) and that the seeds
  L=[p_1-p_2], Q=[p_1^2-p_2^2] really span the standard sector and
  F=[(p_1-p_3)(p_2-p_4)] really lies in the X sector (inner-product checks against
  sum x_{ij} and u_k in the 2-subset module); (4) every per-pair (beta,gamma) table entry
  and every Gram entry in Lemmas 6-8 against the moment table, including the pair counts
  2(m-2) and 4(m-4); (5) the PSD matrix identity
  5m^2(Ktilde - lambda* Gtilde) = (m-2)[[4m+3,6],[6,12/(m+1)]] and its determinant 12m/(m+1);
  (6) the two-row comparison 2(5m-4)/(m+1) > 1; (7) the corollary's weak-duality chain over
  the root atoms and that its conditionality and non-claims are correctly scoped.  Write
  your review under research/reviews/ per the structured contract; do not edit solutions/
  or any ledger.  Verdict pass -> orchestrator (ledger admission of the candidate node is a
  separate orchestrator decision); verdict revise -> return exact repair instructions to the
  prover.
```
