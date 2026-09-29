---
---
# KLS route probe: cut-local replacement for the refuted weighted gate

Date: 2026-08-27

Role: `kls-route-prober`

Run id: `w3`

Concurrency key: `kls-gate:q:weighted`

Scope: one non-trace gate, namely the replacement requested by `q:weighted`. This probe does
not address `q:upgrade`, `q:stein-weighted`, or `q:alignment`, and it asserts no implication
among members of the trace-upgrade cluster. It uses no numerical experiment.

## Gate, quoted verbatim

The active gate in `research/kls/gating.md` is:

> The literal $e_0\le1$ global-operator-norm rate is refuted by the certified
> `prop:weighted-spectator-obstruction`. Formulate a replacement that either uses an explicit
> near-worst-measure hypothesis and re-audits consumption, or uses a cut-local, tensor-stable
> covariance weight that ignores independent spectators while still dominating the aligned
> two-tail mode. It must not insert an unproved lower bound for the localized profile. The
> certified `prop:spectator-excess-rate-obstruction` also refutes every uniform superlinear
> source-vanishing remainder even with weight one. The consumer only needs an $O(T)$ supply, so a
> surviving statement must allow that scale, make the remainder vanish with a genuinely cut-local
> source deficit, or impose an explicit near-worst-measure premise.

The old ledger question asked for
$$
 \mathbb E\int_0^{T\wedge\tau_\eta}
 e_t(E)(1+\|A_t\|_{\mathrm{op}})^{5/2}\,dt
 \le C\bigl(Te_0(E)+T^{1+\gamma}\bigr).
 \tag{W-old}
$$
It is refuted. The object tested here is instead
$$
 \lambda_{\mathrm{cut}}(A,K)
 =\frac{\|K\|_{\mathrm{HS}}^2}
 {\langle K,\mathscr L_A^{-1}K\rangle},
 \qquad
 \mathscr L_A(M)=\frac{AM+MA}{2},
 \tag{1}
$$
for $K\ne0$, with value zero at $K=0$, and the candidate weight
$$
 W_{\mathrm{cut}}(A,K)
 :=(1+\lambda_{\mathrm{cut}}(A,K))^{5/2}.
 \tag{2}
$$

At the start of this probe the Lyapunov node was to be treated as open. The fresh independent
repair review has since passed at
`research/reviews/2026-08-27-lem-lyapunov-stein-duality-repair-proof-review.md`, pinning SHA-256
`ea4680b012c611bb99af21639f885e05103e610e698139ee2f55445d5d28dc33`, and the ledger now records
`lem:lyapunov-stein-duality` as proved and agent-checked. Thus (1), including the support and
direct-sum conventions, is a certified input in the current snapshot.

## Term-by-term decomposition

Put
$$
 Q_t:=\frac{\mathcal S_{\mu_t}(E)}{s_t}
     =s_t\|K_t\|_{\mathrm{HS}}^2.
 \tag{3}
$$
This is the Stein source, equal to the Riccati source at exact balance and comparable to it on
the tight window through `lem:stein-vs-source`.

| term | demanded role | certified control | residue |
|---|---|---|---|
| $p_t$ and $\tau_\eta$ | keep one fixed cut in a universal tight balance window | mass martingale and tight-window consumer | no new issue |
| $e_t=P_t-I_{\mu_t}(p_t)$ | measure loss of near-minimality | unweighted integral is at most $(1+e_0)T$; near-worst bootstrap controls a stopped unweighted expectation | no joint estimate with $\lambda_{\rm cut}$ |
| $K_t$ and $Q_t$ | cut-indexed covariance source | exact Stein identity and tight-window conversion | the matching geometric trace theorem remains separate and open |
| $\lambda_{\rm cut}$ | ignore covariance blocks on which the cut tensor vanishes, while seeing aligned inflation | certified Lyapunov duality and exact direct-sum identity | singular $t^{-1}$ positive-time estimate gives no initial-layer occupation |
| $W_{\rm cut}$ | replace the global operator norm in the excess error | passes the exact cylinder and two-tail tests below | it is homogeneous of degree zero in nonzero $K$ and is not stable at $K=0$ under cross-block leakage |
| time supply | feed the Riccati--Gronwall consumer | only $O(T)$ is needed | $Te_0+T^{1+\gamma}$ is forbidden; a new $O(T)$ or screened supply is required |
| profile input | avoid circularity | explicit competitors may upper-bound a profile; the near-worst bootstrap uses $h_n^*$ externally | no unproved lower bound for $I_{\mu_t}(p_t)$ may be inserted |

The first genuinely new issue is therefore not exact independent spectators. It is robustness
when a tensor which was zero on the spectator block acquires a small spectator or cross-block
component.

## Exact algebra of the cut scale

Let $A\succeq0$, restrict to $H=\operatorname{Ran}(A)$, and diagonalize
$A|_H=\operatorname{diag}(a_1,\ldots,a_r)$ with $a_i>0$. The certified support inverse gives
$$
 \langle K,\mathscr L_A^{-1}K\rangle
 =\sum_{i,j=1}^r\frac{|K_{ij}|^2}{(a_i+a_j)/2}.
 \tag{4}
$$
Thus, for $K\ne0$, $\lambda_{\rm cut}$ is the $|K_{ij}|^2$-weighted harmonic mean of the
pair scales $(a_i+a_j)/2$. In particular,
$$
 \lambda_{\min}(A|_H)
 \le \lambda_{\rm cut}(A,K)
 \le \lambda_{\max}(A|_H).
 \tag{5}
$$

Now take $A=A_0\oplus B$ and write, in eigenbases of the two blocks,
$$
 K=\begin{pmatrix}K_0&C\\ C^T&K_1\end{pmatrix}.
$$
If $a_i$ and $b_j$ are the positive support eigenvalues, then
$$
 \begin{aligned}
 \|K\|_{\rm HS}^2
 &=\|K_0\|_{\rm HS}^2+\|K_1\|_{\rm HS}^2+2\|C\|_{\rm HS}^2,\\
 \langle K,\mathscr L_{A_0\oplus B}^{-1}K\rangle
 &=\langle K_0,\mathscr L_{A_0}^{-1}K_0\rangle
   +\langle K_1,\mathscr L_B^{-1}K_1\rangle
   +4\sum_{i,j}\frac{|C_{ij}|^2}{a_i+b_j}.
 \end{aligned}
 \tag{6}
$$
Equation (6) gives both the exact tensorization and its limit:

1. If $K_1=C=0$, then
   $\lambda_{\rm cut}(A_0\oplus B,K_0\oplus0)=\lambda_{\rm cut}(A_0,K_0)$, independently of
   the size and dimension of $B$.
2. If $K_0\ne0$ and
   $x=\|K_1\|_{\rm HS}^2+2\|C\|_{\rm HS}^2$, positivity of the extra denominator gives
   $$
   \lambda_{\rm cut}(A_0\oplus B,K)
   \le \lambda_{\rm cut}(A_0,K_0)
       \left(1+\frac{x}{\|K_0\|_{\rm HS}^2}\right).
   \tag{7}
   $$
   Thus high spectator eigenvalues cannot cause a blow-up when leakage is small relative to a
   nonzero active tensor.
3. There is no corresponding estimate uniformly through $K_0=0$. Let
   $$
   A_L=\operatorname{diag}(1,L),
   \qquad
   K_\varepsilon=\varepsilon(e_1e_2^T+e_2e_1^T).
   $$
   Then, for every $L>0$ and every $\varepsilon\ne0$,
   $$
   \|K_\varepsilon\|_{\rm HS}^2=2\varepsilon^2,
   \qquad
   \langle K_\varepsilon,\mathscr L_{A_L}^{-1}K_\varepsilon\rangle
     =\frac{4\varepsilon^2}{1+L},
   $$
   and hence
   $$
   \boxed{\lambda_{\rm cut}(A_L,K_\varepsilon)=\frac{1+L}{2}}
   \qquad(\varepsilon\ne0),
   \tag{8}
   $$
   whereas $\lambda_{\rm cut}(A_L,0)=0$ by convention.

Equation (8) is the first exact obstruction. Direct-sum invariance is exact, but it is not
perturbative tensor stability at a zero of the cut tensor. An arbitrarily small cross-block
contrast is charged at the arithmetic pair scale, independent of its amplitude. This is not a
counterexample to an integrated excess theorem: a geometric stability mechanism could force the
excess to vanish with the leakage. It does prove that the scale alone cannot encode that
mechanism. Any robust replacement must either remain in an exact split/cylinder class, impose a
premise ruling out such leakage, or make the excess remainder vanish with a cut-local source
deficit.

## Measurability, the zero convention, and singular support

These points are benign for a $dt$-integrated target, but load-bearing for a proof.

1. **Full-dimensional localization.** An isotropic law on $\mathbb R^n$ has positive-definite
   covariance and full affine support. Every finite-time localization tilt is equivalent to the
   initial law on that support, so $A_t\succ0$ for every finite $t$. On the tight window,
   $p_t,q_t>0$ and the conditional moments defining $K_t$ are adapted and continuous under the
   repository's localization regularity convention.
2. **Affine-support version.** More generally, the finite-time tilt does not change the affine
   support. Its rank is therefore deterministic and constant. On
   $H=\operatorname{Ran}(A_t)$, $K_t=P_HK_tP_H$, and the inverse in (1) is the ordinary inverse
   on $\operatorname{Sym}(H)$ followed by zero extension. Equivalently it is the ambient
   Moore--Penrose inverse. Cross entries involving a null direction are forbidden by support.
3. **Borel measurability.** On each fixed-rank stratum the denominator and quotient are
   continuous away from $K=0$. The Moore--Penrose map is Borel on the positive-semidefinite
   cone, so the totalized map $(A,K)\mapsto\lambda_{\rm cut}(A,K)$ is Borel on supported pairs.
   Consequently $W_{\rm cut}(A_t,K_t)$ is progressively measurable and is legitimate in a
   nonnegative $dt$ integral.
4. **No continuous extension at $K=0$.** For every nonzero scalar $c$,
   $\lambda_{\rm cut}(A,cK)=\lambda_{\rm cut}(A,K)$. Unless $A$ is scalar on its support, the
   directional limits at $K=0$ differ. The convention zero makes the map total and measurable,
   not continuous. The value at the single time $t=0$ is immaterial to a Lebesgue-time integral,
   but an Ito argument applied directly to $W_{\rm cut}$ is unavailable without a regularized,
   amplitude-sensitive surrogate.
5. **The existing excess measurability debt is not cured here.** The original gate already
   integrates $e_t=P_t-I_{\mu_t}(p_t)$. For rough laws and cuts, a proof still needs the same
   completed-filtration or regular-approximation convention for the random isoperimetric profile.
   The countable-family warning in `lem:inf-martingales` must not be mistaken for a profile
   supermartingale. The new weight adds no extra uncountable infimum.

## Required model tests

### Gaussian cuts

For a scalar Gaussian covariance $A=\sigma^2I$,
$\mathscr L_A(M)=\sigma^2M$. Therefore
$$
 \lambda_{\rm cut}(\sigma^2I,K)
 =\begin{cases}\sigma^2,&K\ne0,\\0,&K=0.\end{cases}
 \tag{9}
$$
Along localization of the standard Gaussian,
$\sigma_t^2=(1+t)^{-1}\le1$, so $W_{\rm cut}\le2^{5/2}$. The unconditional excess estimate
therefore gives, for every initially balanced finite-perimeter cut with $e_0\le1$,
$$
 \mathbb E\int_0^{T\wedge\tau_\eta}e_tW_{\rm cut}\,dt
 \le 2^{5/2}(1+e_0)T\le2^{7/2}T.
 \tag{10}
$$
For Gaussian halfspaces, $e_t=0$ identically; at exact balance $K_t=0$. Thus the convention at
$K=0$ causes no false cost on the exact minimizers.

### Aligned anisotropic two-tail

For the certified two-tail pair,
$$
 A_\Lambda=\operatorname{diag}(\Lambda,1,\ldots,1),
 \qquad
 K_\Lambda=8a\varphi(a)\Lambda e_1e_1^T,
$$
and certified Lyapunov calibration gives
$\lambda_{\rm cut}(A_\Lambda,K_\Lambda)=\Lambda$. Also
$$
 Q_\Lambda=16a^2\varphi(a)^2\Lambda^2,
 \qquad
 e_\Lambda=(2\varphi(a)-\varphi(0))\Lambda^{-1/2}.
 \tag{11}
$$
Hence
$$
 e_\Lambda W_{\rm cut}
 =(2\varphi(a)-\varphi(0))\Lambda^{-1/2}(1+\Lambda)^{5/2}
 \asymp\Lambda^2\asymp Q_\Lambda.
 \tag{12}
$$
More precisely, for every $\Lambda\ge1$,
$$
 \frac{Q_\Lambda}{e_\Lambda W_{\rm cut}}
 =\frac{16a^2\varphi(a)^2}{2\varphi(a)-\varphi(0)}
   \left(\frac{\Lambda}{1+\Lambda}\right)^{5/2}
 \ge \kappa_{\rm TT}>0,
 \tag{13}
$$
where the exact universal choice
$$
 \kappa_{\rm TT}
 :=2^{-5/2}\frac{16a^2\varphi(a)^2}{2\varphi(a)-\varphi(0)}
$$
is admissible. Thus the cut scale retains, rather than averages away, the aligned dangerous
mode.

### Fixed-block products

Suppose $\mu_t=\bigotimes_i\mu_t^{(i)}$ and the fixed cut is measurable with respect to
$J$. The certified block-support lemma gives $K_t=P_JK_tP_J$ pathwise. Since $A_t$ is diagonal,
$$
 \lambda_{\rm cut}(A_t,K_t)
 =\frac{\sum_{i,j\in J}|(K_t)_{ij}|^2}
 {\sum_{i,j\in J}|(K_t)_{ij}|^2/((A_t^{(i)}+A_t^{(j)})/2)}
 \le\max_{i\in J}A_t^{(i)}.
 \tag{14}
$$
Every coordinate outside $J$ disappears exactly, irrespective of its variance. In particular,
increasing the spectator dimension leaves the entire weight unchanged. The coordinate-budget
theorem still supplies only $\mathbb E\int S_t\,dt\le|J|$; it does not imply a universal
$O(T)$ estimate for $e_tW_{\rm cut}$. Active-coordinate covariance spikes and their correlation
with perimeter remain an analytic gap, even though irrelevant coordinates have been removed.

### Centered-exponential spectators

For the certified obstruction's cylinder
$E=E_0\times\mathbb R^N$, product localization gives, pathwise,
$$
 A_t=A_t^0\oplus B_t,
 \qquad
 K_t=K_t^0\oplus0.
 \tag{15}
$$
Therefore
$$
 W_{\rm cut}(A_t,K_t)=W_{\rm cut}(A_t^0,K_t^0),
 \tag{16}
$$
and the $N$ spectator variance spikes used in
`prop:weighted-spectator-obstruction` do not alter the weight. On the base-stability event in
the certified dossier, the base tilt ranges over a compact parameter set with a common local
exponential-moment domination. The base covariance is consequently bounded there; (5) bounds
$W_{\rm cut}$ there as well. The old $t^{-5/2}$ lower bound from a spectator coordinate is gone.

The second certified obstruction still applies: since $W_{\rm cut}\ge1$, no estimate with the
old $Te_0+T^{1+\gamma}$ remainder can hold universally. Its lower bound is only order $T$, so it
does not contradict a consumer-compatible $CT$ supply. The certified spectator proof therefore
does exactly what the gate demands on this model: it kills the old rate but does not kill the
cut-local $O(T)$ candidate.

## Attempted $O(T)$ supply and the first unjustified step

The clean candidate would be
$$
 \mathbb E\int_0^{T\wedge\tau_\eta}
 e_t(E)W_{\rm cut}(A_t,K_t)\,dt\le C_ET.
 \tag{17}
$$
It is exactly what the current consumer needs for cuts with $e_0\le1$. The known inputs do not
prove it:

1. $e_t\le P_t$ and the perimeter supermartingale control only
   $\mathbb EP_t$, not the correlated product $P_tW_{\rm cut}$.
2. Equation (5) and Brascamp--Lieb give only
   $W_{\rm cut}\le(1+t^{-1})^{5/2}$, whose integral diverges at zero.
3. The Lyapunov source estimate
   $Q_t\le4\lambda_{\rm cut}(A_t,K_t)/t$ gives a lower requirement on the cut scale when the
   source is large; it gives no upper bound on the weight.
4. `thm:bootstrap` bounds an unweighted stopped excess expectation through the cut-free first
   covariance moment $\Xi_T$. It has neither a weighted correlation estimate nor a high enough
   moment to multiply by (2). Replacing $\lambda_{\rm cut}$ by $\lambda_{\max}$ would erase the
   spectator repair.
5. A direct lower bound for $I_{\mu_t}(p_t)$ would be precisely the forbidden circular step.

The missing assertion is therefore a joint estimate saying that loss of the moving profile and
occupation of a large cut-oriented pair scale do not coincide too often. This is a
`needs new idea` gap, not a constant optimization or a consequence of the certified Lyapunov
lemma.

## Exact replacement interfaces

Two precise candidates survive the audit. Neither is asserted proved.

### Candidate A: minimal near-worst $O(T)$ supply

Fix universal $\varepsilon_{\rm nw},\varepsilon_E>0$ and a universal
$h_\bullet>0$. Ask for universal $C_E,T_0>0$ and $\eta\in(0,1/6]$ such that (17) holds whenever
$$
 h_n^*\le h_\bullet,
 \qquad
 h_\mu\le(1+\varepsilon_{\rm nw})h_n^*,
 \qquad
 p_0=\frac12,
 \qquad
 e_0(E)\le\varepsilon_Eh_\mu.
 \tag{18}
$$
One may choose $h_\bullet<c_{\rm prod}/(1+\varepsilon_{\rm nw})$, where
`prop:products` supplies $c_{\rm prod}>0$ for the centered-exponential products. Then the
certified spectator witnesses are explicitly excluded from (18). This is not an artificial KLS
assumption: if KLS fails, a sequence with $h_n^*\downarrow0$ eventually satisfies the first
condition, and near-worst measures and balanced cuts with arbitrarily small $e_0/h_\mu$ are
exactly the contradiction sequence available to the route.

If a matching Stein trace estimate has the form
$$
 \mathbb E\int_0^{T\wedge\tau_\eta}Q_t\,dt
 \le C_0T+C_1\mathbb E\int r_t\,dt
     +\beta\mathbb E\int D_t\,dt
     +C_2\mathbb E\int e_tW_{\rm cut}\,dt,
 \tag{19}
$$
with $2\beta+64\eta^2<1$, then (17) turns (19) into the certified tight-window Carleson input.
This is the old consumption proof with the global weight and superlinear rate removed. Thus
(17)--(19) are consumer-compatible without any change to the Riccati algebra.

Candidate A is the smallest clean replacement, but equation (8) warns that its full weighted
excess can be much larger than the actual source near $K=0$. Candidate B makes that deficit
explicit.

### Candidate B: source-screened near-worst supply

Choose once and for all $0<\kappa<\kappa_{\rm TT}$ and define the measurable aligned-source set
$$
 \mathcal A_{\kappa,t}
 :=\{Q_t\ge\kappa e_tW_{\rm cut}(A_t,K_t)\}.
 \tag{20}
$$
Ask only for
$$
 \mathbb E\int_0^{T\wedge\tau_\eta}
 e_tW_{\rm cut}\,\mathbf1_{\mathcal A_{\kappa,t}}\,dt
 \le C_ET
 \tag{21}
$$
under the near-worst hypotheses (18). The aligned two-tail configuration belongs to
$\mathcal A_{\kappa,t}$ by (13). In the leakage example (8), if the excess stays bounded below,
$Q_t=2s_t\varepsilon^2$ while $W_{\rm cut}\asymp L^{5/2}$, so the state lies outside
$\mathcal A_{\kappa,t}$ for small $\varepsilon$. Thus (21) charges the calibrated mode but not
an amplitude-free spectral direction with negligible cut source.

The corresponding trace statement must be re-audited, rather than obtained by blindly replacing
the old weight. One exact consumer-compatible form is
$$
 \begin{aligned}
 \mathbb E\int Q_t\,dt
 &\le C_0T+C_1\mathbb E\int r_t\,dt
      +\beta\mathbb E\int D_t\,dt\\
 &\quad+C_2\mathbb E\int
      e_tW_{\rm cut}\mathbf1_{\mathcal A_{\kappa,t}}\,dt
      +\theta\mathbb E\int
      Q_t\mathbf1_{\mathcal A_{\kappa,t}^c}\,dt,
 \end{aligned}
 \tag{22}
$$
where all integrals have limits $0$ and $T\wedge\tau_\eta$, $0\le\theta<1$, and
$$
 \frac{2\beta}{1-\theta}+64\eta^2<1.
 \tag{23}
$$
Indeed, absorb the last term of (22), use (21), and then use
$S_t\le2Q_t+64\eta^2D_t$. The resulting Riccati estimate has damping coefficient exactly the
left side of (23), and `cor:tight-window-consumption` applies.

Equation (22) says precisely what “remainder vanishes with a source deficit” must mean here. On
the complement of (20), a trace proof is not allowed to charge the full discontinuous weight;
it must return an absorbable fraction of the actual source. This is a stronger and more honest
geometric target than replacing $\|A_t\|_{\rm op}$ by $\lambda_{\rm cut}$ syntactically.

Candidate B is the recommended robust interface. It remains an open candidate: neither (21) nor
(22) is derived in this probe. In particular, (22) is not claimed to follow from the current
`q:stein-weighted` statement.

## Fence-by-fence audit

### `obs:two-tail`

Evaded exactly. Equations (11)--(13) show that the full $5/2$ scale is retained on the aligned
mode. The source screening can be chosen with $\kappa<\kappa_{\rm TT}$, so it does not discard
the obstruction.

### `obs:circularity`

Not discharged and not violated. Neither candidate inserts a lower bound for the moving
localized profile or asserts that it is a supermartingale. Candidate A or B still needs a new
non-circular proof, plausibly using the externally anchored near-worst bootstrap plus genuinely
cut-local information.

### `obs:relative-ceiling`

Respected. The proposed supply is absolute $O(T)$, restricted to near-worst measures and
near-minimizing cuts. It is not an all-measure relative bound for $\Xi_T$ and therefore does not
smuggle in KLS through `prop:ceiling`.

### `obs:crude-insufficient`

Respected. No use of the crude $\Xi_T\lesssim\log n$ estimate is made. The report explicitly
identifies why the existing unweighted bootstrap cannot be multiplied by $W_{\rm cut}$.

### `obs:proj-ceiling`

Evaded at the algebraic level. The scale uses the full matrix $K$ and Lyapunov energy, not radial
or projection-only tests. No dimension-free trace conclusion is inferred from this fact.

### `obs:rank-one-refuted`

Respected. Fixed-coordinate product cuts have an exact active block and pass the spectator test;
the coordinate budget remains valid. No rank-one counterexample or implication about
`q:alignment` is proposed.

## Viability verdict and exact residue

The cut-oriented scale materially improves the route: it removes the certified independent
spectator refuter and keeps the certified aligned two-tail calibration. The old global weight was
wrong for an exact algebraic reason; $\lambda_{\rm cut}$ fixes that reason.

It is nevertheless not a standalone replacement theorem. Its exact direct-sum invariance should
be called **cylinder tensor stability**, not perturbative tensor stability. Equation (8) is the
first obstruction to the stronger phrase. The analytic residue is:

1. **needs new idea:** prove the joint $O(T)$ correlation bound (17) under (18), or the screened
   bound (21);
2. **needs new idea:** prove a matching trace estimate such as (19), or preferably the
   source-deficit-aware (22);
3. **technical gap:** if a proof differentiates the weight, replace the discontinuous quotient
   at $K=0$ by an amplitude-sensitive regularization and show that its error realizes the same
   source-deficit split;
4. **fenced:** do not derive any of these bounds from a lower estimate on
   $I_{\mu_t}(p_t)$, from the crude covariance interface, or from projection-only data.

No current certified model refutes Candidate A or Candidate B. No current certified theorem
proves either. The strongest justified control-plane update is therefore to replace the vague
word “tensor-stable” by the exact distinction above and park (18)--(23) as candidate interfaces,
not to stage or promote a new node from this probe alone.

Proposed one-line gate update for the orchestrator:

> Test the near-worst $O(T)$ supply (17) with
> $W_{\rm cut}=(1+\lambda_{\rm cut})^{5/2}$; exact cylinders ignore spectators, but because
> $\lambda_{\rm cut}(\operatorname{diag}(1,L),\varepsilon E_{12}^{\rm sym})=(1+L)/2$ for every
> $\varepsilon\ne0$, a robust package must either control cross-block leakage or use the
> source-screened interface (20)--(23). Do not retain a superlinear remainder and do not insert a
> localized-profile lower bound.

No ledger, manuscript, bibliography, route-control, or knowledge edit is proposed here.

```yaml
outcome: complete
artifacts:
  - research/explorations/2026-08-27-kls-route-prober-cut-local-weighted-replacement-w3.md
proposed_deltas:
  - none; park Candidates A and B for orchestrator comparison and do not promote a new node from this probe
next_role: orchestrator
next_prompt: |
  Compare Candidate A, equations (17)--(19), with the source-screened Candidate B,
  equations (20)--(23). Preserve the exact distinction between direct-sum cylinder stability
  and perturbative cross-block stability. If route-control prose is updated, record the exact
  leakage identity (8), retain only an O(T) or explicitly near-worst/source-screened supply,
  and state that neither propagation nor the matching trace estimate is proved. Do not infer
  any implication involving q:upgrade, q:stein-weighted, or q:alignment.
```
