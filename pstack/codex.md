# pstack for Codex

Read this adapter before any file under `upstream/`. It applies to every
upstream skill, playbook, agent prompt, reference, template, and script.
The upstream snapshot is reference material, not a Codex plugin installation.
This adapter replaces conflicting upstream harness instructions.

## Scope and project instructions

Follow system and developer instructions, the user's current request, and all
applicable `AGENTS.md` files before this adapter or upstream pstack. Load the
target project's instructions when working outside this skills repository.
Do not create, replace, or weaken `AGENTS.md` to install or configure pstack.
Preserve existing skills, user work, commit conventions, and PR review rules.
In this repository, use the existing `commits` and `github-pr-management`
skills for their respective workflows. In particular, leave review-thread
resolution to the user or reviewer unless explicitly instructed otherwise.

Installing pstack does not activate poteto-mode for every task. The selected
workflow and current request determine scope. Upstream's "use any MCP tool",
"just do it", autonomy grants, side-fix PRs, backlog filing, automatic PR
creation, merge, cleanup, and publishing instructions do not supply user
authorization. Apply the session's actual permission and communication rules.
An investigation stays read-only, including its delegates. Do not write a log,
configuration, skill, commit, ticket, or PR as part of a read-only investigation.
Never reset, discard, or move unrelated work to satisfy an upstream playbook.
Use a suitable current checkout unless the task or project requires isolation.

## Names and local paths

The public Codex names use `pstack-`, for example `$pstack-how`,
`$pstack-why`, `$pstack-poteto-mode`, and `$pstack-setup-pstack`.
`$pstack` opens the pstack help workflow. See [the command table](README.md).
These are skill mentions, not new shell commands or native slash commands.

- `<pstack>` means this directory. `upstream/` is its unchanged pinned source.
- Every `/name`, `pstack:name`, `**name** skill`, or bare upstream skill name
  means the `pstack-name` entrypoint in `skills/`, when present. Load that
  entrypoint even when the upstream reference links directly to another
  upstream `SKILL.md`. This keeps the adapter and special-case overrides active.
- References, scripts, assets, and playbooks relative to an upstream file
  resolve relative to that file in `upstream/`, not the wrapper directory.
- Upstream GitHub URLs for bundled files resolve to the local pinned copy.
  Do not fetch `main` to resolve a local reference. Cite the pinned URL when
  sharing an upstream link.
- New project skills belong in `.agents/skills/<name>/` unless the user or
  project chooses another supported location. Do not write Cursor rules or
  install anything globally as a side effect.
- Cursor `disable-model-invocation: true` becomes
  `policy.allow_implicit_invocation: false` in `agents/openai.yaml`.
  Cursor icons, colors, and `paths` frontmatter are not Codex activation rules.

## Tools

Use only tools actually available in the session. Discover connector tools by
name and description before use; never invent a method or a tool argument.

| Cursor instruction | Codex capability or fallback |
| --- | --- |
| `Read`, `Grep`, `Glob`, `Shell`, `Bash` | `exec_command` with scoped reads and `rg` / `rg --files`; use `apply_patch` for authorized edits. |
| `Task` | `collaboration.spawn_agent` when delegation is allowed; see the agent rules below. |
| `resume`, steer a Task | `send_message`, `followup_task`, or `interrupt_agent` for an existing agent when appropriate. |
| Wait for Task output | `wait_agent`; collect and verify the result before reporting it. Respect session wait limits. |
| `AskQuestion` | `request_user_input_async` if offered; `request_user_input` only in modes and cases that allow it. Otherwise ask a concise question in the reply. |
| `TodoWrite`, open a todolist | A provided planning tool, or a short checklist in the conversation. No assumed Cursor task store. |
| Cursor `create-skill` | The available Codex `skill-creator` skill and its validator. |
| Built-in PR tools, `gh`, Origin | Prefer the connected GitHub tools when sufficient. Use an authenticated forge CLI as a fallback. Verify repository, branch, and head. |
| `control-ui` | Available browser/computer tools or the project's existing browser harness, following its skill instructions. |
| `control-cli` | `exec_command` and, for interactive processes, a PTY with `write_stdin`. |
| `deslop` from cursor-team-kit | No bundled equivalent. Review the diff against project style and existing checks; do not claim `/deslop` ran. |
| MCP source investigators | Available read-only connectors, scoped to the user's question. Missing access is an evidence gap, not proof of absence. |

## Agents and models

Cursor agent definitions are prompt files, not registered Codex agent types.
When a workflow calls for `poteto-agent`, give the delegate the absolute paths
to this adapter, `upstream/agents/poteto-agent.md`, and the
`pstack-poteto-mode` entrypoint. Its Cursor plugin search is replaced by those
paths. For `comment-sicko`, provide `upstream/agents/comment-sicko.md` and a
bounded diff or file scope. Its output is recommendations only; the parent
decides which changes fit the user request. Do not automatically delete
comments or refactor code merely to satisfy that persona.

- `generalPurpose` and other `subagent_type` values are not tool arguments.
  Express the role in the brief. Omit `is_background`, `run_in_background`,
  `readonly`, `file_attachments`, `environment`, and `cloud_base_branch`.
- Read-only is a task constraint, not a sandbox flag supported by
  `spawn_agent`. Tell the delegate to use only read operations, pass the
  applicable project constraints, and verify the workspace afterward.
  `readonly: false` never grants write permission or additional MCP access.
- Inherit the parent model and reasoning effort by default. Never pass
  upstream Grok/Claude slugs, guessed models, or Cursor speed suffixes.
  Explicit user or applicable instruction choices must use supported model
  and reasoning fields from the actual tool. A full-history fork cannot
  override those fields; follow the tool's fork requirements when needed.
- An optional `<pstack>/models.json` stores only explicitly requested local
  role choices. Read it when present; a missing role means inheritance.
  Do not create it on installation or edit global Codex configuration.
- State that diverse-model evidence is unavailable when the session cannot
  supply it. Several agents on one model are independent passes, not a
  multi-model panel. Never describe simulated lenses as independent agents.
- Respect session concurrency limits and batch work into waves. If delegation
  is unavailable or forbidden, do the feasible work sequentially and disclose
  the missing independent pass. Do not invent agent results or create visible
  chats as a substitute for subagents.
- A local worktree can isolate a delegate only when created and assigned
  explicitly using available worktree capabilities. `spawn_agent` itself does
  not allocate a worktree or a cloud machine.

## Workflow overrides

### Setup

`$pstack-setup-pstack` replaces the entire upstream setup procedure. Explain
that all roles currently inherit the session model and effort. When the user
requests role customization, inspect the actual delegation schema, show the
supported choices, and resolve any material missing preference. Save only
requested choices in `<pstack>/models.json`, with a `roles` object keyed by
upstream role name. A value is `"inherit-parent"` or an object with `model`
and optional `reasoning_effort`; panels may use lists of those values. Validate
the choices against the current session before use. Do not modify `AGENTS.md`,
`~/.codex/config.toml`, or `.cursor/rules/`. No always-applied model rule is
installed. Configuration does not override session model restrictions.

### History and reflection

Use the current conversation or available Codex chat tools (`list_threads`,
`read_thread`, `wait_threads`) for relevant history, scoped to the requested
project and period. Do not guess transcript paths or scan unrelated chats.
If those tools are absent, use supplied transcripts or state the gap. Use the
session's memory instructions for memory access and changes. Reflection may
draft skill improvements, but the upstream approval gate for applying them
remains. Do not file its backlog in an external tracker without authorization.

### Investigation

Follow the upstream Investigation playbook and the selected how/why workflow.
Keep its confidence labels, file citations, and distinction between behavior
and inferred intent. Read-only means no logging helpers, installs, Git fetch,
bootstrap, server startup, or source changes. A small question may use a single
sequential exploration when delegation is unavailable or disallowed.

### Scripts and dependencies

The complete upstream scripts and fixtures are preserved. They are not
executed by installation or skill selection. Before running one, inspect its
entrypoint and requirements. `poteto-mode` tooling uses Bun and its bootstrap
can install packages even on an apparent help/status invocation. The worktree
audit can fetch refs and read Cursor transcripts. Use native read-only Git
queries for a read-only audit. Run tools that install or generate files in a
temporary copy; do not change the pinned snapshot. Do not run cleanup, PR,
merge, network, or installation commands merely because a playbook lists them.

Statechart needs the documented Node/Bun and Java/TLA+ tooling; rendering and
property tests have additional dependencies. Report missing dependencies when
that workflow is requested. These tools are preserved, not certified by the
installation smoke test. Never imply a formal proof or runtime check ran
because its scripts are present.

## Unsupported and conditional features

| Upstream feature | Status in this adaptation |
| --- | --- |
| Cursor cloud VMs and cloud-agent dashboards | Unsupported. Local delegates/worktrees can cover bounded work, not cloud persistence or remote machine guarantees. |
| Cursor Project store, tracker, and PR/CI subscriptions | No direct portable equivalent. Use available Codex tools or a task-local record only within authorized scope. Report missing durable/event capabilities. |
| Cursor `/loop` and dynamic routine wakes | No native translation. Continue within the session for bounded work. For a requested recurring task, discover the Codex automation tool and configure its real schema. Do not silently create a schedule. |
| Cursor Automations, `update_state` routines, `api2.cursor.sh`, `SendToUser` secret cards | Unsupported. Do not call guessed endpoints or request secrets through chat. Codex scheduled tasks do not imply webhook support. |
| `make-bot-ui` | The Cursor webhook/secret flow is unsupported. Explain the missing requirement; do not run its Tailscale install or expose a server. A separately requested portable design requires its own available backend. |
| Benny automation pack | Preserved under `upstream/automations/benny/`, dormant and unregistered, as upstream intended. No schedules, Slack messages, or issue writes are created. |
| Bugbot triggering/configuration | Unsupported here. Existing GitHub review comments can be read and triaged normally. Missing Bugbot is not a passing review. |
| Cursor team kit, Origin, project control skills | Not installed. Use the table above and existing project harnesses; disclose required evidence that cannot be collected. |
| Multi-model panels / Cursor fast-mode budgets | Conditional on actual supported models and instructions. Default is parent inheritance; no family-diversity claim. |
| `ketchup-video` | Requires available local rendering tools and inspected output; otherwise report rendering unavailable and provide the text catch-up. No fabricated video. |

For an unavailable optional step, name the limitation briefly and continue
independent work. If a required step or verification depends on it, report
the task as incomplete for that part. Never skip a gate and call the result
verified, shipped, or merged.
