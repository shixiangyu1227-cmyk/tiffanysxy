import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
original = content

# ─────────────────────────────────────────────────────────────────
# 01→绿C  02→紫B  03→蓝A  04→紫B  05→蓝A  06→绿C
# 07→蓝A  08→绿C  09→紫B
#
# Card→CSS:  01=--07  02=--03  03=--04  04=--01  05=--09
#            06=--05  07=--08  08=--06  09=--02
#
# New groups:
#   A (Blue  / cover_a.jpg): --04  --09  --08   (cards 03 05 07)
#   B (Purple/ cover_b.jpg): --03  --01  --02   (cards 02 04 09)
#   C (Green / cover_c.jpg): --07  --05  --06   (cards 01 06 08)
# ─────────────────────────────────────────────────────────────────

replacements = [
    # A selector
    (
        '    .card-cover--04, .card-cover--08 {',
        '    .card-cover--04, .card-cover--09, .card-cover--08 {'
    ),
    # B selector
    (
        '    .card-cover--01, .card-cover--09, .card-cover--05 {',
        '    .card-cover--03, .card-cover--01, .card-cover--02 {'
    ),
    # C selector
    (
        '    .card-cover--07, .card-cover--03, .card-cover--06, .card-cover--02 {',
        '    .card-cover--07, .card-cover--05, .card-cover--06 {'
    ),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new, 1)
        sys.stdout.buffer.write(f'  OK: {old.strip()[:60]}\n'.encode())
    else:
        sys.stdout.buffer.write(f'  MISS: {old.strip()[:60]}\n'.encode())

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

checks = [
    ('.card-cover--04, .card-cover--09, .card-cover--08' in content, 'A: cards 03+05+07'),
    ('.card-cover--03, .card-cover--01, .card-cover--02' in content, 'B: cards 02+04+09'),
    ('.card-cover--07, .card-cover--05, .card-cover--06' in content, 'C: cards 01+06+08'),
]
for ok, label in checks:
    sys.stdout.buffer.write(f'  {"OK" if ok else "FAIL"}: {label}\n'.encode())

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
