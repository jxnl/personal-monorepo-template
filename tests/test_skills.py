from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text()
    assert text.startswith("---\n"), f"missing frontmatter: {path}"
    _, raw, _ = text.split("---", 2)
    data: dict[str, object] = {}
    for line in raw.splitlines():
        if not line.strip():
            continue
        key, sep, value = line.partition(":")
        assert sep, f"frontmatter line must be key/value: {path}: {line}"
        data[key.strip()] = value.strip()
    return data


def test_markdown_has_last_edited_frontmatter() -> None:
    markdown_files = sorted(
        path
        for path in ROOT.glob("**/*.md")
        if not any(part.startswith(".") for part in path.relative_to(ROOT).parts)
    )
    assert markdown_files
    for path in markdown_files:
        data = frontmatter(path)
        edited = str(data.get("last_edited", ""))
        assert date.fromisoformat(edited), path


def test_skill_frontmatter_shape() -> None:
    skill_files = sorted((ROOT / ".codex" / "skills").glob("*/SKILL.md"))
    assert skill_files
    for path in skill_files:
        data = frontmatter(path)
        assert set(data) == {"name", "description", "last_edited"}, path
        assert isinstance(data["name"], str) and data["name"]
        assert isinstance(data["description"], str) and data["description"]
        assert path.parent.name == str(data["name"]).strip("\"'")
        assert date.fromisoformat(str(data["last_edited"]))


def test_onboarding_scripts_default_to_repo_root_vault() -> None:
    script_dir = ROOT / ".codex" / "skills" / "onboarding" / "scripts"
    for script_name in (
        "setup_shared_memory_vault.py",
        "new_person_note.py",
        "new_project_note.py",
    ):
        module = load_module(script_dir / script_name)
        assert module.default_vault_dir() == ROOT


def test_shared_memory_setup_is_idempotent_and_preserves_existing_files(tmp_path: Path) -> None:
    script = (
        ROOT
        / ".codex"
        / "skills"
        / "onboarding"
        / "scripts"
        / "setup_shared_memory_vault.py"
    )
    agents = tmp_path / "AGENTS.md"
    agents.write_text("custom instructions\n")

    first = subprocess.run(
        [sys.executable, str(script), "--vault-dir", str(tmp_path)],
        check=True,
        capture_output=True,
        text=True,
    )
    first_result = json.loads(first.stdout)

    assert agents.read_text() == "custom instructions\n"
    assert (tmp_path / "agent" / "USER_CONTEXT.md").exists()
    setup = tmp_path / "agent" / "ASSISTANT_SETUP.md"
    assert "status: brand_new" in setup.read_text()
    assert "workspace_map: pending" in setup.read_text()
    assert "thread_topology: pending" in setup.read_text()
    assert str(agents) not in first_result["created_files"]

    second = subprocess.run(
        [sys.executable, str(script), "--vault-dir", str(tmp_path)],
        check=True,
        capture_output=True,
        text=True,
    )
    assert json.loads(second.stdout)["created_files"] == []


def test_assistant_skills_are_public_and_portable() -> None:
    skill_root = ROOT / ".codex" / "skills"
    skill_dirs = [
        skill_root / "assistant",
        skill_root / "onboarding",
        skill_root / "manage-assistant-threads",
    ]
    forbidden = (
        "/users/",
        "@openai",
        "enterprise.slack.com",
        "~/microwave",
        "oai_gh",
        "openai.com",
        "sushi",
    )

    files: list[Path] = [
        ROOT / ".codex" / "plugins" / "assistant" / "plugin.json",
        ROOT / "README.md",
    ]
    for skill_dir in skill_dirs:
        assert (skill_dir / "SKILL.md").exists()
        files.extend(
            path
            for path in skill_dir.rglob("*")
            if path.is_file() and path.suffix in {".json", ".md", ".py", ".yaml"}
        )

    for path in files:
        text = path.read_text().lower()
        for term in forbidden:
            assert term not in text, f"{term!r} found in {path}"


def test_assistant_behavior_has_one_owner_per_workflow() -> None:
    assistant = (ROOT / ".codex" / "skills" / "assistant" / "SKILL.md").read_text()
    onboarding = (ROOT / ".codex" / "skills" / "onboarding" / "SKILL.md").read_text()
    threads = (
        ROOT / ".codex" / "skills" / "manage-assistant-threads" / "SKILL.md"
    ).read_text()

    assert "../onboarding/SKILL.md" in assistant
    assert "../manage-assistant-threads/SKILL.md" in assistant
    assert "references/first-meeting-flow.md" in onboarding
    assert "## Batch Approval" in threads
    assert "## Ongoing Coordination" in threads
    assert "## Pinned Thread Synthesis" in threads
    assert "Relate work across threads" in assistant
    assert not (ROOT / ".codex" / "skills" / "onboarding" / "references" / "question-bank.md").exists()
    assert not (ROOT / ".codex" / "skills" / "onboarding" / "references" / "starter-capabilities.md").exists()
