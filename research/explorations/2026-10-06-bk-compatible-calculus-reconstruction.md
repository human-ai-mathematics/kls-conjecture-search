---
---

# BK compatible derivatives, Hodge loss, and integration

## Question examined

On the prove lens, reconstruct `lem:bk-compatible-hodge` and
`prop:bk-integration-calculus` for `ap:bk-reconstruction`, from the BK source
at commit `4837c33649ba2271f43c9684e9350ecbdd725f95`, Lemma 3.1,
Appendices A–B and Section 4. The question is whether the projected divergence
estimate survives all tensor ranks on the maximal Hilbert-adjoint domain and
really yields bounded operators on the infinite sum of ranks.

## What we learned

*Established, uncertified:* the arguments are written in
`solutions/lem-bk-compatible-hodge.md` and
`solutions/prop-bk-integration-calculus.md`. They propose the canonical
statements in `lem:bk-compatible-hodge` and `prop:bk-integration-calculus`,
under `def:bk-compatible-calculus` and
`def:bk-uniform-appell-coefficients`.

The domain mechanism has three essential steps: finite-energy scalar
primitives, potential approximation, and the weak higher derivative equation.
The third step proves that the adjoint of the potential-core divergence is
exactly the maximal raw gradient. Density of potential fields by itself
would not establish the required adjoint graph core.

The rank-uniform mechanism is the exact curvature block calculation. On
multiplicity block alpha, subtracting the inverse-curvature cost from the
one-slot curvature gives a constrained quadratic minimization over the
orthogonal complement of the square-root multiplicity vector. The squared
length of that vector is the rank, which cancels the normalization denominator.
No estimate by the Hessian upper bound is used at that step.

| Hypothesis | Actual use |
| --- | --- |
| Smooth positive density on all of Euclidean space | Global curl-free primitives, distributional pairing, local Sobolev regularity and convolution |
| Positive lower Hessian bound | Classical scalar Poincare and positivity of curvature blocks |
| Finite upper Hessian bound | Bounded curvature multiplication in form-domain closure |
| Centering | Choice of primitives; linear primitive is contraction against x |
| Covariance at most identity | Constant-input operator has norm at most one |
| Ordered tensor norm and exterior increasing-index norm | Creation-operator and curl normalizations |
| Fixed finite rank during approximation | Rank-dependent cutoff errors vanish before assembling direct sums |

The integration mechanism is inversion of a form inequality with its domain
inclusion already proved, followed by an orthogonal direct sum. Appell
constant-input bounds use only the formal generating identity and the exact
coefficient norm at the fixed law; no uniform coefficient theorem is presumed.

## What resists

No unclosed mathematical step is claimed in these drafts. They remain
uncertified and require independent review, especially the weak regularity
argument, the simultaneous complex graph core, and the normalization in the
curvature block calculation. No KLS, BKL, SZ v2, CMH, occupation or trace
estimate is an input or a conclusion of these two dossiers.

The full checker was invoked with `UV_CACHE_DIR=/tmp/bk-uv-cache` but its MyST
build failed because sandbox Node/npm discovery fails. Missing-anchor reports
from that failed build are not a mathematical finding. The orchestrator is
coordinating a full check after canonical registration and table-of-contents
integration.

## Proposed next step

A fresh reviewer should check both stated theorems, including bijectivity and
the adjoint graph core, against the registered canonical statements. Check
that the curvature lower bound has no hidden dependence on rank and that
all inversions compare closed forms with the correct domain inclusion.
No route-state change or ledger status transition is proposed by the author.
