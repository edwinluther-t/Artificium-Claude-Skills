#!/usr/bin/env python3
"""
Restructure The Artificium skills collection from:
  skills/<category>/<subcategory>/<skill-name>.md

Into Claude Code's required format:
  output/<skill-name>/SKILL.md

The directory name (skill-name) is taken from the `name:` frontmatter field.
Conflicts (duplicate names) are reported and skipped.
"""

import os
import re
import sys
import shutil
from pathlib import Path

SOURCE_DIR = Path(__file__).resolve().parent / "skills"
OUTPUT_DIR = Path.home() / ".claude" / "skills"

def extract_name(content: str) -> str | None:
    """Extract the `name:` field from YAML frontmatter."""
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None
    frontmatter = match.group(1)
    name_match = re.search(r"^name:\s*(.+)$", frontmatter, re.MULTILINE)
    if not name_match:
        return None
    return name_match.group(1).strip().strip('"').strip("'")

def main():
    if not SOURCE_DIR.exists():
        print(f"ERROR: Source directory not found: {SOURCE_DIR}")
        sys.exit(1)

    skill_files = list(SOURCE_DIR.rglob("*.md"))
    print(f"Found {len(skill_files)} skill files")

    seen_names: dict[str, Path] = {}
    conflicts: list[tuple[Path, str, Path]] = []
    processed = 0
    errors = 0

    for skill_path in sorted(skill_files):
        content = skill_path.read_text(encoding="utf-8")
        name = extract_name(content)

        if not name:
            print(f"  SKIP (no name): {skill_path.relative_to(SOURCE_DIR)}")
            errors += 1
            continue

        if name in seen_names:
            conflicts.append((skill_path, name, seen_names[name]))
            print(f"  CONFLICT: '{name}' in {skill_path.relative_to(SOURCE_DIR)} (already from {seen_names[name].relative_to(SOURCE_DIR)})")
            errors += 1
            continue

        seen_names[name] = skill_path

        dest_dir = OUTPUT_DIR / name
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest_file = dest_dir / "SKILL.md"
        dest_file.write_text(content, encoding="utf-8")

        print(f"  OK: {name}")
        processed += 1

    print()
    print(f"Done: {processed} installed, {errors} skipped/conflicts")
    print(f"Output: {OUTPUT_DIR}")

    if conflicts:
        print()
        print("Conflicts (not installed — resolve manually):")
        for path, name, original in conflicts:
            print(f"  '{name}': {path.relative_to(SOURCE_DIR)} vs {original.relative_to(SOURCE_DIR)}")

if __name__ == "__main__":
    main()
