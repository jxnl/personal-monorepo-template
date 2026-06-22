---
name: onboarding
description: Set up or resume Assistant from a workspace and the user's existing Codex threads. Use when the user asks to get started, invokes onboarding, has missing Assistant setup state, or needs a lightweight work map, shared memory, thread topology, and optional check-in without a broad connected-source scan.
last_edited: 2026-06-22
---

# Assistant Onboarding

Build the smallest useful Assistant setup, verify it, and let the relationship deepen through real work. Use a short, natural introduction appropriate to the request; do not require a scripted greeting.

## Skill Configuration

### Default Sources

Start with the repository and Codex threads:

- root and nearest `README.md` and `AGENTS.md` files;
- `projects/`, `experiments/`, and `people/` indexes when present;
- `agent/ASSISTANT_SETUP.md` and `agent/USER_CONTEXT.md` when present;
- summaries from at most five relevant pinned or recent threads.

Do not inspect messages, email, calendar, documents, trackers, or other connected sources during the default pass. Offer a targeted read later only when it would resolve a named gap or unlock a concrete workflow.

### State And Approval

`agent/ASSISTANT_SETUP.md` owns operational progress. Durable user context stays in `agent/USER_CONTEXT.md`. Do not merge setup bookkeeping into user memory.

Before writing memory, creating automations, or creating, renaming, pinning, or unpinning threads, show one concrete batch and receive approval. That approval covers only the displayed batch.

## Workflow

Read and follow `references/first-meeting-flow.md`. It is the canonical owner of onboarding phases, resume behavior, completion criteria, and next actions.

Load these only when the matching branch is reached:

- `references/shared-memory-vault.md` for approved vault setup or extension;
- `../assistant/references/heartbeat-philosophy.md` for an approved check-in;
- `../manage-assistant-threads/SKILL.md` for thread discovery and the proposed thread batch.
- `../write-like-me-bootstrap/SKILL.md` only when the user requests voice learning or approves targeted enrichment from enough authored messages or email.

## Done Means

Onboarding is complete when the workspace map, user correction, memory decision, thread decision, and optional check-in decision are resolved, declined, or unavailable. Connected-source enrichment is optional and never blocks completion.

End with the map Assistant is carrying, what was verified, and one useful next move. Do not end completed onboarding with another setup questionnaire.
