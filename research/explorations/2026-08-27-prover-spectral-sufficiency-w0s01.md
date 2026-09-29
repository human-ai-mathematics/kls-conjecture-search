---
---
# Prover: full-damping spectral sufficiency

Date: 2026-08-27

Role: `prover`

Concurrency key: `solution:prop-spectral-sufficiency`

Run id: `w0s01`

Author: `/root/prove_spectral_sufficiency`

Status: candidate dossier with `checked_by: none`; no proof certification or ledger delta is
applicable before an independent review.

## Node and dependency audit

The accepted ledger node is `prop:spectral-sufficiency`, anchored at
`prop:spectral-sufficiency` in `modules/kls/30-spectral-route.tex`. Its sole `depends_on` edge is
the open node `q:mm-spectral-occupation`. It has no `bounded_by` edge.

The refined premise is the full-damping estimate: for universal $T_0,C_0,C_1>0$, every normalized
first eigenfunction on every regular centered isotropic log-concave approximant satisfies
$$
\mathbb E\int_0^t\|H_s\|_{\mathrm{HS}}^2\,ds
\le C_0t+C_1\int_0^t\mathbb E|g_s|^2\,ds
+\mathbb E\int_0^t2g_s^TA_sg_s\,ds,
\qquad 0\le t\le T_0.
$$
The coefficient of the exact damping is exactly one. The dossier proves that this premise
implies the dimension-free bound
$$
C_P(\mu)\le \frac2{T_*},
\qquad
T_*=\min\left\{T_0,
\frac1{2(1+C_0T_0)e^{C_1T_0}}\right\}
$$
for every isotropic log-concave law. The conclusion remains conditional because the occupation
premise is open.

## Analytic mechanism

The planted Gaussian observation model gives the fixed-test filtering identity
$$
d\mathbb E_t\phi=\operatorname{Cov}_t(\phi,X)\cdot dW_t.
$$
Writing $m_t=\mathbb E_tf$, $b_t=\mathbb E_tX$,
$g_t=\mathbb E_t[(f-m_t)(X-b_t)]$, and
$H_t=\mathbb E_t[(f-m_t)(X-b_t)^{\otimes2}]$, an explicit Itô product calculation yields
$$
dg_t=H_t\,dW_t-A_tg_t\,dt.
$$
Consequently, for $q(t)=\mathbb E|g_t|^2$,
$$
q(t)=|g_0|^2+
\mathbb E\int_0^t(\|H_s\|_{\mathrm{HS}}^2-2g_s^TA_sg_s)\,ds.
$$
Isotropy makes the coordinate functions orthonormal in $L^2(\mu)$, so Bessel gives
$|g_0|^2\le1$. The full damping in the open hypothesis cancels the full damping in this identity,
leaving
$$
q(t)\le1+C_0t+C_1\int_0^tq(s)\,ds.
$$
Thus $q(t)\le(1+C_0t)e^{C_1t}\le M_*$. At the stated $T_*$, the averaged posterior variance is
$$
\mathbb E\operatorname{Var}_{\mu_{T_*}}(f)
=1-\int_0^{T_*}q(s)\,ds\ge\frac12.
$$
Posterior Brascamp--Lieb and the fixed-gradient tower property give
$$
\mathbb E\operatorname{Var}_{\mu_{T_*}}(f)
\le T_*^{-1}\mathbb E_\mu|\nabla f|^2
=\lambda/T_*.
$$
Hence the first positive eigenvalue satisfies $\lambda\ge T_*/2$.

## Regularization and the avoided dead end

Passing eigenfunctions themselves would require spectral/Mosco convergence and can fail as a
proof strategy when the limiting spectral bottom is not attained. The dossier does not use
eigenfunction convergence. It constructs smooth strongly convex isotropic approximants, proves
the same uniform Poincaré inequality separately on each one, and passes that inequality on each
fixed $C_c^\infty$ test function.

Gaussian convolution alone was not sufficient for the stated regular class: it is smooth and
log-concave but need not be strongly log-concave. The repaired construction is
$$
d\widetilde\nu_{\varepsilon,\delta}(x)
\propto e^{-\delta|x|^2/2}\,d(\nu*\gamma_\varepsilon)(x),
$$
followed by recentering and whitening. For fixed $\varepsilon$, sending $\delta\downarrow0$
gives $W_2$ convergence to the Gaussian convolution; a diagonal choice then converges in $W_2$
to the original isotropic law. Gaussian differentiation gives both lower and upper Hessian
bounds for the tilted potential. Its ground-state Schrödinger potential tends to infinity, so
the approximant generator has compact resolvent and a genuine first eigenfunction. Recentring
and whitening preserve these properties.

For a fixed $h\in C_c^\infty$, weak convergence passes its variance and gradient energy. Standard
value truncation, spatial cutoff, and mollification extend the result to every locally Lipschitz
test. No limiting eigenfunction occurs anywhere.

## Hypotheses actually used and unclosed steps

The proof uses:

- the universal, regularization-independent full-damping occupation hypothesis, explicitly
  stated in the theorem;
- smooth strong log-concavity and compact resolvent only at the approximant level, to have the
  normalized first eigenfunction and justify the fixed-function stochastic calculus;
- centered isotropy for the initial Bessel bound and for the KLS normalization;
- classical filtering, Itô isometry, Grönwall, Brascamp--Lieb, and standard Sobolev density;
- log-concavity and finite second moment in constructing and isotropizing the regular sequence.

There are no hypotheses used but omitted from the theorem and no unclosed analytic step in the
conditional implication. The sole unresolved mathematical premise is
`q:mm-spectral-occupation`. No numerical evidence is used.

## Fence-by-fence check

There is no formal `bounded_by` edge. All live obstruction shapes were nevertheless checked:

- `obs:two-tail`: no cut, slice, excess, or absolute fixed-cut source estimate occurs;
- `obs:proj-ceiling`: no tensor bound is inferred from radial or projection-only tests;
- `obs:crude-insufficient`: no crude covariance integral is used;
- `obs:relative-ceiling`: no relative covariance occupation conclusion is claimed;
- `obs:circularity`: no localized isoperimetric profile or changing competitor family appears;
- `obs:rank-one-refuted`: no product-cut witness or conclusion appears;
- the covariance-spike fence is respected because no pathwise operator-norm control of $A_t$ is
  used; posterior curvature is invoked only at the terminal time;
- no truncated-exponential Stein shortcut, trace-upgrade implication, or CMH claim is made.

## Build and certification state

The deferred artifact candidate is `solutions/prop-spectral-sufficiency.tex`. Its header remains
`checked_by: none`, with reviewer and review fields empty. Therefore there is **no applicable
ledger delta**. Only a distinct cold proof-checker may certify it; after a passing persisted
review, the orchestrator could atomically consider the future
`solution: solutions/prop-spectral-sufficiency.tex` metadata while keeping the node conditional
on `q:mm-spectral-occupation`.

## Build and validation

The first standalone compile exposed a typesetting-only dead end: four TeX commands in the
regularization paragraph had acquired control-character escapes during file creation. The
compiler stopped at the first malformed command. Replacing those four malformed commands with
the intended fraction, convergence-arrow, epsilon, and delimiter commands fixed the build; no
mathematical step or hypothesis changed.

The required command

    cd solutions && latexmk -pdf -outdir=../build prop-spectral-sufficiency.tex

now exits with status 0 and produces "build/prop-spectral-sufficiency.pdf" (four pages). The final
log contains no TeX error, overfull box, underfull box, or package warning. Its only LaTeX
warnings are the five expected unresolved cross-module references in the standalone build:
"q:mm-spectral-occupation", "prop:spectral-sufficiency", "subsec:spectral-sde", and "conj:kls"
(with the occupation reference occurring twice).

"git diff --check" is clean for the two owned artifacts. The read-only structural check
"python3 research/check_ledger.py" reports 180 nodes, 648 labels, and 0 errors. No ledger,
manuscript, route-control, bibliography, review, or other solution file was edited by this
prover.

~~~yaml
outcome: complete
artifacts:
  - solutions/prop-spectral-sufficiency.tex
  - research/explorations/2026-08-27-prover-spectral-sufficiency-w0s01.md
proposed_deltas:
  - none
next_role: proof-checker
next_prompt: |
  Cold-review solutions/prop-spectral-sufficiency.tex for the sole ledger node
  prop:spectral-sufficiency, independently of author
  /root/prove_spectral_sufficiency. The dossier must prove exactly this conditional
  implication: if universal T0,C0,C1>0 give, for every normalized first eigenfunction on
  every smooth strongly log-concave centered isotropic regular approximant and every
  0<=t<=T0,

    E int_0^t ||H_s||_HS^2 ds
    <= C0 t + C1 int_0^t E|g_s|^2 ds
       + E int_0^t 2 g_s^T A_s g_s ds,

  with the coefficient of the exact damping equal to one and constants uniform through
  approximation, then every isotropic log-concave law satisfies

    C_P <= 2/T_*,
    M_*=(1+C0 T0) exp(C1 T0),
    T_*=min{T0,1/(2M_*)}.

  Reconstruct every step from repository artifacts. In the regular case, verify the planted
  observation posterior, innovation Brownian motion, fixed-integrand filtering formula, and the
  product calculation dg_t=H_t dW_t-A_t g_t dt, including stopping and integrability.
  Verify Bessel's bound |g_0|^2<=1, the exact Ito identity for
  q(t)=E|g_t|^2, cancellation of the full damping with no strict surplus, and the stated
  Gronwall constant. Check the total-variance identity
  E Var_t(f)=1-int_0^t q(s)ds, the choice of T_*, posterior Brascamp--Lieb
  E Var_t(f)<=lambda/t, the fixed-gradient tower property, and hence
  lambda>=T_*/2.

  Audit the arbitrary-measure passage especially closely. Confirm that Gaussian convolution
  followed by a vanishing Gaussian tilt, recentering, and whitening gives W_2-convergent
  smooth strongly convex isotropic approximants; verify the conditional-covariance formula for
  the Hessian of the convolved potential and the compact-resolvent argument after the
  ground-state transform. Check that the uniform Poincare inequalities pass on fixed
  C_c-infinity tests and extend to every locally Lipschitz test by value truncation, spatial
  cutoff, and mollification. No convergence of first eigenfunctions may be assumed.

  The sole dependency is the explicitly assumed open node q:mm-spectral-occupation; a passing
  result therefore remains conditional and does not make KLS proved. The ledger node has no
  formal bounded_by edge. Check nonetheless that the dossier uses no cut/slice/excess or
  localized-profile estimate, projection-only tensor conclusion, crude or relative covariance
  occupation bound, product-cut assertion, pathwise universal-time operator-norm control,
  truncated-exponential Stein shortcut, trace-upgrade implication, Letwin preprint input, or
  CMH claim. There is no numerical evidence.

  Re-run cd solutions && latexmk -pdf -outdir=../build
  prop-spectral-sufficiency.tex; the author reports a successful four-page build with no TeX
  errors or box/package warnings and only the expected unresolved manuscript references.
  Persist a structured proof-review under research/reviews/ with a reviewer identity distinct
  from the author. Certify only if the full-damping endpoint, stochastic stopping, explicit
  constants, regular spectral class, and weak-limit passage are complete; otherwise return a
  verbatim next_prompt naming every required repair.
~~~
