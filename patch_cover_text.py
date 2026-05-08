import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
original = content

# 1. card-cover inset: 0 → -2px 0  (hide top/bottom image edge)
r1 = (
    '      position: absolute; inset: 0;\n      opacity: 1; pointer-events: none;',
    '      position: absolute; inset: -2px 0;\n      opacity: 1; pointer-events: none;'
)

# 2. cover-num font-size 1.15rem → 3.45rem  (3×)
r2 = (
    '      font-size: 1.15rem; font-weight: 400;\n      letter-spacing: .04em; line-height: 1;\n      color: var(--num-color); opacity: .48;',
    '      font-size: 3.45rem; font-weight: 400;\n      letter-spacing: .04em; line-height: 1;\n      color: var(--num-color); opacity: .48;'
)

# 3. cover-title: bigger (2.2rem → 3.4rem) + serif italic
r3 = (
    '      font-family: var(--font-ser);\n      font-size: 2.2rem; font-weight: 400;\n      line-height: 1.08; letter-spacing: .01em;\n      color: var(--title-color);',
    '      font-family: var(--font-ser);\n      font-size: 3.4rem; font-weight: 400; font-style: italic;\n      line-height: 1.08; letter-spacing: .01em;\n      color: var(--title-color);'
)

for old, new in [r1, r2, r3]:
    if old in content:
        content = content.replace(old, new, 1)
        sys.stdout.buffer.write(b'  OK\n')
    else:
        sys.stdout.buffer.write(b'  MISS\n')

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

checks = [
    ('inset: -2px 0' in content,    'cover inset -2px top/bottom'),
    ('font-size: 3.45rem' in content, 'num 3x larger'),
    ('font-size: 3.4rem' in content,  'title larger'),
    ('font-style: italic' in content,  'title italic'),
]
for ok, label in checks:
    sys.stdout.buffer.write(f'  {"OK" if ok else "FAIL"}: {label}\n'.encode())

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
