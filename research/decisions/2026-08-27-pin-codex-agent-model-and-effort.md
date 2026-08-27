# Pin Codex agent model and reasoning effort by role

- **Date:** 2026-08-27
- **Type:** agent harness and validation
- **Scope:** `.codex/agents/`, `research/check_agents.py`, `research/tests/test_check_agents.py`
- **Mathematical effect:** none

## Problem

The generated Codex adapters inherited their model and reasoning effort from the parent session.
That made the same repository role run with different capabilities depending on how the main
session was launched. It also left the proof-producing and proof-challenging roles without an
explicit quality-first reasoning policy.

The official
[Codex subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents#choosing-models-and-reasoning)
allows custom agent files to set both `model` and `model_reasoning_effort`, and identifies `high`
for complex logic and `ultra` for the deepest reasoning on a supported model. The official
[GPT-5.6 Sol model documentation](https://developers.openai.com/api/docs/models/gpt-5.6-sol)
identifies `gpt-5.6-sol` as the frontier GPT-5.6 model for complex professional work.

## Decision

Every generated Codex adapter pins `model = "gpt-5.6-sol"`. The baseline reasoning effort is
`high`.

The following mathematical roles use `model_reasoning_effort = "ultra"` because their primary
work is to construct, attack, compare, or certify mathematical arguments:

- `prover`;
- `proof-checker`;
- `refiner`;
- `refutation-seeker`;
- `proof-miner`;
- `kls-route-prober`;
- `kls-route-scout`; and
- `synthesizer`.

The remaining roles use `model_reasoning_effort = "high"`: `scout`, `finum`,
`literature-scout`, `latex-sync`, and `janitor`.

The policy lives in `research/check_agents.py`, at the Codex adapter boundary. Canonical Claude
role frontmatter remains client-neutral and rejects both `model` and `model_reasoning_effort`.
Generated `.codex/agents/*.toml` files remain non-authoritative and must not be hand-edited.

## Migration boundary

This decision supersedes only the model-inheritance sentence in
`2026-08-26-cross-client-agent-execution-contract.md`. It does not change the canonical role
definitions, roster, permissions, write surfaces, concurrency keys, or handoff protocol.

All thirteen existing Codex adapters are regenerated in place with the pinned model and their
role-classified effort. No agent is added or removed.

## Compatibility

Claude role execution is unchanged. Codex sessions must have access to `gpt-5.6-sol` and to the
configured reasoning level. The explicit policy increases expected latency and token use relative
to inherited lower-effort sessions; that is accepted for this quality-first research harness.

No ledger, manuscript statement, proof dossier, review, numerical artifact, claim status, or
mathematical dependency changes.

## Validation

```bash
python3 research/check_agents.py --write-codex
python3 research/check_agents.py
python3 -m unittest discover -s research/tests -p 'test_*.py'
python3 research/check_ledger.py
git diff --check
```
