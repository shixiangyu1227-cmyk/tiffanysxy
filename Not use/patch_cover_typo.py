import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
original = content

# ── 1. Font size +1 step: 2.6rem → 3.0rem ────────────────────────
content = content.replace(
    'font-size: 2.6rem; font-weight: 400; font-style: italic;',
    'font-size: 3.0rem; font-weight: 400; font-style: italic;',
    1
)
sys.stdout.buffer.write(b'  OK: font-size 2.6->3.0rem\n')

# ── 2. Add <br> BEFORE mid-sentence punctuation so next line starts
#    with the punctuation mark (标点符号开始换行).
#    Only taglines that have a comma or period inside the sentence.
line_breaks = [
    # title text in HTML                    →  with <br> before punctuation
    ('class="cover-title">Hire smarter, not harder.<',
     'class="cover-title">Hire smarter<br>, not harder.<'),

    ('class="cover-title">Learn the language, live the life.<',
     'class="cover-title">Learn the language<br>, live the life.<'),

    ('class="cover-title">From idea to image, instantly.<',
     'class="cover-title">From idea to image<br>, instantly.<'),

    ('class="cover-title">Stay sharp. Stay ahead.<',
     'class="cover-title">Stay sharp<br>. Stay ahead.<'),

    ('class="cover-title">Find your city. Design your life.<',
     'class="cover-title">Find your city<br>. Design your life.<'),
]

for old, new in line_breaks:
    if old in content:
        content = content.replace(old, new, 1)
        label = old[20:55]
        sys.stdout.buffer.write(f'  OK: {label}\n'.encode('utf-8'))
    else:
        label = old[20:55]
        sys.stdout.buffer.write(f'  MISS: {label}\n'.encode('utf-8'))

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
