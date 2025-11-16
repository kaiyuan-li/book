#!/usr/bin/env python3
import re
from pathlib import Path
import sys

CHAPTER_RE = re.compile(r"^\s*(第[一二三四五六七八九十百千〇零0-9]+[章回卷].*)\s*$")


def split_novel(src_path: Path, out_dir: Path):
    text = src_path.read_text(encoding="utf-8", errors="replace").splitlines()

    chapters = []  # list of (title, lines)
    cur_title = None
    cur_lines = []

    for line in text:
        m = CHAPTER_RE.match(line)
        if m:
            # flush previous
            if cur_title is not None:
                chapters.append((cur_title, cur_lines))
            cur_title = m.group(1).strip()
            cur_lines = []
        else:
            # skip leading boilerplate before first chapter
            if cur_title is None:
                continue
            # Normalize whitespace: remove leading spaces to avoid Markdown code blocks
            normalized = line.replace("\t", "    ").rstrip("\r").strip()
            # Skip purely empty lines; we insert blank lines between paragraphs later
            if normalized == "":
                continue
            cur_lines.append(normalized)

    if cur_title is not None:
        chapters.append((cur_title, cur_lines))

    if not chapters:
        raise SystemExit("No chapters detected. Adjust CHAPTER_RE.")

    out_dir.mkdir(parents=True, exist_ok=True)

    # Write README.md
    readme = out_dir / "README.md"
    readme.write_text("# 甄嬛传\n\n本目录包含自动拆分的章节。\n\n", encoding="utf-8")

    # Write chapter files
    written = []
    for idx, (title, lines) in enumerate(chapters, start=1):
        fname = out_dir / f"chapter-{idx:03d}.md"
        body = []
        body.append(f"# {title}")
        # Normalize empty lines and trim trailing whitespace
        for l in lines:
            body.append(l)
        content = "\n\n".join([body[0]] + body[1:]) + "\n"
        fname.write_text(content, encoding="utf-8")
        written.append((title, fname))

    return written


def update_summary(summary_path: Path, novel_dir: Path, chapters):
    summary_text = summary_path.read_text(encoding="utf-8")

    # Build Novel section
    lines = ["## Novel", "- [甄嬛传](novel/README.md)"]
    for title, path in chapters:
        rel = path.relative_to(summary_path.parent)
        lines.append(f"  - [{title}]({rel.as_posix()})")
    novel_block = "\n".join(lines) + "\n"

    # If a Novel section exists, replace it; otherwise append
    pattern = re.compile(r"^##\s+Novel[\s\S]*?(?=^##\s+|\Z)", re.MULTILINE)
    if pattern.search(summary_text):
        summary_text = pattern.sub(novel_block, summary_text)
    else:
        if not summary_text.endswith("\n"):
            summary_text += "\n"
        summary_text += "\n" + novel_block

    summary_path.write_text(summary_text, encoding="utf-8")


def main():
    repo_root = Path(__file__).resolve().parents[1]
    src_txt = repo_root / "src/novel/raw.txt"
    out_dir = repo_root / "src/novel"
    summary = repo_root / "src/SUMMARY.md"

    if not src_txt.exists():
        print(f"Source TXT not found: {src_txt}")
        sys.exit(1)
    if not summary.exists():
        print(f"SUMMARY.md not found: {summary}")
        sys.exit(1)

    chapters = split_novel(src_txt, out_dir)
    update_summary(summary, out_dir, chapters)
    print(f"Chapters written: {len(chapters)}")


if __name__ == "__main__":
    main()
