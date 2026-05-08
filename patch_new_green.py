import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
original = content

# Replace the shared B block with 3 individual blocks,
# each using a different crop from new cover.png.
# --03 → card 02 → cover_b1.jpg (top card)
# --01 → card 04 → cover_b2.jpg (bottom-left)
# --02 → card 09 → cover_b3.jpg (bottom-right)
# Text colors updated for dark-green backgrounds.

OLD = """    .card-cover--03, .card-cover--01, .card-cover--02 {
      --title-color: rgba(52,42,72,.78);
      --num-color:   rgba(52,42,72,1);
      background: url('cover_b.jpg') center/cover no-repeat;
    }"""

NEW = """    .card-cover--03 {
      --title-color: rgba(36,52,28,.82);
      --num-color:   rgba(36,52,28,1);
      background: url('cover_b1.jpg') center/cover no-repeat;
    }
    .card-cover--01 {
      --title-color: rgba(36,52,28,.82);
      --num-color:   rgba(36,52,28,1);
      background: url('cover_b2.jpg') center/cover no-repeat;
    }
    .card-cover--02 {
      --title-color: rgba(36,52,28,.82);
      --num-color:   rgba(36,52,28,1);
      background: url('cover_b3.jpg') center/cover no-repeat;
    }"""

if OLD in content:
    content = content.replace(OLD, NEW, 1)
    sys.stdout.buffer.write(b'  OK: B block split into 3\n')
else:
    sys.stdout.buffer.write(b'  MISS: B block\n')

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

checks = [
    ("url('cover_b1.jpg')" in content, '--03 → cover_b1'),
    ("url('cover_b2.jpg')" in content, '--01 → cover_b2'),
    ("url('cover_b3.jpg')" in content, '--02 → cover_b3'),
    ("url('cover_b.jpg')" not in content, 'old cover_b.jpg removed'),
]
for ok, label in checks:
    sys.stdout.buffer.write(f'  {"OK" if ok else "FAIL"}: {label}\n'.encode())

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
