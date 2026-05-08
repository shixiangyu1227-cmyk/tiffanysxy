import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
original = content

# ─────────────────────────────────────────────────────────────────
# Replace CSS radial-gradient backgrounds with cropped image tiles
# from refer.png. Each design gets its own JPEG crop.
# --title-color / --num-color are kept for text legibility.
# ─────────────────────────────────────────────────────────────────

# ── Design A ─────────────────────────────────────────────────────
OLD_A = """    .card-cover--04, .card-cover--08 {
      --title-color: rgba(32,54,68,.80);
      --num-color:   rgba(32,54,68,1);
      background:
        radial-gradient(ellipse 96% 100% at 50% 40%,
          rgba(246,202,108,.82)  0%,
          rgba(246,212,132,.62)  10%,
          rgba(246,222,158,.40)  24%,
          rgba(246,230,180,.22)  40%,
          rgba(246,235,196,.10)  56%,
          rgba(246,238,208,.04)  70%,
          rgba(246,240,214,.01)  82%,
          transparent            92%
        ),
        radial-gradient(ellipse 100% 100% at 50% 42%,
          rgba(244,198,90,.18)   0%,
          rgba(244,212,118,.07)  50%,
          transparent            80%
        ),
        linear-gradient(150deg, #A9CDD9, #B3D5E4 52%, #A5C9D5);
    }"""

NEW_A = """    .card-cover--04, .card-cover--08 {
      --title-color: rgba(32,54,68,.80);
      --num-color:   rgba(32,54,68,1);
      background: url('cover_a.jpg') center/cover no-repeat;
    }"""

# ── Design B ─────────────────────────────────────────────────────
OLD_B = """    .card-cover--01, .card-cover--09, .card-cover--05 {
      --title-color: rgba(52,42,72,.78);
      --num-color:   rgba(52,42,72,1);
      background:
        radial-gradient(ellipse 96% 100% at 50% 46%,
          rgba(240,158,148,.78)  0%,
          rgba(240,172,164,.58)  10%,
          rgba(240,188,182,.38)  24%,
          rgba(240,204,200,.20)  40%,
          rgba(240,215,212,.10)  56%,
          rgba(240,222,220,.04)  70%,
          rgba(240,228,226,.01)  82%,
          transparent            92%
        ),
        radial-gradient(ellipse 100% 100% at 50% 48%,
          rgba(238,146,136,.16)  0%,
          rgba(238,166,158,.06)  50%,
          transparent            80%
        ),
        linear-gradient(150deg, #BCB8CC, #C4BED4 52%, #B8B4C8);
    }"""

NEW_B = """    .card-cover--01, .card-cover--09, .card-cover--05 {
      --title-color: rgba(52,42,72,.78);
      --num-color:   rgba(52,42,72,1);
      background: url('cover_b.jpg') center/cover no-repeat;
    }"""

# ── Design C ─────────────────────────────────────────────────────
OLD_C = """    .card-cover--07, .card-cover--03, .card-cover--06, .card-cover--02 {
      --title-color: rgba(40,52,20,.80);
      --num-color:   rgba(40,52,20,1);
      background:
        radial-gradient(ellipse 96% 100% at 50% 58%,
          rgba(108,132,55,.80)   0%,
          rgba(118,142,65,.60)   10%,
          rgba(130,154,76,.40)   26%,
          rgba(144,166,90,.22)   42%,
          rgba(155,176,102,.10)  58%,
          rgba(165,184,112,.04)  72%,
          rgba(174,190,120,.01)  84%,
          transparent            94%
        ),
        radial-gradient(ellipse 100% 100% at 50% 60%,
          rgba(96,120,46,.18)    0%,
          rgba(108,132,55,.07)   52%,
          transparent            80%
        ),
        linear-gradient(150deg, #BABF95, #C0C49B 52%, #B6BB91);
    }"""

NEW_C = """    .card-cover--07, .card-cover--03, .card-cover--06, .card-cover--02 {
      --title-color: rgba(40,52,20,.80);
      --num-color:   rgba(40,52,20,1);
      background: url('cover_c.jpg') center/cover no-repeat;
    }"""

for old, new, label in [
    (OLD_A, NEW_A, 'A → cover_a.jpg'),
    (OLD_B, NEW_B, 'B → cover_b.jpg'),
    (OLD_C, NEW_C, 'C → cover_c.jpg'),
]:
    if old in content:
        content = content.replace(old, new, 1)
        sys.stdout.buffer.write(f'  OK: {label}\n'.encode())
    else:
        sys.stdout.buffer.write(f'  MISS: {label}\n'.encode())

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

checks = [
    ("url('cover_a.jpg')" in content, 'A uses image'),
    ("url('cover_b.jpg')" in content, 'B uses image'),
    ("url('cover_c.jpg')" in content, 'C uses image'),
    ('radial-gradient' not in content.split('CARD COVER')[1].split('TOUCH')[0], 'no leftover gradients'),
]
for ok, label in checks:
    sys.stdout.buffer.write(f'  {"OK" if ok else "FAIL"}: {label}\n'.encode())

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
