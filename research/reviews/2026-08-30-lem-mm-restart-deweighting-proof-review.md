---
verdict: pass
authors:
  - claude-prover-w4p02
reviewer: proof-checker-w4r02
fingerprints:
  solutions/lem-mm-restart-deweighting.md: e02adbf1cbecb1adf3e0c1867ee8d74dd4709ce27d45703b7e88e782ec84f7cc
  lem:mm-restart-deweighting: ec93efcb1ac959a52ffa4388970b9434e653605ff400c9a1093346afda979f20
  lem:mm-time-weighted-fixed-source: 661b4f05678efc9391f1738433880ef1c5188f8b10291ebbe2b7f9aa5cedeb46
---

# Restart deweighting at a stopping time — independent proof review

Cold review of `solutions/lem-mm-restart-deweighting.tex`, reviewed SHA-256
`8511c90a222f86aea8c4dbc9d48a1b955d2ff6245e2dfe7143692d7d3034c2d2`. The certified dependency
`solutions/lem-mm-time-weighted-fixed-source.tex` was re-read in the state with SHA-256
`7ed2f882b6b7ef62b93c0fedf5b19e85bc72e0b9269d816accfdbd0d38352f4c`. The proof was reconstructed
from the dossier, the manuscript module `modules/kls/30-spectral-route.tex`, the ledger
`research/kls/ledger.yaml`, the obstruction registry, and the certified dependency dossier and
its review. The prover's conversation was not available and the prover's narrative records were
used only to confirm authorship, never as mathematical evidence. Author
(`claude-prover-w4p02`) and reviewer (`proof-checker-w4r02`) are distinct.

## Findings

### Statement agreement

The dossier theorem, the ledger `statement:` for `lem:mm-restart-deweighting`, and the
manuscript statement at `\label{lem:mm-restart-deweighting}` (module lines 210–220) agree
mathematically: for an a.s. positive stopping time $\sigma$ on an $\varepsilon$-regular
approximant and a fixed $f\in L^2(\mu)$, a.s. on $\{\sigma<\infty\}$,

$$
\mathbb E\Bigl[\int_\sigma^\infty\|H_t\|_{\mathrm{HS}}^2\,dt\,\Big|\,\mathcal F_\sigma\Bigr]
\le\frac{\operatorname{Var}_{\mu_\sigma}(f)}{\varepsilon+\sigma}
\le\frac{v_\sigma}{\sigma},
$$

with the same tensor $H_t$, the same denominators, and the same restart mechanism named in all
three surfaces. Two deliberate refinements strengthen, and therefore cover, the manuscript
statement:

1. The dossier takes $\sigma$ in the *usual augmentation* $\mathcal F_t$ of the observation
   filtration, a strictly larger class than raw-filtration stopping times. For a raw stopping
   time, the augmented-filtration bound implies the raw-filtration bound by the tower property,
   because the right-hand side is a measurable function of $(\sigma,c_\sigma)$ and hence
   $\mathcal F^0_\sigma$-measurable. No agreement defect.
2. Isotropy and centering of the Route-S regular class are explicitly not used; the dossier
   proves the lemma for every smooth $\mu$ with $\nabla^2V\succeq\varepsilon I$, $\varepsilon>0$.
   This is a legitimate hypothesis sharpening, recorded in the dossier.

The theorem's added assertions (regular-conditional-distribution property of $\mu_\sigma$ and
$f\in L^2(\mu_\sigma)$ a.s.) are proved content, not imported.

### Step-by-step verification

**Step 1 (fixed-time Bayes and transfer to the augmentation) — verified.** The exponential
domination $|\phi(x)|e^{c_t\cdot x-t|x|^2/2}\le C_\phi(1+|x|^2)e^{(b_\phi+R)|x|}\in L^1(\mu)$ is
valid for strongly log-concave $\mu$ (all exponential moments), giving path continuity and
adaptedness of $N^\phi$. Cameron–Martin for constant drift gives likelihood
$\exp(x\cdot c_t-t|x|^2/2)$, and abstract Bayes gives
$N^\phi_t=\mathbb E[\phi(X)\mid\mathcal F^0_t]$ a.s. The transfer: for $u_k\downarrow t$,
$\bigcap_k\sigma(\mathcal F^0_{u_k}\cup\mathcal N)=\mathcal F_t$ (I checked both inclusions),
reverse martingale convergence applies to the decreasing family, and path continuity closes the
identity at $t$. The extension to $\phi\ge0$ integrable via $\phi\wedge k$ (conditional monotone
convergence on both sides, per fixed $t$) and to $L^1$ by linearity is correct; in particular
$a_t=\mathbb E[X\mid\mathcal F_t]$ a.s. per $t$ with $\mathbb E|a_t|\le\mathbb E|X|$.

**Step 2 (dyadic optional sampling, RCD, $L^2$ membership) — verified.** The dyadic
$\sigma_k=2^{-k}\lceil2^k\sigma\rceil$ are stopping times with $\sigma_k\downarrow\sigma$,
$\sigma_k\ge\sigma$. The elementary optional-sampling computation for the closed bounded
martingale $N^\phi$ at a countably valued stopping time is exact (including the $r=\infty$
piece, where $N^\phi_{\sigma_k}:=N^\phi_\infty$ is $\mathcal F_{\sigma_k}$-measurable).
$\bigcap_k\mathcal F_{\sigma_k}=\mathcal F_\sigma$ by right-continuity; reverse martingale
convergence on the left, path continuity on the right, tower property with
$\mathcal F_\sigma\subseteq\mathcal F_\infty$: identity `(sol-rdw-optional)` holds a.s. on
$\{\sigma<\infty\}$ per bounded $\phi$. Because $\mu_\sigma$ is already an
$\mathcal F_\sigma$-measurable probability kernel ($(\sigma,c_\sigma)$ measurable, kernel a
Borel function of $(t,z)$), the per-Borel-set identity is exactly the definition of a regular
conditional distribution — no simultaneous-null-set gap. Applying the $[0,\infty]$-valued
extension to $\phi=f^2$ and taking expectations gives $f\in L^2(\mu_\sigma)$ and finite
$v_\sigma$ a.s. on $\{\sigma<\infty\}$.

**Step 3 (strong log-concavity of $\mu_\sigma$) — verified.** Pathwise exact:
$V_\sigma=V-c_\sigma\cdot x+\tfrac\sigma2|x|^2$, $\nabla^2V_\sigma\succeq(\varepsilon+\sigma)I$,
smooth. Together with Step 2, $\mu_\sigma(\omega,\cdot)$ lies a.s. in the admissible class of
the certified lemma with $\kappa=\varepsilon+\sigma(\omega)>0$ and admissible test $f$.

**Step 4 (innovation BM and dyadic strong Markov) — verified.** The independence of
$B^{\mathrm{obs}}_t-B^{\mathrm{obs}}_s$ from $\mathcal G_{s+}$ (limit along $u\downarrow s$ with
bounded continuous tests) is correct. The passage to $\mathcal F_s$ uses
$\mathcal F_s=\sigma(\mathcal F^0_{s+}\cup\mathcal N)$; the dossier states this tersely
("independence is unaffected by adjoining null sets"), and I verified the underlying lemma
$\bigcap_{u>s}\sigma(\mathcal F^0_u\cup\mathcal N)=\sigma(\mathcal F^0_{s+}\cup\mathcal N)$ by
the standard $\limsup$-of-representatives argument — a terse but correct step. The conditional
Fubini for $\int_s^t a_r\,dr$ is justified by $\mathbb E|a_r|\le\mathbb E|X|$, and the drift
cancellation $\mathbb E[W_t-W_s\mid\mathcal F_s]=0$ is exact. Quadratic covariation: $W$
differs from $B^{\mathrm{obs}}$ by continuous finite-variation paths, and for continuous
martingales the bracket is the filtration-free limit in probability of partition sums, so
$[W^i,W^j]_t=\delta_{ij}t$; Lévy applies ($W_0=0$, true martingale). The strong Markov identity
`(sol-rdw-strong-markov)` is proved by the same dyadic scheme: per dyadic value $r$,
$A\cap\{\sigma_k=r\}\in\mathcal F_r$ and post-$r$ increments of the $(\mathcal F_t)$-BM are
independent of $\mathcal F_r$; countable summation, path continuity, dominated convergence, and
the cylinder $\pi$-system / functional monotone class upgrade are all valid; the extension to
nonnegative measurable $\Gamma$ in $[0,\infty]$ by monotone convergence is correct.

**Step 5 (restart algebra) — verified.** The exponent identity
$e^{\tilde c_u\cdot x-u|x|^2/2}e^{c_\sigma\cdot x-\sigma|x|^2/2}
=e^{c_{\sigma+u}\cdot x-(\sigma+u)|x|^2/2}$ makes
$\mu_{\sigma+u}=\Theta(\mu_\sigma;u,\tilde c_u)$ *pathwise exact* — no null set — and hence
$H_{\sigma+u}=\mathsf H(\Theta(\mu_\sigma;u,\tilde c_u))$,
$a_{\sigma+u}=\mathsf a(\mu_\sigma;u,\tilde c_u)$ pathwise, since $H_t,a_t$ are defined through
the kernel.

**Step 6 (deterministic solution map; the Yamada–Watanabe replacement) — verified, checked
closely as requested.**
(i) Joint continuity of $\mathsf a(\nu;u,z)$: dominated convergence with $|x|e^{R|x|}\in
L^1(\nu)$, denominator positive and continuous. (ii)
$\nabla_z\mathsf a(\nu;u,z)=\operatorname{Cov}(\Theta(\nu;u,z))$ is the standard tilted-family
identity, differentiation justified by exponential domination; the tilted potential has Hessian
$\succeq(\kappa+u)I$, and Brascamp–Lieb applied to linear functions gives
$\operatorname{Cov}\preceq(\kappa+u)^{-1}I\preceq\kappa^{-1}I$; since the Jacobian is symmetric
PSD with operator norm $\le\kappa^{-1}$, segment integration yields the global Lipschitz
constant $\kappa^{-1}$ in $z$, uniformly in $u$. (iii) The weighted metric
$d(\gamma,\gamma')=\sup_{u\le U}e^{-2u/\kappa}|\gamma_u-\gamma'_u|$ is complete (equivalent to
the sup norm), $\mathcal T$ maps $C([0,U])$ into itself by (i), and I recomputed the contraction
constant: $\kappa^{-1}\int_0^ue^{2s/\kappa}ds=\tfrac12(e^{2u/\kappa}-1)\le\tfrac12e^{2u/\kappa}$,
so $\mathcal T$ is a $\tfrac12$-contraction; Banach gives a unique continuous solution on every
$[0,U]$ and consistency gives the global $\mathsf S_\nu(w)$. Crucially, *any* continuous global
solution restricts to a fixed point of $\mathcal T$ on each $[0,U]$, so pathwise uniqueness
holds in the full class of continuous paths with no integrability side condition — this is what
legitimately replaces Yamada–Watanabe: the noise is additive, the equation is a deterministic
Volterra equation with globally Lipschitz drift, and the identification in Step 7(a)/(d) only
ever needs uniqueness for a path already known to be continuous and to solve the equation.
(iv) Measurability: Picard iterates are measurable by induction (jointly measurable integrand,
continuity in $s$, Riemann-sum approximation of the integral; evaluations generate
$\mathcal B(C_0)$), and pointwise locally uniform limits of measurable $C_0$-valued maps are
measurable; the convergence holds for each $\omega'$ with its own $\kappa(\omega')\ge\varepsilon$.
The joint measurability hypothesis in the application holds because
$\mathsf a(\mu_\sigma;u,z)$ is a ratio of $\mu$-integrals jointly continuous in
$(\sigma,c_\sigma,u,z)$ composed with the $\mathcal F_\sigma$-measurable $(\sigma,c_\sigma)$.

**Step 7 (freezing and the certified budget) — verified.**
(a) $c_t=\int_0^ta_s\,ds+W_t$ holds identically pathwise (definition of $W$; $a$ is defined and
continuous for every path since $c$ is continuous), and with Step 5's pathwise
$a_{\sigma+s}=\mathsf a(\mu_\sigma;s,\tilde c_s)$, the restarted path $\tilde c$ is a continuous
solution of the integral equation with forcing $W^{(\sigma)}$; Step 6(iii) uniqueness gives
$\tilde c=\mathsf S_{\mu_\sigma}(W^{(\sigma)})$ on $\{\sigma<\infty\}$.
(b) $G$ is $\mathcal F_\sigma\otimes\mathcal B(C_0)$-measurable (truncation of $f$, composition
with the Step 6(iv) map, Tonelli in $u$), and the pathwise identity
$\int_\sigma^\infty\|H_t\|^2dt=G(\cdot,W^{(\sigma)})$ follows from Step 5, (a), and the change
of variable $t=\sigma+u$ for a nonnegative integrand.
(c) Freezing: for rectangles $\mathbf 1_B(\omega)\Gamma(w)$ the identity is exactly
`(sol-rdw-strong-markov)` applied to $A\cap B$; the two finite measures
$D\mapsto\mathbb E[\mathbf 1_A\mathbf 1_D(\cdot,W^{(\sigma)})]$ and
$D\mapsto\mathbb E[\mathbf 1_A\int\mathbf 1_D(\cdot,w)\,\mathbb W(dw)]$ agree on the generating
$\pi$-system including the full space, hence everywhere; simple functions and monotone
convergence extend to all nonnegative product-measurable $G$ in $[0,\infty]$. With
$\gamma$ $\mathcal F_\sigma$-measurable this is the generalized conditional-expectation identity
`(sol-rdw-conditional-identity)`.
(d) Evaluation at a frozen prior: for a.e. fixed $\omega$, $\nu=\mu_\sigma(\omega)$ is smooth
$\kappa$-strongly log-concave with $f\in L^2(\nu)$, $\kappa=\varepsilon+\sigma(\omega)$. Steps 1
and 4 rerun on the auxiliary channel use only exponential moments and the finite first moment of
the prior — available for $\nu$ — so $W'\sim\mathbb W$ and $c'=\mathsf S_\nu(W')$ a.s. by the
same pathwise uniqueness; hence $\gamma(\omega)=\mathbb E\int_0^\infty\|H'_u\|^2du$. The
certified Lemma `lem:mm-time-weighted-fixed-source` is consumed *exactly as certified*: its
inequality for every $T>0$ with curvature $\kappa\ge0$, its explicitly certified nonnegativity
of the second integrand (which is dropped, legitimately), and the discard of
$-\kappa|g'_0|^2\le0$. Then $\kappa+u\ge\kappa$ and monotone convergence in $T$ give
$\gamma(\omega)\le\operatorname{Var}_\nu(f)/\kappa$. No internal step of the certified proof is
re-derived or altered.
(e) The chain $\operatorname{Var}_{\mu_\sigma}(f)/(\varepsilon+\sigma)\le v_\sigma/\sigma$ uses
only $\varepsilon>0$ and $\sigma>0$ a.s.; the annotation that positivity of $\sigma$ is needed
only for the second inequality is correct — nothing in (a)–(d) uses it.

**$H$ zero-convention.** For each fixed $t$, $f\in L^2(\mu_t)$ a.s. (Step 2 at the
deterministic time $t$) and $\mu_t$ has finite fourth moments, so by Cauchy–Schwarz the tensor
is absolutely convergent a.s. per $t$, hence off a $dt\otimes d\mathbb P$-null set by Tonelli;
the convention $\mathsf H=0$ elsewhere alters no time integral, on either the original or the
auxiliary channel (where $f\in L^2(\nu)$ plays the same role). I verified this directly; the
dossier's pointer to the companion stopped-window dossier's Step 1 is consistent with that
dossier's content but is not load-bearing here.

### Fences

The ledger node carries no `bounded_by` edge; the registered fences were checked individually
against the actual argument:

- `rem:two-tail-slice-bounds`, `rem:profile-circularity`, `rem:single-coordinate-cuts`: no cut, slice, or excess-profile
  estimate appears anywhere in the proof.
- `rem:projection-ceiling`: no radial or projection-only test is promoted to a tensor bound; the
  tensor is controlled through the certified time-weighted budget only.
- `rem:crude-insufficient`, `rem:relative-ceiling`: no covariance occupation integral
  ($\Xi$-type) occurs; $A_t$ enters only through the Brascamp–Lieb cap
  $\operatorname{Cov}(\Theta)\preceq(\kappa+u)^{-1}I$, a per-instance curvature bound.
- `prop:covariance-spike`: $\|A_t\|_{\mathrm{op}}$ is never bounded along a universal time
  interval; nothing conflicts with covariance spikes.
- The weight-removal no-go recorded in the certified dependency's own remark is respected: the
  weight is not removed at time zero; it is exchanged for the elapsed time $\sigma>0$, which is
  exactly the trade the fence permits. No unweighted initial-layer or universal-time occupation
  claim is made, and the dossier explicitly disclaims any claim about
  `conj:mm-spectral-occupation`.

### Hypothesis accounting

Used: smoothness and $\varepsilon$-strong log-concavity of $\mu$ with $\varepsilon>0$
(exponential moments, the $(\varepsilon+\sigma)$-strongly log-concave restart prior, the
$\varepsilon^{-1}$ drift Lipschitz bound); $f\in L^2(\mu)$; $\sigma$ a stopping time of the
usual augmentation; $\sigma>0$ a.s. (second inequality only); classical theorems
(Cameron–Martin, reverse martingale convergence, Lévy, Banach fixed point, monotone
class/Tonelli); Brascamp–Lieb; the certified dependency. Used but unstated: none found. Stated
but unused: centering and isotropy — already flagged in the dossier as unused (sharpening
recorded, not a defect); positivity of $\sigma$ is unused for the first inequality, which the
theorem itself already annotates.

### Dependency closure and standing

The unique dependency `lem:mm-time-weighted-fixed-source` is `status: proved`, agent-certified
by `research/reviews/2026-08-27-lem-mm-time-weighted-fixed-source-proof-review.md` (verdict
pass, distinct author/reviewer, scope covers the node and active dossier). Its statement is
consumed exactly as certified ($\kappa\ge0$ class contains $\kappa=\varepsilon+\sigma(\omega)$;
$f\in L^2(\nu)$; per-$T$ inequality; certified nonnegativity of the dropped term). No other
mathematical dependency exists. The dossier claims unconditional standing and that claim is
correct: no conditional or preprint-level premise occurs anywhere in the argument.

### Citation debt

The single external citation is `BrascampLieb1976` (J. Funct. Anal. 22 (1976) 366–389, DOI
10.1016/0022-1236(76)90004-5): **published**, classical, and used precisely for the covariance
bound $\operatorname{Cov}\preceq(\nabla^2V_\rho)^{-1}$-type control on strongly log-concave
measures that the paper's Theorem 4.1 supplies. All other tools are textbook classical results
requiring no source classification. No preprint-level import; no verification request needed.

### Header and build

`cd solutions && latexmk -pdf -outdir=../build lem-mm-restart-deweighting.tex` exits 0; the
unresolved cross-module `\ref`s standalone are expected. Header fields: ledger node and
`refines` resolve to the accepted node and manuscript label; `bounded_by: none` matches the
ledger; author named; `checked_by: none` with empty reviewer/review is the correct
pre-certification state. One stale annotation: the header and top comment still describe the
node as "candidate, ledger acceptance pending", while `lem:mm-restart-deweighting` now exists in
`research/kls/ledger.yaml` (status `open`). This is a provenance-comment staleness with no
mathematical content; the orchestrator's post-certification header wiring (checked_by, reviewer,
review) should refresh those lines at the same time.

## Corrections

None required for the mathematics. Mechanical only, for the orchestrator's wiring pass: update
the dossier header's `checked_by`/`reviewer`/`review` fields and the stale
"candidate node, ledger acceptance pending" annotations to reflect the accepted ledger node and
this review.

## Exclusions

Not certified here: `lem:mm-stopped-window-source`, `lem:mm-smallgap-fourth-moment`,
`prop:mm-window-occupation` (separate reviews); any unweighted initial-layer bound; any
universal-time occupation statement; `conj:mm-spectral-occupation`; any joint control of
$v_\sigma$ and $\sigma^{-1}$ (the assembly dossier's business, explicitly disclaimed by the
dossier); the manuscript prose surrounding the lemma. The companion dossiers' internal
conventions were consulted only where this dossier points at them and were independently
re-verified where load-bearing.
