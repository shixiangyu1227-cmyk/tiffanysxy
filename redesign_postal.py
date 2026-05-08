import sys, re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# ────────────────────────────────────────────────
# 1. REPLACE CSS BLOCK
# ────────────────────────────────────────────────
CSS_START = '/* ─── CARD COVER'
CSS_END   = '/* ─── TOUCH / MOBILE'

start_idx = content.find(CSS_START)
end_idx   = content.find(CSS_END)
assert start_idx != -1, 'CSS start not found'
assert end_idx   != -1, 'CSS end not found'

NEW_CSS = r"""/* ─── CARD COVER (postal edition) ─────────────── */
    .card-cover {
      position: absolute; inset: 0;
      opacity: 1; pointer-events: none;
      transition: opacity .5s var(--ease);
      overflow: hidden;
    }
    .project-card:hover .card-cover { opacity: 0; }

    /* Floating-card lift: thumbnail sits above project-info */
    .project-thumb {
      box-shadow:
        0 1px 0 rgba(255,255,255,.72),
        0 4px 18px rgba(0,0,0,.11),
        0 1px 6px rgba(0,0,0,.07);
      position: relative;
    }

    /* Postmark ring — semi-transparent circle, bottom-right */
    .card-cover::before {
      content: '';
      position: absolute;
      right: -14%;
      bottom: 8%;
      width: 96px; height: 96px;
      border-radius: 50%;
      border: 1.5px solid var(--pk);
      box-shadow: 0 0 0 10px var(--pk-thin), inset 0 0 0 10px var(--pk-thin);
      pointer-events: none;
    }

    /* Envelope fold line — subtle diagonal across card */
    .card-cover::after {
      content: '';
      position: absolute; inset: 0;
      background: linear-gradient(
        136deg,
        transparent calc(68% - .5px),
        var(--pk) calc(68% - .5px),
        var(--pk) calc(68% + .5px),
        transparent calc(68% + .5px)
      );
      pointer-events: none;
    }

    /* Stamp-perforation border uses cover-inner pseudo-elements */
    .cover-inner { position: absolute; inset: .72rem; pointer-events: none; }
    .cover-inner::before, .cover-inner::after { display: none; }

    /* Number — smaller (1.45 rem), top-left with stamp dashes */
    .cover-num {
      position: absolute; top: .8rem; left: .88rem;
      font-family: var(--font-mon); font-size: 1.1rem;
      letter-spacing: .06em; line-height: 1;
      color: var(--ct); opacity: .65;
    }
    .cover-num::after {
      content: '';
      position: absolute; inset: -3px -5px;
      border: 1.5px dashed var(--pk);
      border-radius: 2px;
      pointer-events: none;
    }

    /* Title block — centered on card */
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

    /* ── Colour tokens: light text on dark covers ─ */
    .card-cover--02, .card-cover--03, .card-cover--05,
    .card-cover--06, .card-cover--07, .card-cover--08, .card-cover--09 {
      --ct:      rgba(244,239,230,.92);
      --pk:      rgba(244,239,230,.28);
      --pk-thin: rgba(244,239,230,.05);
    }
    /* Dark text on light covers (01 parchment, 04 ivory) */
    .card-cover--01, .card-cover--04 {
      --ct:      rgba(46,36,26,.82);
      --pk:      rgba(46,36,26,.22);
      --pk-thin: rgba(46,36,26,.04);
    }

    /* ── Postal palette — muted, harmonious ─────── */
    .card-cover--01 { /* SmartHire: warm parchment */
      background:
        radial-gradient(ellipse at 38% 30%, rgba(255,248,228,.45) 0%, transparent 62%),
        linear-gradient(152deg, #D4C8A8, #DDD2B2 48%, #CEC4A2);
    }
    .card-cover--02 { /* GameFlow: Prussian postal */
      background:
        radial-gradient(ellipse at 62% 28%, rgba(160,196,228,.18) 0%, transparent 60%),
        linear-gradient(148deg, #4A6478, #54707C 50%, #466070);
    }
    .card-cover--03 { /* Kanelär: reed sage */
      background:
        radial-gradient(ellipse at 44% 32%, rgba(160,210,160,.16) 0%, transparent 58%),
        linear-gradient(145deg, #5E8E68, #6A9A72 52%, #5A8862);
    }
    .card-cover--04 { /* Kaleido: ivory rose */
      background:
        radial-gradient(ellipse at 54% 36%, rgba(255,248,242,.55) 0%, transparent 64%),
        linear-gradient(155deg, #D0B8B0, #DBBFB8 44%, #CCB4AC 80%, #C6ACAA);
    }
    .card-cover--05 { /* KANKAN: ink indigo */
      background:
        radial-gradient(ellipse at 68% 26%, rgba(110,140,190,.2) 0%, transparent 54%),
        linear-gradient(146deg, #3E5062, #48596E 54%, #3A4C5E);
    }
    .card-cover--06 { /* AIHub: slate steel */
      background:
        radial-gradient(ellipse at 40% 30%, rgba(140,168,210,.18) 0%, transparent 56%),
        linear-gradient(150deg, #5C6E88, #687A94 50%, #586882);
    }
    .card-cover--07 { /* KörkortHub: warm umber */
      background:
        radial-gradient(ellipse at 64% 34%, rgba(210,190,148,.22) 0%, transparent 60%),
        linear-gradient(148deg, #88785E, #94846A 46%, #86745C);
    }
    .card-cover--08 { /* SoundClimbing: forest teal */
      background:
        radial-gradient(ellipse at 50% 28%, rgba(110,168,148,.2) 0%, transparent 56%),
        linear-gradient(145deg, #486858, #527464 50%, #446254);
    }
    .card-cover--09 { /* SocialVR: ash rose */
      background:
        radial-gradient(ellipse at 52% 34%, rgba(210,168,158,.22) 0%, transparent 60%),
        linear-gradient(150deg, #886060, #946A6A 46%, #84585C);
    }

    """

content = content[:start_idx] + NEW_CSS + content[end_idx:]

# ────────────────────────────────────────────────
# 2. UPDATE ALL 9 COVER TITLES TO PROJECT NAMES
# ────────────────────────────────────────────────
title_map = [
    # (old_exact_html, new_html)
    ('<div class="cover-title">Hiring,<br>Redesigned.</div>',
     '<div class="cover-title">SmartHire</div>'),

    ('<div class="cover-title">Play Better.</div>',
     '<div class="cover-title">GameFlow</div>'),

    ('<div class="cover-title">Kanel + lär.</div>',
     '<div class="cover-title">Kanelär</div>'),

    ('<div class="cover-title">Color,<br>Multiplied.</div>',
     '<div class="cover-title">Kaleido</div>'),

    ('<div class="cover-title">Where will<br>you go?</div>',
     '<div class="cover-title">KANKAN</div>'),

    ('<div class="cover-title">More Human<br>Than Machine.</div>',
     '<div class="cover-title">AIHub</div>'),

    ('<div class="cover-title">Drive Forward.</div>',
     '<div class="cover-title">KörkortHub</div>'),

    # SoundClimbing has style attribute — match exactly
    ('<div class="cover-title" style="font-style:italic;">Design is<br>Never Neutral.</div>',
     '<div class="cover-title">SoundClimbing</div>'),

    ('<div class="cover-title">Presence Shapes<br>Behavior.</div>',
     '<div class="cover-title">Social VR</div>'),
]

for old, new in title_map:
    if old in content:
        content = content.replace(old, new, 1)
        sys.stdout.buffer.write(f'  OK replaced: {old[:50]}\n'.encode('utf-8'))
    else:
        sys.stdout.buffer.write(f'  MISS: {old[:50]}\n'.encode('utf-8'))

# ────────────────────────────────────────────────
# 3. SAVE
# ────────────────────────────────────────────────
changed = content != original
sys.stdout.buffer.write(f'\nChanged: {changed}\n'.encode())

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved index.html\n')
