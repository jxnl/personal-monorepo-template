---
last_edited: 2026-06-22
---

# Shared Memory Vault

The personal monorepo is Assistant's optional, reviewable shared memory. Use the repository root in place; do not create a nested vault or another default root.

## Separation Of Concerns

```text
agent/ASSISTANT_SETUP.md  operational onboarding state
agent/USER_CONTEXT.md     durable user context and preferences
people/                   recurring collaborators
projects/                 durable workstream packets
notes/                    useful material without a canonical project or person owner
sources/                  retained evidence, read-only by default
```

`AGENTS.md` owns stable routing and behavior. `TODO.md` is for cross-workstream follow-ups that should survive beyond one chat.

## Setup

After the user approves the memory portion of the onboarding batch:

1. Run `../scripts/setup_shared_memory_vault.py` from this repository. Pass `--vault-dir` only when the user chose another root.
2. Preserve every existing file; the script creates missing scaffolding only.
3. Personalize only the approved files.
4. Read back each claimed write.
5. Mark the corresponding setup states complete only after readback succeeds.

## What Belongs

Keep durable goals, responsibilities, preferences, decisions, owners, source routes, important collaborators, and open loops. Exclude raw communication dumps, temporary status, weak guesses, and broad connected-source inventories.

Updating the vault is not permission to send messages, edit shared systems, or take another external action.
