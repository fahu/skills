# Fahu agent skills

Codex skills with pinned pstack, Cloudflare, and Matt Pocock imports.

## Install skills

Run this from the destination project:

```sh
npx skills@1.7.4 add fahu/skills --skill '*' --agent codex
```

To select skills, replace `'*'` with their names. Include `pstack` with any `pstack-*` skill.

Matt Pocock's workflows call other skills in his collection. Install the full collection when you use those workflows.

## Configure a project

For Matt Pocock workflows such as `to-spec` and `triage`, configure each project once. In the destination project's Codex chat, invoke:

```text
$setup-matt-pocock-skills
```

The skill configures the issue tracker, triage labels, and domain documentation. Commit `docs/agents/*.md` and the updated `AGENTS.md` or `CLAUDE.md`.

Keep this interactive setup separate from automated skill restoration. See [the setup skill](skills/setup-matt-pocock-skills/SKILL.md) for configuration details.

## Maintain the collection

Run these commands from this repository:

```sh
npm run skills:build
npm run check
```

The build regenerates pstack exports. The checks verify pstack, Matt Pocock's imported files, and Cloudflare's validators.

To update Matt Pocock's import, use a local upstream checkout and a reviewed full commit SHA. Replace the checkout path and SHA:

```sh
python3 scripts/mattpocock.py --import-from /path/to/mattpocock-skills --revision FULL_COMMIT_SHA
npm run check
```

Review the imported files and [the import manifest](imports/mattpocock.lock.json), then commit them together. If the skill selection changes, update the links in `.agents/skills/`.
