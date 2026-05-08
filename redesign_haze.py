import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# ─────────────────────────────────────────────────────────────────
# Refinements:
#  1. Gradient ellipse: 55%→ 90-95% — diffuses to 75-80% of frame
#  2. Center position: 50% 46% → 50% 38% — slightly high, more dynamic
#  3. Centre opacity: 0.72→ 0.60 — lighter, "soaking in" vs "pasted on"
#  4. Secondary bloom: 100%×100% whisper layer for outer haze
#  5. Base lightness raised + greyish Morandi tone added
#     A: #1D2B1A → #2C3E24   (L 13%→20%, more grey-olive)
#     B: #566840 → #6A7C58   (L 32%→42%, more grey-sage)
#     C: #B6C6A8 → #C0CAB4   (L 72%→74%, greyer / more Morandi)
#  6. Centre colors — purer, brighter, near-luminous
#     A: rgba(202,222,128) → rgba(228,248,162)  (brighter, less saturated)
#     B: rgba(190,228,200) → rgba(208,242,215)  (purer, cooler mint)
#     C: rgba(240,244,222) → rgba(248,252,235)  (near-white, luminous)
# ─────────────────────────────────────────────────────────────────
CSS_START = '/* ─── CARD COVER'
CSS_END   = '/* ─── TOUCH / MOBILE'
start_idx = content.find(CSS_START)
end_idx   = content.find(CSS_END)
assert start_idx != -1 and end_idx != -1

NEW_CSS = """/* ─── CARD COVER — 弥散光 Diffused Haze ──────────────────────── */
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

    /* All decorative lines cleared */
    .card-cover::before, .card-cover::after,
    .cover-inner::before, .cover-inner::after { display: none; }
    .cover-inner { position: absolute; inset: .72rem; }

    /* Number — serif, top-left */
    .cover-num {
      position: absolute; top: .78rem; left: .88rem;
      font-family: var(--font-ser);
      font-size: 1.15rem; font-weight: 400;
      letter-spacing: .04em; line-height: 1;
      color: var(--num-color); opacity: .48;
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
       Base: Morandi dark olive-grey  #2C3E24  (L 20%, greyed)
       Centre: luminous warm chartreuse  rgba(228,248,162)
       Glow at 50% 38% (slightly above centre)
       Diffuses to ~80% of frame — colour "soaks in"             */
    .card-cover--07, .card-cover--01, .card-cover--08 {
      --title-color: rgba(238,236,222,.90);
      --num-color:   rgba(238,236,222,1);
      background:
        /* Primary glow — 7 stops, 90% ellipse, fades to zero at 82% */
        radial-gradient(ellipse 90% 94% at 50% 38%,
          rgba(228,248,162,.60) 0%,
          rgba(215,240,142,.42) 10%,
          rgba(195,228,115,.24) 24%,
          rgba(168,208,84,.10)  42%,
          rgba(135,178,55,.04)  58%,
          rgba(100,145,30,.01)  72%,
          transparent           84%
        ),
        /* Whisper bloom — fills outer haze, 100%×100% */
        radial-gradient(ellipse 100% 100% at 50% 40%,
          rgba(205,232,120,.12) 0%,
          rgba(158,198,72,.05)  48%,
          rgba(110,158,38,.01)  68%,
          transparent           82%
        ),
        /* Morandi dark olive-grey base */
        linear-gradient(148deg, #2C3E24, #344628 55%, #283A20);
    }

    /* ── VARIATION B — Velvet Moss ─────────────────────────────────
       Base: Morandi greyed sage  #6A7C58  (L 42%, more grey)
       Centre: luminous cool mint  rgba(208,242,215)
       Warm outer ↔ cool luminous centre                          */
    .card-cover--03, .card-cover--09, .card-cover--06 {
      --title-color: rgba(238,236,222,.90);
      --num-color:   rgba(238,236,222,1);
      background:
        /* Primary glow — cool silver-mint */
        radial-gradient(ellipse 90% 94% at 50% 38%,
          rgba(208,242,215,.60) 0%,
          rgba(185,232,195,.42) 10%,
          rgba(158,218,168,.22) 24%,
          rgba(125,192,138,.09) 42%,
          rgba(88,162,102,.03)  58%,
          rgba(55,128,68,.01)   72%,
          transparent           84%
        ),
        /* Whisper bloom */
        radial-gradient(ellipse 100% 100% at 50% 40%,
          rgba(188,228,198,.11) 0%,
          rgba(138,192,148,.04) 48%,
          rgba(88,148,98,.01)   68%,
          transparent           82%
        ),
        /* Morandi greyed sage base */
        linear-gradient(145deg, #687C56, #72865E 55%, #647850);
    }

    /* ── VARIATION C — Morning Veil ─────────────────────────────────
       Base: Morandi pale grey-sage  #C0CAB4  (L 74%, greyer)
       Centre: near-white warm ivory  rgba(248,252,235)
       Cool washed sage ↔ warm luminous cream                     */
    .card-cover--04, .card-cover--05, .card-cover--02 {
      --title-color: rgba(42,56,30,.80);
      --num-color:   rgba(42,56,30,1);
      background:
        /* Primary glow — near-white ivory, very luminous */
        radial-gradient(ellipse 90% 94% at 50% 38%,
          rgba(248,252,235,.86) 0%,
          rgba(236,246,218,.64) 10%,
          rgba(218,236,196,.36) 24%,
          rgba(195,220,168,.14) 42%,
          rgba(168,200,138,.05) 58%,
          rgba(140,178,108,.01) 72%,
          transparent           84%
        ),
        /* Whisper bloom */
        radial-gradient(ellipse 100% 100% at 50% 40%,
          rgba(238,248,222,.38) 0%,
          rgba(205,225,180,.14) 48%,
          rgba(170,198,142,.03) 68%,
          transparent           82%
        ),
        /* Morandi pale grey-sage base */
        linear-gradient(152deg, #BEC8B2, #C4CEB8 50%, #BAC6AE);
    }

    """

content = content[:start_idx] + NEW_CSS + content[end_idx:]

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

checks = [
    ('90% 94%' in content, 'large 90% gradient ellipse'),
    ('50% 38%' in content, 'glow offset above centre'),
    ('100% 100%' in content, 'whisper bloom fills frame'),
    ('rgba(228,248,162' in content, 'A luminous chartreuse'),
    ('rgba(208,242,215' in content, 'B luminous mint'),
    ('rgba(248,252,235' in content, 'C near-white ivory'),
    ('#2C3E24' in content, 'A raised Morandi base'),
    ('#687C56' in content, 'B raised greyed sage'),
    ('#BEC8B2' in content, 'C greyed pale sage'),
    ('var(--title-color)' in content, 'per-variation text'),
    ('display: none' in content and 'cover-deco' in content, 'deco hidden'),
]
for ok, label in checks:
    sys.stdout.buffer.write(f'  {"OK" if ok else "FAIL"}: {label}\n'.encode())

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
