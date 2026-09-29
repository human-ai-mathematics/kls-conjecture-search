---
---
# KLS frontier audit: Letwin QCTS, route triage, and numerical retraction

Date: 2026-08-20

Targets: `def:qcts`, `q:upgrade`, `q:weighted`, `q:stein-weighted`, `q:taming`, `q:splitting`,
`q:alignment`, and the logical/numerical gates surrounding them.

Outcome: one important imported input, several elementary consequences, no proof of KLS, and a
set of necessary status corrections. The strongest new source is a recent version-1 preprint;
all consequences that improve the published frontier retain that caveat.

**Supersession note.** Sections 6--7 record the route decision at the time of this audit. The
tail-union computation, first-eigenfunction localization derivation, and $H^{-1}$ endpoint audit
were subsequently completed the same day. Their integrated verdict is in
[`2026-08-20-kls-program-cycle-1.md`](2026-08-20-kls-program-cycle-1.md); the historical
validation counts and artifact discussion below are intentionally left unchanged.

## 1. New primary input

Brayden Letwin, *The KLS Constant is $O(\log^{1/4}n)$*, arXiv:2607.24164v1, submitted
27 July 2026, proves (Theorem 1.2) that for isotropic log-concave $Y$ and symmetric $N$,

$$
\operatorname{Var}(Y^TNY)
\le 2\,\mathbb E|\nabla(Y^TNY)|^2
=8\lVert N\rVert_{\mathrm{HS}}^2.
$$

This is exactly the repository's quadratic-chaos thin-shell statement `def:qcts`, with constant
8. The proof uses the moment measure, a positive symmetric Stein kernel, and an $H^{-1}$
inequality. Source checked: [arXiv:2607.24164v1](https://arxiv.org/abs/2607.24164), submitted
27 July 2026; the downloaded 21-page v1 PDF had SHA-256
`5dd9194cf36d91e2e4929a48564fe99d8d163a0a5ec7b31d80dc1f58a41778f1`. It is not yet peer
reviewed.

Letwin's Theorem 1.1 gives the inverse-Cheeger scale $O(\log^{1/4}n)$, hence in this repository's
convention

$$
h_n^\star\gtrsim(\log n)^{-1/4},
\qquad
C_P\lesssim\sqrt{\log n}.
$$

The earlier published benchmark remains $h_n^\star\gtrsim(\log n)^{-1/2}$.

## 2. Checked elementary consequences

Let $\nu$ be centered log-concave with covariance $A$, let $E$ have mass $p$, put
$s=p(1-p)$, and let $K$ and $G$ be the translation-invariant and covariance two-color contrasts.
Whitening and Cauchy--Schwarz give

$$
s\lVert A^{-1/2}KA^{-1/2}\rVert_{\mathrm{HS}}^2\le8,
\qquad
s\lVert K\rVert_{\mathrm{HS}}^2\le8\lambda_{\max}(A)^2.
$$

On $p\in[1/3,2/3]$, the explicit centroid correction and $s|\delta|^2\le\lambda_{\max}(A)$ give

$$
S=s\lVert G\rVert_{\mathrm{HS}}^2\le17\lambda_{\max}(A)^2;
$$

at exact balance $K=G$ and the constant is 8. Thus the intrinsic static source is closed, but
unwhitening leaves exactly the dynamic covariance-alignment loss.

For the third-moment tensor

$$
M_\theta=\mathbb E[\langle X,\theta\rangle X\otimes X],
$$

the same inequality yields $\lVert M_\theta\rVert_{\mathrm{HS}}\le2\sqrt2$, hence
$\kappa_n\le2\sqrt2$. Klartag--Lehec Corollary 5.4 then gives, for every fixed $p\ge1$,

$$
\mathbb E\lVert A_t\rVert_{\mathrm{op}}^p\le C_p
\quad\text{for}\quad t\le c/\log n.
$$

This closes the formerly open fixed-time moment interval between $c/\log^2n$ and $c/\log n$,
conditional on Letwin v1. It does not silently strengthen the separate published sup-over-time
theorem, and it does not reach a universal time. The two-sided-exponential product indicates that
$1/\log n$ is the natural endpoint of covariance-only control.

## 3. What this does and does not discharge

Discharged, conditional on the preprint:

- intrinsic QCTS (`thm:letwin-qcts`);
- the whitened two-color source estimate (`cor:qcts-source`);
- universal boundedness of $\kappa_n$ (`prop:letwin-kappa`);
- the fixed-time covariance-moment window $c/\log n$ (`cor:letwin-window`);
- the corresponding dimension-dependent `(V2)` window.

Still open:

- `q:upgrade`: universal-time, cut-aware operator-to-trace occupation;
- `q:alignment`: whether a fixed high-complexity product cut can align many coordinate budgets
  with random inflation excursions;
- `q:weighted`: joint weighted excess/covariance occupation;
- `q:stein-weighted`: the dynamic boundary trace, not its intrinsic quadratic input;
- `q:taming`: a cut-free, near-worst-specific universal-time improvement;
- `q:splitting`: even the zero-curvature rigidity direction, before quantitative stability.

No headline open node and no conditional KLS implication is proved by QCTS alone.

## 4. Proof-status corrections found during the audit

### Relative-scale ceiling

The old `prop:ceiling` inferred $\Xi_T\le\kappa T$ for $T<T_0$ from the one-time hypothesis
$\Xi_{T_0}\le\kappa T_0$; that inference is invalid. The repaired statement runs at $T_0$
itself and assumes

$$
9(1+\kappa)T_0\le\tfrac12.
$$

This proves that the all-measure relative input is KLS-sufficient. It does not prove a converse
equivalence.

The open target `q:taming` is deliberately weaker and different: it asks, only for near-worst
measures, for

$$
h_\mu\bigl(T_0^{4/3}+\Xi_{T_0}(\mu)\bigr)\le\kappa T_0.
$$

This supplies absolute-scale excess through the bootstrap. It should not be described as the
unweighted all-measure hypothesis of `prop:ceiling`, nor as relative-scale propagation.

### Weighted-package quantifiers

The consumption proof formerly chose the tight-window parameter after the package supplied an
unspecified fixed window. Restricting a Stein inequality to a smaller stopping time is not
automatic because its right-hand integrals also shrink. The package now includes one fixed
$\eta$ with the explicit absorption condition

$$
2\beta+64\eta^2<1.
$$

### Moving-family circularity

The infimum of a fixed family of perimeter martingales is a supermartingale. The family

$$
\{S:\mu_t(S)\in[1/2-\eta,1/2+\eta]\}
$$

is random and time-dependent, so the fixed-family lemma does not show that the localized profile
is a supermartingale. The exact excess identity remains valid. “Direct propagation is circular”
has been downgraded from a machine no-go to a methodological warning.

### Jacobi/Reilly foundation

`prop:exact-splitting` proves two one-way statements: global cylinder plus global Hessian flatness
implies a log-affine product; an already split log-affine factor has a flat orthogonal halfspace.
It does not prove $\mathfrak K_\Sigma=0\Rightarrow$ global splitting. Boundary-local flatness alone
cannot determine a global potential (for example $V(z)=z^4$ is flat to second order at zero but
is not log-affine).

More fundamentally, the fixed cut followed under localization is not automatically a smooth
critical local minimizer. Nonnegative second variation is not quantitative coercivity (Gaussian
halfspaces have tangential linear Jacobi zero modes), and Reilly leaves mixed boundary terms for
the global Poisson solution. The geometric route first needs a localization-uniform
almost-stability trace theorem modulo this kernel; `rem:almost-stability-gap` records it.

### Weight versus time rate

The two-tail example calibrates the covariance power $5/2$, not the time exponent. If the
Brascamp--Lieb cap $\lVert A_t\rVert\sim t^{-1}$ were saturated deterministically, the formerly
suggested $\mathbb E e_t\lesssim t^{3/2}$ would leave a nonintegrable $t^{-1}$ factor. A
pointwise $t^{5/2+\gamma}$ rate would be sufficient; a realistic proof likely needs a joint
rare-event estimate instead.

## 5. Retraction of the 2026-06-21 localization interpretation

The append-only artifact `research/runs/2026-06-21-kls-loc.jsonl` called a flat/decreasing
$\Xi_S/n$ sweep “supports taming.” That interpretation is withdrawn:

- raw $\Xi_S\asymp n$ would make $\Xi_S/n$ flat while violating a dimension-free source bound;
- the computed $\Xi_S$ is cut-specific, whereas `q:taming` concerns the cut-free
  $\Xi_T=\int\mathbb E(\lambda_{\max}(A_t)-1)_+dt$ for near-worst measures;
- the target did not compute the masked `q:alignment` source, $r$, $D$, weighted excess, or a
  Stein trace;
- default runs skipped the FFT/MC gate, calibration was omitted from eligibility, and there was
  no $dt$ refinement or along-path tilted-state convergence;
- the artifact records a dirty worktree at a commit that does not contain the KLS target code,
  so its provenance is not reconstructible.

The historical artifact is preserved. The target and gating documentation now emit diagnostics
and `no-verdict` in all cases until the route observables and dynamic gates exist.

The older `research/runs/2026-06-20-kls.jsonl` artifact has the same unreconstructible
provenance (dirty worktree at `c960281`, before the `experiments/` tree existed) and only probes
static Poincare geometries, not the cut-specific dynamic rank-one theorem. Its former
`evidence_run` link from `cor:refutation` has therefore been removed. In fact every artifact
currently stored under `research/runs/` records `git_dirty: true`; none should promote a proof
node until regenerated from a clean, code-containing commit with complete parameters and gates.

## 6. Highest-value next computation

Replace the radial energy shell by the balanced tail-union cut

$$
E_n=\{\max_i|x_i|\ge a_n\},\qquad\mu(E_n)=1/2.
$$

It is permutation-symmetric, depends on all coordinates, is coordinate-selective rather than
radial, and has a product complement of truncated one-dimensional factors. A refutation-seeking
experiment should use true tilted-Laplace conditional moments and report, on interval sweeps past
$c/\log n$,

$$
\int S_t^Hdt,
\qquad \int r_tdt,
\qquad \int D_tdt,
$$

where $S_t^H$ counts every matrix entry of $G_t$ incident to a coordinate with
$A_t^{(i)}\ge2$ (so high--low entries receive their full multiplicity),

together with balance survival, path/seed uncertainty, $dt$ refinement, and quadrature checks at
representative tilted states. It remains model evidence, never proof.

## 7. Alternative-route ranking

1. **Moment-map / Stein / spectral.** Best distinct hybrid. Extend Letwin's $H^{-1}$ control from
   quadratic data to the first nonzero eigenfunction; the prose-only route brief is
   `research/kls/routes/moment-map-spectral/README.md`.
2. **Direct spectral/Bochner.** Closely related. A sufficient headline is to improve the current
   comparison to $C_P\le C(1+\kappa_n^2)$; Letwin's universal $\kappa_n$ would then close KLS.
3. **Brownian/Follmer transport.** A bounded expected squared Jacobian is sufficient, but current
   derivative estimates reuse known KLS information; universal almost-sure Lipschitz transport is
   impossible for exponential tails.
4. **Jacobi/Reilly/splitting.** Speculative until the almost-stability trace bridge exists.
5. **Classical needles.** No current mechanism preserves all isotropic covariance constraints in
   a one-dimensional reduction; this is a diagnosis, not a no-go theorem.

## 8. Validation

Final checks after the audit edits:

- `python3 research/check_ledger.py`: 2 ledgers, 113 nodes, 0 errors; one pre-existing
  unrelated `conj:a1-bis` label warning;
- `python3 -m unittest discover -s research/tests -p 'test_*.py'`: 12 passed;
- `experiments/.venv/bin/python -m pytest -p no:cacheprovider experiments/tests`: 35 passed;
- `experiments/.venv/bin/python -m finum selftest` (from `experiments/`): PASS, 0 failures;
- `latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/kls-explore-build main.tex`:
  successful 88-page build with no unresolved references;
- `git diff --check`: clean.
