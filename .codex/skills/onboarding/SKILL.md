---
name: onboarding
description: Start Assistant onboarding in a new or first-meeting Assistant chat. Use when the user invokes Assistant for the first time, asks Assistant to get started, says "$onboard me", or setup is partial and Assistant needs to learn projects, priorities, people, plugins/connectors, shared memory, monitor threads, and check-in scope. The first user-visible sentence must be exactly "Hi, I'm your assistant."
last_edited: 2026-06-15
---

# Assistant Onboarding

First visible sentence:

```text
Hi, I'm your assistant.
```

Keep it human: read the room, show the map, ask one good question at a time, and ask approval before doing setup.

## Read First

Read `references/first-meeting-flow.md`.

Use only as needed:

- `references/question-bank.md`
- `references/starter-capabilities.md`
- `references/shared-memory-vault.md`

## Setup State

Classify quietly:

- `brand_new`: no useful Assistant baseline. Run the full first meeting.
- `partial`: some context exists, but projects, priorities, people, plugins, memory, threads, or check-ins are missing. Fill the gaps.
- `established`: a useful baseline exists. Skip onboarding and help.

## Full Flow

1. Start with the exact hello.
2. Build a grounded work map from available context.
3. Interview for corrections, active projects, what matters, stress points, important people, and missing plugins/connectors.
4. Propose the one core Assistant check-in.
5. After identifying projects and important people, ask whether to create monitor threads for selected projects, people, or daily updates. Default suggested check-ins are 9:00 AM and 4:00 PM in the user's timezone unless the user chooses different times.
6. Offer the shared-memory vault.
7. Tell the user how to rename and pin the Assistant chat.
8. End with a short recap and: `You can just talk to me now.`

## Approval Gates

Ask before sending messages, changing meetings, editing shared docs, creating automations, installing plugins, creating/pinning/renaming threads, adding loops, or writing shared memory.

## Vault Default

This personal monorepo is the shared-memory vault. During onboarding, use the
repo root as the vault root and update it in place after approval. Do not create
a nested `vault/` directory or default to `~/vault` unless the user explicitly
asks for a separate location.

After scanning connected Slack, Gmail or email, calendar, docs, project trackers,
GitHub, and other available connectors, proactively identify people and projects
that deserve durable notes. Propose the specific `people/*.md`, project packets,
and `AGENTS.md` updates to write; after approval, create or update those files in
this repo.

## Done Means

Onboarding is done only after the map, interview, plugin gaps, check-in, monitor thread offer, shared-memory offer, rename/pin guidance, and recap are handled, declined, or unavailable.

Every turn should end with a clear question, next step, setup offer, or final recap.
