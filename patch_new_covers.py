import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
original = content

# Replace old cover file references and update text colors for olive-green palette

replacements = [
    # 01cover — cards 01 04 07 (CSS --07 --01 --08)
    (
        "      --title-color: rgba(28,42,68,.82);\n      --num-color:   rgba(28,42,68,1);\n      background: url('cover01.jpg') center/cover no-repeat;",
        "      --title-color: rgba(38,48,18,.84);\n      --num-color:   rgba(38,48,18,1);\n      background: url('01cover.jpg') center/cover no-repeat;"
    ),
    # 02cover — cards 02 05 08 (CSS --03 --05 --06)
    (
        "      --title-color: rgba(68,40,32,.82);\n      --num-color:   rgba(68,40,32,1);\n      background: url('cover02.jpg') center/cover no-repeat;",
        "      --title-color: rgba(38,48,18,.80);\n      --num-color:   rgba(38,48,18,1);\n      background: url('02cover.jpg') center/cover no-repeat;"
    ),
    # 03cover — cards 03 06 09 (CSS --04 --09 --02)
    (
        "      --title-color: rgba(232,242,228,.90);\n      --num-color:   rgba(232,242,228,1);\n      background: url('cover03.jpg') center/cover no-repeat;",
        "      --title-color: rgba(38,48,18,.84);\n      --num-color:   rgba(38,48,18,1);\n      background: url('03cover.jpg') center/cover no-repeat;"
    ),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new, 1)
        sys.stdout.buffer.write(b'  OK\n')
    else:
        sys.stdout.buffer.write(b'  MISS\n')

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

checks = [
    ("url('01cover.jpg')" in content, '01cover.jpg used'),
    ("url('02cover.jpg')" in content, '02cover.jpg used'),
    ("url('03cover.jpg')" in content, '03cover.jpg used'),
    ('cover01.jpg' not in content and 'cover02.jpg' not in content, 'old cover0x.jpg removed'),
]
for ok, label in checks:
    sys.stdout.buffer.write(f'  {"OK" if ok else "FAIL"}: {label}\n'.encode())

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
