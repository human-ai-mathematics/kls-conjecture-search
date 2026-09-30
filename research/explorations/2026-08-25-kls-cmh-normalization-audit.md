---
---

# Route C CMH normalization and exact cases — independent adversarial audit

This non-certifying audit was performed by `/review/kls-cmh-independent-audit` on work authored
by `/orchestrator/kls-cmh-normalization`. Its verdict was a partial pass: 13 of 17 nodes were
recommended for promotion, three required corrections, and one was not recommended. One dossier
proof and one manuscript proof were invalid as written, although the corresponding statements
were true.

---

## Scope

Certified in scope:

- [`solutions/thm-cmh-normalization.tex`](../../solutions/thm-cmh-normalization.tex) — every
  lemma, proposition, theorem and corollary, and the two scope paragraphs;
- [`solutions/thm-cmh-dirichlet.tex`](../../solutions/thm-cmh-dirichlet.tex) — likewise;
- the mirroring manuscript sections `modules/kls/41-cmh-normalization.tex` and
  `modules/kls/42-cmh-exact-cases.tex`, **including their proofs**, because the ledger node
  ids are the `\label`s in those files and the manuscript is the object of record;
- consistency against `modules/kls/04-family-moment-map.tex` (external Letwin / Chen–Klartag
  inputs, not re-verified) and `modules/kls/40-moment-map-cmh.tex` (pre-existing Route C
  construction layer, not re-verified);
- the `bounded_by: none` justifications against `research/kls/obstructions.{md,yaml}`;
- a literature sweep for prior art and for the two external citations.

**Explicitly excluded.** This audit does **not** certify: $\mathrm{CMH}(4)$ in general;
`conj:gate-zero`; anything in the Haar/Schur–Piola construction layer
(`conj:mm-invariant-lift`, `conj:mm-square-root-commutator`); the Letwin and Chen–Klartag preprint
inputs themselves (`import_class: preprint-unreviewed`); the `cmh-gate-zero` `finum`
artifact's code path (its *conclusions* were independently reproduced here, see §5, but the
target implementation was not read); the closure/approximation arguments beyond the level of
plausibility stated in §3.C; and `conj:kls` by any route.

## How each claim was verified

Three independent channels were used, and where the channels are listed together they agree.

- **hand** — full index-level re-derivation by the reviewer, written out and checked, not a
  reading of the dossier's own algebra.
- **symbolic** — `sympy`, exact rational/symbolic arithmetic.
- **exact-numeric** — pure-`Fraction` Dirichlet moments
  ($\E\prod P_i^{k_i}=\prod(\alpha_i)_{k_i}/(A)_{|k|}$), Galerkin quadratic forms on polynomial
  test spaces, then a float generalized eigenproblem on the non-degenerate subspace.
  **No Monte Carlo was used anywhere in this audit** (hard constraint 2 of `CLAUDE.md`); every
  number below is a deterministic exact-moment computation. These are reviewer-side
  corroborations and carry **no** R1 status — they are not `finum` artifacts and no ledger
  claim rests on them.

---

## Per-claim verdict table

| # | Claim | Verdict | How |
|---|---|---|---|
| 1 | Dirichlet-form/symmetry lemma; $\ker\Aop=$ constants | **VERIFIED** | hand |
| 2 | Bochner identity $\E(L_\mu g)^2=\E[\langle H\nabla g,\nabla g\rangle+\Tr(HD^2g\,HD^2g)]$ | **statement VERIFIED / proof GAP** | hand + symbolic |
| 3 | Endpoint reduction $\CPaff\le\CMH$ | **VERIFIED WITH CORRECTION** (dossier ok; **manuscript proof WRONG**) | hand |
| 4 | Weighted Hodge identity; operator norm *exactly* $\CPaff$; 1-D solenoidal vanishing | **VERIFIED** | hand |
| 5 | Algebraic countermodel, $m\ge18$ | **VERIFIED** | hand + symbolic + exact-numeric |
| 6 | Static commutator $\Tr(B^2H^2)=\Tr(BHBH)+\tfrac12\|[B,H]\|_{\HS}^2$ | **VERIFIED** | hand |
| 7 | 1-D identity $\CMH=\CP/\Var$; sharpness | **VERIFIED WITH CORRECTION** (citation + centering) | hand + exact-numeric |
| 8 | Product formula and cross-term identity | **VERIFIED** (manuscript sign-word error) | hand |
| 9 | Dirichlet theorem, steps (a)–(k) | **VERIFIED WITH CORRECTION** (two presentational gaps) | hand + symbolic + exact-numeric |
| 10 | Independent numerical corroboration | **VERIFIED — no violation found** | exact-numeric |

Sub-table for item 9, since it is the flagship:

| step | content | verdict | how |
|---|---|---|---|
| 9a | $H=C(p)/A$, $L_\mu=L_\alpha/A$, softmax pushforward | VERIFIED | hand |
| 9b | covariance formula, tangent pseudo-inverse | VERIFIED | hand |
| 9c | $\mathrm{CMH}(4)\iff A(A+1)d_\alpha\le4n_\alpha$ (powers of $A$) | VERIFIED | hand + symbolic |
| 9d | Gamma–Bochner identity | VERIFIED | hand + symbolic |
| 9e | row completion; $\E[Y^2uu']$ IBP; $\delta_i\ge0\iff\alpha_i\ge1$ | VERIFIED (exact equivalence confirmed) | hand |
| 9f | Euler identity; constrained row minimization; $\sum w_j^{-1}=S/Y_i$ | VERIFIED | hand |
| 9g | $\calL_\Gamma G=S^{-1}L_\alpha g$, $Y_iG_i=u_i$, $S\perp P$, $\E S^{-1},\E S^{-2}$ | VERIFIED | hand |
| 9h | $z_A\alpha_i\times(\text{coefficient})=F_A(\alpha_i,P_i)$ **exactly** | VERIFIED | symbolic (residual $\equiv0$) |
| 9i | angular minimization, both branches, interface | VERIFIED (and **sharp**) | hand + numeric |
| 9j | $z_A/4+A-\tfrac12=A(A+1)/4$ | VERIFIED | symbolic |
| 9k | $m=2$ base case; $A\ge3$ for inverse Gamma moments | VERIFIED | hand |
| — | the hypothesis $\alpha_i\le A-2$ | **not needed, and automatic** — see D6b | hand |

---

## Defects found

Ordered by severity. Every one of these is reported, not fixed.

### D1 — **WRONG.** The manuscript proof of `thm:cmh-implies-affine-poincare` contains a false step

`modules/kls/41-cmh-normalization.tex`, proof of Theorem `thm:cmh-implies-affine-poincare`:

> "The right-hand gradient energy is bounded by that of $f$ because
> $\one_{[\eps,R]}(\Aop)$ is a contraction commuting with the form."

This is false. $\one_{[\eps,R]}(\Aop)$ is a function of $\Aop$, so it commutes with the
$H$-form $\calE_H$ — but the "right-hand gradient energy" in that display is the **$\Sigma$-form**
$\E_\mu\langle\Sigma\nabla\cdot,\nabla\cdot\rangle$, whose generator
$\Aop_1=-\Div_\mu(\Sigma\nabla\,\cdot\,)$ does **not** commute with $\Aop$. Being an $L^2$
contraction does not bound a Dirichlet form. This is precisely the gap the dossier itself
identifies ("the $\Sigma$-form and the $H$-form do not commute") and repairs.

The dossier's Step 2 **is** correct, and I verified it independently: applying the
Cauchy–Schwarz chain to $f$ against $g_{\eps,R}$ gives
$\E[f\,\Pi_{\eps,R}f]=\E\langle\nabla f,H\nabla g_{\eps,R}\rangle
\le(\E\langle\Sigma\nabla f,\nabla f\rangle)^{1/2}C^{1/2}\|\Pi_{\eps,R}f\|_2$; the left side
equals $\|\Pi_{\eps,R}f\|_2^2$ because $\Pi_{\eps,R}=\Pi_{\eps,R}^2=\Pi_{\eps,R}^*$ (legitimate,
checked); and $\Pi_{\eps,R}f\to f$ because $\one_{[\eps,R]}(\Aop)\to\one_{(0,\infty)}(\Aop)$
strongly and $\one_{(0,\infty)}(\Aop)f=f$ for $f\perp\ker\Aop$, with $\ker\Aop$ the constants.
No spectral gap is used. The dossier's answer to the specific question posed to me — does the
repair avoid the gap — is **yes**.

**Required:** replace the manuscript proof by the dossier's. As it stands the `\label` the
ledger node binds to carries an invalid proof.

### D2 — **GAP.** Neither proof of the Bochner identity `prop:cmh-bochner` works; the statement is true

The **statement is true** — I proved it independently and confirmed it exactly. Both offered
proofs are unsound.

*What is actually true.* Writing $\Phi_{mk\ell}:=H_{mj}\partial_jH_{k\ell}$ (target
coordinates), a full index computation using only $\E[H_{ij}\partial_jF]=\E[x_iF]$ gives the
**exact** identity
$$\E(L_\mu g)^2=\E\bigl[\langle H\nabla g,\nabla g\rangle+\Tr(HD^2g\,HD^2g)\bigr]
+\E\bigl[\Phi_{mk\ell}\,(g_{mk}g_\ell-g_m g_{k\ell})\bigr].$$
The correction vanishes **iff $\Phi$ is totally symmetric**. For a moment map it is:
$\partial_{x_j}H_{k\ell}=(H^{-1})_{ja}\varphi_{ak\ell}$, hence
$\Phi_{mk\ell}=\varphi_{mk\ell}$, totally symmetric. That is the Hessian-metric / Codazzi
property — and it is **not** implied by symmetry, positivity and $\Div_\mu H=-p$.

*Why the dossier's proof fails.* The dossier says the assembly follows "after one further
integration by parts using $\Div_\mu H=-p$ in the second slot". It never consumes the
Hessian structure, and it cannot: I built a symmetric Stein kernel that satisfies every
property the dossier names and violates the identity. Take $\mu=N(0,\Id_2)$,
$H=\Id+\eps K$ with $\rho K=R_\perp^\top D^2\lambda\,R_\perp$, $\lambda=\rho\,xy$, i.e.
$$K=\begin{pmatrix}xy(y^2-3)&-(1-x^2)(1-y^2)\\-(1-x^2)(1-y^2)&xy(x^2-3)\end{pmatrix},$$
which is symmetric with $\Div(\rho K)=0$ (verified symbolically), hence $\Div_\mu H=-x$
exactly. The defect $\E(L_\mu g)^2-\E[\langle H\nabla g,\nabla g\rangle+\Tr(HD^2g\,HD^2g)]$ is
then, by exact Gaussian moments,
$160\eps^2$ for $g=x^2y$, $-320\eps^2$ for $g=x^3+xy^2$, $1536\eps^2$ for $g=x^2y^2$ —
and in each case it **equals the $\Phi$-asymmetry term above to the last coefficient**.
(Positivity plays no role in the identity or in this computation, so the demonstration
refutes the *proof strategy*, not the theorem.)

*Why the manuscript's proof fails.* The $\Gamma_2$ route — "the third-derivative terms
produced by $\Gamma_2$ cancel against the connection terms carried by $\calL(D^2\varphi)$" — is
not verifiable as written, and is structurally suspicious: the differentiated Monge–Ampère
identity `eq:differentiated-MA` supplies two manifestly **nonnegative** sources, which would
naturally yield an *inequality* $\Gamma_2\ge\|\mathrm{Hess}\|^2+\Gamma$, not the asserted
equality. The manuscript's fallback ("Equivalently and without invoking $\Gamma_2$, expand …
and use $\Div_\mu H=-p$ twice") is the same insufficient argument as the dossier's.

*Confirmation that the statement holds.* For the genuine moment-map kernel $H=C(p)/A$ I
checked $\E(L_\alpha g)^2=\E[A\langle C\nabla g,\nabla g\rangle+\Tr(CD^2g\,CD^2g)]$ in exact
rational arithmetic for $\alpha\in\{(1,1,1),(1,2,3),(2,3,5,7),(\tfrac32,4,5)\}$ and
$g=p^{(3,0,0)},p^{(2,1,0)},p^{(1,1,0)},p^{(2,2,0)},p^{(1,2,1)}$: defect $=0$ in all 20 cases.
The Laguerre specialization `eq:cmh-gamma-bochner` is the same identity at $H=\diag(Y)$ and
was re-derived by hand.

**Required:** write the index proof and state explicitly that total symmetry of
$\varphi_{mk\ell}$ is the hypothesis consumed. Also: the remark that "the same reduction
applies verbatim to any positive symmetric Stein kernel" is correct **only** for
`thm:cmh-implies-affine-poincare`; it must not be allowed to read as covering
`prop:cmh-bochner`, which is false for a general Stein kernel.

### D3 — **OVERCLAIM.** "CMH is strictly stronger than KLS" is not proved

`cor:sol-cmh-strictly-stronger` asserts "$\mathrm{CMH}(C)$ implies, **and is not implied by**,
$\CPaff\le C$"; `cor:cmh-hodge-comparison` asserts "$\mathrm{CMH}(4)$ is a *strictly stronger*
statement than KLS with constant 4"; the manuscript subsection is titled "CMH is strictly
stronger than KLS"; and the ledger carries `cor:cmh-hodge-comparison` at `status: proved`.

What is actually proved: (i) the orthogonal splitting `eq:cmh-hodge`; (ii) that the
$\Sigma\nabla\psi$ channel alone has operator norm exactly $\CPaff$; (iii) that the solenoidal
channel is empty in dimension one. What is **not** proved, anywhere: that the excess is
nonzero *at or near a CMH-extremizing $g$* in dimension $\ge2$; and, a fortiori, that there
exists a log-concave $\mu$ with $\CPaff(\mu)\le4<\CMH(\mu)$. The load-bearing phrase is "in
dimension at least two $w$ is generically nonzero", which is asserted without argument and
without a single example. Non-implication between two *statements* requires a separating
instance.

The honest version — $\CMH\ge\CPaff$ always, the difference is the solenoidal excess, so
$\mathrm{CMH}(4)$ is *not known to be* equivalent to KLS(4) and may fail while KLS holds — is
fully supported and is what `rem:cmh-normalization`'s note and `rem:cmh-program` already say.
The dossier corollary's own heading ("The route's headline **may** be false") and the closing
sentence are correctly hedged; the middle sentence is not.

**Required:** demote `cor:cmh-hodge-comparison` from `proved`, or restate it as the
supported claim. See §7.

### D4 — **GAP.** Domain/core hypothesis in the endpoint reduction is unstated

`thm:cmh-implies-affine-poincare` concludes for "every $f\in H^1(\mu)$", i.e. every $f$ of
finite $\Sigma$-energy. But Step 2 uses $\langle f,\Aop g\rangle=\calE_H(f,g)$, which for
self-adjoint $\Aop$ requires $f\in\Dom(\calE_H)$, i.e. **finite $H$-energy**. $H$ is unbounded
in general (already $\tau(x)=x+1$ on the line), so the two classes need not coincide and the
$\Sigma$-class is not obviously the smaller one. The standard repair — run the argument on a
core ($C_c^\infty$, which does have finite $H$-energy since $H$ is locally bounded), then
extend by density in the $\Sigma$-form — is not mentioned in either the dossier or the
manuscript. Low mathematical risk, but it is a real hole in a proof offered for
certification.

### D5 — **GAP (small but genuine).** `cor:cmh-dirichlet-surplus` is not proved for $m=2$

The corollary is stated for all $A>3$. The surplus inequality `eq:cmh-dirichlet-surplus` is
derived only inside the branch "Assume $m\ge3$"; the $m=2$ branch is routed to
`thm:cmh-1d`, which yields $\CMH\le4$ with **no** surplus. So e.g. $\mathrm{Beta}(2,2)$
($m=2$, $A=4>3$) is claimed by the corollary but not covered by the printed proof.

The claim is nevertheless **true**: the Gamma lift needs only $A\ge3$, never $m\ge3$, so the
$m\ge3$ argument applies verbatim to $m=2$ whenever $A\ge3$. Confirmed numerically:
$\mathrm{Beta}(2,2)$ gives $\max A(A+1)d_\alpha/n_\alpha=1.0818$ against the surplus ceiling
$3.3616$; $\mathrm{Beta}(1,20)$ gives $2.3151$ against $3.4608$. **Fix is one sentence**
("the $m\ge3$ argument uses only $A\ge3$"), but as written the corollary outruns its proof.

### D6 — **IMPRECISIONS** in the Dirichlet section

**(a) `rem:cmh-dirichlet-logconcavity` mislocates where log-concavity is spent.** It states
that $\alpha_i\ge1$ "is used at precisely one place in this entire section, the sign of
$\delta_i$." That is wrong for the Dirichlet theorem. In the Dirichlet chain $\delta_i$ enters
**exactly** (through $z_A\delta_i$ inside $F_A$), not through its sign; what actually consumes
$\alpha_i\ge1$ is the constraint $a\ge1$ in `lem:cmh-angular-coefficient`, and it is
load-bearing there: $F_A(a,p)\to-z/4<0$ as $a\downarrow0$. The remark is correct only about
the *product-Gamma* corollary of `lem:cmh-gamma-completion`. That $\alpha_i\ge1$ is genuinely
necessary for the conclusion is confirmed numerically: $\Dir(0.2,3,3)$ (not log-concave) gives
$\max A(A+1)d_\alpha/n_\alpha=5.1999>4$, a clean violation of `eq:cmh-dirichlet-main` outside
the hypothesis. The same wording appears verbatim in the ledger note for
`lem:cmh-gamma-completion` ("LOG-CONCAVITY IS SPENT HERE AND NOWHERE ELSE in the Dirichlet
proof") and is wrong there too.

**(b) The $\alpha_i\le A-2$ question (asked explicitly).** The hypothesis appears nowhere in
the current manuscript or dossier; only the ledger note for `lem:cmh-angular-coefficient`
records that it "is never used and was dropped." **That is correct on both counts**, and
doubly so: (i) no step needs an upper bound on $a$ — the angular lemma is proved for all
$a\ge1$, and the $z\ge4$ branch handles arbitrarily large $a$ through the interface argument;
(ii) in the only branch where the lemma is invoked ($m\ge3$, all $\alpha_j\ge1$),
$A-\alpha_i=\sum_{j\ne i}\alpha_j\ge m-1\ge2$, so $\alpha_i\le A-2$ holds automatically. Its
absence from the dossier is **correct, not a gap.**

**(c) The angular lemma is sharp, which is worth recording.** Brute-force minimization of
$F_A$ over $a\ge1$, $0<p\le1$ reproduces the claimed bound $A-\tfrac12+s_A$ to $10^{-11}$ with
**equality** for every $A\in\{3,3.0001,3.5,3.732,3.74,4,5,6,8,10,20,50,102,1000\}$, at
$a=1$ and at $p=1$ (when $z\le4$) or $p=p_*=(a+1)/\sqrt z$ (when $z\ge4$) exactly as claimed.
The case split at $\sqrt z\le a+1$, the monotonicity in $a$ and in $r=a/(a+1)$, and the
interface continuity (both branch formulas agree at $a+1=\sqrt z$, which I checked by hand)
are all correct.

### D7 — **ERROR (wording), manuscript.** Sign of the product generators

`modules/kls/42-cmh-exact-cases.tex`: "$L_\mu=\sum_iL_i$, the summands being commuting
**nonnegative** generators." They are non**positive** ($\E[gL_ig]=-\E[\tau_i(\partial_ig)^2]\le0$;
$\Aop=-L_\mu\ge0$). The dossier says "nonpositive" and is right. The manuscript also says
"commuting nonnegative generators" a second time in the block-version sentence. Direct
contradiction between the two files under audit.

### D8 — **TYPO, dossier.** Meaningless factor in the Hodge proof

`solutions/thm-cmh-normalization.tex`, proof of `prop:sol-cmh-hodge`:
"$\Div_\mu w=\Div_\mu u+\Div_\mu(\Sigma\nabla\psi)\cdot(-1)^{0}=-h+h=0$". The
"$\cdot(-1)^{0}$" is not a sign convention, it is $\cdot1$, and it makes the display read as
$-h-h$. The identity is correct; the notation is garbage.

### D9 — **COSMETIC, manuscript.** Countermodel presentation

- "$\E H=(c+d/m)\,\Id_m\oplus1=\Id_{m+1}$": the block order is reversed — the $(1,1)$ entry is
  $1$ and the $m$-block is $(c+d/m)\Id_m$. The dossier has it right.
- "The Schur complement … is $c\,\Id_m\succeq0$ and $c>0$": mixes $\succeq$ with strict
  positivity; it is $\succ0$.
- "The $O(m)$-invariant decomposition … **diagonalizes** this form": it block-diagonalizes into
  three sectors; the scalar sector $(a,t)$ is 2-dimensional and is *not* diagonal — which is the
  whole point, since the equality ray $a=dt$ lives there.

### D10 — **CITATION DEFECTS** (see §6 for the evidence)

- `\cite[Eq.~(2.25)]{cattiaux2018poincare}` for "the sharp one-dimensional log-concave bound
  $\CP\le4\Var$". The pointer is **locatable and the inequality is correct**, but (i) (2.25) in
  Cattiaux–Guillin reads $\mathrm{Var}_\nu(f)\le4\,\mathrm{Var}_\nu(x)\,\nu(|\nabla f|^2)$, a
  $\R^d$ statement with $\mathrm{Var}_\nu(x)=\Tr\Sigma$, not a one-dimensional statement; (ii)
  Cattiaux–Guillin explicitly **credit it to Kannan–Lovász–Simonovits**, so the dossier cites a
  secondary source as if it were primary; (iii) the word "sharp" is the dossier's, not
  Cattiaux–Guillin's — sharpness in $d=1$ comes from the exponential limit, which the dossier
  supplies separately. Equation numbers in an arXiv preprint are also version-dependent and are
  a fragile citation target.
- "the standard one-sided exponential $e^{-x}\one_{x\ge0}\dd x$ has $\Var=1$, $\CP=4$". The
  numbers are right, but **that measure is not centered**, contradicting the theorem's own
  standing hypothesis; it should be the centered shift $x\mapsto x-1$ (for which
  $\tau(x)=x+1$ on $(-1,\infty)$, as used implicitly elsewhere). The `BobkovLedoux1997`
  attribution I could not confirm as the primary source for the *one-sided* value; that paper's
  title concerns the (two-sided) exponential distribution. Low risk, but unverified.

### D11 — **PROCESS / METADATA**

- Both dossier headers were written with `checked_by: agent`, `reviewed_by:
  /review/kls-cmh-independent-audit` and `review: research/reviews/2026-08-25-…md` **already
  filled in**, and the ledger was already flipped to `status: proved` for all 17 nodes, before
  this review existed. `check_ledger.py` currently reports 16 errors, all of the form
  "`review: … does not exist`" — i.e. the only thing standing between the promotion and a green
  check was the physical existence of this file. That is the wrong order of operations: the
  gate is the review's *content*, not its *filename*.
- Both dossier headers declare `evidence_run: none`, while the ledger nodes
  `thm:cmh-dirichlet` and `conj:gate-zero` carry
  `evidence_run: research/runs/2026-08-25T070915.854321Z-cmh-gate-zero.jsonl` with
  `evidence: numerical-directional`. The dossiers' position (the artifact supports no statement
  proved therein) is the more defensible one; the two should be reconciled.
- `def:cmh` is a `kind: definition` at `status: proved`. Nothing here is wrong — the definition
  is well posed and I checked that the pseudo-inverse conventions make the affine-subspace case
  (the Dirichlet laws) meaningful — but "proved" is a category error for a definition and the
  orchestrator may want a distinct status.

### Non-defects (checked and clean)

- **`bounded_by: none` is defensible.** `research/kls/obstructions.md` scopes all six entries to
  the fixed-cut Eldan program in its own header, and `obstructions.yaml`'s enforcement is by
  declared `mechanism` tag. `rem:projection-ceiling` forbids the tags `projection-only` and
  `radial-only`; neither dossier uses projection tests or radial information — the endpoint
  reduction is a duality argument, the countermodel is finite-dimensional matrix algebra, and
  the Dirichlet proof uses the **full Hessian row** through the Euler constraint. Neither makes
  a thin-shell claim. **`rem:projection-ceiling` is genuinely not violated.**
- **Scope honesty on the Dirichlet result is good.** "What this does not show" states plainly
  that it is a family result, not evidence for universal $\mathrm{CMH}(4)$, and points at
  `cor:cmh-dirichlet-surplus` (strict interiority) and `thm:cmh-product` (the saturating
  direction lies elsewhere). The manuscript's "first genuinely nonproduct family for which
  **the route** has a theorem" is correctly route-scoped.
- **The `conj:trace-upgrade`/`conj:product-alignment` single-owner discipline (hard constraint 6) is respected**:
  `rem:gate-zero-trace-upgrade` and both dossiers explicitly decline to assert equivalence.
- **The machinery is not over-engineered.** I checked whether the cheap pointwise criterion
  $\CMH\le\operatorname*{ess\,sup}\lmax(\Sigma^{-1/2}H\Sigma^{-1/2})$ already settles the
  Dirichlet family — it does not. That supremum is $2.00$ for $\Dir(1,1,1)$ but $4.50$ for
  $\Dir(1^{\times8})$, $6.50$ for $\Dir(1,1,10)$ and $51.50$ for $\Dir(1,1,100)$. The Gamma-lift
  argument is genuinely needed.
- **`rem:cmh-dirichlet-sharp`'s Bessel formula is right** (spot-checked, see §5).
- **The aggregation consistency check in `rem:cmh-dirichlet-closure` is right**:
  $\E[\sum_{a\in G_i}Q_a^2/\beta_a\mid P]=P_i^2(\alpha_i+|G_i|)/(\alpha_i(\alpha_i+1))
  \ge P_i^2/\alpha_i$ iff $|G_i|\ge1$. Re-derived.
- Both dossiers **compile standalone** (`latexmk`, only the expected unresolved `\ref`s), and
  `latexmk -pdf main.tex` builds the full manuscript with **no** undefined references or
  citations.

---

## 5. Independent numerical corroboration (item 10)

Method: exact rational Dirichlet moments; ambient polynomial test functions in
$p_1,\dots,p_{m-1}$ of total degree $\le K$; $u_i=(C(p)\nabla g)_i$ and
$L_\alpha g=\Tr(C D^2g)+\langle\alpha-Ap,\nabla g\rangle$ expanded exactly; Gram matrices for
$d_\alpha$ and $n_\alpha$ formed in `Fraction` arithmetic; largest generalized eigenvalue of
$A(A+1)d_\alpha$ against $n_\alpha$ on the non-degenerate subspace. The constant function is the
only kernel direction (checked: $u=0\iff\nabla g=0$ on the open simplex).

| $\alpha$ | deg | $\max A(A+1)d_\alpha/n_\alpha$ | surplus ceiling $4/(1+4s_A/(A(A+1)))$ | $\le4$? | $\le$ ceiling? |
|---|---|---|---|---|---|
| $(1,1)$ | 8 | 1.215854204 | — ($A=2$) | yes | — |
| $(2,2)$ | 8 | 1.081763630 | 3.361633 | yes | yes |
| $(1,5)$ | 8 | 1.517274262 | 3.117546 | yes | yes |
| $(1,20)$ | 10 | 2.315069781 | 3.460840 | yes | yes |
| $(1,1,1)$ | 6 | 1.380656071 | 4.000000 | yes | yes |
| $(1,1,10)$ | 5 | 2.017399441 | 3.250807 | yes | yes |
| $(1,1,100)$ | 6 | 3.194463900 | 3.854707 | yes | yes |
| $(1,1,1000)$ | 5 | 3.377437200 | 3.984160 | yes | yes |
| $(1,2,3)$ | 5 | 1.566605103 | 3.117546 | yes | yes |
| $(3,5,7)$ | 4 | 1.231222460 | 3.333762 | yes | yes |
| $(1,50,50)$ | 4 | 3.164499700 | 3.853380 | yes | yes |
| $(1,1,1,100)$ | 4 | 3.177054400 | 3.856010 | yes | yes |
| $(1,1,1,1)$ | 4 | 1.513949356 | 3.361633 | yes | yes |
| $(1,2,3,4,5)$ | 3 | 2.123965749 | 3.333762 | yes | yes |
| $(2,3,5,7)$ | 3 | 1.493990300 | 3.381520 | yes | yes |
| $(1^{\times6})$ | 3 | 1.720995900 | 3.117550 | yes | yes |
| $(1^{\times7})$ | 3 | 1.804953000 | 3.115050 | yes | yes |
| $(1.5,1.5,1.5)$ | 5 | 1.269317665 | 3.237181 | yes | yes |

**No violation of `eq:cmh-dirichlet-main`, and no violation of the sharper surplus bound
`cor:cmh-dirichlet-surplus`, was found anywhere.** Outside the hypothesis the bound does break,
as it must: $\Dir(0.2,3,3)$ gives $5.1999>4$, and $\Dir(0.5,0.5,5)$ gives $2.5234$ (inside, but
with the surplus ceiling $3.1176$ still respected only accidentally).

Two independent confirmations of the *normalization* itself, which are stronger than the
inequality checks because they pin exact values through two unrelated routes:

1. $\Dir(1,1)$ = uniform on $[0,1]$, computed entirely on the simplex side, gives
   $\CMH=1.215854204$. $12/\pi^2=1.2158542038\ldots$ — i.e. exactly $\CP/\Var$ for the uniform
   law. This confirms `thm:cmh-1d` and the whole $A$-power bookkeeping of item 9c to ten digits.
2. `rem:cmh-dirichlet-sharp` claims
   $\CMH(\mathrm{Beta}(1,b))=(b+1)^2(b+2)/(b\,j_{b/2,1}^2)$. Against the simplex-side
   computation:

   | $b$ | Bessel formula | Galerkin | rel. diff |
   |---|---|---|---|
   | 1 | 1.215854204 | 1.215854204 | $2.6\cdot10^{-13}$ |
   | 2 | 1.225993461 | 1.225993461 | $8.6\cdot10^{-13}$ |
   | 3 | 1.320738209 | 1.320738209 | $1.5\cdot10^{-12}$ |
   | 5 | 1.517274262 | 1.517274262 | $8.4\cdot10^{-13}$ |
   | 10 | 1.887211106 | 1.887211106 | $2.3\cdot10^{-13}$ |
   | 20 | 2.315069781 | 2.315069781 | $6.7\cdot10^{-11}$ |
   | 40 | 2.732144233 | 2.732143442 | $2.9\cdot10^{-7}$ |

   and the formula gives $3.189$ at $b=100$, $3.788$ at $b=1000$ — the approach to $4$ claimed in
   that remark.

**Limitation to record:** at large $A$ the exact-moment Gram matrices become badly conditioned
and the effective polynomial dimension collapses (e.g. $\alpha=(1,1,1000)$ retains only 9 of
20 directions), so the table's large-$A$ entries under-resolve the true supremum. They cannot
therefore *exclude* a violation at high polynomial degree for large $A$; they only fail to find
one. The moderate-$A$ entries are well resolved and stable in degree.

**Countermodel (item 5), verified three ways.** I re-derived $\E\Tr(BHBH)$ from scratch by block
expansion and obtained the dossier's display **exactly**, including the $|r|^2$ coefficient
$2(c+2d/m)$ (a first attempt of mine gave $2(1+\sqrt d/m)$; the error was mine, the dossier is
right). I then built the superoperator $\calT(B)=\E[HBH]$ explicitly on
$\mathrm{Sym}(m+1)$ from the exact moments $\E z=0$, $\E zz^\top=\Id/m$,
$\E[z_iz_jz_kz_\ell]=(\delta\delta+\delta\delta+\delta\delta)/(m(m+2))$, cross-checked the
closed form against a brute-force moment contraction (agreement to $10^{-16}$), and diagonalized:

| $m$ | 2 | 5 | 10 | 17 | 18 | 20 | 30 | 50 |
|---|---|---|---|---|---|---|---|---|
| $\lmax(\calT)$ | 2.0000 | 2.0000 | 2.0000 | 2.0000 | 2.0000 | 2.0000 | 2.0000 | 2.0000 |
| $(\E H^2)_{11}=1+d$ | 2.155 | 2.667 | 3.294 | 3.959 | **4.043** | 4.203 | 4.906 | 6.025 |

$\lmax(\calT)=2$ **exactly** for every $m$ (saturated on the scalar ray $a=dt$, as claimed), and
$1+d$ crosses $4$ exactly at $m=18$ ($m^2-18m+9>0$, positive root $9+6\sqrt2\approx17.485$).
Since $\lmax$ is taken over the *entire* symmetric space, **the "for every symmetric $B$"
quantifier is genuinely established** — not merely on the three sectors, which I also confirmed
decouple (the form's only cross term is $a\cdot\Tr D$, and $\Tr(tI\cdot D_0)=0$).
Positivity ($H\succ0$ via Schur complement $c\Id_m$, $c>0$), $\E H=\Id_{m+1}$, the traceless
coefficient $1+(m-2)/((2m-1)(m+2))\le2$, the scalar identity $mc^2+2cd+d^2=m+d^2-d^2/m$, and the
perfect square $(a-dt)^2$ (via $d^2(2-1/m)=m$) were each re-derived by hand and all check out.

The repository's own `finum` artifact
`research/runs/2026-08-25T070915.854321Z-cmh-gate-zero.jsonl` reports
`max_galerkin_Q_over_ceiling = 0.933`, `gate_zero_refuted: false`,
`dirichlet_theorem_refuted: false`, `monte_carlo_used: false`,
`one_plus_d_at_m18 = 4.0426` — all consistent with the independent numbers above. Its own note
correctly warns that every instance lies inside a class already covered by a theorem, so it is
calibration, not evidence.

---

## 6. Literature findings

**(i) The affine Poincaré constant of Dirichlet / simplex laws is prior art — qualitatively.**
Kolesnikov–Milman, *The KLS isoperimetric conjecture for generalized Orlicz balls*
(Ann. Probab. 46(6), 2018; [arXiv:1610.06336](https://arxiv.org/abs/1610.06336)), §1.2, states:

> "The conjecture has been confirmed (uniformly in $n$) for unit-balls of $\ell_p^n$ (by
> S. Sodin when $p\in[1,2]$ and R. Latała and J. Wojtaszczyk when $p\in[2,\infty]$), **the
> simplex by F. Barthe and P. Wolff**, convex bodies of revolution by N. Huet"

and that the extended KLS conjecture is established "for certain Gibbs measures corresponding
to **conservative spin systems** by Barthe–Wolff and Barthe–Milman." The canonical Gibbs
measure of independent $\Gamma(\alpha_i,1)$ variables conditioned on their sum **is** the
Dirichlet law — exactly the class of `thm:cmh-dirichlet`. The relevant primary references are
almost certainly F. Barthe & P. Wolff, *Remarks on non-interacting conservative spin systems:
the case of gamma distributions*, Stochastic Process. Appl. **119** (2009)
([ScienceDirect S0304414909000337](https://www.sciencedirect.com/science/article/pii/S0304414909000337)),
and F. Barthe & E. Milman on transference for conservative spin systems; I was **not** able to
open either full text (403 / PDF unparseable), so the exact statements, hypotheses ($\alpha_i\ge1$
or not) and constants **remain unverified** and must be checked before any external write-up.
`fi_references.bib` currently contains **zero** Dirichlet, simplex, Wright–Fisher or
Barthe–Wolff entries.

**Consequence for the repository.** `cor:cmh-dirichlet-poincare` ("Every log-concave Dirichlet
law satisfies $\CPaff\le4$") is, as a *qualitative* statement, already in the literature. What
appears genuinely new is (a) the **explicit constant 4** with the quantitative surplus
`eq:cmh-dirichlet-surplus`, (b) fully anisotropic $\alpha$, and (c) the statement at the
**CMH level**, which is strictly stronger than the Poincaré level. The ledger note on
`cor:cmh-dirichlet-poincare` already flags this ("Literature reconciliation is task M11 and is
NOT complete"), which is the right posture — but the *manuscript corollary itself carries no
citation and no hedge*, and a reader of §42 alone would take it as new. **Required before any
external circulation, and recommended now:** add the Barthe–Wolff citation and one sentence
saying precisely which part is new.

**(ii) The Wright–Fisher / Dirichlet spectral gap in a different normalization.** Feng, Miclo &
Wang, *Poincaré inequality for Dirichlet distributions and infinite-dimensional
generalizations* ([arXiv:1504.02829](https://arxiv.org/abs/1504.02829), 2015) prove a **sharp**
Poincaré inequality for $\Dir(\alpha)$ with constant $1/\alpha_{N+1}$ — but in a *different*
Dirichlet form, $\bigl(1-\sum_ix_i\bigr)\sum_nx_n(\partial_nf)^2$, not the covariance-weighted
form that KLS is about and not the Wright–Fisher form $\sum_{ij}C(p)_{ij}\partial_if\partial_jf$.
It does not collide with `thm:cmh-dirichlet`, and it is not the affine constant. Worth citing
for context; it is not prior art for this theorem.

**(iii) No Stein-kernel Riesz-transform precedent found.** In the Stein-kernel literature
(Fathi, *Stein kernels and moment maps*, Ann. Probab. 47(4) 2019,
[arXiv:1804.04699](https://arxiv.org/abs/1804.04699); Courtade–Fathi–Pananjady, *Existence of
Stein kernels under a spectral gap*, AIHP 55(2) 2019,
[arXiv:1703.07707](https://arxiv.org/abs/1703.07707)) I found no second-order /
Riesz-transform bound of the form
$\|\Sigma^{-1/2}H\nabla\Aop^{-1}\|_{L^2\to L^2}\le\sqrt C$, and no statement that such a bound
implies Poincaré/KLS. The standard consequence of the moment-map Stein kernel in that
literature is the first-order Brascamp–Lieb-type inequality
$\Var_\mu f\le\E\langle\tau_\mu\nabla f,\nabla f\rangle$, which the repository already records as
`eq:mm-brascamp-lieb`. **Caveat: a null web search is weak evidence**; I could not read the full
texts of several relevant papers. `def:cmh` and `thm:cmh-implies-affine-poincare` appear to be
new formulations, but that is a "not found", not a "does not exist".

**(iv) `cattiaux2018poincare` Eq. (2.25) — located and read.** In Cattiaux–Guillin, *On the
Poincaré constant of log-concave measures* ([arXiv:1810.08369](https://arxiv.org/abs/1810.08369)),
equation (2.25) reads
$$\mathrm{Var}_\nu(f)\le4\,\mathrm{Var}_\nu(x)\,\nu(|\nabla f|^2),$$
introduced by the sentence "A stronger similar result (**credited to Kannan, Lovász and
Simonovits**) is mentioned in [1] p.11, namely". So: the pointer is real and the inequality is
correct, the one-dimensional specialization $\CP\le4\Var$ is exactly what the dossier uses, but
the attribution belongs to KLS 1995 and is being routed through a secondary source without
saying so. See D10.

**(v) Gate zero.** I found no occurrence of $\E[H\Sigma^{-1}H]\preceq4\Sigma$ (or
$\E H^2\preceq4\Id$ for moment-map Hessians) in the literature. Note that the countermodel's
mathematical content is the unsurprising fact that a **trace** bound
($\E\Tr(BHBH)\le2\Tr(B^2)$) does not imply a **Loewner** bound; its value is the explicit
construction that saturates the trace bound while blowing past $4$ in operator norm, and that
value is real. The Letwin ($\E\Tr(BHBH)\le2\Tr B^2$) and Chen–Klartag ($\E\|H\|_{\HS}^2\le2n$,
$\Var|X|^2\le8n$, $\|T_3\|^2\le4n$) inputs were **not** re-verified here; they carry
`import_class: preprint-unreviewed` and were audited on 2026-08-24.

---

## 7. Promotion recommendation, per ledger node

`solutions/thm-cmh-normalization.tex`:

| node | recommendation |
|---|---|
| `def:cmh` | **PROMOTE.** Well posed; the affine-tangent pseudo-inverse convention was checked against the Dirichlet case and is coherent. (Consider a status other than `proved` for a definition — D11.) |
| `prop:cmh-bochner` | **DO NOT PROMOTE** as currently written. Statement verified true; **both** offered proofs are invalid (D2). Promote once the index proof naming the total symmetry of $\varphi_{mk\ell}$ replaces them. |
| `thm:cmh-implies-affine-poincare` | **HOLD, then PROMOTE.** The dossier's proof is correct and the specific repair I was asked to scrutinize does work. But the node's `file:` is the manuscript, whose printed proof contains a false step (D1). Fix D1, add the core/density sentence (D4), then promote. |
| `prop:cmh-hodge` | **PROMOTE.** Fully verified, including that the operator norm is *exactly* $\CPaff$ and that a square-integrable divergence-free field with no flux vanishes in dimension one (and that the no-flux convention is genuinely needed there — a constant field on a compactly supported law is a counterexample without it). Fix the typo D8. |
| `cor:cmh-hodge-comparison` | **DO NOT PROMOTE.** Overclaim (D3): "strictly stronger" and "generically nonzero" are asserted, not proved, and no separating measure is exhibited. Demote to `heuristic`, or restate as "not known to be equivalent; may fail while `conj:kls` holds", which *is* proved. |
| `prop:letwin-not-gate-zero` | **PROMOTE.** Fully verified by hand, symbolically and by exact superoperator diagonalization; the universal-$B$ quantifier is genuinely established; the scope corollary is honest. |

`solutions/thm-cmh-dirichlet.tex`:

| node | recommendation |
|---|---|
| `thm:cmh-1d` | **PROMOTE after D10.** The identity is correct — I re-derived it by a cleaner route than the dossier's ($\rho u=\rho v'$ where $v=(D_\mu^*D)^{-1}h$, giving $\|u\|^2=\langle h,(D_\mu^*D)^{-1}h\rangle$ directly and bypassing the $((D_\mu^*)^{-1})^*=D^{-1}$ formalism, which is only formally justified). Confirmed to ten digits by two unrelated computations. Fix the KLS attribution and the non-centered measure. |
| `thm:cmh-product` | **PROMOTE after D7.** Cross-term identity re-derived and correct; both directions of the max formula check out. |
| `cor:cmh-linear-images` | **PROMOTE.** Correct, including that no invertibility is needed and that it is a $\CPaff$-level statement only. |
| `lem:cmh-gamma-completion` | **PROMOTE.** Every step re-derived; $\delta_i\ge0\iff\alpha_i\ge1$ is an exact equivalence as claimed. Correct the note's "spent here and nowhere else" (D6a). |
| `lem:cmh-row-min` | **PROMOTE.** Euler identity, the weight sum $S/Y_i$, and the constrained minimum all verified. |
| `lem:cmh-angular-coefficient` | **PROMOTE.** Both branches, the case split, the monotonicity, and the interface argument verified; numerically sharp at every $A$ tested. |
| `thm:cmh-dirichlet` | **PROMOTE.** The flagship. Every step (a)–(k) independently re-derived; 9h and 9j confirmed symbolically to be exact identities; end-to-end conclusion corroborated on 24 parameter vectors with no violation; the hypothesis $\alpha_i\ge1$ shown to be load-bearing by an explicit out-of-hypothesis violation. |
| `cor:cmh-dirichlet-surplus` | **PROMOTE after D5.** True but not proved for $m=2$ by the printed argument; one sentence fixes it. |
| `cor:cmh-dirichlet-poincare` | **PROMOTE the mathematics; REQUIRE the literature hedge.** The derivation is correct. But the statement is qualitatively prior art (Barthe–Wolff, §6(i)) and the manuscript corollary carries no citation. Add the citation and a one-line novelty statement before promotion, not after. |
| `cor:cmh-product-saturation` | **SPLIT.** The factual half — products of one-sided exponentials attain $\CMH=4$ exactly, and `prop:cmh-hodge` splits the numerator — is **proved** and may be promoted. The inference "Hence any perturbation … would push $\CMH$ above 4 and refute $\mathrm{CMH}(4)$" is **heuristic**: it inherits D3 and it presupposes the very second-order computation that `conj:cmh-second-variation` explicitly leaves open. Do not certify that clause. |

Unaffected by this review: `conj:gate-zero`, `rem:gate-zero-dichotomy`, `conj:cmh-second-variation`,
`rem:gate-zero-trace-upgrade` (all correctly `open`/`conditional`), and
`rem:cmh-normalization`, whose `status: proved` rests on `def:cmh` +
`thm:cmh-implies-affine-poincare` and inherits the D1 hold.

## 8. Validation performed

- `latexmk -pdf` on both dossiers standalone: builds, only the expected unresolved `\ref`s.
- `latexmk -pdf main.tex`: builds; **no** undefined references or citations.
- `python3 research/check_ledger.py`: 2 ledgers, 170 nodes, 630 labels, **16 errors**, all of the
  form "`<node>.review: research/reviews/2026-08-25-kls-cmh-normalization-audit.md` does not
  exist". Those clear on this file's existence — which is exactly why the *content* above, not
  the exit code, is the gate.
- All 17 node ids occur exactly once as a `\label`, in the file the ledger declares.

## 9. Reviewer's bottom line

The Dirichlet theorem is real, and it is the substantial piece of work here. Every one of its
eleven steps survived independent re-derivation, two of its exact algebraic identities were
confirmed symbolically to be identities rather than inequalities, its scalar minimization is
sharp, and twenty-four independent exact-moment computations found no violation of either the
theorem or its quantitative refinement. The countermodel is likewise clean and its universal
quantifier is genuinely established rather than sector-by-sector hand-waved.

Against that: the **Bochner identity is asserted with a proof that cannot work**, and I can
demonstrate concretely that it cannot, because the properties its proof names are satisfied by
a Stein kernel that violates the identity at order $\eps^2$. The **manuscript's endpoint proof
contains a false commutation claim** that the dossier itself knows to be false and repairs
elsewhere — the two files under audit contradict each other on the decisive step. And the
route's most quotable slogan, "CMH is strictly stronger than KLS", is **not a theorem**; it is a
plausible expectation dressed as one, and it currently sits in the ledger at `status: proved`.

None of these three is fatal. Two are writing failures around true statements and one is an
overclaim that a rewording fixes. But `check_ledger.py` was one empty file away from certifying
all three, which is the situation hard constraint 4 of `CLAUDE.md` exists to describe.
