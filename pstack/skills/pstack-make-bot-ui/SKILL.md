---
name: pstack-make-bot-ui
description: "pstack: Explain pstack bot UI requirements and the unsupported Cursor webhook flow; assess a portable alternative only when requested."
license: MIT
---

# pstack · make-bot-ui

This is a Codex adaptation of Lauren Tan’s **pstack**, pinned in
[upstream.lock.json](../../upstream.lock.json).

1. Read [the Codex adapter](../../codex.md) before following upstream material.
   It replaces incompatible tool, model, autonomy, and path instructions.
   Applicable project instructions and the user’s request take precedence.
2. Read [the upstream workflow](../../upstream/skills/make-bot-ui/SKILL.md)
   and apply it through that adapter. Load supporting files only as needed.
3. Route cross-skill calls through the prefixed entrypoints in `../`.
   Resolve other relative references beside the original upstream file.
   Report missing required capabilities; do not claim skipped checks passed.

Follow the adapter’s unsupported-feature handling for **make-bot-ui**. Stop before the upstream webhook, secret-card, Tailscale, or server-exposure steps.
