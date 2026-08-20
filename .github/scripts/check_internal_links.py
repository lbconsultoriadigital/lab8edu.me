#!/usr/bin/env python3
"""Validate relative links in Markdown files without making network requests."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SKIPPED_SCHEMES = {"http", "https", "mailto", "tel"}


def candidate_paths(source: Path, destination: str) -> list[Path]:
    parsed = urlsplit(destination)
    raw_path = unquote(parsed.path)
    if not raw_path:
        return []

    base = ROOT if raw_path.startswith("/") else source.parent
    target = (base / raw_path.lstrip("/")).resolve()

    candidates = [target]
    if target.suffix == ".html":
        candidates.append(target.with_suffix(".md"))
    if not target.suffix:
        candidates.extend(
            [
                target.with_suffix(".md"),
                target / "index.md",
                target / "README.md",
            ]
        )
    elif target.is_dir():
        candidates.extend([target / "index.md", target / "README.md"])
    return candidates


def main() -> int:
    errors: list[str] = []
    for source in sorted(ROOT.rglob("*.md")):
        if ".git" in source.parts or "node_modules" in source.parts:
            continue
        text = source.read_text(encoding="utf-8")
        for match in LINK_PATTERN.finditer(text):
            destination = match.group(1).strip().split(maxsplit=1)[0].strip("<>")
            parsed = urlsplit(destination)
            if parsed.scheme in SKIPPED_SCHEMES or destination.startswith("#"):
                continue
            if "{{" in destination or "{%" in destination:
                continue

            candidates = candidate_paths(source, destination)
            if not candidates:
                continue
            if not any(candidate.exists() for candidate in candidates):
                relative_source = source.relative_to(ROOT)
                errors.append(f"{relative_source}: missing target {destination}")

    if errors:
        print("Broken internal Markdown links:")
        print("\n".join(f"- {error}" for error in errors))
        return 1

    print("All internal Markdown links are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
