---
name: pstack-principle-boundary-discipline
description: "pstack: Apply when wiring validation, error handling, or framework adapters. Concentrate guards at system boundaries (CLI, config, network, external APIs); trust internal types and keep business logic in pure functions."
license: MIT
---

# pstack · principle-boundary-discipline

This is a Codex adaptation of Lauren Tan’s **pstack**, pinned in
[upstream.lock.json](../../upstream.lock.json).

1. Read [the Codex adapter](../../codex.md) before following upstream material.
   It replaces incompatible tool, model, autonomy, and path instructions.
   Applicable project instructions and the user’s request take precedence.
2. Read [the upstream workflow](../../upstream/skills/principle-boundary-discipline/SKILL.md)
   and apply it through that adapter. Load supporting files only as needed.
3. Route cross-skill calls through the prefixed entrypoints in `../`.
   Resolve other relative references beside the original upstream file.
   Report missing required capabilities; do not claim skipped checks passed.
