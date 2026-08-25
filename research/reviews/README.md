# Independent proof reviews

This directory stores the scope and verdict of reviews used by `checked_by: agent` ledger
promotions. A valid report names the proof author and a distinct reviewer, enumerates every
covered ledger node, records exclusions or corrections, and points to the standalone solution
dossier that was reviewed.

For mechanical validation, the opening metadata must contain the exact Markdown field
`- **Verdict:** pass ...`, must name every certified node id, and must name the reviewer exactly
as recorded by the node's `reviewed_by:` field. Qualifiers after `pass` must not weaken the
verdict for a listed node. A report headed `partial pass`, `hold`, or any other verdict cannot
certify a ledger promotion; after repairs, write a new follow-up report rather than changing the
historical verdict.

Review reports are proof provenance, not numerical evidence. A partial or caveated audit may be
kept here, but only claims receiving an unqualified pass may be promoted to `status: proved`.
