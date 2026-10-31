# pstack for Codex

A project-local adaptation of [Lauren Tan’s pstack](https://github.com/cursor/plugins/tree/4dd1d05818d19792e7cd6e818f1667f95f7e1dbe/pstack), version **0.15.36**.
The MIT license and all 573 upstream files are preserved unchanged in
[`upstream/`](upstream/), including scripts, fixtures, assets, guides,
agent prompts, and the dormant Benny automation pack.

## Use it

- `$pstack` opens help and selects a workflow.
- `$pstack-poteto-mode` applies pstack’s broader engineering workflow to the current task.
- `$pstack-how How are skills organized in this repository?` starts a read-only code investigation.
- `$pstack-why Why was this design chosen?` investigates rationale with available sources.
- `$pstack-setup-pstack` explains or customizes Codex role choices. All roles inherit the current session by default.

Every imported command uses the **pstack-** prefix. No `p` shell alias or Cursor
slash command is installed. In Codex, select a skill or mention its `$name`.
The entrypoints are exposed through project-local `.agents/skills/` symlinks,
which Codex supports. They will be available on the next turn; restart Codex
if the selector has not refreshed. See the
[official skill documentation](https://learn.chatgpt.com/docs/build-skills).
Nothing is installed into your global skills directory.

To import the tools into another project through npm, use this repository's
`fahu-skills install` CLI. It copies the full bundle into `.agents/pstack/`
and regular entrypoint folders into `.agents/skills/`. The package's root
README documents GitHub installation, group selection, and conflict handling.
The copied tools work independently of npm's cache and `node_modules`.

The 58 public upstream skills have prefixed entrypoints, plus the `$pstack`
help entrypoint. Upstream marks 57 public skills explicit-only; that policy is
preserved in `agents/openai.yaml`. Setup and the help entrypoint allow implicit
selection. Cross-skill calls still work by reading their prefixed entrypoints.
The three Benny automation skills stay dormant and outside discovery.

## Codex adaptation

Every entrypoint first loads [`codex.md`](codex.md), then its unchanged upstream
workflow. The adapter applies transitively to the workflow’s references,
playbooks, prompts, and scripts. Cross-skill calls return through the adapter
entrypoints. Keeping one adapter avoids changing the preserved source or
losing supporting files during conversion.

The adapter maps Cursor tools to shell, patch, connector, browser, and
collaboration capabilities actually available in the session. Cursor agents
become bounded prompt roles, rather than invented Codex agent types. Models
inherit the session instead of using upstream Grok or Claude defaults.

Applicable `AGENTS.md` files, session instructions, the user’s scope, and
existing project skills take precedence. The existing `commits` and
`github-pr-management` directories are unchanged. At installation time no
`AGENTS.md` existed in this repository or its filesystem ancestor directories;
none was added or replaced. When using these skills in another project, its
instructions still apply. Installation does not grant permission to send
messages, file tickets, create PRs, merge, deploy, or delete work.

### Limitations

Cursor cloud machines, webhook routines, secret-request cards, Project stores,
`/loop`, and Bugbot triggering have no direct mapping here. Benny stays
unregistered. `make-bot-ui` explains that its Cursor backend is unavailable and
stops before provisioning anything. Local delegates do not provide cloud
persistence. Multiple passes on one model do not provide model diversity.
The complete mapping and fallback behavior are in [`codex.md`](codex.md).

`cursor-team-kit` control skills and `deslop` are not bundled upstream and are
not installed here. Use available project harnesses and report missing checks.
The statechart and PR watcher scripts retain their original dependencies;
installation neither installs those dependencies nor claims those workflows
were tested. Some scripts bootstrap packages or fetch Git refs, so read-only
investigations use native reads instead of running them.

## Reviewed source and pin

- Repository: `https://github.com/cursor/plugins`
- Commit: `4dd1d05818d19792e7cd6e818f1667f95f7e1dbe`
- Subtree: `pstack`
- Subtree Git tree: `4719e1c4b4c43bac85d4206a8b41dd2899769c1c`
- Review date: 2026-10-31.
- File hashes, executable modes, command map, and invocation policies:
  [`upstream.lock.json`](upstream.lock.json).

The pinned repository head’s merge subject is “Update Gopuff logo”; it is a
repository-wide revision, not a pstack release tag. The pstack version is read
from that revision’s `plugin.json`. The subtree tree ID identifies the actual
pstack content.

The review covered public skill metadata, the main routing and investigation
workflows, agent definitions, harness guidance, setup, history, reflection,
autonomy and PR/cleanup playbooks, and script entrypoints and dependency
behavior. Material compatibility differences are addressed in the adapter.
This is an integration review, not an exhaustive audit of every upstream
script or fixture. No upstream code runs during discovery.

The source was fetched into a temporary Git checkout, pinned, and copied with
the skill-installer’s non-overwriting copy helper. Supporting files are kept
as one complete subtree. There is no auto-update or floating dependency.

### Validate or update

Run the offline integrity and entrypoint check from the repository root:

```sh
python3 pstack/scripts/verify.py
```

In an npm-imported project, run `python3 .agents/pstack/scripts/verify.py`.

For a future update, fetch a new revision into a separate temporary checkout,
review the pstack subtree diff and license, then update the snapshot, lock,
wrappers, and adapter together. Preserve original file modes. Recheck all
wrapper links, invocation policies, and actual Codex discovery, and repeat a
read-only investigation. Never replace the snapshot from floating `main`
without reviewing and recording the new commit.

[`SMOKE-TEST.md`](SMOKE-TEST.md) records installation verification and its limits.

## Command map

These are skill names to mention in Codex. The upstream folder remains the
original name inside `upstream/skills/`.

| Codex skill | Upstream workflow | Invocation |
| --- | --- | --- |
| `$pstack` | Help router | Explicit or implicit |
| `$pstack-architect` | [architect](upstream/skills/architect/SKILL.md) | Explicit |
| `$pstack-arena` | [arena](upstream/skills/arena/SKILL.md) | Explicit |
| `$pstack-automate-me` | [automate-me](upstream/skills/automate-me/SKILL.md) | Explicit |
| `$pstack-benchmark-checklist` | [benchmark-checklist](upstream/skills/benchmark-checklist/SKILL.md) | Explicit |
| `$pstack-blast-radius` | [blast-radius](upstream/skills/blast-radius/SKILL.md) | Explicit |
| `$pstack-bro` | [bro](upstream/skills/bro/SKILL.md) | Explicit |
| `$pstack-correct` | [correct](upstream/skills/correct/SKILL.md) | Explicit |
| `$pstack-create-formal-verification-skill` | [create-formal-verification-skill](upstream/skills/create-formal-verification-skill/SKILL.md) | Explicit |
| `$pstack-create-verification-skill` | [create-verification-skill](upstream/skills/create-verification-skill/SKILL.md) | Explicit |
| `$pstack-figure-it-out` | [figure-it-out](upstream/skills/figure-it-out/SKILL.md) | Explicit |
| `$pstack-how` | [how](upstream/skills/how/SKILL.md) | Explicit |
| `$pstack-in-your-own-words` | [in-your-own-words](upstream/skills/in-your-own-words/SKILL.md) | Explicit |
| `$pstack-interrogate` | [interrogate](upstream/skills/interrogate/SKILL.md) | Explicit |
| `$pstack-ketchup` | [ketchup](upstream/skills/ketchup/SKILL.md) | Explicit |
| `$pstack-ketchup-video` | [ketchup-video](upstream/skills/ketchup-video/SKILL.md) | Explicit |
| `$pstack-maintain-formal-verification-skill` | [maintain-formal-verification-skill](upstream/skills/maintain-formal-verification-skill/SKILL.md) | Explicit |
| `$pstack-maintain-verification-skill` | [maintain-verification-skill](upstream/skills/maintain-verification-skill/SKILL.md) | Explicit |
| `$pstack-make-bot-ui` | [make-bot-ui](upstream/skills/make-bot-ui/SKILL.md) | Explicit |
| `$pstack-no-comments` | [no-comments](upstream/skills/no-comments/SKILL.md) | Explicit |
| `$pstack-poteto-help` | [poteto-help](upstream/skills/poteto-help/SKILL.md) | Explicit |
| `$pstack-poteto-mode` | [poteto-mode](upstream/skills/poteto-mode/SKILL.md) | Explicit |
| `$pstack-principle-attack-the-premise` | [principle-attack-the-premise](upstream/skills/principle-attack-the-premise/SKILL.md) | Explicit |
| `$pstack-principle-boundary-discipline` | [principle-boundary-discipline](upstream/skills/principle-boundary-discipline/SKILL.md) | Explicit |
| `$pstack-principle-build-the-lever` | [principle-build-the-lever](upstream/skills/principle-build-the-lever/SKILL.md) | Explicit |
| `$pstack-principle-encode-lessons-in-structure` | [principle-encode-lessons-in-structure](upstream/skills/principle-encode-lessons-in-structure/SKILL.md) | Explicit |
| `$pstack-principle-exhaust-the-design-space` | [principle-exhaust-the-design-space](upstream/skills/principle-exhaust-the-design-space/SKILL.md) | Explicit |
| `$pstack-principle-experience-first` | [principle-experience-first](upstream/skills/principle-experience-first/SKILL.md) | Explicit |
| `$pstack-principle-explain-the-number` | [principle-explain-the-number](upstream/skills/principle-explain-the-number/SKILL.md) | Explicit |
| `$pstack-principle-fix-root-causes` | [principle-fix-root-causes](upstream/skills/principle-fix-root-causes/SKILL.md) | Explicit |
| `$pstack-principle-foundational-thinking` | [principle-foundational-thinking](upstream/skills/principle-foundational-thinking/SKILL.md) | Explicit |
| `$pstack-principle-guard-the-context-window` | [principle-guard-the-context-window](upstream/skills/principle-guard-the-context-window/SKILL.md) | Explicit |
| `$pstack-principle-laziness-protocol` | [principle-laziness-protocol](upstream/skills/principle-laziness-protocol/SKILL.md) | Explicit |
| `$pstack-principle-make-operations-idempotent` | [principle-make-operations-idempotent](upstream/skills/principle-make-operations-idempotent/SKILL.md) | Explicit |
| `$pstack-principle-migrate-callers-then-delete-legacy-apis` | [principle-migrate-callers-then-delete-legacy-apis](upstream/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md) | Explicit |
| `$pstack-principle-minimize-reader-load` | [principle-minimize-reader-load](upstream/skills/principle-minimize-reader-load/SKILL.md) | Explicit |
| `$pstack-principle-model-the-domain` | [principle-model-the-domain](upstream/skills/principle-model-the-domain/SKILL.md) | Explicit |
| `$pstack-principle-never-block-on-the-human` | [principle-never-block-on-the-human](upstream/skills/principle-never-block-on-the-human/SKILL.md) | Explicit |
| `$pstack-principle-outcome-oriented-execution` | [principle-outcome-oriented-execution](upstream/skills/principle-outcome-oriented-execution/SKILL.md) | Explicit |
| `$pstack-principle-prove-it-works` | [principle-prove-it-works](upstream/skills/principle-prove-it-works/SKILL.md) | Explicit |
| `$pstack-principle-redesign-from-first-principles` | [principle-redesign-from-first-principles](upstream/skills/principle-redesign-from-first-principles/SKILL.md) | Explicit |
| `$pstack-principle-separate-before-serializing-shared-state` | [principle-separate-before-serializing-shared-state](upstream/skills/principle-separate-before-serializing-shared-state/SKILL.md) | Explicit |
| `$pstack-principle-sequence-verifiable-units` | [principle-sequence-verifiable-units](upstream/skills/principle-sequence-verifiable-units/SKILL.md) | Explicit |
| `$pstack-principle-subtract-before-you-add` | [principle-subtract-before-you-add](upstream/skills/principle-subtract-before-you-add/SKILL.md) | Explicit |
| `$pstack-principle-test-behavior-not-implementation` | [principle-test-behavior-not-implementation](upstream/skills/principle-test-behavior-not-implementation/SKILL.md) | Explicit |
| `$pstack-principle-type-system-discipline` | [principle-type-system-discipline](upstream/skills/principle-type-system-discipline/SKILL.md) | Explicit |
| `$pstack-recall` | [recall](upstream/skills/recall/SKILL.md) | Explicit |
| `$pstack-reflect` | [reflect](upstream/skills/reflect/SKILL.md) | Explicit |
| `$pstack-setup-pstack` | [setup-pstack](upstream/skills/setup-pstack/SKILL.md) | Explicit or implicit |
| `$pstack-sharpen` | [sharpen](upstream/skills/sharpen/SKILL.md) | Explicit |
| `$pstack-show-me-your-work` | [show-me-your-work](upstream/skills/show-me-your-work/SKILL.md) | Explicit |
| `$pstack-statechart` | [statechart](upstream/skills/statechart/SKILL.md) | Explicit |
| `$pstack-swarm` | [swarm](upstream/skills/swarm/SKILL.md) | Explicit |
| `$pstack-tdd` | [tdd](upstream/skills/tdd/SKILL.md) | Explicit |
| `$pstack-teach` | [teach](upstream/skills/teach/SKILL.md) | Explicit |
| `$pstack-technical-writing` | [technical-writing](upstream/skills/technical-writing/SKILL.md) | Explicit |
| `$pstack-typescript-best-practices` | [typescript-best-practices](upstream/skills/typescript-best-practices/SKILL.md) | Explicit |
| `$pstack-unslop` | [unslop](upstream/skills/unslop/SKILL.md) | Explicit |
| `$pstack-why` | [why](upstream/skills/why/SKILL.md) | Explicit |
