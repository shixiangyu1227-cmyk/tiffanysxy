import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# 1. GameFlow card: change card-cover--06 to card-cover--03
content = content.replace('card-cover card-cover--06', 'card-cover card-cover--03', 1)

# 2. Hide all .cover-deco SVG decorations
content = content.replace(
    '.cover-deco { position: absolute; pointer-events: none; }',
    '.cover-deco { display: none; }'
)

# 3. Hide .cover-sub subtitle
old_sub = '    .cover-sub {\n      font-family: var(--font-san); font-size: .62rem;\n      font-weight: 400; line-height: 1.5; color: var(--cs);\n    }'
new_sub = '    .cover-sub { display: none; }'
content = content.replace(old_sub, new_sub)

# 4. Center .cover-text in the middle
old_text = '    .cover-text { position: absolute; bottom: 1rem; left: 1rem; right: 1rem; }'
new_text = '    .cover-text { position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 1.5rem; }'
content = content.replace(old_text, new_text)

# 5. Maximize .cover-title font size + remove margin-bottom
old_title = '    .cover-title {\n      font-family: var(--font-ser); font-size: 1.05rem; font-weight: 400;\n      line-height: 1.15; margin-bottom: .22rem; color: var(--ct);\n    }'
new_title = '    .cover-title {\n      font-family: var(--font-ser); font-size: 1.85rem; font-weight: 400;\n      line-height: 1.1; color: var(--ct);\n    }'
content = content.replace(old_title, new_title)

# 6. Make .cover-num 5x larger: .58rem * 5 = 2.9rem
old_num = '    .cover-num {\n      position: absolute; top: .68rem; left: .85rem;\n      font-family: var(--font-mon); font-size: .58rem;\n      letter-spacing: .2em; color: var(--cn);\n    }'
new_num = '    .cover-num {\n      position: absolute; top: .68rem; left: .85rem;\n      font-family: var(--font-mon); font-size: 2.9rem;\n      letter-spacing: .04em; line-height: 1; color: var(--cn);\n    }'
content = content.replace(old_num, new_num)

changed = content != original
sys.stdout.buffer.write(b'Changed: ' + str(changed).encode() + b'\n')

checks = [
    ('card-cover card-cover--03' in content, 'GameFlow card-cover--03'),
    ('.cover-deco { display: none; }' in content, 'cover-deco hidden'),
    ('.cover-sub { display: none; }' in content, 'cover-sub hidden'),
    ('justify-content: center' in content, 'cover-text centered'),
    ('font-size: 1.85rem' in content, 'cover-title large'),
    ('font-size: 2.9rem' in content, 'cover-num large'),
]
for ok, label in checks:
    status = b'OK' if ok else b'FAIL'
    sys.stdout.buffer.write(b'  ' + status + b': ' + label.encode() + b'\n')

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
else:
    sys.stdout.buffer.write(b'No changes - strings may not match exactly.\n')
