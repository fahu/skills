---
name: pstack-setup-pstack
description: "pstack: Configure explicitly requested local pstack role choices for Codex; roles inherit the session model by default. Preserve project instructions and global configuration."
license: MIT
---

# pstack · setup-pstack

This is a Codex adaptation of Lauren Tan’s **pstack**, pinned in
[upstream.lock.json](../../upstream.lock.json).

1. Read [the Codex adapter](../../codex.md) before following upstream material.
   It replaces incompatible tool, model, autonomy, and path instructions.
   Applicable project instructions and the user’s request take precedence.
2. Read [the upstream workflow](../../upstream/skills/setup-pstack/SKILL.md)
   and apply it through that adapter. Load supporting files only as needed.
3. Route cross-skill calls through the prefixed entrypoints in `../`.
   Resolve other relative references beside the original upstream file.
   Report missing required capabilities; do not claim skipped checks passed.

Follow only the adapter’s **Setup** replacement; do not execute the upstream Cursor setup steps. The upstream file is retained for reference.
