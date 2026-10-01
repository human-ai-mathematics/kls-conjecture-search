---
authors:
  - researcher_implications, gpt-6-astra, 2026-10-01
reviewer: reviewer_implications, gpt-6-astra, 2026-10-01
fingerprints:
  solutions/thm-centroid-implies-kls.md: 8e9a13746994862e649f2af8ecd39974306d6162b594a7f6b17aef5cddbc4e0d
  thm:centroid-implies-kls: bec6e9e498c2213c6df56d73527db7b7852448a3e752803658da5621c8b0b44a
  lem:survival-implies-kls: fcc0ff284f00b4f7d903900409e37db884463ad15f1f7cbb2c48ecb254e4cc64
  ass:stopped-centroid: 432245682ae8c45cd4f82b39e269d572d49da816fa22e4a038eecfe1576211bc
  thm:intro-all-cut: 78be5464d7a8b5d0bf207fff884df733be0c64715d2a27760109e1128ccc5547
  cor:tight-window-consumption: 7d0f9e5dce52482fc3b8f93155bb46e66596d3aac7d92a63f7e508bc25b59946
  ass:all-cut-carleson: b452ee3e85d2c88c77f54ad68ef18d21c1d2ccb788281c54bd11f83daea4bba6
verdict: pass
---

**Findings.** Certify lens; fresh context reconstructed from repository artifacts,
with no access to the authoring conversation. The assignment supplies the author
identity. This review certifies exactly `thm:centroid-implies-kls` and
`thm:intro-all-cut` in `solutions/thm-centroid-implies-kls.md`.

The theorem at lines 36–40 agrees with `modules/21-mass-martingale.md`'s
canonical centroid implication. Lines 78–81 agree with `thm:intro-all-cut`
in `modules/14-eldan-statements.md`. The universal Cheeger conclusion is the
equivalent KLS formulation in `modules/00-overview.md`. I checked the full
statements of both antecedents, the survival lemma and the tight-window
corollary, together with the localization and stopping conventions in
`modules/27-notation.md` and the ledger edges.

Every proof step was checked:

- Lines 17–34: the indicator covariance is $p_t(m_t^E-a_t)=s_t\delta_t$.
  The stopped mass increment is a bounded continuous martingale, so its
  square is an integrable nonnegative submartingale and the stopped
  quadratic-variation isometry is legitimate.
- Lines 44–60: half-mass cuts are covered by the assumed initial range.
  Continuous exit forces displacement at least $1/6$ on $\{\tau\le T\}$.
  The weak maximal inequality applied to the square gives exactly
  $36\mathbb E M_T^2$; no factor from the strong $L^2$ maximal inequality
  is missing. The bracket is the displayed integral, and $s_t^2\le1$
  gives the claimed bound. The antecedent ensures its finiteness.
- Lines 63–75: $T_* >0$, including when $C=0$, and
  $36CT_*\le C/[2(C+1)]<1/2$. Survival yields posterior masses at least
  $1/3$ with probability at least $1/2$. The certified survival lemma
  supplies the universal conclusion for every isotropic log-concave law.
- Lines 85–102: at $\eta=1/6$, the conditions
  $|p_t-1/2|>\eta$ and $p_t\notin[1/3,2/3]$ are identical. Thus the
  stopping times agree exactly, with no substitution of a boundary-hitting
  convention. The corollary allows this endpoint, and $p_0=1/2$ satisfies
  its nested initial condition. Applying the assumption to each deterministic
  $I=[0,T]$ supplies its entire prefix premise with the same universal
  constants. No additional random stop is inserted. The certified corollary
  and survival lemma have exactly the required conclusion.
- Lines 105–116: dependencies and retained antecedents match the ledger.
  Every `depends_on` is certified; neither implication depends on an open
  node. The open assumptions affect applicability, not the implications' truth.

The hypotheses used are isotropic log-concavity in arbitrary finite dimension,
a fixed measurable half-mass cut, the manuscript's localization, positive
universal horizon, finite universal constants, and the respective antecedent.
For Carleson, $C_0,C_1\ge0$ and $\alpha<1$ match the certified corollary.
There is no hidden smooth-boundary or compact-support requirement in this
application of the certified statements. The centroid antecedent's larger
initial range and the Carleson antecedent's non-prefix intervals are stronger
than this dossier needs; that is no defect.

Neither target has a `bounded_by` edge. The brief's P2 is respected: neither
antecedent is discharged and no route or unconditional KLS claim closes.
P1 is respected: there is no asserted equivalence among trace-upgrade routes.
The profile-circularity and equivalent-strength traps are avoided by using
the certified survival implication with the explicit conditional input.
No spectral bootstrap, slice-wise source bound, spectator-sensitive estimate,
projection test, or numerical evidence enters the proof. The other geometric
and sharp-constant fences in the brief have no operative step here.

**Corrections.** None required. There are no unchecked steps within the stated
scope. The dossier imports no external preprint or uncatalogued result;
certified nodes are relied on as stated, as authorized. No unavailable source
prevents this review.

**Validation.** `UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py` first
failed at MyST startup in the sandbox. The identical command succeeded with
tool escalation, exit 0, without changing the checks or environment versions;
there were no MyST or certification errors. Audited input hashes were rechecked
before fingerprinting and were unchanged. The front-matter fingerprint block
is the exact successful output of
`UV_CACHE_DIR=/tmp/kls-uv-cache uv run scripts/check.py --fingerprint solutions/thm-centroid-implies-kls.md`,
also run with escalation, immediately before recording this verdict.

**Exclusions.** This does not re-review the existing tight-window or survival
proofs, certify either antecedent, or prove unconditional KLS. The checkpoint's
observation about the existing tight-window proof is not used as evidence;
reliance here is on its certified statement. This report does not review
`solutions/thm-intro-weighted.md`, the Letwin imports, or the separate
Carleson-to-centroid dossier.

```yaml
files:
  - research/reviews/2026-10-01-conditional-bridges-review.md
deltas:
  - path: research/program/ledger.yaml
    id: thm:centroid-implies-kls
    status: proved
    depends_on: [lem:survival-implies-kls]
    assumes: [ass:stopped-centroid]
    proofs:
      - artifact: solutions/thm-centroid-implies-kls.md
        review: research/reviews/2026-10-01-conditional-bridges-review.md
  - path: research/program/ledger.yaml
    id: thm:intro-all-cut
    status: proved
    depends_on: [cor:tight-window-consumption, lem:survival-implies-kls]
    assumes: [ass:all-cut-carleson]
    proofs:
      - artifact: solutions/thm-centroid-implies-kls.md
        review: research/reviews/2026-10-01-conditional-bridges-review.md
```
