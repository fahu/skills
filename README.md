# Codex skills

From another project, install **all skills in this repository** from `main`:

```sh
npx --yes --package=github:fahu/skills#main fahu-skills install
```

This installs all **61 skills** locally in `.agents/skills/`:

| Package | Included skills |
| --- | --- |
| `commits` | Atomic commits and conventional commit messages |
| `github-pr-management` | Review feedback, fixes, and reviewer replies |
| `pstack` | 59 prefixed entrypoints, including `$pstack` and `$pstack-how` |

Requires Node.js 22 or newer, npm, and Git. Replace `main` with a reviewed full
commit SHA for a reproducible install. The package is consumed directly from
GitHub; it is not published to the npm registry. npm supports GitHub dependency
references and commit pins
([package specs](https://docs.npmjs.com/cli/v11/using-npm/package-spec/)).

## Install individual packages

Use `--only` to select any package:

```sh
npx --yes --package=github:fahu/skills#main fahu-skills install --only commits
npx --yes --package=github:fahu/skills#main fahu-skills install --only github-pr-management
npx --yes --package=github:fahu/skills#main fahu-skills install --only pstack
```

Append `--target /path/to/project` to install into a different existing project.

For a saved development dependency instead:

```sh
npm install --save-dev github:fahu/skills#main
npx fahu-skills install
```

Installing the dependency alone does not modify the project’s skills.
Run the installer explicitly. There are no install hooks or runtime package
dependencies. The package is marked private to prevent accidental registry
publication.

## Installed files

Installation creates:

```text
.agents/
  pstack/                 Complete pinned bundle and Codex adapter
  skills/
    pstack/               Help entrypoint
    pstack-how/           Read-only investigation entrypoint
    pstack-.../           Other prefixed pstack entrypoints
    commits/
    github-pr-management/
```

Skill folders are regular copies, with references adjusted to the shared
bundle. They continue to work after removing the npm dependency or clearing
npm’s cache. Commit the installed `.agents/` content to share it with your
team. Codex discovers skills there; select `$pstack` or `$pstack-how` after
the skills refresh. Most upstream workflows retain explicit-only invocation.

The installer checks the pinned upstream hashes before writing. It restores
the upstream `.gitignore` from a bundled fallback because npm omits that
filename from tarballs. It rejects existing conflicting content and symlinked
destination directories before installation. An identical repeat is a no-op.
It never changes `AGENTS.md` or another skill. To upgrade a customized bundle,
review and back up those changes before removing the specific conflicting
installation paths and rerunning; there is no force-overwrite option.

## Why the installer exists

[`bin/fahu-skills.mjs`](bin/fahu-skills.mjs) implements the npm command.
Downloading an npm package alone does not register its contained Codex skills.
The CLI copies every selected skill into `.agents/skills/`, preserves pstack's
shared supporting files, and adjusts the entrypoint references to those files.
It also checks upstream integrity and protects existing project content.

## Verify this repository

The checkout uses relative `.agents/skills/` symlinks to the canonical pstack
entrypoints. npm packages exclude those symlinks; the CLI creates portable
skill copies in destination projects instead.

```sh
python3 pstack/scripts/verify.py
```

For a manual npm smoke check, pack the repository with `npm pack`, then use
`npm exec --yes --package=/absolute/path/to/the.tgz -- fahu-skills install`
from a temporary project. The CLI is verified locally on macOS; Windows
execution has not been verified.

See [pstack’s source pin and tool mapping](pstack/README.md),
[unsupported features](pstack/codex.md), and
[installation checks](pstack/SMOKE-TEST.md).

## Licenses

pstack’s [MIT license](pstack/upstream/LICENSE) and the commits skill’s
[Apache-2.0 license](commits/LICENSE) are preserved with their respective
files. Importing a skill does not change its license or project instructions.
