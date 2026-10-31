---
name: pstack-principle-attack-the-premise
description: "pstack: Apply when two or more fixes that share one premise have failed the same gate. Write the premise down and test it directly before you write another fix that assumes it."
license: MIT
---

# pstack · principle-attack-the-premise

This is a Codex adaptation of Lauren Tan’s **pstack**, pinned in
[upstream.lock.json](../../upstream.lock.json).

1. Read [the Codex adapter](../../codex.md) before following upstream material.
   It replaces incompatible tool, model, autonomy, and path instructions.
   Applicable project instructions and the user’s request take precedence.
2. Read [the upstream workflow](../../upstream/skills/principle-attack-the-premise/SKILL.md)
   and apply it through that adapter. Load supporting files only as needed.
3. Route cross-skill calls through the prefixed entrypoints in `../`.
   Resolve other relative references beside the original upstream file.
   Report missing required capabilities; do not claim skipped checks passed.
