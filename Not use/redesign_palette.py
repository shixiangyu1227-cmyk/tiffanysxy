import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# ────────────────────────────────────────────────
# 1. REPLACE CSS BLOCK — strip all lines, apply 4-color palette
# ────────────────────────────────────────────────
CSS_START = '/* ─── CARD COVER'
CSS_END   = '/* ─── TOUCH / MOBILE'

start_idx = content.find(CSS_START)
end_idx   = content.find(CSS_END)
assert start_idx != -1, 'CSS start not found'
assert end_idx   != -1, 'CSS end not found'

#
# Card → CSS class mapping:
#   01 SmartHire  → card-cover--07  → olive
#   02 GameFlow   → card-cover--03  → forest
#   03 Kanelär    → card-cover--04  → cream
#   04 Kaleido    → card-cover--01  → cream
#   05 KANKAN     → card-cover--09  → olive
#   06 AIHub      → card-cover--05  → forest
#   07 KörkortHub → card-cover--08  → ice blue
#   08 SoundClimb → card-cover--03  → forest (shared with GameFlow)
#   09 Social VR  → card-cover--02  → ice blue
#
# Grid visual balance:
#   Row 1: olive(dark) | forest(dark) | cream(light)
#   Row 2: cream(light)| olive(dark)  | forest(dark)
#   Row 3: ice(light)  | forest(dark) | ice(light)
#

NEW_CSS = """/* ─── CARD COVER ──────────────────────────── */
    .card-cover {
      position: absolute; inset: 0;
      opacity: 1; pointer-events: none;
      transition: opacity .5s var(--ease);
      overflow: hidden;
    }
    .project-card:hover .card-cover { opacity: 0; }

    /* Floating lift: thumbnail above project-info */
    .project-thumb {
      box-shadow:
        0 1px 0 rgba(255,255,255,.70),
        0 4px 20px rgba(0,0,0,.12),
        0 1px 6px rgba(0,0,0,.07);
      position: relative;
    }

    /* All pseudo-elements cleared — no decorative lines */
    .card-cover::before, .card-cover::after,
    .cover-inner::before, .cover-inner::after { display: none; }
    .cover-inner { position: absolute; inset: .72rem; }

    /* Number — top-left */
    .cover-num {
      position: absolute; top: .8rem; left: .88rem;
      font-family: var(--font-mon); font-size: 1.05rem;
      letter-spacing: .07em; line-height: 1;
      color: var(--ct); opacity: .55;
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

    /* ── Palette from reference image cards 03 / 04 / 07 / 08 ──────── */

    /* DARK FOREST GREEN  (ref 03) — GameFlow(--03), AIHub(--05), SoundClimbing(--03) */
    .card-cover--03, .card-cover--05 {
      --ct: rgba(232,228,216,.88);
      background:
        radial-gradient(ellipse at 38% 30%, rgba(52,84,44,.40) 0%, transparent 62%),
        linear-gradient(150deg, #1A2B18, #1E3020 54%, #161E12);
    }

    /* WARM CREAM  (ref 04) — Kanelär(--04), Kaleido(--01) */
    .card-cover--01, .card-cover--04 {
      --ct: rgba(40,32,20,.80);
      background:
        radial-gradient(ellipse at 48% 36%, rgba(255,252,238,.55) 0%, transparent 64%),
        linear-gradient(153deg, #E0D6C0, #EAE0CA 48%, #DCD2BC 80%, #D4CABA);
    }

    /* DARK OLIVE GREEN  (ref 07) — SmartHire(--07), KANKAN(--09) */
    .card-cover--07, .card-cover--09 {
      --ct: rgba(232,228,216,.88);
      background:
        radial-gradient(ellipse at 62% 32%, rgba(82,122,52,.36) 0%, transparent 60%),
        linear-gradient(147deg, #263C1A, #2E4820 54%, #22381A);
    }

    /* PALE ICE BLUE  (ref 08) — KörkortHub(--08), Social VR(--02) */
    .card-cover--02, .card-cover--06, .card-cover--08 {
      --ct: rgba(28,38,58,.80);
      background:
        radial-gradient(ellipse at 52% 38%, rgba(255,255,255,.52) 0%, transparent 64%),
        linear-gradient(155deg, #CBDAE8, #D4E0EE 46%, #C8D6E4 80%, #C2CDE0);
    }

    """

content = content[:start_idx] + NEW_CSS + content[end_idx:]

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

# Verify key elements
checks = [
    ('display: none' in content and 'card-cover::before' in content, 'pseudo-elements cleared'),
    ('#1A2B18' in content, 'forest green color present'),
    ('#E0D6C0' in content, 'warm cream color present'),
    ('#263C1A' in content, 'olive green color present'),
    ('#CBDAE8' in content, 'ice blue color present'),
    ('cover-sub  { display: none; }' in content, 'subtitle hidden'),
    ('cover-deco { display: none; }' in content, 'deco hidden'),
]
for ok, label in checks:
    sys.stdout.buffer.write(f'  {"OK" if ok else "FAIL"}: {label}\n'.encode())

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
