import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# ─────────────────────────────────────────────────────────────────
# CSS class → card → variation mapping:
#
#   --07  Card 01 SmartHire    → A Nocturne  (dark forest × warm chartreuse)
#   --03  Card 02 GameFlow     → B Velvet    (warm olive  × cool silver-mint)
#   --04  Card 03 Kanelär      → C Morning   (pale sage   × warm ivory)
#   --01  Card 04 Kaleido      → A Nocturne
#   --09  Card 05 KANKAN       → B Velvet
#   --05  Card 06 AIHub        → C Morning
#   --08  Card 07 KörkortHub   → A Nocturne
#   --06  Card 08 SoundClimbing→ B Velvet
#   --02  Card 09 Social VR    → C Morning
#
# Grid:  A | B | C
#        A | B | C
#        A | B | C
#
# Soft-focus (柔焦) technique:
#   6-stop radial gradient with very gradual opacity decay
#   + secondary bloom layer offset slightly
#   No hard edges — everything dissolves into base color
# ─────────────────────────────────────────────────────────────────
CSS_START = '/* ─── CARD COVER'
CSS_END   = '/* ─── TOUCH / MOBILE'
start_idx = content.find(CSS_START)
end_idx   = content.find(CSS_END)
assert start_idx != -1 and end_idx != -1

NEW_CSS = """/* ─── CARD COVER — 弥散光 Diffused Light System ──────────────── */
    .card-cover {
      position: absolute; inset: 0;
      opacity: 1; pointer-events: none;
      transition: opacity .65s var(--ease);
      overflow: hidden;
    }
    .project-card:hover .card-cover { opacity: 0; }

    /* Floating lift */
    .project-thumb {
      box-shadow:
        0 1px 0 rgba(255,255,255,.72),
        0 5px 22px rgba(0,0,0,.12),
        0 2px 7px rgba(0,0,0,.08);
      position: relative;
    }

    /* All pseudo-elements and decoration cleared */
    .card-cover::before, .card-cover::after,
    .cover-inner::before, .cover-inner::after { display: none; }
    .cover-inner { position: absolute; inset: .72rem; }

    /* Number — serif, top-left, whisper opacity */
    .cover-num {
      position: absolute; top: .78rem; left: .88rem;
      font-family: var(--font-ser);
      font-size: 1.15rem; font-weight: 400;
      letter-spacing: .04em; line-height: 1;
      color: var(--num-color);
      opacity: .50;
    }

    /* Title — large, centred */
    .cover-text {
      position: absolute; inset: 0;
      display: flex; flex-direction: column;
      align-items: center; justify-content: center;
      text-align: center; padding: 1.6rem;
    }
    .cover-title {
      font-family: var(--font-ser);
      font-size: 2.2rem; font-weight: 400;
      line-height: 1.08; letter-spacing: .01em;
      color: var(--title-color);
    }
    .cover-sub  { display: none; }
    .cover-deco { display: none; }

    /* ── VARIATION A — Nocturne ────────────────────────────────────
       Outer: deep Morandi forest #1D2B1A (cool, dark)
       Center glow: warm chartreuse  rgb(202,222,128)
       Cold dark outer ↔ warm luminous center
       Text: light cream                                           */
    .card-cover--07, .card-cover--01, .card-cover--08 {
      --title-color: rgba(238,236,222,.90);
      --num-color:   rgba(238,236,222,1);
      background:
        /* Primary soft-focus glow — warm chartreuse centre */
        radial-gradient(ellipse 55% 62% at 50% 46%,
          rgba(202,222,128,.72) 0%,
          rgba(185,208,105,.50) 12%,
          rgba(162,188,78,.28)  28%,
          rgba(128,158,52,.10)  50%,
          rgba(92,122,34,.03)   66%,
          transparent           82%
        ),
        /* Secondary diffusion bloom — slightly offset */
        radial-gradient(ellipse 80% 76% at 52% 50%,
          rgba(178,205,95,.20)  0%,
          rgba(140,170,62,.09)  38%,
          rgba(90,130,38,.03)   60%,
          transparent           78%
        ),
        /* Dark Morandi forest base */
        linear-gradient(148deg, #1D2B1A, #232F1E 55%, #19261600);
    }

    /* ── VARIATION B — Velvet Moss ─────────────────────────────────
       Outer: warm Morandi olive  #586A44 (warm, mid)
       Center glow: cool silver-mint  rgb(190,228,200)
       Warm earthy outer ↔ cool luminous centre
       Text: light cream                                           */
    .card-cover--03, .card-cover--09, .card-cover--06 {
      --title-color: rgba(238,236,222,.90);
      --num-color:   rgba(238,236,222,1);
      background:
        /* Primary glow — cool silver-mint centre */
        radial-gradient(ellipse 55% 62% at 50% 46%,
          rgba(190,228,200,.68) 0%,
          rgba(165,215,178,.46) 12%,
          rgba(135,196,152,.24) 28%,
          rgba(100,168,118,.09) 50%,
          rgba(68,138,88,.03)   66%,
          transparent           82%
        ),
        /* Secondary bloom */
        radial-gradient(ellipse 78% 74% at 51% 48%,
          rgba(172,218,185,.18) 0%,
          rgba(125,180,140,.08) 40%,
          rgba(80,142,98,.02)   62%,
          transparent           78%
        ),
        /* Warm olive base */
        linear-gradient(145deg, #566840, #5E724A 55%, #52643E);
    }

    /* ── VARIATION C — Morning Veil ─────────────────────────────────
       Outer: pale cool Morandi sage  #B8C8AA
       Center glow: warm ivory-cream  rgb(240,244,222)
       Cool washed sage outer ↔ warm glowing ivory centre
       Text: dark olive (light bg)                                */
    .card-cover--04, .card-cover--05, .card-cover--02 {
      --title-color: rgba(42,56,30,.80);
      --num-color:   rgba(42,56,30,1);
      background:
        /* Primary glow — warm ivory-cream centre */
        radial-gradient(ellipse 55% 62% at 50% 46%,
          rgba(240,244,222,.85) 0%,
          rgba(225,234,200,.62) 12%,
          rgba(205,218,172,.34) 28%,
          rgba(180,198,142,.14) 50%,
          rgba(155,176,112,.04) 66%,
          transparent           82%
        ),
        /* Secondary diffusion */
        radial-gradient(ellipse 76% 72% at 50% 48%,
          rgba(230,238,208,.38) 0%,
          rgba(200,214,170,.16) 40%,
          rgba(168,186,132,.04) 62%,
          transparent           76%
        ),
        /* Pale Morandi sage base */
        linear-gradient(152deg, #B6C6A8, #C2D0B2 50%, #B2C4A4);
    }

    """

content = content[:start_idx] + NEW_CSS + content[end_idx:]

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

checks = [
    ('弥散光' in content, 'diffused light comment'),
    ('radial-gradient(ellipse 55% 62%' in content, '6-stop soft-focus gradient'),
    ('rgba(202,222,128' in content, 'Nocturne warm chartreuse center'),
    ('rgba(190,228,200' in content, 'Velvet cool mint center'),
    ('rgba(240,244,222' in content, 'Morning ivory center'),
    ('#1D2B1A' in content, 'Nocturne dark forest base'),
    ('#566840' in content, 'Velvet olive base'),
    ('#B6C6A8' in content, 'Morning pale sage base'),
    ('var(--title-color)' in content, 'per-variation text color'),
    ('display: none' in content and 'cover-deco' in content, 'deco hidden'),
    ('backdrop-filter' not in content, 'no backdrop-filter (pure gradient)'),
]
for ok, label in checks:
    sys.stdout.buffer.write(f'  {"OK" if ok else "FAIL"}: {label}\n'.encode())

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
