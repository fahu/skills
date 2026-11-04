# Installation verification

## Standard CLI distribution, 2026-11-01

Verified the new `skills/` layout with `skills@1.7.4`, Node.js 24.21.0, Python 3, and the installed Codex app server on macOS.

| Check | Result |
| --- | --- |
| Full installation | Both `skills add` and a `package.json` Git source declaration installed all 61 public skills into temporary projects. Existing `AGENTS.md` and an unrelated skill were preserved. No `@fahu/skills` dependency or custom installer was needed. |
| Selected installation | `commits` and `github-pr-management` installed individually. `pstack` installed alone and alongside `pstack-how` using copy mode. The complete shared snapshot and internal workflows remained available in both pstack cases. |
| Git revision and restore | A temporary Git fixture supplied all 61 skills at one explicit commit. After advancing its default branch and deleting installed skills, `skills experimental_install` restored the original revision and preserved the lock, project instructions, and unrelated skill. A subprocess-scoped URL rewrite kept this transport test local. |
| Upstream preservation | All 573 upstream files retain their recorded hashes and executable modes. Both standalone skills retain their original contents after relocation. No relocated or generated file is ignored by Git. |
| Export validation | The integrity utility checked every internal and public entrypoint, local reference target, and invocation policy. It rejected modified upstream content, exported instructions, and exported metadata. Partial installations passed without `--require-all` and failed when all public entrypoints were required. |
| Skill format | The skill-creator validator and YAML parser accepted all 61 public skills and their Codex metadata. PyYAML was installed only in a temporary validation environment. |
| Actual Codex discovery | `skills/list` with `forceReload: true` found exactly 61 enabled repository skills in this checkout and 61 packaged skills plus the existing skill in the full consumer. Partial consumers exposed exactly one and two selected skills. There were no duplicate names, raw upstream skills, Benny skills, or load errors. |
| Hidden support directory | `.bundle/` keeps original upstream `SKILL.md` files and internal entrypoints outside Codex discovery while the standard installer copies them with the main `pstack` skill. |

These checks used temporary consumers and a temporary Git fixture. No GitHub revision was published, no model turn or pstack workflow was executed, and no upstream runtime dependencies were installed. They verify distribution and discovery, not every upstream workflow or Windows execution.

Consumers must select `pstack` alongside individual `pstack-*` entrypoints and keep them on the same reviewed revision. The standard CLI does not resolve this dependency automatically. Public entrypoints report a missing base without fetching or installing anything during a workflow.

The canonical wrappers are in `skills/` relative to this support directory. The repository's export generator produces the public wrappers before commit; consumers install those committed files directly. Run the integrity utility at `.agents/skills/pstack/.bundle/scripts/verify.py` after installation, adding `--require-all` for the complete collection.

## Original verification, 2026-10-31

The following records the original layout before the standard CLI adaptation. Paths in this historical record refer to that layout.

Verified locally on 2026-10-31 against the pin in
[`upstream.lock.json`](upstream.lock.json).

### Results

| Check | Result |
| --- | --- |
| Upstream preservation | All 573 files match the pinned checkout's Git blob hashes. Executable modes match the recorded manifest. No snapshot files are ignored by Git. |
| Existing skills | All five tracked files under `commits/` and `github-pr-management/` match `HEAD`; their directories were not changed. |
| Project constraints | No `AGENTS.md` was present in the project or ancestor directories. None was created or replaced; the adapter explicitly preserves applicable project instructions. |
| Skill format | The bundled Codex skill-creator validator passed for all 59 entrypoints. UI metadata parsed successfully, including default prompts and short descriptions. |
| Invocation policy | All 57 explicit-only upstream skills retain that policy in `agents/openai.yaml`. Upstream setup and the new help entrypoint allow implicit invocation. |
| Integrity utility | `python3 pstack/scripts/verify.py` passed for all 573 source files, 59 entrypoints, local reference targets, policies, and discovery links. |
| Integrity rejection checks | In an isolated temporary copy, the utility rejected modified upstream content, a changed explicit-invocation policy, and a discovery link pointing at raw upstream. |
| Actual discovery | Codex app-server `skills/list` with `forceReload: true` found exactly 59 enabled, repository-scoped pstack entrypoints, no duplicates, and no load errors. No raw upstream or Benny skills were exposed. |
| Read-only investigation | An independent explainer completed the question below through the installed entrypoint. A before/after content-and-symlink comparison across 759 files and links found zero changes. |

The discovery probe used Codex CLI 0.164.0 with an isolated temporary `CODEX_HOME`, initialized a
local stdio app server, then requested:

```json
{
  "id": 2,
  "method": "skills/list",
  "params": {
    "cwds": ["/Users/fahu/dev/fahu/skills"],
    "forceReload": true
  }
}
```

It did not start a model turn, alter global configuration, or require account
credentials. This tests the installed CLI's real loader, rather than only
counting `SKILL.md` files. Desktop selector refresh is checked separately by
the user on the next turn or after a restart if needed.

### Read-only investigation

The independent explainer received the `pstack-how` entrypoint and this question:

> How are pstack skills discovered in this project, and how do they reach
> their implementation without replacing the existing skills or project
> constraints?

It traced the route as:

```text
.agents/skills/pstack-how
  -> pstack/skills/pstack-how/SKILL.md
  -> pstack/codex.md
  -> pstack/upstream/skills/how/SKILL.md
  -> relevant upstream references
```

It read the how explainer template, Investigation playbook, and unslop workflow,
and returned file-and-line evidence. It confirmed that cross-skill calls return
through the prefixed wrappers, supporting paths stay relative to upstream
files, and project instructions and existing skills take precedence. It used
local reads only. No package install, upstream script, Git fetch, external
service, source edit, or further delegation occurred during that investigation.

The independent explainer did not run the discovery API or integrity utility;
the installing agent ran those separately. It inherited the parent model,
so this is an independent pass, not evidence from a different model family.

### Limits

This verifies packaging, discovery, preservation, and one investigation path.
It does not certify every workflow, formal-verification tool, PR watcher,
video renderer, cloud integration, or automation. Upstream dependencies were
not installed or executed. The investigation encountered a denied incidental
mise cache write outside the workspace; it did not affect its reads or the
verified workspace contents.

Unsupported and conditional capabilities are documented in
[`codex.md`](codex.md). The initial installation created no PR, commit,
schedule, external message, or global skill installation.
