---
---
# Prover attempt: CMH approximation closure

Date: 2026-08-27

Role: `prover`

Concurrency key: `solution:q-cmh-approximation`

Target: `prop:cmh-approximation-closure`

Author: `/root/prove_cmh_approximation`

## Outcome of the attempt

The candidate dossier is
`solutions/q-cmh-approximation.tex`. It constructs regular compact-target approximants for every
centered log-concave law and proves the constant-preserving closure implication under the route's
intended premise
$\sup_k C_{\mathrm{CMH}}(\mu_k)\le C$.

The construction is unconditional. The conclusion is conditional on the uniform CMH premise;
the dossier does not prove that premise, universal $\mathrm{CMH}(4)$, or KLS.

## Dependency and fence check

The complete dependency closure read for this attempt is:

- `def:cmh`, defined in `modules/kls/41-cmh-normalization.tex` and certified by
  `solutions/thm-cmh-normalization.tex` plus
  `research/reviews/2026-08-25-kls-cmh-normalization-repair-audit.md`;
- `thm:cmh-implies-affine-poincare`, certified by the same dossier and review;
- `thm:regular-moment-map-compact-target`, the published import in
  `modules/kls/04-family-moment-map.tex`, backed by `BermanBerndtsson2013RealMA` and
  `Fathi2019SteinMomentMaps`.

The target has no `bounded_by` edge. The argument also avoids every fixed-cut obstruction
mechanism listed in `research/kls/obstructions.md`: it uses no tail split, projection ceiling,
localization occupation estimate, relative trace upgrade, evolving isoperimetric competitor, or
rank-one cut estimate. It does not touch the trace-upgrade cluster.

## The theorem stated in the dossier

For an arbitrary centered log-concave probability $\mu$ on $\mathbb R^n$, with
$\Sigma=\operatorname{Cov}(\mu)$ and $S=\operatorname{Ran}\Sigma$, the dossier explicitly
constructs centered, full-dimensional, compactly supported regular moment-map laws $\mu_k$ with
$W_2(\mu_k,\mu)\to0$ in the original coordinates and proves

$$
C_P^{\mathrm{aff}}(\mu)
\le \liminf_k C_P^{\mathrm{aff}}(\mu_k)
\le \liminf_k C_{\mathrm{CMH}}(\mu_k).
$$

Here the limiting space $H^1_\Sigma(\mu)$ is explicitly the intrinsic closed relaxation of the
constant covariance form on $S$. No equality with an unnamed maximal Neumann or distributional
Sobolev domain is asserted. Consequently, the hypothesis
$\sup_k C_{\mathrm{CMH}}(\mu_k)\le C$ implies
$C_P^{\mathrm{aff}}(\mu)\le C$ with no loss, including when $S$ is proper or zero-dimensional.

## Construction and regularity match

Let $q_\delta$ be the density of $\mu*N(0,\delta I_n)$. For
$\delta,\varepsilon>0$ and $R<\infty$, the uncentered target has density proportional to

$$
\mathbf 1_{B(0,R)}(x)q_\delta(x)e^{-\varepsilon|x|^2/2}.
$$

It is then translated by its mean. The dossier takes $\delta_k=k^{-4}$ and chooses
$0<\varepsilon_k<k^{-1}$ and $R_k>k$ so that the truncated/tilted law is within $k^{-1}$ in
$W_2$ of the Gaussian convolution. Its centered version satisfies the explicit bound

$$
W_2(\mu_k,\mu)<\frac2k+\frac{\sqrt n}{k^2}.
$$

Each target has a translated-ball support, a positive ambient-$C^\infty$ density, and a smooth
interior potential whose Hessian is at least $\varepsilon_k I_n$. Thus it is centered,
full-dimensional, log-concave, and interior strictly convex. Berman--Berndtsson Theorem 1.1 gives
the smooth strictly convex canonical potential and global gradient diffeomorphism; Fathi Theorem
2.3 gives the positive canonical Stein kernel, Stein identity, and weak zero flux. A cutoff equal
to a coordinate function on the compact support gives
$\mathbb E_{\mu_k}H_k=\Sigma_k$.

## Closed-form convention

On the restrictions of $\mathbb R+C_c^\infty(\mathbb R^n)$ to the compact target, the dossier
defines

$$
\mathcal E_{H_k}(f,f)=\int\langle H_k\nabla f,\nabla f\rangle\,d\mu_k.
$$

Finite core energy follows from $\mathbb EH_k=\Sigma_k$. Closability is proved locally: on each
compact subset of the support interior, the density and the positive smooth matrix $H_k$ are
uniformly nondegenerate, so closedness of distributional differentiation kills the gradient
limit of any null $L^2$ sequence. Exhaustion handles the boundary, which has zero measure. The
same argument identifies the closed-form kernel with the constants. This is the Friedrichs
ambient-core convention used by `def:cmh`; no maximal-domain identification is made.

The certified regular endpoint then gives
$C_P^{\mathrm{aff}}(\mu_k)\le C_{\mathrm{CMH}}(\mu_k)$.

## Constant-preserving closure and affine degeneration

Ambient $W_2$ convergence gives $\Sigma_k\to\Sigma$. On the single common core
$\mathbb R+C_c^\infty(\mathbb R^n)$, bounded continuity gives convergence of variances, and

$$
\begin{aligned}
&\left|\int\langle\Sigma_k\nabla F,\nabla F\rangle d\mu_k
-\int\langle\Sigma\nabla F,\nabla F\rangle d\mu\right|\\
&\quad\le
\|\Sigma_k-\Sigma\|_{\mathrm{op}}\|\nabla F\|_\infty^2
+\left|\int\langle\Sigma\nabla F,\nabla F\rangle d\mu_k
-\int\langle\Sigma\nabla F,\nabla F\rangle d\mu\right|\to0.
\end{aligned}
$$

Passing along a liminf subsequence proves the common-core inequality with the same constant.
The dossier then proves density of $\mathbb R+C_c^\infty(S)$ in the intrinsic closed covariance
form by value truncation, spatial cutoff, and mollification inside $S$.

Ambient restrictions and intrinsic functions agree: every intrinsic smooth compactly supported
function has an ambient extension constant in the normal variable near $S$, and
$\Sigma P_{S^\perp}=\Sigma^+P_{S^\perp}=0$. Thus both the covariance energy and the
Moore--Penrose metric ignore normal derivatives. If $\dim S=0$, then $\mu=\delta_0$, all
variances vanish, and the affine Poincare constant is zero.

Covariance eigenvalues are tracked with Weyl's inequality. Each $\Sigma_k$ may be whitened, and
affine covariance permits the regular inequality to be pulled back. When covariance collapses,
the whitening maps diverge in normal directions, so the proof unwhitens each inequality before
taking the limit in the original coordinates. It never transports the canonical kernel through
a noninvertible map.

## Dead end avoided and unresolved limitations

The upstream probe's untruncated Gaussian-convolution/Gaussian-tilt family was not used. The
published theorem available in the repository covers bounded convex targets, not the required
full-support canonical-potential regularity. Adding the growing-ball truncation is the
source-verified repair and still gives ambient $W_2$ convergence.

There are no deliberately unclosed proof steps in the candidate dossier under its stated
closed-relaxation convention. The unresolved mathematical premise is exactly the assigned route
premise $\sup_k C_{\mathrm{CMH}}(\mu_k)\le C$; it is stated as a hypothesis, not treated as a
gap or as evidence for plausibility. If the project later changes $H^1_\Sigma(\mu)$ to a
separately defined maximal domain, equality with this closed relaxation would be a new theorem
outside the present dossier.

No numerical result is used anywhere in the proof.

## Validation

- Prescribed standalone build:
  `cd solutions && latexmk -pdf -outdir=../build q-cmh-approximation.tex` — exit code 0.
- Output: `build/q-cmh-approximation.pdf`, 6 pages.
- The build log has no TeX error, undefined control sequence, overfull box, or underfull box.
  Cross-manuscript references remain undefined in standalone mode, as permitted by
  `solutions/README.md`; both bibliography entries resolve through Biber.
- `git diff --check -- solutions/q-cmh-approximation.tex` — exit code 0.

## Certification and ledger status

The dossier header is `checked_by: none`. There is no applicable ledger delta from this prover
round. The future path
`solution: solutions/q-cmh-approximation.tex` is only a deferred artifact candidate and must not
be added unless a distinct proof checker passes the dossier and the orchestrator applies the
solution, review, `checked_by`, and conditional status atomically.

```yaml
outcome: complete
artifacts:
  - solutions/q-cmh-approximation.tex
  - research/explorations/2026-08-27-prover-cmh-approximation-harness-01.md
proposed_deltas:
  - none; solutions/q-cmh-approximation.tex is only a deferred solution candidate pending independent review
next_role: proof-checker
next_prompt: |
  Cold-review `solutions/q-cmh-approximation.tex` as a candidate dossier for
  `prop:cmh-approximation-closure`. Reconstruct it from repository artifacts rather than from the author's
  account. The theorem constructs, for every centered log-concave `mu` on `R^n`, centered
  full-dimensional compact-target regular moment-map approximants `mu_k` by Gaussian
  convolution, Gaussian tilt, growing-ball truncation, and centering, with an explicit ambient
  `W_2` diagonal bound. Under the sole unresolved hypothesis
  `sup_k C_CMH(mu_k) <= C`, it proves `C_P^aff(mu) <= C` with no loss, including proper affine
  support and `dim Ran(Sigma)=0`. Audit every construction and `W_2` step; match all hypotheses
  of imported `thm:regular-moment-map-compact-target`; check the weak zero-flux and mean-kernel
  deductions; independently verify closability and the constant kernel on the exact ambient
  restriction core; verify use of certified `thm:cmh-implies-affine-poincare`; reconstruct the
  common-core variance/energy limits and the liminf inequality; and check the intrinsic closed
  covariance-form relaxation, density of `R+C_c^infty(S)`, ambient extension independence,
  Moore--Penrose normal annihilation, eigenvalue collapse, and whitening/unwhitening order.
  Confirm that the dossier asserts neither lower semicontinuity of `C_CMH`, equality with an
  unnamed maximal Sobolev domain, transport of the canonical kernel through a noninvertible map,
  universal `CMH(4)`, nor KLS. The ledger target has no `bounded_by` edge; nevertheless verify
  that no fixed-cut or trace-upgrade obstruction is invoked. The standalone prescribed build
  succeeds to a 6-page PDF with no actual TeX error; expected cross-manuscript references are
  unresolved standalone. Authors are `/root/prove_cmh_approximation`; the reviewer must be
  distinct. Persist the result under `research/reviews/` and return the exact atomic ledger
  delta only if the verdict is pass; otherwise return a verbatim repair prompt naming every
  defect.
```
