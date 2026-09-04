---
type: exploration
date: "2026-09-04"
outcome: candidate
approach: ap:cone-boundary-gap
nodes:
  - conj:kls
candidates:
  - id: cand:cone-seam-capacity
    statement: >-
      There is a dimension-free bound on the seam capacity of a multi-facet or product
      cone boundary: for normalized cone measure on a polytopal cone in R^n, the
      tangential Dirichlet energy concentrated on the union of facet seams is bounded by
      a universal constant times the total tangential Dirichlet energy, uniformly in the
      dimension and in the number of facets.
  - id: cand:brenier-simplex-hessian
    statement: >-
      The Brenier potential transporting the standard Gaussian to the isotropic uniform
      simplex in R^m has Hessian bounded in operator norm by a universal constant,
      uniformly in m, after the rotation that optimizes the Monge-Ampere transmission
      condition at the vertices.
---

# Synthesizer: search state at the harness migration

*Written during the migration onto `conjecture-search-template`. It records the search state that
the retired route documents used to hold, so that `research/program/portfolio.yaml` can name a
blocker without restating it.*

## Why this record exists

`research/kls/routes.md`, `gating.md`, `obstructions.md` and `routes/*.md` were mutable documents
mixing three things the new harness keeps apart: mathematical claims (now the manuscript and
ledger), search state (now the portfolio), and the reasons search state changed (now checkpoints).
Their unique content has been distributed. This checkpoint carries the part that is neither a
claim nor a route state: two precise statements that block parked probes and that had no home in
the old layout, because the old layout had no candidate genre.

## The two parked probes

**Cone-boundary spectral.** A universal tangential Poincaré gap for normalized cone measure would
feed the published Kolesnikov–Milman Hardy boundary bridge. The analytic right-cone falsification
test survives uniformly, including smooth isotropic roundings, so the probe was not killed. The
first open wall is a dimension-free multi-facet/product seam-capacity estimate, recorded above as
`cand:cone-seam-capacity`. See
[the route scout](2026-08-27-kls-route-scout-novel-w2n01.md) and
[the cone probe](2026-08-27-kls-route-prober-cone-boundary-spectral-w3b01.md). No theorem, no KLS
implication beyond the published conditional bridge, and no ledger status is asserted here.

**Laplace–Brenier simplex.** The rotation-optimized simplex Monge–Ampère transmission bound must
be decided before a Laplace–Brenier route is worth registering; it is recorded above as
`cand:brenier-simplex-hessian`. See
[the probe](2026-08-27-kls-route-prober-laplace-brenier-simplex-w2b01.md).

Both are candidates rather than nodes on purpose. Neither has a manuscript anchor, neither has a
status, and a candidate is the only place a statement may be written down that is not yet a node
(`CLAUDE.md` constraint 7). That is what lets the portfolio block a route on a named statement
without copying it.

## Carried forward from wave four

The wave-four record notes an interruption before close-out, so these remain open coordination
items rather than mathematical claims:

- a cold independent check of `solutions/lem-cmh-linear-spectral-resolution.tex`, whose node
  `lem:cmh-linear-spectral-resolution` is `open` and whose dossier is unreviewed;
- the never-written review of `lem:fiber-root-degree-two`, likewise `open` with an unreviewed
  dossier; and
- six proposed adversarial instances awaiting curation into `research/instances.md`:
  `stress-fiber-frame-simplex-pencil`, `stress-tailunion-cut-scale`,
  `stress-cylinder-spectator-excess`, `stress-cmh-ab-exponential-limit`,
  `stress-cmh-ab-reservoir-split`, `fence-cmh-m9-boundary`.

## What this record does not do

It asserts no mathematics. Every fence formerly listed in `obstructions.md` is now an
`obstruction` environment in the manuscript with its own ledger node, and every gate deliverable
formerly in `gating.md` is now an approach objective in the portfolio.
