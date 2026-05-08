import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# ────────────────────────────────────────────────────────────────
# CSS class → card order (unchanged HTML):
#   --07  Card 01 SmartHire    → H≈88°  warm yellow-green
#   --03  Card 02 GameFlow     → H≈97°  green
#   --04  Card 03 Kanelär      → H≈106° fresh green
#   --01  Card 04 Kaleido      → H≈116° mid-green
#   --09  Card 05 KANKAN       → H≈125° green-teal
#   --05  Card 06 AIHub        → H≈134° teal-green
#   --08  Card 07 KörkortHub   → H≈143° teal
#   --06  Card 08 SoundClimbing→ H≈152° blue-teal
#   --02  Card 09 Social VR    → H≈162° cool blue-green
#
# Each card:
#  - backdrop-filter: blur(20px) saturate(165%) → frosted photo glass
#  - inset neumorphic shadows → physical depth
#  - diagonal soft-light gradient → light refraction
#  - radial center glow → luminal warmth
#  - rgba tint base → shifts hue across 9 steps
#  - ::before glass-edge border → crisp glass rim
# ────────────────────────────────────────────────────────────────
CSS_START = '/* ─── CARD COVER'
CSS_END   = '/* ─── TOUCH / MOBILE'
start_idx = content.find(CSS_START)
end_idx   = content.find(CSS_END)
assert start_idx != -1 and end_idx != -1

NEW_CSS = """/* ─── CARD COVER — Soft Glass × Neumorphism × Luminal Gradient ─ */
    .card-cover {
      position: absolute; inset: 0;
      opacity: 1; pointer-events: none;
      transition: opacity .6s var(--ease);
      overflow: hidden;
      /* Real frosted glass — blurs project photo underneath */
      backdrop-filter: blur(22px) saturate(170%) brightness(1.04);
      -webkit-backdrop-filter: blur(22px) saturate(170%) brightness(1.04);
      /* Neumorphic inset — glass pressed into the card */
      box-shadow:
        inset 2.5px 2.5px 9px rgba(255,255,255,.22),
        inset -2px  -2px  7px rgba(0,0,0,.14);
    }
    .project-card:hover .card-cover { opacity: 0; }

    /* Floating lift: thumbnail rises above text area */
    .project-thumb {
      box-shadow:
        0 1px 0 rgba(255,255,255,.78),
        0 6px 28px rgba(0,0,0,.15),
        0 2px 8px rgba(0,0,0,.09);
      position: relative;
    }

    /* Glass rim — bright top/left edge, dim bottom/right */
    .card-cover::before {
      content: '';
      position: absolute; inset: 0;
      border-top:   1px solid rgba(255,255,255,.36);
      border-left:  1px solid rgba(255,255,255,.26);
      border-right: 1px solid rgba(255,255,255,.10);
      border-bottom:1px solid rgba(255,255,255,.10);
      pointer-events: none;
      z-index: 2;
    }
    .card-cover::after,
    .cover-inner::before, .cover-inner::after { display: none; }
    .cover-inner { position: absolute; inset: .72rem; }

    /* Number — light serif, top-left */
    .cover-num {
      position: absolute; top: .78rem; left: .88rem;
      font-family: var(--font-ser);
      font-size: 1.15rem; font-weight: 400;
      letter-spacing: .04em; line-height: 1;
      color: rgba(244,242,232,.52);
      text-shadow: 0 1px 4px rgba(0,0,0,.18);
      z-index: 3;
    }

    /* Title — large, centred */
    .cover-text {
      position: absolute; inset: 0;
      display: flex; flex-direction: column;
      align-items: center; justify-content: center;
      text-align: center; padding: 1.6rem;
      z-index: 3;
    }
    .cover-title {
      font-family: var(--font-ser);
      font-size: 2.2rem; font-weight: 400;
      line-height: 1.08; letter-spacing: .01em;
      color: rgba(244,242,232,.92);
      text-shadow:
        0 1px 0 rgba(255,255,255,.12),
        0 2px 10px rgba(0,0,0,.24);
    }
    .cover-sub  { display: none; }
    .cover-deco { display: none; }

    /* ── Tinted glass tints: warm yellow-green → cool blue-teal ──
       RGB base shifts: R↓ (95→40), G≈steady (~112), B↑ (58→124)
       Opacity: 0.42 → 0.34 (lighter glass as hue cools)         */

    /* Card 01 SmartHire  H≈88°  rgb(95,115,58) */
    .card-cover--07 {
      background:
        linear-gradient(138deg,
          rgba(255,255,255,.22) 0%,
          rgba(255,255,255,.08) 35%,
          transparent 56%,
          rgba(0,0,0,.07) 100%),
        radial-gradient(ellipse at 40% 28%, rgba(255,255,255,.18) 0%, transparent 60%),
        rgba(95,115,58,.42);
    }
    /* Card 02 GameFlow   H≈97°  rgb(82,115,65) */
    .card-cover--03 {
      background:
        linear-gradient(138deg,
          rgba(255,255,255,.20) 0%,
          rgba(255,255,255,.07) 35%,
          transparent 56%,
          rgba(0,0,0,.07) 100%),
        radial-gradient(ellipse at 44% 30%, rgba(255,255,255,.16) 0%, transparent 60%),
        rgba(82,115,65,.40);
    }
    /* Card 03 Kanelär    H≈106° rgb(68,115,72) */
    .card-cover--04 {
      background:
        linear-gradient(138deg,
          rgba(255,255,255,.20) 0%,
          rgba(255,255,255,.07) 35%,
          transparent 56%,
          rgba(0,0,0,.07) 100%),
        radial-gradient(ellipse at 42% 30%, rgba(255,255,255,.15) 0%, transparent 60%),
        rgba(68,115,72,.40);
    }
    /* Card 04 Kaleido    H≈116° rgb(56,114,80) */
    .card-cover--01 {
      background:
        linear-gradient(138deg,
          rgba(255,255,255,.19) 0%,
          rgba(255,255,255,.06) 35%,
          transparent 56%,
          rgba(0,0,0,.06) 100%),
        radial-gradient(ellipse at 46% 30%, rgba(255,255,255,.15) 0%, transparent 60%),
        rgba(56,114,80,.38);
    }
    /* Card 05 KANKAN     H≈125° rgb(48,114,90) */
    .card-cover--09 {
      background:
        linear-gradient(138deg,
          rgba(255,255,255,.18) 0%,
          rgba(255,255,255,.06) 35%,
          transparent 56%,
          rgba(0,0,0,.06) 100%),
        radial-gradient(ellipse at 44% 30%, rgba(255,255,255,.14) 0%, transparent 60%),
        rgba(48,114,90,.38);
    }
    /* Card 06 AIHub      H≈134° rgb(44,113,100) */
    .card-cover--05 {
      background:
        linear-gradient(138deg,
          rgba(255,255,255,.17) 0%,
          rgba(255,255,255,.06) 35%,
          transparent 56%,
          rgba(0,0,0,.06) 100%),
        radial-gradient(ellipse at 42% 30%, rgba(255,255,255,.14) 0%, transparent 60%),
        rgba(44,113,100,.37);
    }
    /* Card 07 KörkortHub H≈143° rgb(42,112,110) */
    .card-cover--08 {
      background:
        linear-gradient(138deg,
          rgba(255,255,255,.17) 0%,
          rgba(255,255,255,.05) 35%,
          transparent 56%,
          rgba(0,0,0,.06) 100%),
        radial-gradient(ellipse at 40% 30%, rgba(255,255,255,.13) 0%, transparent 60%),
        rgba(42,112,110,.36);
    }
    /* Card 08 SoundClimb H≈152° rgb(40,112,118) */
    .card-cover--06 {
      background:
        linear-gradient(138deg,
          rgba(255,255,255,.16) 0%,
          rgba(255,255,255,.05) 35%,
          transparent 56%,
          rgba(0,0,0,.05) 100%),
        radial-gradient(ellipse at 44% 28%, rgba(255,255,255,.13) 0%, transparent 60%),
        rgba(40,112,118,.35);
    }
    /* Card 09 Social VR  H≈162° rgb(38,110,126) */
    .card-cover--02 {
      background:
        linear-gradient(138deg,
          rgba(255,255,255,.15) 0%,
          rgba(255,255,255,.05) 35%,
          transparent 56%,
          rgba(0,0,0,.05) 100%),
        radial-gradient(ellipse at 46% 30%, rgba(255,255,255,.12) 0%, transparent 60%),
        rgba(38,110,126,.34);
    }

    """

content = content[:start_idx] + NEW_CSS + content[end_idx:]

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

checks = [
    ('backdrop-filter: blur' in content, 'glass blur'),
    ('-webkit-backdrop-filter' in content, 'webkit prefix'),
    ('inset 2.5px 2.5px 9px' in content, 'neumorphic inset'),
    ('card-cover::before' in content and 'border-top' in content, 'glass rim border'),
    ('var(--font-ser)' in content and 'cover-num' in content, 'serif number'),
    ('rgba(95,115,58' in content, 'warm start (card 01)'),
    ('rgba(38,110,126' in content, 'cool end (card 09)'),
    ('2.2rem' in content, 'title size maintained'),
    ('display: none' in content and 'cover-deco' in content, 'deco hidden'),
]
for ok, label in checks:
    sys.stdout.buffer.write(f'  {"OK" if ok else "FAIL"}: {label}\n'.encode())

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
