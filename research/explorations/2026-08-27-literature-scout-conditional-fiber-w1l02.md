---
type: exploration
date: "2026-08-27"
outcome: proposed
nodes:
  - conj:kls
---
# Literature scout: conditional-fiber frames and simplex exchange gaps

Date: 2026-08-27

Role: `literature-scout`

Run id: `w1l02`

Write scope: this append-only exploration only

No numerical evidence is used. No ledger, bibliography, manuscript, route-control, dossier,
review, or knowledge file is changed.

## Decisive outcome

The nearby published exchange literature does **not** resolve the existential conditional-fiber
frame target. It does, however, contain direct prior art for the failure of the natural simplex
root frame.

More precisely, Sasada's published 2015 paper proves, by the same vertex-cap mechanism, that a
complete-graph simplex heat bath with pair rate $(\eta_i+\eta_j)^s$ has no dimension-free gap for
any negative exponent $s$. In the exact normalization of the conditional-fiber probe, her bound
at $s=-2$ gives

$$
 \operatorname{gap}(\mathcal D_{\mathrm{root}})
 \le \frac{48}{m(m+1)}=O(m^{-2}).
 \tag{1}
$$

Thus the conclusion that the $A_{m-1}$ root frame has gap $O(m^{-2})$ is not only supported by
the repository's independent analytic cap calculation; its underlying negative-rate exchange
obstruction is published prior art. The exact fixed-$\varepsilon$ cap formula in the route probe
is still a repository statement, not a quotation from Sasada.

Caputo proves the exact positive gap of the unweighted flat-simplex heat bath. Carlen--Posta--Toth
prove a dimension-free gap for the positively weighted rates $(\eta_i+\eta_j)^s$ when
$s\in[0,1]$. These results meet precisely at the sign boundary relevant here: they cover
$s\ge0$, whereas the root form has $s=-2$. Sasada's cap shows that extending their conclusion
to negative $s$ would be false.

No source found in this search chooses an arbitrary even isotropic tight frame of directions, or
proves or refutes a dimension-free gap after optimizing over all such frames. Therefore the
existential all-frame simplex quantity remains unresolved:

$$
 \sup_{\rho:\ (m-1)\int\theta\theta^T\,d\rho=I}
 \operatorname{gap}(\mathcal D_{\mu_m,\rho}).
 \tag{2}
$$

The root-frame obstruction cannot be promoted to an all-frame obstruction.

## Exact search target

Let

$$
 \Delta_{m-1}=\{p\in\mathbb R_+^m:\textstyle\sum_i p_i=1\},
 \qquad \eta_i=mp_i,
 \qquad \sum_i\eta_i=m,
 \tag{3}
$$

with the flat Dirichlet law $\operatorname{Dir}(1,\ldots,1)$. For $i<j$, let
$\operatorname{Var}_{ij}(f)$ mean conditional variance after fixing all coordinates other than
$i,j$, equivalently after uniformly redistributing the conserved sum $\eta_i+\eta_j$.

The exact questions searched were:

1. Does the complete-graph pair-refresh form
   $$
    \frac1m\sum_{i<j}
    \mathbb E\big[(\eta_i+\eta_j)^s\operatorname{Var}_{ij}(f)\big]
    \tag{4}
   $$
   have a dimension-free gap for $s=0$, for $s\ge0$, or for $s=-2$?
2. Can a published theorem be converted exactly to the root-frame form
   $$
    \mathcal D_{\mathrm{root}}(f)
    =\frac{12}{m+1}\sum_{i<j}
      \mathbb E\big[(\eta_i+\eta_j)^{-2}
      \operatorname{Var}_{ij}(f)\big]?
    \tag{5}
   $$
3. Does any source decide the stronger order of quantifiers
   $$
    \forall\mu\ \exists\rho_\mu\ \forall f
   \tag{6}
   $$
   for an even isotropic tight frame $\rho_\mu$ and inverse-conditional-variance line
   resampling?

We also searched weaker and stronger neighbors: uniform pair refresh, nonnegative power rates,
general symmetric Dirichlet laws, arbitrary-direction hit-and-run, and frame-based conditional
variance estimates.

## Normalization dictionary

To avoid collision between the simplex size and the exponent, write $m$ for the number of
coordinates and $s$ for a pair-rate exponent. Define Sasada's complete-graph form at mean energy
one by

$$
 \mathcal E^{\mathrm{Sa}}_{s,m}(f)
 :=\frac1m\sum_{i<j}
 \mathbb E\big[(\eta_i+\eta_j)^s\operatorname{Var}_{ij}(f)\big].
 \tag{7}
$$

Define the Carlen--Posta--Toth normalization by

$$
 \mathcal E^{\mathrm{CPT}}_{s,m}(f)
 :=\frac{m}{\binom m2}\sum_{i<j}
 \mathbb E\big[(\eta_i+\eta_j)^s\operatorname{Var}_{ij}(f)\big].
 \tag{8}
$$

Then

$$
 \mathcal E^{\mathrm{CPT}}_{s,m}
 =\frac{2m}{m-1}\mathcal E^{\mathrm{Sa}}_{s,m}.
 \tag{9}
$$

The root-frame calculation in the route probe gives

$$
 \mathcal D_{\mathrm{root}}
 =\frac{12m}{m+1}\mathcal E^{\mathrm{Sa}}_{-2,m}
 =6\frac{m-1}{m+1}\mathcal E^{\mathrm{CPT}}_{-2,m}.
 \tag{10}
$$

All conversions below use (7)--(10); no constants are suppressed.

## Found 1: Caputo's exact flat-simplex heat-bath gap

**Citation and class.** Pietro Caputo, *On the spectral gap of the Kac walk and other binary
collision processes*, ALEA 4 (2008), 205--222. `import_class: published`.

- Published primary source:
  <https://alea.math.cnrs.fr/articles/v4/04-10.pdf>
- arXiv source read: <https://arxiv.org/pdf/0807.3415>, version 1, 22 July 2008.
- Proof status in this scout: Section 2.2, the generator normalization, the three-component
  calculation, the spectral computation of the one-coordinate conditional operator, and the
  exact-gap conclusion were read in the primary paper.

### Exact source statement

On the flat simplex $\{\eta\ge0:\sum_i\eta_i=\omega\}$, Caputo uses

$$
 Lf=\frac1m\sum_{i<j}(P_{ij}f-f),
 \tag{11}
$$

where $P_{ij}$ is conditional expectation given all coordinates outside the pair. His equation
(2.7) is

$$
 \operatorname{gap}(-L)=\frac{m+1}{3m},\qquad m>2,
 \tag{12}
$$

independently of the total energy $\omega$. The proof identifies the $m=3$ gap $4/9$, with
$\sum_i\eta_i^2$ as a gap eigenfunction, and applies the complete-graph reduction.

### Local conversion

For the flat Dirichlet law, the Dirichlet form of (11) is exactly
$\mathcal E^{\mathrm{Sa}}_{0,m}$. Thus (12) is already in the normalization (7):

$$
 \operatorname{gap}(\mathcal E^{\mathrm{Sa}}_{0,m})
 =\frac{m+1}{3m}.
 \tag{13}
$$

Using (9),

$$
 \operatorname{gap}(\mathcal E^{\mathrm{CPT}}_{0,m})
 =\frac{2(m+1)}{3(m-1)}.
 \tag{14}
$$

This proves that the pair directions themselves are not the obstruction: with constant pair
rates, the same complete-graph root updates have a universal gap.

### What it does not give

Caputo inserts no factor $(\eta_i+\eta_j)^{-2}$. Equation (13) therefore cannot be transferred to
(5). It also fixes the coordinate-pair/root orbit and does not optimize over direction frames.

## Found 2: Sasada's published negative-exponent cap obstruction

**Citation and class.** Makiko Sasada, *Spectral gap for stochastic energy exchange model with
nonuniformly positive rate function*, Annals of Probability 43(4) (2015), 1663--1711,
doi:10.1214/14-AOP916. `import_class: published`.

- Published primary source:
  <https://doi.org/10.1214/14-AOP916>
- Journal reprint read at arXiv: <https://arxiv.org/pdf/1305.4066>, version 3,
  9 September 2015. The reprint identifies itself as the published article.
- Proof status in this scout: the invariant conditional Gamma/Dirichlet law, the complete-graph
  generator and Dirichlet-form definitions, and the complete proof of Remark 2.4 were read.

### Exact source statement

Sasada uses a shape parameter $a>0$ (denoted $\gamma$ in her paper) and the symmetric
Dirichlet law obtained by conditioning independent Gamma variables on
$m^{-1}\sum_i\eta_i=1$. For a pair-rate exponent $s<0$ (denoted $m$ in her paper), her
long-range form is exactly (7), with the conditional pair redistribution distributed as
$\operatorname{Beta}(a,a)$.

Remark 2.4 takes

$$
 f_m(\eta)=\mathbf1_{\{\eta_1>m/2\}}
 \tag{15}
$$

and proves

$$
 \operatorname{gap}(\mathcal E^{\mathrm{Sa},a}_{s,m})
 \le 2^{-s}m^s,
 \qquad a>0,\ s<0.
 \tag{16}
$$

The mechanism is exact: only the $m-1$ pairs involving coordinate $1$ can change (15), and on a
fiber where its conditional variance is nonzero one has $\eta_1+\eta_j>m/2$. Since $s<0$,
the rate there is at most $(m/2)^s$.

### Local conversion and the root-frame constant

At $a=1$, the invariant law and pair redistribution are the flat simplex and uniform pair refresh
used in the route probe. At $s=-2$, (16) gives

$$
 \operatorname{gap}(\mathcal E^{\mathrm{Sa}}_{-2,m})\le\frac4{m^2}.
 \tag{17}
$$

Multiplying by the exact factor in (10) yields

$$
 \boxed{
 \operatorname{gap}(\mathcal D_{\mathrm{root}})
 \le \frac{12m}{m+1}\frac4{m^2}
 =\frac{48}{m(m+1)}.}
 \tag{18}
$$

This is a published-source route to the $O(m^{-2})$ root-frame obstruction. It is quantitatively
stronger than the convenient $96/m^2$ corollary in the route probe, although the two use slightly
different vertex caps.

### Fence check and collision audit

There is no collision with a repository obstruction. Sasada's result agrees with the analytic
vertex-cap fence in
`research/explorations/2026-08-27-kls-route-prober-conditional-fiber-frame-w1f01.md`.
It strengthens the provenance classification of the underlying mechanism from "new analytic
observation" to "independently derived analytic observation with published prior art."

It does not certify the repository's exact fixed-$\varepsilon$ formula, and it does not replace a
prover/reviewer cycle for any repository-authored structural dossier.

### What it does not give

Sasada's form uses only the complete graph of coordinate-pair/root updates. It does not consider a
probability $\rho$ over arbitrary directions, the tight-frame constraint, the supremum over such
frames, or a continuum of direction orbits. Her cap therefore refutes the root orbit only.

## Found 3: Carlen--Posta--Toth for nonnegative pair exponents

**Citation and class.** Eric A. Carlen, Gustavo Posta, and Imre P\'eter T\'oth, *Spectral gap for
the stochastic exchange model*, Stochastic Processes and their Applications 190 (2025), article
104769, doi:10.1016/j.spa.2025.104769. `import_class: published`.

- Published source and metadata:
  <https://doi.org/10.1016/j.spa.2025.104769>
- arXiv source read: <https://arxiv.org/pdf/2504.13533>, version 2, 17 July 2025;
  manuscript date 18 July 2025.
- Proof status in this scout: the model and form definitions, scaling lemma, Theorem 1.3, the
  induction inequality, and the final summable-product closure were read. The long sequence of
  technical correlation estimates was not independently re-proved in this scout.

### Exact source statement

On $\sum_i\eta_i=m$ with the uniform simplex law, their Dirichlet form is exactly (8). Their
Theorem 1.3 states that for every fixed $s\in[0,1]$ there exists $c_s>0$, independent of the
number of particles $m\ge2$, such that

$$
 \operatorname{gap}(\mathcal E^{\mathrm{CPT}}_{s,m})\ge c_s.
 \tag{19}
$$

At general mean energy $E$, their Lemma 1.1 gives the exact scaling $E^s$. For two particles the
gap is exactly $2^{1+s}$ in their normalization.

### Local conversion

The form (19) is the exchange family appearing in the route probe, but the root frame is the
member with exponent $s=-2$, outside the theorem. Formally, (10) identifies the precise missing
extension:

$$
 s\in[0,1]\quad\hbox{is published and uniformly gapped};
 \qquad s=-2\quad\hbox{has gap at most }\frac8{m(m-1)}
 \tag{20}
$$

in the CPT normalization, where the upper bound follows from (9) and (17). Hence a sign-blind
extension of (19) is impossible.

### Where the proof stops relative to the route

The CPT induction exploits nonnegative power rates and controlled correlations of simplex
coordinates. It preserves the coordinate-pair update graph. It neither constructs an arbitrary
tight frame nor supplies a comparison between a general directional conditional-line form and
one of its pair-refresh models. The result is a sharp neighboring theorem, not a discharge of
(2).

## The exact unresolved all-frame problem

For the isotropic uniform simplex in $H_0=\mathbf1^\perp$, let

$$
 \mathfrak F_{m-1}
 =\left\{\rho:\rho\text{ even on }S(H_0),\quad
 (m-1)\int\theta\theta^T\,d\rho(\theta)=I_{H_0}\right\}.
 \tag{21}
$$

The literature checked here leaves both directions below open:

$$
 \inf_m\sup_{\rho\in\mathfrak F_{m-1}}
 \operatorname{gap}(\mathcal D_{\mu_m,\rho})>0,
 \tag{22}
$$

or

$$
 \sup_{\rho\in\mathfrak F_{m-1}}
 \operatorname{gap}(\mathcal D_{\mu_m,\rho})\longrightarrow0.
 \tag{23}
$$

The published results establish only that one admissible point
$\rho_{\mathrm{root}}\in\mathfrak F_{m-1}$ has gap $O(m^{-2})$. Because (22) is a supremum over
frames, this is not evidence for (23) without an upper certificate uniform over every admissible
$\rho$.

In particular, permutation symmetrization does not reduce all invariant frames to the root orbit;
it still permits mixtures of continuously many permutation orbits. No source found supplies the
all-frame min--max or its dual certificate.

## Proposed imported node

One imported obstruction is mathematically justified by a proof read in a published primary
source. It is proposed only after the orchestrator creates an appropriate manuscript anchor; the
current ledger has no admitted `conditional-fiber-frame` route or manuscript file containing this
label, so **no immediate ledger edit is structurally applicable**.

```yaml
- id: imp:sasada-negative-exchange-obstruction
  kind: obstruction
  status: imported
  route: shared
  file: modules/kls/XX-conditional-fiber-frame.tex
  statement: "For every symmetric-Dirichlet shape a>0, every negative pair-rate exponent s<0, and every m>=2, on the simplex sum_i eta_i=m the complete-graph heat-bath form m^(-1) sum_(i<j) E[(eta_i+eta_j)^s Var_ij(f)] has spectral gap at most 2^(-s)m^s. In particular, for the flat simplex and s=-2, the A_(m-1) root conditional-fiber form has gap at most 48/[m(m+1)]."
  import_class: published
  references: [Sasada2015EnergyExchange]
```

Caputo's and Carlen--Posta--Toth's results are exact and relevant, but no separate imported nodes
are proposed: they are comparison neighbors rather than dependencies of a live route. Their
bibliography entries are nevertheless worth accepting if the comparison paragraph is promoted to
the manuscript.

## Exact bibliography proposals

These keys do not currently occur in `fi_references.bib`. The orchestrator should deduplicate and
append accepted entries atomically.

```bibtex
@article{Caputo2008BinaryCollision,
  author        = {Caputo, Pietro},
  title         = {On the Spectral Gap of the {Kac} Walk and Other Binary Collision Processes},
  journal       = {ALEA. Latin American Journal of Probability and Mathematical Statistics},
  volume        = {4},
  pages         = {205--222},
  year          = {2008},
  eprint        = {0807.3415},
  archivePrefix = {arXiv},
  primaryClass  = {math.PR},
  url           = {https://alea.math.cnrs.fr/articles/v4/04-10.pdf}
}

@article{Sasada2015EnergyExchange,
  author        = {Sasada, Makiko},
  title         = {Spectral Gap for Stochastic Energy Exchange Model with Nonuniformly Positive Rate Function},
  journal       = {Annals of Probability},
  volume        = {43},
  number        = {4},
  pages         = {1663--1711},
  year          = {2015},
  doi           = {10.1214/14-AOP916},
  eprint        = {1305.4066},
  archivePrefix = {arXiv},
  primaryClass  = {math.PR}
}

@article{CarlenPostaToth2025Exchange,
  author        = {Carlen, Eric A. and Posta, Gustavo and T{\H{o}}th, Imre P{\'e}ter},
  title         = {Spectral Gap for the Stochastic Exchange Model},
  journal       = {Stochastic Processes and their Applications},
  volume        = {190},
  pages         = {104769},
  year          = {2025},
  doi           = {10.1016/j.spa.2025.104769},
  eprint        = {2504.13533},
  archivePrefix = {arXiv},
  primaryClass  = {math.PR}
}
```

## Citation debt

1. The route probe's statement that the weighted exchange literature covers nonnegative exponents
   is correct, but it omitted Sasada's published negative-exponent obstruction. Any promoted
   literature paragraph should add that source and should credit the $m^{-2}$ root-gap mechanism
   as prior art.
2. Sasada's Theorem 3 states the exact unweighted symmetric-Dirichlet gap
   $(am+1)/[m(2a+1)]$ and cites earlier sources. This scout read the statement in Sasada but did
   not read both underlying proofs for general $a$. Accordingly, only the flat case $a=1$ read in
   Caputo is treated here as a verified exact import from its proving source.
3. The fixed-$\varepsilon$ cap probability and bound in the route probe were not found verbatim in
   the literature. They remain repository-authored mathematics even though Sasada proves a closely
   related and quantitatively stronger half-simplex cap bound for the spectral gap.
4. No citation presently supports an assertion that the root frame is optimal among invariant
   frames. Such an assertion would be false as a literature claim: no source found proves it.

## Searched and not found

The following searches were run against paper indices and primary-source citation trails:

- `simplex tight frame inverse conditional variance heat bath spectral gap`
- `"inverse conditional variance" "spectral gap" simplex`
- `"tight frame" conditional expectation Poincare simplex`
- `simplex conditional line resampling direction frame spectral gap`
- `stochastic exchange model negative gamma spectral gap simplex`
- `energy exchange model gamma negative spectral gap complete graph simplex`
- `"(eta_i+eta_j)^{-2}" spectral gap`
- `Caputo flat Kac model simplex exact spectral gap`
- `Carlen Posta Toth stochastic exchange gamma spectral gap`

No paper was found that:

- studies the inverse-conditional-variance form averaged over arbitrary Euclidean line
  directions;
- optimizes the spectral gap over even probabilistic tight frames;
- proves that the root orbit is extremal among permutation-invariant frames;
- supplies an all-frame simplex dual certificate; or
- converts ordinary hit-and-run estimates into the lower form inequality needed here without
  already assuming a Poincar\'e/KLS bound.

Frame-theory search hits concerned reconstruction frames or decompositions of the identity, not
conditional-line heat-bath gaps. Ordinary hit-and-run sources concern unnormalized chord
resampling and therefore do not answer (22)--(23).

## Recommended orchestrator action

1. Correct the literature assessment wherever it is promoted: cite Sasada for the published
   negative-exponent cap obstruction.
2. If the conditional-fiber route is admitted and receives a manuscript module, import
   `imp:sasada-negative-exchange-obstruction` with the exact statement above and add the three
   bibliography entries atomically.
3. Keep the root obstruction and the existential all-frame question logically separate. The next
   decisive work remains an all-frame simplex certificate or a uniform-gap construction, not
   further analysis of the dead root orbit.

```yaml
outcome: complete
artifacts:
  - research/explorations/2026-08-27-literature-scout-conditional-fiber-w1l02.md
proposed_deltas:
  - "When an appropriate manuscript anchor exists, add imported obstruction imp:sasada-negative-exchange-obstruction with import_class published and reference Sasada2015EnergyExchange, using the exact YAML in this report."
  - "If the conditional-fiber literature comparison is promoted, append the three exact BibTeX entries Caputo2008BinaryCollision, Sasada2015EnergyExchange, and CarlenPostaToth2025Exchange."
  - "Replace any claim that the root-cap mechanism is new with the precise statement that the repository has an independent fixed-epsilon derivation and Sasada 2015 supplies published prior art for the negative-exponent vertex-cap obstruction."
  - "Do not infer an all-frame simplex verdict: the existential supremum over admissible tight frames remains unresolved."
next_role: orchestrator
next_prompt: |
  Read research/explorations/2026-08-27-literature-scout-conditional-fiber-w1l02.md. Preserve the
  distinction between the root orbit and the all-frame problem. If a conditional-fiber manuscript
  anchor is created, add the published imported obstruction imp:sasada-negative-exchange-obstruction
  with the exact statement and reference in the report, and atomically append the three proposed
  BibTeX entries after deduplication. Record that Sasada's negative-exponent cap gives the local
  bound gap(D_root) <= 48/[m(m+1)], but do not claim that it refutes or resolves the existential
  all-frame target. No status change to KLS or to a live route follows from this literature import.
```
