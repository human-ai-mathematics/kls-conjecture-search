# Instructions for agents in this program

The rules are in [`SPECIFICATION.md`](SPECIFICATION.md), and the roles in
[`.claude/agents/`](.claude/agents/) and [`.codex/agents/`](.codex/agents/). Both come from
the template: propose changes to them there. This file adds what is specific to the KLS
program.

## Orchestrator: keep `HISTORY.md`

[`HISTORY.md`](HISTORY.md) records the milestones of the search, newest first. It is the
entry point for collaborators who join later.

**When to add an entry.** At the end of a wave or of a session that changed the picture:

- a result certified, or a certification withdrawn or repaired;
- a statement refuted;
- an approach opened, closed or reprioritised;
- an outside preprint integrated;
- a restructuring of the manuscript;
- a migration of the harness.

Routine sessions, repairs that change nothing a reader sees, and single runs get no entry.

**How to write it.**

- Add a dated `##` section at the top, or extend today's.
- Use one bullet per milestone, a few lines each, in prose a mathematician can read.
- Name statements by label, never by module file name.
- End with the checkpoint(s) holding the detail, as paths.
- Say *certified* only after a passing independent review, and name a human reviewer when
  there is one.

**What not to do.**

- Do not rewrite past entries. If a later milestone corrects an earlier one, say so in the
  new entry.
- The ledger stays the source of truth for statuses; `HISTORY.md` never decides one.
