---
name: manage-assistant-threads
description: Inspect, organize, create, rename, pin, schedule, or steer Codex threads for Assistant. Use when the user wants a multi-thread work system, asks Assistant to manage projects across threads, or onboarding needs a reviewable hub-and-satellites topology. Reuse existing threads and require approval before topology changes.
last_edited: 2026-06-22
---

# Manage Assistant Threads

Turn the user's Codex threads into a small, legible work system. This skill owns thread discovery, topology proposals, mutations, verification, and ongoing coordination. It does not own onboarding or durable memory policy.

## Topology

- `Assistant`: the pinned coordination hub.
- `Project: <name>`: one active project with a distinct outcome or working context.
- `Monitor: <scope>`: narrowly scoped recurring observation.
- `loop: <task>` and `done: <task>`: temporary automation lifecycle names owned by `../loop/SKILL.md`.

Prefer the smallest topology that creates clear ownership. During onboarding, recommend at most three satellite threads. Do not create a thread per person, source, or task by default.

## Inspect Before Proposing

1. List available saved projects when project-scoped creation may be needed.
2. List recent threads and identify pinned, similarly named, or same-project candidates.
3. Read summaries for likely matches; read detailed outputs only when needed to distinguish ownership, progress, or duplication.
4. Classify each proposed lane as `reuse`, `rename`, `create`, `pin`, `unpin`,
   `schedule`, or `leave unchanged`.

Do not treat activity or a pin as proof that a thread is current. Prefer reuse when an existing thread already owns substantially the same outcome.

## Pinned Thread Synthesis

Treat pinning as a strong relevance signal, not a guarantee that the lane is current. On proactive Assistant passes:

1. List pinned threads before choosing where to read deeply.
2. Read summaries first and expand only when a decision, blocker, dependency, or contradiction needs evidence.
3. Connect related work across threads, including shared owners, artifacts, deadlines, and duplicated requests.
4. Report the smallest synthesis that changes a priority, handoff, or next action.

Reading a pinned thread does not add it to the approved topology. Ask through a new batch before renaming, pinning, unpinning, scheduling, or steering an unapproved thread.

## Batch Approval

Before a topology change, show one compact table with:

- intended title and role;
- existing thread to reuse, when any;
- proposed create, rename, pin, unpin, or schedule actions;
- initial scope or follow-up prompt;
- check-in cadence and notification threshold, when any.

State that no changes have happened. Receive approval for the displayed batch; material additions or substitutions require another approval.

## Apply An Approved Batch

1. Re-list threads immediately before mutation to avoid racing a recent change.
2. Create only lanes that still lack a suitable owner:
   - use a saved project with a local environment for project work;
   - use a projectless thread for general coordination;
   - do not create a worktree for monitoring or coordination;
   - omit model and reasoning overrides unless the user requested them.
3. Rename and pin only the approved threads. Preserve unrelated pins.
4. Add a hub check-in only when approved. Use `../assistant/references/heartbeat-philosophy.md`.
5. Add a satellite automation only when it needs an independent cadence, owner, or completion condition that the hub cannot cover.
6. Read back every changed thread and automation. Report partial success honestly and leave failed operations incomplete.

## Ongoing Coordination

Within an approved topology, Assistant may:

- read thread status and recent turns;
- send bounded follow-ups that advance the thread's existing scope;
- surface cross-thread dependencies, duplicate work, stalled handoffs, conflicting ownership, and decisions;
- reconcile meaningful status into the hub;
- recommend archiving, unpinning, or restructuring through a new approved batch.

Do not silently expand a thread's scope, override its model, move its checkout, archive it, or perform an external action. A follow-up should name the outcome, source of truth, expected evidence, and stop condition without copying a large workspace context packet into the prompt.

## Failure Behavior

- If thread tools are unavailable, return the proposed topology without claiming changes.
- If creation succeeds but rename or pin fails, report the created thread and the failed readback.
- If a matching thread appears during application, stop and reuse or ask before duplicating it.
- Never invent thread IDs, project IDs, titles, pin state, or automation state.

## Output

Lead with the resulting topology or the approval-ready batch. For applied changes, include direct thread links when available and identify anything not verified.
