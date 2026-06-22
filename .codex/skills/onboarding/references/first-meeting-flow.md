---
last_edited: 2026-06-22
---

# Quick-First Onboarding Flow

This file owns onboarding state, transitions, completion, and user-facing next actions. Resume at the first incomplete step in `agent/ASSISTANT_SETUP.md`.

## Step 1: Orient

- **State:** `workspace_map`
- Read only the default workspace and thread sources from `../SKILL.md`; use the thread-management skill for read-only thread discovery.
- If the user arrived with a real task, begin that work before continuing setup.
- Do not broaden into connected sources because they are available.
- Complete when there is enough evidence for a short map of active work, likely priorities, and uncertain areas.

## Step 2: Show The Map

- Return a compact map: current projects, relevant existing threads, what appears important, and what remains uncertain.
- Keep the map provisional. Do not write it to memory yet.
- Complete when the user has seen a concrete first read rather than a generic capability list.

## Step 3: Calibrate

- **State:** `user_calibration`
- Ask one question at a time and no more than three questions total.
- Prefer, in order: what the map got wrong; what matters soon; which work should be coordinated in separate threads.
- Stop asking once the remaining ambiguity would not change the setup batch.
- Complete when the user has corrected the map or accepts it as useful enough.

## Step 4: Propose One Batch

- **States:** `memory`, `thread_topology`, `check_in`
- Show one reviewable proposal containing only applicable actions:
  - files to create or update and the durable meaning each will preserve;
  - up to three proposed satellite threads, including reuse, names, pins, and scope;
  - one optional hub check-in at 9:00 AM and 4:00 PM on weekdays in the user's timezone;
  - targeted connected-source enrichment, only when tied to a named gap.
- State clearly that no action has happened yet.
- Complete when the user approves, edits, or declines the batch.

## Step 5: Apply And Verify

- Mark setup `in_progress` before applying an approved batch.
- Use the shared-memory reference for files and the thread-management skill for threads.
- Preserve existing files and reuse existing threads.
- Read back every claimed file, title, pin, and automation state.
- Record each state as `complete`, `declined`, or `unavailable`; do not leave an approved action marked complete after a failed write or readback.

## Step 6: Close Or Deepen

- Set setup status to `ready` when all required states are resolved.
- Recap the map, verified setup, and how Assistant will help now.
- Offer at most one targeted enrichment action when it has a concrete payoff.
- If the user declines or stops, leave onboarding complete and continue through ordinary work.

## Guided Continuation

While status is `brand_new` or `in_progress`, finish or present the next incomplete high-value step. Do not replay completed steps, repeat the last recap, or force an optional branch. A normal user request can pause onboarding; help with it and then resume only when setup is relevant again.

When the user wants a reusable writing voice and has approved access to enough authored messages or email, `write-like-me-bootstrap` is one valid targeted enrichment action. Show the inferred posture preview and ask again before writing the generated skill. Declining or deferring it does not reopen onboarding.
