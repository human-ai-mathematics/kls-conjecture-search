---
---
# Prover: cut-oriented Lyapunov--Stein duality (wave 2, S01)

Date: 2026-08-27

Role: `/root/prove_lyapunov_stein_duality_w2`

Scope key: `solution:lem-lyapunov-stein-duality`

## Contract, dependency, and target audit

The open ledger node is `lem:lyapunov-stein-duality`, anchored at
`lem:lyapunov-stein-duality` in `modules/kls/21-carleson.tex`. Its statement is
$$
s_t\langle K_t,\mathscr L_{A_t}^{-1}K_t\rangle\le \frac4t,
\qquad
\mathscr L_A(M)=\frac{AM+MA}{2},
$$
and hence, with
$$
\lambda_{\rm cut}(A,K)
=\frac{\|K\|_{\rm HS}^2}{\langle K,\mathscr L_A^{-1}K\rangle}
$$
for $K\ne0$ and zero for $K=0$,
$$
s_t\|K_t\|_{\rm HS}^2
\le \frac{4\lambda_{\rm cut}(A_t,K_t)}t.
$$
The statement also requires invariance under irrelevant direct sums
$A\oplus B,K\oplus0$. The surrounding manuscript prose identifies the scale as a weighted
harmonic mean and says it equals the inflated variance in the anisotropic two-tail example.

The only direct dependency is the proved, agent-certified `lem:pathwise-BL`; its proof and its
persisted review contain and check the stronger anisotropic intermediate inequality used here.
Its transitive two-color input `prop:stein-rep` is also agent-certified. The target has no
`bounded_by` edge. There is no unresolved premise, so the dossier is an unconditional candidate
proof in the stated localization setting.

There is no statement mismatch among the current manuscript, ledger, and dossier. The dossier
adds only the requested covariance-support convention, Moore--Penrose realization, harmonic-mean
formula, and two-tail calibration; it does not strengthen the stochastic conclusion.

## Proof mechanism

At a fixed $t>0$, let $H_t=\operatorname{Ran}(A_t)$. Every zero-variance direction is constant
$\mu_t$-almost surely, so all conditional means and covariances defining the color tensor obey
$K_t=P_tK_tP_t$. Thus the Lyapunov operator can be inverted on the finite-dimensional Hilbert
space $\operatorname{Sym}(H_t)$.

For $M\in\operatorname{Sym}(H_t)$, the certified pathwise Brascamp--Lieb calculation gives the
anisotropic estimate
$$
s_t\langle K_t,M\rangle^2
\le \frac4t\operatorname{Tr}(MA_tM)
=\frac4t\langle M,\mathscr L_{A_t}M\rangle.
$$
Here the exact two-color pairing is obtained from
$g=(\mathbf 1_E-p_t)/\sqrt{s_t}$ and the centered quadratic $f_M$:
$$
\mathbb E_{\mu_t}[g f_M]=\sqrt{s_t}\langle K_t,M\rangle.
$$
The posterior is $t$-uniformly log-concave on its affine support, and its Gaussian factor places
$f_M$ in the Brascamp--Lieb form domain.

For a positive-definite self-adjoint operator $L$ on a finite-dimensional Hilbert space,
$$
\sup_{M\ne0}\frac{\langle K,M\rangle^2}{\langle M,LM\rangle}
=\langle K,L^{-1}K\rangle.
$$
Applying this with $L=\mathscr L_{A_t}$ proves the claimed dual estimate. For $K_t\ne0$, the
denominator is strictly positive and multiplication by its defining quotient yields the
cut-scale source bound. The case $K_t=0$ is handled separately, so no $0/0$ division occurs.

If $A$ is merely positive semidefinite, then in an ambient $A$-eigenbasis the Moore--Penrose
inverse is
$$
(\mathscr L_A^\dagger C)_{ij}
=\begin{cases}
2C_{ij}/(\lambda_i+\lambda_j),&\lambda_i+\lambda_j>0,\\
0,&\lambda_i+\lambda_j=0.
\end{cases}
$$
On supported inputs this agrees with the inverse on $\operatorname{Sym}(\operatorname{Ran}A)$.
Consequently, for positive support eigenvalues $\lambda_1,\ldots,\lambda_r$,
$$
\lambda_{\rm cut}(A,K)
=\frac{\sum_{i,j}|K_{ij}|^2}
{\sum_{i,j}|K_{ij}|^2/((\lambda_i+\lambda_j)/2)},
$$
the $|K_{ij}|^2$-weighted harmonic mean of $(\lambda_i+\lambda_j)/2$.

For block-diagonal input, the support inverse sends
$K\oplus0$ to $\mathscr L_A^{-1}K\oplus0$, proving exact direct-sum invariance. In the
two-tail example,
$$
A_\Lambda=\operatorname{diag}(\Lambda,1,\ldots,1),
\qquad
K_\Lambda=8a\varphi(a)\Lambda e_1e_1^T,
$$
so $\mathscr L_{A_\Lambda}^{-1}K_\Lambda=K_\Lambda/\Lambda$ and
$\lambda_{\rm cut}(A_\Lambda,K_\Lambda)=\Lambda$ exactly.

## Dead ends and exclusions

- Choosing only $M=K/\|K\|_{\rm HS}$ in the anisotropic inequality recovers the coarser
  $\lambda_{\max}(A)$ bound and discards the cut orientation. The proof instead takes the full
  Hilbert-space dual norm of the Lyapunov energy.
- Treating $\mathscr L_A$ as invertible on every ambient symmetric matrix is false when $A$ is
  singular. The dossier restricts to the covariance support and records the exactly equivalent
  Moore--Penrose formula on supported inputs.
- The quotient definition cannot be used blindly at $K=0$. That case is stated and proved
  separately.
- Direct-sum invariance is claimed only for a genuinely irrelevant block with contrast zero. No
  invariance is asserted for cross-block or spectator contrast.
- The result is static at each $t>0$. Integrating the displayed $t^{-1}$ upper bound through zero
  is invalid; no initial-time occupation, operator-to-trace upgrade, or high-rank trace estimate
  is claimed.

## Fence and hypothesis audit

There is no formal `bounded_by` edge. The proof nevertheless respects the live obstructions:

- On `rem:two-tail-slice-bounds`, it returns $\lambda_{\rm cut}=\Lambda$ rather than an impossible absolute
  constant.
- It uses the complete matrix orientation and therefore does not infer tensor control from radial
  or projection-only tests (`rem:projection-ceiling`).
- Its exact spectator invariance removes no active block and proves no equivalence inside the
  trace-upgrade cluster.
- The singular $t^{-1}$ factor is retained, so the dossier does not disguise the open small-time
  covariance-occupation problem.

The hypotheses actually used are: a fixed $t>0$; a finite-time stochastic-localization posterior
on its affine covariance support; $p_t,q_t>0$ so the two-color quantities are defined; the
$t$-uniform Brascamp--Lieb inequality; and the certified two-color pairing. No isotropy at time
$t$, full ambient rank, numerical evidence, compact support, smooth cut, or open conjectural
input is used. There are no unclosed analytic steps or unstated hypotheses.

## Validation and status

The standalone command

```bash
cd solutions && latexmk -pdf -outdir=../build lem-lyapunov-stein-duality.tex
```

succeeded and produced a three-page PDF. The log contains only expected unresolved cross-module
references; it has no TeX error, overfull box, or underfull box. The artifact hashes are:

```text
a66f3d93d9af8d38eba1c8ced50adcdb6a744d341af34275ab131f7a15bd69af  solutions/lem-lyapunov-stein-duality.tex
a328d60845b0be79bf8733e5ed18abbdf826ed73c8b777de53d985f99446e4cb  build/lem-lyapunov-stein-duality.pdf
```

The dossier remains `checked_by: none`. There is no applicable ledger delta before independent
review. The deferred candidate value is
`solution: solutions/lem-lyapunov-stein-duality.tex`.

```yaml
outcome: complete
artifacts:
  - solutions/lem-lyapunov-stein-duality.tex
  - research/explorations/2026-08-27-prover-lyapunov-stein-duality-w2s01.md
proposed_deltas:
  - none; checked_by remains none and the solution path is deferred until independent certification
next_role: proof-checker
next_prompt: |
  Cold-review `solutions/lem-lyapunov-stein-duality.tex` for ledger node
  `lem:lyapunov-stein-duality`, without using the prover's conversation history. The theorem is
  unconditional in the manuscript's localization setup and claims, for each fixed `t>0`,
  `s_t <K_t,L_{A_t}^{-1}K_t> <= 4/t`, hence
  `s_t||K_t||_HS^2 <= 4 lambda_cut(A_t,K_t)/t`, with `lambda_cut=0` handled
  separately at `K=0`; exact invariance under `A direct-sum B,K direct-sum 0`; the
  eigenbasis weighted-harmonic-mean formula; and `lambda_cut=Lambda` on the certified
  anisotropic two-tail pair. Reconstruct the proof from repository artifacts. In particular,
  verify that a covariance contrast is supported on `Ran(A_t)`; that the anisotropic
  Brascamp--Lieb inequality
  `s_t<K_t,M>^2 <= (4/t)Tr(MA_tM)` follows with the exact factor 4 and valid form-domain
  closure; that `Tr(MA_tM)=<M,L_{A_t}M>`; and that finite-dimensional energy duality gives
  `<K,L_A^{-1}K>` without a reciprocal or constant error. Audit the covariance-support and
  ambient Moore--Penrose conventions, including singular `A`; positivity of the denominator;
  the explicit `K=0` branch; off-diagonal multiplicities in the harmonic-mean formula; direct
  sums when either covariance block is singular; and the exact two-tail calculation. Confirm
  the node has the proved dependency `lem:pathwise-BL`, no unresolved premise, and no formal
  `bounded_by` edge. Check that the dossier makes only a static `t>0` statement and does not
  infer an integrable initial-time or covariance-occupation theorem. Recompile standalone. If
  and only if every step and the manuscript/ledger match pass, persist a distinct-author proof
  review and propose the atomic certification delta to the orchestrator; otherwise return one
  verbatim repair contract covering every defect.
```
