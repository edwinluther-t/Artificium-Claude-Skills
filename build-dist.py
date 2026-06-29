#!/usr/bin/env python3
"""
Build skills-dist/ from skills/

Reads every .md file in skills/, extracts the `name:` frontmatter field,
and writes it to skills-dist/<name>/SKILL.md

Run this after adding or editing any skill in skills/.
Conflicts (duplicate name: values) are reported and skipped.
"""

import re
import sys
from pathlib import Path

SOURCE_DIR = Path(__file__).parent / "skills"
DIST_DIR = Path(__file__).parent / "skills-dist"


def extract_name(content: str) -> str | None:
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None
    name_match = re.search(r"^name:\s*(.+)$", match.group(1), re.MULTILINE)
    if not name_match:
        return None
    return name_match.group(1).strip().strip('"').strip("'")


def main():
    if not SOURCE_DIR.exists():
        print(f"ERROR: {SOURCE_DIR} not found")
        sys.exit(1)

    # Wipe and rebuild dist
    if DIST_DIR.exists():
        import shutil
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir()

    skill_files = sorted(SOURCE_DIR.rglob("*.md"))
    print(f"Found {len(skill_files)} skill files in skills/")

    seen: dict[str, Path] = {}
    conflicts: list[tuple[Path, str, Path]] = []
    installed = 0

    for path in skill_files:
        content = path.read_text(encoding="utf-8")
        name = extract_name(content)

        if not name:
            print(f"  SKIP (no name:): {path.relative_to(SOURCE_DIR)}")
            continue

        if name in seen:
            conflicts.append((path, name, seen[name]))
            print(f"  CONFLICT '{name}': {path.relative_to(SOURCE_DIR)} vs {seen[name].relative_to(SOURCE_DIR)}")
            continue

        seen[name] = path
        dest = DIST_DIR / name / "SKILL.md"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content, encoding="utf-8")
        installed += 1

    print(f"\nDone: {installed} skills written to skills-dist/")

    if conflicts:
        print(f"\n{len(conflicts)} conflict(s) — not installed (fix the name: field in one of each pair):")
        for path, name, original in conflicts:
            print(f"  '{name}'")
            print(f"    kept:    {original.relative_to(SOURCE_DIR)}")
            print(f"    skipped: {path.relative_to(SOURCE_DIR)}")

    if conflicts:
        sys.exit(1)


if __name__ == "__main__":
    main()
