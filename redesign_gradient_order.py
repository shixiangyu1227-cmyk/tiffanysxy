import sys, re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# ────────────────────────────────────────────────
# 1. Move SoundClimbing from card-cover--03 to card-cover--06
#    so each card has a unique CSS class
#    SoundClimbing is the SECOND occurrence of card-cover--03
# ────────────────────────────────────────────────
instances = [m.start() for m in re.finditer(r'card-cover card-cover--03', content)]
assert len(instances) == 2, f'Expected 2 instances of --03, found {len(instances)}'
# Replace only the second one (SoundClimbing = card 08)
second = instances[1]
content = content[:second] + 'card-cover card-cover--06' + content[second + len('card-cover card-cover--03'):]
sys.stdout.buffer.write(b'Moved SoundClimbing to --06\n')

# ────────────────────────────────────────────────
# 2. REPLACE CSS BLOCK
#
# Card number order vs CSS class:
#   Card 01 SmartHire   → CSS --07  → stop 1 (darkest)
#   Card 02 GameFlow    → CSS --03  → stop 2
#   Card 03 Kanelär     → CSS --04  → stop 3
#   Card 04 Kaleido     → CSS --01  → stop 4
#   Card 05 KANKAN      → CSS --09  → stop 5
#   Card 06 AIHub       → CSS --05  → stop 6
#   Card 07 KörkortHub  → CSS --08  → stop 7
#   Card 08 SoundClimb  → CSS --06  → stop 8
#   Card 09 Social VR   → CSS --02  → stop 9 (lightest)
#
# Hue family: 105–112°, S 16–28%, L 11%→72%
# 9 evenly-spaced lightness steps:
#   11 | 18 | 25 | 32 | 39 | 46 | 53 | 62 | 72 %
#
# Light text (cream) for stops 1–7; dark text for stops 8–9
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

    /* Number — serif font, top-left */
    .cover-num {
      position: absolute; top: .75rem; left: .85rem;
      font-family: var(--font-ser);
      font-size: 1.15rem; font-weight: 400;
      letter-spacing: .04em; line-height: 1;
      color: var(--ct); opacity: .52;
    }

    /* Title — centred, 3 sizes larger */
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
      color: var(--ct);
    }
    .cover-sub  { display: none; }
    .cover-deco { display: none; }

    /* ── Monochromatic green: card 01→09 = dark→light ──────────── */
    /* Light cream text (stops 1–7) */
    .card-cover--07, .card-cover--03, .card-cover--04,
    .card-cover--01, .card-cover--09, .card-cover--05,
    .card-cover--08 {
      --ct: rgba(228,234,220,.90);
    }
    /* Dark green text (stops 8–9) */
    .card-cover--06, .card-cover--02 {
      --ct: rgba(26,40,18,.76);
    }

    /* Stop 1 — darkest  (Card 01 SmartHire, CSS --07, L≈11%) */
    .card-cover--07 {
      background:
        radial-gradient(ellipse at 42% 30%, rgba(48,76,34,.40) 0%, transparent 62%),
        linear-gradient(148deg, #141D12, #182316 54%, #101810);
    }
    /* Stop 2  (Card 02 GameFlow, CSS --03, L≈18%) */
    .card-cover--03 {
      background:
        radial-gradient(ellipse at 56% 28%, rgba(50,82,36,.36) 0%, transparent 60%),
        linear-gradient(150deg, #1D3018, #22381C 54%, #192C14);
    }
    /* Stop 3  (Card 03 Kanelär, CSS --04, L≈25%) */
    .card-cover--04 {
      background:
        radial-gradient(ellipse at 44% 32%, rgba(70,108,48,.34) 0%, transparent 60%),
        linear-gradient(146deg, #2A4020, #304826 54%, #263C1C);
    }
    /* Stop 4  (Card 04 Kaleido, CSS --01, L≈32%) */
    .card-cover--01 {
      background:
        radial-gradient(ellipse at 62% 30%, rgba(88,130,58,.30) 0%, transparent 58%),
        linear-gradient(152deg, #385228, #40602E 54%, #345026);
    }
    /* Stop 5  (Card 05 KANKAN, CSS --09, L≈39%) */
    .card-cover--09 {
      background:
        radial-gradient(ellipse at 50% 34%, rgba(100,148,68,.26) 0%, transparent 58%),
        linear-gradient(148deg, #476636, #4E703C 54%, #436232);
    }
    /* Stop 6  (Card 06 AIHub, CSS --05, L≈46%) */
    .card-cover--05 {
      background:
        radial-gradient(ellipse at 40% 30%, rgba(120,168,82,.22) 0%, transparent 58%),
        linear-gradient(150deg, #567A44, #5E844C 54%, #527640);
    }
    /* Stop 7  (Card 07 KörkortHub, CSS --08, L≈53%) */
    .card-cover--08 {
      background:
        radial-gradient(ellipse at 58% 32%, rgba(160,210,110,.18) 0%, transparent 58%),
        linear-gradient(147deg, #6A9058, #748A62 54%, #669054);
    }
    /* Stop 8  (Card 08 SoundClimbing, CSS --06, L≈62%) */
    .card-cover--06 {
      background:
        radial-gradient(ellipse at 46% 36%, rgba(200,240,160,.22) 0%, transparent 62%),
        linear-gradient(153deg, #84A472, #8EAE7C 50%, #80A06E);
    }
    /* Stop 9 — lightest  (Card 09 Social VR, CSS --02, L≈72%) */
    .card-cover--02 {
      background:
        radial-gradient(ellipse at 52% 38%, rgba(255,255,248,.35) 0%, transparent 64%),
        linear-gradient(150deg, #A0B890, #AABF9A 50%, #9CB48C);
    }

    """

content = content[:start_idx] + NEW_CSS + content[end_idx:]

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

checks = [
    ('card-cover card-cover--06' in content, 'SoundClimbing uses --06'),
    ('var(--font-ser)' in content and 'cover-num' in content, 'number uses serif'),
    ('font-size: 2.2rem' in content, 'title 2.2rem'),
    ('#141D12' in content, 'stop 1 darkest'),
    ('#A0B890' in content, 'stop 9 lightest'),
    ('display: none' in content and 'card-cover::before' in content, 'no decorative lines'),
]
for ok, label in checks:
    sys.stdout.buffer.write(f'  {"OK" if ok else "FAIL"}: {label}\n'.encode())

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
