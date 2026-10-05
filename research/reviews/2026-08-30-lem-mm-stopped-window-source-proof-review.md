---
verdict: pass
authors:
  - claude-prover-w4p02, unknown, 2026-08-30
reviewer: proof-checker-w4r03, unknown, 2026-08-30
fingerprints:
  solutions/lem-mm-stopped-window-source.md: 6720200970a6602c89fb52b16fe1be8116f5996d647d824ef9aa678e3bb191b4
  lem:mm-stopped-window-source: c405064bb67767843b0c86c8266cc60e9693dc13df3968410792d1a5b3f6b5e1
  thm:letwin-qcts: 8e2ac0819f46db553fe83a6f3034436816565262316c2e6bde7d81baead1a082
---

# Stopped initial-layer source bound — independent proof review

Cold review of `solutions/lem-mm-stopped-window-source.tex`, reviewed SHA-256
`a559c44fc9288c76be10be2d75a650c7f74524ef3ed5562490867f51a16a7e82`. The proof was
reconstructed from the dossier, the manuscript (`modules/kls/30-spectral-route.tex`,
`modules/kls/02-family-stochastic-localization.tex`, `modules/kls/14-qcts-obstruction.tex`,
`modules/kls/00-orientation.tex`), the KLS ledger, and the bibliography. The prover's
conversation was not available and the prover's exploration record was consulted only to
confirm authorship. Author (`claude-prover-w4p02`) and reviewer (`proof-checker-w4r03`) are
distinct.

## Findings

### Statement agreement

The dossier theorem, the ledger `statement:` of `lem:mm-stopped-window-source`
(`research/kls/ledger.yaml`), and the manuscript lemma at
`\label{lem:mm-stopped-window-source}` in `modules/kls/30-spectral-route.tex` agree
mathematically: for every regular approximant, every fixed test with $\Var_\mu(f)=1$, every
$L\ge1$ and $T>0$, with $\tau_L=\inf\{t:\norm{A_t}_\op\ge L\}$,
$\E\int_0^{T\wedge\tau_L}\norm{H_t}_{\HS}^2\,dt\le 8L^2T$, uniformly in dimension and
regularization, **conditional on `thm:letwin-qcts`**. All three surfaces carry the same
constant $8L^2$, the same quantifiers, and the same conditionality. The tensor
$H_t=\E_t[(f-\E_tf)(X-a_t)^{\otimes2}]$ and $A_t=\Cov_{\mu_t}(X)$ match
`\eqref{eq:spectral-quantities}` verbatim, and the dossier's posterior tilt
$\dd\mu_t\propto\exp(c_t\cdot x-t|x|^2/2)\dd\mu$ is exactly the localization density
`\eqref{eq:sl-density}` of `subsec:sl-process`, realized through the planted filtering
channel — the same convention as in the previously certified dossiers
`lem-mm-time-weighted-fixed-source` and `lem-mm-posterior-defect` (checked against the
former's density display directly). The dossier proves slightly more than the manuscript
demands (centering and isotropy of $\mu$ are not used), which is a legitimate refinement,
explicitly recorded.

The header comment "candidate node, ledger acceptance pending / ledger entry has not yet
been created" is stale: the node now exists in `research/kls/ledger.yaml` with
`status: open` and `depends_on: [thm:letwin-qcts]`. The created statement is the one the
dossier proves, so this is an editorial remark, not a semantic mismatch.

### Conditional standing (constraint 7)

The conditional standing is carried in **both** the statement (the theorem title and its
first sentence "Assume Hypothesis~`ass:sol-sws-letwin`") and the header (`conditional :
thm:letwin-qcts`). Hypothesis `ass:sol-sws-letwin` restates the imported bound
$\Var(Y^TMY)\le8\norm M_{\HS}^2$ for isotropic log-concave $Y$ and symmetric $M$; this is
verbatim the ledger statement of `thm:letwin-qcts` and the manuscript display
`\eqref{eq:letwin-qcts}` in `modules/kls/14-qcts-obstruction.tex` (whose remark records the
version-1 arXiv preprint status of `Letwin2026QuadraticKLS`). The dossier certifies only
the implication; under constraint 7 the node stays at most `conditional` after this review.

### The steps, checked line by line

**Step 0 (posterior facts).** Conditional on $X=x$, $(c_s)_{s\le t}$ is Brownian motion
with constant drift $x$; the Cameron–Martin density of that path law against Wiener measure
is $\exp(\int_0^t x\cdot\dd w_s-\tfrac t2|x|^2)=\exp(x\cdot c_t-t|x|^2/2)$, so the
likelihood depends on the path only through $c_t$ and Bayes' rule for the joint law
$\mu(\dd x)\otimes P^x$ gives exactly `\eqref{eq:sol-sws-posterior}` as a version of
$\mathcal L(X\mid\mathcal F_t)$ at each fixed $t$. The extension of
`\eqref{eq:sol-sws-bayes}` from bounded to $L^1(\mu)$ tests by conditional monotone
convergence and linearity is correct (the a.s. null set may depend on the test; only
countably many tests are used, at fixed times). The posterior potential
$V(x)-c_t\cdot x+\tfrac t2|x|^2$ has Hessian $\succeq(\varepsilon+t)I$, so $\mu_t$ is
smooth, strongly log-concave, has Gaussian tails hence all moments, and $A_t\succ0$ (a
nontrivial linear functional cannot be a.s. constant under an everywhere-positive density).
Joint measurability of the posterior moments in $(t,\omega)$ via the explicit ratios
evaluated at $(t,c_t(\omega))$ is correct.

**Step 1 (a.e. definedness of $H_t$).** For fixed $t$, $\E[\E_tf^2]=\E_\mu f^2<\infty$
gives $\E_tf^2<\infty$ a.s.; Tonelli (joint measurability from Step 0) makes the
exceptional set $\dd t\otimes\dd\Prob$-null. Off it, conditional Cauchy–Schwarz plus all
posterior moments give absolute convergence of the defining integral of $H_t$, so the
zero-convention on the bad set is harmless for every integral in the proof. Checked.

**Step 2 (whitened duality).** At a fixed good pair, $Y=A_t^{-1/2}(X-a_t)$ is an
invertible affine image of the log-concave $\mu_t$, hence log-concave, centered, with
covariance $I$: isotropic log-concave, so Hypothesis `ass:sol-sws-letwin` applies to its
law. The algebra
$\langle M,\widehat H_t\rangle_{\HS}=\E_t[(f-m_t)Y^TMY]=\Cov_{\mu_t}(f,Y^TMY)$ is correct
for symmetric $M$ (trace cyclicity; the interchange of $\E_t$ and trace is licensed by
Step 1's absolute convergence; the covariance identity uses that $f-m_t$ is centered and
$Y^TMY\in L^2(\mu_t)$). Cauchy–Schwarz plus the hypothesis give
$\langle M,\widehat H_t\rangle\le v_t^{1/2}\sqrt8\norm M_{\HS}$; since $\widehat H_t$ is
symmetric (congruence of the symmetric $H_t$ by the symmetric $A_t^{-1/2}$), the supremum
over symmetric $M$ with $\norm M_{\HS}\le1$ attains the full HS norm (take
$M=\widehat H_t/\norm{\widehat H_t}_{\HS}$). This yields
$\norm{\widehat H_t}_{\HS}^2\le8v_t$ a.e., with no expectation, no stopping, and no
independence assertion — as claimed.

**Step 3 (unwhitening strictly before the exit time).** $t<\tau_L$ implies
$\norm{A_t}_\op<L$ purely from the definition of the infimum; the HS-ideal inequality
$\norm{A_t^{1/2}\widehat H_tA_t^{1/2}}_{\HS}\le\norm{A_t^{1/2}}_\op^2\norm{\widehat
H_t}_{\HS}=\norm{A_t}_\op\norm{\widehat H_t}_{\HS}$ is correct
($\norm{A^{1/2}}_\op^2=\norm A_\op$ for $A\succeq0$). Hence
$\norm{H_t}_{\HS}^2\one_{\{t<\tau_L\}}\le8L^2v_t$ a.e. The operator norm enters only
through this deterministic pathwise bound; **no moment of $\norm{A_t}_\op$ and no
independence step occurs anywhere in the dossier** — verified by reading every display.

**Measurability of the stopped integral (reviewer-verified routine detail).** The
dossier's claim that only the inf-implication and "no stopping-time property" of $\tau_L$
are needed is accurate in the sense intended (no optional stopping, no strong Markov, no
martingale property is invoked). Plain measurability of the event $\{t<\tau_L\}$ is still
required for the statement's expectation and for Tonelli in Step 4; it holds, and I
verified it from the dossier's own standing hypotheses: for each fixed $\omega$, $t\mapsto
c_t(\omega)$ is continuous, and the tilted moment integrals
$(t,z)\mapsto\int x^{\otimes j}e^{z\cdot x-t|x|^2/2}\dd\mu$ ($j=0,1,2$) are continuous on
$[0,\infty)\times\R^n$ by dominated convergence (dominant $|x|^je^{R|x|}$, integrable
because $\nabla^2V\succeq\varepsilon I$ gives Gaussian tails), with positive denominator;
hence $t\mapsto A_t(\omega)$ is continuous. For continuous paths,
$\{\tau_L>t\}=\{\sup_{s\in([0,t]\cap\mathbb Q)\cup\{t\}}\norm{A_s}_\op<L\}$, a measurable
event, so $\tau_L$ is a measurable random time and $\{(t,\omega):t<\tau_L(\omega)\}$ is
product-measurable. This is a routine completion consistent with the proof as written; it
changes no constant and adds no hypothesis.

**Step 4 (variance budget and integration).** $\E m_t=\E_\mu f$ and Jensen give
$\E m_t^2\ge(\E_\mu f)^2$; the split $\E v_t=\E_\mu f^2-\E m_t^2$ is legitimate because
both terms are finite ($\E m_t^2\le\E\E_tf^2=\E_\mu f^2$). Hence $\E v_t\le\Var_\mu(f)=1$
**without assuming $f$ centered** — the dossier correctly routes around the missing
centering via Jensen. Tonelli for the nonnegative, jointly measurable integrand, the
pathwise bound of Step 3, and $\int_0^T\E v_t\,\dd t\le T$ give
$\E\int_0^{T\wedge\tau_L}\norm{H_t}_{\HS}^2\dd t\le8L^2T$. All constants check:
$8=(\sqrt8)^2$ from the hypothesis, $L^2$ from one operator-norm factor squared, $T$ from
the variance budget. The claimed uniformity holds: neither $n$, nor $\varepsilon$, nor $T$,
nor any property of $f$ beyond $\Var_\mu(f)=1$ enters the constant.

### Hypothesis accounting

Used: (i) the planted Gaussian channel and the fixed-time Bayes identification; (ii)
$V\in C^\infty$, $\nabla^2V\succeq\varepsilon I$, $\varepsilon>0$ — only for posterior
positive-definite covariance, all posterior moments, and (in the reviewer-verified detail)
Gaussian-tail domination; $\varepsilon$ enters no constant; (iii) $f\in L^2(\mu)$ with
$\Var_\mu(f)=1$; (iv) Hypothesis `ass:sol-sws-letwin` — the sole unresolved premise. Unused
but stated: $L\ge1$ (the proof is valid verbatim for every $L>0$; a sharpening
opportunity, not a defect); centering/isotropy of $\mu$ and every other regular-class
property (explicitly disclaimed in the dossier, deliberately so for the restart
companion). No hypothesis is used silently.

### Dependency closure and citation debt

The node's only formal dependency is `thm:letwin-qcts`, `import_class:
preprint-unreviewed` (`Letwin2026QuadraticKLS`, arXiv v1, 27 July 2026). The dossier
imports its statement exactly as recorded in the ledger and manuscript and carries it as an
explicit hypothesis; the preprint itself is not verifiable with this reviewer's tools and
is *not* certified here — only the implication is. Cameron–Martin/Bayes is classical
textbook material requiring no bibliography debt. No numerical artifact, run, or battery
result is used anywhere.

### Fences

The ledger node carries no `bounded_by` edge; I checked the registered obstructions
independently of the dossier's own fence paragraph and concur:

- `prop:covariance-spike` (published, `modules/kls/00-orientation.tex`): respected
  constructively — the estimate is confined strictly before the exit time $\tau_L$ and
  asserts nothing unstopped; the dossier's scope remark correctly disclaims any
  universal-time or unstopped occupation claim.
- `rem:two-tail-slice-bounds`, `rem:profile-circularity`, `rem:single-coordinate-cuts`: no cut, slice, or excess
  estimate occurs.
- `rem:projection-ceiling`: the only tensor input is the full symmetric-matrix quadratic bound,
  imported conditionally; no projection/radial test is promoted.
- `rem:crude-insufficient`, `rem:relative-ceiling`: no crude covariance integral or
  relative occupation premise appears.
- The recorded marginal-independence fallacy is not engaged: the product
  $\E[v_t\norm{A_t}_\op^2]$ is never formed.

Constraint 6 is untouched: nothing crosses to `conj:trace-upgrade`, `conj:stein-weighted`, or
`conj:product-alignment`.

### Standalone build

From `solutions/`: `latexmk -g -pdf -outdir=../build lem-mm-stopped-window-source.tex`
exits 0 and produces the PDF; the only warnings are the expected standalone `??`
cross-module references (`thm:letwin-qcts`, `subsec:spectral-sde`,
`lem:mm-time-weighted-fixed-source`, `lem:mm-posterior-defect`,
`prop:covariance-spike`, `conj:mm-spectral-occupation`). Before this report,
`python3 research/check_ledger.py` reported 0 errors (202 nodes).

## Corrections

None required for correctness. Two optional editorial hardenings for a future pass,
neither affecting the proved claim: (a) add one sentence recording pathwise continuity of
$t\mapsto A_t$ (dominated convergence, Gaussian tails) so that the measurability of
$\{t<\tau_L\}$ used by Tonelli is explicit; (b) refresh the stale "ledger entry has not
yet been created" header comment.

## Exclusions

This review certifies only the conditional implication
`thm:letwin-qcts` $\Rightarrow$ `lem:mm-stopped-window-source` in the immutable dossier
scope above. It does not certify the Letwin preprint, any unstopped or universal-time
source bound, any occupation statement toward `conj:mm-spectral-occupation`, the companion
dossiers (`lem-mm-restart-deweighting`, `lem-mm-smallgap-fourth-moment`,
`prop-mm-window-occupation`), any property of $\tau_L$ beyond measurability and the
inf-implication (in particular not that it is a stopping time), or any claim for
non-smooth or degenerate laws. Ledger wiring, header updates, and manuscript changes are
outside this reviewer's write surface.
