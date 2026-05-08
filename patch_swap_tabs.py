import re, sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
original = content

# ── 1. Swap Kanelär (--04) ↔ Kaleido (--01) HTML blocks ──────────
blocks = re.findall(r'<article[^>]*>.*?</article>', content, re.S)
kanelar = kaleido = None
for b in blocks:
    if 'card-cover--04' in b: kanelar = b
    if 'card-cover--01' in b: kaleido = b

if kanelar and kaleido:
    content = content.replace(kanelar, '<<<KANELAR>>>', 1)
    content = content.replace(kaleido, '<<<KALEIDO>>>', 1)
    content = content.replace('<<<KANELAR>>>', kaleido)
    content = content.replace('<<<KALEIDO>>>', kanelar)
    sys.stdout.buffer.write(b'  OK: swapped Kanelar <-> Kaleido\n')
else:
    sys.stdout.buffer.write(b'  MISS: swap blocks\n')

# ── 2. Fix cover-num in swapped blocks ───────────────────────────
# Kaleido (--01) now at pos3 → needs num 03 (had 04)
# Kanelär (--04) now at pos4 → needs num 04 (had 03)
def fix_num(html, css_class, old_n, new_n):
    def rep(m):
        body = m.group(0)
        if f'card-cover--{css_class}' in body:
            body = body.replace(f'class="cover-num">{old_n}<',
                                f'class="cover-num">{new_n}<', 1)
        return body
    return re.sub(r'<article[^>]*>.*?</article>', rep, html, flags=re.S)

content = fix_num(content, '01', '04', '03')
content = fix_num(content, '04', '03', '04')
sys.stdout.buffer.write(b'  OK: cover-num 03/04 corrected\n')

# ── 3. Update data-category on all 9 cards ───────────────────────
# After swap the positions are:
#   pos1 --07 SmartHire  card01: featured + enterprise
#   pos2 --03 GameFlow   card02: featured + enterprise
#   pos3 --01 Kaleido    card03: featured + ai-powered
#   pos4 --04 Kanelar    card04: featured
#   pos5 --05 AIHub      card05: featured + ai-powered
#   pos6 --09 KANKAN     card06: ai-powered
#   pos7 --08 KorkortHub card07: ai-powered
#   pos8 --06 SoundClimb card08: (none)
#   pos9 --02 Social VR  card09: (none)
cat_map = {
    '--07': 'featured enterprise',
    '--03': 'featured enterprise',
    '--01': 'featured ai-powered',
    '--04': 'featured',
    '--05': 'featured ai-powered',
    '--09': 'ai-powered',
    '--08': 'ai-powered',
    '--06': '',
    '--02': '',
}

def update_cats(html):
    def rep(m):
        block = m.group(0)
        for css, cat in cat_map.items():
            if f'card-cover{css}' in block:
                block = re.sub(r'data-category="[^"]*"',
                               f'data-category="{cat}"', block, count=1)
                break
        return block
    return re.sub(r'<article[^>]*>.*?</article>', rep, html, flags=re.S)

content = update_cats(content)
sys.stdout.buffer.write(b'  OK: data-category updated\n')

# ── 4. Replace tab HTML (use regex to avoid separator char issues) ─
old_tabs = re.search(
    r'<div class="work-tabs"[^>]*>.*?</div>',
    content, re.S
)
if old_tabs:
    new_tabs = """<div class="work-tabs" role="tablist" aria-label="Project categories">
      <button class="work-tab active" data-tab="featured" role="tab" aria-selected="true">Featured</button>
      <span class="work-tab-sep" aria-hidden="true">&middot;</span>
      <button class="work-tab" data-tab="enterprise" role="tab" aria-selected="false">Enterprise</button>
      <span class="work-tab-sep" aria-hidden="true">&middot;</span>
      <button class="work-tab" data-tab="ai-powered" role="tab" aria-selected="false">AI-Powered</button>
    </div>"""
    content = content[:old_tabs.start()] + new_tabs + content[old_tabs.end():]
    sys.stdout.buffer.write(b'  OK: tab HTML replaced\n')
else:
    sys.stdout.buffer.write(b'  MISS: tab HTML\n')

# ── 5. Update JS filter logic ────────────────────────────────────
js_fixes = [
    # multi-category matching
    (
        "const match = cat === 'all' || card.dataset.category === cat;",
        "const match = card.dataset.category.split(' ').includes(cat);"
    ),
    # moreCard visibility
    (
        "moreCard.classList.toggle('visible', cat === 'design');",
        "moreCard.classList.toggle('visible', cat === 'featured');"
    ),
    # initial tab
    (
        "activateTab('design');",
        "activateTab('featured');"
    ),
]
for old, new in js_fixes:
    if old in content:
        content = content.replace(old, new, 1)
        sys.stdout.buffer.write(f'  OK JS: {old[:50]}\n'.encode())
    else:
        sys.stdout.buffer.write(f'  MISS JS: {old[:50]}\n'.encode())

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

# Verification
sys.stdout.buffer.write(b'\nCard order after patch:\n')
for m in re.finditer(r'<article[^>]*>.*?</article>', content, re.S):
    b = m.group()
    num  = re.search(r'cover-num[^>]*>(.*?)<', b)
    cat  = re.search(r'data-category="([^"]*)"', b)
    proj = re.search(r'project-title[^>]*>(.*?)<', b)
    line = f'  [{num.group(1) if num else "?"}] cat="{cat.group(1) if cat else "?"}" {proj.group(1) if proj else "?"}\n'
    sys.stdout.buffer.write(line.encode('utf-8'))

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
