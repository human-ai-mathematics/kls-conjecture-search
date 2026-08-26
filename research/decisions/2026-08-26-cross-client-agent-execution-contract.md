# Make agent roles executable across Claude and Codex

- **Date:** 2026-08-26
- **Type:** agent harness and validation
- **Scope:** `.claude/agents/`, `.codex/agents/`, `research/check_agents.py`
- **Mathematical effect:** none

## Problem

The role taxonomy was precise about mathematical duties but not executable as one shared client
configuration. `.codex/agents` was a symlink to Claude Markdown definitions, while Codex requires
one standalone TOML file per project agent with `name`, `description`, and
`developer_instructions`. The symlink therefore exposed no Codex custom agents. Claude-only
`model: sonnet` fields also contradicted the claim of a shared definition.

The client-format boundary was checked against the official
[Codex subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents)
on 2026-08-26.

The role README described safe fan-out too broadly. Parallel literature scouts could edit the
single `fi_references.bib`; parallel numerical workers could edit shared `finum` registries; and
dated exploration slugs had no collision rule. Several handoffs were prose only. In particular,
the prover proposed a `solution:`-only ledger delta even though the ledger checker requires
`solution` and `checked_by` atomically, and a failed proof review had no typed route back to the
prover.

## Decision

1. `.claude/agents/*.md` is the canonical role source. Claude reads it directly.
2. `.codex/agents/*.toml` contains generated project-scoped adapters. Each adapter copies the
   canonical name, description, and instruction body and sets `sandbox_mode` to `read-only` for
   `scout`, `janitor`, and `latex-sync`, or `workspace-write` for roles with declared artifacts.
   Model selection is inherited from the parent rather than embedded in the canonical source.
3. `research/check_agents.py --write-codex` generates the adapters;
   `python3 research/check_agents.py` rejects missing roles, stale or hand-edited adapters,
   mismatched names, write tools on read-only roles, and roster omissions.
4. The orchestrator remains the only owner of ledgers, bibliography, route-control files, and
   accepted manuscript changes. `literature-scout` and `latex-sync` now return exact patches
   rather than editing those single-file merge points.
5. Concurrency keys distinguish safe fan-out from shared writes. `finum-code`, `knowledge`,
   bibliography, manuscript, route control, and ledger work are single-owner. Stable numerical
   runs may fan out only on distinct target/profile/seed keys. Exploration paths are create-only
   and include a role, scope, and run-specific suffix.
6. Every role ends with a shared typed handoff envelope: `outcome`, `artifacts`,
   `proposed_deltas`, `next_role`, and a verbatim `next_prompt`. Prose words such as “done” do not
   control transitions.
7. The proof loop is atomic and cold-reviewed. A prover supplies no applicable ledger delta;
   only a passing independent proof review proposes `solution`, `checked_by`, `review`, and
   status together. A failed review returns exhaustive repair instructions verbatim to the
   prover. When supported by the runtime, the reviewer starts without the author's conversation
   history.
8. Exact refutations use the existing roles rather than a new one: `refutation-seeker` proposes
   the witness, `prover` proves a refuter node, `proof-checker` certifies it, and the orchestrator
   applies `refuted_by` provenance.

The earlier decision `2026-08-26-agent-role-definitions.md` remains immutable history. This record
supersedes only its cross-client symlink claim and sharpens its parallelism and handoff contracts.

## Compatibility

The mathematical role roster stays at thirteen. No ledger, schema, claim status, manuscript
statement, proof dossier, review, numerical artifact, or exploration is changed. Existing Claude
role names remain stable. Codex now discovers the same names through its native TOML format.

Local client state remains ignored, while `.claude/agents/**` and `.codex/agents/**` are explicit
tracked exceptions in `.gitignore`.

## Validation

```bash
python3 research/check_agents.py
python3 research/check_ledger.py
python3 -m unittest discover -s research/tests -p 'test_*.py'
git diff --check
```
