# The KLS theorem and its methods

**[Read the manuscript](https://human-ai-mathematics.github.io/kls-conjecture-search/)**:
the site opens on a short welcome page with reading paths ([`modules/index.md`](modules/index.md));
the mathematical introduction is [`modules/00-overview.md`](modules/00-overview.md).

The Kannan–Lovász–Simonovits conjecture — the dimension-free Poincaré bound
$C_P \le K\lambda_{\max}(\mathrm{Cov})$ for every log-concave measure — was proved twice on
4 October 2026: by Song–Zhang, in the
[second version](https://arxiv.org/abs/2610.01447v2) of a preprint whose
[first version](https://arxiv.org/abs/2610.01447v1) gave an iterated-logarithm bound, and by
Bizeul–Klartag–Lehec ([arXiv:2610.05474v1](https://arxiv.org/abs/2610.05474v1)). This
repository is a MyST manuscript that reconstructs, checks and compares the two proofs, surveys
the methods that led to them, and develops four approaches whose questions remain open after
KLS (a deterministic moment-map inequality, fixed-eigenfunction and fixed-cut stochastic
localization, conditional-fiber frames). It also holds the record of the **sustained
conjecture search** that produced it. Proofs here are checked by independent agent reviews,
which is distinct from journal refereeing; the ledger, not this file, is the source of truth
for what has been certified.

The rules are in [`SPECIFICATION.md`](SPECIFICATION.md), from
[conjecture-search-template v0.5.0](https://github.com/human-ai-mathematics/conjecture-search-template/releases/tag/v0.5.0).
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
| [`.claude/agents/`](.claude/agents/), [`.codex/agents/`](.codex/agents/) | the three roles: `researcher`, `reviewer` and `writer`, for Claude Code and for Codex |
| [`templates/`](templates/) | an empty copy of each file genre |
| [`HISTORY.md`](HISTORY.md) | the milestones of the search, newest first |
| [`example/`](example/README.md) | the template's worked search, kept green as a fixture |

The milestones of the search — results certified, refutations, approaches opened or
closed, migrations of the harness — are in [`HISTORY.md`](HISTORY.md), newest first.

## Setup and verify

Needs [uv](https://docs.astral.sh/uv/), which provisions Python and PyYAML from
`pyproject.toml`, and Node.js 18+ for MyST (pinned in `package.json`):

```bash
npm ci
./scripts/check.sh               # the checker, the worked example, the unit tests
uv run scripts/check.py         # full check; 0 errors required before any status change
uv run scripts/check.py --fast  # research state only, no MyST build
uv run scripts/check.py --impact # compact scope for grouped re-reviews; same validation
uv run scripts/check.py --diff   # the same, with each change's diff for an editorial note
uv run scripts/check.py --statements   # before and after a writer's pass: must not change
uv run scripts/check.py --drafts       # the draft dossiers, never published
npx myst start                   # read the manuscript and the proofs in a browser
```

Agents run the checker and MyST many times per session. Approve those commands once and
for good (`uv run scripts/check.py` and `node_modules/.bin/myst`): in Claude Code, as
`allow` rules in `.claude/settings.json`; in Codex, by accepting the prefix rule offered
on the first escalation. Each approval asked again costs a turn, and in Codex a call to
its reviewing model. See *Running agents* below for practical guidance; the independence
requirement is in *Review* in `SPECIFICATION.md`.

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

## Running agents

Prefer the client's agent tools so assignments, results and progress remain visible.
Load the corresponding instructions from `.claude/agents/` or `.codex/agents/` for each
role. In Claude Code, use the Agent tool's role selection when available. In Codex,
use `spawn_agent` with `fork_turns: "none"` for an independent reviewer and ensure its
assignment loads the reviewer instructions; use the role-selection mechanism your client
actually exposes rather than assuming an `agent_type` argument exists.

A reviewer must not inherit the conversation that authored or directed the proof. Check
that the chosen launch mechanism supplies that fresh context. Other agents can receive
context useful to their tasks. Prefer these managed tools over background shell sessions.

Use completion notifications or blocking waits (such as `wait_agent`) rather than repeated
status polling. Choose a timeout within the client's limits that still allows progress
updates and responses to the user; no fixed wait duration is part of the repository
contract. Start a new session when it helps keep context focused, not automatically after
each task. The recommended scientific workflow is in *Workflow* in `SPECIFICATION.md`.

At the end of a wave or a session that changed the picture (a result certified or
withdrawn, a refutation, an approach opened or closed, a preprint integrated, a
restructuring, a migration), the orchestrator adds a dated entry at the top of
[`HISTORY.md`](HISTORY.md): a few lines in plain prose, statements named by label, the
checkpoint holding the detail. Past entries are never rewritten, and the ledger stays the
source of truth for statuses.

## Licence

The text (manuscript, proofs and research records) is under
[CC BY 4.0](LICENSE-CC-BY-4.0.txt), the code under MIT; [`LICENSE`](LICENSE) says which is which.
