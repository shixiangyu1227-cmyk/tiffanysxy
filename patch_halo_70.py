import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# ─────────────────────────────────────────────────────────────────
# Expand halo to cover ~70% of card:
#  - Ellipse: 90%→96% / 94%→100%  (larger radial reach)
#  - Opacity stays ≥ 0.10 until 56-60% of gradient
#  - Fades gently 0.04→0.01→transparent by 92%
#  - Secondary bloom: 100% unchanged (outer whisper stays)
# ─────────────────────────────────────────────────────────────────

replacements = [
    # ── Design A: Sky × Amber ──────────────────────────────────
    (
      """        radial-gradient(ellipse 90% 94% at 50% 40%,
          rgba(242,185,58,.72)  0%,
          rgba(244,200,88,.52)  10%,
          rgba(244,215,120,.28) 24%,
          rgba(244,228,158,.11) 42%,
          rgba(244,238,188,.04) 58%,
          rgba(245,242,210,.01) 72%,
          transparent           84%
        ),""",
      """        radial-gradient(ellipse 96% 100% at 50% 40%,
          rgba(242,185,58,.70)  0%,
          rgba(244,200,88,.54)  10%,
          rgba(244,215,120,.36) 24%,
          rgba(244,228,158,.20) 40%,
          rgba(244,235,178,.10) 56%,
          rgba(245,240,200,.04) 70%,
          rgba(245,242,212,.01) 82%,
          transparent           92%
        ),"""
    ),

    # ── Design B: Lavender × Coral ─────────────────────────────
    (
      """        radial-gradient(ellipse 90% 94% at 50% 40%,
          rgba(235,125,108,.72) 0%,
          rgba(238,148,132,.52) 10%,
          rgba(238,172,160,.28) 24%,
          rgba(237,198,190,.11) 42%,
          rgba(237,218,213,.04) 58%,
          rgba(238,228,225,.01) 72%,
          transparent           84%
        ),""",
      """        radial-gradient(ellipse 96% 100% at 50% 40%,
          rgba(235,125,108,.70) 0%,
          rgba(238,148,132,.54) 10%,
          rgba(238,172,160,.36) 24%,
          rgba(237,198,190,.20) 40%,
          rgba(237,213,208,.10) 56%,
          rgba(238,224,220,.04) 70%,
          rgba(238,230,226,.01) 82%,
          transparent           92%
        ),"""
    ),

    # ── Design C: Sage × Forest (lower glow at 50% 58%) ────────
    (
      """        radial-gradient(ellipse 90% 94% at 50% 58%,
          rgba(95,118,44,.74)   0%,
          rgba(108,132,54,.54)  10%,
          rgba(122,148,65,.30)  26%,
          rgba(138,162,78,.12)  44%,
          rgba(152,174,90,.04)  60%,
          rgba(164,184,100,.01) 74%,
          transparent           86%
        ),""",
      """        radial-gradient(ellipse 96% 100% at 50% 58%,
          rgba(95,118,44,.72)   0%,
          rgba(108,132,54,.56)  10%,
          rgba(122,148,65,.36)  26%,
          rgba(138,162,78,.20)  42%,
          rgba(150,172,88,.10)  58%,
          rgba(162,182,98,.04)  72%,
          rgba(172,190,108,.01) 84%,
          transparent           94%
        ),"""
    ),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        sys.stdout.buffer.write(b'  OK: replaced\n')
    else:
        sys.stdout.buffer.write(b'  MISS: not found\n')
        # Debug: show normalized version
        import re as _re
        norm = _re.sub(r'\s+', ' ', old[:60])
        sys.stdout.buffer.write(f'  Looking for: {norm}\n'.encode('utf-8'))

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

checks = [
    ('ellipse 96% 100%' in content, 'expanded ellipse 96%×100%'),
    ('.10) 56%' in content, 'A/B opacity 0.10 at 56%'),
    ('.10)  58%' in content, 'C opacity 0.10 at 58%'),
    ('transparent           92%' in content, 'A/B fade at 92%'),
    ('transparent           94%' in content, 'C fade at 94%'),
]
for ok, label in checks:
    sys.stdout.buffer.write(f'  {"OK" if ok else "FAIL"}: {label}\n'.encode())

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
