#!/usr/bin/env python3
"""Create a small plain-file shared-memory vault for Assistant."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def default_vault_dir() -> Path:
    return Path(__file__).resolve().parents[4]


ROOT_AGENTS_TEMPLATE = """# AGENTS.md

## Shared Memory Goal

Treat this vault as durable work memory for the user.

The vault should make future chats easier to resume from something explicit and
reviewable. It is not a transcript dump and it is not a replacement for the
user's repos, docs, email, or chat systems.

## User Snapshot

Assistant should personalize this section from the first meeting and keep it
current when the user's durable work shape changes.

- User:
- Role and work context:
- How they spend their time:
- What useful help feels like:
- Important people and spaces to learn first:

## Source Order

Prefer the best current evidence available for the task:

1. Existing vault notes and canonical packets
2. The user's current self-report and corrections
3. Connected work context such as messages, email, calendar, docs, and project systems when available
4. Current chat context and artifacts

Use absolute dates. Separate facts, self-report, and inference when that
distinction changes how future work should read the note.

## Writing Rules

- Preserve durable meaning, not activity logs.
- Prefer updating existing canonical notes before creating adjacent notes.
- Route TODOs, people, projects, daily summaries, and scratch notes explicitly.
- Preserve decisions, blockers, owners, dates, useful links, and open loops.
- In people notes, keep confirmed Slack handles, email addresses, teams, relationship context, collaboration guidance, and dated evidence.
- In project packets, keep owners and open loops in `README.md`; keep recurring Slack, DM, email, document, meeting, or repository routes in the nearest `AGENTS.md`.
- Keep raw source dumps, secrets, and noisy transcripts out of canonical notes.
- Do not send messages, reply to email, change meetings, edit shared documents, create automations, or write shared memory unless the user explicitly approves that specific action.
- If nothing meaningful changed, do not churn the vault.

## Vault Conventions

- `AGENTS.md` is the root operating guide for this vault.
- `TODO.md` is the vault-wide list for cross-workstream follow-ups.
- `agent/` is for user context, daily summaries, and agent-authored syntheses.
- `people/` is for notes about recurring collaborators and relationships.
- `projects/` is for rolling workstream packets.
- `projects/<project>/README.md` carries durable project state; `projects/<project>/AGENTS.md` carries recurring source and routing instructions.
- `notes/` is for durable scratch notes that do not yet belong in a person or project note.
- `sources/` is for retained imported evidence and source material; treat it as read-only by default.

## Where To Write

- User profile and operating preferences: `agent/USER_CONTEXT.md`
- Daily context worth carrying forward: `agent/daily-summary-YYYY-MM-DD.md`
- Cross-workstream follow-ups: `TODO.md`
- Person context: `people/<person>.md`
- Workstream state: `projects/<project>/README.md`
- Recurring project source routes: `projects/<project>/AGENTS.md`
- Other durable notes: `notes/`
- Retained imported evidence: `sources/` (read-only by default)

## Update Thresholds

- Update this `AGENTS.md` when the user teaches durable operating preferences, routing rules, or what useful help should feel like.
- Update the nearest project packet `AGENTS.md` when recurring sources or project-local routing becomes meaningfully clearer.
- Update person notes when relationship context, role, ownership, or collaboration guidance becomes meaningfully clearer.
- Update project packets when the source of truth, status, blocker, owner, decision, or open loop changes.
- Update `TODO.md` when a follow-up should survive beyond one chat or one project note.
- Keep transient facts and routine status out of `AGENTS.md`; write them to the canonical note they belong in.
- Keep weak guesses tentative until the user confirms them or repeated evidence supports them.
"""


TODO_TEMPLATE = """# TODO

## Purpose

This is the vault-wide list for cross-workstream follow-ups and open loops that
should not live only inside one chat.

## Active

## Waiting

## Completed
"""


USER_CONTEXT_TEMPLATE = """# User Context

This note is Assistant's durable working profile for the user.

## Snapshot

- User:
- Role and work context:
- How they spend their time:

## Important People And Spaces

## Workstreams

## Stress And Attention Patterns

## How Assistant Should Help

## Action Boundaries

- Draft or propose first. Act only after the user explicitly approves that specific external or shared action.
"""


PROJECTS_README_TEMPLATE = """# Projects

This folder holds pages for ongoing projects.

Prefer one page per project over scattered status notes.

## Active packets
"""


PROJECTS_AGENTS_TEMPLATE = """# AGENTS.md

## Purpose

This folder holds canonical rolling project packets.

## Structure

- `projects/README.md` indexes active packets.
- `projects/<project>/README.md` holds durable project state, decisions, blockers, open loops, and evidence links.
- `projects/<project>/AGENTS.md` holds recurring sources and update-routing instructions.

## Defaults

- Prefer updating an existing canonical packet over creating an adjacent status note.
- Keep recurring Slack, DM, email, document, meeting, and repository inputs in the nearest packet `AGENTS.md`.
- Keep current status and one-off evidence links in the packet `README.md`.
- Use absolute dates and label inference when it matters.
"""


def resolve_path(raw: str) -> Path:
    return Path(raw).expanduser().resolve(strict=False)


def ensure_dir(path: Path, created_dirs: list[str], dry_run: bool) -> None:
    if path.exists():
        return
    created_dirs.append(str(path))
    if not dry_run:
        path.mkdir(parents=True, exist_ok=True)


def ensure_file(path: Path, content: str, created_files: list[str], dry_run: bool) -> None:
    if path.exists():
        return
    created_files.append(str(path))
    if not dry_run:
        path.write_text(content, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Set up Assistant shared-memory vault files.")
    parser.add_argument(
        "--vault-dir",
        default=str(default_vault_dir()),
        help="Vault root path. Defaults to the personal monorepo root containing this script.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print planned actions without writing.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    vault_dir = resolve_path(args.vault_dir)

    created_dirs: list[str] = []
    created_files: list[str] = []

    for rel_dir in ("agent", "people", "projects", "notes", "sources"):
        ensure_dir(vault_dir / rel_dir, created_dirs, args.dry_run)

    ensure_file(vault_dir / "AGENTS.md", ROOT_AGENTS_TEMPLATE, created_files, args.dry_run)
    ensure_file(vault_dir / "TODO.md", TODO_TEMPLATE, created_files, args.dry_run)
    ensure_file(
        vault_dir / "agent" / "USER_CONTEXT.md",
        USER_CONTEXT_TEMPLATE,
        created_files,
        args.dry_run,
    )
    ensure_file(
        vault_dir / "projects" / "README.md",
        PROJECTS_README_TEMPLATE,
        created_files,
        args.dry_run,
    )
    ensure_file(
        vault_dir / "projects" / "AGENTS.md",
        PROJECTS_AGENTS_TEMPLATE,
        created_files,
        args.dry_run,
    )

    result = {
        "ok": True,
        "dry_run": bool(args.dry_run),
        "vault_dir": str(vault_dir),
        "created_dirs": created_dirs,
        "created_files": created_files,
        "next_steps": [
            "Personalize AGENTS.md and agent/USER_CONTEXT.md from the calibrated first meeting.",
            "Propose initial person notes and project packets, then create only explicitly approved items.",
            "Treat sources/ as read-only by default when retaining imported evidence.",
        ],
    }
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
