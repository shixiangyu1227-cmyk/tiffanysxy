import re, sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
original = content

# ── 1. Fix swapped cover numbers for AIhub (--05) and KANKAN (--09) ──
# AIhub block has num=06 → should be 05
# KANKAN block has num=05 → should be 06
# Replace inside each card's article block to avoid collisions

def patch_card(html, css_class, old_num, new_num):
    # Find the article block containing this css_class
    pat = r'(<article[^>]*>)(.*?)(</article>)'
    def replacer(m):
        body = m.group(2)
        if f'card-cover--{css_class}' in body:
            body = body.replace(
                f'class="cover-num">{old_num}<',
                f'class="cover-num">{new_num}<',
                1
            )
        return m.group(1) + body + m.group(3)
    return re.sub(pat, replacer, html, flags=re.S)

content = patch_card(content, '05', '06', '05')
content = patch_card(content, '09', '05', '06')
sys.stdout.buffer.write(b'  OK: num swap fixed\n')

# ── 2. Replace all cover-title texts ──────────────────────────────
title_map = {
    '>SmartHire<':      '>Hire smarter, not harder.<',
    '>GameFlow<':       '>Where game ideas become game plans.<',
    '>Kanelär<':        '>Learn the language, live the life.<',
    '>Kaleido<':        '>From idea to image, instantly.<',
    '>AIHub<':          '>Stay sharp. Stay ahead.<',
    '>KANKAN<':         '>Find your city. Design your life.<',
    '>KörkortHub<':     '>Your road to the Swedish road.<',
    '>SoundClimbing<':  '>Climb by sound.<',
    '>Social VR<':      '>Can a virtual face change a real mind?<',
}

for old, new in title_map.items():
    if old in content:
        content = content.replace(old, new, 1)
        sys.stdout.buffer.write(f'  OK: {old[1:-1]}\n'.encode('utf-8'))
    else:
        sys.stdout.buffer.write(f'  MISS: {old[1:-1]}\n'.encode('utf-8'))

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

# Verify
import re as _re
blocks = _re.findall(r'<article[^>]*>.*?</article>', content, _re.S)
sys.stdout.buffer.write(b'\nVerification:\n')
for i, b in enumerate(blocks, 1):
    num  = _re.search(r'cover-num[^>]*>(.*?)<', b)
    ctit = _re.search(r'cover-title[^>]*>(.*?)<', b)
    line = f'  {i}: num={num.group(1) if num else "?"} | {ctit.group(1)[:45] if ctit else "?"}\n'
    sys.stdout.buffer.write(line.encode('utf-8'))

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
