---
type: proof-review
date: "2026-09-06"
verdict: pass
authors:
  - /w5/researcher-third-moment
reviewer: /w5/reviewer-third-moment
nodes:
  - lem:linear-sector-third-moment
  - cor:gate-zero-third-moment
solutions:
  - solutions/lem-linear-sector-third-moment.tex
---

# The linear sector and the third moment — independent certification review

Reviewer run id `w5r03`, lens `certify`, concurrency key
`review:solutions/lem-linear-sector-third-moment.tex`. Subject:
`solutions/lem-linear-sector-third-moment.tex`, 577 lines, SHA-256
`feca15ac18da3db660562f1583e1ac38ab1b47514bb7856de90a0c8818e1acfc` (uncommitted working-tree
file; no `proofs[]` record names it at review time). Ledger nodes
`lem:linear-sector-third-moment` and `cor:gate-zero-third-moment`, both `status: open`,
`provenance: internal`, `file: modules/kls/41-cmh-normalization.tex`. Manuscript statements:
`modules/kls/41-cmh-normalization.tex` lines 311–331 (lemma) and 340–353 (corollary), read in the
working tree after the orchestrator's rewording of the lemma's last sentence (lines 327–330);
the ledger summaries were read from the working-tree `ledger.yaml`.

The author's checkpoint `research/explorations/2026-09-06-researcher-third-moment-w5p02.md`
was opened only to confirm the author identity and the run id; nothing in it was used as
evidence. The author's conversation was not available and was not used. The reviewer authored
no part of the dossier.

## 1. Statement agreement (lens item 1)

**Lemma.** Manuscript hypotheses: $\mu$ isotropic log-concave probability on $\R^n$, the moment
measure of a convex $\varphi\in C^2(\R^n)$ with $\E_\nu\|D^2\varphi\|_{\HS}^2<\infty$;
$\tau=\tau_\mu$ the canonical Stein kernel `eq:stein-kernel-def`
($\tau_\mu(x)=H((\nabla\varphi)^{-1}(x))$, `modules/kls/04-family-moment-map.tex` line 197–200).
Conclusions: for every $a$, $\tau a=a+\tfrac12T_3(a)X+v_a$ orthogonally in $L^2(\mu;\R^n)$ with
$\E v_a=0$, $\E[v_a\otimes X]=0$, the Pythagorean identity `eq:linear-sector-third-moment`;
"Equivalently, $\E_\nu[\partial_{ij}\varphi\,\partial_k\varphi]=\tfrac12\E_\mu[X_iX_jX_k]$;
when moreover $\varphi\in C^3$ with $D^3\varphi\in L^1(\nu)$, this says that the gap-mode
coefficient tensor $\E_\nu[\partial_{ijk}\varphi]$ of Lemma `cmh-linear-spectral-resolution`
is one half of the third-moment tensor."

Dossier Theorem `thm:sol-lstm-main` under $(\mathrm H)$: (b) is the display and the
Pythagorean identity verbatim (with pairwise orthogonality of the three summands proved, which
is what "decomposes orthogonally" means); (a) is
$\E_\nu[\varphi_{ij}\varphi_k]=\E_\mu[\tau_{ij}X_k]=\tfrac12\E_\mu[X_iX_jX_k]$; (c) is
$\E_\nu[\varphi_{ijk}]=\tfrac12\E_\mu[X_iX_jX_k]$ under exactly the manuscript's extra
hypothesis ($\varphi\in C^3$, every $\varphi_{ijk}\in L^1(\nu)$, which is
$D^3\varphi\in L^1(\nu)$). Lemma `lem:sol-lstm-logconcave` shows the manuscript hypotheses imply
$(\mathrm H)$ (checked in §2 below), so the dossier's theorem is at least as strong as the
manuscript lemma. The word "Equivalently" is justified: (a) and (b) are each proved outright,
and I checked directly that (b) with its stated orthogonality gives back (a) by pairing
$(\tau a)_i$ with $X_b$ and varying $a$. Agreement holds.

On the phrase "gap-mode coefficient tensor of Lemma `cmh-linear-spectral-resolution`": the
manuscript sentence names $\E_\nu[\partial_{ijk}\varphi]$ by apposition, and the identity it
asserts about that tensor is the one the dossier proves. I confirmed that the (uncertified,
`status: open`) dossier `solutions/lem-cmh-linear-spectral-resolution.tex` defines its
coefficient as $(M_a)_{ib}=a_k\int\psi_{kib}\,d\eta$ (line 210), so the apposition matches that
lemma's definition; nothing here depends on that lemma (see §7).

**Ledger summary** of `lem:linear-sector-third-moment` restates the manuscript lemma sentence
by sentence, including the reworded last sentence with the $C^3$/$L^1$ proviso. Agreement
holds.

**Corollary.** Manuscript: under the lemma's hypotheses, for every unit $a$,
$\|T_3(a)\|_{\HS}^2\le4(a^\top\E_\mu[\tau^2]a-1)\le4(\lambda_{\max}(\E_\mu\tau^2)-1)$; on a
class with $\E\tau^2\preceq c\,\Id$ every directional third moment is $\le2\sqrt{c-1}$, gate
zero giving $2\sqrt3$ and sharp gate zero $2$, attained by products of centered exponentials;
conversely an isotropic law in the class with $\|T_3(a)\|_{\HS}>2\sqrt3$ for some $a$ refutes
gate zero. Dossier Corollary `cor:sol-lstm-gate` states exactly this under $(\mathrm H)$, adds
$c\ge1$ and $\E_\mu[\tau^2]=\E_\nu[H^2]$, and proves attainment by
Example `ex:sol-lstm-exponential`. The ledger summary of `cor:gate-zero-third-moment` matches.
One reading convention: in the manuscript's "for some $a$" I read $a$ as a unit vector, as the
corollary's opening quantifier fixes it (for non-unit $a$ the claim would be false by scaling);
the dossier says "unit $a$" explicitly. A one-word manuscript clarification is proposed to the
orchestrator below; it is not a disagreement between the proved statement and the intended one.

## 2. Hypothesis accounting (lens item 3)

Hypotheses actually used, and where:

- $\varphi\in C^2(\R^n)$ convex, $\nu=e^{-\varphi}dy$ a probability: the divergence-theorem
  computations (Prop. `sol-lstm-stein`, Prop. `sol-lstm-third-derivative`), the structure lemma
  (convexity makes gradient fibres segments on which $H$ degenerates), $H\succeq0$ hence
  $\tau\succeq0$, and the shell lemma. That $\nu$ is a probability is the manuscript's
  `eq:moment-measure` convention ($d\nu=e^{-\varphi}dy$ with $(\nabla\varphi)_\#\nu=\mu$ a
  probability).
- $\mu\ll\mathrm{Leb}$: only in Lemma `sol-lstm-structure`(ii), to make $\nu(\{\det H=0\})=0$
  through the Sard lemma, i.e. to give `eq:stein-kernel-def` a $\mu$-a.e. meaning.
- $\E_\mu|X|^3<\infty$: absolute convergence of $\E_\mu[X_if(X)]$ for quadratic $f$, and
  finiteness of $T_3$.
- Isotropy ($\E X=0$, $\E X\otimes X=\Id$): orthonormality of $\{\mathbf1,X_b\}$,
  $\E_\mu[\tau]=\Id$, $\E_\nu|\nabla\varphi|^2=n$, the $c\ge1$ step, and $\Sigma=\Id$ in the
  converse of the corollary.
- $\E_\nu\|D^2\varphi\|_{\HS}^2<\infty$: $\tau_{ij}\in L^2(\mu)$, the domination of the interior
  integrands, and the shell function $\|H\|_{\HS}$ in Prop. `sol-lstm-third-derivative`.
- Log-concavity of $\mu$: used only through Lemma `sol-lstm-logconcave`, i.e. to supply
  $\mu\ll\mathrm{Leb}$ (the `sec:notation` convention "density $e^{-V}$ on its convex support,
  $V$ convex") and $\E_\mu|X|^3<\infty$ (Lemma `sol-lstm-linear-growth`).
- For part (c) only: $\varphi\in C^3$, $D^3\varphi\in L^1(\nu)$, stated in the manuscript.

Used but unstated: none. Stated but not fully used: log-concavity — the theorem and corollary
hold for any isotropic moment measure that is absolutely continuous with finite third moment,
as the dossier's Remark `sol-lstm-hypotheses` records. This is a sharpening opportunity, not a
defect. Isotropy is used in the standard sense (centered, identity covariance), which is how the
manuscript uses the word throughout (e.g. `eq:kappa-def`).

## 3. Barriers (lens item 2)

Neither node carries `bounded_by` or `heuristic_barriers`; confirmed in the ledger. The
dossier's closing paragraph audits the six obstruction nodes and `prop:letwin-not-gate-zero`;
I agree with each line: the theorem is an exact identity on a fixed measure and the corollary an
implication whose antecedent is the open `conj:gate-zero`, so nothing here is a bound of
KLS-equivalent strength, no isoperimetric profile is used, and the constant-matrix estimate is
neither used nor claimed to imply gate zero. Program constraint P1: no member of the
trace-upgrade cluster is opened and no transfer between members is asserted.

## 4. Dependency and applicability (lens item 4)

`lem:linear-sector-third-moment` has no `depends_on`, and the dossier uses no ledger node: the
mean-Hessian identity and the general Stein identity `eq:stein-identity` are not cited; the
quadratic special case is proved from scratch. `cor:gate-zero-third-moment` has
`depends_on: [lem:linear-sector-third-moment]`, and its proof uses exactly Theorem
`sol-lstm-main`(b) plus the transport lemma; both are certified here together, so the edge is
closed by this review. No `assumes` is needed: the corollary's conditional clauses ("on any
class with $\E\tau^2\preceq c\,\Id$") are inside the statement, not antecedents of the node.
Per P2, neither node is a route target closure and neither is progress on `conj:kls`.

## 5. Citation debt (lens item 5)

Two external results appear, both only in remarks and in no proof step:

- `Klartag2013MomentMeasures` (Lecture Notes in Math. 2116, Springer): **published**. Its
  Theorem 1.1 pointwise Hessian bound is quoted in Remark `sol-lstm-specialisations` (and in
  the manuscript prose after the lemma) to say the compact-target class satisfies $(\mathrm H3)$.
  I could not open the source with my tools; since no certified step uses it, no verification
  request is needed. The statement "the compact-target regular class satisfies the hypothesis"
  is manuscript prose outside both nodes and is not certified here.
- `CorderoErausquinKlartag2015MomentMeasures` (J. Funct. Anal. 268 (2015)): **published**.
  Essential uniqueness of the moment potential up to translation is what identifies the
  $\varphi$ of the hypothesis with the potential in `conj:gate-zero`; the dossier records this in
  Remark `sol-lstm-hypotheses` together with the trivial translation invariance of
  $\E_\nu[H^2]$. The dossier's inequality $a^\top\E_\nu[H^2]a>4$ is proved for the given
  $\varphi$ without it.

No preprint is cited. No numerical evidence, run artifact, or `experiments/` path appears
anywhere in the file (grep-verified).

## 6. The steps (lens item 6)

Every step was re-derived independently. Findings, in dossier order:

1. **Lemma `sol-lstm-logconcave`.** Correct. The notation convention makes $\mu\ll\mathrm{Leb}$;
   extending $V$ by $+\infty$ off the support gives a convex $V$ with $\int e^{-V}=1$, and the
   linear-growth lemma yields all moments. Isotropy forces full dimension, so "density on the
   convex support" is a density on $\R^n$.
2. **Lemma `sol-lstm-linear-growth`.** Correct. $D=\{V<\infty\}$ has nonempty interior;
   $K=\{V\le m_0+1\}$ has finite measure by $e^{-(m_0+1)}\mathrm{Leb}(K)\le\int e^{-V}$; the
   cone $\operatorname{conv}(B_\delta(y_0)\cup\{z\})$ has volume
   $\tfrac1n\omega_{n-1}\delta^{n-1}|z-y_0|$ (for $n=1$ this is the segment length, with
   $\omega_0=1$), giving the diameter bound $\rho_0$; the convexity step
   $V(y)\ge m_0+(V(z)-m_0)/t$ with $t=\rho/|y-y_0|$ and $V(z)>m_0+1$ gives
   $V(y)\ge m_0+|y-y_0|/\rho$ outside $B_\rho(y_0)$; the subgradient bound handles the inside;
   the constants $C_1$, $C$ are right; $|y|^k\le k!\,\eps^{-k}e^{\eps|y|}$.
3. **Lemma `sol-lstm-sard`.** Correct and complete. $Z$ closed so $F(Z)$ is $\sigma$-compact
   (measurable); the integral form of the remainder gives norm $\le\omega(d)d$ because the
   segment stays inside the convex subcube; the range of the singular $DF(y_0)$ lies in a
   hyperplane $E'$; the cylinder volume $2\omega_{n-1}((L+\omega(d))d)^{n-1}\omega(d)d$ is
   right; $N^n d^n=n^{n/2}$, and the bound $2\omega_{n-1}n^{n/2}(L+\omega(d))^{n-1}\omega(d)\to0$.
4. **Lemma `sol-lstm-structure`.** (i) Correct: the two subgradient inequalities add to
   $0\ge0$, so $g(t)=\varphi(y_1+tw)-\varphi(y_1)-t\langle p,w\rangle$ is $C^2$, convex,
   $\ge0$, and vanishes at $0$ and $1$, hence on $[0,1]$; $g''\equiv0$ on $(0,1)$ and
   continuity give $g''(0)=\langle H(y_1)w,w\rangle=0$; positive semidefiniteness gives
   $H(y_1)w=0$. Injectivity on $G$ and $(\nabla\varphi)^{-1}(\Omega)=G$ follow. (ii) Correct:
   $\nabla\varphi(Z)$ is Lebesgue-null by step 3, $\mu$-null by absolute continuity, and
   $\nu(Z)\le\nu((\nabla\varphi)^{-1}(\nabla\varphi(Z)))=\mu(\nabla\varphi(Z))=0$; the inverse
   function theorem plus global injectivity on $G$ gives the $C^1$ diffeomorphism onto the open
   $\Omega$. (iii) Correct; on $\Omega$ the manuscript's formula is unambiguous by (i), and the
   complement is $\mu$-null. (iv) Correct: pushforward plus $\tau\circ\nabla\varphi=H$ on $G$
   with $\nu(G)=1$; the real-valued case via $|\Phi|,\Phi^\pm$.
5. **Lemma `sol-lstm-shells`.** Correct. Tonelli in polar coordinates gives
   $\int_0^\infty S(R)\,dR=\int Fe^{-\varphi}<\infty$ (with $\sigma_R$ the surface measure on
   $\partial B_R$, and counting measure on $\{\pm R\}$ for $n=1$); the selection
   $\{R\ge k:S(R)\le1/k\}$ has positive measure.
6. **Proposition `sol-lstm-stein`.** Correct. Integrability: $|X_if|\le C_f|X|(1+|X|^2)$
   uses the third moment; $\E_\mu\tau_{ij}^2=\E_\nu\varphi_{ij}^2<\infty$ by transport and
   $(\mathrm H3)$; $|\tau_{ij}|(1+|X|)\le\tfrac12\tau_{ij}^2+1+|X|^2$ is right. Divergence:
   $\partial_i[f(\nabla\varphi)e^{-\varphi}]=[\sum_j(\partial_jf)(\nabla\varphi)\varphi_{ji}-f(\nabla\varphi)\varphi_i]e^{-\varphi}$,
   and the ball identity `eq:sol-lstm-ibp-ball` follows (for $n=1$ the boundary term is
   $W(R)-W(-R)$, matching the counting-measure convention). Boundary term bounded by
   $C_f\int_{\partial B_R}(1+|\nabla\varphi|^2)e^{-\varphi}d\sigma_R$ with
   $\int(1+|\nabla\varphi|^2)d\nu=1+n$; shells kill it; dominated convergence on the interior
   since both integrands are in $L^1(\nu)$; transport gives `eq:sol-lstm-stein`.
7. **Corollary `sol-lstm-stein-consequences`.** Correct: $f=x_j$ gives
   $\E[\tau_{ij}]=\delta_{ij}$; $f=x_jx_k$ with $\partial_lf=\delta_{lj}x_k+\delta_{lk}x_j$
   gives $T_{ijk}=N_{ijk}+N_{ikj}$ (consistent at $j=k$).
8. **Lemma `sol-lstm-N`.** Correct. Finiteness by Cauchy–Schwarz; $N_{ijk}=N_{jik}$ by
   symmetry of $\tau$; subtracting the $(i\leftrightarrow j)$-exchanged identity gives
   $N_{ikj}=N_{jki}=N_{kji}$, i.e. invariance under the $(13)$ transposition; with $(12)$ this
   generates $S_3$; then $T_{ijk}=2N_{ijk}$.
9. **Proof of (b).** Correct. $\{\mathbf1,X_b\}$ orthonormal by isotropy;
   $\E[u_i]=a_i$; $\E[u_iX_b]=\sum_ka_kN_{ikb}=\tfrac12\sum_ka_kT_{kib}=\tfrac12T_3(a)_{ib}$,
   and I confirmed $T_3(a)_{ib}=\E[\langle X,a\rangle X_iX_b]=\sum_ka_kT_{kib}$ from the
   manuscript's definition; $v_a=(\mathrm{id}-P)$ applied entrywise; the three cross terms
   vanish as displayed; $\E|T_3(a)X|^2=\|T_3(a)\|_{\HS}^2$ by $\E[X_bX_c]=\delta_{bc}$.
10. **Proof of Corollary `sol-lstm-gate`.** Correct. $|(\tau^2)_{ij}|\le\|\tau\|_{\HS}^2$
    integrable; $\E_\mu[\tau^2]=\E_\nu[H^2]$ by transport; $|\tau a|^2=a^\top\tau^2a$ for
    symmetric $\tau$; the chain
    $\|T_3(a)\|^2=4(\E|\tau a|^2-1-\E|v_a|^2)\le4(a^\top\E[\tau^2]a-1)\le4(\lambda_{\max}-1)$;
    $c\ge\E|\tau a|^2\ge1$; the constants $2\sqrt3$ and $2$; the converse
    $a^\top\E_\nu[H^2]a>4$ is the negation of `eq:gate-zero` at $\Sigma=\Id$.
11. **Example `sol-lstm-exponential`.** Verified analytically: $e^{y}e^{-e^{y}}$ is the density
    of $\log E$, $E\sim\mathrm{Exp}(1)$; $\nabla\varphi=(e^{y_j}-1)$ so $\mu$ is the law of
    $(E_j-1)$, log-concave on $(-1,\infty)^n$, isotropic; $\E_\nu\|H\|^2=2n$;
    $\tau(x)=\mathrm{diag}(1+x_j)$; $\E(E-1)^3=6-6+3-1=2$; mixed $T_{ijk}$ vanish;
    $T_3(a)=\mathrm{diag}(2a_j)$; $\|T_3(a)\|_{\HS}=2|a|$; $\E[\tau^2]=2\Id$; $v_a=0$; $2=1+1+0$.
12. **Proposition `sol-lstm-third-derivative`.** Correct.
    $\operatorname{div}(\varphi_{ij}e^{-\varphi}e_k)=(\varphi_{ijk}-\varphi_{ij}\varphi_k)e^{-\varphi}$;
    boundary term bounded by $\int_{\partial B_R}\|H\|_{\HS}e^{-\varphi}d\sigma_R$ with
    $\|H\|_{\HS}\in L^1(\nu)$ by $(\mathrm H3)$; shells; both interior integrands in $L^1(\nu)$
    (the second by step 8); dominated convergence.

Steps I could not verify: none. Every lemma, proposition, corollary, and the example were
checked; the closing obstruction paragraph was checked against the ledger.

## 7. Independence from `lem:cmh-linear-spectral-resolution`

That node is `status: open` with a same-day audit
(`research/reviews/2026-09-06-lem-cmh-linear-spectral-resolution-audit.md`, a different
subject, not superseded by this report). The dossier's only mention of it is in the Scope
paragraph and in Remark `sol-lstm-third-derivative-hypothesis`, both disclaiming any use.
Confirmed: no proof step in this dossier invokes it, its dossier, or any of its definitions
($\mathsf N$, $\mathsf D$, $\mathsf R$, $\mathsf A_{\rm op}$ do not occur).

## 8. Standalone build (lens item 7)

`cd solutions && latexmk -pdf -interaction=nonstopmode -outdir=../build lem-linear-sector-third-moment.tex`:
exit 0, no TeX errors, two cosmetic overfull boxes, PDF written. All undefined references are
cross-module labels, and each was confirmed to exist under `modules/` (none is dangling).
`python3 scripts/check.py` reports 0 errors on the working tree before this report was added.

## Corrections

None required for certification. Two editorial notes for the orchestrator (manuscript) and the
researcher (dossier prose), neither touching a proved step:

1. `modules/kls/41-cmh-normalization.tex` line 352: "for some $a$" would be clearer as
   "for some unit $a$", matching the corollary's opening quantifier and the dossier.
2. The dossier's Scope paragraph (lines 53–58) and Remark `sol-lstm-third-derivative-hypothesis`
   (lines 486–489) describe the manuscript's last sentence as lacking the $C^3$/$L^1$ proviso.
   After the orchestrator's rewording the manuscript states that proviso itself, so the
   remark's account of the manuscript is stale. The mathematics (Theorem (c)) is exactly what
   the reworded sentence asserts. If the remark is edited, the file's hash changes and the
   edit should be recorded as editorial in a checkpoint; this report certifies the file at
   the SHA-256 above.

## Exclusions

- Nothing about `conj:gate-zero`, `conj:gate-zero-sharp`, or `conj:kls` beyond the exact
  implication in the corollary; no bound on $\kappa_n$.
- The manuscript prose after the lemma ("the compact-target regular class satisfies the
  hypothesis, since its Hessian is bounded"; "so does every exponential cone measure") is not
  part of either node and is not certified; the Klartag Theorem 1.1 bound it rests on was not
  checked against its source.
- The identification of $\E_\nu[\partial_{ijk}\varphi]$ with the coefficient tensor
  $(M_a)_{ib}$ of `lem:cmh-linear-spectral-resolution` is by that lemma's definition and is
  not a claim of this dossier; that lemma remains uncertified.
- The general Stein identity `eq:stein-identity` (for non-polynomial $f$) and the mean-Hessian
  identity `eq:mean-hessian-identity` are not certified here; only the degree-$\le2$ case is.
- On the compact-target class, whether $D^3\varphi\in L^1(\nu)$ holds is a separate claim not
  addressed by the dossier or this review.
