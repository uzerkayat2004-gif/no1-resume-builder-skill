#!/usr/bin/env python3
from __future__ import annotations

import argparse
import zipfile
from pathlib import Path


EXCLUDED_PARTS = {"__pycache__", ".pytest_cache"}
EXCLUDED_SUFFIXES = {".pyc", ".pyo"}


def package(skill: Path, output: Path) -> Path:
    skill = skill.resolve()
    if not (skill / "SKILL.md").exists():
        raise ValueError(f"Not a skill folder: {skill}")
    output.mkdir(parents=True, exist_ok=True)
    destination = output / f"{skill.name}.skill"
    with zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(skill.rglob("*")):
            if not path.is_file():
                continue
            relative = path.relative_to(skill.parent)
            if any(part in EXCLUDED_PARTS for part in relative.parts):
                continue
            if path.suffix in EXCLUDED_SUFFIXES:
                continue
            archive.write(path, relative.as_posix())
    with zipfile.ZipFile(destination) as archive:
        bad = archive.testzip()
        if bad:
            raise RuntimeError(f"Archive integrity failed at {bad}")
    return destination


def main() -> int:
    parser = argparse.ArgumentParser(description="Package a Codex skill.")
    parser.add_argument(
        "--skill",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "skills" / "resume-builder",
    )
    parser.add_argument(
        "--outdir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "dist",
    )
    args = parser.parse_args()
    try:
        destination = package(args.skill, args.outdir)
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"error: {exc}")
        return 1
    print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

