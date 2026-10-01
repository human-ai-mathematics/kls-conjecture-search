---
verdict: pass
authors:
  - prover w4p04, claude-fable-5, 2026-08-30
reviewer: reviewer-fiber-root, unknown, 2026-09-06
fingerprints:
  solutions/lem-fiber-root-degree-two.md: a3a1c477d045824928fcbcfd65e04f381551cdca076448e87acc7953783f10e3
  lem:fiber-root-degree-two: a5c0cb72ddb6f073b7035b72173b2ba7d3652b6d33821866c122000b29870f0e
  lem:conditional-fiber-form: f2110f8c5c36056fda52257a3ad145a50f7c460b5bdc6b9ec4146e907db3cec2
  prop:conditional-fiber-root-obstruction: 4879b9619c0db837d35837800889e002d0ca3ba085521cbccc7d0a671435f67f
---

# Degree-two root-frame pencil identity — independent certification review

Reviewer run id `w5r02`, lens `certify`, concurrency key
`review:solutions/lem-fiber-root-degree-two.tex`. This review was launched cold, without the
author's conversation, and reconstructs the argument from the repository artifacts only. The
author's checkpoint `research/explorations/2026-08-30-prover-fiber-root-degree-two-w4p04.md`
was opened solely to confirm the author identity in the dossier header; nothing in it was
treated as evidence. This is the review the wave-four orchestrator record
(`research/explorations/2026-08-31-orchestrator-kls-angles-wave-w4.md`) planned as `w4r05`,
which was killed before writing anything.

## Scope and immutable dossier

Reviewed file: `solutions/lem-fiber-root-degree-two.tex` at HEAD `5b772c9`, SHA-256

```
3028534cb2917ec9df1362aeee7fa61fc402b26a39cc9f6a597aad7e6709f018
```

(1005 lines, working tree clean). The commit `8edb752` named in the orchestrator record holds
an earlier copy of the same file; `git diff 8edb752 HEAD` on it is one header-only hunk
(comment lines 1–39: the legacy `checked_by`/`reviewer`/`review` header fields were removed
by the template migration `29be4d6`). No line of mathematics differs.

The certifying scope is exactly the node `lem:fiber-root-degree-two` and this dossier. The
dossier has two claims: an unconditional Theorem (the pencil identity) and a Corollary
(degree-two dual certificates) whose only hypothesis is the certified root-frame
identification.

## Findings

### 1. Statement agreement

Three texts were compared: the dossier Theorem plus Corollary; the ledger `summary:`; and the
manuscript lemma at `\label{lem:fiber-root-degree-two}` in
`modules/kls/45-conditional-fiber-frame.tex` (lines 179–195). They agree mathematically:

- the space is the degree-$\le2$ polynomial quotient $V_{m,2}$ of $L^2(\mu)$ modulo
  constants, $\mu$ the uniform (flat Dirichlet) law on $\Delta_{m-1}$; polynomials of degree
  $\le2$ in $P$ and in the isotropic $X=R_m(P-\tfrac1m\mathbf 1)$ are the same space, so the
  manuscript's "isotropic" qualifier changes nothing;
- $K(f,f)=\tfrac{12}{m^2(m+1)}\sum_{i<j}\mathbb E[\operatorname{Var}_{ij}(f)/(P_i+P_j)^2]$ is
  literally the manuscript's `eq:conditional-root-form` and the ledger's formula, with
  $\operatorname{Var}_{ij}$ the conditional variance given all coordinates other than $i,j$
  (the manuscript's "redistribution of $(P_i,P_j)$ with their sum fixed");
- $G=\operatorname{Var}$, $\lambda_{\min}(K,G)=(m+2)(m+3)/(5m^2)$ for every $m\ge3$, attained
  exactly on $\mathbb R[\,|X|^2-(m-1)\,]$;
- the consequences (every degree-two dual certificate has objective $\ge(m+2)(m+3)/(5m^2)>1/5$;
  no vanishing degree-two refuter sequence; any fixed-degree polynomial dual refuter needs
  degree $\ge3$; $\Lambda_{m,2}\ge(m+2)(m+3)/(5m^2)$) are conditional, in all three texts, on
  the identification of $K$ with the conditional-fiber root pencil; and
- the non-claims coincide: no upper bound on $\Lambda_{m,2}$, nothing at degree three, nothing
  about the full $L^2$ gap.

The dual-certificate framework and $\Lambda_{m,2}$ are not defined inside the manuscript
module; the dossier restates them self-containedly (its eq. `sol-frd2-certificate` is the
factored form $Z=\sum_r w_rc_rc_r^T$ of equations (44)–(47) of the w1f01 probe checkpoint it
names, and its $\Lambda_{m,2}$ is (43) there with $d=m-1$). The dossier's definitions are what
this review certifies the Corollary against. That the manuscript uses the symbol without a
local definition is a manuscript-side presentation matter for the `sync` lens, not a defect of
the proof.

### 2. Barriers

The node has no `bounded_by` edge and no `heuristic_barriers`. The dossier's consistency
paragraph against `prop:conditional-fiber-root-obstruction` (full-$L^2$ root gap
$O(m^{-2})$) and the imported `prop:sasada-negative-exchange` is correct: both bounds are
witnessed by non-polynomial (cap-type) tests, so a degree-two floor bounded away from zero
does not contradict them. No Eldan-localization proof shape occurs.

### 3. Hypothesis accounting

Used in the Theorem: $P\sim\operatorname{Dir}(1,\dots,1)$ (the moment formula and the uniform
pair fibre both need the flat shape); $m\ge3$ (needed for the $p_1p_3$ coefficient in the
independence of $L,Q$, for the two-orbit count in $\operatorname{Hom}(M,N)$, and for the sign
of the factor $m-2$ in the standard sector); the pair-form definition of $K$. The isotropic
normalisation $R_m$ is used only to rewrite the minimiser as $|X|^2-(m-1)$ — the dossier says
so explicitly — and is otherwise idle: a sharpening opportunity, not a defect.

Used in the Corollary in addition: the certified identification
$K(f,f)=(m-1)\int\mathcal Q_\theta[f]\,d\rho_{\rm root}$ for polynomial $f$; admissibility of
$\rho_{\rm root}$ (the tight-frame identity $(m-1)\int\theta\theta^T d\rho_{\rm root}=I_{H_0}$);
finiteness of $\mathcal Q_\theta[f]$ for polynomial $f$ (log-concavity of the simplex through
the certified factor-$4$ bound). No hypothesis is used without being stated.

### 4. Dependencies and applicability

`depends_on` is `lem:conditional-fiber-form` and `prop:conditional-fiber-root-obstruction`.
Both are `status: proved`, `provenance: internal`, with `proofs[].mode: agent` pointing at
`solutions/conditional-fiber-frame-structure.tex` and the persisted review
`research/reviews/2026-08-27-conditional-fiber-frame-structure-proof-review.md` (author and
reviewer distinct from each other and from the present author and reviewer). I read that
dossier's definitions (`eq:sol-fiber-form`, `eq:sol-fiber-max-domain`) and its Proposition
`prop:sol-conditional-fiber-root-obstruction`, whose `eq:sol-fiber-root-form` is exactly the
identification the Corollary assumes, for the same $\operatorname{Var}_{ij}$ convention. The
Theorem uses neither dependency. No open node enters. The node has no `assumes`; the
Corollary's "granting the identification" is an antecedent that is itself a certified fact, so
it is correctly a `depends_on`, not an `assumes` (P2 does not bite).

### 5. Citation debt

The dossier contains no `\cite`. External inputs, all classical textbook facts and classified
`published`:

- Gamma–Dirichlet factorisation ($E_i/S$ is flat Dirichlet and independent of
  $S\sim\Gamma(m,1)$) and $\mathbb E S^r=\Gamma(m+r)/\Gamma(m)$ — standard; I re-derived the
  resulting moment formula.
- Complete reducibility and Schur's lemma over $\mathbb R$, orbit counting for permutation
  modules, multiplicity via $\operatorname{Hom}$, and one-dimensionality of invariant bilinear
  forms on an absolutely irreducible module (facts F1–F5) — standard; each is stated with the
  $\operatorname{End}(E)=\mathbb R$ hypothesis it needs, and the dossier verifies that
  hypothesis for the three irreducibles it uses.
- The certified structural dossier (internal, agent-certified) — used only by the Corollary.

No preprint is cited. No literature request is needed.

### 6. The steps, line by line

**Normalisation and forms.** $\mu$ flat on $\Delta_{m-1}$; $K,G$ as displayed; both are
$S_m$-invariant by exchangeability and by invariance of the set of pairs. Correct.

**Dirichlet moments (Lemma `sol-frd2-moments`).** From the factorisation,
$\prod a_i!=\mathbb E S^{|a|}\cdot\mathbb E\prod P_i^{a_i}$, giving
$\mathbb E\prod P_i^{a_i}=(m-1)!\prod a_i!/(m-1+|a|)!$. I recomputed every entry of the table
with $D_r=m(m+1)\cdots(m+r-1)$: $1/m$, $2/D_2$, $1/D_2$, $6/D_3$, $2/D_3$, $24/D_4$, $6/D_4$,
$4/D_4$, $2/D_4$, $1/D_4$. All correct. Consequences: $\mathbb E s=2/m$,
$\mathbb E s^2=(4+2)/D_2=6/D_2$, $\mathbb E(P_a-P_b)^2=(4-2)/D_2=2/D_2$. Correct.

**Pair fibre (Lemma `sol-frd2-pair`).** Conditional on the other coordinates the density of
$(P_i,P_j)$ on the segment $P_i+P_j=s$ is constant, so $\delta/s=2P_i/s-1$ is uniform on
$[-1,1]$ independently of $\mathcal F_{ij}$; the face $\{s=0\}$ is null. With
$\mathbb EV^2=\tfrac13$, $\mathbb EV^4=\tfrac15$, odd moments zero:
$\operatorname{Var}(\delta)=s^2/3$, $\operatorname{Var}(\delta^2)=s^4(\tfrac15-\tfrac19)=4s^4/45$,
$\operatorname{Cov}(\delta,\delta^2)=0$. The substitution table
($p_i^2=\tfrac{s^2}4+\tfrac s2\delta+\tfrac14\delta^2$, $p_ip_j=\tfrac{s^2-\delta^2}4$,
$p_ip_\ell=\tfrac{p_\ell}2(s+\delta)$) is correct; $\beta_f$ has degree $\le1$, $\gamma_f$ is a
constant. Since $\alpha_f,\beta_f,\gamma_f$ are $\mathcal F_{ij}$-measurable,
$\operatorname{Cov}_{ij}(f,g)=\beta_f\beta_g s^2/3+\gamma_f\gamma_g\,4s^4/45$, and dividing by
$s^2$ gives a bounded polynomial integrand. So $K$ is finite, bilinear, symmetric, positive
semidefinite and descends to $V_{m,2}$. Correct.

**Representation facts (F1)–(F5).** Correctly stated for real representations, with the
absolute-irreducibility hypothesis where it is needed.

**The three irreducibles (Lemma `sol-frd2-irreducibles`).** $\dim\operatorname{End}(M)=2$
(two orbits on $[m]^2$), $M^{S_m}$ one-dimensional, hence $\mathbf 1^\perp$ has
$\operatorname{End}=\mathbb R$ and is irreducible; the vanishing of both cross-Homs between
$\mathrm{triv}$ and $C$ follows from F1–F2 (a nonzero equivariant map $C\to\mathrm{triv}$ would
give a trivial quotient, hence a trivial submodule of $C$). For $N$ and $m\ge4$:
$\dim\operatorname{End}(N)=3$ (three intersection sizes), $\dim\operatorname{Hom}(M,N)=2$,
$\dim N^{S_m}=1$, so $\mathrm{std}$ has multiplicity one, and the remainder $\mathrm X$ has
$\operatorname{End}=\mathbb R$, is irreducible, of dimension
$\binom m2-1-(m-1)=m(m-3)/2$, and is not $\mathrm{triv}$ or $\mathrm{std}$. At $m=3$ the
intersection-size-$0$ orbit is absent and $N=\mathrm{triv}\oplus\mathrm{std}$, $3=1+2$.
Correct.

**Decomposition of $V_{m,2}$ (Lemma `sol-frd2-decomposition`).** The kernel of
$W_{\rm poly}\to V_{m,2}$ is computed correctly: a degree-$\le2$ polynomial constant on the
simplex is constant on the hyperplane $\sum p_i=1$, hence of the form
$c+(\sum p_i-1)\ell$ with $\ell$ affine; zero constant term forces $c=\ell(0)=b_0$, giving
$\{b_0\sum p_i+(\sum p_i-1)\sum b_ip_i\}\cong 2\,\mathrm{triv}\oplus\mathrm{std}$, injectivity
by comparing quadratic parts. $W_{\rm poly}\cong M\oplus M\oplus N$ has multiplicities
$(3,3,1)$; subtracting $(2,1,0)$ gives $\mathrm{triv}\oplus\mathrm{std}\otimes\mathbb R^2\oplus\mathrm X$,
$\dim=1+2(m-1)+m(m-3)/2=(m-1)(m+2)/2=\binom{m+1}2-1$. Parts (1)–(3): $[f_0]\ne0$ (coefficient
of $p_1p_2$ would be $2$); $L,Q$ independent (the $p_1p_3$ coefficient forces $b=0$, then
$a=b_0=-a$); the two image copies of $\mathrm{std}$ are distinct by F4–F5 and span the
$2(m-1)$-dimensional isotypic part; for $m\ge4$ the vector
$v=x_{12}-x_{23}-x_{14}+x_{34}$ is orthogonal to $\sum x_{ij}$ and to every $u_k$ (I checked
all four incidence cases and $k\ge5$), so lies in $W_{\mathrm X}(N)$, maps to
$F=[(p_1-p_3)(p_2-p_4)]$, and $F\ne0$ since the left side has no $p_i^2$ term but a nonzero
$p_1p_2$ term. Correct throughout.

**Invariant pencil reduction (Lemma `sol-frd2-reduction`).** Cross-isotypic orthogonality of an
invariant form is Schur; the tensor description $B(T_au,T_bu')=\widehat B_{ab}J_E(u,u')$ is F5;
the sum formula $B(f,f)=\sum_\alpha s_\alpha^T\widehat Bs_\alpha$ over a $J_E$-orthonormal
basis gives the equivalence "$B\ge0$ (resp. $>0$) on $W_E$ iff the $k\times k$ Gram matrix
at any seed $v_0\ne0$ is $\succeq0$ (resp. $\succ0$)". Correct.

**Trivial sector.** For every pair $(\beta,\gamma)=(0,\tfrac12)$, so
$E_{ij}=\tfrac4{45}\cdot\tfrac14\cdot\tfrac6{D_2}=\tfrac2{15D_2}$;
$K(f_0,f_0)=\tfrac{12}{m^2(m+1)}\cdot\tfrac{m(m-1)}2\cdot\tfrac2{15m(m+1)}=\tfrac{4(m-1)}{5m^2(m+1)^2}$.
$\mathbb Ef_0=\tfrac2{m+1}$, $\mathbb Ef_0^2=\tfrac{24m+4m(m-1)}{D_4}=\tfrac{4m(m+5)}{D_4}$,
and $(m+5)(m+1)-(m+2)(m+3)=m-1$ gives $G(f_0,f_0)=\tfrac{4(m-1)}{(m+1)^2(m+2)(m+3)}$. Quotient
$(m+2)(m+3)/(5m^2)$. On the simplex $|X|^2=m(m+1)(f_0-\tfrac1m)$, so
$[|X|^2-(m-1)]=m(m+1)[f_0]$. Correct.

**Standard sector.** The $(\beta,\gamma)$ table for $L=p_1-p_2$, $Q=p_1^2-p_2^2$ on the pair
types $(1,2)$, $(1,j)$, $(2,j)$ is correct (I re-expanded each). Pair energies:
$E_{12}(L,L)=\tfrac13$, $E_{1j}(L,L)=\tfrac1{12}$, $E_{12}(L,Q)=\tfrac2{3m}$,
$E_{1j}(L,Q)=\tfrac1{6m}$, $E_{12}(Q,Q)=\tfrac2{D_2}$,
$E_{1j}(Q,Q)=\mathbb Es^2(\tfrac1{12}+\tfrac1{180})=\tfrac8{15D_2}$. Sums over the
$1+2(m-2)$ contributing pairs: $\tfrac m6$, $\tfrac13$, $\tfrac{2(8m-1)}{15D_2}$. After the
prefactor: $K(L,L)=\tfrac2{m(m+1)}$, $K(L,Q)=\tfrac4{m^2(m+1)}$,
$K(Q,Q)=\tfrac{8(8m-1)}{5m^3(m+1)^2}$. Variances: $\tfrac2{D_2}$, $\tfrac{12-4}{D_3}$,
$\tfrac{48-8}{D_4}$. Normalised by $m(m+1)/2$ and subtracting $\lambda^*\widetilde G$:
$(11)=\tfrac{(4m+3)(m-2)}{5m^2}$, $(12)=\tfrac{6(m-2)}{5m^2}$,
$(22)=\tfrac{12(m-2)}{5m^2(m+1)}$; the bracketed matrix has determinant
$\tfrac{12(4m+3)}{m+1}-36=\tfrac{12m}{m+1}>0$ and positive diagonal, and $m-2>0$. So
$K-\lambda^*G\succ0$ on $W_{\rm std}$ for every $m\ge3$. All algebra rechecked, including the
factorisation $4m^2-5m-6=(4m+3)(m-2)$ and the value at $m=3$.

**Two-row sector ($m\ge4$).** The ten-row $(\beta,\gamma)$ table for
$F=(p_1-p_3)(p_2-p_4)$ is correct; I re-expanded the six pairs inside $\{1,2,3,4\}$ (signs of
$\gamma=\mp\tfrac14$ and the $\beta$'s) and the four far-pair types, and the pair count
$6+4(m-4)+\binom{m-4}2=\binom m2$. Energies $\tfrac2{3D_2}$ (twice), $\tfrac1{5D_2}$ (four
times), $\tfrac1{6D_2}$ ($4(m-4)$ times), total $\tfrac{2(5m-4)}{15D_2}$, so
$K(F,F)=\tfrac{8(5m-4)}{5m^3(m+1)^2}$. $\mathbb EF=0$ and
$\mathbb EF^2=(16-16+4)/D_4=4/D_4$. Ratio $\tfrac{2(5m-4)}{m+1}\lambda^*$ with
$2(5m-4)-(m+1)=9(m-1)>0$. Correct.

**Assembly.** $\Phi=K-\lambda^*G$ is block-diagonal across the three isotypic parts, zero on
the one-dimensional trivial part, positive definite on the other two; hence
$K\ge\lambda^*G$ on $V_{m,2}$ with equality exactly on $\mathbb R[f_0]$, so
$\lambda_{\min}=\lambda^*$ attained exactly on the radial line. $(m+2)(m+3)>m^2$ gives
$\lambda^*>\tfrac15$, and $\lambda^*\to\tfrac15$. The $m=3$ case (no $\mathrm X$ part) is
handled explicitly. Correct.

**Corollary.** Given the identification: applying the direction bound at the $m(m-1)$ atoms of
$\rho_{\rm root}$ and averaging, $\sum_rw_rK(c_r,c_r)\le\operatorname{Tr}\bigl(M\,(m-1)\!\int\theta\theta^Td\rho_{\rm root}\bigr)=\operatorname{Tr}M\le\varepsilon$;
the Theorem gives $\sum_rw_rK(c_r,c_r)\ge\lambda^*\sum_rw_rG(c_r,c_r)=\lambda^*$. Parts (2)
and (3) follow: the objective floor is uniform in $m$, and the supremum defining
$\Lambda_{m,2}$ dominates its value at $\rho_{\rm root}$. The quantifier order is right (the
certificate must beat every direction; the root frame is one admissible frame). Correct.

### 7. Standalone build

`cd solutions && latexmk -pdf -interaction=nonstopmode -outdir=../build lem-fiber-root-degree-two.tex`
exits 0 with zero TeX errors. The seven unresolved references are the manuscript labels
`sec:conditional-fiber-frame`, `conj:conditional-fiber-frame`, `eq:conditional-root-form`, the
expected standalone behaviour permitted by `solutions/README.md`. `python3 scripts/check.py`
reports 0 errors.

### Defect location, not evidence

Following the numerical record `research/explorations/2026-08-30-finum-fiber-frame-dual-w4f01.md`
only to look for a defect, I recomputed the pencil in exact rational arithmetic from the raw
definition (own script, pure `fractions`, not a run artifact) at $m=3,\dots,7$: $K-\lambda^*G$
is positive semidefinite with a one-dimensional kernel spanned by the radial class, and every
sector Gram entry of Lemmas `sol-frd2-standard` and `sol-frd2-tworow` matches. This located
no defect. Per `CLAUDE.md` constraint 2 and the reviewer contract it certifies nothing; the
verdict rests on the line-by-line reading above.

## Corrections

None required. Two editorial observations, neither affecting the proof:

- Remark `rem:sol-frd2-unclosed` describes the two dependencies as "`checked_by: agent`", the
  pre-migration header vocabulary; the current ledger records them as `proofs[].mode: agent`.
  The statement is true in substance.
- The manuscript lemma uses $\Lambda_{m,2}$ and "the all-frame min–max framework" without a
  local definition in `modules/kls/45-conditional-fiber-frame.tex`; the dossier defines them.
  A `sync`-lens item, outside this review.

## Exclusions

This review does not certify `conj:conditional-fiber-frame`, any statement about $\Lambda_{m,k}$
for $k\ge3$, any upper bound on $\Lambda_{m,2}$, any statement about the full $L^2$ root-frame
gap beyond the already certified `prop:conditional-fiber-root-obstruction`, optimality of the
root orbit among admissible frames, the ledger admission of the dual-certificate framework as
a node, the imported `prop:sasada-negative-exchange`, or anything about KLS. The numerical
artifacts named in Remark `rem:sol-frd2-artifacts` are not reviewed and carry no weight here.
