import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# ── 1. Remove --06 from Variation B group selector ──────────────
old_sel = '.card-cover--03, .card-cover--09, .card-cover--06 {'
new_sel = '.card-cover--03, .card-cover--09 {'
if old_sel in content:
    content = content.replace(old_sel, new_sel, 1)
    sys.stdout.buffer.write(b'  OK: removed --06 from Variation B selector\n')
else:
    sys.stdout.buffer.write(b'  MISS: Variation B selector\n')

# ── 2. Insert card-cover--06 block after the Variation B block ──
# Anchor: find the end of Variation B's closing comment block
# and insert before Variation C
ANCHOR = '/* ── VARIATION C'
if ANCHOR not in content:
    sys.stdout.buffer.write(b'  MISS: anchor for Variation C\n')
else:
    NEW_BLOCK = """/* ── CARD 08 SoundClimbing — Lavender × Peach ─────────────────
       Base: Morandi lavender  #9690A8  (cool, grey-violet)
       Centre: deep warm peach, radiates outward getting lighter
       Deep coral-peach core → soft peach mid → pale cream edge   */
    .card-cover--06 {
      --title-color: rgba(255,250,245,.90);
      --num-color:   rgba(255,250,245,1);
      background:
        /* Primary — deep peach core fading radially to light */
        radial-gradient(ellipse 90% 94% at 50% 38%,
          rgba(230,130,80,.68)  0%,
          rgba(240,162,112,.48) 10%,
          rgba(248,188,148,.26) 24%,
          rgba(252,210,172,.10) 42%,
          rgba(254,225,195,.04) 58%,
          rgba(255,238,218,.01) 72%,
          transparent           84%
        ),
        /* Whisper bloom — outer peachy haze */
        radial-gradient(ellipse 100% 100% at 50% 40%,
          rgba(245,185,138,.12) 0%,
          rgba(248,205,165,.05) 48%,
          rgba(252,220,185,.01) 68%,
          transparent           82%
        ),
        /* Morandi lavender base */
        linear-gradient(148deg, #9690A8, #9E98B0 55%, #928CA4);
    }

    """
    content = content.replace(ANCHOR, NEW_BLOCK + ANCHOR, 1)
    sys.stdout.buffer.write(b'  OK: inserted --06 lavender-peach block\n')

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

checks = [
    ('.card-cover--03, .card-cover--09 {' in content, '--06 removed from Variation B'),
    ('.card-cover--06 {' in content, 'standalone --06 rule'),
    ('#9690A8' in content, 'lavender base'),
    ('rgba(230,130,80' in content, 'deep peach core'),
    ('rgba(252,210,172' in content, 'pale peach mid'),
]
for ok, label in checks:
    sys.stdout.buffer.write(f'  {"OK" if ok else "FAIL"}: {label}\n'.encode())

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
