#!/usr/bin/env python3

"""Validate the repository's Markdown question-bank structure."""

from pathlib import Path
from urllib.parse import unquote
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
QUESTION_BANK = ROOT / "question-bank"
errors: list[str] = []
SECTION_HEADINGS = {
    "Questions To Ask The Interviewer",
    "Self-Reflection Prompts",
    "References",
    "Topic Map",
}


def fail(path: Path, message: str) -> None:
    errors.append(f"{path.relative_to(ROOT)}: {message}")


def github_heading_anchors(text: str) -> set[str]:
    """Approximate GitHub's generated anchors for Markdown headings."""
    anchors: set[str] = set()
    occurrences: dict[str, int] = {}
    for heading in re.findall(r"^#{1,6} (.+)$", text, flags=re.MULTILINE):
        value = re.sub(r"<[^>]+>", "", heading.lower())
        value = re.sub(r"[^\w\- ]", "", value)
        value = re.sub(r" +", "-", value.strip())
        duplicate_index = occurrences.get(value, 0)
        occurrences[value] = duplicate_index + 1
        anchors.add(value if duplicate_index == 0 else f"{value}-{duplicate_index}")
    return anchors


for required in (ROOT / "README.md", ROOT / "CONTRIBUTING.md", QUESTION_BANK / "README.md"):
    if not required.is_file():
        fail(required, "required file is missing")

for text_file in ROOT.rglob("*.txt"):
    if ".git" not in text_file.parts:
        fail(text_file, "legacy text file must be migrated to Markdown")

for markdown in ROOT.rglob("*.md"):
    if ".git" in markdown.parts:
        continue

    data = markdown.read_bytes()
    if b"\r\n" in data or b"\r" in data:
        fail(markdown, "uses CRLF or CR line endings")

    text = data.decode("utf-8")
    heading_anchors = github_heading_anchors(text)
    fences = list(re.finditer(r"^```(?!`)([^\n]*)$", text, flags=re.MULTILINE))
    if len(fences) % 2:
        fail(markdown, "contains an unmatched fenced-code delimiter")
    else:
        for opening in fences[::2]:
            if not opening.group(1).strip():
                line_number = text.count("\n", 0, opening.start()) + 1
                fail(markdown, f"code fence near line {line_number} has no language identifier")

    for target in re.findall(r"!?(?:\[[^]]*\])\(([^)]+)\)", text):
        target = target.strip()
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        if target.startswith("#"):
            anchor = unquote(target[1:])
            if anchor not in heading_anchors:
                fail(markdown, f"broken heading link: {target}")
            continue
        relative_target = unquote(target.split("#", 1)[0])
        if relative_target and not (markdown.parent / relative_target).resolve().exists():
            fail(markdown, f"broken relative link: {target}")

    if QUESTION_BANK in markdown.parents and markdown.name != "README.md":
        lines = text.splitlines()
        if not lines or not lines[0].startswith("# "):
            fail(markdown, "must start with one level-one title")
        if "[Back to the question-bank index](../README.md)" not in text:
            fail(markdown, "missing question-bank index link")

        headings: dict[str, int] = {}
        for line_number, line in enumerate(lines, 1):
            if line.startswith(("## ", "### ")):
                normalized = re.sub(r"[^a-z0-9]+", " ", line.lstrip("# ").lower()).strip()
                if normalized in headings:
                    fail(
                        markdown,
                        f"duplicate heading at lines {headings[normalized]} and {line_number}",
                    )
                headings[normalized] = line_number

        empty_answer = re.search(
            r"\*\*(?:Answer|Answer framework)\*\*\s*(?=#{2,3}\s|\Z)",
            text,
        )
        if empty_answer:
            line_number = text.count("\n", 0, empty_answer.start()) + 1
            fail(markdown, f"empty answer near line {line_number}")

        h2_matches = list(re.finditer(r"^## (.+)$", text, flags=re.MULTILINE))
        for index, heading in enumerate(h2_matches):
            title = heading.group(1).strip()
            if title in SECTION_HEADINGS:
                continue
            end = h2_matches[index + 1].start() if index + 1 < len(h2_matches) else len(text)
            section = text[heading.end():end]
            if "**Answer**" not in section and "**Answer framework**" not in section:
                line_number = text.count("\n", 0, heading.start()) + 1
                fail(markdown, f"question heading near line {line_number} has no answer marker")

if errors:
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    print(f"Validation failed with {len(errors)} error(s).", file=sys.stderr)
    raise SystemExit(1)

topic_count = sum(1 for path in QUESTION_BANK.rglob("*.md") if path.name != "README.md")
print(f"Validation passed for {topic_count} topic files.")
