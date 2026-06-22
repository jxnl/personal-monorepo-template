---
last_edited: 2026-06-15
---

# Personal Codex Vault

Starter workspace for giving Codex durable context: projects, people, skills,
onboarding, recurring checks, and writing-style memory.

Canonical repo: `jxnl/personal-monorepo-template`.

This template gives Codex a place to look before it acts and a place to write
important context after you approve it:

- `projects/` for active work
- `experiments/` for short spikes
- `people/` for collaborators and agents
- `.codex/skills/` for repo-local skills

This repo is the Assistant shared-memory vault. Onboarding should update this
repo in place; it should not create a nested `vault/` directory or a separate
`~/vault` unless you explicitly choose a different location.

## Fast Start

Press `Cmd+Cmd` to open Codex and say:

```text
Set me up with jxnl/personal-monorepo-template as ~/vault
```

Codex should clone this template, create a Codex project rooted at `~/vault`,
start onboarding, and use that repo as the vault.

## Manual Setup

If you want to create the vault yourself:

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

## Set Up Codex

1. Open Codex.
2. Install the plugins you actually use.
3. Create a new Codex project rooted at `~/vault`.
4. Create a new thread in that project.
5. Say:

```text
$onboard me
```

## Plugins To Install First

Install plugins before onboarding so Assistant can read the right context.

Start with the tools where your work happens:

- Assistant
- Gmail or Outlook Email
- Google Calendar or Outlook Calendar
- Google Drive, Notion, Documents, Spreadsheets, Presentations, or PDF
- Slack or Teams
- GitHub, Linear, or Notion for project tracking
- Browser
- Chrome
- Computer Use

For Chrome workflows, install the Chrome plugin and the [Codex Chrome Extension](https://chromewebstore.google.com/detail/codex/hehggadaopoacecdllhhajmbjkdcmajg).

## What Onboarding Does

Onboarding should explain what it is checking before it checks it.

It should:

- read the workspace
- ask what projects exist and what matters
- ask who Codex should know about
- check whether useful plugins are missing
- offer thread automations for recurring checks
- offer a daily update monitor, people monitor, and project monitors where useful, defaulting to 9:00 AM and 4:00 PM check-ins in your timezone
- offer to bootstrap a `write-like-me` skill from your sent Slack and email writing
- offer shared-memory setup by using this repo as the vault
- proactively propose `people/*.md`, project packets, and `AGENTS.md` updates after scanning connected Slack, email, calendar, docs, project trackers, and GitHub context

Assistant should ask before sending messages, changing meetings, editing shared docs, creating automations, creating, pinning, renaming, or looping threads, installing plugins, or writing shared memory.

## Skills

Repo-local skills live under `.codex/skills/`.

Useful starting points:

- `onboarding`: first setup
- `assistant`: ongoing work support after onboarding
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
