import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# ────────────────────────────────────────────────
# New range: darkest #131C11 (L≈11%) → lightest #476638 (L≈39%)
# 9 even steps via linear RGB interpolation
#
# Start RGB: (19, 28, 17)   End RGB: (71, 102, 56)
# ΔR≈6.5, ΔG≈9.25, ΔB≈4.9 per step
#
# CSS class → card order:
#   stop 1 → --07 SmartHire   (darkest)
#   stop 2 → --03 GameFlow
#   stop 3 → --04 Kanelär
#   stop 4 → --01 Kaleido
#   stop 5 → --09 KANKAN
#   stop 6 → --05 AIHub
#   stop 7 → --08 KörkortHub
#   stop 8 → --06 SoundClimbing
#   stop 9 → --02 Social VR   (lightest ≈ current stop 5)
#
# All dark → all use light cream text
# ────────────────────────────────────────────────

CSS_START = '/* ─── CARD COVER'
CSS_END   = '/* ─── TOUCH / MOBILE'
start_idx = content.find(CSS_START)
end_idx   = content.find(CSS_END)
assert start_idx != -1 and end_idx != -1

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

    /* Number — serif, top-left */
    .cover-num {
      position: absolute; top: .75rem; left: .85rem;
      font-family: var(--font-ser);
      font-size: 1.15rem; font-weight: 400;
      letter-spacing: .04em; line-height: 1;
      color: rgba(228,234,220,.52);
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
      font-size: 2.2rem; font-weight: 400;
      line-height: 1.08; letter-spacing: .01em;
      color: rgba(228,234,220,.90);
    }
    .cover-sub  { display: none; }
    .cover-deco { display: none; }

    /* ── Monochromatic green 01→09 dark→light (range L 11%→39%) ── */

    /* Stop 1 — L≈11%  Card 01 SmartHire (CSS --07) */
    .card-cover--07 {
      background:
        radial-gradient(ellipse at 42% 30%, rgba(52,82,36,.38) 0%, transparent 62%),
        linear-gradient(148deg, #131C11, #172115 54%, #101810);
    }
    /* Stop 2 — L≈15%  Card 02 GameFlow (CSS --03) */
    .card-cover--03 {
      background:
        radial-gradient(ellipse at 56% 28%, rgba(56,88,38,.36) 0%, transparent 60%),
        linear-gradient(150deg, #192516, #1D2B1A 54%, #16221300);
    }
    /* Stop 3 — L≈19%  Card 03 Kanelär (CSS --04) */
    .card-cover--04 {
      background:
        radial-gradient(ellipse at 44% 32%, rgba(62,98,42,.34) 0%, transparent 60%),
        linear-gradient(146deg, #20301B, #253720 54%, #1C2C17);
    }
    /* Stop 4 — L≈23%  Card 04 Kaleido (CSS --01) */
    .card-cover--01 {
      background:
        radial-gradient(ellipse at 62% 30%, rgba(70,110,48,.32) 0%, transparent 58%),
        linear-gradient(152deg, #273A20, #2C4225 54%, #23361C);
    }
    /* Stop 5 — L≈27%  Card 05 KANKAN (CSS --09) */
    .card-cover--09 {
      background:
        radial-gradient(ellipse at 50% 34%, rgba(80,124,54,.30) 0%, transparent 58%),
        linear-gradient(148deg, #2E4425, #34502A 54%, #2A4022);
    }
    /* Stop 6 — L≈31%  Card 06 AIHub (CSS --05) */
    .card-cover--05 {
      background:
        radial-gradient(ellipse at 40% 30%, rgba(90,138,60,.28) 0%, transparent 58%),
        linear-gradient(150deg, #354E2A, #3C5A30 54%, #324C28);
    }
    /* Stop 7 — L≈34%  Card 07 KörkortHub (CSS --08) */
    .card-cover--08 {
      background:
        radial-gradient(ellipse at 58% 32%, rgba(100,152,66,.26) 0%, transparent 58%),
        linear-gradient(147deg, #3C582F, #446435 54%, #385430);
    }
    /* Stop 8 — L≈37%  Card 08 SoundClimbing (CSS --06) */
    .card-cover--06 {
      background:
        radial-gradient(ellipse at 46% 36%, rgba(110,166,72,.24) 0%, transparent 60%),
        linear-gradient(153deg, #416234, #4A6E3A 50%, #3E5E30);
    }
    /* Stop 9 — L≈39%  Card 09 Social VR (CSS --02) — max lightness */
    .card-cover--02 {
      background:
        radial-gradient(ellipse at 52% 38%, rgba(118,178,78,.22) 0%, transparent 62%),
        linear-gradient(150deg, #476638, #506E40 50%, #436234);
    }

    """

content = content[:start_idx] + NEW_CSS + content[end_idx:]

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

checks = [
    ('#131C11' in content, 'stop 1 darkest'),
    ('#476638' in content, 'stop 9 = current stop5 level'),
    ('2.2rem' in content, 'title size unchanged'),
    ('var(--font-ser)' in content and 'cover-num' in content, 'serif number'),
    ('display: none' in content and 'card-cover::before' in content, 'no decorative lines'),
]
for ok, label in checks:
    sys.stdout.buffer.write(f'  {"OK" if ok else "FAIL"}: {label}\n'.encode())

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
