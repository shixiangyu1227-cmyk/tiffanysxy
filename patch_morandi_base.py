import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# ─────────────────────────────────────────────────────────────────
# Morandi base color adjustments — raise L, reduce S for grey tone
#
# A Nocturne:   #2C3E24 (L19%,S24%) → #4A6238 (L32%,S17%)  darker-Morandi
# B Velvet:     #687C56 (L42%,S19%) → #7A9068 (L51%,S14%)  mid-Morandi
# C Morning:    #BEC8B2 (L74%,S12%) → #C4CCBA (L78%,S 9%)  pale-Morandi
# ─────────────────────────────────────────────────────────────────

replacements = [
    # ── Variation A base ──
    ('linear-gradient(148deg, #2C3E24, #344628 55%, #283A20)',
     'linear-gradient(148deg, #4A6238, #527040 55%, #466034)'),

    # ── Variation B base ──
    ('linear-gradient(145deg, #687C56, #72865E 55%, #647850)',
     'linear-gradient(145deg, #7A9068, #849A72 55%, #768C64)'),

    # ── Variation C base ──
    ('linear-gradient(152deg, #BEC8B2, #C4CEB8 50%, #BAC6AE)',
     'linear-gradient(152deg, #C4CCBA, #CAD4C0 50%, #C0CAB6)'),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        sys.stdout.buffer.write(f'  OK: {old[:40]}\n'.encode('utf-8'))
    else:
        sys.stdout.buffer.write(f'  MISS: {old[:40]}\n'.encode('utf-8'))

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
