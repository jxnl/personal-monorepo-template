#!/usr/bin/env python3
"""Create a replaceable person-note scaffold in an Assistant vault."""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path


def default_vault_dir() -> Path:
    return Path(__file__).resolve().parents[4]


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def normalize_key(value: str) -> str:
    text = normalize_text(value).lower()
    if "@" in text:
        text = text.split("@", 1)[0]
    text = re.sub(r"[^a-z0-9._-]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a new person note. Optionally choose a stable key when a durable handle is known."
    )
    parser.add_argument(
        "--vault-dir",
        default=str(default_vault_dir()),
        help="Vault root path. Defaults to the personal monorepo root containing this script.",
    )
    parser.add_argument("--name", required=True, help="Display name.")
    parser.add_argument(
        "--key",
        default="",
        help="Optional stable file key; defaults to the normalized name. Prefer a durable handle when known.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Report the proposed creation without writing.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    vault_dir = Path(args.vault_dir).expanduser().resolve(strict=False)
    name = normalize_text(args.name)
    if not name:
        raise SystemExit("Invalid --name value after normalization.")
    key = normalize_key(args.key or name)
    if not key:
        raise SystemExit("Invalid stable key after normalization.")

    note_path = vault_dir / "people" / f"{key}.md"
    if note_path.exists():
        raise SystemExit(f"Person note already exists; update the canonical note instead: {note_path}")

    today = date.today().isoformat()
    content = "\n".join(
        [
            "---",
            f"title: {json.dumps(name)}",
            "usernames: []",
            "aliases: []",
            "emails: []",
            "github_usernames: []",
            "teams: []",
            "tags:",
            "  - people",
            "last_seen_at:",
            f"created_at: {today}",
            f"updated_at: {today}",
            "---",
            "",
            "## Snapshot",
            "",
            f"- Name: {name}",
            "- Primary handle: Replace with a confirmed handle or directory ID when known.",
            "- Contact: Replace with a confirmed address when useful.",
            "- Team / role: Replace with confirmed context when known.",
            "",
            "## Why They Matter Now",
            "",
            "- Replace with a short, dated reason this relationship matters.",
            "",
            "## Working Style & Interaction Notes",
            "",
            "- Replace with evidence-backed collaboration patterns.",
            "",
            "## Collaboration Guidance",
            "",
            "- Replace with practical guidance for future work with this person.",
            "",
            "## Evidence Log",
            "",
            "- Add dated links to relevant conversations, documents, meetings, or project notes.",
            "",
            "## Open Questions",
            "",
        ]
    )

    result = {"ok": True, "dry_run": bool(args.dry_run), "path": str(note_path), "stable_key": key}
    if not args.dry_run:
        note_path.parent.mkdir(parents=True, exist_ok=True)
        note_path.write_text(content, encoding="utf-8")
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
