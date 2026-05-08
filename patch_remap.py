import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# ─────────────────────────────────────────────────────────────────
# Old → New selector mapping
# Card 07 (CSS --08) not mentioned → keep in Design A
#
# Old A: --07, --01, --08   New A: --04, --08
# Old B: --03, --09, --06   New B: --01, --09, --05
# Old C: --04, --05, --02   New C: --07, --03, --06, --02
# ─────────────────────────────────────────────────────────────────

replacements = [
    # Design A selector
    (
        '    .card-cover--07, .card-cover--01, .card-cover--08 {',
        '    .card-cover--04, .card-cover--08 {'
    ),
    # Design B selector
    (
        '    .card-cover--03, .card-cover--09, .card-cover--06 {',
        '    .card-cover--01, .card-cover--09, .card-cover--05 {'
    ),
    # Design C selector
    (
        '    .card-cover--04, .card-cover--05, .card-cover--02 {',
        '    .card-cover--07, .card-cover--03, .card-cover--06, .card-cover--02 {'
    ),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new, 1)
        sys.stdout.buffer.write(f'  OK: {old.strip()[:55]}\n'.encode('utf-8'))
    else:
        sys.stdout.buffer.write(f'  MISS: {old.strip()[:55]}\n'.encode('utf-8'))

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

checks = [
    ('.card-cover--04, .card-cover--08 {' in content,                          'A: cards 03+07'),
    ('.card-cover--01, .card-cover--09, .card-cover--05 {' in content,         'B: cards 04+05+06'),
    ('.card-cover--07, .card-cover--03, .card-cover--06, .card-cover--02 {' in content, 'C: cards 01+02+08+09'),
]
for ok, label in checks:
    sys.stdout.buffer.write(f'  {"OK" if ok else "FAIL"}: {label}\n'.encode())

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
