---
type: exploration
date: "2026-09-06"
outcome: proposed
approach: ap:cmh-gate-zero
nodes:
  - lem:linear-sector-third-moment
  - cor:gate-zero-third-moment
---
# Researcher (`prove`): dossier for `lem:linear-sector-third-moment` and `cor:gate-zero-third-moment`

Date: 2026-09-06. Role: `researcher`, lens `prove`. Agent identity `/w5/researcher-third-moment`.
Run id `w5p02`. Concurrency key held: `solution:solutions/lem-linear-sector-third-moment.tex`.

## What was produced

One standalone dossier, `solutions/lem-linear-sector-third-moment.tex`, header
`ledger-node : lem:linear-sector-third-moment; cor:gate-zero-third-moment`, no certification
fields. It compiles standalone (`cd solutions && latexmk -pdf -interaction=nonstopmode
-outdir=../build lem-linear-sector-third-moment.tex`, 7 pages; only cross-module `??`/`[?]`,
two cosmetic overfull boxes). No `proofs[]` record names it: it is an uncertified draft with
no ledger value until an independent review certifies it.

## What is proved, and under which hypotheses

Standing hypotheses $(\mathrm H)$: $\varphi\in C^2(\R^n)$ convex with $\nu=e^{-\varphi}\,dy$ a
probability measure; $\mu=(\nabla\varphi)_\#\nu$ absolutely continuous, isotropic, with
$\E_\mu|X|^3<\infty$; $\E_\nu\|D^2\varphi\|_{\mathrm{HS}}^2<\infty$. The manuscript's
hypotheses (isotropic log-concave moment measure of a $C^2$ convex $\varphi$ with finite
Hessian energy) imply $(\mathrm H)$ — the dossier proves this from the manuscript's convention
"log-concave = density $e^{-V}$ on the convex support, $V$ convex", via a self-contained
linear-growth lemma for integrable convex functions. Log-concavity is used for nothing else.

Proved from $(\mathrm H)$, with no ledger dependency and no literature import inside any proof:

1. **Stein kernel made rigorous without injectivity.** On $G=\{\det D^2\varphi>0\}$ the map
   $\nabla\varphi$ is injective and $(\nabla\varphi)^{-1}(\nabla\varphi(G))=G$ (convexity:
   two points with the same gradient bound a segment on which $\varphi$ is affine, so $H$
   degenerates at both endpoints); $\nu(G)=1$ because the critical values of a $C^1$ map
   $\R^n\to\R^n$ are Lebesgue-null (proved in full, elementary cube-counting) and
   $\mu\ll\mathrm{Leb}$. Hence $\tau=H\circ(\nabla\varphi|_G)^{-1}$ is defined on an open set
   of full $\mu$-measure, agrees with `eq:stein-kernel-def`, and $\tau\circ\nabla\varphi=H$
   $\nu$-a.e., so every $\E_\mu[\Phi(X,\tau)]=\E_\nu[\Phi(\nabla\varphi,H)]$ exactly.
2. **Quadratic Stein identity** $\E_\mu[X_if]=\sum_j\E_\mu[\tau_{ij}\partial_jf]$ for
   polynomials $f$ of degree $\le2$: divergence theorem on balls, boundary terms killed along a
   shell sequence selected by Fubini in polar coordinates from $\int(1+|\nabla\varphi|^2)d\nu<\infty$,
   dominated convergence for the interior. Consequences: $\E_\mu\tau=\E_\nu H=\Id$ and
   $\E[X_iX_jX_k]=\E[\tau_{ij}X_k]+\E[\tau_{ik}X_j]$.
3. **Total symmetry** of $N_{ijk}=\E_\mu[\tau_{ij}X_k]=\E_\nu[\varphi_{ij}\varphi_k]$ and
   $N=\tfrac12T_3(\mu)$. This follows from item 2 alone (compare the identity with $i,j$
   exchanged; first-pair symmetry then yields the $(13)$ transposition). The orchestrator's
   alternative divergence identity
   $(\varphi_{bi}\varphi_a-\varphi_{ba}\varphi_i)e^{-\varphi}=\partial_i(\varphi_b\varphi_ae^{-\varphi})-\partial_a(\varphi_b\varphi_ie^{-\varphi})$
   was verified but not needed; it would give the same symmetry without finite third moments.
4. **The lemma's display**: $\tau a=a+\tfrac12T_3(a)X+v_a$, $\E v_a=0$, $\E[v_a\otimes X]=0$,
   pairwise orthogonality, and $\E|\tau a|^2=|a|^2+\tfrac14\|T_3(a)\|_{\mathrm{HS}}^2+\E|v_a|^2$,
   by projecting each $L^2(\mu)$ entry of $\tau a$ onto $\operatorname{span}\{1,X_b\}$
   (orthonormal by isotropy); index bookkeeping $\E[(\tau a)_iX_b]=\sum_ka_kN_{ikb}=\tfrac12T_3(a)_{ib}$
   checked against $T_3(a)_{ib}=\sum_kT_{kib}a_k$.
5. **The corollary**, including $\E_\mu[\tau^2]=\E_\nu[H^2]$ (exact, not Jensen), $c\ge1$
   automatically, the $2\sqrt{c-1}$ class bound, the converse (a directional third moment
   above $2\sqrt3$ gives $a^\top\E_\nu[H^2]a>4$, negating `eq:gate-zero` in isotropic position),
   and the saturating example: $\varphi(y)=\sum(e^{y_j}-y_j)$, $\mu$ = product of centered
   exponentials, $\tau=\operatorname{diag}(1+x_j)$, $T_3(a)=\operatorname{diag}(2a_j)$,
   $\|T_3(a)\|_{\mathrm{HS}}=2$ for every unit $a$, $\E\tau^2=2\,\Id$, $v_a=0$.
6. **Third-derivative form** $\E_\nu[\varphi_{ijk}]=\tfrac12\E_\mu[X_iX_jX_k]$ under the
   explicit extra hypothesis $\varphi\in C^3$, $D^3\varphi\in L^1(\nu)$ (shell sequence from
   $\|H\|_{\mathrm{HS}}\in L^1(\nu)$).

## Unclosed steps and hypothesis accounting (for the reviewer)

- No proof step is left open under $(\mathrm H)$. The one place where the manuscript lemma
  says more than $(\mathrm H)$ supports is its last sentence
  "$\E_\nu[\partial_{ijk}\varphi]=\tfrac12\E_\mu[X_iX_jX_k]$", which needs
  $\partial_{ijk}\varphi$ to exist and be $\nu$-integrable. The dossier proves it under exactly
  that extra hypothesis (Proposition 7 / Remark "Which hypothesis the manuscript's last
  sentence uses") and proves unconditionally the second-derivative form
  $\E_\nu[\varphi_{ij}\varphi_k]=\tfrac12\E_\mu[X_iX_jX_k]$, which is what the gap-mode
  coefficient in the decomposition actually is. The dossier does not assert the identification
  with the coefficient tensor of the uncertified `lem:cmh-linear-spectral-resolution`.
- Two published results are cited only in remarks, never in a proof: Klartag 2013 Thm 1.1
  (pointwise Hessian bound on the compact-target class, so that class satisfies $(\mathrm H3)$;
  already audited in `2026-08-27-literature-scout-cmh-hessian-recovery-w3l01.md`), and
  Cordero-Erausquin–Klartag 2015 essential uniqueness (identifying the hypothesis' $\varphi$
  with "the" potential in `conj:gate-zero`; $\E_\nu H^2$ is translation-invariant).
- Fence check: neither node carries `bounded_by` or `heuristic_barriers`. The six
  obstruction nodes and `prop:letwin-not-gate-zero` are audited in the dossier's closing
  paragraph; nothing here claims gate zero or a KLS-strength statement, and P1 is untouched.

## Suggested manuscript touch (proposal only; orchestrator's decision)

If the dossier is certified, the last sentence of `lem:linear-sector-third-moment` could
read "…is one half of the third-moment tensor,
$\E_\nu[\partial_{ij}\varphi\,\partial_k\varphi]=\tfrac12\E_\mu[X_iX_jX_k]$, and, when
$\varphi\in C^3$ with $D^3\varphi\in L^1(\nu)$, $\E_\nu[\partial_{ijk}\varphi]=\tfrac12\E_\mu[X_iX_jX_k]$",
so that the statement carries the hypothesis its third-derivative form uses. This changes no
mathematics and is not required for certification of the display.

## Deferred artifact

Future `proofs[].artifact`: `solutions/lem-linear-sector-third-moment.tex` for both
`lem:linear-sector-third-moment` (proposed `depends_on: []`) and `cor:gate-zero-third-moment`
(existing `depends_on: ['lem:linear-sector-third-moment']`). No ledger delta is applicable
until an independent `reviewer` certifies it; no ledger, manuscript, review or portfolio file
was written by this run.

## Portfolio delta (proposal for the synthesizer)

`ap:cmh-gate-zero`: remains `queued`/unchanged in objective; note that its falsification
channel now has a drafted analytic lower bound on the gate matrix needing only third
moments (this dossier), pending review. Not a blocker change. No duplication found.
