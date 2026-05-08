import re, sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
original = content

# ─── 1. Swap KANKAN (card-cover--09) and AIhub (card-cover--05) ───
blocks = re.findall(r'<article[^>]*project-card[^>]*>.*?</article>', content, re.S)

kankan_block = aihub_block = None
for b in blocks:
    if 'card-cover--09' in b: kankan_block = b
    if 'card-cover--05' in b: aihub_block  = b

if kankan_block and aihub_block:
    # swap: replace first occurrence of each with the other
    content = content.replace(kankan_block, '__KANKAN_PLACEHOLDER__', 1)
    content = content.replace(aihub_block,  '__AIHUB_PLACEHOLDER__',  1)
    content = content.replace('__KANKAN_PLACEHOLDER__', aihub_block)
    content = content.replace('__AIHUB_PLACEHOLDER__',  kankan_block)
    sys.stdout.buffer.write(b'  OK: swapped KANKAN <-> AIhub\n')
else:
    sys.stdout.buffer.write(b'  MISS: could not find both blocks\n')

# ─── 2. Replace all card-cover CSS rules with 3 new groups ────────
# After swap, CSS class → card position:
#   cover01.jpg: --07 --01 --08  (cards 01 04 07)
#   cover02.jpg: --03 --05 --06  (cards 02 05 08)
#   cover03.jpg: --04 --09 --02  (cards 03 06 09)
#
# Text colors:
#   cover01 (blue ~149,172,204):  dark navy
#   cover02 (peach ~218,190,179): dark warm
#   cover03 (dark ~30,44,30):     light

# Find the start of the first design comment/selector after .cover-deco
# Anchor: end of '.cover-deco { display: none; }' line, up to end of last design block

CSS_START = "    .cover-sub  { display: none; }\n    .cover-deco { display: none; }"
CSS_END_MARKER = "\n\n    "  # blank line + indent that begins next section after last block

# Find start index (just after cover-deco line)
start_idx = content.find(CSS_START)
if start_idx == -1:
    sys.stdout.buffer.write(b'  MISS: CSS_START anchor not found\n')
else:
    start_idx += len(CSS_START)

    # Find the last closing brace of the design blocks
    # The last block ends with "    }\n\n" before the TOUCH/MOBILE comment
    end_anchor = '/* ─── TOUCH / MOBILE'
    end_idx = content.find(end_anchor)
    if end_idx == -1:
        sys.stdout.buffer.write(b'  MISS: end anchor not found\n')
    else:
        old_css_section = content[start_idx:end_idx]

        NEW_CSS = """

    /* ── 01cover — cards 01 04 07 ───────────────────────────────── */
    .card-cover--07, .card-cover--01, .card-cover--08 {
      --title-color: rgba(28,42,68,.82);
      --num-color:   rgba(28,42,68,1);
      background: url('cover01.jpg') center/cover no-repeat;
    }

    /* ── 02cover — cards 02 05 08 ───────────────────────────────── */
    .card-cover--03, .card-cover--05, .card-cover--06 {
      --title-color: rgba(68,40,32,.82);
      --num-color:   rgba(68,40,32,1);
      background: url('cover02.jpg') center/cover no-repeat;
    }

    /* ── 03cover — cards 03 06 09 ───────────────────────────────── */
    .card-cover--04, .card-cover--09, .card-cover--02 {
      --title-color: rgba(232,242,228,.90);
      --num-color:   rgba(232,242,228,1);
      background: url('cover03.jpg') center/cover no-repeat;
    }

    """

        content = content[:start_idx] + NEW_CSS + content[end_idx:]
        sys.stdout.buffer.write(b'  OK: CSS cover rules replaced\n')

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

checks = [
    ('card-cover--09' in content[content.find('AI Learning Hub')-500:content.find('AI Learning Hub')+100]
     or 'AI Learning Hub' in content, 'swap check (AIhub present)'),
    ("url('cover01.jpg')" in content, 'cover01.jpg in CSS'),
    ("url('cover02.jpg')" in content, 'cover02.jpg in CSS'),
    ("url('cover03.jpg')" in content, 'cover03.jpg in CSS'),
    ('cover_a.jpg' not in content, 'old cover_a removed'),
    ('cover_c.jpg' not in content, 'old cover_c removed'),
    ('cover_b1.jpg' not in content, 'old cover_b1 removed'),
]
for ok, label in checks:
    sys.stdout.buffer.write(f'  {"OK" if ok else "FAIL"}: {label}\n'.encode())

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
