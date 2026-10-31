# Installation verification

Verified locally on 2026-10-31 against the pin in
[`upstream.lock.json`](upstream.lock.json).

## Results

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

## Read-only investigation

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

## Limits

This verifies packaging, discovery, preservation, and one investigation path.
It does not certify every workflow, formal-verification tool, PR watcher,
video renderer, cloud integration, or automation. Upstream dependencies were
not installed or executed. The investigation encountered a denied incidental
mise cache write outside the workspace; it did not affect its reads or the
verified workspace contents.

Unsupported and conditional capabilities are documented in
[`codex.md`](codex.md). The initial installation created no PR, commit,
schedule, external message, or global skill installation.

## npm distribution and pre-PR review

At PR creation, npm package verification used the actual packed tarball with
`npm install` and `npm exec`. All six installer tests passed. They covered
complete upstream hashes and entrypoint references, existing project files,
paths with spaces, idempotent repeats, conflicts, destination symlinks,
group selection, and corrupted package contents.

The tarball omits upstream `.gitignore` under npm's packaging rules. The CLI
restores it from `bin/npm-files.json` and checks it against the pinned hash
before any target writes. All 573 upstream files are present after import.
No upstream package dependencies or install hooks are run.

A fresh consumer project received all 61 skills. After clearing the temporary
npm cache, its imported integrity verifier passed and Codex CLI 0.164.0
`skills/list` discovered all 59 pstack entrypoints plus both existing skills
as enabled repository skills, with no load errors or raw upstream exposure.

Before opening the PR, the added `pstack-interrogate` workflow ran two
independent adversarial passes. Both ran the tests and additional CLI probes
and reported no verified findings; zero findings were dropped. Both inherited
the parent model, so no model-diversity evidence is claimed. The
`pstack-blast-radius` review's key invariant was that conflicts and corrupt
payloads fail before project writes; executable tests confirmed it.
`pstack-no-comments` suggested deleting one redundant verifier docstring,
which was accepted. No upstream comments or files were changed. Windows
execution and a published npm registry package were not verified.

## Review feedback follow-up

The authored installer test suite and `npm test` script were removed in
response to review feedback. The earlier test results above are historical;
the preserved upstream fixtures and the integrity utility remain unchanged.
The root README now starts with installation of all three packages from
`main`, documents each package selector, and explains the npm CLI's purpose.
Manual packed-tarball smoke checks confirmed the default 61-skill import and
individual imports for `commits` (1), `github-pr-management` (1), and `pstack`
(59), while preserving the destination's `AGENTS.md`. Repeat installation and
the imported integrity utility also passed.
