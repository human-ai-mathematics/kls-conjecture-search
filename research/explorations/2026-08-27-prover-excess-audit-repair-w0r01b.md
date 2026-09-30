---
---
# Excess-audit dossier repair W0R01b

Date: 2026-08-27  
Role: prover (/root/repair_excess_dossier)  
Artifact: solutions/kls-excess-audit.tex  
Artifact SHA-256: 2b7621ec14eb26db23a0266fac06c693733a87e45345374daf5fe3418e2e7cae  
Repair contract: research/reviews/2026-08-27-kls-excess-repair-w0-audit.md

## Scope and certification state

This is the second repair of the dossier covering prop:intro-audit,
prop:trivial-excess, lem:perimeter-martingale, lem:excess-identity, and
lem:inf-martingales. The fresh cold audit was treated as the complete correction contract.

The dossier remains checked_by: none. The 2026-08-25 review is retained only as historical
provenance and does not certify the repaired source. No review, manuscript, ledger, route, or
bibliography file was edited by this prover.

## Perimeter convention

The dossier now works in the manuscript's lower outer Minkowski convention. For a Borel set
$E$, let

$$
E_r=\{x:\operatorname{dist}(x,E)<r\},
\qquad
P_t(E)=\mu_t^+(E)
=\liminf_{r\downarrow0}\frac{\mu_t(E_r)-\mu_t(E)}r.
$$

Two statements are kept separate.

1. For an arbitrary Borel $E$ with $P_0(E)<\infty$, the process $P_t(E)$ is an integrable
   nonnegative supermartingale, without any support or boundary regularity assumption.
2. True-martingale equality and the driftless surface SDE are asserted only when the initial
   density is smooth and compactly supported and $E$ has a $C^2$ boundary with a tubular
   neighborhood over that support.

The second clause is not claimed for an arbitrary rough finite-perimeter cut. Compact support
alone does not turn a raw lower Minkowski liminf into a surface integral.

## General Minkowski supermartingale

For positive rational $q$, define

$$
X_{q,t}
=\frac{\mu_t(E_q)-\mu_t(E)}q
=\frac{\mu_t(E_q\setminus E)}q.
$$

The bounded-test localization identity makes each $X_q$ a bounded nonnegative true martingale.
For $n\ge1$, set

$$
Y_{n,t}
=\inf\{X_{q,t}:q\in\mathbb Q,\ 0<q<1/n\}.
$$

This is a countable fixed infimum. For every admissible $q$,

$$
\mathbb E[Y_{n,t}\mid\mathcal F_s]
\leq\mathbb E[X_{q,t}\mid\mathcal F_s]
=X_{q,s}.
$$

Countability supplies one common null set, so infimizing gives

$$
\mathbb E[Y_{n,t}\mid\mathcal F_s]\leq Y_{n,s}.
$$

Each $Y_{n,t}$ is integrable because it is bounded above by any one admissible $X_{q,t}$.
For any probability measure $\nu$, continuity from below gives

$$
q_k\uparrow r
\quad\Longrightarrow\quad
\nu(E_{q_k}\setminus E)\uparrow\nu(E_r\setminus E).
$$

Thus rational radii determine the same infimum as all real radii, and

$$
Y_{n,t}\uparrow P_t(E).
$$

Ordinary monotone convergence yields

$$
\mathbb E P_t(E)
=\lim_n\mathbb E Y_{n,t}
\leq\lim_nY_{n,0}
=P_0(E)<\infty.
$$

Conditional monotone convergence then gives the full process inequality

$$
\mathbb E[P_t(E)\mid\mathcal F_s]\leq P_s(E).
$$

This directly covers arbitrary support and arbitrary Borel cuts of finite initial lower
Minkowski perimeter. It replaces the rejected attempt to pass from a smooth reduced-boundary
formula to a rough Minkowski boundary by an unspecified approximation.

## Compact smooth equality and stochastic Fubini

In the compact-support smooth class, the one-sided tube formula identifies the same Minkowski
perimeter with

$$
P_t(E)=\int_{\partial^*E}F_t\,d\sigma_0,
\qquad
d\sigma_t=F_t\,d\sigma_0.
$$

If $K$ contains the support and $D=\operatorname{diam}K$, then
$|x-a_u|\le D$ for $\sigma_0$-almost every boundary point. After localizing the pointwise
density SDE, Itô and Gronwall give

$$
\mathbb E F_u(x)^2\le e^{D^2u}.
$$

Consequently, for finite $T$,

$$
\mathbb E\int_0^T\int_{\partial^*E}
  |F_u(x)(x-a_u)|^2\,d\sigma_0(x)\,du
\le
D^2\sigma_0(\partial^*E)\int_0^T e^{D^2u}\,du
<\infty.
$$

Since $\sigma_0$ is finite, Cauchy--Schwarz also makes the already-integrated stochastic
coefficient square-integrable in boundary time. These are genuine pre-interchange hypotheses
for stochastic Fubini, which now yields the driftless perimeter SDE. Novikov, or the same
$L^2$ bound, makes every fixed-$x$ density a true martingale; conditional Tonelli then gives
$\mathbb E[P_t(E)\mid\mathcal F_s]=P_s(E)$ in exactly this regular class.

The earlier perimeter-level stopping estimate was discarded because it bounded the candidate
coefficient only after interchange and therefore did not itself justify stochastic Fubini.

## Fixed competitor families

The false extension from a countable family to an arbitrary measurable uncountable family was
removed. The dossier proves the supermartingale conclusion for:

- a fixed nonempty countable family of Borel sets of finite initial lower Minkowski perimeter;
- a prescribed larger family only when it has a fixed countable determining subfamily whose
  pointwise infimum agrees almost surely at every time under consideration.

The proof uses

$$
\mathbb E[J_t\mid\mathcal F_s]
\leq\mathbb E[P_t(S)\mid\mathcal F_s]
\leq P_s(S)
$$

for every member of the countable family, followed by its infimum. Nonemptiness gives the
integrable upper bound $J_t\le P_t(S_\star)$. Mere measurability of a raw uncountable pointwise
infimum is explicitly declared insufficient.

The windowed exact-mass family remains random and time-dependent. Only its pathwise order
relative to the isoperimetric profile is used; no supermartingale conclusion is drawn for it.

## Bobkov input and dependency audit

The imprecise attribution of $\|f\|_\infty\le1$ was replaced by the exact checked input from
Bobkov, Proposition 4.1 and equation (4.2). If $\nu$ is the variance-one coordinate marginal
with density $f$ and median $m$, then

$$
\operatorname{Is}(\nu)=2f(m),
\qquad
\operatorname{Is}(\nu)^2
\le\frac2{\operatorname{Var}_\nu(X)},
$$

so $f(m)\le1/\sqrt2<1$. This is exactly what prop:trivial-excess needs.

During this repair cycle, the orchestrator applied the following central deltas:

- prop:trivial-excess now depends_on lem:perimeter-martingale and records its isotropic,
  log-concave, half-mass, finite-perimeter hypotheses;
- prop:intro-audit now depends_on lem:half;
- lem:inf-martingales now uses the countable/countably-determined convention and rejects mere
  uncountable measurability;
- Bobkov1999LogConcave now carries DOI 10.1214/aop/1022874820.

The dossier header agrees with both dependency edges, and the consumption proof cites
lem:half at the balanced-near-minimizer step.

## Exact remaining statement synchronization

The dossier proves a broader arbitrary-support inequality but a narrower equality/SDE than the
current short labels suggest. The orchestrator should use the following exact ledger
replacement statements after a successful fresh proof review.

For lem:perimeter-martingale:

~~~yaml
statement: "For every Borel cut E with finite initial lower outer Minkowski perimeter, the fixed-cut perimeter process is an integrable nonnegative supermartingale: E[P_t(E)|F_s] <= P_s(E). If the initial density is smooth and compactly supported and E has a C^2 boundary with a tubular neighborhood over the support, the same lower Minkowski perimeter equals weighted surface area, is a true martingale, and satisfies the displayed driftless surface SDE."
~~~

For lem:excess-identity:

~~~yaml
statement: "Under the compact-support smooth-density and C^2 tubular-boundary hypotheses of lem:perimeter-martingale, E e_t(E) = e_0(E) + I_mu(p_0) - E I_{mu_t}(p_t) for every finite t. No exact noncompact or arbitrary-rough-set identity is asserted."
~~~

The remaining module-24 synchronization is:

1. Replace the labeled perimeter lemma by the same two-clause statement: arbitrary Borel
   finite-initial-Minkowski supermartingale inequality, and true martingale/SDE only in the
   compact smooth density plus $C^2$ tubular-boundary class.
2. Replace its proof by the rational boundary-layer construction for the first clause and the
   tube formula plus the displayed $L^2$ stochastic-Fubini estimate for the second.
3. Qualify the exact excess-identity lemma by the same compact smooth regularity hypotheses.
4. State finite lower Minkowski perimeter in prop:trivial-excess and replace its supremum-density
   sentence by Bobkov's median estimate $f(m)\le1/\sqrt2$.
5. In the proof of prop:intro-audit, cite lem:half for
   $h_\nu=2I_\nu(1/2)$ and balanced near-minimizers.

The countable-family statement and proof have already been synchronized centrally and require no
further patch from this repair.

## Other four-node audit

- prop:trivial-excess uses only $0\le e_t(E)\le P_t(E)$, deterministic-time perimeter
  supermartingale control, Tonelli, isotropy through a variance-one marginal, half mass, and
  Bobkov's published median estimate. It does not use optional stopping.
- lem:excess-identity uses true perimeter equality only in the explicitly regular compact class.
- lem:inf-martingales now has nonemptiness, measurability through countability, integrability,
  and the correct two-inequality argument.
- prop:intro-audit retains the coefficients $(2C_0+4C_2)$, $2C_1$, and
  $2\beta+64\eta^2<1$. It uses only proved dependencies and treats the unweighted estimate as
  the antecedent of an implication.

No hidden open, conditional, refuted, or preprint-unreviewed premise enters these proofs.

## Fences and status

The five nodes have no ledger bounded_by edges. The proof nevertheless respects rem:profile-circularity:
it does not infer monotonicity for the random balanced-profile family and uses perimeter equality
only in the explicit regular compact class. The two-tail input is used only to refute the
one-time-slice unweighted estimate, not time-nonlocal or covariance-weighted approaches.

No numerical evidence appears. No mathematical step is left open in the dossier under its stated
hypotheses. The arbitrary rough-set result is deliberately the supermartingale inequality only;
claiming rough compact-support equality would require a separate perimeter-identification theorem
and is not part of this candidate.

## Validation

The command

~~~bash
cd solutions
latexmk -pdf -outdir=../build kls-excess-audit.tex
~~~

completed with exit code zero and produced build/kls-excess-audit.pdf. The final log contains no
TeX error, undefined control sequence, emergency stop, or fatal error. Remaining warnings are
the expected unresolved cross-manuscript references of a standalone subfile and an empty
standalone citation destination.

The structural command

~~~bash
python3 research/check_ledger.py
~~~

also completed with exit code zero: 2 ledgers, 185 nodes, 652 labels, 0 errors.

The candidate path for future certification is solutions/kls-excess-audit.tex. It has no ledger
value while checked_by remains none and requires a fresh distinct proof checker.
