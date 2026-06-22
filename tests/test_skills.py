from __future__ import annotations

import importlib.util
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
        if ".git" not in path.parts
    )
    assert markdown_files
    for path in markdown_files:
        data = frontmatter(path)
        assert data.get("last_edited") == "2026-06-15", path


def test_skill_frontmatter_shape() -> None:
    skill_files = sorted((ROOT / ".codex" / "skills").glob("*/SKILL.md"))
    assert skill_files
    for path in skill_files:
        data = frontmatter(path)
        assert set(data) == {"name", "description", "last_edited"}, path
        assert isinstance(data["name"], str) and data["name"]
        assert isinstance(data["description"], str) and data["description"]
        assert data["last_edited"] == "2026-06-15"


def test_onboarding_scripts_default_to_repo_root_vault() -> None:
    script_dir = ROOT / ".codex" / "skills" / "onboarding" / "scripts"
    for script_name in (
        "setup_shared_memory_vault.py",
        "new_person_note.py",
        "new_project_note.py",
    ):
        module = load_module(script_dir / script_name)
        assert module.default_vault_dir() == ROOT
