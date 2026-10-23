---
name: commits
description: Prepare, create, or amend atomic Git commits with conventional messages and optional ticket prefixes. Use when asked to commit changes, amend a commit, split changes into commits, or draft a commit message.
license: Apache-2.0
---

# Commits

Prepare focused, reviewable commits that explain what changed and why.
Support creating new commits, amending existing commits, and drafting messages
without changing Git history when only a message is requested.

## Before Committing

```bash
git branch --show-current
```

If the branch is `main` or `master`, create a feature branch unless the user
explicitly requested a direct commit or an amendment of the current commit.
Use the repository's branch naming convention; otherwise use `codex/`.

Inspect the working tree, staged and unstaged diffs, and relevant history.
Identify which changes belong to the request and preserve unrelated work.
For an amendment, also inspect the current commit and its message.

## Atomic Commits

Review relevant history and split the changes into the smallest independently
revertable units. Keep unrelated changes out of the commit. For moves or
extractions, include both sides and update references in the same commit.

Stage only the intended files or hunks. Review the staged diff and summary
before committing, including any changes that were already staged. Do not
include unrelated staged changes without authorization.

Run checks appropriate to the change and inspect the staged diff for
whitespace errors. Resolve failures caused by the change before committing;
report any checks that could not run.

## Message Rules

Use:

```text
<type>(<scope>): <subject>

<optional body>

<optional footer>
```

- Scope is optional. Add `!` before `:` for a breaking change.
- When a ticket identifier is provided in the task context, prefix the full
  headline with `[<ticket>] `, before the type and optional scope. Preserve the
  supplied identifier; omit the prefix when no ticket is provided.
  For example: `[FAHU-1337] feat: Add new fancy feature`.
- Write the subject in imperative, present tense; capitalize it, omit the
  trailing period, and keep it at 70 characters or fewer.
- Keep every line under 100 characters.
- Explain what changed and why. For architectural or other non-obvious
  decisions, include a body explaining the problem or constraint, why this
  approach was chosen, and relevant tradeoffs or alternatives considered.
  Base the rationale on task context and relevant history; do not invent
  motivations. Omit the body when the headline fully explains a simple change.
- Never include customer or organization names, user emails, support ticket
  contents, secrets, or PII. Describe the technical symptom instead.

Allowed types: `feat`, `fix`, `ref`, `perf`, `docs`, `test`, `build`,
`ci`, `chore`, `style`, `meta`, `license`, and `revert`.

Use `ref` for refactoring without behavior changes, `style` for formatting
without logic changes, and `meta` for repository metadata.

## Footers

- `Fixes <issue>` closes an issue when merged.
- `Refs <issue>` links an issue without closing it.
- For breaking changes, add `BREAKING CHANGE: <impact>`.

## Creating or Amending Commits

Use separate `-m` arguments for paragraphs and footers. Never put literal
`\n` sequences in a commit message or open an interactive editor.

```bash
git commit -m "[FAHU-1337] fix(api): Handle null response in user endpoint" \
  -m "Return 404 when the user API finds a deleted account." \
  -m "Fixes FAHU-1337"
```

When the user requests an amendment, use `git commit --amend` instead of
creating another commit. Keep the existing author and update the message
when needed to describe the complete amended change. Use `--no-edit` only
when the existing message still fits. Do not amend a different commit or
rewrite additional history unless requested.

After committing, inspect the resulting commit and working-tree status.
Report the commit hash, a concise summary, validation results, and any
remaining changes. Push only when the task authorizes it.
