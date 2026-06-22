---
last_edited: 2026-06-15
---

# Shared Memory Vault

The vault is optional plain-file memory for durable work context outside one chat.

Default path: the personal monorepo root that contains this skill. This template
repo is the vault. Do not create a nested `vault/` directory or a separate
`~/vault` during onboarding unless the user explicitly names another folder.

Default shape in this template:

```text
personal-monorepo/
|-- AGENTS.md
|-- TODO.md
|-- agent/
|   `-- USER_CONTEXT.md
|-- people/
|-- projects/
|-- notes/
`-- sources/
```

Use it for:

- the user's working profile
- durable projects and workstreams
- important people
- open loops and decisions
- source routes future Assistant chats should know

Do not use it for raw email/chat dumps, one-off names, weak guesses, or activity logs.

## Setup

After the interview is calibrated:

1. Explain the vault in one short paragraph.
2. Ask before creating or extending it.
3. If approved, run `../scripts/setup_shared_memory_vault.py` from this repo. Do not pass `--vault-dir` unless the user explicitly chose a different root.
4. Personalize `AGENTS.md` and `agent/USER_CONTEXT.md`.
5. Mention the path in the final recap.

If the template repo already has `AGENTS.md`, `people/`, `projects/`, or other
vault files, inspect them first and preserve their structure. Extend the existing
repo in place instead of creating another vault root.

## User-Facing Explanation

```md
**Shared Memory**

This chat is where we talk. The check-in is what brings me back. The vault is the plain-file memory I maintain so durable work context does not live only inside one chat.

**Question**

Want me to set that up?
```
