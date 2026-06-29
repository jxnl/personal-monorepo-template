---
name: rename-and-pin
description: Rename and pin the current Codex thread. Use when the user asks to rename, retitle, name, or pin this thread.
last_edited: 2026-06-29
---

# Rename And Pin

Give the current thread a title that fits the user's existing sidebar conventions, then pin it. This skill changes only the current thread; it does not create, rename, pin, unpin, or archive any other thread.

## Workflow

1. Use `list_threads` to inspect the other threads before choosing a title. Compare their prefixes, casing, punctuation, and level of detail. Give the most weight to recent pinned threads and threads in the same project.
2. Identify the current thread from runtime context or the thread list. Never guess its ID.
3. Choose a concise title that describes the thread's actual purpose and follows the observed convention. If the user supplied an exact title, use it exactly after completing the convention check.
4. Use `set_thread_title` to rename the current thread.
5. Use `set_thread_pinned` to pin the current thread. Preserve every other thread's pin state.
6. List or read back the current thread and verify both the exact title and pinned state.

A direct request to use this skill authorizes these two changes to the current thread; do not ask for an extra confirmation. If thread tools are unavailable, do not invent a title, thread ID, or successful mutation. If only one change succeeds, report the partial result plainly.

## Output

Return the final title and confirm that the current thread is pinned. Mention only failures or unverified state that still need attention.
