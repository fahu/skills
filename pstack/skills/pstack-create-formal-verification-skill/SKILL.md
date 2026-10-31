---
name: pstack-create-formal-verification-skill
description: "pstack: Generate a project-local skill that formally verifies the code where a bug costs the most and tests reach the least, in any language, with whichever verification tool fits. Use for $pstack-create-formal-verification-skill, \"model-check this race\", \"prove this invariant\", or when concurrency, retries, state machines, parsers, or unsafe code need more than tests."
license: MIT
---

# pstack · create-formal-verification-skill

This is a Codex adaptation of Lauren Tan’s **pstack**, pinned in
[upstream.lock.json](../../upstream.lock.json).

1. Read [the Codex adapter](../../codex.md) before following upstream material.
   It replaces incompatible tool, model, autonomy, and path instructions.
   Applicable project instructions and the user’s request take precedence.
2. Read [the upstream workflow](../../upstream/skills/create-formal-verification-skill/SKILL.md)
   and apply it through that adapter. Load supporting files only as needed.
3. Route cross-skill calls through the prefixed entrypoints in `../`.
   Resolve other relative references beside the original upstream file.
   Report missing required capabilities; do not claim skipped checks passed.
