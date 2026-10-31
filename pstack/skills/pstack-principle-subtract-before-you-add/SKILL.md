---
name: pstack-principle-subtract-before-you-add
description: "pstack: Apply when sequencing an addition, refactor, or rewrite. Remove dead code, redundant validators, and stub references first, then build on the simpler base."
license: MIT
---

# pstack · principle-subtract-before-you-add

This is a Codex adaptation of Lauren Tan’s **pstack**, pinned in
[upstream.lock.json](../../upstream.lock.json).

1. Read [the Codex adapter](../../codex.md) before following upstream material.
   It replaces incompatible tool, model, autonomy, and path instructions.
   Applicable project instructions and the user’s request take precedence.
2. Read [the upstream workflow](../../upstream/skills/principle-subtract-before-you-add/SKILL.md)
   and apply it through that adapter. Load supporting files only as needed.
3. Route cross-skill calls through the prefixed entrypoints in `../`.
   Resolve other relative references beside the original upstream file.
   Report missing required capabilities; do not claim skipped checks passed.
