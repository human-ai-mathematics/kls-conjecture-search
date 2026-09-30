---
verdict: pass
authors:
  - claude-prover-w4p02
reviewer: proof-checker-w4r03
fingerprints:
  solutions/lem-mm-smallgap-fourth-moment.md: e06ceebeb8e44119c9f6229074f155a1ca6490262e0040da5aa3030391bfbbb8
  lem:mm-smallgap-fourth-moment: 5efc054693b4557b794756da70c6b5a5ba03e38dc8bd743eca82855cc796d1df
  thm:klartag-logn: 70dd5528111bc813bcfa6750d3afcfcdc31121dbf564fb0681db32265b576b60
---

# Small-gap fourth-moment bootstrap — independent proof review

Cold review of `solutions/lem-mm-smallgap-fourth-moment.tex`, reviewed SHA-256
`3a722083c961595dbaf8ed3e6b610b5dfe189f3d726c675479224bbaaabdd2a1`. The proof was
reconstructed from the dossier, the manuscript (`modules/kls/30-spectral-route.tex`,
`modules/kls/15-covariance-technology.tex`), the KLS ledger, and the bibliography. The
prover's conversation was not available and the prover's exploration record was consulted
only to confirm authorship. Author (`claude-prover-w4p02`) and reviewer
(`proof-checker-w4r03`) are distinct.

## Findings

### Statement agreement

The dossier theorem, the ledger `statement:` of `lem:mm-smallgap-fourth-moment`
(`research/kls/ledger.yaml`), and the manuscript lemma at
`\label{lem:mm-smallgap-fourth-moment}` in `modules/kls/30-spectral-route.tex` agree
mathematically. All three are the implication: if every isotropic log-concave law on
$\R^n$ satisfies $\CP\le K_n$, then every normalized first nonconstant eigenfunction
($\E_\mu f=0$, $\E_\mu f^2=1$, $-Lf=\lambda f$) of a regular isotropic approximant with
$\lambda\le3/(8K_n)$ satisfies $\E_\mu f^4\le2$, via
$\lambda\E f^4=3\E f^2|\nabla f|^2$ and Poincaré for $f^2$. The manuscript instantiates
$K_n$ as the constant of `thm:klartag-logn`; the dossier proves the implication for an
arbitrary $K_n$ satisfying the uniform Poincaré hypothesis and instantiates it by the
same import, so the dossier statement implies the manuscript statement. The Poincaré
convention $\Var(h)\le K_n\E|\nabla h|^2$ matches `thm:klartag-logn` in
`modules/kls/15-covariance-technology.tex`. The bound $2$ is universal, with
$\varepsilon$ entering only the qualitative finiteness of $\E f^4$, exactly as all three
surfaces state.

The header comment "candidate node, ledger acceptance pending" and the parallel remark
about `thm:klartag-logn` are stale: both nodes now exist in `research/kls/ledger.yaml`
(`lem:mm-smallgap-fourth-moment` with `status: open`,
`depends_on: [thm:klartag-logn]`; `thm:klartag-logn` with `status: imported`,
`import_class: published`). Editorial only; the created statements are the ones reviewed.

### The steps, checked line by line

**Step 1 (qualitative $L^4$ finiteness).** Bakry–Émery for $\nabla^2V\succeq\varepsilon
I$ gives a logarithmic Sobolev inequality with $\varepsilon$-dependent constant, and Gross
hypercontractivity supplies $t_0(\varepsilon)$ with
$\norm{P_{t_0}g}_{L^{q(t_0)}}\le\norm g_{L^2}$, $q(t_0)\ge4$; for a probability measure
$\norm\cdot_{L^4}\le\norm\cdot_{L^{q}}$ for $q\ge4$. Since $P_{t_0}f=e^{-\lambda t_0}f$,
$\norm f_{L^4}\le e^{\lambda t_0}<\infty$. Correct, and used only for finiteness; the
$\varepsilon$-dependence contaminates no constant in the conclusion. Smoothness of $f$ by
elliptic bootstrap for $\Delta f-\nabla V\cdot\nabla f=-\lambda f$ with smooth
coefficients, and $f$ in the form domain with $\E|\nabla f|^2=\langle
f,-Lf\rangle=\lambda$, are standard and correctly invoked. $\lambda>0$ for a first
nonconstant eigenfunction is correctly argued ($\lambda=\E|\nabla f|^2=0$ would force $f$
constant, contradicting normalization).

**Step 2 (the identity $\lambda\E f^4=3\E f^2|\nabla f|^2$ in $[0,\infty]$).** The
truncated cubic $\varphi_k$ was checked at the matching points: values and slopes agree at
$s=\pm k$, so $\varphi_k\in C^1$, odd, nondecreasing, $3k^2$-Lipschitz,
$\varphi_k(0)=0$, $\varphi_k'(s)=3(|s|\wedge k)^2$. Form-domain membership of
$\varphi_k(f)$: $\varphi_k/(3k^2)$ is a normal contraction ($1$-Lipschitz, vanishing at
$0$), and normal contractions operate on the domain of a Dirichlet form — the Friedrichs
form (closure of the $C_c^\infty$ energy) is a Dirichlet form; the chain rule
$\nabla\varphi_k(f)=\varphi_k'(f)\nabla f$ is classical for $C^1\circ C^\infty$ and
consistent with the form's carré du champ. Pairing the eigenequation with
$\varphi_k(f)$ through the form gives the truncated identity
$\lambda\E[f\varphi_k(f)]=3\E[(|f|\wedge k)^2|\nabla f|^2]$; this is the definitional
pairing $\langle-Lf,g\rangle=\E[\nabla f\cdot\nabla g]$ for $f\in D(L)$ and $g$ in the
form domain. Monotonicity in $k$ was verified on both sides: for $|s|>k$,
$\partial_k[k^3+3k^2(|s|-k)]=6k(|s|-k)>0$ and the value at $k=|s|$ is $|s|^3$, so
$s\varphi_k(s)\uparrow s^4$ pointwise; $(|f|\wedge k)^2|\nabla f|^2\uparrow
f^2|\nabla f|^2$ trivially. Two-sided monotone convergence therefore yields the identity
**as an identity in $[0,\infty]$**, with no integrability assumed at this stage. Step 1
then makes both sides finite. Correct.

**Step 3 (Poincaré for $f^2$).** $\mu$ is centered isotropic and log-concave
($\nabla^2V\succeq\varepsilon I\succ0$), so the frontier hypothesis applies to $\mu$
itself. $h=f^2$ is $C^1$, in $L^2(\mu)$ by Step 1, with
$\E|\nabla h|^2=4\E[f^2|\nabla f|^2]<\infty$ by Step 2. With $\E f^2=1$,
$\Var(f^2)=\E f^4-1$, so $\E f^4-1\le4K_n\E[f^2|\nabla f|^2]$. Correct; this is the
only place isotropy and centering are used.

**Step 4 (closure).** Substituting the Step-2 identity,
$\E f^4-1\le\tfrac{4K_n\lambda}3\E f^4\le\tfrac12\E f^4$ under
$\lambda\le3/(8K_n)$; the rearrangement subtracting $\tfrac12\E f^4$ is licensed
exactly by the Step-1 finiteness, giving $\E f^4\le2$. The constant chain
$\tfrac{4K_n}3\cdot\tfrac3{8K_n}=\tfrac12$ checks. The bound is universal in $n$,
$\varepsilon$, $\mu$, $\lambda$.

**Remarks are remarks.** The non-circularity observation ($K=1/\lambda$ yields
coefficient $p^2/(4(p-1))=1+(p-2)^2/(4(p-1))>1$ for all $p>2$; the algebra checks) and
the large-gap branch remark ($\lambda>3/(8K_n)\Rightarrow\CP=1/\lambda<8K_n/3$) derive
no statement and are correctly confined to remark environments; the branch split is
explicitly deferred to the consuming assembly dossier. The claimed downstream
non-circularity (input $O(\log n)$, output $O(\log^2n)$) concerns the pipeline, not this
lemma, and is not certified here.

### Hypothesis accounting

Used: (i) $V\in C^\infty$, $\nabla^2V\succeq\varepsilon I$, $\varepsilon>0$ — only for
elliptic regularity and the qualitative hypercontractive $L^4$ bound; (ii) centering and
isotropy of $\mu$ — only so the frontier hypothesis applies in Step 3; (iii) the
eigenequation through the Friedrichs form pairing, with $\E f=0$, $\E f^2=1$; (iv) the
Dirichlet-form normal-contraction and chain-rule property; (v) Hypothesis
`ass:sol-sfm-frontier`. No hypothesis is used silently; none of the stated hypotheses is
idle. No stochastic localization, no Letwin input (`thm:letwin-qcts` is explicitly not
used), and no numerical artifact appears anywhere.

### Dependency closure and citation debt

The node's only formal dependency is `thm:klartag-logn`, recorded in the ledger as
`status: imported`, `import_class: published`, reference `Klartag2023Logarithmic`
(B. Klartag, *Logarithmic bounds for isoperimetry and slices of convex sets*, Ars
Inveniendi Analytica 2023:4, DOI `10.15781/jsjy-0b06`) — a peer-reviewed journal
publication proving the Cheeger bound $h^*_n\ge c(\log n)^{-1/2}$, which Cheeger's
inequality converts to $\CP\le C\log n$; this matches the ledger and manuscript import
statement, and the dossier consumes exactly that statement, cited and not proved. The
remaining external inputs are classical published results used qualitatively:
Bakry–Émery (`BakryEmery1985`) and Gross hypercontractivity as presented in
Bakry–Gentil–Ledoux (`BakryGentilLedoux2014`, Ch. 5), both in `fi_references.bib` and
checked against this reviewer's knowledge of the sources. **No preprint-unreviewed input
occurs anywhere in this dossier.** With the published import discharging the hypothesis,
no unresolved premise remains: the node is eligible for `status: proved` at the
orchestrator's discretion.

### Fences

The ledger node carries no `bounded_by` edge; I checked the registered obstructions
independently and concur with the dossier's fence paragraph: the argument is static and
cut-free (`rem:two-tail-slice-bounds`, `rem:profile-circularity`, `rem:single-coordinate-cuts` untouched); no
projection or radial test is promoted to a tensor bound (`rem:projection-ceiling`); no
covariance occupation functional or crude integral appears (`rem:crude-insufficient`,
`rem:relative-ceiling` — the frontier constant is consumed as a calibrated external
input toward a strictly weaker downstream output, not as a relative occupation premise);
no localization occurs, so `prop:covariance-spike` is not engaged. Constraint 6 is
untouched.

### Standalone build

From `solutions/`: `latexmk -g -pdf -outdir=../build lem-mm-smallgap-fourth-moment.tex`
exits 0 and produces the PDF; the only warnings are the two expected standalone `??`
references (`subsec:spectral-sde`, `thm:letwin-qcts` — the latter appearing only in the
sentence disclaiming its use). Before this report, `python3 research/check_ledger.py`
reported 0 errors (202 nodes).

## Corrections

None required for correctness. One optional editorial refresh for a future pass: the
"ledger acceptance pending" header comments are stale now that both the node and the
import exist in the ledger.

## Exclusions

This review certifies only `lem:mm-smallgap-fourth-moment` in the immutable dossier scope
above. It does not certify the Klartag import itself (accepted repository provenance is
relied on for its published classification), the large-gap branch split, the downstream
window-occupation assembly (`prop-mm-window-occupation`) or its non-circularity claim,
any $L^p$ bound for $p\ne4$, any statement for non-smooth, non-isotropic, or degenerate
laws, existence or uniqueness of the first eigenfunction, or any localization statement.
Ledger wiring, header updates, and manuscript changes are outside this reviewer's write
surface.
