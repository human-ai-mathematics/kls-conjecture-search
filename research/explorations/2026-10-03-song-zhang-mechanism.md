---
---

# Song–Zhang: the polynomial–curvature iteration and its remaining audit

## Question examined

Starting lens: **mine**. What does Song–Zhang, *An $O(4^{\log^*n})$ Bound for
the KLS Constant*, arXiv:2610.01447v1 (submitted 1 October 2026), add to
`conj:kls`, and which interfaces require checking before this repository relies
on it? The pinned source is [version 1](https://arxiv.org/html/2610.01447v1).
This is source integration, not a proof dossier or certification. No existing
route changes state. In particular, the comparisons below do not alter
`ap:s-occupation`, `ap:e-trace-upgrade`, or `ap:c-gate-zero`.

## What we learned

**Observed — source statements and conventions.** Theorems 5.1 and 7.1,
Proposition 6.1, and Lemmas 5.4 and 6.4 were read in the pinned HTML. Their
complete proofs and analytic dependencies have not received independent review
in this task. Here $\ell_0(x)=x$ and $\ell_{r+1}(x)=\log(e+\ell_r(x))$;
$\log^*$ instead counts ordinary natural logarithms until the argument is at
most one. These are different functions. The source's $\psi$ is the reciprocal
Cheeger constant, agreeing with the repository's $\Psi$ convention.

The exact all-depth bound announced in source Theorem 7.1 is

$$
C_P(\mu)\le C16^r\ell_r(\log(en))^2,
\qquad \psi_n\le C'4^r\ell_r(\log(en)),
$$

for every integer $n\ge1$, every isotropic log-concave probability measure
$\mu$ on $\mathbb R^n$, and every integer $r\ge1$, with $C,C'$ independent of
both $n$ and $r$. Its stated consequence is the corresponding
$16^{\log^*(n+2)}$ and $4^{\log^*(n+2)}$ bounds. Recording only fixed-depth
constants $C_r$ would lose precisely the assertion needed to choose $r$ using
$n$.

**Observed — hypothesis use and interfaces.** Put
$c_k(\nu)=\sqrt{K_k(\nu)}/k!$, where $K_k$ is the supremum of the variance of
the degree-$k$ Appell polynomial over symmetric coefficient tensors of unit
Hilbert–Schmidt norm, with all ordered tensor indices counted.

| Source item | Hypotheses that must travel with it | Mechanism and bottleneck |
|---|---|---|
| Theorem 5.1 | $0<\epsilon\le1$; nondecreasing $\ell:\mathbb N\to[1,\infty)$; $R\ge2^{40}\epsilon^{-2}$; centered regular $\nu$, $\operatorname{Cov}\nu\preceq I$; $c_k\le R^k\ell(k)^k/(k+1)^2$ for every $k$; curvature $D^2W\succeq aI$, $a>0$ | For dyadic $d\ge2$, obtains $C_P\le16(1+\epsilon)R^2\ell(d)^2\max\{1,a^{-1/(d+1)}\}$. A lowest nonconstant eigenfunction generates centered inverse-square-root derivative families. The unresolved audit is the accounting of removed mass and normalization defects. |
| Lemma 6.4 | Universal $K,r_0$; $r\ge r_0$; $\Gamma\ge Kr^2$; the depth-$r$ curvature profile holds for **every** centered regular law with covariance at most $I$, for all positive curvature parameters | Produces $c_d\le[(1+r^{-2})\Gamma]^d\ell_r(d)^d/(d+1)^2$ for every degree and every isotropic log-concave law, with covariance-contraction extension. Keeping zero initial values below top derivative order permits short-time localization with relative error approaching one. |
| Proposition 6.1 | Same centered regular class and covariance restriction; all $a>0$; constants universal across measures, dimensions and depths | Establishes $C_P\le\Gamma_r^2\ell_r(a^{-1})^2$ with $\Gamma_r\le C_04^r$. Theorem 5.1 and Lemma 6.4 alternate; Lemma 6.2 transports the profile to nonsmooth localization posteriors. |
| Theorem 7.1 | Arbitrary isotropic log-concave laws; every finite depth $r$ | Gaussian localization retains variance of a bounded near-extremizing test while covariance stays between fixed multiples of $I$. Whitening supplies curvature at time of order $1/\log(en)$; regular approximation removes regularity. |

In this article, “regular” means $e^{-W}dx$ with $W$ smooth and
$0<a_0I\preceq D^2W\preceq b_0I<\infty$, with $a_0,b_0$ depending on the
measure. This is a source-specific analytic class, not an identification with
the repository's CMH approximant assumptions.

**Observed — the Letwin entry point.** Source Lemma 2.1 is Letwin's quadratic
inequality, exactly the input recorded in `thm:letwin-qcts`. It is used in the
covariance-adapted polynomial localization of Section 4 and in the covariance
exit estimate of Lemma 7.3. The source does not require the general KLS bound
`thm:letwin-kls` as its bootstrap antecedent. Existing verification of
`thm:letwin-qcts` does not verify the new polynomial hierarchy or its analytic
extensions. The affine covariance factors and cross variations remain part of
the new proof's audit.

**Established — a limitation of the proposed “summable losses” direction.**
This is an algebraic observation about the displayed source thresholds, not a
new KLS theorem. At the refined step the source sets $\epsilon=r^{-2}$ and
$R=(1+r^{-2})\Gamma_r$. Hence Theorem 5.1 requires
$R\ge2^{40}r^4$, in addition to Lemma 6.4's $\Gamma_r\ge Kr^2$.
A uniformly bounded sequence $\Gamma_r$ cannot meet either growing threshold.
Therefore replacing only the factor $4$ in
$\Gamma_{r+1}=4e^{3/r^2}\Gamma_r$ by $1$ does not turn this written proof into
a dimension-free argument. An improvement must also redesign the coefficient
comparison thresholds, or avoid invoking them at arbitrarily large $r$.
Conversely these thresholds are requirements of the present proof, not lower
bounds on the true best curvature constants.

**Established — what the displayed recurrence does and does not say.** For a
fixed starting depth, multiplication gives
$\Gamma_r=4^{r-r_0}\Gamma_{r_0}\exp(3\sum_{j=r_0}^{r-1}j^{-2})$; convergence
of the series controls the second factor only. This verifies the elementary
constant bookkeeping conditional on the recurrence, without verifying that
recurrence's analytic input. Replacing $4$ by any fixed $q>1$ in the same
bookkeeping still yields an unbounded $q^r$ envelope; that is not a lower bound
or a counterexample to KLS.

**Observed — repository fences and non-implications.** The dimension-dependent
conclusion does not settle `conj:kls`. No implication has been supplied to
`conj:mm-spectral-occupation`, `conj:trace-upgrade`, `conj:gate-zero`,
`conj:gate-zero-sharp`, or the CMH approximation antecedents. In particular,
the inverse-operator family in Section 5 is not the canonical moment-map
Hessian; Appell degree estimates are not conditional-fiber spectral estimates;
and a new curvature bound does not discharge a fixed-cut occupation bound.
`prop:letwin-not-gate-zero` remains a fence on fixed-matrix deductions, while
the weighted spectator obstruction remains a fence on cut-relative routes.
No node with an open antecedent loses that antecedent here. The source's
improved general bound and the repository's `cor:loglog` concern different
quantities and must not be compared by their names alone.

## What resists

The main missing artifact is a source-import dossier and an independent
source-proof review. By the repository's imported-results rule, this new
preprint must remain open until that channel is completed. A favorable first
reading and a matching normalization do not replace it.

The most sensitive interface is Lemma 5.4 into Theorem 5.1: normalizers are
controlled only on a justified prefix; swap errors propagate through later
operators; dyadic recovery creates overlapping lag intervals. The argument
needs a degree-independent bound after summation, not merely an estimate at
each fixed degree. Lemma 6.4 then needs uniformity simultaneously in degree,
dimension and the induction depth. The thresholds above are a separate
obstacle to proposing bounded accumulated constants as an immediate extension.

## Proposed next step

1. Audit Section 3 and Lemmas 5.2–5.4 through Theorem 5.1 in a dedicated source
   dossier: operator domains, weak mixed derivatives, one normalization for the
   full family, adjacent-slot errors, factorial telescoping, lag-kernel
   summation and the first-exit justification. State exactly which source
   inequalities are imported and which have been rederived.
2. Audit Lemma 6.4 and Proposition 6.1 with both induction variables visible:
   small-degree initialization below $\lceil32r^2\rceil$; the uniform
   contraction estimate; regular-to-nonsmooth passage; and a single initial
   constant satisfying every later threshold. Then audit Section 7, including
   covariance lower control under whitening and the extension to all
   finite-energy locally Lipschitz tests.
3. Only after those audits, ask whether a new polynomial-to-curvature estimate
   can reduce the leading loss **and** remove the growing lower bounds on
   $R$ and $\Gamma$. Keep this as a research question until a precise statement
   and its blockers are formulated; no new speculative route is opened here.
