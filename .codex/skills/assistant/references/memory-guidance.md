---
last_edited: 2026-06-15
---

# Memory Guidance

The memory system should keep Assistant useful over time without turning into a raw archive of work activity.

Preserve durable meaning, not motion.

## Durable Memory Contract

Assistant should keep a compact canonical model with these sections:

1. `Assistant Profile`
   - who the user is
   - role, remit, broad work shape, and how they like help
   - Assistant's fixed role in this chat
2. `Company And Work Context`
   - the company, organization, team, product, customer, or operating context that makes the user's work legible
   - durable workstreams, responsibilities, and current chapter
3. `What I Am Carrying Right Now`
   - near-term priorities, pressure, commitments, and risks that matter beyond a single turn
4. `Important People`
   - recurring collaborators, reports, partners, customers, or stakeholders that materially shape the user's work
   - enough definition for each person that future Assistant knows who they are and why they matter
5. `Conversation Spaces`
   - channels, group conversations, recurring forums, or shared spaces that reliably shape the user's work
   - what each space is for and why it matters
6. `Operating Preferences`
   - what should be surfaced
   - what should stay quiet
   - what Assistant may draft
   - the user's email and Slack/chat tone when there is enough grounded evidence
   - how proactive it should be
7. `Recurring Help`
   - the core hourly check-in posture
   - the one Assistant check-in scope the user accepted or requested
   - recurring checks the user paused, rejected, or wants changed

## First Interview Seed

The deep first read by itself should not seed durable memory. It is still Assistant's inference. Seed memory after the user has answered at least the first interview question and Assistant has updated the working map from that calibration.

Only seed Codex memory through a real durable-memory tool or Assistant profile surface when one is explicitly available. Do not use shell commands or filesystem writes to create local Codex memory notes as a substitute. If no durable-memory surface is available, keep the calibrated map as the chat baseline and say that plainly.

## Shared Memory Vault

The explicit shared-memory vault is a different memory surface from Codex's
local Memories. When the user approves vault setup, Assistant may create or
update the plain-file vault described in
`../../onboarding/references/shared-memory-vault.md`.

In this template, the personal monorepo root is that vault. Use the repo in
place; do not create a nested `vault/` directory or a separate `~/vault` unless
the user explicitly chose a different path.

Use the vault for durable, reviewable work context outside one chat:

- the user profile and operating guidance
- recurring people and relationship context
- rolling workstream packets
- cross-workstream follow-ups and open loops
- daily context only when it is worth resuming later
- repo-local `AGENTS.md` routing rules that make future work easier to place

Do not treat the vault as permission to dump raw messages, transcripts, source
exports, or every inference into files. The same durable-memory discipline
still applies.

Capture:

- the grounded user snapshot
- the company or organization context that seems durable
- recurring workstreams versus current pressure
- people and conversation spaces supported by real source context
- the user's calibration, correction, stress/overhead patterns, and important-people guidance
- additions or corrections the user gives after Assistant proposes what the hourly check-in will watch
- the first help recommendation and any recurring-help decisions
- monitor-thread decisions, including accepted 9:00 AM and 4:00 PM check-ins or any timing the user chose instead

Use recurring evidence from roughly the last 90 days when sources support it. Keep recent pressure separate from durable identity and context.

## People And Spaces

The working first-meeting map can be broader than durable memory.

For people:

- preserve stable identity, role or team, and why they matter
- prefer resolved profile or directory facts over display-name guesses when people tools are available
- keep relationship reads provisional when evidence is inferential
- do not preserve a person from one incidental mention plus a profile lookup
- after Slack, email, calendar, docs, and project scans, proactively propose people notes for recurring collaborators, decision makers, reports, customers, partners, or other people who materially shape the user's work
- after approval, create or update the relevant `people/*.md` files directly in the vault

For channels and shared spaces:

- preserve only spaces that materially improve future interpretation or retrieval
- state what the space is for and why it matters to the user
- do not preserve a raw list of every channel search happened to surface

Do not create a giant shallow people map or a giant shallow channel map.

## Keep These Kinds Of Memory

- user goals, preferences, and working style when stated or strongly supported
- durable tone preferences for email, Slack, or chat replies when supported by self-report or repeated sent-message evidence
- company or team context that changes how the user's work should be read
- durable workstreams and responsibilities
- important people and recurring conversation spaces
- recurring pressure patterns, prep needs, or follow-up risks
- accepted recurring routines and interruption thresholds

## Usually Do Not Remember

- raw transcripts
- every interesting email or message
- ordinary inbox churn
- one-off wording quirks from a single message
- one-off asks with no lasting significance
- momentary task status
- every person or channel mentioned once
- weak guesses about personality or motivation

## Facts, Self-Report, And Inference

Keep these distinct when useful:

- fact: directly supported by source material
- self-report: something the user said about themselves
- inference: Assistant's current read based on evidence

If an inference materially affects future behavior, either keep it tentative or ask the user before making it durable.

When the user corrects you:

1. update the relevant durable memory
2. revise future scan emphasis and interruption thresholds
3. avoid continuing to behave as though the older read is still true
