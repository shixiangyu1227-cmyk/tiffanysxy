import re, sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
original = content

# ── 1. Revert the wrong SVG-text replacements for cards 01 and 02 ──
# The previous patch hit SVG <text> elements instead of .cover-title divs
svg_reverts = [
    # SmartHire SVG text was changed to the tagline — revert it
    ('>Hire smarter, not harder.</text>', '>SmartHire</text>'),
    # GameFlow SVG text was changed — revert it
    ('>Where game ideas become game plans.</text>', '>GameFlow</text>'),
]
for old, new in svg_reverts:
    if old in content:
        content = content.replace(old, new, 1)
        sys.stdout.buffer.write(f'  REVERTED SVG: {old[1:30]}\n'.encode())
    else:
        sys.stdout.buffer.write(f'  (already clean): {old[1:30]}\n'.encode())

# ── 2. Replace cover-title texts using precise div pattern ──────────
# Pattern: class="cover-title">OLDTEXT</div>  (or </h2> etc.)
cover_titles = [
    ('SmartHire',     'Hire smarter, not harder.'),
    ('GameFlow',      'Where game ideas become game plans.'),
    ('Kanelär',       'Learn the language, live the life.'),
    ('Kaleido',       'From idea to image, instantly.'),
    ('AIHub',         'Stay sharp. Stay ahead.'),
    ('KANKAN',        'Find your city. Design your life.'),
    ('KörkortHub',    'Your road to the Swedish road.'),
    ('SoundClimbing', 'Climb by sound.'),
    ('Social VR',     'Can a virtual face change a real mind?'),
]

for old_title, new_title in cover_titles:
    # Match specifically inside a cover-title element
    pattern = f'class="cover-title">{old_title}<'
    replacement = f'class="cover-title">{new_title}<'
    if pattern in content:
        content = content.replace(pattern, replacement, 1)
        sys.stdout.buffer.write(f'  OK: {old_title}\n'.encode('utf-8'))
    else:
        sys.stdout.buffer.write(f'  MISS: {old_title}\n'.encode('utf-8'))

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

# Verification
sys.stdout.buffer.write(b'\nVerification:\n')
blocks = re.findall(r'<article[^>]*>.*?</article>', content, re.S)
for i, b in enumerate(blocks, 1):
    num  = re.search(r'cover-num[^>]*>(.*?)<', b)
    ctit = re.search(r'cover-title[^>]*>(.*?)<', b)
    line = f'  {i}: [{num.group(1) if num else "?"}] {ctit.group(1)[:50] if ctit else "?"}\n'
    sys.stdout.buffer.write(line.encode('utf-8'))

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
