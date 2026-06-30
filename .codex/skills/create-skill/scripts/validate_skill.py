from __future__ import annotations

import argparse
import re
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


class ValidationReport:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    @property
    def ok(self) -> bool:
        return not self.errors


def parse_frontmatter(path: Path, report: ValidationReport) -> dict[str, str]:
    text = path.read_text()
    if not text.startswith("---\n"):
        report.errors.append(f"missing YAML frontmatter: {path}")
        return {}

    parts = text.split("---", 2)
    if len(parts) < 3:
        report.errors.append(f"unterminated YAML frontmatter: {path}")
        return {}

    data: dict[str, str] = {}
    for line in parts[1].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, separator, value = line.partition(":")
        if not separator:
            report.errors.append(f"frontmatter line must be key/value: {path}: {line}")
            continue
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def validate_links(skill_dir: Path, report: ValidationReport) -> None:
    for path in sorted(skill_dir.rglob("*.md")):
        for target in MARKDOWN_LINK_RE.findall(path.read_text()):
            target = target.split("#", 1)[0].strip()
            if not target or "://" in target or target.startswith(("mailto:", "/")):
                continue
            target = target.split(" ", 1)[0].strip("<>")
            if not (path.parent / target).exists():
                report.errors.append(f"broken relative link: {path}: {target}")


def validate_python(skill_dir: Path, report: ValidationReport) -> None:
    for path in sorted(skill_dir.rglob("*.py")):
        try:
            compile(path.read_text(), str(path), "exec")
        except SyntaxError as error:
            report.errors.append(f"invalid Python: {path}:{error.lineno}: {error.msg}")


def validate_skill(path: Path) -> ValidationReport:
    report = ValidationReport()
    skill_path = path if path.name == "SKILL.md" else path / "SKILL.md"
    skill_dir = skill_path.parent

    if not skill_path.is_file():
        report.errors.append(f"missing SKILL.md: {skill_path}")
        return report

    frontmatter = parse_frontmatter(skill_path, report)
    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")

    if not name:
        report.errors.append("frontmatter is missing name")
    elif not NAME_RE.fullmatch(name):
        report.errors.append(f"name must be lowercase hyphen-case: {name}")
    elif name != skill_dir.name:
        report.errors.append(f"name '{name}' does not match folder '{skill_dir.name}'")

    if not description:
        report.errors.append("frontmatter is missing description")
    elif len(description) > 300:
        report.warnings.append(
            "description exceeds 300 characters; check for workflow detail that belongs in the body"
        )

    if not re.search(r"^#\s+\S", skill_path.read_text(), re.MULTILINE):
        report.errors.append("SKILL.md is missing an H1 title")

    validate_links(skill_dir, report)
    validate_python(skill_dir, report)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate the mechanical shape of a Codex skill directory."
    )
    parser.add_argument("path", type=Path, help="Skill directory or SKILL.md path")
    args = parser.parse_args()

    report = validate_skill(args.path.resolve())
    for warning in report.warnings:
        print(f"warning: {warning}")
    for error in report.errors:
        print(f"error: {error}")

    if report.ok:
        print("ok: skill mechanics validated")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
