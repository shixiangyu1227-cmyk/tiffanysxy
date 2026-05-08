import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
original = content

# ─────────────────────────────────────────────────────────────────
# Color-match to refer.png image (Image #4):
#
# A (Sky x Amber):
#   - Core: orange-amber rgb(242,185,58) → golden-warm rgb(246,202,108)  [lighter, less orange]
#   - Base: #B3D4DF → #A9CDD9  [lighter, more saturated sky blue]
#
# B (Lavender x Coral):
#   - Core: coral-orange rgb(235,125,108) → rose-salmon rgb(240,158,148)  [softer, pinker]
#   - Glow position: 50% 40% → 50% 46%  [more centered vertically]
#   - Base: #BBB7CC → #BCB8CC  [minimal adjust]
#
# C (Sage x Forest):
#   - Core: rgb(95,118,44) → rgb(108,132,55)  [slightly lighter, less harsh]
#   - Base: keep
# ─────────────────────────────────────────────────────────────────

OLD_A = """        radial-gradient(ellipse 96% 100% at 50% 40%,
          rgba(242,185,58,.70)  0%,
          rgba(244,200,88,.54)  10%,
          rgba(244,215,120,.36) 24%,
          rgba(244,228,158,.20) 40%,
          rgba(244,235,178,.10) 56%,
          rgba(245,240,200,.04) 70%,
          rgba(245,242,212,.01) 82%,
          transparent           92%
        ),
        radial-gradient(ellipse 100% 100% at 50% 42%,
          rgba(238,176,46,.13)  0%,
          rgba(240,198,78,.05)  50%,
          transparent           80%
        ),
        linear-gradient(150deg, #B3D4DF, #BBD9E6 52%, #AFD0DB);"""

NEW_A = """        radial-gradient(ellipse 96% 100% at 50% 40%,
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
        linear-gradient(150deg, #A9CDD9, #B3D5E4 52%, #A5C9D5);"""

OLD_B = """        radial-gradient(ellipse 96% 100% at 50% 40%,
          rgba(235,125,108,.70) 0%,
          rgba(238,148,132,.54) 10%,
          rgba(238,172,160,.36) 24%,
          rgba(237,198,190,.20) 40%,
          rgba(237,213,208,.10) 56%,
          rgba(238,224,220,.04) 70%,
          rgba(238,230,226,.01) 82%,
          transparent           92%
        ),
        radial-gradient(ellipse 100% 100% at 50% 42%,
          rgba(228,112,95,.13)  0%,
          rgba(232,142,126,.05) 50%,
          transparent           80%
        ),
        linear-gradient(150deg, #BBB7CC, #C3BDD4 52%, #B7B3C8);"""

NEW_B = """        radial-gradient(ellipse 96% 100% at 50% 46%,
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
        linear-gradient(150deg, #BCB8CC, #C4BED4 52%, #B8B4C8);"""

OLD_C = """        radial-gradient(ellipse 96% 100% at 50% 58%,
          rgba(95,118,44,.72)   0%,
          rgba(108,132,54,.56)  10%,
          rgba(122,148,65,.36)  26%,
          rgba(138,162,78,.20)  42%,
          rgba(150,172,88,.10)  58%,
          rgba(162,182,98,.04)  72%,
          rgba(172,190,108,.01) 84%,
          transparent           94%
        ),
        radial-gradient(ellipse 100% 100% at 50% 60%,
          rgba(85,108,38,.14)   0%,
          rgba(105,128,50,.05)  52%,
          transparent           80%
        ),
        linear-gradient(150deg, #BABF94, #C0C49A 52%, #B6BB90);"""

NEW_C = """        radial-gradient(ellipse 96% 100% at 50% 58%,
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
        linear-gradient(150deg, #BABF95, #C0C49B 52%, #B6BB91);"""

for old, new, label in [
    (OLD_A, NEW_A, 'A: golden amber core + lighter sky base'),
    (OLD_B, NEW_B, 'B: rose-salmon core + centered glow'),
    (OLD_C, NEW_C, 'C: lighter forest green core'),
]:
    if old in content:
        content = content.replace(old, new, 1)
        sys.stdout.buffer.write(f'  OK: {label}\n'.encode())
    else:
        sys.stdout.buffer.write(f'  MISS: {label}\n'.encode())

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

checks = [
    ('rgba(246,202,108' in content,  'A golden core'),
    ('#A9CDD9' in content,           'A sky blue base'),
    ('rgba(240,158,148' in content,  'B rose-salmon core'),
    ('50% 46%' in content,           'B glow centered'),
    ('rgba(108,132,55' in content,   'C lighter forest core'),
]
for ok, label in checks:
    sys.stdout.buffer.write(f'  {"OK" if ok else "FAIL"}: {label}\n'.encode())

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
