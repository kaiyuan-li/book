#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
NOVEL_DIR = ROOT / 'src' / 'novel'
SUMMARY = ROOT / 'src' / 'SUMMARY.md'

WATERMARK_PAT = re.compile(r'(奇.?书.?网|w!w!w|QiShu)', re.IGNORECASE)
NOTE_PAT = re.compile(r'(最后那句话看不清楚|用户上传之内容开始)')

def fix_title(title: str) -> str:
    # Normalize ASCII parens to full-width in title only
    t = title
    if t.startswith('# '):
        t = t.replace('(', '（').replace(')', '）')
        # Ensure （上/中/下） closed
        for part in ('（上', '（中', '（下'):
            if part in t and '）' not in t[t.find(part):]:
                t = t + '）'
    return t

def normalize_file(p: Path) -> bool:
    changed = False
    lines = p.read_text(encoding='utf-8', errors='replace').splitlines()
    out = []
    for i, line in enumerate(lines):
        orig = line
        if i == 0:  # title
            line = fix_title(line)
        # Replace mistaken name
        line = line.replace('甄环', '甄嬛')
        # Fix ASCII quote after period: 。" -> .”
        line = line.replace('。"', '。”')
        # Drop known watermark or reader notes lines
        if WATERMARK_PAT.search(line) or NOTE_PAT.search(line):
            changed = True
            continue
        if line != orig:
            changed = True
        out.append(line)
    if changed:
        Path(p).write_text('\n'.join(out) + '\n', encoding='utf-8')
    return changed

def normalize_summary(p: Path) -> bool:
    text = p.read_text(encoding='utf-8')
    orig_text = text
    text = text.replace('甄环', '甄嬛')

    def fix_bracket_text(match: re.Match) -> str:
        inner = match.group(1)
        fixed = inner.replace('(', '（').replace(')', '）')
        for part in ('（上', '（中', '（下'):
            if part in fixed and '）' not in fixed[fixed.find(part):]:
                fixed = fixed + '）'
        return '[' + fixed + ']'

    # Only mutate the display text between [..] leaving (...url) untouched
    text = re.sub(r'\[([^\]]+)\]', fix_bracket_text, text)

    if text != orig_text:
        p.write_text(text, encoding='utf-8')
        return True
    return False

def main():
    changed = 0
    for md in sorted(NOVEL_DIR.glob('chapter-*.md')):
        if normalize_file(md):
            changed += 1
    schg = normalize_summary(SUMMARY)
    print(f'Normalized {changed} chapter files; summary changed={schg}')

if __name__ == '__main__':
    main()

