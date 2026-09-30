# The Kannan–Lovász–Simonovits frontier

A MyST manuscript on routes toward the Kannan–Lovász–Simonovits conjecture — the
dimension-free Poincaré bound $C_P \le K\lambda_{\max}(\mathrm{Cov})$ for every isotropic
log-concave measure — together with the harness of a **sustained conjecture search** on it:
what is claimed, what the search is doing, and why. KLS itself is open, and nothing here
proves it; four routes are developed (fixed-cut and fixed-eigenfunction stochastic
localization, a deterministic moment-map programme, conditional-fiber frames), each with its
certified advances and its exact open estimate. The ledger, not this file, is the source of
truth for what is proved.

The rules are in [`SPECIFICATION.md`](SPECIFICATION.md), from
[conjecture-search-template v0.4.0](https://github.com/numina-functional-inequalities/conjecture-search-template/releases/tag/v0.4.0).
Start every session that edits the repository by reading it.

## Layout

| path | holds |
|---|---|
| [`modules/`](modules/) | the manuscript, the text a reader reads: every claim as a labelled `prf:` directive, in prose written for a mathematician; reading order in [`myst.yml`](myst.yml) |
| [`research/program/`](research/program/) | the ledger, the problem brief (target `conj:kls`) and the portfolio of routes |
| [`research/explorations/`](research/explorations/) | dated checkpoints and candidate statements |
| [`research/reviews/`](research/reviews/) | independent proof reviews |
| [`research/runs/`](research/runs/) | run output (JSONL, provenance on the first line) |
| [`research/lib/`](research/lib/) | the shared numerics package `numerics`, its tests and its instance registry |
| [`solutions/`](solutions/) | standalone proof and refutation dossiers |
| [`.claude/agents/`](.claude/agents/) | the three roles: `researcher`, `reviewer` and `writer` |
| [`templates/`](templates/) | an empty copy of each file genre |
| [`example/`](example/README.md) | the template's worked search, kept green as a fixture |

The repository was migrated from its v0.1 LaTeX harness on 2026-09-29, then to v0.3.0 and
v0.4.0 on 2026-09-30 (v0.4.0 changed nothing in the program's content);
[`research/explorations/2026-09-29-migration-v0.2.0.md`](research/explorations/2026-09-29-migration-v0.2.0.md)
and
[`research/explorations/2026-09-30-migration-v0.3.0.md`](research/explorations/2026-09-30-migration-v0.3.0.md)
say what was converted and how;
[`research/explorations/2026-09-30-sync-after-migration.md`](research/explorations/2026-09-30-sync-after-migration.md)
closes their open items and maps the ids renamed at that point.

## Setup and verify

Needs [uv](https://docs.astral.sh/uv/), which provisions Python and PyYAML from
`pyproject.toml`, and Node.js 18+ for MyST (pinned in `package.json`):

```bash
npm ci
./scripts/check.sh               # the checker, the worked example, the unit tests
uv run scripts/check.py         # full check; 0 errors required before any status change
uv run scripts/check.py --fast  # research state only, no MyST build
uv run scripts/check.py --statements   # before and after a writer's pass: must not change
uv run scripts/check.py --drafts       # the draft dossiers, never published
npx myst start                   # read the manuscript and the proofs in a browser
```

The numerics package has its own environment:

```bash
cd research/lib
uv run pytest                    # the fast lane; `uv run pytest -m slow` for the rest
uv run python -m numerics list   # the run targets
```

A green check establishes structure only; whether a proof is correct is the reviewer's job.
Each statement shows its status, read from the ledger by
[`scripts/status.mjs`](scripts/status.mjs). The `pages` workflow publishes the manuscript
and the certified dossiers to GitHub Pages when dispatched by hand, after a person has
read them.
