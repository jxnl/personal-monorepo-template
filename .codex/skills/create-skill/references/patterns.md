---
last_edited: 2026-06-15
---

# Skill Design Patterns

Use these patterns only when the corresponding design choice is difficult.

## Invocation Decision

| Need | Default | Cost to manage |
| --- | --- | --- |
| Agent must discover the workflow from ordinary user intent | Implicit | Context load and false-positive routing |
| Another skill must hand off automatically | Implicit | Overlap with sibling descriptions |
| User intentionally controls a specialized or costly workflow | Explicit | User must remember the skill |
| Many explicit skills are hard to remember | Explicit behind a router | Router must remain a compact index |

An implicit description should name distinct request branches, not synonyms for
one branch. For example, `create`, `improve`, and `validate` describe different
authoring intents; `make`, `build`, and `author` often describe the same one.

## Branch Map

Use a short table before writing a conditional workflow:

| Branch | Entry condition | Owned output | Terminal condition |
| --- | --- | --- | --- |
| Create | No durable skill exists | New skill directory | Artifact validates |
| Improve | Editable source exists | Behavior-preserving patch | Regression prompts keep intended behavior |
| Audit | User did not authorize edits | Findings and proposed delta | Evidence and next action are clear |

If every branch needs a rule, keep the compact rule in `SKILL.md`. If only one
branch needs a long template or edge-case guide, put it in a reference and link
it from that branch.

## Leading Words

A useful leading word recruits established meaning and appears naturally in the
agent's plan or reasoning. Test it by checking whether the word predicts a
different action.

| Desired behavior | Candidate | Observable consequence |
| --- | --- | --- |
| Deliver an end-to-end increment before layers | `vertical slice` | Plan crosses storage, logic, and interface in one increment |
| Keep one authoritative behavior location | `single source of truth` | Duplicate rules are removed or linked to one owner |
| Explore enough before planning | `reconnaissance` | Agent gathers named evidence before proposing work |
| Preserve behavior while simplifying | `refactor` | Regression cases are stated before deletion |

Reject a candidate when it is vague (`robust`, `thorough`), newly invented, or
needs more explanation than the prose it replaces.

## Completion Criteria

Weak:

```text
Review the source and create the skill.
```

Stronger:

```text
Complete source review when every requested behavior is mapped to one owning
step, reference, script, or explicit exclusion. Complete creation when the
skill validates and the primary and failure prompts have expected outcomes.
```

A criterion should be observable and exhaustive where omission matters. Prefer
`every modified surface accounted for` over `check the changes`.

## Behavior Test Matrix

Write expected outcomes before running prompts:

| Prompt type | What it proves | Expected observation |
| --- | --- | --- |
| Positive, direct wording | Main trigger and path | Skill activates and produces its owned artifact |
| Positive, alternate wording | Trigger recall | Same skill activates without copied description text |
| Neighboring negative | Boundary | Adjacent workflow remains unclaimed |
| Missing input or failure | Recovery | Agent asks narrowly, falls back safely, or stops clearly |

Static validation proves file shape, not invocation quality. Runtime tests prove
behavior only for the harness and environment in which they ran.
