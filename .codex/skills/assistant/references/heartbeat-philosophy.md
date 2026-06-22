---
last_edited: 2026-06-22
---

# Assistant Check-Ins

Recurring check-ins exist to do useful work, not to manufacture notifications.

## Default Shape

- One optional check-in belongs to the pinned `Assistant` hub.
- Default proposal: 9:00 AM and 4:00 PM on weekdays in the user's timezone.
- The hub may inspect approved project and monitor threads during its pass.
- A satellite gets its own automation only when its cadence, owner, or completion condition cannot be handled cleanly by the hub.
- Update an existing matching automation rather than creating a duplicate.

## Approval And Readback

Show the name, cadence, scope, and notification threshold before creation. Create or change the automation only after approval. Afterward, read back the live state before saying it is active.

If automation tools are unavailable, say so and continue without a workaround.
Do not emit raw scheduling syntax or create a detached job as a substitute for a thread-attached check-in.

## What A Check-In Does

1. List pinned threads, then inspect summaries for the most relevant pins and approved lanes.
2. Look for a meaningful change, stalled handoff, duplicated effort, pending decision, preparation gap, or useful synthesis.
3. Relate decisions, blockers, dependencies, people, deadlines, and artifacts across threads.
4. Steer an approved thread when a bounded follow-up can unblock it.
5. Preserve durable meaning only when it passes `memory-guidance.md`.
6. Notify only when the synthesis would likely change the user's decision or action.

Routine churn, unchanged status, and weak guesses are not notifications. It is valid to inspect, do useful work, and stay quiet.

Automation prompts should stay thin: name the work to inspect, the completion or notification threshold, and the focused skill to use. Do not copy this entire contract into each prompt.
