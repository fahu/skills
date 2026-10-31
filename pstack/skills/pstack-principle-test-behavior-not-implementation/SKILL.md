---
name: pstack-principle-test-behavior-not-implementation
description: "pstack: Apply when you write, change, or keep a test. Assert what the code's users can observe, so that the test fails when that behavior breaks and keeps passing when only the internals change."
license: MIT
---

# pstack · principle-test-behavior-not-implementation

This is a Codex adaptation of Lauren Tan’s **pstack**, pinned in
[upstream.lock.json](../../upstream.lock.json).

1. Read [the Codex adapter](../../codex.md) before following upstream material.
   It replaces incompatible tool, model, autonomy, and path instructions.
   Applicable project instructions and the user’s request take precedence.
2. Read [the upstream workflow](../../upstream/skills/principle-test-behavior-not-implementation/SKILL.md)
   and apply it through that adapter. Load supporting files only as needed.
3. Route cross-skill calls through the prefixed entrypoints in `../`.
   Resolve other relative references beside the original upstream file.
   Report missing required capabilities; do not claim skipped checks passed.
