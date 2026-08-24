# CMH route — regression models

These are fixed adversarial models, not a menu from which a prover may choose a convenient
subset. They are registered in the shared battery at
[`../../../knowledge/instances.md`](../../../knowledge/instances.md). No CMH-specific `finum`
target exists yet, so the status below is analytic/reporting status only.

| model | evidence level | detects | does not decide |
|---|---|---|---|
| Gaussian moment map | exact calibration | signs, adjoints, square-root normalization; all commutators vanish | noncommutative shape control |
| aligned product moment maps | analytic calibration | tensorization and commuting multipliers | eigenframe rotation |
| rotated product exponentials | reported; dossier pending | negative individual Haar nodes in the originating calculation | failure of the globally summed inequality |
| Gamma/Laguerre near-extremizers | reported; dossier pending | near-exhaustion of descendant and leaf slack | the exact universal constant in the global bound |
| localized high-frequency product exponential | reported; dossier pending | wrong leading sign for conformal-only reservoir allocation | the coupled conformal/traceless/corrector estimate |
| $45^\circ$ two-exponential projection with one-dimensional child | structural calibration under boundary decay | conditional/scalar channel; the scalar Stein equation forces $S=K$ | Airy mismatch, because $\mathsf D=0$ structurally |
| rotated Gamma--Gaussian | reported; dossier pending | failure of the guessed conservation of $\mathbb E[\operatorname{cof}(T)a\mid z]$ | full tensor Hodge estimate |
| three-exponential projection | exact density/kernel compatibility audit | a genuine canonical-versus-inherited Stein mismatch | universal CMH without reconstructing $K$ |

## Three-exponential projection

Let $Y_1,Y_2,Y_3$ be independent standard exponentials and

$$
\xi_1=Y_1-Y_3,\qquad \xi_2=Y_2-Y_3,
\qquad m(\xi)=\max(0,-\xi_1,-\xi_2).
$$

The reported density and inherited Stein kernel are

$$
\rho(\xi)=\frac13e^{-\xi_1-\xi_2-3m(\xi)},
$$

$$
S(\xi)=
\begin{pmatrix}
\xi_1+2m+2/3&m+1/3\\
m+1/3&\xi_2+2m+2/3
\end{pmatrix}.
$$

On the positive cone, the exploration reports that $S^{-1}$ fails the Hessian compatibility
equations, so the inherited kernel is not the canonical moment-map kernel: $S-K\not\equiv0$.
The next exact model calculation is to solve for an Airy potential in

$$
K_\lambda=S-\rho^{-1}R^\top D^2\lambda R
$$

under the requirement that $K_\lambda^{-1}$ be a Hessian, with positive-definiteness, global
convexity, interface, boundary, and integrability conditions across the three cones. This is the
preferred nontrivial Hodge regression.

## Gate discipline

- A model that is too commutative to activate a term is a calibration, not positive evidence.
- A negative node does not refute a full-tree statement.
- A sampled quantity can be directional only unless `finum` supplies the repository-prescribed
  provenance and verdict gates.
- A rigorous analytic model can refute a precise universal form, but the calculation must be
  persisted; the consolidated summary alone is not the dossier.
