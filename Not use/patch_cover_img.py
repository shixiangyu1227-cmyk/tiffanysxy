import re, sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
original = content

# ── 1. Separate --08 (KörkortHub / card07) from the 01cover group ──
# Old: --07, --01, --08 all share 01cover.jpg
# New: --07, --01 keep 01cover.jpg; --08 gets kort.png with light text

old_rule = """    /* ── 01cover — cards 01 04 07 ───────────────────────────────── */
    .card-cover--07, .card-cover--01, .card-cover--08 {
      --title-color: rgba(38,48,18,.84);
      --num-color:   rgba(38,48,18,1);
      background: url('01cover.jpg') center/cover no-repeat;
    }"""

new_rule = """    /* ── 01cover — cards 01 04 ─────────────────────────────────── */
    .card-cover--07, .card-cover--01 {
      --title-color: rgba(38,48,18,.84);
      --num-color:   rgba(38,48,18,1);
      background: url('01cover.jpg') center/cover no-repeat;
    }
    /* ── kort.png — card 07 (KörkortHub) ───────────────────────── */
    .card-cover--08 {
      --title-color: rgba(235,245,255,.92);
      --num-color:   rgba(235,245,255,1);
      background: url('kort.png') center/cover no-repeat;
    }"""

if old_rule in content:
    content = content.replace(old_rule, new_rule, 1)
    sys.stdout.buffer.write(b'  OK: --08 split to kort.png\n')
else:
    sys.stdout.buffer.write(b'  MISS: 01cover group rule\n')

# ── 2. Update More Work card: replace SVG scene with C1.png bg image ─
# Add background to .more-work-card CSS rule
old_mwc_css = """    .more-work-card {
      display: none;
      position: relative;
      overflow: hidden;
      cursor: none;
      min-height: 220px;
      transition: transform .4s var(--ease);
    }"""

new_mwc_css = """    .more-work-card {
      display: none;
      position: relative;
      overflow: hidden;
      cursor: none;
      min-height: 220px;
      background: url('C1.png') center/cover no-repeat;
      transition: transform .4s var(--ease);
    }"""

if old_mwc_css in content:
    content = content.replace(old_mwc_css, new_mwc_css, 1)
    sys.stdout.buffer.write(b'  OK: more-work-card bg set to C1.png\n')
else:
    sys.stdout.buffer.write(b'  MISS: .more-work-card CSS\n')

# ── 3. Remove the <svg class="mwc-scene"> block from the HTML ────────
# Keep only the .mwc-content text overlay
svg_pat = re.compile(
    r'\s*<!-- Scenic SVG.*?</svg>\s*\n',
    re.S
)
result = svg_pat.sub('\n        ', content, count=1)
if result != content:
    content = result
    sys.stdout.buffer.write(b'  OK: SVG scene removed from HTML\n')
else:
    sys.stdout.buffer.write(b'  MISS: SVG scene pattern\n')

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
