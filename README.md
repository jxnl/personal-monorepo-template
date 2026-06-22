---
last_edited: 2026-06-22
---

# Personal Monorepo

Starter workspace for Codex.

Canonical repo: `jxnl/personal-monorepo-template`.

This template gives Codex a place to look before it acts:

- `projects/` for active work
- `experiments/` for short spikes
- `people/` for collaborators and agents
- `.codex/skills/` for repo-local skills

This repo is also the Assistant shared-memory vault. Onboarding should update
this repo in place; it should not create a nested `vault/` directory or a
separate `~/vault` unless you explicitly choose a different location.

## Install

Create your vault from the template:

```sh
cd ~
git clone https://github.com/jxnl/personal-monorepo-template.git vault
cd vault
rm -rf .git
git init
```

That gives you:

```text
~/vault
```

This repo is the vault. Do not create a second `vault/` directory inside it.

If you do not want to think about the setup, press `Cmd+Cmd` to open Codex and
say: `Set me up with jxnl/personal-monorepo-template as ~/vault`.

## Set Up Codex

1. Open Codex.
2. Create a new Codex project rooted at `~/vault`.
3. Create a new thread in that project.
4. Say:

```text
Help me get started with Assistant.
```

Assistant starts from this workspace and your existing Codex threads. Connected
tools are optional and never block setup.

## What Onboarding Does

The default onboarding is deliberately small:

1. Read the workspace and summaries from up to five relevant Codex threads.
2. Show a provisional map of projects, priorities, and existing thread ownership.
3. Ask at most three useful questions, one at a time.
4. Propose memory changes, up to three project or monitor threads, and an optional check-in as one batch.
5. Apply the approved batch and verify every write, title, pin, and automation.
6. Offer a targeted connected-source read only when it unlocks something concrete.

Assistant can complete onboarding even when no connected tools are installed.
Later, it may recommend a message, email, calendar, document, tracker, code-host,
browser, or computer-control connection when a specific workflow needs one.

One optional enrichment is `write-like-me-bootstrap`, which can infer distinct writing postures from approved authored-message or email sources and create a private repo-local writing skill. It is never required to finish onboarding.

## Thread Topology

Assistant uses a small hub-and-satellites model:

- `Assistant`: the pinned coordination hub.
- `Project: <name>`: active project work with a distinct outcome.
- `Monitor: <scope>`: narrowly scoped recurring observation.
- `loop: <task>` and `done: <task>`: temporary automation lifecycle names.

Before changing threads, Assistant shows a single reviewable batch covering reuse,
creation, names, pins, scope, and scheduling. Within an approved topology it may
read and steer those threads, while external and consequential actions still
require their own approval.

Pinned threads are Assistant's proactive radar. It reads summaries selectively
and relates decisions, blockers, dependencies, owners, deadlines, and artifacts
across them when the connection changes what should happen next.

The optional hub check-in runs at 9:00 AM and 4:00 PM on weekdays in your
timezone. Satellite threads get their own automation only when they need a
genuinely different cadence or completion condition.

## Skills

Repo-local skills live under `.codex/skills/`.

Useful starting points:

- `onboarding`: first setup
- `assistant`: ongoing work support after onboarding
- `manage-assistant-threads`: organize and coordinate the thread topology
- `loop`: recurring checks on a thread
- `new-project`: create a project or experiment
- `new-person`: create a person note
- `write-like-me-bootstrap`: create a personal writing-style skill from Slack and email

## Structure

- `projects/`: long-lived work
- `experiments/`: short-lived spikes
- `people/`: notes about people or agents
- `.codex/`: skills, plugin metadata, and assets
- `templates/`: starter files
- `tests/`: checks for template integrity
