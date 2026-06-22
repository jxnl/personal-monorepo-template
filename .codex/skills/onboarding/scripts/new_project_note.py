#!/usr/bin/env python3
"""Create and list a project packet in an Assistant vault."""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path


ACTIVE_PACKETS_HEADING = "## Active packets"


def default_vault_dir() -> Path:
    return Path(__file__).resolve().parents[4]


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def normalize_slug(value: str) -> str:
    text = normalize_text(value).lower()
    text = re.sub(r"[^a-z0-9._-]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create and list a new project packet.")
    parser.add_argument(
        "--vault-dir",
        default=str(default_vault_dir()),
        help="Vault root path. Defaults to the personal monorepo root containing this script.",
    )
    parser.add_argument("--title", required=True, help="Human-readable project title.")
    parser.add_argument(
        "--slug",
        default="",
        help="Optional file-system slug; defaults to the normalized title.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Report the proposed creation without writing.")
    return parser.parse_args()


def insert_router_entry(content: str, entry: str) -> str:
    if ACTIVE_PACKETS_HEADING not in content:
        raise ValueError(
            "Existing projects/README.md does not contain '## Active packets'; inspect the nonstandard router before writing."
        )
    if entry.rstrip() in {line.rstrip() for line in content.splitlines()}:
        return content
    marker_index = content.index(ACTIVE_PACKETS_HEADING) + len(ACTIVE_PACKETS_HEADING)
    line_end = content.find("\n", marker_index)
    if line_end < 0:
        return content + f"\n\n{entry}\n"
    return content[: line_end + 1] + f"\n{entry}" + content[line_end + 1 :]


def main() -> int:
    args = parse_args()
    vault_dir = Path(args.vault_dir).expanduser().resolve(strict=False)
    title = normalize_text(args.title)
    if not title:
        raise SystemExit("Invalid --title value after normalization.")
    slug = normalize_slug(args.slug or title)
    if not slug:
        raise SystemExit("Invalid --slug value after normalization.")

    projects_dir = vault_dir / "projects"
    router_path = projects_dir / "README.md"
    packet_dir = projects_dir / slug
    packet_path = packet_dir / "README.md"
    routing_path = packet_dir / "AGENTS.md"
    if packet_dir.exists():
        raise SystemExit(f"Project packet already exists; inspect and update that packet instead: {packet_dir}")
    if not router_path.exists():
        raise SystemExit(f"Missing projects list; run vault setup before creating project packets: {router_path}")

    router_content = router_path.read_text(encoding="utf-8")
    entry = f"- [[projects/{slug}/README|{title}]]\n"
    try:
        updated_router = insert_router_entry(router_content, entry)
    except ValueError as error:
        raise SystemExit(str(error)) from error

    updated_at = date.today().isoformat()
    packet = "\n".join(
        [
            "---",
            f"title: {json.dumps(title)}",
            'status: "active"',
            "owner:",
            f"created_at: {updated_at}",
            f"updated_at: {updated_at}",
            "tags:",
            "  - project",
            "---",
            "",
            f"# {title}",
            "",
            "## Purpose",
            "",
            "- Replace with why this project matters and the outcome to track.",
            "",
            "## Current Status",
            "",
            "- Replace with the latest durable status, dated when timing matters.",
            "",
            "## People",
            "",
            "- Replace with owners, decision makers, collaborators, and links to canonical people notes.",
            "",
            "## Open Loops",
            "",
            "- Replace with pending decisions, blockers, and follow-ups.",
            "",
            "## Sources",
            "",
            "- Add direct evidence links with absolute dates.",
            "",
            "## Update History",
            "",
            f"- `{updated_at}`: Created project packet.",
            "",
        ]
    )
    routing = "\n".join(
        [
            "# AGENTS.md",
            "",
            "## Purpose",
            "",
            f"This packet tracks `{title}` as a canonical workstream.",
            "",
            "## Canonical Files",
            "",
            "- `README.md`: durable status, owners, decisions, blockers, open loops, and evidence links.",
            "",
            "## Recurring Sources To Revisit",
            "",
            "- Communication spaces / threads: Replace with recurring spaces that matter.",
            "- Direct conversations: Replace with recurring conversations that matter.",
            "- Decision-bearing correspondence: Replace with recurring threads when useful.",
            "- Documents / meetings / repositories: Replace with canonical working artifacts.",
            "",
            "## Update Rules",
            "",
            "- Update `README.md` when durable status, ownership, blockers, decisions, or open loops change.",
            "- Update this file only when recurring sources or packet routing change.",
            "- Keep one-off evidence links in `README.md` under `Sources`.",
            "- Use absolute dates and label inference when it matters.",
            "",
        ]
    )

    result = {
        "ok": True,
        "dry_run": bool(args.dry_run),
        "packet_path": str(packet_path),
        "routing_path": str(routing_path),
        "router_path": str(router_path),
        "router_entry": entry.rstrip(),
        "slug": slug,
    }
    if not args.dry_run:
        packet_dir.mkdir(parents=True, exist_ok=False)
        packet_path.write_text(packet, encoding="utf-8")
        routing_path.write_text(routing, encoding="utf-8")
        router_path.write_text(updated_router, encoding="utf-8")
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
