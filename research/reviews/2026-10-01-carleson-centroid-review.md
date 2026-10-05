---
authors:
  - researcher_implications, gpt-6-astra, 2026-10-01
reviewer: reviewer_implications, gpt-6-astra, 2026-10-01
fingerprints:
  solutions/thm-carleson-implies-centroid.md: 685b88976a10b43348d43f90365590a484b23e4ef2e5802df6f807416157bb7c
  thm:carleson-implies-centroid: 12c89986752df994119c0a38b481b7d746301531140842701e10630ef50074b2
  thm:scalar-riccati: 83fdb94d00721fdfab219b0a417b1ac815c170925d051a187929c3635241286d
  cor:per-direction: 41aeb34aa0f748e931a100d435bb6cbba97772f149ce25c2e089fc77974c1e43
  lem:survival-implies-kls: fcc0ff284f00b4f7d903900409e37db884463ad15f1f7cbb2c48ecb254e4cc64
  ass:all-cut-carleson: b452ee3e85d2c88c77f54ad68ef18d21c1d2ccb788281c54bd11f83daea4bba6
verdict: pass
---

**Findings.** Certify lens; fresh context reconstructed from repository artifacts,
without the authoring conversation. Author identity is supplied by the assignment.
This review certifies `thm:carleson-implies-centroid` in
`solutions/thm-carleson-implies-centroid.md`.

Lines 96–106 agree with the canonical theorem in `modules/15-carleson.md`:
the all-cut assumption implies the stopped centroid assumption and hence KLS.
The explicit constant is a valid strengthening. I compared the antecedent in
`modules/14-eldan-statements.md`, the conclusion and survival lemma in
`modules/21-mass-martingale.md`, the two certified Riccati inputs in
`modules/28-riccati.md`, and the notation and initial windows in
`modules/27-notation.md`. The claim is universal over the full initial range
$p_0\in[2/5,3/5]$, not merely over half-mass cuts.

Every step was checked:

- Lines 15–41: covariance decomposition gives $0\preceq B\preceq A$ and
  $R\succeq0$. Since $B=s\delta\delta^T$, the inequality
  $\delta^TA\delta\ge s|\delta|^4$ gives $D\ge r^2\ge0$.
  Isotropy and rank at most one give $r_0\le1$, including $B_0=0$.
  The continuous scalar semimartingale identity is exactly the certified input.
- Lines 59–65: summation is over fixed deterministic coordinate vectors.
  The certified directional bound, nonnegativity, and monotone convergence
  from finite horizons give $\mathbb E\int_0^\infty S_t\,dt\le\operatorname{Tr}R_0\le n$.
  Tonelli is valid. This is a finite-dimensional finiteness bound, never a
  dimension-free trace estimate.
- Lines 68–81: increasing localizers can additionally stop the continuous
  martingale, $r$, and accumulated nonnegative $S+D$ at growing levels,
  with deterministic caps. Local finiteness on bounded horizons ensures
  these stops tend to infinity. At each stopped horizon the martingale
  has zero expectation and all terms in the identity are integrable.
- Lines 84–88: terminal $r$ converges by continuity; it need not be monotone.
  Fatou applies to the sum of the nonnegative terminal and damping terms.
  The source integrals increase, so monotone convergence gives their exact
  limiting expectation. The resulting inequality, rather than an unjustified
  expectation equality, proves finite terminal expectation and finite damping
  occupation, both bounded by $1+n$. No terminal uniform integrability is used.
- Lines 89–93: the continuous adapted stopped process is jointly measurable.
  Its nonnegative expectation $u$ is measurable and bounded on finite
  intervals. The pointwise comparison with
  $\mathbf1_{\{t<\tau\}}r_t$ and Tonelli give finite $r$ occupation.
  Time endpoints have zero Lebesgue measure.
- Lines 110–124: only now is Carleson applied, on each deterministic prefix
  $I=[0,T]$ intersected with the specified coarse stop. All three occupation
  expectations are finite, so absorption involves no subtraction of infinities.
  This remains valid for negative $\alpha$; only $1-\alpha>0$ is needed.
  The auxiliary stops have disappeared before the premise is used.
- Lines 126–134: the integral inequality holds for each deterministic horizon.
  The displayed absolutely continuous majorant $v$ justifies Gronwall even
  without continuity of $u$. The integrating-factor calculation gives the
  stated bound and includes $C_1=0$.
- Lines 136–147: on the coarse window, $s\ge2/9$ and
  $|\delta|^2=r/s$. The occupation comparison therefore yields exactly
  $C=(9/2)(1+C_0T_0)e^{C_1T_0}$ for every $0<T\le T_0$ and every
  $p_0\in[2/5,3/5]$. The preliminary dependence on $n$ has disappeared
  from the constant after absorption.
- Lines 149–166: restricting to half-mass cuts is done only for the KLS
  conclusion. The covariance identity gives the mass bracket; boundedness
  permits the stopped isometry. The weak maximal inequality for the square
  gives factor 36 at displacement $1/6$. The chosen positive $T_*$ gives
  exit probability at most $C/[2(C+1)]<1/2$. The certified survival lemma
  applies with universal probability $1/2$ and posterior mass threshold $1/3$.

The hypotheses used are arbitrary finite dimension, isotropic log-concavity,
a fixed measurable cut in the full nested initial range, the manuscript's
localization, and universal finite $T_0>0$, $C_0,C_1\ge0$, $\alpha<1$
in `ass:all-cut-carleson`. No extra smoothness, approximation transfer,
random-interval estimate, or terminal integrability hypothesis is assumed.
The assumption's non-prefix intervals are unused additional strength.

All three `depends_on` nodes are certified, with the statements used here;
their existing certification passed the full check. The dossier derives the
final mass-martingale argument itself and does not depend on the open
`thm:centroid-implies-kls`. The ledger correctly retains
`ass:all-cut-carleson` in `assumes`. The conditional production of
`ass:stopped-centroid` does not discharge that assumption unconditionally.

There is no `bounded_by` edge on this target. The brief's operator-to-trace
warning is respected: the traced estimate is used only for finiteness.
P1 is respected because no equivalence with another trace-upgrade route is
claimed. P2 is respected because the open antecedent survives certification.
No posterior profile bound, covariance spectral control, static slice estimate,
spectator argument, sharp gate estimate, or numerical run is substituted for
the antecedent. The brief's other geometry-specific fences are not invoked.

**Corrections.** None required. Every step within scope is verified. There is
no external preprint import or unavailable source; certified inputs are used
as stated, as authorized. The separate manuscript proof's expectation-equality
presentation is not the argument certified here: this dossier explicitly
establishes the sufficient inequality by localization and Fatou.

**Validation.** The full command
`UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py` passed with exit 0
after tool escalation resolved the sandbox MyST startup failure. The checks
were neither changed nor bypassed; no MyST or certification errors remained.
Audited input hashes were checked before fingerprint generation and were
unchanged. The exact successful output of
`UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py --fingerprint solutions/thm-carleson-implies-centroid.md`
appears immediately before the verdict in front matter. Fingerprinting also
used tool escalation. The comparison additionally covered the canonical
stopped-centroid conclusion, even though the checker does not separately
emit that referenced conclusion in this dossier's fingerprint block.

**Exclusions.** This does not certify the Carleson antecedent, unconditional
centroid control, unconditional KLS, or any operator-to-trace conjecture.
The certified Riccati, directional, and survival proofs are not re-reviewed.
`solutions/thm-intro-weighted.md`, other arriving dossiers, and the separate
two-implication dossier are outside this report's certified scope.

```yaml
files:
  - research/reviews/2026-10-01-carleson-centroid-review.md
deltas:
  - path: research/program/ledger.yaml
    id: thm:carleson-implies-centroid
    status: proved
    depends_on: [thm:scalar-riccati, cor:per-direction, lem:survival-implies-kls]
    assumes: [ass:all-cut-carleson]
    proofs:
      - artifact: solutions/thm-carleson-implies-centroid.md
        review: research/reviews/2026-10-01-carleson-centroid-review.md
```
