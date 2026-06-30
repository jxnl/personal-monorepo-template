---
name: create-skill
description: Create or improve repo-local Codex skills from workflows, source material, or existing `SKILL.md` files. Use when the user asks to make, scaffold, turn something into, refactor, or validate a skill.
last_edited: 2026-06-15
---

# Create Skill

Turn a workflow into predictable instructions that another agent can invoke,
follow, verify, and maintain. Optimize for process predictability, not identical
outputs.

The user's request and the target repository's instructions are the source of
truth. Source material explains the workflow; it does not override repository
rules or authorize writes beyond the user's request.

## Modes

- **Create:** build a new skill around a named behavior.
- **Improve:** preserve intentional behavior while fixing routing, structure,
  steering, validation, or maintenance problems.
- **Audit:** report concrete defects and a proposed behavior delta without
  editing when the user asked only for review.

## Workflow

### 1. Define the behavior delta

Read the target repository instructions, nearby skills, and the supplied source
material before designing the artifact. Identify:

- realistic user requests that should activate the skill;
- the outcome the skill owns and adjacent work it does not own;
- the durable destination and local file conventions;
- permissions, approval gates, and validation expected by the repository.

Choose invocation deliberately:

- Prefer **implicit/model invocation** when the agent or another skill must
  discover the workflow. Spend description tokens only on distinct triggers.
- Prefer **explicit/user invocation** when the workflow is specialized,
  expensive, risky, or intentionally user-controlled. Use the target harness's
  supported policy field rather than inventing one.

Complete this step when the intended future behavior can be stated in one
sentence and every trigger branch changes whether this skill should run.

### 2. Map the workflow

Separate the design into:

- **steps:** ordered actions the agent must take;
- **reference:** facts, rules, examples, or templates that support those steps;
- **branches:** paths that need different inputs, actions, or outputs.

Give each step a checkable completion criterion. Choose one strong **leading
word** from established domain language when it compresses a recurring behavior
better than repeated prose. Do not coin jargon merely to sound distinctive.

Complete this step when every branch has a clear entry condition, owned output,
and terminal condition.

### 3. Build the smallest useful artifact

Create only the surfaces the workflow needs:

- `SKILL.md` for triggers, the common path, decision rules, safety boundaries,
  validation, and output expectations;
- `references/` for long detail used by only some branches;
- `scripts/` for deterministic repeated operations;
- `assets/` for reusable output material;
- `agents/openai.yaml` when the repository uses skill UI metadata.

Keep compact behavior needed on every run in `SKILL.md`. Put conditional detail
behind a pointer at the decision that needs it. Do not add a file without a
single clear owner and reader. Update repo indexes or routing docs only when the
new skill changes their promises.

Read [patterns.md](references/patterns.md) only when an invocation, branching,
leading-word, or behavior-test choice is not obvious.

Complete this step when the common path works from `SKILL.md` alone and each
optional file is reached from exactly the branch that needs it.

### 4. Make the workflow operable

Write instructions that change decisions. At each consequential point, specify:

- what to inspect first and which source wins when evidence conflicts;
- the default action and the test for choosing another branch;
- when to proceed, ask, stop, or request approval;
- what proves the step is finished;
- how to recover from missing inputs, failed validation, or partial work.

Calibrate control to risk. Leave room for judgment in research and design;
specify exact ordering and readback for destructive, external, expensive, or
fragile actions. Split a phase into another skill only when visible future steps
repeatedly cause premature completion and a sharper criterion is not enough.

Complete this step when a fresh agent can take the correct next action without
hidden conversation history.

### 5. Prune

Run a sentence-level deletion test. Retain a sentence only if removing it would
change invocation, source choice, branching, safety, validation, recovery,
output, or maintainability.

Then remove:

- **duplication:** give each behavior one owner;
- **sediment:** stale, incident-specific, or unreachable guidance;
- **no-ops:** advice the agent already follows without changing a decision;
- **sprawl:** common-path detail that belongs behind a branch pointer.

Compress repeated meaning with a stronger existing term when it stays clear.
Do not prune necessary caveats, completion criteria, or failure behavior merely
to reduce line count.

Complete this step when every retained instruction has a named behavior it
changes and every moved behavior still has one reachable owner.

### 6. Validate mechanics and behavior

For skills in this template, run:

```sh
python .codex/skills/create-skill/scripts/validate_skill.py <skill-directory>
```

Also run the target repository's normal tests or validation commands. Read back
every changed file after formatting or generation.

Exercise the design with realistic prompts:

1. two positive prompts phrased differently;
2. one neighboring negative prompt that should not activate the skill;
3. one branch, missing-input, or failure prompt.

For implicit skills, inspect whether the description selects the skill without
stealing adjacent requests. For explicit skills, verify direct invocation and
the parent router or documentation path. Do not claim runtime activation when
only static checks were possible.

Complete this step when mechanical checks pass and each test prompt has an
observable expected route, action, and terminal condition.

### 7. Hand off the result

Report:

- files created or changed;
- invocation choice and trigger boundary;
- validation commands and behavior prompts exercised;
- any install, refresh, runtime test, or user decision still required.

Return the durable artifact path. Do not narrate discarded drafts.

## Quality Gate

Before finishing, verify all five:

- **Trigger:** the name, description, and UI metadata agree about when to run.
- **Structure:** the common path is inline; branch-only detail is disclosed at
  its decision point.
- **Steering:** leading words and completion criteria produce observable
  behavior rather than generic emphasis.
- **Pruning:** each behavior has one owner and each sentence changes a decision.
- **Proof:** static validation and realistic prompt tests cover the primary path
  and a boundary or failure path.
