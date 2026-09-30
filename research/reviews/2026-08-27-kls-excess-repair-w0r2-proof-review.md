---
verdict: pass
authors:
  - /root/kls_bootstrap_author
  - /root/repair_excess_dossier
reviewer: /root/review_excess_repair_w0r2
fingerprints:
  solutions/kls-excess-audit.md: 4a87955fd2c105aa8e6e072e00d42c97a216349cfde817ac6376f3a6baef461c
  prop:intro-audit: 8dbbea111a4c607be2501cbef1b2fd914e0a188ff8b97b9631156b63ff018d73
  prop:trivial-excess: a48276dd038b07e29bdf15f7978fb1451dce76c2fd9754ca442124bb019c0c6f
  prop:two-tail: 85de1f26b16a82f85696ec5a655749365c0f036976c11265cee235f780c44d7b
  lem:stein-vs-source: 6bd84bc399d194fcb26d5a831feb198bcda29c1beaa21a9d1ebe64320eca30b5
  cor:tight-window-consumption: 7d0f9e5dce52482fc3b8f93155bb46e66596d3aac7d92a63f7e508bc25b59946
  lem:half: 1d4daf2283e1a1022580a067533d1cc3aae4194fa319d223aa00e4112d031a2f
  lem:perimeter-martingale: c0e1c3539694fe07c6ebe7c767bafeeadef66ac4778e02f7d217b6c9d3ad3daa
  lem:excess-identity: f131066c290e6c26f2de7acbdbff70216e8fb3fceb81b4ab5a6fe42b1be7096d
  lem:inf-martingales: 3a548b25863f6597c2c6a66b30d9a6684c865e0d7611ad0a74ad87f2a339b265
---

*Follows up* `research/reviews/2026-08-27-kls-excess-repair-w0-audit.md`.

# KLS perimeter/excess repair W0R2 — cold proof review

This review was reconstructed from the repository artifacts, independently of the proof authors'
conversation.  The earlier audit was read only as the repair contract and is not mathematical
evidence for this verdict.  The reviewer is distinct from both the original author and the repair
author, and no exploration log names this reviewer as an author.

## Frozen review boundary

The mathematical review used these exact bytes:

| Artifact | SHA-256 |
|---|---|
| `solutions/kls-excess-audit.tex` | `2b7621ec14eb26db23a0266fac06c693733a87e45345374daf5fe3418e2e7cae` |
| `modules/kls/10-notation.tex` | `eeb37fc6c4d54651a0a493012ebc4908f20ba71d837e1f111a99befd3b4f918c` |
| `modules/kls/20-eldan-statements.tex` | `d3b40f203df4387019f6e59c07f9a1cee5d47ff7bf8819e14997f59d85acc315` |
| `modules/kls/24-excess-propagation.tex` | `fc5570729317ab23b83551bae8d8f9b26203219a001f754165b072d941ea5777` |
| `research/kls/ledger.yaml` | `876b5c62d87f83153b4434d74cc5f48c64cab8adeccb62ce3b33bb29d1b250b2` |

The ledger hash differs from the initially supplied snapshot only because four disjoint open nodes
were appended by the ledger owner during the review.  I re-read the current five-node slice and its
dependency closure after that append; the reviewed entries and all four primary TeX artifacts were
unchanged.

## Findings

### Statement agreement

The dossier theorem statements, current ledger summaries, and labeled manuscript statements agree
mathematically:

| Node | Agreement checked |
|---|---|
| `prop:intro-audit` | The three-part dossier statement at `solutions/kls-excess-audit.tex:320` and the manuscript statement at `modules/kls/20-eldan-statements.tex:164` assert the same unconditional excess bound, the same implication from the full unweighted replacement of the fixed-window Stein-trace estimate, and the same two-tail obstruction to a universal slice-wise inequality.  The ledger at `research/kls/ledger.yaml:384` records the same three conclusions and now includes the explicitly used `lem:half` edge. |
| `prop:trivial-excess` | The dossier at `solutions/kls-excess-audit.tex:212`, manuscript at `modules/kls/24-excess-propagation.tex:15`, and ledger at `research/kls/ledger.yaml:398` all require isotropic log-concave data, a balanced Borel cut of finite initial perimeter in the repository's lower outer Minkowski convention, arbitrary $T>0$, and an arbitrary stopping time, and assert the same $(1+e_0)T$ bound.  The ledger now records the used perimeter dependency. |
| `lem:perimeter-martingale` | The dossier at `solutions/kls-excess-audit.tex:79`, manuscript at `modules/kls/24-excess-propagation.tex:66`, notation convention at `modules/kls/10-notation.tex:169`, and ledger at `research/kls/ledger.yaml:420` all separate the general fixed-Borel-cut supermartingale from the true martingale/SDE, which is restricted to a smooth compactly supported initial density and a $C^2$ tubular boundary. |
| `lem:excess-identity` | The dossier at `solutions/kls-excess-audit.tex:247`, manuscript at `modules/kls/24-excess-propagation.tex:120`, and ledger at `research/kls/ledger.yaml:430` all restrict the exact expectation identity to precisely the smooth compact-support/tubular-boundary class of the perimeter equality.  No noncompact equality is asserted. |
| `lem:inf-martingales` | The dossier at `solutions/kls-excess-audit.tex:272`, manuscript at `modules/kls/24-excess-propagation.tex:140`, and ledger at `research/kls/ledger.yaml:441` all require a fixed nonempty countable family, or a prescribed family with a fixed countable determining subfamily.  All three reject mere measurability of a raw uncountable infimum and reject a supermartingale inference for the random time-dependent balanced family. |

The dossier header enumerates all five nodes and the dependency edges actually used.  The displaced
proof of `prop:intro-audit` is correctly identified as lying in module 24 even though its statement
label is in module 20.

### General lower-Minkowski perimeter supermartingale

I checked the construction at `solutions/kls-excess-audit.tex:98`--`150` in the manuscript's exact
perimeter convention.

1. For a fixed rational $q>0$, $E\subset E_q$ and
   $$
   X_{q,t}=q^{-1}\mu_t(E_q\setminus E).
   $$
   The test function $q^{-1}\mathbf 1_{E_q\setminus E}$ is bounded and fixed before localization,
   so the bounded-test localization identity makes $X_q$ a nonnegative true martingale.  This uses
   neither a smooth-set approximation nor a surface-perimeter convention.

2. For fixed $n$, the family of rational $q\in(0,1/n)$ is nonempty and countable.  Hence
   $Y_{n,t}=\inf_qX_{q,t}$ is measurable, nonnegative, and bounded above by any one admissible
   $X_{q_n,t}$, so it is integrable.  From $Y_{n,t}\le X_{q,t}$,
   $$
   \mathbb E[Y_{n,t}\mid\mathcal F_s]
   \le X_{q,s}
   $$
   for every rational $q$.  Countability permits the conditional inequalities to be realized on
   one full-probability set before taking the infimum, giving
   $\mathbb E[Y_{n,t}\mid\mathcal F_s]\le Y_{n,s}$.

3. For any probability measure $\nu$ and any real $r>0$, choose rational $q_k\uparrow r$.
   Then $E_{q_k}\setminus E\uparrow E_r\setminus E$, so continuity from below and
   $q_k\to r$ give
   $$
   \frac{\nu(E_{q_k}\setminus E)}{q_k}
   \longrightarrow
   \frac{\nu(E_r\setminus E)}r.
   $$
   Thus the rational infimum on $(0,1/n)$ is no larger than every real-radius value; the reverse
   inequality follows because the rationals are a subset.  The rational and real infima are equal.
   Since the intervals shrink with $n$,
   $$
   Y_{n,t}\uparrow
   \sup_n\inf_{0<r<1/n}\frac{\mu_t(E_r)-\mu_t(E)}r
   =\mu_t^+(E).
   $$

4. Ordinary monotone convergence at $s=0$ yields
   $\mathbb E\mu_t^+(E)\le\mu_0^+(E)<\infty$, so the limiting perimeter is integrable.  Conditional
   monotone convergence can then be applied to the already established nonnegative inequalities,
   and gives
   $$
   \mathbb E[\mu_t^+(E)\mid\mathcal F_s]\le\mu_s^+(E).
   $$
   The order of these two limit operations is correct: integrability is established before the
   result is named an integrable supermartingale.

### Smooth tube formula, stochastic Fubini, and true-martingale upgrade

I checked `solutions/kls-excess-audit.tex:152`--`207` separately from the preceding rough-set
argument.

- The canonical localization density from `modules/kls/10-notation.tex:30` is continuous in $x$;
  hence $w_t=F_tw_0$ is a continuous compactly supported density for each finite time and sample
  path.  On the relevant compact portion of a $C^2$ boundary, the stipulated tubular neighborhood
  supplies outward normal coordinates with Jacobian $1+O(r)$.  Dominated convergence therefore
  gives the one-sided formula
  $$
  \mu_t^+(E)=\int_{\partial^*E}F_t\,d\sigma_0,
  \qquad d\sigma_t=F_t\,d\sigma_0.
  $$
  This is the same lower outer Minkowski content used in the general clause, not an identification
  with surface area for a rough set.  Compactness and the tubular hypothesis also make
  $\sigma_0(\partial^*E)<\infty$.

- If $K$ contains the initial support and $D=\operatorname{diam}K$, then
  $|x-a_u|\le D$ for $\sigma_0$-almost every boundary point because both $x$ and $a_u$ lie in
  $\operatorname{conv}K$.  Localizing the pointwise density SDE, applying Ito to $F^2$, and then
  Gronwall and Fatou gives the uniform pre-interchange estimate
  $$
  \mathbb E F_u(x)^2\le e^{D^2u}.
  $$
  Consequently, for each finite $T$,
  $$
  \mathbb E\int_0^T\int_{\partial^*E}
  |F_u(x)(x-a_u)|^2\,d\sigma_0(x)\,du<\infty.
  $$
  Since $\sigma_0$ is finite, Cauchy--Schwarz also gives
  $$
  \mathbb E\int_0^T
  \left|\int_{\partial^*E}F_u(x)(x-a_u)\,d\sigma_0(x)\right|^2du<\infty.
  $$
  These bounds are established before integration of the pointwise stochastic integral.  They are
  the required product-space and integrated-coefficient hypotheses for stochastic Fubini, which
  yields the displayed driftless surface SDE with no circular appeal to that SDE.

- For each fixed boundary point, the stochastic-exponential integrand $x-a_u$ is bounded by $D$.
  Novikov holds on every bounded interval; equivalently, the stopped $L^2$ bounds are uniformly
  integrable.  Thus every canonical $F_t(x)$ is a true martingale on finite intervals.  Conditional
  Tonelli applied to the nonnegative surface representation then gives
  $$
  \mathbb E[P_t(E)\mid\mathcal F_s]
  =\int\mathbb E[F_t(x)\mid\mathcal F_s],d\sigma_0(x)
  =P_s(E).
  $$
  This equality is not used or claimed outside the smooth compact-support/tubular class.

### Integrated excess and exact identity

For `prop:trivial-excess`, $0\le e_t(E)\le P_t(E)$ holds because the profile is nonnegative and
$E$ is an admissible exact-mass competitor.  Tonelli and the deterministic-time consequence of the
perimeter supermartingale give
$$
\mathbb E\int_0^{T\wedge\tau}e_t(E)\,dt
\le TP_0(E).
$$
This uses only the indicator of $\{t<\tau\}$; no optional-stopping theorem and no independence of
$\tau$ is used.

For the constant, a coordinate marginal of an isotropic log-concave law is a one-dimensional
log-concave law of variance one.  A median halfspace is balanced and has lower Minkowski perimeter
$f(m)$.  Bobkov's published 1999 *Annals of Probability* paper, Proposition 4.1 and equation (4.2),
gives $\operatorname{Is}(\nu)=2f(m)$ and
$\operatorname{Is}(\nu)^2\le2/\operatorname{Var}_\nu(X)$; hence $f(m)\le1/\sqrt2<1$.  The checked
primary source is [Bobkov's paper](https://www-users.cse.umn.edu/~bobko001/papers/1999_AOP_Isop.pdf),
and the repository DOI `10.1214/aop/1022874820` is correct.  This is a published result, not an
unreviewed preprint.  Therefore $P_0(E)=I_\mu(1/2)+e_0\le1+e_0$.

For `lem:excess-identity`, $0\le I_{\mu_t}(p_t)\le P_t(E)$ makes the profile term integrable.  In
the smooth class just checked, $\mathbb EP_t(E)=P_0(E)$, so direct substitution gives
$$
\mathbb Ee_t(E)=e_0(E)+I_\mu(p_0)-\mathbb EI_{\mu_t}(p_t).
$$
The proof correctly notes that the general-support argument would give only an inequality and does
not use it for this identity.

### Fixed competitor families and the moving-profile warning

For a fixed nonempty countable family, $J_t\le P_t(S)$ for every $S$.  Conditional expectation and
the fixed-cut result give
$$
\mathbb E[J_t\mid\mathcal F_s]
\le\mathbb E[P_t(S)\mid\mathcal F_s]
\le P_s(S).
$$
Countability supplies a common null set before infimizing the right side.  Choosing one
$S_\star$ supplies $0\le J_t\le P_t(S_\star)$ and hence integrability.  The larger-family variant
is valid because the process is explicitly defined by a fixed countable determining subfamily;
the dossier does not use an uncountable intersection of full-probability sets.

On $\{t<\tau_\eta\}$, the exact-$p_t$ competitor family is contained in the mass-window family, so
the direction $I_{\mu_t}(p_t)\ge J_t(\eta)$ is correct.  Eligibility in the latter family depends
on $(t,\omega)$, and the proof explicitly refuses to apply the fixed-family conditional-expectation
argument to it.

### Consumption audit and the `lem:half` contradiction

The antecedent in part 2 is exactly the full unweighted replacement of the stable Stein-trace
estimate in `modules/kls/20-eldan-statements.tex:117`--`150`: one universal $T_0$, fixed universal
window, universal constants, every eligible initial cut, and every $T\le T_0$.  For
$0<\eta\le1/6$, the certified Stein/source conversion applies, and the unconditional excess bound
for $e_0\le1$ gives
$$
\mathbb E\int_0^{T\wedge\tau_\eta}S_t\,dt
\le(2C_0+4C_2)T
 +2C_1\mathbb E\int_0^{T\wedge\tau_\eta}r_t\,dt
 +(2\beta+64\eta^2)\mathbb E\int_0^{T\wedge\tau_\eta}D_t\,dt.
$$
The coefficient of the damping term is strictly below one by the stated margin, exactly matching
the hypothesis of `cor:tight-window-consumption`.

The final contradiction is now explicit and complete.  If KLS failed, there would be isotropic
log-concave $\mu_k$ with $h_{\mu_k}\to0$.  The proved dependency `lem:half` gives
$I_{\mu_k}(1/2)=h_{\mu_k}/2\to0$.  By the definition of the profile, choose balanced finite-perimeter
cuts $E_k$ with
$P_0(E_k)\le I_{\mu_k}(1/2)+o(1)$.  Then $P_0(E_k)\to0$ and
$0\le e_0(E_k)\to0$, so eventually $e_0(E_k)\le1$ and the universal unweighted antecedent applies.
The absorptive estimate and tight-window consumption give a universal positive lower bound for
those same $P_0(E_k)$, a contradiction.  Part 3 uses the certified two-tail family only to refute
the universal one-time-slice inequality of the displayed absolute-excess form; it makes no claim
against time-nonlocal or covariance-weighted proofs.

### Hypothesis accounting

- The general perimeter result uses a fixed Borel cut, finite initial lower outer Minkowski
  perimeter, and the bounded-test localization martingale identity.  Isotropy and log-concavity are
  not used in this measure-theoretic subargument beyond the ambient localization setup.
- The true perimeter equality and exact excess identity additionally use a smooth compactly
  supported initial density, the canonical pointwise localization density, a $C^2$ boundary with a
  tubular neighborhood over the support, and finite time.  These hypotheses are all stated.
- The integrated excess bound uses log-concavity, half mass, unit coordinate variance from
  isotropy, finite initial perimeter, and the perimeter supermartingale.  The mean-zero part of
  isotropy and the stopping-time property beyond measurability of the random-horizon indicator are
  unused; these are harmless sharpening opportunities.
- The infimum result uses fixedness, nonemptiness, countability, and finite initial perimeter for
  every member.  The determining-family extension uses the explicitly stated fixed countable
  subfamily.  No selector or raw uncountable null-set intersection is hidden.
- The consumption implication uses the universal quantifiers and strict absorption margin of its
  antecedent, $e_0\le1$ only for the near-minimizing cuts, and the five declared dependencies.
  The antecedent is not asserted to be proved.

No hypothesis used by the proof is absent from the synchronized statement package.  The unused
hypotheses just listed are opportunities to generalize, not defects in the stated conclusions.

### Dependency closure, citations, and fences

The direct dependencies are recorded exactly.  Their closure runs through
`prop:trivial-excess`, `lem:perimeter-martingale`, `prop:two-tail`, `lem:stein-vs-source`,
`cor:tight-window-consumption`, `lem:half`, `prop:stein-rep`, `thm:scalar-riccati`,
`lem:matrix-riccati`, and `lem:survival-implies-kls`.  Every node in that closure is currently
`proved` with agent-certified dossier provenance.  No `conditional`, open, refuted, imported
`preprint-unreviewed`, or numerical premise occurs in the closure.  This review relies on the
active certifications for the dependency dossiers but does not recertify them.

The only direct external citation in the reviewed dossier is the published Bobkov result checked
above.  The localization mass and density SDEs are part of the synchronized repository setup and
their uses here can also be derived directly from the canonical exponential density.  Standard
conditional monotone convergence, the smooth tube calculation, Ito/Gronwall, Novikov, and
stochastic Fubini were checked at their points of use rather than treated as numerical evidence.

None of the five ledger nodes has a `bounded_by` edge.  The two relevant nearby fences are still
respected:

- `rem:profile-circularity`: exact perimeter equality is confined to the smooth compact-support class, and
  no fixed-family supermartingale argument is transferred to the random mass-constrained profile.
- `rem:two-tail-slice-bounds`: the construction is used only against the universal slice-wise unweighted
  inequality of the asserted form, not against a time-nonlocal proof or the weighted package.

## Corrections

None.  All defects listed in the followed-up audit are repaired in the frozen dossier and
synchronized statement package.

## Validation

- `cd solutions && latexmk -pdf -g -outdir=../build kls-excess-audit.tex`: exit code 0; only the
  expected standalone cross-manuscript references remain unresolved.
- Standalone builds of `modules/kls/10-notation.tex`, `modules/kls/20-eldan-statements.tex`, and
  `modules/kls/24-excess-propagation.tex`: exit code 0 in separate `/tmp` output directories; only
  expected cross-module reference warnings remain.
- `latexmk -pdf -g -outdir=build main.tex`: exit code 0; the synchronized modules were typeset in
  the 157-page manuscript.
- `python3 research/check_ledger.py`: 0 structural errors on 189 nodes before this report was
  appended.  It was rerun after the append as recorded below.

## Proposed active-review delta

All premises are discharged, so each of the five nodes may retain `status: proved`.  For each node,
replace the historical active review pointer by:

```yaml
status: proved
solution: solutions/kls-excess-audit.tex
checked_by: agent
review: research/reviews/2026-08-27-kls-excess-repair-w0r2-proof-review.md
```

Apply this block to `prop:intro-audit`, `prop:trivial-excess`, `lem:perimeter-martingale`,
`lem:excess-identity`, and `lem:inf-martingales`; leave their current statements, labels, routes,
dependency edges, and absent `bounded_by` fields unchanged.  The 2026-08-25 review and the
2026-08-27 failed audit remain append-only historical records.

## Exclusions

This review does not certify KLS, the truth of the unweighted Stein-trace antecedent, the weighted
geometric package, weighted excess propagation, any supermartingale property for the moving
balanced-profile infimum, a raw uncountable pointwise infimum, or true-martingale equality for a
rough or noncompact cut.  It does not recertify the dependency dossiers, `lem:half`, any bootstrap
node, any numerical artifact, or the rest of the manuscript merely because the full build passed.

```yaml
outcome: complete
artifacts:
  - research/reviews/2026-08-27-kls-excess-repair-w0r2-proof-review.md
proposed_deltas:
  - "For prop:intro-audit, prop:trivial-excess, lem:perimeter-martingale, lem:excess-identity, and lem:inf-martingales, retain status: proved and solution: solutions/kls-excess-audit.tex, set checked_by: agent, and set review: research/reviews/2026-08-27-kls-excess-repair-w0r2-proof-review.md; preserve every statement and graph edge."
next_role: orchestrator
next_prompt: |
  Atomically update the active review pointer for prop:intro-audit, prop:trivial-excess,
  lem:perimeter-martingale, lem:excess-identity, and lem:inf-martingales to
  research/reviews/2026-08-27-kls-excess-repair-w0r2-proof-review.md.  Retain status: proved,
  solution: solutions/kls-excess-audit.tex, checked_by: agent, and every current statement,
  dependency edge, route, and absent bounded_by field.  Preserve all prior reports as history and
  run python3 research/check_ledger.py after the atomic ledger update.
```
