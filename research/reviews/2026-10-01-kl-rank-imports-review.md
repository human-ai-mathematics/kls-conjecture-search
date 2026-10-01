---
verdict: pass
authors:
  - researcher_kl_rank, gpt-6-astra, 2026-10-01
reviewer: reviewer_kl_rank, gpt-6-astra, 2026-10-01
fingerprints:
  solutions/thm-kl-rank-imports.md: 52cd35f3794190112e2f36593b406fcca2fcd497a2b61be956da9d6909c987de
  thm:kl-stopped-rank-tail: 7d8dc0ce69117b511df2a07d6645566c72a46a4e1fc7d0b85c402162e0155fb7
  thm:improved-lichnerowicz: e95e127c46fbf098fb23cb186b9d7312b213063339704596555ab33696f2968f
  thm:kl-integrated-rank-covariance: d7cca26dd40d0570566c90fbc463c9fb64ab148aef54eec9f84e0d04baddd43d
---

# Independent certification of the Klartag–Lehec rank imports

## Findings

**Pass**, for both `thm:kl-stopped-rank-tail` and
`thm:kl-integrated-rank-covariance`, on the fingerprinted versions above.
This is a `certify` review under `.codex/agents/reviewer.toml`. I reconstructed
the argument from the repository and the actual sources in a fresh context
containing the assignment and author handoff, without the conversation that
produced the proof. I did not author or repair the dossier and used no subagents.
The checkpoint and structural checker were not evidence of mathematical validity.

### Statements, dependencies, and scope

The theorem bodies at `solutions/thm-kl-rank-imports.md:38–64` agree with
`modules/30-covariance-technology.md:48–74`. The class is compactly supported,
isotropic log-concave probabilities on $\mathbb R^n$, $n\ge1$. The stopping
times are relative to the driving Brownian filtration, including its usual
augmentation. The threshold is exactly $3$, the exponential is exactly
$\exp(-t^{-1/8})$, the inverse second moment has logarithmic power $16$, and
the integrated exponential has coefficient $2$ on precisely $[0,1]$.
There is no time rescaling. The tilt and covariance SDE also agree with
`modules/27-notation.md:29–80`.

I read the actual ledger entries at `research/program/ledger.yaml:146–158`:

| Node | Current status | Recorded proof dependency | Assessment |
|---|---|---|---|
| `thm:improved-lichnerowicz` | proved, on `Klartag2023Logarithmic` | none | Established published input; statement and application checked |
| `thm:kl-stopped-rank-tail` | open | `thm:improved-lichnerowicz` | Exactly the analytic input used in the dossier |
| `thm:kl-integrated-rank-covariance` | open | `thm:kl-stopped-rank-tail` | Supplies the inverse moment; the covariance cap is derived in the same dossier from the transitive analytic input |

Neither target has `assumes` or `bounded_by` entries. No open antecedent is
silently assumed. The stopped result, currently open in the ledger, is proved
earlier in this same dossier and is certified by this report together with the
integrated result. Consequently the proposed status transitions must install
both proof records, with the stopped result preceding or accompanying the
integrated one. Certifying only the integrated node while leaving its dependency
open would not be a valid ledger transition.

The established input at `modules/03-family-bochner-hminus1.md:18–26` matches
Theorem 1.3, equation (1.8), of Klartag, *Logarithmic bounds for isoperimetry and
slices of convex sets*, **Ars Inveniendi Analytica** (2023), Paper 4. I checked
the actual [published-text PDF](https://arxiv.org/pdf/2303.14938v2), including
its strong log-concavity convention and the argument in Section 2. Its constant
is $1$ in $C_P\le\sqrt{\|\operatorname{Cov}\mu\|_{\rm op}/t}$, with the
variance/Dirichlet-energy convention used here. This is an established input,
not another unreviewed preprint import or a consequence of the target being
certified.

### Complete source dependency audit

The pinned source is Klartag–Lehec, *Thin-shell bounds via parallel coupling*,
[arXiv:2507.15495v2 PDF](https://arxiv.org/pdf/2507.15495v2), with its
[v2 HTML](https://arxiv.org/html/2507.15495v2) also available. The PDF identifies
the version as 23 February 2026 and carries a title-page date of 24 February
2026. I read the proof sections themselves, including the local PDF text,
rather than inferring validity from the abstract or source availability.
Every row of the dossier's dependency map was checked:

| Source location (printed PDF pages) | Dossier lines | Result of audit |
|---|---|---|
| Section 2, (8)–(14), Lemma 2.1, pp. 6–7 | 110–150 | The bounded, Lipschitz tilt barycenter gives the required global adapted solution from zero. Spatial flow derivatives from the rest of Lemma 2.1 are unnecessary. |
| Section 4, (36), p. 16 | 152–178 | The same $A(t,\theta)\preceq t^{-1}I$ is derived from the established input, with nonsmooth laws covered. |
| Section 5, (57)–(59), pp. 23–24 | 385–408 | The direct bounded-coefficient martingale argument proves the qualitative initial exit estimate actually used. The quantitative window (58) is not imported. |
| Lemma 5.2, (60)–(62), pp. 24–25 | 182–211 | The projected quadratic Poincaré and Cauchy–Schwarz argument gives the exact tensor bound. |
| Lemma 5.3, (63)–(70), pp. 25–26 | 131–150, 213–259 | Covariance SDE, Hessian, and stopping are justified, with the necessary a.e. derivative interpretation. |
| Lemma 5.4, (71)–(74), pp. 27–29 | 261–327 | All large/large, separated, and remaining low-pair regions are covered. |
| Lemma 5.5, (75)–(78), pp. 29–30 | 331–382 | A fully explicit replacement proves coefficient $64$. The source's interpolation exercise and coefficient $12$ are not needed. |
| Proposition 5.1, (79)–(87), pp. 30–32 | 412–478 | Geometric iteration, terminal limit, and all-time extension preserve the exact target. |
| Corollary 6.1, (88)–(91), pp. 32–33 | 482–519 | Stopping at the first rank hit and layer cake yield the two stated consequences. |
| Theorem 6.2, pp. 33–34 | 521–554 | The pathwise first-hit split and integrable rank profile give the exact integrated estimate. |

The reference to Corollary 4.10 in Theorem 6.2 introduces covariance/eigenvalue
notation. The proof of Theorem 6.2 does not invoke its transport or negative
Sobolev conclusion. Guan's technique motivates the source argument, but the
required tensor and growth estimates are proved here; no separate unchecked
Guan theorem remains in this dependency chain.

### Mathematical checks

**Localization and analytic class (lines 110–211).** Compact support permits
all tilt differentiations and bounds centered moments uniformly over the tilt
parameters for the fixed law. The bounded covariance is the Jacobian of the
barycenter, so the pathwise ODE has global existence and uniqueness; Picard
iteration gives adaptation. Positive tilts preserve affine support, and
isotropy makes that support full dimensional. Differentiating the logarithmic
normalizer in time and applying Itô gives the displayed density martingale.
The product rule for the barycenter outer product gives precisely the drift
$-A_t^2$ and centered third-moment diffusion tensor. The finite-dimensional
coefficient bounds suffice for the stochastic integrals used subsequently.

The projection argument factors out $e^{-t|y|^2/2}$; the remaining joint
integrand is log-concave, so Prékopa–Leindler preserves the parameter on the
projected subspace. For Gaussian smoothing, completing the square leaves
strong-convexity parameter $t/(1+t\varepsilon)$ and covariance
$\operatorname{Cov}\nu+\varepsilon I$. These are the correct parameters,
not $t$ after smoothing. Compactly supported $Y$ and the coupling
$Y+\sqrt\varepsilon G$ justify convergence through fourth moments. Smooth
cutoffs justify the polynomial tests for the convolved laws. Passing their
Poincaré inequalities to the limit proves the required quadratic inequality
without imposing smoothness on the original density or its support boundary.
The linear top-eigenvector test gives $u\le\sqrt{u/t}$, hence $u\le t^{-1}$.
The bound holds for every tilt, so it is pathwise at all positive times.

For the restricted tensor, $H$ is symmetric and
$S=\operatorname{Tr}H^2=\mathbb E[X_kY^THY]$. The gradient of $Y^THY$ is
$2HY$, giving variance at most $4t^{-1/2}u^{3/2}S$. Centering $X_k$ allows
Cauchy–Schwarz with this variance, proving the claimed inequality after
division by $S$ when positive. The cases $S=0$ and the zero subspace are
covered. Independence of coordinates is never assumed.

**Spectral calculus, stopping, and growth (lines 213–327).** The polynomial
trace expansion gives the displayed Hessian with a sum over all ordered
pairs, including its diagonal terms. Uniform polynomial approximation of
$f''$, integrated twice, controls both derivatives and divided differences;
it extends the formula to $C^2$ functions and repeated eigenvalues. Rotating
the noise coordinates preserves the sum of squared third-tensor components.
Thus no differentiable choice of eigenvectors, eigenvalue simplicity, or
uncounted collision contribution is required.

Bounded coefficients on each finite time interval make the stopped stochastic
integral a true martingale and its drift integrable. The expectation is
absolutely continuous. Replacing $\mathbf1_{t\le\sigma}$ by
$\mathbf1_{t<\sigma}$ changes neither the time nor Brownian integral, since
their difference is supported on the graph of a single time per path.
The formula is justified a.e.; it is not a pointwise differentiability
assertion at deterministic stopping times.

In the growth bound, assigning a largest eigenvalue in each triple costs at
most three by tensor symmetry, with ties harmless. The restricted tensor bound
then gives $12t^{-1/2}\sum_{\lambda_i\ge r}\lambda_i^{5/2}$, and the cap
turns this into $12t^{-1}\sum_i f(\lambda_i)$. For two high eigenvalues the
divided difference is $2$; for eigenvalues separated by the interval
$[r,r+1]$ it is at most $8$. Every remaining pair has maximum at most $r+1$.
Its divided difference is at most $D^2f$ evaluated at its larger eigenvalue.
For a low third index, use the tensor estimate with the first index fixed;
for a high third index, use $f(\lambda_i)\le16$ and fix the third index.
Both sums have the claimed $t^{-1/2}$ bound. These are upper bounds, so a
possibly negative divided difference presents no sign problem; no convexity
of $f$ was used. The nonnegative potential permits domination of the stopped
drift by the stopped potential itself.

**Replacement cutoff (lines 331–382).** I checked the four endpoint data,
the integral $J=7a/12+b/2-d/12$, and the factorization proving positivity of
$h_*$. The condition $d\le b/2$ follows from $rD\ge2$. The bound on $J$
ensures $M>0$, while $J>0$ gives $M\le270$. The quartic bump has integral
$1/30$ and vanishing value and derivative at both endpoints. Thus the
integrated polynomial has the required endpoint values and first two
derivatives. The stated basis derivative bounds give $|h'|<600$; since
$f\ge1/e$ and $e<3$, this yields
$f''\le1800D^2f<(64D)^2f$. The exponential and quadratic pieces satisfy
the bound too. Positivity, monotonicity, and $C^2$ matching are all proved.

**Initial remainder and iteration (lines 385–478).** At the first operator
norm hit of $2$, the identity
$M=A-I+\int A_s^2ds$ forces $\lambda_{\max}(M)\ge1$. Some matrix entry
therefore has absolute value at least $1/n$. Bounded quadratic variation and
the two-sided exponential martingale bound give the displayed union estimate,
which is faster than every power for each fixed law and dimension. It is
valid uniformly in the subsequently chosen stopping time.

The threshold decrements sum to $2t^{1/8}\le1$. On each positive time
interval, $D_j^2/\sqrt{s}\le1/s$; replacing $D_j$ by $64D_j$ only enlarges
the universal growth constant. Absolute continuity suffices for Gronwall.
I checked all three regions of $f_j\le(9/4)g_{j+1}+e^{-t_j^{-1/8}}$ and
the resulting recursive factors. The series defining $C_b$ converges for
every fixed universal $b$. The remainder is bounded by
$L_\mu 2^{bm}\mathbb P(\tau_*\le t_m)$ and tends to zero by the preceding
estimate. Neither $L_\mu$ nor the law-dependent quadratic variation bound
survives this limit. This proves a universal constant even though the initial
window was not uniform in the law or dimension. For $t\ge2^{-8}$ the trivial
count and $e^{-t^{-1/8}}\ge e^{-2}$ complete the all-time assertion.

**Hitting times and integration (lines 482–554).** Continuous adapted ordered
eigenvalues give stopping times $\sigma_k>0$, allowing the value $\infty$.
On a finite first hit the $k$th eigenvalue equals $3$, so at least $k$
eigenvalues of the stopped covariance are at least $3$. This yields $n/k$.
Tonelli's layer cake is applied to the nonnegative inverse hitting time;
strict/non-strict events only enlarge its bound. With $q=n/k$,
$x_0=(2\log q)^8$ gives $qe^{-x_0^{1/8}/2}=1$. Splitting the exponent
leaves a finite integral proportional to $\Gamma(16)$ and the term
$(2\log q)^{16}$. This includes $q=1$ and the convention
$\infty^{-2}=0$.

For each rank, the interval before $\sigma_k\wedge1$ uses the threshold
bound and the remaining interval uses $1/t$. No singular integral at zero
is introduced. Exponentiation gives $e^6\max(1,\sigma_k^{-2})$, bounded
by the displayed $e^6(1+\sigma_k^{-2})$. The function
$(1+\log(1/x))^{16}$ is decreasing and integrable on $(0,1]$, so its right
endpoint rank sum is at most its integral times $n$. Covariance continuity
and finite-sum Tonelli justify the integrals and expectations. Eigenvalues
are reordered at each time throughout; eigenvector trajectories are absent.

### Hypotheses and build evidence

All hypotheses used are present or conventional for the stated process:
compact support, log-concavity, isotropy, finite positive dimension, standard
Brownian normalization, adapted stopping, positive times in the growth
argument, and ordered ranks $1\le k\le n$. Compact support supplies the
moment and martingale bounds and the terminal limit. Log-concavity supplies
the projected analytic estimates. Covariance identity supplies the initial
separation from thresholds. Mean zero is part of the stated isotropic
normalization; the proof is translation invariant, so this component alone
could be relaxed without affecting the result. There is no hidden smooth
boundary, unconditional symmetry, or uniform support-radius assumption.

I ran `UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py`. The initial
sandboxed run failed at Node startup and could not load manuscript anchors;
those resulting missing-anchor messages are not mathematical findings.
The requested tool-escalated full run completed the MyST build and reported
exactly one error:

```text
FAIL prop:weighted-spectator-obstruction.proofs[0]: the statement of 'ass:weighted-package' changed since research/reviews/2026-08-27-prop-weighted-spectator-obstruction-repair-proof-review.md fingerprinted it; it needs a new review
```

It reported no MyST error for this dossier, which remained listed as a draft.
The unrelated stale certification was neither changed nor counted as a defect
in these proofs. The full repository check is therefore not claimed to be green.

The escalated command
`UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py --fingerprint solutions/thm-kl-rank-imports.md`
then exited successfully. Its exact output is the front-matter fingerprint
block. Repeated byte hashes confirmed that the dossier, both relevant
statement modules, and the ledger did not change between the mathematical
reads, full check, and fingerprint run. No numerical experiment was used as
proof evidence.

## Corrections

No mathematical correction is required for either target.

There is a nonblocking provenance discrepancy at
`solutions/thm-kl-rank-imports.md:577–585`: the description of the ledger read
by the author is historical, and its reference to the “present ledger” no
longer describes the entries reviewed here. The two dependency edges now
exist, as recorded above. I used those actual entries and checked the
corresponding statements. This discrepancy does not omit a mathematical
dependency from the argument or from the fingerprints. No dossier edit was
made; a later edit would require a new review of the changed version.

The two source qualifications are valid and material: the arbitrary-stopping
derivative is used only a.e., and coefficient $64$ replaces the unverified
coefficient $12$ construction. Every downstream step was checked with these
qualifications. This pass does not certify the stronger auxiliary formulations
that the dossier explicitly declines to use.

## Exclusions

This review certifies only the two exact rank statements. It does not certify
the full preprint, the thin-shell conclusion, Corollary 4.10's transport or
$H^{-1}$ estimates, Guan's separate results, or an extension to noncompact
laws, arbitrary initial covariance, or anticipative random times. The published
analytic theorem and standard Prékopa–Leindler, Itô, and continuous-martingale
background are external inputs, not newly certified repository results.

No orientation, cut-tensor alignment, posterior-Hessian alignment,
eigenfunction-source alignment, or KLS conclusion follows from this review.
In particular `conj:trace-upgrade`, `conj:mm-spectral-occupation`, and
`conj:stein-weighted` are not discharged. The independent recertification
involving `ass:weighted-package` is outside scope.

## Proposed certification records and handoff

The following are proposed ledger changes only. Apply both target records
and retain their existing references and dependency edges; no additional
`assumes` or `bounded_by` relation is proposed. The established improved
Lichnerowicz node remains unchanged.

```yaml
files:
  - research/reviews/2026-10-01-kl-rank-imports-review.md
deltas:
  - file: research/program/ledger.yaml
    node: thm:kl-stopped-rank-tail
    set:
      status: proved
      depends_on: [thm:improved-lichnerowicz]
      references: [KlartagLehec2025ThinShell]
      proofs:
        - artifact: solutions/thm-kl-rank-imports.md
          review: research/reviews/2026-10-01-kl-rank-imports-review.md
  - file: research/program/ledger.yaml
    node: thm:kl-integrated-rank-covariance
    set:
      status: proved
      depends_on: [thm:kl-stopped-rank-tail]
      references: [KlartagLehec2025ThinShell]
      proofs:
        - artifact: solutions/thm-kl-rank-imports.md
          review: research/reviews/2026-10-01-kl-rank-imports-review.md
```
