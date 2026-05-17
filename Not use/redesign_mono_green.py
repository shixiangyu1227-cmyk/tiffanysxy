import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

original = content

CSS_START = '/* ─── CARD COVER'
CSS_END   = '/* ─── TOUCH / MOBILE'

start_idx = content.find(CSS_START)
end_idx   = content.find(CSS_END)
assert start_idx != -1 and end_idx != -1

#
# CSS class → card mapping (unchanged HTML):
#   --01  Kaleido        → pale sage
#   --02  Social VR      → pale sage (warmer)
#   --03  GameFlow       → muted mid-sage   (shared with SoundClimbing --03)
#   --04  Kanelär        → near-black forest
#   --05  AIHub          → deep forest
#   --07  SmartHire      → dark forest
#   --08  KörkortHub     → light sage
#   --09  KANKAN         → medium-dark forest
#
# 3×3 grid value rhythm:
#   dark      │ mid-sage   │ near-black
#   very-pale │ med-dark   │ deep-forest
#   light     │ mid-sage   │ pale-warm
#
# Page bg: #c2c9b0 (H≈100°, S≈16%, L≈74%)
# All 9 greens share hue 102–112°, saturation 14–32%, lightness 10–82%
#

NEW_CSS = """/* ─── CARD COVER ──────────────────────────── */
    .card-cover {
      position: absolute; inset: 0;
      opacity: 1; pointer-events: none;
      transition: opacity .5s var(--ease);
      overflow: hidden;
    }
    .project-card:hover .card-cover { opacity: 0; }

    /* Floating lift */
    .project-thumb {
      box-shadow:
        0 1px 0 rgba(255,255,255,.70),
        0 4px 20px rgba(0,0,0,.12),
        0 1px 6px rgba(0,0,0,.07);
      position: relative;
    }

    /* No decorative lines */
    .card-cover::before, .card-cover::after,
    .cover-inner::before, .cover-inner::after { display: none; }
    .cover-inner { position: absolute; inset: .72rem; }

    /* Number */
    .cover-num {
      position: absolute; top: .8rem; left: .88rem;
      font-family: var(--font-mon); font-size: 1.05rem;
      letter-spacing: .07em; line-height: 1;
      color: var(--ct); opacity: .50;
    }

    /* Title — centred */
    .cover-text {
      position: absolute; inset: 0;
      display: flex; flex-direction: column;
      align-items: center; justify-content: center;
      text-align: center; padding: 1.6rem;
    }
    .cover-title {
      font-family: var(--font-ser);
      font-size: 1.55rem; font-weight: 400;
      line-height: 1.1; letter-spacing: .015em;
      color: var(--ct);
    }
    .cover-sub  { display: none; }
    .cover-deco { display: none; }

    /* ── Monochromatic green palette — 9 distinct values ──────── */
    /* Page bg: #c2c9b0  |  All hues: 100–112°, S 14–30%, L 10–82% */

    /* 01 Kaleido — very pale sage (L 82%) */
    .card-cover--01 {
      --ct: rgba(30,42,22,.76);
      background:
        radial-gradient(ellipse at 48% 38%, rgba(255,255,248,.48) 0%, transparent 66%),
        linear-gradient(152deg, #CDD8C4, #D6E0CC 48%, #C9D4C0);
    }

    /* 02 Social VR — pale sage, slightly warmer (L 74%) */
    .card-cover--02 {
      --ct: rgba(26,38,20,.78);
      background:
        radial-gradient(ellipse at 52% 36%, rgba(255,255,244,.38) 0%, transparent 64%),
        linear-gradient(148deg, #B4C4AA, #BED0B4 50%, #B0C0A6);
    }

    /* 03 GameFlow + SoundClimbing — muted mid-sage (L 50%) */
    .card-cover--03 {
      --ct: rgba(226,232,218,.90);
      background:
        radial-gradient(ellipse at 44% 32%, rgba(180,222,160,.18) 0%, transparent 60%),
        linear-gradient(150deg, #728A68, #7C9472 52%, #6E8664);
    }

    /* 04 Kanelär — near-black forest (L 11%) */
    .card-cover--04 {
      --ct: rgba(226,232,218,.90);
      background:
        radial-gradient(ellipse at 38% 28%, rgba(50,78,36,.42) 0%, transparent 62%),
        linear-gradient(145deg, #161E14, #1A2416 54%, #121A10);
    }

    /* 05 AIHub — deep forest (L 16%) */
    .card-cover--05 {
      --ct: rgba(226,232,218,.90);
      background:
        radial-gradient(ellipse at 62% 30%, rgba(52,82,40,.38) 0%, transparent 60%),
        linear-gradient(148deg, #1E3018, #243A1E 54%, #1A2C14);
    }

    /* 06 (unused — balanced fallback) */
    .card-cover--06 {
      --ct: rgba(226,232,218,.90);
      background: linear-gradient(148deg, #3A5830, #42622C);
    }

    /* 07 SmartHire — dark forest (L 22%) */
    .card-cover--07 {
      --ct: rgba(226,232,218,.90);
      background:
        radial-gradient(ellipse at 58% 32%, rgba(78,118,52,.34) 0%, transparent 58%),
        linear-gradient(147deg, #2A4220, #324A26 54%, #263E1E);
    }

    /* 08 KörkortHub — light sage (L 62%) */
    .card-cover--08 {
      --ct: rgba(28,40,22,.78);
      background:
        radial-gradient(ellipse at 50% 36%, rgba(255,255,248,.40) 0%, transparent 64%),
        linear-gradient(155deg, #98AA8C, #A2B496 48%, #94A688 80%, #90A284);
    }

    /* 09 KANKAN — medium-dark forest (L 28%) */
    .card-cover--09 {
      --ct: rgba(226,232,218,.90);
      background:
        radial-gradient(ellipse at 64% 30%, rgba(72,112,50,.30) 0%, transparent 58%),
        linear-gradient(147deg, #385828, #40622E 54%, #344C24);
    }

    """

content = content[:start_idx] + NEW_CSS + content[end_idx:]

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

# Spot checks
checks = [
    ('#161E14' in content, 'near-black (Kanelär)'),
    ('#1E3018' in content, 'deep forest (AIHub)'),
    ('#2A4220' in content, 'dark forest (SmartHire)'),
    ('#385828' in content, 'med-dark (KANKAN)'),
    ('#728A68' in content, 'mid-sage (GameFlow/Sound)'),
    ('#98AA8C' in content, 'light sage (Körkort)'),
    ('#B4C4AA' in content, 'pale sage (SocialVR)'),
    ('#CDD8C4' in content, 'very pale (Kaleido)'),
    ('display: none' in content and 'card-cover::before' in content, 'no decorative lines'),
]
for ok, label in checks:
    sys.stdout.buffer.write(f'  {"OK" if ok else "FAIL"}: {label}\n'.encode())

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
