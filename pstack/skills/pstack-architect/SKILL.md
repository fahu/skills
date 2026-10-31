---
name: pstack-architect
description: "pstack: Sketch types, signatures, and module structure before code, then stay in the loop while implementation fills in. Use for $pstack-architect, 'architect this', 'design this', or non-trivial work where jumping to code would lock in the wrong shape."
license: MIT
---

# pstack · architect

This is a Codex adaptation of Lauren Tan’s **pstack**, pinned in
[upstream.lock.json](../../upstream.lock.json).

1. Read [the Codex adapter](../../codex.md) before following upstream material.
   It replaces incompatible tool, model, autonomy, and path instructions.
   Applicable project instructions and the user’s request take precedence.
2. Read [the upstream workflow](../../upstream/skills/architect/SKILL.md)
   and apply it through that adapter. Load supporting files only as needed.
3. Route cross-skill calls through the prefixed entrypoints in `../`.
   Resolve other relative references beside the original upstream file.
   Report missing required capabilities; do not claim skipped checks passed.
