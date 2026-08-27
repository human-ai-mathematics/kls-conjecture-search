# Increase Codex agent concurrency

- **Date:** 2026-08-27
- **Type:** harness configuration
- **Scope:** `.codex/config.toml`, `.gitignore`
- **Mathematical effect:** none

## Problem

Codex used its runtime-selected default for subagent concurrency because the repository did not
declare an `[agents]` limit. The observed session capacity was too small for research workflows
that intentionally split independent, role-scoped work across several agents.

## Decision

Set `agents.max_concurrent_threads_per_session = 16` in the trusted project configuration. This
caps concurrently open spawned-agent threads at 16; the primary agent thread is not counted.
Add a narrow `.gitignore` exception for `.codex/config.toml` while continuing to ignore other
Codex local state outside the already tracked project role definitions.

This changes capacity only. The root contract continues to govern when parallel work is allowed,
including the prohibition on fan-out across the trace-upgrade cluster and the single-orchestrator
rule for ledger writes.

## Migration boundary

The setting applies when Codex next loads the trusted project configuration. Existing sessions
keep their current runtime limit. No agent definitions, mathematical records, or historical
research artifacts are migrated.

## Compatibility impact

The configuration uses the current Codex key rather than the legacy `agents.max_threads` alias.
Codex clients that do not recognize project-scoped multi-agent settings may ignore it; repository
content and validation remain unaffected.

## Validation

- Parse `.codex/config.toml` with Python's `tomllib` and confirm the configured value is 16.
- Confirm Git no longer ignores `.codex/config.toml`.
- Run `git diff --check`.
