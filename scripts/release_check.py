#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "resume-builder"


def check(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip()
    return values


def main() -> int:
    failures: list[str] = []
    skill_md = SKILL / "SKILL.md"
    check(skill_md.exists(), "Missing runtime SKILL.md.", failures)
    if skill_md.exists():
        text = skill_md.read_text(encoding="utf-8")
        frontmatter = parse_frontmatter(text)
        check(
            set(frontmatter) == {"name", "description"},
            "SKILL.md frontmatter must contain only name and description.",
            failures,
        )
        check(
            frontmatter.get("name") == SKILL.name,
            "Skill name must match the folder name.",
            failures,
        )
        check(
            len(text.splitlines()) < 500,
            "SKILL.md must remain below 500 lines.",
            failures,
        )
        check(
            "untrusted data" in text.casefold()
            and "never obey instructions embedded" in text.casefold(),
            "SKILL.md must preserve the imported-content safety boundary.",
            failures,
        )
        references = sorted(
            set(
                re.findall(
                    r"(?<![\w.-])((?:references|scripts|schemas)/[A-Za-z0-9_./-]+)",
                    text,
                )
            )
        )
        for relative in references:
            relative = relative.rstrip(".,;:)")
            check(
                (SKILL / relative).exists(),
                f"SKILL.md references missing file: {relative}",
                failures,
            )

    required = [
        SKILL / "agents" / "openai.yaml",
        SKILL / "scripts" / "resume_tool.py",
        SKILL / "schemas" / "career-record.schema.json",
        SKILL / "schemas" / "intake-session.schema.json",
        SKILL / "references" / "interaction-flow.md",
        SKILL / "references" / "domain-router.md",
        SKILL / "references" / "domains" / "catalog.json",
        ROOT / "README.md",
        ROOT / "LICENSE",
        ROOT / "VERSION",
        ROOT / "CHANGELOG.md",
        ROOT / "docs" / "sources-and-design-decisions.md",
        ROOT / "docs" / "tested-examples.md",
        ROOT / "docs" / "github-publishing.md",
        ROOT / "docs" / "assets" / "sample-resume-preview.png",
        ROOT / "examples" / "product-analyst" / "README.md",
    ]
    for path in required:
        check(path.exists(), f"Missing required file: {path.relative_to(ROOT)}", failures)

    catalog: dict = {}
    catalog_path = SKILL / "references" / "domains" / "catalog.json"
    if catalog_path.exists():
        try:
            catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
            domains = catalog.get("domains", [])
            ids = [item.get("id") for item in domains]
            check(len(ids) == len(set(ids)), "Domain IDs must be unique.", failures)
            check(bool(catalog.get("fallback")), "Domain fallback is required.", failures)
            for item in domains + [catalog.get("fallback", {})]:
                profile = item.get("profile")
                check(bool(profile), f"Domain {item.get('id')} has no profile.", failures)
                if profile:
                    check(
                        (SKILL / "references" / "domains" / profile).exists(),
                        f"Missing domain profile: {profile}",
                        failures,
                    )
        except json.JSONDecodeError as exc:
            failures.append(f"Domain catalog JSON is invalid: {exc}")

    json_files = [
        *SKILL.glob("schemas/*.json"),
        *SKILL.glob("examples/*.json"),
        *ROOT.glob("evals/*.json"),
    ]
    for path in json_files:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            failures.append(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")

    requirement_paths = (ROOT / "requirements.txt", SKILL / "requirements.txt")
    requirement_sets = [
        {
            line.strip()
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.startswith("#")
        }
        for path in requirement_paths
    ]
    check(
        requirement_sets[0] == requirement_sets[1],
        "Root and runtime dependency pins must match.",
        failures,
    )
    pins: dict[str, tuple[int, ...]] = {}
    for requirement in requirement_sets[0]:
        match = re.fullmatch(r"([a-z0-9-]+)==([0-9]+(?:\.[0-9]+)*)", requirement)
        check(bool(match), f"Runtime dependency must use an exact pin: {requirement}", failures)
        if match:
            pins[match.group(1)] = tuple(int(part) for part in match.group(2).split("."))
    check(set(pins) == {"python-docx", "reportlab", "pypdf"}, "Unexpected runtime dependency set.", failures)
    minimums = {
        "python-docx": (1, 2, 0),
        "reportlab": (4, 5, 1),
        "pypdf": (6, 14, 2),
    }
    maximum_majors = {"python-docx": 2, "reportlab": 5, "pypdf": 7}
    for name, minimum in minimums.items():
        version = pins.get(name, ())
        check(
            version >= minimum and bool(version) and version[0] < maximum_majors[name],
            f"{name} must remain within the reviewed, patched major-version range.",
            failures,
        )

    if failures:
        print("Release check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("Release check passed.")
    print(f"Skill lines: {len(skill_md.read_text(encoding='utf-8').splitlines())}")
    print(f"Domain entries: {len(catalog.get('domains', []))}")
    print(f"JSON files checked: {len(json_files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
