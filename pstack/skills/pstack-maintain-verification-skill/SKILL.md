---
name: pstack-maintain-verification-skill
description: "pstack: Periodic pass that keeps a project's verification skill and feature map honest: parallel source readers per feature, one live session driving every feature, at most one PR of proven corrections. Use for $pstack-maintain-verification-skill or \"audit the verify skill\"."
license: MIT
---

# pstack · maintain-verification-skill

This is a Codex adaptation of Lauren Tan’s **pstack**, pinned in
[upstream.lock.json](../../upstream.lock.json).

1. Read [the Codex adapter](../../codex.md) before following upstream material.
   It replaces incompatible tool, model, autonomy, and path instructions.
   Applicable project instructions and the user’s request take precedence.
2. Read [the upstream workflow](../../upstream/skills/maintain-verification-skill/SKILL.md)
   and apply it through that adapter. Load supporting files only as needed.
3. Route cross-skill calls through the prefixed entrypoints in `../`.
   Resolve other relative references beside the original upstream file.
   Report missing required capabilities; do not claim skipped checks passed.
