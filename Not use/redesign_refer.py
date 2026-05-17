import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# ─────────────────────────────────────────────────────────────────
# 3 designs from reference image applied to 9 cards:
#
#   A  Sky × Amber      — powder blue outer, warm amber glow (brighter center)
#   B  Lavender × Coral — soft lavender outer, coral-salmon glow (brighter center)
#   C  Sage × Forest    — pale olive-sage outer, deep forest core (darker center)
#
# Grid rhythm (A|B|C repeating):
#   CSS --07  Card 01 SmartHire   → A
#   CSS --03  Card 02 GameFlow    → B
#   CSS --04  Card 03 Kanelär     → C
#   CSS --01  Card 04 Kaleido     → A
#   CSS --09  Card 05 KANKAN      → B
#   CSS --05  Card 06 AIHub       → C
#   CSS --08  Card 07 KörkortHub  → A
#   CSS --06  Card 08 SoundClimb  → B  (re-merged into group)
#   CSS --02  Card 09 Social VR   → C
# ─────────────────────────────────────────────────────────────────
CSS_START = '/* ─── CARD COVER'
CSS_END   = '/* ─── TOUCH / MOBILE'
start_idx = content.find(CSS_START)
end_idx   = content.find(CSS_END)
assert start_idx != -1 and end_idx != -1

NEW_CSS = """/* ─── CARD COVER — 弥散光 · Reference Palette ─────────────────── */
    .card-cover {
      position: absolute; inset: 0;
      opacity: 1; pointer-events: none;
      transition: opacity .65s var(--ease);
      overflow: hidden;
    }
    .project-card:hover .card-cover { opacity: 0; }

    .project-thumb {
      box-shadow:
        0 1px 0 rgba(255,255,255,.72),
        0 5px 22px rgba(0,0,0,.12),
        0 2px 7px rgba(0,0,0,.08);
      position: relative;
    }

    .card-cover::before, .card-cover::after,
    .cover-inner::before, .cover-inner::after { display: none; }
    .cover-inner { position: absolute; inset: .72rem; }

    .cover-num {
      position: absolute; top: .78rem; left: .88rem;
      font-family: var(--font-ser);
      font-size: 1.15rem; font-weight: 400;
      letter-spacing: .04em; line-height: 1;
      color: var(--num-color); opacity: .48;
    }
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

    /* ── A  Sky × Amber ────────────────────────────────────────────
       Outer: powder blue    #B5D5E0
       Core:  warm amber     rgb(242,185,58)  — brighter than outer
       Glow radiates centre→edge, getting lighter                  */
    .card-cover--07, .card-cover--01, .card-cover--08 {
      --title-color: rgba(32,54,68,.80);
      --num-color:   rgba(32,54,68,1);
      background:
        radial-gradient(ellipse 90% 94% at 50% 40%,
          rgba(242,185,58,.72)  0%,
          rgba(244,200,88,.52)  10%,
          rgba(244,215,120,.28) 24%,
          rgba(244,228,158,.11) 42%,
          rgba(244,238,188,.04) 58%,
          rgba(245,242,210,.01) 72%,
          transparent           84%
        ),
        radial-gradient(ellipse 100% 100% at 50% 42%,
          rgba(238,176,46,.13)  0%,
          rgba(240,198,78,.05)  50%,
          transparent           80%
        ),
        linear-gradient(150deg, #B3D4DF, #BBD9E6 52%, #AFD0DB);
    }

    /* ── B  Lavender × Coral ───────────────────────────────────────
       Outer: soft lavender  #BDB8CC
       Core:  coral-salmon   rgb(235,125,108) — brighter than outer
       Glow radiates centre→edge, getting lighter                  */
    .card-cover--03, .card-cover--09, .card-cover--06 {
      --title-color: rgba(52,42,72,.78);
      --num-color:   rgba(52,42,72,1);
      background:
        radial-gradient(ellipse 90% 94% at 50% 40%,
          rgba(235,125,108,.72) 0%,
          rgba(238,148,132,.52) 10%,
          rgba(238,172,160,.28) 24%,
          rgba(237,198,190,.11) 42%,
          rgba(237,218,213,.04) 58%,
          rgba(238,228,225,.01) 72%,
          transparent           84%
        ),
        radial-gradient(ellipse 100% 100% at 50% 42%,
          rgba(228,112,95,.13)  0%,
          rgba(232,142,126,.05) 50%,
          transparent           80%
        ),
        linear-gradient(150deg, #BBB7CC, #C3BDD4 52%, #B7B3C8);
    }

    /* ── C  Sage × Forest ──────────────────────────────────────────
       Outer: pale sage-olive  #BCBF96
       Core:  deep forest      rgb(95,118,44)  — DARKER than outer
       Glow positioned lower (at 50% 58%), core darkens downward   */
    .card-cover--04, .card-cover--05, .card-cover--02 {
      --title-color: rgba(40,52,20,.80);
      --num-color:   rgba(40,52,20,1);
      background:
        radial-gradient(ellipse 90% 94% at 50% 58%,
          rgba(95,118,44,.74)   0%,
          rgba(108,132,54,.54)  10%,
          rgba(122,148,65,.30)  26%,
          rgba(138,162,78,.12)  44%,
          rgba(152,174,90,.04)  60%,
          rgba(164,184,100,.01) 74%,
          transparent           86%
        ),
        radial-gradient(ellipse 100% 100% at 50% 60%,
          rgba(85,108,38,.14)   0%,
          rgba(105,128,50,.05)  52%,
          transparent           80%
        ),
        linear-gradient(150deg, #BABF94, #C0C49A 52%, #B6BB90);
    }

    """

content = content[:start_idx] + NEW_CSS + content[end_idx:]

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

checks = [
    ('rgba(242,185,58' in content,  'A amber core'),
    ('#B3D4DF' in content,          'A powder blue base'),
    ('rgba(235,125,108' in content, 'B coral core'),
    ('#BBB7CC' in content,          'B lavender base'),
    ('rgba(95,118,44' in content,   'C forest core'),
    ('#BABF94' in content,          'C sage base'),
    ('50% 58%' in content,          'C glow positioned lower'),
    ('.card-cover--03, .card-cover--09, .card-cover--06' in content, 'B group re-merged'),
    ('display: none' in content and 'cover-deco' in content, 'deco hidden'),
]
for ok, label in checks:
    sys.stdout.buffer.write(f'  {"OK" if ok else "FAIL"}: {label}\n'.encode())

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
