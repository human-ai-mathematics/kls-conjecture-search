---
verdict: pass
authors:
  - /root/kls_proof_audit
reviewer: /root/kls_evidence_audit
fingerprints:
  solutions/thm-cmh-normalization.md: e46056f3b5044d2d4c8690907be9d6188b19d9093670e47c96c2691aa6fc28c5
  prop:cmh-bochner: 237164772a03afb3fb5bfb7a896dbd45f8487332637efa548b827454d8f8ea6c
  def:cmh: 5971e940e93fa8179ce6c80c9817d3b3a88ac7db2ffe56897f1957c02431f9e7
  thm:cmh-implies-affine-poincare: 434bde8b4ccac59502b5c71180a4f20df98e1abc02f85826578bba9321480559
  prop:cmh-hodge: e53f8f0d21ff4afad0be69fb034e09db1f7daaa882338a1d927af40c3117410e
  rem:cmh-stronger-than-kls: 42676f87e102fd9313af73973dcf29ff5a7f17ccec197c3284254e7cf2c0e0cc
  thm:cmh-1d: 20ca97481f8d3f33bab114618adc59596740cec2d34e37ad9c5c8ec1b9fa9904
  prop:letwin-not-gate-zero: d01d5a5df0ca378b977846fd59185615903c42ec4bf019d71ebb41b5bf8e7c3a
---

*Follows up* `research/explorations/2026-08-25-kls-cmh-normalization-audit.md`.

# Route C CMH normalization layer — independent repair audit

The original proof author was `/orchestrator/kls-cmh-normalization`; `/root/kls_proof_audit`
authored the certified repair. The audit also compared the dossier with
`modules/kls/40-moment-map-cmh.tex` and `modules/kls/41-cmh-normalization.tex`.

## Certified scope

This follow-up review certifies the repaired statements and proofs of exactly these seven nodes:

1. `q:cmh-normalization` — every operator datum in the regular-class CMH endpoint is fixed, and
   the endpoint reduction is proved on that class.
2. `def:cmh` — the Hilbert space, closed Stein generator, admissible class, covariance inverse,
   and kernel pseudoinverse conventions are well posed and affine-covariant.
3. `prop:cmh-bochner` — the integrated identity holds for the canonical moment-map Hessian on
   the operator core and its graph-norm closure.
4. `thm:cmh-implies-affine-poincare` —
   $\CPaff(\mu)\le\CMH(\mu)$ on the stated regular moment-map class, without assuming a spectral
   gap or boundedness of $H$.
5. `prop:cmh-hodge` — the weighted orthogonal splitting and the exact affine-Poincar\'e operator
   norm are correct.
6. `rem:cmh-stronger-than-kls` — only the proved nonnegative solenoidal channel and
   $\CMH\ge\CPaff$ are asserted; equivalence and strict nonimplication remain open.
7. `prop:letwin-not-gate-zero` — the explicit random-matrix law satisfies the universal
   constant-matrix inequality but violates gate zero for every integer $m\ge18$.

Each id occurs exactly once as a manuscript `\label`. The current manuscript statements, dossier
statements, and KLS ledger statements agree in hypotheses, constants, and conclusions. The
normalization dossier has no numerical premise and no applicable `bounded_by` obstruction.

## Independent mathematical re-derivation

### Stein generator, Bochner indices, and graph closure

The Stein identity gives

$$
 \partial_i(\rho H_{ij})=-\rho p_j,
 \qquad L_\mu g=H_{k\ell}g_{k\ell}-p_kg_k.
$$

Starting from the Dirichlet-form identity and differentiating $L_\mu g$ gives the four printed
terms. Integrating only the third-derivative term in $p_k$ gives

$$
 -\mathbb E[H_{ij}g_jH_{k\ell}g_{ik\ell}]
 =-\mathbb E[p_\ell H_{ij}g_jg_{i\ell}]
  +\mathbb E[H_{k\ell}(\partial_kH_{ij})g_jg_{i\ell}]
  +\mathbb E[H_{k\ell}H_{ij}g_{jk}g_{i\ell}].
$$

The first term cancels the differentiated-drift term after relabelling, and the last is
$\operatorname{Tr}(HD^2g\,HD^2g)$. For the two remaining terms, target/source differentiation
of the genuine moment-map Hessian gives

$$
 H_{mj}\partial_jH_{k\ell}
 =H_{mj}(H^{-1})_{rj}\varphi_{k\ell r}
 =\varphi_{mk\ell}.
$$

This tensor is totally symmetric. The residual is therefore exactly

$$
 \mathbb E[g_jg_{i\ell}\varphi_{\ell ij}]
 -\mathbb E[g_jg_{k\ell}\varphi_{jk\ell}]=0.
$$

Thus every sign and contracted index in the repaired proof is correct. In particular, the proof
now consumes the Codazzi/total-symmetry property explicitly and does not claim that the identity
holds for an arbitrary symmetric Stein kernel.

For graph-norm closure, applying the identity to $g_q-g_r$ controls both nonnegative fields
$H^{1/2}\nabla g_q$ and $H^{1/2}D^2g_qH^{1/2}$ in their respective $L^2$ spaces. Their limits are
independent of the core approximation, while $L_\mu g_q$ converges by graph-norm convergence.
This proves the stated closed identity on the operator-core closure; it does not enlarge the
claim beyond that closure.

### Endpoint pairing, unbounded $H$, and density

For the initial class $\mathscr C=\mathbb R+C_c^\infty$, bounded gradient and the exact Stein
normalization $\mathbb EH=\Sigma$ give

$$
 \mathbb E\langle H\nabla f,\nabla f\rangle
 \le \lVert\nabla f\rVert_\infty^2\operatorname{Tr}\Sigma<\infty.
$$

Hence the form--operator pairing is legitimate even when $H$ is unbounded. With
$\Pi_{\varepsilon,R}=\mathbf1_{[\varepsilon,R]}(\mathcal A)$ and
$g_{\varepsilon,R}=\Pi_{\varepsilon,R}\mathcal A^{-1}f$, the repaired proof uses

$$
 \lVert\Pi_{\varepsilon,R}f\rVert_2^2
 =\langle f,\mathcal A g_{\varepsilon,R}\rangle
 =\mathbb E\langle\nabla f,H\nabla g_{\varepsilon,R}\rangle,
$$

followed by Cauchy--Schwarz in the constant $\Sigma$ metric and the definition of $\CMH$. It does
not commute the $\mathcal A$ spectral projection with the unrelated $\Sigma$-form. This yields

$$
 \lVert\Pi_{\varepsilon,R}f\rVert_2^2
 \le \CMH(\mu)\,\mathbb E\langle\Sigma\nabla f,\nabla f\rangle.
$$

Strict positivity of $H$ and connectedness of the log-concave support identify
$\ker\mathcal A$ with the constants, so the spectral projections converge strongly to a
centered $f$ without a gap assumption. Finally, density of $\mathscr C$ in the declared
$H^1_\Sigma(\mu)$ norm passes variance and $\Sigma$-energy to arbitrary Sobolev functions. The
proof never asserts that finite $\Sigma$-energy implies finite $H$-energy. The observation that
the same endpoint argument works for a positive symmetric Stein kernel is correctly isolated
from the moment-map-only Bochner proposition.

### Hodge identity and the non-strict scope statement

With $u=H\nabla g$, $h=-\operatorname{Div}_\mu u$,
$-\operatorname{Div}_\mu(\Sigma\nabla\psi)=h$, and
$w=u-\Sigma\nabla\psi$, the repaired sign is

$$
 \operatorname{Div}_\mu w=-h-(-h)=0.
$$

Weighted integration by parts gives
$\mathbb E\langle\Sigma\nabla\psi,\Sigma^{-1}w\rangle=0$, so expanding the square proves the
printed Hodge identity. Writing
$\mathcal A_1=-\operatorname{Div}_\mu(\Sigma\nabla\,\cdot\,)$ identifies the affine term with
$\langle h,\mathcal A_1^{-1}h\rangle$; its operator norm on centered $L^2$ is exactly
$\CPaff(\mu)$.

In one dimension, $\operatorname{Div}_\mu w=0$ says $\rho w$ is constant, and the declared
no-flux convention forces that constant to vanish. In higher dimension compactly supported
weighted divergence-free fields show that the solenoidal space is nontrivial, but this alone
says nothing about a CMH extremizer and gives no separating measure. The repaired manuscript,
dossier, and ledger consequently assert $\CMH\ge\CPaff$ and an additional nonnegative channel,
while explicitly leaving equivalence and strict nonimplication open. No claim called “strictly
stronger” survives as a mathematical conclusion.

### Algebraic countermodel

For

$$
 H(z)=\begin{pmatrix}1&\sqrt d\,z^\top\\ \sqrt d\,z&cI_m+dzz^\top\end{pmatrix},
 \qquad d=\frac m{\sqrt{2m-1}},\qquad c=1-\frac dm,
$$

the Schur complement is $cI_m\succ0$, and spherical first and second moments give
$\mathbb EH=1\oplus(c+d/m)I_m=I_{m+1}$. Re-expanding $\mathbb E\operatorname{Tr}(BHBH)$ for
$B=\left(\begin{smallmatrix}a&r^\top\\r&D\end{smallmatrix}\right)$ reproduces the printed
formula. The $O(m)$ splitting has three noninteracting sectors, with comparison coefficients

$$
 2(1+d/m)\le4,
 \qquad
 1+\frac{m-2}{(2m-1)(m+2)}\le2,
$$

and scalar deficit

$$
 2(a^2+mt^2)-\mathbb E\operatorname{Tr}(BHBH)=(a-dt)^2\ge0.
$$

This proves the quantifier over every symmetric $B$. Meanwhile
$e_1^\top\mathbb EH^2e_1=1+d>4$ exactly for integer $m\ge18$. The repaired manuscript also has
the correct strict Schur-complement notation, block order, and description of the two-dimensional
scalar sector. The construction is explicitly only a matrix-law countermodel: it imposes no
Monge--Amp\`ere, Codazzi, or moment-map compatibility and therefore does not refute gate zero for
genuine moment maps.

## Approximation scope and cross-plane agreement

The general-measure paragraphs are conditional templates only. They assume regular approximants
$\mu_q$ with second-moment convergence, assume a uniform bound
$\sup_q\CMH(\mu_q)\le C$, and condition the final passage on limiting smooth-core density and
affine-support control. Under those hypotheses the displayed inequality for a fixed
$C_c^\infty$ test function passes to the limit; no continuity of $\CMH$ is asserted.

Accordingly, `q:cmh-approximation` remains `status: open` in the KLS ledger and is stated as a
separate question in `modules/kls/40-moment-map-cmh.tex`. The certified endpoint theorem is the
regular-class implication. Its route-level sentence that a universal CMH bound would prove KLS
is a conditional consequence, not a claim that the universal bound or approximation closure has
been established.

The corrected ledger note for `thm:cmh-implies-affine-poincare` also agrees with the manuscript
and dossier: the endpoint uses only a positive symmetric Stein kernel, but no converse and no
strict nonimplication from KLS is proved.

## Mechanical validation

- `solutions/thm-cmh-normalization.tex` compiles standalone to a 5-page PDF. Its unresolved
  cross-manuscript references are the standalone behavior expressly allowed by
  `solutions/README.md`; there is no TeX error.
- `main.tex` recompiles to a 149-page PDF after the final manuscript repairs, with no undefined
  references, undefined citations, or TeX errors.
- All seven certified manuscript labels occur exactly once.
- Immediately before this report was added, `python3 research/check_ledger.py` reported exactly
  seven errors: the missing certified solution link for `q:cmh-normalization` and the historical
  partial-review verdict for each of the other six nodes. It reported no warning and no unrelated
  structural error. This report supplies the replacement proof-review artifact; provenance
  rewiring in the shared ledger and dossier header remains with the orchestrator.

## Explicit exclusions

This audit does not certify `q:cmh-approximation`, universal $\mathrm{CMH}(4)$,
`conj:gate-zero`, `q:gate-zero`, the construction-layer Haar/commutator questions, any universal
KLS conclusion, the separate exact-case dossier, or any `finum` artifact. It certifies the
regular-class normalization implication, its stated structural consequences, and the exact
algebraic countermodel only. These exclusions do not qualify the verdict for any of the seven
nodes listed in the opening metadata.
