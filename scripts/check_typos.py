#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CH_DIR = ROOT / 'src/novel'

# Bracket/quote pairs common in zh text
PAIRS = [
    ('(', ')'),
    ('（', '）'),
    ('[', ']'),
    ('【', '】'),
    ('{', '}'),
    ('《', '》'),
    ('「', '」'),
    ('『', '』'),
    ('“', '”'),
    ('‘', '’'),
]

punct_repeat_re = re.compile(r'[。．，、？！；：…—\-·,\.!\?;:]{3,}')
latin_block_re = re.compile(r'[A-Za-z]{6,}')
rep_char_re = re.compile(r'(.)\1{4,}')  # 5+ same chars
replacement_char_re = re.compile(r'\uFFFD|�')


def check_brackets(line: str):
    issues = []
    for l, r in PAIRS:
        cL = line.count(l)
        cR = line.count(r)
        if cL != cR:
            # allow cases like ellipsis in title where one appears; still flag
            issues.append(f'brackets-unbalanced {l}{r} {cL}!={cR}')
    return issues


def scan_file(path: Path):
    probs = []
    with path.open('r', encoding='utf-8', errors='ignore') as f:
        for i, raw in enumerate(f, start=1):
            line = raw.rstrip('\n')
            # skip markdown heading markers when blank
            if not line.strip():
                continue
            local = []
            local += check_brackets(line)
            if punct_repeat_re.search(line):
                local.append('punctuation-repeat')
            if latin_block_re.search(line):
                local.append('long-latin-word')
            if rep_char_re.search(line):
                local.append('repeat-char-5+')
            if replacement_char_re.search(line):
                local.append('unicode-replacement-char')
            # ASCII quotes inside CJK-heavy line
            if '"' in line and re.search(r'[\u4e00-\u9fff]', line):
                local.append('ascii-quote-in-cjk')
            if local:
                probs.append((i, line, local))
    return probs


def main():
    if not CH_DIR.exists():
        print('Novel chapter directory not found:', CH_DIR, file=sys.stderr)
        sys.exit(1)
    files = sorted(CH_DIR.glob('chapter-*.md'))
    total = 0
    flagged = 0
    report_lines = []
    for p in files:
        total += 1
        probs = scan_file(p)
        if probs:
            flagged += 1
            report_lines.append(f'== {p.name} ({len(probs)} lines) ==')
            # cap per file entries
            for i, (ln, text, tags) in enumerate(probs[:8], start=1):
                snippet = text.strip()
                if len(snippet) > 120:
                    snippet = snippet[:117] + '…'
                report_lines.append(f'  L{ln}: [{",".join(tags)}] {snippet}')
    print(f'Checked {total} files; {flagged} files had potential issues.')
    print('\n'.join(report_lines))


if __name__ == '__main__':
    main()

