---
name: pstack-ketchup-video
description: "pstack: Catch the user up like $pstack-ketchup, with a short subtitled video of slides for what happened and the waiting calls as text under it. Use for $pstack-ketchup-video."
license: MIT
---

# pstack · ketchup-video

This is a Codex adaptation of Lauren Tan’s **pstack**, pinned in
[upstream.lock.json](../../upstream.lock.json).

1. Read [the Codex adapter](../../codex.md) before following upstream material.
   It replaces incompatible tool, model, autonomy, and path instructions.
   Applicable project instructions and the user’s request take precedence.
2. Read [the upstream workflow](../../upstream/skills/ketchup-video/SKILL.md)
   and apply it through that adapter. Load supporting files only as needed.
3. Route cross-skill calls through the prefixed entrypoints in `../`.
   Resolve other relative references beside the original upstream file.
   Report missing required capabilities; do not claim skipped checks passed.
