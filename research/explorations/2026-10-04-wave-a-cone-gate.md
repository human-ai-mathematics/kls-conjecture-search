---
---

# Wave A: the product-simplex cone gate

## Question examined

Lens: prove. Route `ap:c-gate-zero`; candidate
`cand:cone-transverse-equality-simplex`; targets `conj:gate-zero-sharp` and
`conj:gate-zero`. Derive the full linear gate spectrum for all product-simplex
and interval bases and every real $\beta\ge n$, using the certified
`prop:cone-moment-map`, rather than a finite parameter sweep.

The precise proposed family theorem, including all quantifiers, is the theorem
`thm:sol-product-simplex-cone-gate` in
`solutions/prop-product-simplex-cone-gate.md`, proposed for the new node
`prop:product-simplex-cone-gate`. It is an uncertified draft.

## What we learned

*Established, pending independent review:* after making each simplex factor
isotropic, the three required scalar base moments are

$$
a_k=\frac{2(k+2)}{k+4},\qquad
b_k=\frac{2(k+1)(k+2)}{(k+3)(k+4)},\qquad
c_k=\frac{(k+2)(k^2+9k+2)}{(k+3)(k+4)}.
$$

They are respectively the scalar coefficients of
$\mathbb ET^2$, $\mathbb E[VV^\top T]$, and
$\mathbb E[|V|^2VV^\top]$ for an isotropic uniform $k$-simplex and its
canonical kernel $T$. The dossier derives them from the simplex integral.
Independent permutation symmetries make the cone gate block diagonal, with
axis eigenvalue $1+n/\beta$ and transverse block eigenvalue

$$
\lambda_k=\frac{a_k\beta^2+(1+2b_k)\beta+n-k+c_k}{\beta(\beta+1)}.
$$

For $t=\beta-n\ge0$ and $d=n-k-1\ge0$, its sharp gap has the exact identity

$$
(k+3)(k+4)\beta(\beta+1)(2-\lambda_k)
=4(k+3)t^2+[5k^2+27k+28+8(k+3)d]t
+4d[(k+3)n+k+1].
$$

All coefficients are positive. Thus every such cone satisfies the sharp
linear bound two; the axis attains it exactly at $\beta=n$ and a transverse
block attains it exactly at $\beta=n$, $k=n-1$. With more than one
positive-dimensional factor, the axis is the full equality eigenspace.
With one factor and $\beta=n$, the gate is $2I$.

*Established correction to the earlier candidate's parametrization:*
an interval is a one-dimensional simplex. If its wording allows $r=0,s=1$,
then its literal assertion “if and only if $r=1,s=0$” omits that same geometric
base represented as one interval. This case already appears in the certified
`cor:cube-cone-gate-zero` at $n=\beta=2$. The corrected condition is
“exactly one positive-dimensional simplex factor, counting each interval as a
one-dimensional simplex.” This is a parametrization correction, not a new
geometric equality case or violation of the sharp bound. If the candidate
silently required $r\ge1$, its wording needs only that convention made explicit.

The identity also gives $\lambda_k\to a_k$ as $\beta\to\infty$, identifying
the limiting transverse value with the gate of the simplex base. No numerical
computation is used as evidence or as a route decision in this checkpoint.

## What resists

No algebraic step remains open in the family proof as written; its correctness
awaits independent review. The argument requires product-simplex symmetry and
explicit polynomial base kernels. It does not cover a general convex base,
nonlinear CMH test functions, or either universal gate conjecture. It asserts
no equivalence between the gate and the high-rank trace-upgrade cluster.
In particular passing the sharp linear bound does not prove $\mathrm{CMH}(4)$.

## Proposed next step

Add the proposed canonical statement as an open node, then assign a fresh
reviewer to `solutions/prop-product-simplex-cone-gate.md`. Audit in particular
the intrinsic simplex Jacobian, all three block moments, vanishing mixed
blocks, the positive-coefficient identity, and the interval convention.
Proposed dependencies are `def:exponential-cone` and `prop:cone-moment-map`;
there are no conditional antecedents. These nodes and the gate conjectures
have no `bounded_by` edges; the brief's distinction between constants two and
four is respected. The Dirichlet kernel is rederived rather than relying on
the stronger statement `thm:cmh-dirichlet`.

After certification, promote the family theorem and close
`cand:cone-transverse-equality-simplex` with the interval convention corrected.
Keep `ap:c-gate-zero` active: replace its completed family-algebra test by a
test of which base moment inequalities control transverse gates without
product-simplex symmetry. No universal target status changes, and no
certification or candidate closure is asserted by this checkpoint.
