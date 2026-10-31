---
name: pstack-principle-encode-lessons-in-structure
description: "pstack: Apply when you catch yourself writing the same instruction a second time, or notice a recurring correction. Encode the rule as a lint, metadata flag, runtime check, or script instead of more text."
license: MIT
---

# pstack · principle-encode-lessons-in-structure

This is a Codex adaptation of Lauren Tan’s **pstack**, pinned in
[upstream.lock.json](../../upstream.lock.json).

1. Read [the Codex adapter](../../codex.md) before following upstream material.
   It replaces incompatible tool, model, autonomy, and path instructions.
   Applicable project instructions and the user’s request take precedence.
2. Read [the upstream workflow](../../upstream/skills/principle-encode-lessons-in-structure/SKILL.md)
   and apply it through that adapter. Load supporting files only as needed.
3. Route cross-skill calls through the prefixed entrypoints in `../`.
   Resolve other relative references beside the original upstream file.
   Report missing required capabilities; do not claim skipped checks passed.
