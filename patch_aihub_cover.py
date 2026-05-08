import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
original = content

# Split --05 (AIhub) out of the shared 02cover group and give it the watercolor image.
OLD = """    .card-cover--03, .card-cover--05, .card-cover--06 {
      --title-color: rgba(38,48,18,.80);
      --num-color:   rgba(38,48,18,1);
      background: url('02cover.jpg') center/cover no-repeat;
    }"""

NEW = """    .card-cover--03, .card-cover--06 {
      --title-color: rgba(38,48,18,.80);
      --num-color:   rgba(38,48,18,1);
      background: url('02cover.jpg') center/cover no-repeat;
    }
    .card-cover--05 {
      --title-color: rgba(255,252,255,.90);
      --num-color:   rgba(255,252,255,1);
      background: url('cover_aihub.jpg') center/cover no-repeat;
    }"""

if OLD in content:
    content = content.replace(OLD, NEW, 1)
    sys.stdout.buffer.write(b'  OK: --05 split out with watercolor\n')
else:
    sys.stdout.buffer.write(b'  MISS: group selector not found\n')

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

checks = [
    ('.card-cover--03, .card-cover--06' in content,      '--05 removed from group'),
    ('.card-cover--05 {' in content,                     '--05 standalone rule'),
    ("url('cover_aihub.jpg')" in content,                'watercolor image referenced'),
    ("url('02cover.jpg')" in content,                    '02cover.jpg still used for --03 --06'),
]
for ok, label in checks:
    sys.stdout.buffer.write(f'  {"OK" if ok else "FAIL"}: {label}\n'.encode())

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
