import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
original = content

# Insert mobile hero background fix just before the TOUCH/MOBILE media query.
# Fix: disable expensive SVG filters (hero-flowers) on mobile and substitute
# a lightweight CSS radial-gradient that approximates the same soft sage wash.

ANCHOR = "    /* ─── TOUCH / MOBILE"
if ANCHOR not in content:
    # try with garbled encoding as fallback
    ANCHOR = "    /* " + "����" + " TOUCH / MOBILE"

NEW_CSS = """    /* ─── MOBILE HERO BACKGROUND FIX ────────────────────────────────
       SVG feGaussianBlur(38) + feTurbulence/feDisplacementMap exceed
       mobile GPU budget → blank render. Replace with CSS gradients.    */
    @media (max-width: 768px) {
      .hero-flowers { display: none; }
      .hero {
        background:
          radial-gradient(ellipse 130% 90% at 15% 20%, rgba(162,175,140,.72) 0%, transparent 52%),
          radial-gradient(ellipse 110% 80% at 85% 70%, rgba(176,188,156,.60) 0%, transparent 52%),
          radial-gradient(ellipse 100% 70% at 50% 95%, rgba(152,166,130,.48) 0%, transparent 50%),
          radial-gradient(ellipse 90%  60% at 60% 10%, rgba(184,196,164,.45) 0%, transparent 48%),
          #c2c9b0;
      }
    }

"""

idx = content.find(ANCHOR)
if idx != -1:
    content = content[:idx] + NEW_CSS + content[idx:]
    sys.stdout.buffer.write(b'  OK: mobile fix inserted\n')
else:
    sys.stdout.buffer.write(b'  MISS: anchor not found\n')

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

checks = [
    ('.hero-flowers { display: none; }' in content, 'hero-flowers hidden on mobile'),
    ('radial-gradient' in content[content.find('@media (max-width: 768px)'):
                                   content.find('@media (max-width: 768px)')+400],
     'CSS gradient fallback present'),
]
for ok, label in checks:
    sys.stdout.buffer.write(f'  {"OK" if ok else "FAIL"}: {label}\n'.encode())

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
