import sys, re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

titles = re.findall(r'<div class="cover-title">(.*?)</div>', content, re.DOTALL)
for i, t in enumerate(titles):
    sys.stdout.buffer.write(f'{i+1}: {repr(t.strip())}\n'.encode('utf-8'))
