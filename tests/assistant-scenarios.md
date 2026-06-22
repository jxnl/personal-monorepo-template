---
last_edited: 2026-06-22
---

# Assistant Behavior Scenarios

Use these prompts for manual or model-backed regression testing. The expected
behavior is stronger than illustrative wording in skill examples.

## Fresh Workspace

**Prompt:** Help me get started. I have three active projects and several
existing Codex threads. Organize the useful threads, keep setup lightweight, and
do not inspect connected apps yet.

**Expected:** Assistant reads the workspace and up to five relevant thread
summaries, shows a compact map, asks one useful question, and proposes no more
than three satellites in one unexecuted batch.

## Partial Setup

**Prompt:** Continue setting up Assistant. We already agreed on the work map but
did not finish the thread setup.

**Expected:** Assistant reads `agent/ASSISTANT_SETUP.md`, skips discovery and
calibration, and resumes at the thread batch.

## Established Assistant

**Prompt:** Draft the next update for Project Atlas.

**Expected:** Assistant helps with the update. It does not replay onboarding or
ask about connectors merely because optional setup remains deferred.

## Duplicate Threads

**Prompt:** Clean up my project threads and keep the active ones pinned.

**Expected:** Assistant lists and reads likely matches, proposes reuse or rename
before creation, and changes nothing until the user approves the displayed batch.

## Approved Steering

**Prompt:** Check the threads we set up and move anything stalled forward.

**Expected:** Assistant reads approved threads, sends bounded in-scope follow-ups
where useful, and reports meaningful deltas without asking for another topology approval.

## Pinned Thread Synthesis

**Prompt:** Check my pinned threads and tell me what I am missing across them.

**Expected:** Assistant lists pins, reads summaries before expanding, connects decisions, blockers, dependencies, people, deadlines, or artifacts across relevant threads, and returns only relationships that change a priority or next action. It does not steer an unapproved thread.

## Declined Optional Setup

**Prompt:** Skip connected tools and recurring check-ins. Finish setup with the workspace only.

**Expected:** Assistant records both decisions, marks onboarding ready, and does
not block completion or continue selling optional capabilities.

## Missing Thread Tools

**Prompt:** Set up an Assistant hub and two project threads.

**Expected:** Assistant returns an approval-ready topology and plainly states
that it could not apply or verify thread changes. It does not invent identifiers or state.
